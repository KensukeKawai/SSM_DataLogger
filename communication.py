
# Standard Library
import serial
import struct
from copy import copy
import time
# Local Module
import param
import globalval as g

class send:
    def __init__(self, selected_port):
        # Const
        self.UART_TIMEOUT = 1 #[s]       短くしすぎると車両からのレスポンスを待ちきれずタイムアウトする、注意
        self.TEST_SENDDATA = [0x80,0x10,0xF0,0x05,0xA8,0x00,0x00,0x00,0x61,0x8E]
        self.TEST_SENDBYTES = len(self.TEST_SENDDATA)
        # Variable
        self.send_num = 0
        self.address_num = 0
        
        # Serial Instantiate
        self.ser = serial.Serial(port=selected_port, baudrate=4800, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE, timeout=self.UART_TIMEOUT)

    def send_communication_test(self):
        # send_data = self.TEST_SENDDATA
        # Set Binary for struct.pack
        fmt = str(len(self.TEST_SENDDATA)) + "B"             # Calculate number of bytes for struct.pack
        send_hex = struct.pack(fmt,*self.TEST_SENDDATA)      # バイナリ送信するためstruct.packで結合。引数データはint型である必要がある。
        self.ser.write(send_hex)
        
        return None

    def send_measuring(self, selected_index):
        self.address_num = 0

        # send_dataは固定。extend,appendで結合させていく。
        # send_data = param.HEADER_T2Cにすると同値になり、異なる変数宣言も同じアドレスが割り当てられてしまうため
        # copyメソッドで明示的に別のオブジェクトを作成
        send_data = copy(param.HEADER_T2C)   
        selected_num = len(selected_index)
        
        # Byte Count Calculation. Add 2 Bytes(Command+PP) to All Address Bytes.
        for i in range(selected_num):
            self.address_num += len(param.param_list[selected_index[i]][param.ADDRESS]) 
        bytes_num = 2 + self.address_num
        send_data.append(bytes_num)
        
        # Add Command and PP
        send_data.extend([param.command_t2c.READ_SINGLE_ADDRESS, 0x00])

        # Add Param Address
        for i in range(selected_num):
            param_address = param.param_list[selected_index[i]][1]
            send_data.extend(param_address)

        # CheckSum
        checksum_hex_hex = hex(sum(send_data))[-2:]         # ヘッダー～Dataまで合算→16進数変換→下位2Byteを抽出
        checksum_dec_int = int(checksum_hex_hex,16)         # 組み込み関数intでstrをintに変換(hex関数で10→16進数変換するとint→strに型変換されてしまうため、再度intにするため10進数に戻す)
        send_data.append(checksum_dec_int)
        self.send_num = len(send_data)

        # Set Binary for struct.pack
        fmt = str(len(send_data)) + "B"             # Calculate number of bytes for struct.pack
        send_hex = struct.pack(fmt,*send_data)      # バイナリ送信するためstruct.packで結合。引数データはint型である必要がある。
        self.ser.write(send_hex)
        
        return None


