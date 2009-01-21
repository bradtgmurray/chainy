import chainymail
import unittest
import threading, asyncore, smtplib

class TestableChain(object):
    def __init__(self, chain_id, subject, users):
        self.chain_id = chain_id
        self.subject = subject
        self.users = users

        self.posts = []

    def add_post(self, poster, body):
        self.posts.append((poster, body))

class TestableOutputConnection(object):
    def __init__(self):
        self.chains = {}

    def create_chain(self, subject, users):
        new_chain_id = len(self.chains)
        self.chains[new_chain_id] = TestableChain(new_chain_id, subject, users)
        return new_chain_id

    def add_post_to_chain(self, chain_id, poster, body):
        c = self.chains[int(chain_id)]
        c.add_post(poster, body)

class MailServerThread(threading.Thread):
    def __init__(self, output_connection):
        threading.Thread.__init__(self)

        self.stop = False
        self.server = chainymail.MailServer(output_connection)

    def run(self):
        while not self.stop:
            asyncore.loop(timeout=1)

class TestMailServerSystem(unittest.TestCase):
    def setUp(self):
        self.output_connection = TestableOutputConnection()

        self.server_thread = MailServerThread(self.output_connection)
        self.server_thread.start()
        
        self.client = smtplib.SMTP()
        #self.client.set_debuglevel(1)
        self.client.connect(port=8001)

    def testBasicMail(self):
        msg = 'Hello world!\n'
        self.client.sendmail('test1@test.com', 'master@chainy.neckbeard.ca', msg)
        self.client.sendmail('test2@test.com', '0@chainy.neckbeard.ca', msg)
        self.assertEqual(len(self.output_connection.chains), 1)
        self.assertEqual(len(self.output_connection.chains[0].posts), 2)
        
    def tearDown(self):
        self.client.quit()
        self.server_thread.stop = True

if __name__ == '__main__':
    unittest.main()
