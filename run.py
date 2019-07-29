from fbchat import Client
from fbchat.models import *
import time;

localtime = time.asctime(time.localtime(time.time()))

prev_authors = []

with open('msg1.txt', encoding='utf8') as my_file1:
	txt1 = my_file1.read().strip()

with open('msg2.txt', encoding='utf8') as my_file2:
	txt2 = my_file2.read().strip()

primary_text = txt1 + "\nTimestamp: " + localtime
secondary_text = txt2 + "\nTimestamp: " + localtime

class CustomClient(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
		if author_id != self.uid:
			if thread_type != ThreadType.GROUP:
				if author_id in prev_authors:
					message_id = client.send(Message(text=secondary_text), thread_id=thread_id, thread_type=thread_type)
				else:
					message_id = client.send(Message(text=primary_text), thread_id=thread_id, thread_type=thread_type)
					prev_authors.append(author_id)

client = CustomClient('email', 'password') # replace your username and password here
session_cookies = client.getSession()
client.getSession()
client.listen()
