#ignore used for testing only


from phue import Bridge
from time import sleep

hueBridge = Bridge("10.0.0.5")
hueBridge.connect()
lights = hueBridge.lights
for l in lights :
    print(f"{l}")
#print(f"{hueBridge.get_api()}")
#command =  {'transitiontime' : 300, 'on' : True, 'bri' : 254}    
#hueBridge.set_light("Ferdie Uplight 1", command)
#sleep(300)
#hueBridge.set_light("Ferdie Uplight 1", 'on', False)
uplight2 = hueBridge.get_light("Ferdie Uplight 2")
print(f"{uplight2}")