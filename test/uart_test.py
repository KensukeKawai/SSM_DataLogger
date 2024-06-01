import serial
import time
import struct
import numpy as np
import view_list_ports as vlp
import param

# Serial Initialize. SSM Setting.
uart = serial.Serial(port="COM14", baudrate=4800, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)

def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()

send_data = param.HEADER_TOLL_TO_ECU          # send_dataは固定。extend,appendで結合させていく。

set_data = param.TEST_RESPONSE
send_data.extend(set_data)

# CheckSum
checksum_hex_str = hex(sum(send_data))[-2:]    # ヘッダー～Dataまで合算→16進数変換→下位2Byteを抽出
checksum_dec_int = int(checksum_hex_str,16)       # 組み込み関数intでstrをintに変換(hex関数で10→16進数変換するとint→strに型変換されてしまうため、再度intにするため10進数に戻す)
send_data.append(checksum_dec_int)

# struct.packでバイナリ変数生成
fmt = str(len(send_data)) + "B" # struct.packのByte数を計算
set_str = struct.pack(fmt,*send_data)   # バイナリ送信するためstruct.packで結合。引数データはint型である必要がある。

print(checksum_hex_str)
print(set_str)

# a = [1]
# a.extend([2,3])
# [1,2,3]
# 配列の末尾にextendで配列を結合すると、入れ子にならない
# 配列をappendで結合すると、入れ子になる([1,[2,3]])

# a.append(数値)
# [1,2]
# listに数値単体をappendで結合する場合は、末尾に数値が結合

# struct.pack("B",128)
# "Byte数。1Byteなら"B"、2Byteなら"2B""
# 10進数を入れると、16進数に変換して送信
# 0x**を入れると、**を16進数として送信

vlp.view_list_ports()

while True:
    # serialstr_read = serial.read
    uart.write(set_str)
    time.sleep(1)

    try:
        print(set_str)

    except:
        pass