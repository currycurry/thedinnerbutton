{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf460
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 AndaleMono;\f2\froman\fcharset0 Times-Roman;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue233;\red47\green255\blue18;\red180\green36\blue25;
}
\margl1440\margr1440\vieww18680\viewh7680\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\b\fs24 \cf0 Summary:
\b0 \
\
The Dinner Button is running on a Raspberry Pi. A momentary push button triggers a python script using GPIO. When the button is pressed at dinner time on weekdays, a webcam takes a picture of the kitchen counter and attaches it to an all agency email. The button also has an LED in it that responds when the button is pressed, and whenever the script starts up.\
\
\
/////////\

\b Debugging:\
\

\b0 The button is active between 7 and 9pm. If you press it at any other time, the button will light up once to let you know it heard the push, but it\'92s not dinner time. \
\
If you press it between 7 and 9, the light will blink 3 times quickly, letting you know it thinks its taking a picture and sending an email. If no all agency email is sent, try restarting the raspberry pi.\
\

\b Restart:\

\b0 Most issues will be solved by restarting the raspberry pi. There is a second tiny push button on a perf board sitting on top of the raspberry pi that initiates a safe shutdown. Press hold it for 5 seconds. This will trigger a safe shutdown of the pi. The status lights will flash a bit then all but the pwr light will go off. Unplug the power cable (micro usb) for a minute, then plug it back in.\
\
Don\'92t just yank the power cable, this can brick the sd card.\
\
When the pi starts up again, it will auto launch the dinner button script. You should see the button light blink twice to indicate this has happened. \
\

\b Gmail:
\b0 \
If this doesn\'92t work, check it\'92s d5 gmail account and see if there are any bounced messages.\
\pard\pardeftab720\partightenfactor0
\cf0 login: {\field{\*\fldinst{HYPERLINK "mailto:dinnerbutton@droga5.com"}}{\fldrslt \cf2 \ul \ulc2 dinnerbutton@droga5.com}}\
password : thedinnerbutton\
\
Contact IT if there are sent messages that bounced.\
\
2 step authentication is currently going to my phone (Catherine\'92s - 413.320.3267 in case someone needs to contact me about this)\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \

\b Network:
\b0 \
The Dinner Button is assigned a static ip address\
192.168.9.118\
\
You can ssh into it from the Droga5 offices\
$ ssh pi@192.168.9.118\
password: raspberry\
\
There is a directory called dinnersHere on the desktop. inside that folder you\'92ll find a couple of scripts that test individual parts of the system - camera, button, email\'85 there is also a folder of images, and a couple of other images.\
\
dinnersHere_live.py is the active code running the dinner button. \
\
It uses GPIO to talk to the buttons and LED. \
It takes pictures with the webcam using fswebcam\
It sends emails with attachments using mpack.\
\
The script is set to send debug emails to the button\'92s maintainer - debugEmailRecipient. When the script starts debugEmailRecipient will receive an email with a snapshot taken at startup. They will also get an email every weekday at 7pm when the button activates.\
\
Check currently running python scripts with\
$ ps aux | grep python\
\
you should see 5 items, something like:\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f1 \cf3 \cb0 \CocoaLigature0 root      2268  0.0  0.5   3608  2260 ?        S    14:28   0:00 sudo \cf4 python\cf3  /home/pi/bin/shutdown.py\
root      2269  0.0  0.5   3608  2236 ?        S    14:28   0:00 sudo \cf4 python\cf3  /home/pi/dinnersHere/dinnersHere_live.py\
root      2278  0.1  1.1   6620  5300 ?        S    14:28   0:00 \cf4 python\cf3  /home/pi/bin/shutdown.py\
root      2279 90.4  1.2   7128  5556 ?        R    14:28   2:50 \cf4 python\cf3  /home/pi/dinnersHere/dinnersHere_live.py\
pi        2329  0.0  0.4   3552  1832 pts/0    S+   14:31   0:00 grep --color=auto \cf4 python\cf3 \
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0 \cf0 \cb1 \CocoaLigature1 \
because the dinner button and the shutdown button use GPIO, they need to be run as root. You will see two processes for each script. \
\
restart the dinner button script by killing the process\
$ sudo kill 2269\
\
then launch it again and run in the background.\
$ sudo python dinnersHere_live.py &\
\
The script will start, the led will blink, debugEmailRecipient will get an email with a picture attached.\
\
////////\

\b More Network Issues?
\b0 \
\
If you can\'92t ssh into the pi, or ping 192.168.9.118, contact IT.\
\
You can also do a port scan to see if you can find it anywhere on the network. I use nmap then search for it\'92s MAC Address: 00:E0:4C:04:F1:AC\
\
$ sudo map -v -sP 192.168.9.0/24\
.\
.\
.\
Nmap scan report for 192.168.9.118\
Host is up (0.14s latency).\
MAC Address: 00:E0:4C:04:F1:AC (Realtek Semiconductor)\
.\
.\
.\
\
Drogue has 192.168.9.0/24, 192.168.10.0/24, 192.168.11.0/24, 192.168.12.0/24 (maybe more at this point)\
If Its IP has changed, ask someone in IT.\
\
\pard\pardeftab720\partightenfactor0

\f2 \cf0 \
}