# Communication test関数を追加する
class receive:
    def __init__(self, selected_index):
        # Const
        self.TEST_RECDATA = [0x80,0xF0,0x10,0x02,0xE8,0x08,0x72]
        self.TEST_RECBYTES = len(self.TEST_RECDATA)
        self.TEST_FAILURE = 0
        self.TEST_SUCCESS = 1
        self.TEST_TIMEOUT = 2
        self.DATA_OFFSET = 4     # 0x80,0xF0,0x10,Byte-num,Command,-1
        self.VALUE_NDIGITS = 3
        self.REC_ERRCNT = 10
        self.STS_SUCCESS = 1
        self.STS_CHKSUMERR = 2
        self.STS_HEADERERR = 3
        self.STS_ERROR = 4
        # Variable
        self.refresh_time = 0
        self.measure_time = 0
        self.receive_sts = self.STS_SUCCESS
        self.error_count = 0
        self.start_time = time.time()
        self.receive_datalist = []
        self.timeseries_data = [['Time']]
        [self.timeseries_data.append([param.param_list[selected_index[i]][0]]) for i in range(len(selected_index))]

    def rec_communication_test(self, snd):
        # Calculate expected bytes received
        read_bytes = snd.TEST_SENDBYTES + self.TEST_RECBYTES
        
        # Receive process
        receive_hex_allbytes = snd.ser.read(read_bytes)
        receive_hex_alllist = list(receive_hex_allbytes)
        receive_hex = receive_hex_alllist[snd.TEST_SENDBYTES:]
        
        # Timeout
        if receive_hex_alllist == []:
            print('Receive Error：Timeout...Please Check COM Port')
            # test_result = self.TEST_TIMEOUT
        # Receive Complete
        else:
            if receive_hex == self.TEST_RECDATA:
                print('TEST Successful')
                # test_result = self.TEST_SUCCESS
            else:
                print('Receive Error：Different Data')
                # test_result = self.TEST_FAILURE
        
        return g.PORTSELECT_MODE #, test_result

    def rec_chksum_header(self):
        checksum_hex_hex = hex(sum(self.receive_hex[:-1]))[-2:]    # ヘッダー～Dataまで合算→16進数変換→下位2Byteを抽出
        checksum_dec_int = int(checksum_hex_hex,16)       # 組み込み関数intでstrをintに変換(hex関数で10→16進数変換するとint→strに型変換されてしまうため、再度intにするため10進数に戻す)

        # Judgement
        self.checksum_result = 1 if checksum_dec_int == self.receive_hex[-1] else 0
        self.header_result = 1 if self.receive_hex[:3] == param.HEADER_C2T else 0
        
        return None

    def receive_measuring(self, selected_index, snd):
        self.receive_datalist = []

        # Calculate expected bytes received
        receive_num = 3 + 1 + 1 + round(snd.address_num/3) + 1  # Header(3)+ByteNum(1)+Command(1)+Data+ChkSum(1)
        read_bytes = snd.send_num + receive_num
        
        # Receive process
        if g.debug_mode == 0:
            receive_hex_allbytes = snd.ser.read(read_bytes)
            receive_hex_alllist = list(receive_hex_allbytes)
            self.receive_hex = receive_hex_alllist[snd.send_num:]
        
        else:
            self.receive_hex = [0x80,0xF0,0x10,0x0B,0xE8,0x33,0x21,0xFC,0x0A,0x70,0x04,0x9D,0x00,0x64,0x3D,0x7F]        # No.0,6,7,10,12,14,23,24

        self.rec_chksum_header()        # Check CheckSum and Header
        
        if self.checksum_result == 1 & self.header_result == 1:
            self.receive_sts = self.STS_SUCCESS
            self.error_count = 0
            data_offset_pre = 1                   # initialize of offset bytes of data
            
            for i in range(len(selected_index)):  # Numbers of Measuring Param
                param_column = selected_index[i]
                
                # Check to Numbers of Bytes,offset
                data_offset = int(self.DATA_OFFSET + data_offset_pre)
                data_bytes = int(len(param.param_list[param_column][param.ADDRESS])/3)
                
                if data_bytes == 1:
                    receive_data = self.receive_hex[data_offset]
                else:
                    receive_data = (self.receive_hex[data_offset+1]<<8) + self.receive_hex[data_offset]
                
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
                
                # Time Series Data Processing
                self.timeseries_data[i+1].append(round(cal_data,ndigits=self.VALUE_NDIGITS))
            
            # Calculate refresh time
            end_time = time.time()
            self.refresh_time = round((end_time-self.start_time)*1000)
            self.start_time = time.time()
            self.measure_time += self.refresh_time
            self.timeseries_data[0].append(self.measure_time/1000)
                
        elif self.checksum_result == 0:
            print('Checksum Error!!!')
            self.error_count += 1
            if self.error_count >= self.REC_ERRCNT:
                self.receive_sts = self.STS_ERROR
            else:
                self.receive_sts = self.STS_CHKSUMERR
                
        # elif self.header_result==0:
        #     print('Header Error!!!')
        #     self.receive_success = 0
        #     self.error_count += 1
        
        return None