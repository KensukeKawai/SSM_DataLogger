
import serial
import param
import send
import struct
import sys

# Communication test関数を追加する

class receive:
    def __init__(self):
        self.DATA_OFFSET = 4     # 0x80,0xF0,0x10,Byte-num,Command,-1
        self.receive_datalist = []

    def rec_chksum_header(self,receive_data):
        checksum_hex_str = hex(sum(receive_data[:-1]))[-2:]    # ヘッダー～Dataまで合算→16進数変換→下位2Byteを抽出
        checksum_dec_int = int(checksum_hex_str,16)       # 組み込み関数intでstrをintに変換(hex関数で10→16進数変換するとint→strに型変換されてしまうため、再度intにするため10進数に戻す)

        # Judgement
        self.checksum_result = 1 if checksum_dec_int == receive_data[-1] else 0
        self.header_result = 1 if receive_data[:3] == param.HEADER_C2T else 0

    def receive_measuring(self,selected_index):
        self.receive_datalist = []
        # receive_str = []

        # read_bytes = send.send_num + send.receive_num
        
        # # Receive process
        # receive_str_all_bytes = send.uart.read(read_bytes)
        # receive_str_all = list(receive_str_all_bytes)
        # receive_str_slice = receive_str_all[send.send_num:]
        # receive_str = receive_str_slice
        
        # Ex.MAP,AP,MRP,EL,TOA,IAT,ROS,ES
        receive_str = [0x80,0xF0,0x10,0x0B,0xE8,0x33,0x21,0xFC,0x0A,0x70,0x04,0x9D,0x00,0x64,0x3D,0x7F]

        self.rec_chksum_header(receive_str)
        print(self.checksum_result)
        print(self.header_result)
        
        if self.checksum_result == 1 & self.header_result == 1:
            receive_success = 1
            data_offset_pre = 1                   # initialize of offset bytes of data
            
            for i in range(len(selected_index)):  # Numbers of Measuring Param
                param_column = selected_index[i]
                
                # Check to Numbers of Bytes,offset
                data_offset = int(self.DATA_OFFSET + data_offset_pre)
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
                self.receive_datalist.append(cal_data)
                
        else:
            if self.checksum_result==0: print('Checksum Error!!!')
            if self.header_result==0: print('Header Error!!!')
            receive_success = 0
        
        return receive_success, self.receive_datalist


# def checksum(receive_data):
#     checksum_hex_str = hex(sum(receive_data[:-1]))[-2:]    # ヘッダー～Dataまで合算→16進数変換→下位2Byteを抽出
#     checksum_dec_int = int(checksum_hex_str,16)       # 組み込み関数intでstrをintに変換(hex関数で10→16進数変換するとint→strに型変換されてしまうため、再度intにするため10進数に戻す)

#     # CheckSum Judgement
#     if checksum_dec_int == receive_data[-1]:
#         r_checksum = 1
#     else:
#         r_checksum = 0
    
#     return r_checksum

# def check_header(receive_header):
#     if receive_header == param.HEADER_C2T:
#         check = 1
#     else:
#         check = 0
    
#     return check

# def receive_measuring(selected_index):
#     DATA_OFFSET = 4     # 0x80,0xF0,0x10,Byte-num,Command,-1
#     receive_data = []
#     receive_str = []

#     num = send.send_num + send.receive_num
    
#     # Receive process
#     receive_str_all_bytes = send.uart.read(num)
#     receive_str_all = list(receive_str_all_bytes)
#     receive_str_slice = receive_str_all[send.send_num:]
#     receive_str = receive_str_slice
    
#     print(num)
#     print(receive_str_all_bytes)
#     print(receive_str_all)
#     print(len(receive_str_all))
#     print(receive_str_slice)
#     print(type(receive_str_slice))

#     # Ex.Engine Speed
#     # receive_str = [0x80,0xF0,0x10,0x03,0xE8,0xFD,0x0A,0x72]
#     # Ex.MAP,AP,MRP,EL,TOA,IAT,ROS,ES
#     # receive_str = [0x80,0xF0,0x10,0x0B,0xE8,0x21,0x64,0x3D,0x33,0x04,0x70,0x9D,0x00,0xFC,0x0A,0x7F]
#     # receive_str = [0x80,0xF0,0x10,0x0B,0xE8,0x33,0x21,0xFC,0x0A,0x70,0x04,0x9D,0x00,0x64,0x3D,0x7F]

#     checksum_result = checksum(receive_str)
#     header_result = check_header(receive_str[:3])
    
#     if checksum_result == 1 & header_result == 1:
#         receive_success = 1
#         data_offset_pre = 1                   # initialize of offset bytes of data
        
#         for i in range(len(selected_index)):  # Numbers of Measuring Param
#             param_column = selected_index[i]
            
#             # Check to Numbers of Bytes,offset
#             data_offset = int(DATA_OFFSET + data_offset_pre)
#             data_bytes = int(len(param.param_list[param_column][param.ADDRESS])/3)
            
#             if data_bytes == 1:
#                 receive_data = receive_str[data_offset]
#             else:
#                 receive_data = (receive_str[data_offset+1]<<8) + receive_str[data_offset]
            
#             data_offset_pre += data_bytes
#             cal_data = receive_data
#             for j in range(param.SYM1,param.SYM4+1,2):          # sym1→sym2→sym3→sym4
#                 if param.param_list[param_column][j] == 'mul':
#                     cal_data *= param.param_list[param_column][j+1]
#                 elif param.param_list[param_column][j] == 'div':
#                     cal_data /= param.param_list[param_column][j+1]
#                 elif param.param_list[param_column][j] == 'sub':
#                     cal_data -= param.param_list[param_column][j+1]
#                 elif param.param_list[param_column][j] == 'add':
#                     cal_data += param.param_list[param_column][j+1]
#                 elif param.param_list[param_column][j] == '-':
#                     break
#             receive_data.append(cal_data)
            
#     else:
#         if checksum_result==0: print('Checksum Error!!!')
#         if header_result==0: print('Header Error!!!')
#         receive_success = 0
    
#     return receive_success,receive_data