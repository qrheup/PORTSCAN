import socket
print("""
      :::::::::       ::::::::       :::::::::   :::::::::::       ::::::::       ::::::::           :::        ::::    :::
     :+:    :+:     :+:    :+:      :+:    :+:      :+:          :+:    :+:     :+:    :+:        :+: :+:      :+:+:   :+:
    +:+    +:+     +:+    +:+      +:+    +:+      +:+          +:+            +:+              +:+   +:+     :+:+:+  +:+
   +#++:++#+      +#+    +:+      +#++:++#:       +#+          +#++:++#++     +#+             +#++:++#++:    +#+ +:+ +#+
  +#+            +#+    +#+      +#+    +#+      +#+                 +#+     +#+             +#+     +#+    +#+  +#+#+#
 #+#            #+#    #+#      #+#    #+#      #+#          #+#    #+#     #+#    #+#      #+#     #+#    #+#   #+#+#
###             ########       ###    ###      ###           ########       ########       ###     ###    ###    ####
\ncredit by BELAYA_VORONA\n\n """)
vibor = int(input("[>]введите выбор 1 или 2\n\n[1]-проверка 1 порта\n\n[2]-проверка нескольких\n\n[>]portscanner:"))

def scan_port(ip,ports):
	try:
		s = socket.socket()
		s.connect((ip,ports))
		print(f"[+] OPEN {ports}")
	except: 
		print(f"[-] BLOCK {ports}")

def for_multi_scan_port(ip,ports):
        try:
                s = socket.socket()
                s.connect((ip,ports))
                print(f"[+] OPEN {ports}")
        except: 
                pass


def multi_scan_port(ip,ports):
	for i in range(0,ports + 1):
		for_multi_scan_port(ip, i)
if __name__ == "__main__":
	if vibor == 1:
		ip = input("[>]введите ip:")
		ports = int(input("[>]введите port:"))
		scan_port(ip, ports)
	elif vibor == 2:
		ip = input("[>]введите ip:")
		ports = int(input("[>]введите ports:"))
		multi_scan_port(ip, ports)
