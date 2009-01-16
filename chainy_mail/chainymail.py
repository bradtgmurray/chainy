import asyncore
from smtpd import SMTPServer

class MailServer(SMTPServer):
    def __init__(self, output_connection):
        SMTPServer.__init__(self, ('localhost', 8000), None)
        self.output_connection = output_connection

    def process_message(self, peer, mailfrom, rcpttos, data):
        print peer + mailfrom + rcpttos + data

class OutputConnection(object):
    def create_chain(self, subject, users):
        pass
    
    def add_post_to_chain(self, chain_id, poster, body):
        pass

if __name__ == '__main__':
    server = MailServer(OutputConnection())
    asyncore.loop()
