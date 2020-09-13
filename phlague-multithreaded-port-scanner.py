#!/usr/bin/env python
#this is the phlague-multithreaded-port-scanner

import socket, threading, thread

class PortScanner(threading.Thread):
    openportcount = 0
    
    def __init__(self, hostname, portrange):
        threading.Thread.__init__(self)
        self.hostname = hostname
        self.portrange = portrange
        
    def run(self):
        while True:            
            for port in range(self.portrange[0],self.portrange[1]):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                status = sock.connect_ex((self.hostname,port))
                print status
                if status == 0:
                    #print "from thread %s"%str(threading.current_thread().name)
                    print "open\t%d"%port
                    PortScanner.openportcount+=1
                    sock.close()
                else:
                    pass
            
            thread.exit()
            


def main():
    print "[*] Starting Port Scanner....\n"
    hostname = raw_input("[?] Host name for port scanning : ")
    portrange = list((raw_input("[?] Port range : ").split("-")))
 
 
    lport = int(portrange[0])
    uport = int(portrange[1])
    
    if lport>uport:
        tempport = uport
        uport = lport
        lport = tempport
    
    if uport > 65535:
        uport = 65535
        print "[!] Port must be 0-65535\n[!] Port range set to %d - 65535\n"%lport
    elif lport < 0:
        lport = 0
        print "[!] Port must be 0-65535\n[!] Port range set to 0 - %d\n"%uport
    

    no_of_threads = int(raw_input("[?] No of threads : "))
  
    r = (uport - lport)/no_of_threads
    
    print "\n[+] %d Threads starting...\n"%no_of_threads
 
    threads = []
    for i in range(1,no_of_threads+1):
        uport = lport + r+ 1
        if uport>65535:
            uport=65535
        ports = [lport, uport]
        thread = PortScanner(hostname, ports)
        lport = uport+1
        thread.start()
        threads.append(thread)
    
    for t in threads:
        t.join()
        
    print "\n%d open ports found!"%PortScanner.openportcount
    print "\nDone!"
        
        
if __name__ == "__main__":
    main()
