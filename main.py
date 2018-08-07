import pyconnect
import sys

host_port = pyconnect.DomainPort(sys.argv[1], int(sys.argv[2]))

print("Host: %s" % host_port.domain.domain)
print("IP:   %s" % host_port.domain.ip)
print("Port: %d" % host_port.port)

try:
    for i in sys.argv:
        if i == '--ping' or i == '-ping':
            if pyconnect.ping(host_port.domain.ip, udp=True):
                print("Able to ping %s" % host_port.domain.ip)
        elif i == '--telnet' or i == '-telnet':
            telnet = pyconnect.Telnet(host_port.domain.ip, host_port.port)
            if telnet.telnet(10):
                print("Able to connect")
                telnet.telnet().close()
except Exception as e:
    print(e)
    sys.exit(1)










