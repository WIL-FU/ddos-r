#ddos-r version 1.0.0
import os
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
def syn_flood(ip, port):
    print("wehbruguiweryughiwer")
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
    outputAsListItem("", s)
    outputAsListItem("IP ADDRESS: ", s)
    outputAsListItem("PORT: ", s)
    closeList(s)
#program begin
attack_setup(attack_type())