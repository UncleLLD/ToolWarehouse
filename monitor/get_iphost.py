import socket


def get_host_name():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


if __name__ == '__main__':
    host_name = get_host_name()
    print(host_name)
