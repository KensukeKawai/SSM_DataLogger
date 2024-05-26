import serial
import time
import struct
import numpy as np

def view_list_ports():
    # List of Ports
    import serial.tools.list_ports

    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)
        print(" device       :", p.device)
        print(" name         :", p.name)
        print(" description  :", p.description)
        print(" hwid         :", p.hwid)
        print(" vid          :", p.vid)
        print(" pid          :", p.pid)
        print(" serial_number:", p.serial_number)
        print(" location     :", p.location)
        print(" manufactuer  :", p.manufacturer)
        print(" product      :", p.product)
        print(" interface    :", p.interface)
        print("")

# Serial Initialize
uart = serial.Serial(port="COM14", baudrate=4800, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)

def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()

CMD_START = 0x80
CMD_TOOL = 0xF0
CMD_ECU = 0x10
HEADER_TOLL_TO_ECU = [CMD_START,CMD_ECU,CMD_TOOL]
HEADER_ECU_TO_TOOL = [CMD_START,CMD_TOOL,CMD_ECU]
send_data = HEADER_TOLL_TO_ECU

test_response_send = [0x05,0xA8,0x00,0x00,0x00,0x61]

set_data = test_response_send
send_data.extend(set_data)

checksum_hex_str = hex(sum(send_data))[-2:]    # ヘッダー～Dataまで合算→16進数変換→下位2Byteを抽出
checksum_dec_int = int(checksum_hex_str,16)       # 組み込み関数intでstrをintに変換(hex関数で10→16進数変換するとint→strに型変換されてしまうため、再度intにするため10進数に戻す)
print(checksum_hex_str)
send_data.append(checksum_dec_int)

fmt = str(len(send_data)) + "B" # struct.packのByte数を計算

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

set_str = struct.pack(fmt,*send_data)   # 引数データはint型である必要がある
print(set_str)

# view_list_ports()

while True:
    # serialstr_read = serial.read
    uart.write(set_str)
    time.sleep(1)

    try:
        print(set_str)

    except:
        pass