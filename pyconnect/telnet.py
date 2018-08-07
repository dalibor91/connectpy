import telnetlib
from .domain import DomainPort


class Telnet:

    __domain_port = None

    __telnet = None

    def __init__(self, domain, port):
        self.__domain_port = DomainPort(domain, port)

    @property
    def domain_port(self):
        return self.__domain_port

    def telnet(self, timeout=1000):
        if self.__telnet is None:
            self.__telnet = telnetlib.Telnet(self.__domain_port.domain.ip, self.__domain_port.port, timeout=timeout)
        return self.__telnet