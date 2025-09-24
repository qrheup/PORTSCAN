import socket
from scapy.all import *
print("""
      :::::::::       ::::::::       :::::::::   :::::::::::       ::::::::       ::::::::           :::        ::::    :::
     :+:    :+:     :+:    :+:      :+:    :+:      :+:          :+:    :+:     :+:    :+:        :+: :+:      :+:+:   :+:
    +:+    +:+     +:+    +:+      +:+    +:+      +:+          +:+            +:+              +:+   +:+     :+:+:+  +:+
   +#++:++#+      +#+    +:+      +#++:++#:       +#+          +#++:++#++     +#+             +#++:++#++:    +#+ +:+ +#+
  +#+            +#+    +#+      +#+    +#+      +#+                 +#+     +#+             +#+     +#+    +#+  +#+#+#
 #+#            #+#    #+#      #+#    #+#      #+#          #+#    #+#     #+#    #+#      #+#     #+#    #+#   #+#+#
###             ########       ###    ###      ###           ########       ########       ###     ###    ###    ####
\ncredit by BELAYA_VORONA\n\n """)
vibor = int(input("[>]введите выбор 1 или 2\n\n[1]-SYN scan\n\n[2]-FULL TCP CONNECT SCAN\n\n[>]portscanner:"))


def SYN_check_port(ip,port):
        rep = sr1(IP(dst=ip)/TCP(dport=port , flags="S"),timeout=2, verbose=0)

        if not rep:
                print(f"[-]Port:{port} filtred/host down")
                return
        if rep.haslayer(TCP):
                tcp = rep.getlayer(TCP)

                if tcp.flags == 0x12:
                        print(f"[+]port:{port} OPEN")
                        send(IP(dst=ip) / TCP(dport=port , flags="R"), verbose=0)

                #elif tcp.flags == 0x14:
                        #print(f"[-]port:{port} CLOSED")
        else:
                print(f"Port:{port}UNKNOWN")

def scan_port(ip,port):
	try:
		s = socket.socket()
		s.connect((ip,port))
		print(f"[+] OPEN {port}")
	except:
		pass


if __name__ == "__main__":
	if vibor == 1:
		ip = input("[>]введите ip:")
		for port in range(65536):
			SYN_check_port(ip,port)
	elif vibor == 2:
		ip = input("[>]введите ip:")
		for port in range(65536):
                        scan_port(ip,port)
