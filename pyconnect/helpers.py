from sys import exit as sys_exit
from . import ping as ping_host
from . import DomainPort
from .telnet import Telnet

def ping(host):
    try:
        return ping_host(host, udp=True)
    except:
        pass
    return None

def telnet(host, port, timeout=10):
    try:
        _dp = DomainPort(host, port)
        return Telnet(_dp.domain.domain, _dp.port).telnet(timeout)
    except:
        pass
    return None

def _msg(msg, type="info"):
    print("[ %s ] : %s" % (str(type).upper().ljust(10), str(msg)))

def error_msg(msg, exit_code=None):
    _msg(msg, "error")
    if exit_code is not None:
        sys_exit(exit_code)

def info_msg(msg):
    _msg(msg, "info")