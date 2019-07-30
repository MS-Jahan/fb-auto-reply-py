from fbchat import Client
from fbchat.models import *
from random import randrange
import time

prev_authors = []
bloc_authors = []

with open('msg1.txt', encoding='utf8') as my_file1:
	txt1 = my_file1.read().strip()

with open('msg2.txt', encoding='utf8') as my_file2:
	txt2 = my_file2.read().strip()

with open('blacklist.txt', encoding='utf') as my_file3:
	for line in my_file3:
		bloc_authors.append(str(int(line)))

class CustomClient(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
		localtime = time.asctime(time.localtime(time.time()))
		time.sleep(randrange(4,10))
		primary_text = txt1 + "\nTimestamp: " + localtime
		secondary_text = txt2 + "\nTimestamp: " + localtime
		if author_id != self.uid:
			if thread_type != ThreadType.GROUP:
				if author_id in bloc_authors:
					None
				elif author_id in prev_authors:
					message_id = client.send(Message(text=secondary_text), thread_id=thread_id, thread_type=thread_type)
					bloc_authors.append(author_id)
				else:
					message_id = client.send(Message(text=primary_text), thread_id=thread_id, thread_type=thread_type)
					prev_authors.append(author_id)

client = CustomClient('email', 'password') # replace your username and password here
session_cookies = client.getSession()
client.getSession()
client.listen()
