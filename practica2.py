import os

hostname = "200.33.171.0"
os.system("nmap -sP " + f"{hostname}/24")

"""
Starting Nmap 7.80 ( https://nmap.org ) at 2020-02-27 11:40 CST
Nmap scan report for mail.itmorelia.edu.mx (200.33.171.3)
Host is up (0.00081s latency).
Nmap scan report for delfin2.itmorelia.edu.mx (200.33.171.11)
Host is up (0.00077s latency).
Nmap scan report for 200.33.171.13
Host is up (0.00056s latency).
Nmap scan report for dsc.itmorelia.edu.mx (200.33.171.20)
Host is up (0.016s latency).
Nmap scan report for libra.itmorelia.edu.mx (200.33.171.54)
Host is up (0.00063s latency).
Nmap scan report for 200.33.171.85
Host is up (0.00084s latency).
Nmap scan report for 200.33.171.86
Host is up (0.012s latency).
Nmap scan report for 200.33.171.127
Host is up (0.00069s latency).
Nmap done: 256 IP addresses (8 hosts up) scanned in 9.73 seconds
"""
