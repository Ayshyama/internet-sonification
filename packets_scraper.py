from scapy.all import *
from pythonosc.udp_client import SimpleUDPClient
from scapy.layers.inet import TCP


# Apple Mobile Device Ethernet #2
print('MAX/MSP Host IP: ')
Host_IP = input()
print('Host IP is: ' + Host_IP)

print('Choose an available interface: ')
show_interfaces()
iFace = input()


def analyze_packet(pkt):
    if TCP in pkt:
        p_length = str(len(pkt))

        if pkt[TCP].flags == 'A':
            client = SimpleUDPClient(Host_IP, 1120)
            client.send_message('A', p_length)

        if pkt[TCP].flags == 'S':
            client = SimpleUDPClient(Host_IP, 1121)
            client.send_message('S', p_length)

        if pkt[TCP].flags == 'SA':
            client = SimpleUDPClient(Host_IP, 1122)
            client.send_message('SA', p_length)

        if pkt[TCP].flags == 'PA':
            client = SimpleUDPClient(Host_IP, 1123)
            client.send_message('PA', p_length)

        if pkt[TCP].flags == 'R':
            client = SimpleUDPClient(Host_IP, 1124)
            client.send_message('R', p_length)

        if pkt[TCP].flags == 'FA':
            client = SimpleUDPClient(Host_IP, 1125)
            client.send_message('FA', p_length)

    return pkt.summary()



# a = sniff(prn=analyze_packet, iface=iFace, filter='tcp')


filter_str = f"tcp and host 140.82.121.4 and port 443"
a = sniff(prn=analyze_packet, iface=iFace, filter=filter_str)
