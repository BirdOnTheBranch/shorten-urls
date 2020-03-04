import random
import string

class Shortner:
    token_size  = 5

    def __init__(self, token_size=5):
        self.token_size = token_size 

    def issue_token(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(self.token_size))
