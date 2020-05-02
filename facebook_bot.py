from fbchat import Client
from fbchat.models import *


class FacebookBot:
    def __init__(self, email, password):
        self.client = Client(email, password)

    def send_message_to_user(self, msg, uid):
        self.client.send(Message(text=msg), thread_id=uid, thread_type=ThreadType.USER)

    def __logout(self):
        self.client.logout()
