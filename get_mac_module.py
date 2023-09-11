import scapy.all as scapy

def get_mac(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcastingt_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcastingt_packet / arp_packet
    # print(combined_packet.summary())
    
    answered = scapy.srp(combined_packet, timeout=2, verbose=False)[0]
    if answered:
        for (sent, received) in answered:
            return received.hwsrc
    else:
        return None

    
    

    

get_mac("192.168.162.26")