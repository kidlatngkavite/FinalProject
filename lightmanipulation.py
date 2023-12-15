#ignore used for testing only

# import the threading module
from threading import Thread
from phue import Bridge
from time import sleep
from random import randint
hueBridge = Bridge("10.0.0.5")
hueBridge.connect()
lights = hueBridge.lights
 
class lightShow(Thread): 
    def __init__(self, lightName, hit, brightness): 
        global hueBridge
        Thread.__init__(self) 
        self.lightName = lightName 
        self.hit = hit 
        self.bri = brightness
        self.hueBridge = hueBridge
        
 
        # helper function to execute the threads
    def run(self):
        if self.hit :
            print("hit"); 
        else :
            print(str(self.lightName) +" "+ str(self.hit)); 
            command =  {"transitiontime" : 1, 'on' : True,}
            self.hueBridge.set_light(self.lightName, command)
            for i in range(1,15) :
                randomHue = randint(3000,6000)
                randomBri =  randint(20,self.bri)
                #command =  {"transitiontime" : 30, 'on' : True, "bri" : 254, "hue": 4557, "sat": 249}    
                #command =  {"transitiontime" : 1, 'on' : True, "bri" : 254, "hue": randomHue, "sat": 249}
                command =  {"transitiontime" : 1, "bri" : randomBri, "hue": randomHue, "sat": 249}
                self.hueBridge.set_light(self.lightName, command)
                sleep(0.1)
            hueBridge.set_light(self.lightName, 'on', False)    
 
    def miss(self):
        if self.hit :
            print("hit"); 
        else :
            print(str(self.lightName) +" "+ str(self.hit)); 
            command =  {"transitiontime" : 1, 'on' : True,}
            self.hueBridge.set_light(self.lightName, command)
            for i in range(1,15) :
                randomHue = randint(3000,6000)
                randomBri =  randint(20,self.bri)
                #command =  {"transitiontime" : 30, 'on' : True, "bri" : 254, "hue": 4557, "sat": 249}    
                #command =  {"transitiontime" : 1, 'on' : True, "bri" : 254, "hue": randomHue, "sat": 249}
                command =  {"transitiontime" : 1, "bri" : randomBri, "hue": randomHue, "sat": 249}
                self.hueBridge.set_light(self.lightName, command)
                sleep(0.1)
            hueBridge.set_light(self.lightName, 'on', False)    
 
 
backLeft = lightShow("Ferdie Uplight 1", False, 50) 
backRight = lightShow("Ferdie Uplight 2", False, 50) 
frontLeft = lightShow("Ferdie Task Light 1", False, 50) 
frontRight = lightShow("Ferdie Task Light 2", False, 50)


backLeft.start() 
backRight.start() 
frontLeft.start() 
frontRight.start()
sleep(5)
backLeft.miss() 
backRight.miss() 
frontLeft.miss() 
frontRight.miss()    

#backLeft.hit() 
#backRight.hit() 
#frontLeft.hit() 
#frontRight.hit() 
 
print("Exit") 

#"Ferdie Ceiling 1"
#"Ferdie Ceiling 2"
#"Ferdie Ceiling 3"
#"Ferdie Task Light 1"
#"Ferdie Uplight 1"
#"Ferdie Task Light 2"
#"Ferdie Uplight 2"
#"Hue ambiance lamp 1"