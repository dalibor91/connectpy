import socket

class Domain:

    __domain = None

    __cache = {}

    def __init__(self, domain):
        self.__domain = domain

    @property
    def domain(self):
        return self.__domain

    @property
    def ip(self):
        if self.__get_cache('ip') is None:
            self.__add_cache('ip', socket.gethostbyname(self.domain))

        return self.__get_cache('ip')

    def addr_info(self, port=80, proto=socket.IPPROTO_TCP):
        if self.__get_cache('addr_info') is None:
            self.__add_cache('addr_info', socket.getaddrinfo(self.domain, port, 0, 0, proto))

        return self.__get_cache('addr_info')

    def get_ip_v6(self, port=80, proto=socket.IPPROTO_TCP):
        _data = self.addr_info(port, proto)
        _ip1 = _data[1][4][0] if len(_data) > 1 and len(_data[1]) > 4 and len(_data[1][4])>0 else None
        _ip2 = _data[0][4][0] if len(_data) > 1 and len(_data[0]) > 4 and len(_data[0][4])>0 else None

        return _ip1 if _ip1 is not None and ':' in _ip1 else _ip2

    @property
    def hostname(self):
        __info = self.__fetch_info()
        return __info[0] if len(__info) > 0 else None

    @property
    def aliases(self):
        __info = self.__fetch_info()
        return __info[1] if len(__info) > 1 else []

    @property
    def addresses(self):
        __info = self.__fetch_info()
        return __info[2] if len(__info) > 2 else []

    def __fetch_info(self):
        if self.__get_cache('addrs') is None:
            self.__add_cache('addrs', socket.gethostbyaddr(self.ip))

        return self.__get_cache('addrs', None)

    def __add_cache(self, name, val):
        self.__cache[name] = val
        return self

    def __get_cache(self, name, default=None):
        if name in self.__cache:
            return self.__cache[name]

        return default

    def __str__(self):
        return str({
            'ip' : self.ip,
            'domain': self.domain,
            'ipv6': str(self.get_ip_v6()),
            'hostname': self.hostname,
            'aliases':self.aliases,
            'addresses': self.addresses,
         #   '_cache':self.__cache
        })

    @staticmethod
    def create_from_ip(ip):
        return Domain(socket.gethostbyaddr(ip))


class DomainPort:

    __domain = None
    __port = None

    def __init__(self, domain, port):
        if isinstance(domain, Domain):
            self.__domain = domain
        else:
            self.__domain = Domain(domain)
        self.__port = int(port)

    @property
    def domain(self):
        return self.__domain

    @property
    def port(self):
        return self.__port

    def addr_info(self, proto=socket.IPPROTO_TCP):
        return self.domain.addr_info(self.port, proto)

    @staticmethod
    def from_ip(ip, port):
        return DomainPort(Domain.create_from_ip(ip), port)

    def __str__(self):
        return str({
            'domain': str(self.domain),
            'port': str(self.port)
        })
