import sys

try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")
import time
i=1
n=int(input("how any times of you want:"))
color.write("Hi, MOM \n","KEYWORD")
color.write("Hi, DAD \n","COMMENT")
while i<=n:
    print("                                    ð¸")
    color.write("         ðHappy anniversary to both of you my parents!ð","COMMENT")
    print("") 
    color.write("                    ð¸","STRING")
    print("         ð¸")
    color.write("                               ð¸","STRING")
    time.sleep(0.4)
    print("ð¸") 
    print("                                 ")
    print("                                                 ð¸")
    print("")
    print("                         ð¸")
    time.sleep(0.4)
    print("             ð¸")
    color.write("                                    ð¸","STRING")
    print("ð¸")
    color.write("ð¥³ð¤©ðði love youâ¤ð¥³ð¤©ðð")
    time.sleep(0.4)
    print("                                 ")
    print("                              ð¸")
    print("")
    color.write("              ð¸","STRING")
    print("    ð¸")
    print("                       ð¸")
    time.sleep(0.4)
    print("                      ð¥³ð¤©ðði love youâ¤ð¥³ð¤©ðð")
    print("                                  ")
    time.sleep(0.4)
    print("")
    color.write("ð i love youâ¤","KEYWORD")
    print("                                                       ")
    print("")
    print("")
    print("")
    color.write("wishing you both continued and happiness for many years to come..\n","KEYWORD")
    print("")
    print("")
    time.sleep(0.4)
    i+=1
    print("thanku\n")


