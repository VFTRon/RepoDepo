import socket  # Get everything from the socket library.


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 5000
    result = sock.connect_ex((host, port))
    print('Result: {}'.format(result))
    sock.close()


if __name__ == '__main__':
    main()
