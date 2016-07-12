#!/usr/bin/python
#Dinner Button

#import GPIO for hardware
import RPi.GPIO as GPIO
import time
import datetime
import os

#init hardware
GPIO.setwarnings( False )
GPIO.setmode( GPIO.BCM )
GPIO.setup( 24, GPIO.IN, pull_up_down=GPIO.PUD_UP )
GPIO.setup( 17, GPIO.OUT )

width = 1280
height = 720
maxFiles = 20
currentTime = time.time()
snapTime = datetime.datetime.fromtimestamp( currentTime ).strftime('%Y-%m-%d_%H:%M:%S')
dayOfTheWeek = datetime.datetime.now().weekday()
lastDayOfTheWeek = dayOfTheWeek - 1
currentHour = datetime.datetime.now().hour
lastHour = currentHour - 1
buttonPrimed = False

#debug print statements
print( "day of the week: " + str( dayOfTheWeek ))
print( "current hour: " + str( currentHour ))
print( "button state: " + str( GPIO.input(24)))
print( "buttonPrimed: " + str( buttonPrimed ))

#minHour = 17
#maxHour = 18
minHour = 19
maxHour = 21

iterator = 0

#file paths etc
device = "/dev/video0"
path = "/home/pi/dinnersHere/images/"
imageFile = path + str( snapTime ) + ".jpg"
primedFile = "/home/pi/dinnersHere/hungry_child.jpg"
frownFile = "/home/pi/dinnersHere/frown.jpg"

#email addresses
dinnerMessage = "\"Dinner\'s Here!\""
pizzaMessage = "\"Pizza\'s Here!\""
#dinnerEmailRecipient = "cmccurry@droga5.com" 
dinnerEmailRecipient = "droga5ny@droga5.com"
noDinnerMessage = "\"Not sure what happened. No dinner, though.\""
#noDinnerEmailRecipient = "cmccurry@droga5.com"
noDinnerEmailRecipient = "rtoma@droga5.com"
debugEmailRecipient = "cmccurry@droga5.com"

#blink button twice on startup
for i in range( 0, 2 ):
        GPIO.output( 17, True )
        time.sleep( .5 )
        GPIO.output( 17, False )
        time.sleep( .5 )

#take a picture and send it to debug on startup
testMessage = "\"Startup Test\""
os.system( "sudo fswebcam -r 1280x720 --no-banner " + imageFile )
print( "image saved attempting to send email" )
os.system( "mpack -s" + " " + testMessage + " " + imageFile + " " + debugEmailRecipient )
print( "check your email" )

def check_internet():
        if( os.system( "ping -c 2 -t 5 192.168.8.1" ) > 0 ):
                print( "Not connected to the router" )
                for i in range( 0, 5 ): #blink slowly to indicate issue with router communication
                        GPIO.output( 17, True )
                        time.sleep( 1 )
                        GPIO.output( 17, False )
                        time.sleep( 1 )
                os.system( "sudo /home/pi/network-monitor.sh" )
        if( os.system( "ping -c 2 -t 5 8.8.8.8" ) > 0 ):
                print( "Not connected to the internet" )
                for i in range( 0, 10 ): #two quick blinks indicates we can't reach the outside world
                        GPIO.output( 17, True )
                        time.sleep( .05 )
                        GPIO.output( 17, False )
                        time.sleep( .05 )
                        GPIO.output( 17, True )
                        time.sleep( .05 )
                        GPIO.output( 17, False )
                        time.sleep( .2 )
                os.system( "sudo /home/pi/network-monitor.sh" )
                check_internet()

#check_internet()



