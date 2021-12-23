# VPS port scanner is designed for use with CYB 333 classroom environment.
# Special conditions such as network connections to Metasploitable
# In a virtualized environment exist. Refer to README.txt for details.


import socket


class VPS:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []

    def __repr__(self):
        return 'VPS: {}'.format(self.ip)

    def add_port(self, port):
        self.open_ports.append(port)

    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport + 1):
            if self.is_open(port):
                self.add_port(port)

    def is_open(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((self.ip, port))
        # print('Port {}:      {}'.format(port, result))
        sock.close()
        return result == 0

    def write(self, filepath):
        openport = map(str, self.open_ports)
        with open(filepath, 'w') as f:
            f.write('\n'.join(openport))


def main():
    ip = '192.168.0.233'  # IP address of metasploitable machine
    vpscan = VPS(ip)
    vpscan.scan(1, 100)  # Define lower and upper scan range
    # print(vpscan.open_ports)
    vpscan.write('./loot')


if __name__ == '__main__':
    main()
