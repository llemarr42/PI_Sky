# PI_Sky
Pi in the sky project
.

## Materials used

* Latex balloon(s)
* ~ 3 cubic feet of helium (max)
* Raspberry Pi zero
* Battery
* PowerBoost 500C
* Pi Camera
* 180 degree servo
* Temperature/humidity sensor
* Small switch
* small button
* 3D printed casing
* Valve to control airflow
* accelerometer

## CAD renderings

![balloon_](https://user-images.githubusercontent.com/56924009/170523966-5f947796-b087-4268-bb39-d09f454969da.PNG)





![Balloon_2](https://user-images.githubusercontent.com/56924009/170523982-3d9e8043-6101-4f8d-a412-942f798ea53d.PNG)


## Actual photos and/or video (well lit and in focus)

## A diagram of your circuit

![Circuit](https://user-images.githubusercontent.com/60944294/170525997-beada2d2-2537-4bdd-9b0a-c7a35084f0e8.PNG)

## Commented code
```python
import time
import adafruit_mpl3115a2
import board
from gpiozero import Servo, Button
import os
import picamera


sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60) 
sensor.sealevel_pressure = 102250
i2c = board.I2C()
servo = Servo(18) # servo pin is 18
directory = "../pictures" # will save photos in the picture folder
initialTime = time.time() # gets the time at which it launches
camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

servo.max # makes sure that the servo is in place
altitudeRec[] 
tempratureRec[]
pressureRec[]
while True: 
  altitudeRec.append(sensor.altitude)
  tempratureRec.append(sensor.temprature)
  pressureRec.append(sensor.pressure) # records data into lists to be 
  if altitudeRec[-1] >= altitudeRec[0] + 20 or time.time() >= initialTime + 120: # defines the maximum altitude, and deflates the variable balloon once it reaches it.
    camera.capture('../pictures/image + '.jpg')
    servo.min
```
    
  

## Description of the planning that went into the project, design decisions, and engineering details
Our biggest initial decision was how to design the valve which controls the flow of helium out of the balloon. The valve had to balance being light, fairly simple, easy to control, and reliable. It also had to be able to open AND close. We came up with many designs and after creating three of them in CAD, we decided to go with a plug design which would be pulled down by a string and held in place by some sort of elastic or spring force. 

![Valve Ideas](https://user-images.githubusercontent.com/56133021/153914632-c87b205c-47ad-4936-98ec-13a5f4c2b97d.jpg)

We also needed to design a payload container which was easy to attach the balloon to but was sturdy enough to survive impact. This meant balancing the ease of opening and closing the container. We considered screws as a very reliable option, but because they take some time to put in and take out, they were not suitable for the frequency that the container had to be opened. The design we eventually settled on were 3D printed tabs on the roof of the container which would slide into holes on the body and hold the container shut. When we initially printed them, they were too small and so they easily broke off, but we redesigned them to be bigger in CAD and now they are working well.

## Your process or a schedule of how you spent your time


* _________ through _________: Design the valve: We created and discarded multiple different disigns of valvles in order to find something that fufills all of our needs. This was one of the harder and more time consuming sections even for how simple it seems. The valve is the fulcrom of our project as it is the main peice for controling the assent and dessent of the whole project. It was made much harder by the fact that all the designs we saw online were not what we needed or simply way too heavy, so we had to create our own design using the tools that we had.  

* _________ through _________: Design the capsule: This portion of our project involved the majority of the CAD work that we needed to do. Our goal was to make a box that would hold all of our electronics and other peices and make sure that it or anything in it would not break. We needed to not only do this but it needed to the absolute lightest as we could possibly make it. This is because of our small weight limit due to the low lifting power of the balloons.

* _________ through _________: Write the code: I had some issues figuring out the best way to control the release of air. I made the decision to make it a 180 degree servo instead of a continuous servo because we needed the ability to set the position of the valve to precise values, which a continuous servo would not allow. Additionally, discovering how to measure time in a value of seconds since an epoch was mildly difficult, but by reading through the time library documentation I was able to power through.
* _________ through _________: Test and revise: While we were constantly revising and changing different parts throughout the whole project, this section refers specifically to testing and revisions after everything was printed. We found errors and mistakes that we did not forsee as we made the parts. We the remade or redisigned the parts. One thing that we had to change for a lot of the parts is their thickness because many pieces would snap off or bend.

## Discussion of problems, errors, miscalculations, and missteps and how you overcame them

Our first big roadblock was designing a valve that would fit all of our needs.  We came up with a bunch of individual valve ideas that used different methods of holding the air inside of the balloon, but a lot of them we found flaws that would make them impossible for us to set it up, unable to retain the helium, or they couldn't reseal after we release an amount of air (Which was a requirement for them to be usable for us). 

The big overarching problem with our whole porject was that there was a severe weight limit since a helium balloon can only lift a tiny amount of weight. because of this problem we got larger balloons so that they could lift more, while at the same time we minimized the additional weight added by the unessential peices of our project. after making everything as small as possible we still discovered we would need an extra balloon to be able to lift our payload. This also brought another problem, when we reduced the materials we made everything as thin as was prudent and this caused our wall and supports to be thin, flexible, and weak. This meant some of our peices immeadiatly snapped off before we even got our hands on the actual 3D print. The way we overcame this was by thickening points that were especially weak, adding ribbing accross the roof where the rubber bands were adding strain, and making more secure backup features to the box that would function to keep everything together in case peices of our box failed.
