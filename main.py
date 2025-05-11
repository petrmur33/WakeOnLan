import socket
import sys


def wol(lunaMacAddress: bytes):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    magic = b'\xff' * 6 + lunaMacAddress * 16
    s.sendto(magic, ('<broadcast>', 7))


def main(args: list[str]):
    if len(args) < 2:
        print("""python3 -m main <MAC address> - sends WakeOnLan broadcast with specified MAC address
MAC address must be six bytes in hex each separated with ':' symbol. You can use both upper and lower case.
This utility doesn't verify MAC address, so invalid MAC can cause some unexpected things""")
        return
    mac = bytes.fromhex(args[1].replace(":", " "))
    wol(mac)


if __name__ == '__main__':
    main(sys.argv)
