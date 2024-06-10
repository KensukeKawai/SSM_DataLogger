import serial
import param
import struct
from copy import copy

class send():
    def __init__(self):
        self.UART_TIMEOUT = 0.05 #[s]
        self.send_num = 0
        self.receive_num = 0
        self.address_num = 0
        
        # Serial Instantiate
        # self.ser = serial.Serial(port="COM17", baudrate=4800, bytesize=8, timeout=self.self.ser_TIMEOUT, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)
        self.ser = serial.Serial(port="COM14", baudrate=4800, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)

    def send_communication_test(self):
        send_data = [0x80,0x10,0xF0,0x05,0xA8,0x00,0x00,0x00,0x61,0x8E]
        # struct.packでバイナリ変数生成
        fmt = str(len(send_data)) + "B" # struct.packのByte数を計算
        send_bytes = struct.pack(fmt,*send_data)   # バイナリ送信するためstruct.packで結合。引数データはint型である必要がある。
        self.ser.write(send_bytes)

    def send_measuring(self,selected_index):
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

        # Calculate expected bytes received
        self.receive_num = 3 + 1 + 1 + round(self.address_num/3) + 1
        
        # Add Command and PP
        send_data.extend([param.command_t2c.READ_SINGLE_ADDRESS, 0x00])

        # Add Param Address
        for i in range(selected_num):
            param_address = param.param_list[selected_index[i]][1]
            send_data.extend(param_address)

        # CheckSum
        checksum_hex_str = hex(sum(send_data))[-2:]    # ヘッダー～Dataまで合算→16進数変換→下位2Byteを抽出
        checksum_dec_int = int(checksum_hex_str,16)       # 組み込み関数intでstrをintに変換(hex関数で10→16進数変換するとint→strに型変換されてしまうため、再度intにするため10進数に戻す)
        send_data.append(checksum_dec_int)
        self.send_num = len(send_data)

        # struct.packでバイナリ変数生成
        fmt = str(len(send_data)) + "B" # struct.packのByte数を計算
        send_bytes = struct.pack(fmt,*send_data)   # バイナリ送信するためstruct.packで結合。引数データはint型である必要がある。
        self.ser.write(send_bytes)



# UART_TIMEOUT = 0.05 # [s]

# # Serial Initialize. SSM Setting.
# # uart = serial.Serial(port="COM17", baudrate=4800, bytesize=8, timeout=UART_TIMEOUT, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)
# uart = serial.Serial(port="COM14", baudrate=4800, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)

# global .send_num,.receive_num

# def send_measuring(selected_index):
#     global .send_num, .receive_num
#     address_num = 0

#     # send_dataは固定。extend,appendで結合させていく。
#     # send_data = param.HEADER_T2Cにすると同値になり、異なる変数宣言も同じアドレスが割り当てられてしまうため
#     # copyメソッドで明示的に別のオブジェクトを作成
#     send_data = copy(param.HEADER_T2C)   
    
#     param_count = len(selected_index)
    
#     # Byte Count Calculation. Add 2 Bytes(Command+PP) to All Address Bytes.
#     for i in range(param_count):
#         address_num += len(param.param_list[selected_index[i]][param.ADDRESS]) 
#     bytes_num = 2 + address_num
#     send_data.append(bytes_num)

#     # Calculate expected bytes received
#     .receive_num = 3 + 1 + 1 + round(address_num/3) + 1
    
#     # Add Command and PP
#     send_data.extend([param.command_t2c.READ_SINGLE_ADDRESS, 0x00])

#     # Add Param Address
#     for i in range(param_count):
#         param_address = param.param_list[selected_index[i]][1]
#         send_data.extend(param_address)

#     # CheckSum
#     checksum_hex_str = hex(sum(send_data))[-2:]    # ヘッダー～Dataまで合算→16進数変換→下位2Byteを抽出
#     checksum_dec_int = int(checksum_hex_str,16)       # 組み込み関数intでstrをintに変換(hex関数で10→16進数変換するとint→strに型変換されてしまうため、再度intにするため10進数に戻す)
#     send_data.append(checksum_dec_int)
#     .send_num = len(send_data)

#     # struct.packでバイナリ変数生成
#     fmt = str(len(send_data)) + "B" # struct.packのByte数を計算
#     send_str = struct.pack(fmt,*send_data)   # バイナリ送信するためstruct.packで結合。引数データはint型である必要がある。
#     uart.write(send_str)


# def send_communication_test():
#     send_data = [0x80,0x10,0xF0,0x05,0xA8,0x00,0x00,0x00,0x61,0x8E]
#     # struct.packでバイナリ変数生成
#     fmt = str(len(send_data)) + "B" # struct.packのByte数を計算
#     send_str = struct.pack(fmt,*send_data)   # バイナリ送信するためstruct.packで結合。引数データはint型である必要がある。
#     uart.write(send_str)