def buttonPressed_callback( channel ):
        print("button callback called")
        print("button state: " + str(GPIO.input(24)))

        global buttonPrimed
        if ( GPIO.input(24) == 0 ):
                print( str( datetime.datetime.fromtimestamp( currentTime ).strftime('%Y-%m-%d_%H_%M_%S')))
                if ( buttonPrimed == True ):
                        print("and buttonPrimed == True")
                        dayOfTheWeek = datetime.datetime.now().weekday()
                        if ( dayOfTheWeek == 0 or dayOfTheWeek == 1 or dayOfTheWeek == 2 or dayOfTheWeek == 3 ):
                                print( "and today is a weekday" )
                                for i in range( 0, 3 ):
                                        GPIO.output( 17, True )
                                        time.sleep( .325 )
                                        GPIO.output( 17, False )
                                        time.sleep( .325 )

                                buttonPrimed = False

                                GPIO.output( 17, True )

                                if ( dayOfTheWeek == 0 or dayOfTheWeek == 1 or dayOfTheWeek == 2 ):
                                        dinnerMessage = "\"Dinner\'s Here!\""
                                        print( "dinner's here" )

                                elif ( dayOfTheWeek == 3 ):
                                        dinnerMessage = "\"Pizza\'s Here!\""
                                        print( "pizza's here" )

                                else:
                                        dinnerMessage = "\"JK no food for you!\""
                                        print( "jk no food for you" )


                                snapTime = datetime.datetime.fromtimestamp( currentTime ).strftime('%Y-%m-%d_%H_%M_%S')
                                imageFile = path + str( snapTime ) + ".jpg"
                                os.system( "sudo fswebcam -r 1280x720 --no-banner " + imageFile )
                                print("image saved attempting to send email" )

                                os.system( "mpack -s" + " " + dinnerMessage + " " + imageFile + " " + dinnerEmailRecipient )

                                global iterator
                                iterator += 1
                                if ( iterator >= maxFiles ):
                                        print( "clearing memory" )
                                        clearMemory()

                                GPIO.output( 17, False )

                        else:
                                print( "button pressed and primed but no dinner tonight" )
                                for i in range( 0, 2 ):
                                        GPIO.output( 17, True )
                                        time.sleep( .5 )
                                        GPIO.output( 17, False )
                                        time.sleep( .5 )

                                        time.sleep( .5 )
                else:
                        print( "button pressed but not primed" )
                        GPIO.output( 17, True )
                        time.sleep( 1 )
                        GPIO.output( 17, False )
        else:
                print( str( datetime.datetime.fromtimestamp( currentTime ).strftime('%Y-%m-%d_%H_%M_%S')))
                print( "false positive" )

def clearMemory():
        print( "clearing now" )
        os.system( "sudo rm " + path + "/*" )
        global iterator
        iterator = 0

def primeButton():
        global buttonPrimed
        os.system( "mpack -s 7pm" + " " + primedFile + " " + debugEmailRecipient )
        buttonPrimed = True
        print( "buttonPrimed: " + str( buttonPrimed ))
        print( "7pm button primed" )
        for i in range( 0, 2 ):
                GPIO.output( 17, True )
                time.sleep( .5 )
                GPIO.output( 17, False )
                time.sleep( .5 )

def disableButton():
        global buttonPrimed
        os.system( "mpack -s 9pm" + " " + frownFile + " " + noDinnerEmailRecipientt )
        #tell the system not to wait for a dinner message
        buttonPrimed = False
        print( "9pm button disabled" )
        for i in range( 0, 4 ):
                GPIO.output( 17, True )
                time.sleep( .1 )
                GPIO.output( 17, False )
                time.sleep( .1 )

#GPIO.add_event_detect( 24, GPIO.FALLING, callback=buttonPressed_callback, bouncetime = 30000 )

try:
        while True:

                currentTime = time.time()
                currentHour = datetime.datetime.now().hour
                dayOfTheWeek = datetime.datetime.now().weekday()
                if ( dayOfTheWeek >= 0 and dayOfTheWeek <= 3 ):
                        if dayOfTheWeek != lastDayOfTheWeek:
                                print( "today is a weekday" )

                        #prime the button for pressing at 7 pm 0019 hours
                        if ( currentHour == minHour and currentHour != lastHour ):
                                print( "7pm priming button")
                                primeButton()

                        #if it's after 9 and the button hasn't been pressed, alert the authorities
                        if ( currentHour >= maxHour and buttonPrimed == True ):
                                print( "9pm no button press disabling button" )
                                disableButton()

                if(GPIO.input(24) == 0):
                        print("Button pressed")
                        time.sleep( .1 )
                        buttonPressed_callback(1)
                        time.sleep( 3 )

                lastHour = currentHour
                lastDayOfTheWeek = dayOfTheWeek

except KeyboardInterrupt:
        GPIO.cleanup()

finally:
        GPIO.cleanup()

