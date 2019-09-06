from fbchat import Client
from fbchat.models import *
from random import randrange
import time
from datetime import datetime
import sys
import string
from pygtail import Pygtail
import pickle
from getpass import getpass


prev_threads = []
bloc_threads = []

prebloc_threads = []

received = []
reply = []

auto = '[Auto Reply by bot! 🤖 ] \n '




with open('msg1.txt', encoding='utf8') as my_file1:
	txt1 = my_file1.read().strip()

with open('msg2.txt', encoding='utf8') as my_file2:
	txt2 = my_file2.read().strip()

with open('blacklist.txt', encoding='utf8') as my_file3:
	for line in my_file3:
		prebloc_threads.append(line.strip())

with open('received.txt', encoding='utf8') as my_file4:
	for line in my_file4:
		received.append(line.strip())

with open('reply.txt', encoding='utf8') as my_file5:
	for line in my_file5:
		reply.append(line.strip())




def reload1():
	for line in Pygtail("received.txt"):
		received.append(line.strip())
	for line in Pygtail("reply.txt"):
	    reply.append(line.strip())
	for line in Pygtail("blacklist.txt"):
	 	prebloc_threads.append(line.strip())


def reload2():
	with open('msg1.txt', encoding='utf8') as my_file1:
	 	txt1 = my_file1.read().strip()
	with open('msg2.txt', encoding='utf8') as my_file2:
		txt2 = my_file2.read().strip()
	 	        


class CustomClient(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
		reload1()
		reload2()
		localtime = datetime.now()
		time.sleep(randrange(4,10))
		thread = self.fetchThreadInfo(thread_id)[thread_id]
		primary_text = auto + '\n' + thread.name + ", " + txt1 + "\nTimestamp: " + localtime
		secondary_text = auto + '\n' + thread.name + ", " +  txt2 + "\nTimestamp: " + localtime
		
		index = 100000
		
		signal = 1
		text = message_object.text
		
		try:
			matching = text.lower()
			matching = matching.translate(str.maketrans('', '', string.punctuation))
		except:
			matching = None

		'''if author_id == self.uid:
			if thread_type != ThreadType.Group:
				if text is 'bot100, stop replying':
					self.send(Message(text= auto + '\n okay, stopping reply to ' + thread.name), thread_id=thread_id, thread_type=thread_type)
					bloc_threads.append(thread_id)
				if text is 'bot100, restart replying':
					message_id = client.send(Message(text=auto + ' \n okay, restarting reply to ' + thread.name), thread_id=thread_id, thread_type=thread_type)
					bloc_threads.remove(thread_id)
				if text is 'bot100, add received':
					message_id = client.send(Message(text=auto + ' \n okay, waiting for received data... (12 seconds remaining)'), thread_id=thread_id, thread_type=thread_type)
					time.sleep(12)
					if text != 'bot100, add received':
						received.append(text + '\n')
						with open("received.txt", "a") as my_file4:
							my_file4.write(text + '\n')
						message_id = client.send(Message(text=auto + ' \n added received data in array and file.'), thread_id=thread_id, thread_type=thread_type)
				if text is 'bot100, add reply':
					message_id = client.send(Message(text=auto + ' \n okay, waiting for reply data... (12 seconds remaining)'), thread_id=thread_id, thread_type=thread_type)
					time.sleep(12)
					if text != 'bot100, add reply':
						reply.append(text + '\n')
						with open("reply.txt", "a") as my_file5:
							my_file5.write(text + '\n')
						message_id = client.send(Message(text=auto + ' \n added reply data in array and file.'), thread_id=thread_id, thread_type=thread_type)
				if text is 'bot100, shutdown':
					message_id = client.send(Message(text=auto + ' \n Shutting Down...'), thread_id=thread_id, thread_type=thread_type)
					time.sleep(3)
					sys.exit()'''
					
		if author_id != self.uid:
			if thread_type != ThreadType.GROUP:
				
				if matching != None:
					for replies in received:
						if matching in replies:
							index = received.index(replies)
							msg = auto + reply[index]
							message_id = client.send(Message(text=msg), thread_id=thread_id, thread_type=thread_type)
							break
							
				if thread_id not in prebloc_threads:
					if thread_id not in bloc_threads:
						if thread_id in prev_threads and matching != None and index == 100000:
							message_id = client.send(Message(text=secondary_text), thread_id=thread_id, thread_type=thread_type)
							bloc_threads.append(thread_id)
			
			
				
					
					
				if thread_id not in prev_threads and thread_id not in bloc_threads and thread_id not in prebloc_threads and matching != None and index == 100000:
					message_id = client.send(Message(text=primary_text), thread_id=thread_id, thread_type=thread_type)
					prev_threads.append(thread_id)
				else:
					None

try:
	print('Checking for cookies...')
	session_cookies = pickle.load(open('cookies.p','rb'))
	client = CustomClient("cookie", "cookie", session_cookies = session_cookies) # replace your username and password here
	print('Cookies found!')
except:
	print('Cookies not found. Please enter credentials.')
	client = CustomClient(input('Email: '), getpass('Password: ')) # replace your username and password here
	session = client.getSession()
	pickle.dump(session, open('cookies.p','wb'))
	print('Cookies saved to cookies.p file.')


print('Starting program...')
client.listen()
