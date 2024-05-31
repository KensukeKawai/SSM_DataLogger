import send
import param

DATA_OFFSET = 4     # 0x80,0xF0,0x10,Byte-num,Command,-1

def checksum(receive_data):
    checksum_hex_str = hex(sum(receive_data[:-1]))[-2:]    # ヘッダー～Dataまで合算→16進数変換→下位2Byteを抽出
    checksum_dec_int = int(checksum_hex_str,16)       # 組み込み関数intでstrをintに変換(hex関数で10→16進数変換するとint→strに型変換されてしまうため、再度intにするため10進数に戻す)

    # CheckSum Judgement
    if checksum_dec_int == receive_data[-1]:
        r_checksum = 1
    else:
        r_checksum = 0
    
    return r_checksum

def check_header(receive_header):
    if receive_header == param.HEADER_C2T:
        check = 1
    else:
        check = 0
    
    return check

def receive_measuring(setparam_num):
    # receive_str = serial.read
    measurement_data = []
    # Ex.Engine Speed
    # receive_str = [0x80,0xF0,0x10,0x03,0xE8,0xFD,0x0A,0x72]
    # Ex.MAP,AP,MRP,EL,TOA,IAT,ROS,ES
    receive_str = [0x80,0xF0,0x10,0x0B,0xE8,0x21,0x64,0x3D,0x33,0x04,0x70,0x9D,0x00,0xFC,0x0A,0x7F]

    checksum_result = checksum(receive_str)
    header_result = check_header(receive_str[:3])
    
    print("checksum:{}, header:{}".format(checksum_result,header_result))
    
    if checksum_result == 1 & header_result == 1:
        receive_successful = 1
        data_offset_pre = 1                   # initialize of offset bytes of data
        
        for i in range(len(setparam_num)):  # Numbers of Measuring Param
            param_column = setparam_num[i]
            
            # Check to Numbers of Bytes,offset
            data_offset = int(DATA_OFFSET + data_offset_pre)
            data_bytes = int(len(param.param_list[param_column][param.ADDRESS])/3)
            
            if data_bytes == 1:
                receive_data = receive_str[data_offset]
            else:
                receive_data = (receive_str[data_offset+1]<<8) + receive_str[data_offset]
            
            data_offset_pre += data_bytes
            cal_data = receive_data
            for j in range(param.SYM1,param.SYM4+1,2):          # sym1→sym2→sym3→sym4
                if param.param_list[param_column][j] == 'mul':
                    cal_data *= param.param_list[param_column][j+1]
                elif param.param_list[param_column][j] == 'div':
                    cal_data /= param.param_list[param_column][j+1]
                elif param.param_list[param_column][j] == 'sub':
                    cal_data -= param.param_list[param_column][j+1]
                elif param.param_list[param_column][j] == 'add':
                    cal_data += param.param_list[param_column][j+1]
                elif param.param_list[param_column][j] == '-':
                    break
            measurement_data.append(cal_data)
            
            print("{}:{} [{}]".format(param.param_list[param_column][param.NAME],measurement_data[i],param.param_list[param_column][param.UNIT]))
    else:
        receive_successful = 0
    
    return receive_successful,measurement_data