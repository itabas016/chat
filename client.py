#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>

from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore
import threading
import logging
import sys, io
from argparse import ArgumentParser
import config as cfg

class ChatClient(async_chat):
    """
    A chat client
    """

    def __init__(self, host=cfg.HOST, port=cfg.PORT):
        self.logger = logging.getLogger()
        self.write_buffer = ""
        self.read_buffer = io.StringIO()

        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (host, port)
        self.logger.info('connecting to %s' % format(address))
        self.connect(address)
        self.set_terminator('\r\n')
        self.buffer = []

    def handle_connect(self):
        self.logger.debug('handle_connect()')

    def handle_close(self):
        self.logger.debug('handle_close()')
        self.close()

    def writable(self):
        is_writable = (len(self.write_buffer) > 0)
        if is_writable:
            self.logger.debug('writable() -> %s', is_writable)
        return is_writable

    def readable(self):
        self.logger.debug('readable() -> True')
        return True

    def handle_write(self):
        sent = self.send(self.write_buffer.encode(cfg.UTF8))
        self.logger.debug('handle_write() -> "%s"', self.write_buffer[:sent])
        self.write_buffer = self.write_buffer[sent:]

    def handle_read(self):
        data = self.recv(cfg.BUFFER_SIZE).decode(cfg.UTF8)
        self.logger.debug('handle_read() -> %d bytes', len(data))
        self.read_buffer.write(data)

def parse_cli():
    parser = ArgumentParser(description='Simple client tool implementation')
    parser.add_argument(
        '-h', '--host', required=True, help='chat server ip for connection')
    parser.add_argument(
        '-p', '--port', type=int, required=True, help='chat server port')
    return parser.parse_args()

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s',)
    # args = parse_cli()
    c = ChatClient(cfg.HOST, cfg.PORT)

    t = threading.Thread(target=asyncore.loop)
    t.daemon = True
    t.start()

    while True:
        msg = input('>')
        c.send(msg + '\r\n')

if __name__ == '__main__':
    main()    