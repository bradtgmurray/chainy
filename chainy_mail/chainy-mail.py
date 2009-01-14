import asyncore
from smtpd import SMTPServer

class ChainyMailServer(SMTPServer):
    def __init__(self):
        SMTPServer.__init__(self, ('localhost', 8000), None)

    def process_message(self, peer, mailfrom, rcpttos, data):
        print peer + mailfrom + tcpttos + data

server = ChainyMailServer()
asyncore.loop()
