import os

#для линукс и мак
export MY_VAR="123"
#для виндовс
#set MY_VAR="123"

class Environment:
    DEV = 'dev'
    PROD = 'prod'

    URLS = {
        DEV: 'https://playground.learnqa.ru/ajax/api_dev',
        PROD: 'https://playground.learnqa.ru/ajax/api'
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
        exept KeyError:
            self.env = self.DEV
    def get_base_url(self):
