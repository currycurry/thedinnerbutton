#!/usr/bin/env python

import time
import os

testMessage = "\"Cam Test\""
emailRecipient = "cmccurry@droga5.com"

snapTime = datetime.datetime.fromtimestamp( currentTime ).strftime('%Y-%m-%d_%H_%M_%S')
imageFile = path + str( snapTime ) + ".jpg"
os.system( "sudo fswebcam -r 1280x720 --no-banner " + imageFile )
print( "image saved attempting to send email" )
os.system( "mpack -s" + " " + testMessage + " " + imageFile + " " + emailRecipient )
print( "check your email" )

