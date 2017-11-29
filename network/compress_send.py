# -*-coding:utf8-*-

import argparse
import string
import os
import sys
import gzip
import cStringIO
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8800
HTML_CONTENT = ""


class RequstHandler(BaseHTTPRequestHandler):
    """ custom request handler """

    def go_GET(self):
        """ Handler for the GET requests """
        self.send_response(200)
        self.send_header('Content-tye', 'text/html')
        self.send_header('Content-Encoding', 'gzip')
        zbuf = self.compress_buffer(HTML_CONTENT)
        sys.stdout.write("Content-Encoding:gzip\r\n")
        self.send_header('Content-Length', len(zbuf))
        self.send_header()

        # Send the message to browser
        zbuf = self.compress_buffer(HTML_CONTENT)
        sys.stdout.write("Content-Encoding:gzip\r\n")
        sys.stdout.write("Content-Length:%d\r\n" % (len(zbuf)))
        sys.stdout.write("\r\n")
        self.wfile.write(zbuf)
        return

    def compress_buffer(self, buf):
        zbuf = cStringIO.StringIO()
        zfile = gzip.GzipFile(mode='wb', fileobj=zbuf, compresslevel=6)
        zfile.write(buf)
        zfile.close()
        return zbuf.getvalue()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', action="store", dest="port", type=int, default=DEFAULT_PORT)
    given_args = parser.parse_args()
    port = given_args.port
    server_address = (DEFAULT_HOST, port)
    server = HTTPServer(server_address, RequstHandler)
    server.serve_forever()