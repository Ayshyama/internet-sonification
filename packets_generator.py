from scapy.all import *
import time

from scapy.layers.inet import TCP, IP
from scapy.layers.l2 import Ether

# Apple Mobile Device Ethernet #2
print('MAX/MSP Host IP: ')
Host_IP = input()
print('Host IP is: ' + Host_IP)

print('Choose an available interface: ')
show_interfaces()
iFace = input()


def send_packets():
    flags = ['A', 'S', 'SA', 'PA', 'R', 'FA']

    while True:
        size1 = random.randint(1, 500)
        size2 = random.randint(500, 1000)
        size3 = random.randint(1, 2000)

        flag1 = random.choice(flags)
        flag2 = random.choice(flags)
        flag3 = random.choice(flags)

        # Create packets with random sizes and flags
        packet1 = Ether() / IP(src="172.20.10.2", dst="159.124.13.192") / TCP(sport=58874, dport=443,
                                                                              flags=flag1) / Raw(b"X" * size1)
        packet2 = Ether() / IP(src="159.124.13.192", dst="172.20.10.2") / TCP(sport=443, dport=58874,
                                                                              flags=flag2) / Raw(b"Y" * size2)
        packet3 = Ether() / IP(src="159.124.13.192", dst="172.20.10.2") / TCP(sport=443, dport=58874,
                                                                              flags=flag3) / Raw(b"Z" * size3)

        delay1 = random.uniform(0.1, 0.4)

        sendp(packet1, iface=iFace)
        print(packet1)
        print(f'size: {size1}')

        sendp(packet2, iface=iFace)
        print(packet2)
        print(f'size: {size2}')

        sendp(packet3, iface=iFace)
        print(packet3)
        print(f'size: {size3}')

        time.sleep(delay1)


send_packets()
