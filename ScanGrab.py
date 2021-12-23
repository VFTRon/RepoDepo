from VFTRPortScanVPS import VPS
from BanGrab import Grabber


def main():
    ip = '192.168.0.233'
    scanner = VPS(ip)
    scanner.scan(1, 100)
    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip, port)
            print(grabber.read())
            grabber.close()
        except Exception:
            print('No bueno: Port ',port,'returned no result')


if __name__ == '__main__':
    main()
