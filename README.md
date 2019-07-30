# Features
<ul style="list-style-type:circle;">
<li>Replies a specific message to every recipient who messages you.</li>
<li>If anyone messages you twice, then secondary message system is available.</li>
<li>If primary and secondary messages are sent once to a recipient, then bot will not reply to the recipient anymore in an active session.</li>
<li>Waits for a random number (between 4 to 10) of seconds before sending every message to act as a human, to minimize the chance of getting blocked from Facebook.</li> 
<li>Avoids group messages.</li>
<li>Blacklist option available if you want the bot not to respond to specific users.</li>
</ul>

# Before Getting Started
After cloning this repository, edit the <b>run.py</b> with your facebook username and password. Also edit the <b>msg1.txt</b>, <b>msg2.txt</b> and <b>blacklist.txt</b> files with your desired auto reply.

# Installation
Make sure you have installed python3 in your machine. You can also use python2 by converting the whole code.
Then:
<ol>
<li>Install fbchat module: <code>pip3 install fbchat</code></li>
<li>Clone this repository: <code>git clone https://github.com/MS-Jahan/fb-auto-reply-py</code></li>
<li>Change directory to this project folder: <code>cd fb-auto-reply-py</code></li>
<li>Now run the script: <code>python3 run.py</code></li>
</ol>

# Credits
The main core of this project is the <b><a href = 'https://github.com/carpedm20/fbchat'>fbchat</a></b> module. Without the module, it would be a very difficult task.
I just read their <a href = 'https://fbchat.readthedocs.io/en/master/'>doc</a> and copied their <a href = 'https://github.com/carpedm20/fbchat/tree/master/examples'>example code</a> and modified it for beginner users. ;-)
