from fbchat import Client
from fbchat.models import *
import time;

localtime = time.asctime( time.localtime(time.time()))

with open('msg1.txt', encoding='utf8') as f:
	txt = f.read().strip()


final_text = txt + "\n\n\nTimestamp: " + localtime

class CustomClient(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
		if author_id != self.uid:
			if thread_type != ThreadType.GROUP:
				message_id = client.send(Message(text=final_text), thread_id=thread_id, thread_type=thread_type)

client = CustomClient('username', 'password') # replace your username and password here
session_cookies = client.getSession()
client.getSession()
client.listen()
