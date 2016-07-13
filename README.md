**Summary:**

The Dinner Button is running on a Raspberry Pi. A momentary push button triggers a python script using GPIO. When the button is pressed at dinner time on weekdays, a webcam takes a picture of the kitchen counter and attaches it to an all agency email. The button also has an LED in it that responds when the button is pressed, and whenever the script starts up.

/////////

**Debugging:**


The button is active between 7 and 9pm. If you press it at any other time, the button will light up once to let you know it heard the push, but it's not dinner time. 

If you press it between 7 and 9, the light will blink 3 times quickly, letting you know it thinks its taking a picture and sending an email. If no all agency email is sent, try restarting the raspberry pi.


**Restart:**

Most issues will be solved by restarting the raspberry pi. There is a second tiny push button on a perf board sitting on top of the raspberry pi that initiates a safe shutdown. Press hold it for 5 seconds. The status lights will flash a bit then all but the pwr light will go off. Unplug the power cable (micro usb) for a minute, then plug it back in.

Don't just yank the power cable, this can brick the sd card.

When the pi starts up again, it will auto launch the dinner button script. You should see the button light blink twice to indicate this has happened. 


**Gmail:**

If this doesn't work, check its d5 gmail account and see if there are any bounced messages.

login: dinnerbutton@droga5.com <br />
password : thedinnerbutton

Contact IT if there are sent messages that bounced.

2 step authentication is currently going to catherine's phone (Catherine's - 413.320.3267 in case someone needs to contact me about this)

**Network:**

The Dinner Button is assigned a static ip address:<br /> 
**192.168.9.118**

You can ssh into it from the Droga5 offices <br />
$ ssh pi@192.168.9.118 <br />
password: raspberry

There is a directory called dinnersHere on the desktop. inside that folder you'll find a couple of scripts that test individual parts of the system - camera, button, email... there is also a folder of images taken by the webcam, and a couple of other images.

dinnersHere_live.py is the active code running the dinner button. 

The script is set to send debug emails to the button's maintainer - debugEmailRecipient. When the script starts debugEmailRecipient will receive an email with a snapshot taken at startup. They will also get an email every weekday at 7pm when the button activates.

Check currently running python scripts with <br />
$ ps aux | grep python

you should see 5 items, something like:

root      2268  0.0  0.5   3608  2260 ?        S    14:28   0:00 sudo python /home/pi/bin/shutdown.py <br />
root      2269  0.0  0.5   3608  2236 ?        S    14:28   0:00 sudo python /home/pi/dinnersHere/dinnersHere_live.py <br />
root      2278  0.1  1.1   6620  5300 ?        S    14:28   0:00 python /home/pi/bin/shutdown.py <br />
root      2279 90.4  1.2   7128  5556 ?        R    14:28   2:50 python /home/pi/dinnersHere/dinnersHere_live.py <br />
pi        2329  0.0  0.4   3552  1832 pts/0    S+   14:31   0:00 grep --color=auto python <br />

Because the dinner button and the shutdown button use GPIO, they need to be run as root. You will see two processes for each script. 

restart the dinner button script by killing the process <br />
$ sudo kill 2269

then launch it again and run in the background. <br />
$ sudo python dinnersHere_live.py &

The script will start, the led will blink, debugEmailRecipient will get an email with a picture attached.

////////

**More Network Issues?**

If you can't ssh into the pi, or ping 192.168.9.118, contact IT.

You can also do a port scan to see if you can find it anywhere on the network. I use nmap then search for its MAC Address: 00:E0:4C:04:F1:AC

$ sudo map -v -sP 192.168.9.0/24<br />
. <br />
. <br />
. <br />
Nmap scan report for 192.168.9.118 <br />
Host is up (0.14s latency). <br />
MAC Address: 00:E0:4C:04:F1:AC (Realtek Semiconductor) <br />
. <br />
. <br />
. <br />

Droga has 192.168.9.0/24, 192.168.10.0/24, 192.168.11.0/24, 192.168.12.0/24 (maybe more at this point)
If its IP has changed, ask someone in IT.
