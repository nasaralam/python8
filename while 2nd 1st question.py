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
    print("                                    🔸")
    color.write("         🎂Happy anniversary to both of you my parents!🎉","COMMENT")
    print("") 
    color.write("                    🔸","STRING")
    print("         🔸")
    color.write("                               🔸","STRING")
    time.sleep(0.4)
    print("🔸") 
    print("                                 ")
    print("                                                 🔸")
    print("")
    print("                         🔸")
    time.sleep(0.4)
    print("             🔸")
    color.write("                                    🔸","STRING")
    print("🔸")
    color.write("🥳🤩🎂🎉i love you❤🥳🤩🎂🎉")
    time.sleep(0.4)
    print("                                 ")
    print("                              🔸")
    print("")
    color.write("              🔸","STRING")
    print("    🔸")
    print("                       🔸")
    time.sleep(0.4)
    print("                      🥳🤩🎂🎉i love you❤🥳🤩🎂🎉")
    print("                                  ")
    time.sleep(0.4)
    print("")
    color.write("🎉 i love you❤","KEYWORD")
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


