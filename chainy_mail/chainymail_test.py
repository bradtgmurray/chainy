import chainymail
import unittest

class TestChain(object):
    def __init__(self, chain_id, subject, users):
        self.chain_id = chain_id
        self.subject = subject
        self.users = users

        self.posts = []

    def add_post(self, poster, body):
        self.posts += (poster, body)

class TestOutputConnection(object):
    def __init__(self):
        self.chains = {}        

    def create_chain(self, subject, users):
        new_chain_id = len(self.chains)
        self.chains[new_chain_id] = TestChain(new_chain_id, subject, users)

    def add_post_to_chain(self, chain_id, poster, body):
        c = self.chains[chain_id]
        c.add_post(poster, body)

class TestMailServer(unittest.TestCase):
    def setUp(self):
        self.output_connection = TestOutputConnection()
        self.mail_server = chainymail.MailServer(self.output_connection)

    def testNewChain(self):
        self.mail_server.process_message('peer', 'mailfrom', 'rcpttos', 'data')
        
        self.assertEqual(len(self.output_connection.chains), 1)

if __name__ == '__main__':
    unittest.main()
