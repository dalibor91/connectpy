import sys
import datetime

from argparse import ArgumentParser
from pyconnect import helpers
from pyconnect import Domain

_parser = ArgumentParser(description="Check connectivity to some server")
_parser.add_argument("-d", "--domain", dest="host", help="Domain name what to check")
_parser.add_argument("-ip", "--ip", dest="ip", help="IP Address to check")
_parser.add_argument("-p", "--port", dest="port", type=int, help="Port number")
_parser.add_argument("-t", "--type", dest="type", choices=["ping", "telnet"], default="ping")



if __name__ == "__main__":

    _data = _parser.parse_args()

    if _data.host is None and _data.ip is None:
        helpers.error_msg("Host or IP are required", 1)

    _domain = Domain(_data.host) if _data.host is not None else Domain.create_from_ip(_data.ip)

    helpers.info_msg("IP     : %s" % str(_domain.ip))
    helpers.info_msg("Domain : %s" % str(_domain.domain))
    helpers.info_msg("Port   : %s" % str(_data.port))
    helpers.info_msg("Start  : %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if _data.type == 'telnet':
        if _data.port is None:
            helpers.error_msg("Port is required for telnet")

        _telnet = helpers.telnet(_domain.ip, _data.port)

        if _telnet is None:
            helpers.error_msg("Unable to telnet (%s, %s)" % (str(_domain.ip), str(_data.port)), 2)
    elif _data.type == 'ping':
        _ping = helpers.ping(_domain.ip)

        if _ping is None:
            helpers.error_msg("Unable to ping %s" % str(_domain.ip), 3)

helpers.info_msg("End    : %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

sys.exit(0)
'''
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
'''










