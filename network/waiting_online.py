# -*-coding:utf-8-*-

import argparse
import socket
from time import time as now

DEFAULT_TIMEOUT = 120
DEFAULT_SERVER_HOST = 'localhost'
DEFAULT_SERVER_PORT = 80


class NetServiceChecker(object):
    """ wait for a network service to come online """
    def __init__(self, host, port, timeout=DEFAULT_TIMEOUT):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def end_wait(self):
        self.sock.close()

    def check(self):
        """ check the service """
        if self.timeout:
            end_time = now() + self.timeout

        while True:
            try:
                if self.timeout:
                    next_timeout = end_time - now()
                    if next_timeout < 0:
                        return False
                    else:
                        print "setting socket next timeout %ss" % round(next_timeout)
                        self.sock.settimeout(next_timeout)
                self.sock.connect((self.host, self.port))
            except socket.timeout, err:
                if self.timeout:
                    return False
            except socket.error, err:
                print "Exception: %s" % err
            else:
                self.end_wait()
                return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wait for Network service')
    parser.add_argument('--host', action='store', dest='host', default=DEFAULT_SERVER_HOST)
    parser.add_argument('--port', action='store', dest='port', default=DEFAULT_SERVER_PORT)
    parser.add_argument('--timeout', action='store', dest='timeout', type=int, default=DEFAULT_TIMEOUT)
    given_args = parser.parse_args()
    host, port, timeout = given_args.host, given_args.port, given_args.timeout
    service_checker = NetServiceChecker(host, port, timeout)
    if service_checker.check():
        print 'service is available again'