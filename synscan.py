import socket
from struct import *
import binascii
import sys

src_ip = sys.argv[1]
dst_ip = sys.argv[2]
dst_port = sys.argv[3]

def gen_packet():
    # IP header
    version = 0x4
    ihl = 0x5
    type_of_service = 0x0
    total_length = 0x20
    identification = 0xabcd
    flags = 0x0
    fragment_offset = 0x0
    ttl = 0x40
    protocol = 0x6
    header_checksum = 0x0
    src_addr = socket.inet_aton(src_ip)
    dst_addr = socket.inet_aton(dst_ip)
    v_ihl = (version << 4) + ihl
    f_fo = (flags << 13) + fragment_offset

    # TCP header
    src_port = 0x3039
    seq_no = 0x0
    ack_no = 0x0
    data_offset = 0x5
    reserved = 0x0
    ns = 0x0
    cwr = 0x0
    ece = 0x0
    urg = 0x0
    ack = 0x0
    psh = 0x0
    rst = 0x0
    syn = 0x1
    fin = 0x0
    window_size = 0x7110
    checksum = 0x0
    urg_pointer = 0x0
    data_offset_res_flags = (data_offset << 12)
    data_offset_res_flags += (reserved << 9)
    data_offset_res_flags += (ns << 8)
    data_offset_res_flags += (cwr << 7)
    data_offset_res_flags += (ece << 6)
    data_offset_res_flags += (urg << 5)
    data_offset_res_flags += (ack << 4)
    data_offset_res_flags += (psh << 3)
    data_offset_res_flags += (rst << 2)
    data_offset_res_flags += (syn << 1)
    data_offset_res_flags += fin

    tcp_header = b""
    ip_header = b""
    packet = b""


    return

def send_packet():

    return


def main():

    return



main()
