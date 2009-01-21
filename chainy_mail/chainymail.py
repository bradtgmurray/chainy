import asyncore
from smtpd import SMTPServer

chainy_mail_domain = 'chainy.neckbeard.ca'
master_inbox = 'master@' + chainy_mail_domain

class MailServer(SMTPServer):
    def __init__(self, output_connection):
        SMTPServer.__init__(self, ('localhost', 8001), None)
        self.output_connection = output_connection

    def process_message(self, peer, mailfrom, rcpttos, data):
        processed = False
        for address in rcpttos:
            inbox, domain = address.split('@')[:2]
            if domain == chainy_mail_domain and address != master_inbox:
                self.output_connection.add_post_to_chain(int(inbox),
                                                         mailfrom, data)
                processed = True

        if not processed:
            chain_id = self.output_connection.create_chain(data, mailfrom)
            self.output_connection.add_post_to_chain(chain_id, mailfrom, data)

class OutputConnection(object):
    def create_chain(self, subject, users):
        pass
    
    def add_post_to_chain(self, chain_id, poster, body):
        pass

if __name__ == '__main__':
    server = MailServer(OutputConnection())
    asyncore.loop()
