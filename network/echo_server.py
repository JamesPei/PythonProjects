# -*-coding:utf-8-*-

import argparse
import socket

host = 'localhost'
data_payload = 2048
backlog = 5


def echo_server(port):
    # create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind the socket to the port
    server_address = (host, port)
    sock.bind(server_address)
    # listen to the clients, backlog argument specifies the max no. of queued connections
    sock.listen(backlog)
    while True:
        client, address = sock.accept()
        data = client.recv(data_payload)
        if data:
            print "Data:%s" % data
            client.send(data)
            print "sent %s bytes back to %s" % (data, address)
        # end connection
        client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)