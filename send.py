import serial
import param
import struct
from copy import copy

# Serial Initialize. SSM Setting.
uart = serial.Serial(port="COM14", baudrate=4800, bytesize=8, timeout=0.004, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)

def send_measuring(setparam_num):

    # send_dataは固定。extend,appendで結合させていく。
    # send_data = param.HEADER_T2Cにすると同値になり、異なる変数宣言も同じアドレスが割り当てられてしまうため
    # copyメソッドで明示的に別のオブジェクトを作成
    send_data = copy(param.HEADER_T2C)   
    
    param_count = len(setparam_num)
    
    # Byte Count Calculation. Add 2 Bytes(Command+PP) to All Address Bytes.
    bytes_num = param_count * 3 + 2
    send_data.append(bytes_num)
    
    # Add Command and PP
    send_data.extend([param.command_t2c.READ_SINGLE_ADDRESS, 0x00])

    # Add Param Address
    for i in range(param_count):
        param_address = param.param_list[setparam_num[i]][1]
        send_data.extend(param_address)

    # CheckSum
    checksum_hex_str = hex(sum(send_data))[-2:]    # ヘッダー～Dataまで合算→16進数変換→下位2Byteを抽出
    checksum_dec_int = int(checksum_hex_str,16)       # 組み込み関数intでstrをintに変換(hex関数で10→16進数変換するとint→strに型変換されてしまうため、再度intにするため10進数に戻す)
    send_data.append(checksum_dec_int)

    # struct.packでバイナリ変数生成
    fmt = str(len(send_data)) + "B" # struct.packのByte数を計算
    send_str = struct.pack(fmt,*send_data)   # バイナリ送信するためstruct.packで結合。引数データはint型である必要がある。
    uart.write(send_str)
    
    # print(send_data)
    # print(send_str)
    

def send_communication_test():
    send_data = [0x80,0x10,0xF0,0x05,0xA8,0x00,0x00,0x00,0x61,0x8E]
    # struct.packでバイナリ変数生成
    fmt = str(len(send_data)) + "B" # struct.packのByte数を計算
    send_str = struct.pack(fmt,*send_data)   # バイナリ送信するためstruct.packで結合。引数データはint型である必要がある。
    uart.write(send_str)
    
    # print(send_str)