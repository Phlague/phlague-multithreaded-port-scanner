# phlague-multithreaded-port-scanner
I have created a multi-threaded port scanner using python. I ran the script in Kali-Linux. - Functionality in brief: This program uses python's "socket","threading" and "thread" modules. Using socket module, this script tries to establish a connection to each port in the port range in the given host. If the connection can be established to a port, this program detects that port as an open port. Otherwise that port is discarded as a closed port.  Multi-threading: Once the user gives a port range to scan and number of threads for scanning, this program devides the port range into equal sized sub-ranges and assigns them to each thread. Following code illustrates that functionality.