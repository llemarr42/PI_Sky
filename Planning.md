# Table of Contents
* [Initial Ideas](#Options_for_Project)
* [Final Idea Description](#Final_Idea_Description)
* [Schedule](#Schedule)
* [Code](#Code)
* [Bill of Materials](#Bill_of_Materials)
* [Risk Mitigation](#Risk_Mitigation)

# Options_for_Project

## Balloon

### requirements / description

A balloon filled with helium that is carrying a payload.

The balloon should be able to carry the weight of said payload and be able to rise. Once at a certain height, the Pi will do some action to begin descent (pop balloon, slowly let air out of balloon, separate Pi from balloon). The Pi will be collecting data on acceleration and position for the duration of the flight. Additionally, the Pi might take photos or collect data on temperature, humidity, or other undetermined variables. 

### Materials:

* Pi

* accelerometer

* balloon

* helium

* Pi camera

* Capsule / shell


### pros
* Easy to launch/simple flight mechanisms
* Good for taking photos because the camera can be mounted in the same direction for the duration of the flight
* Long flight time means more time to collect data (as opposed to a rocket or the like)

### cons
* How are we getting helium?

### other things to consider
* We have to have a very reliable system of descent, otherwise we will lose the Pi
* If the system of descent involves destroying or losing the balloon, we will have to buy a LOT of balloons
* Every descent will also cost helium of which we will have a limited supply

## Monocopter

### requirements / description

This project should use a single central propeller to lift the project in a vertical direction. 

The motor that controls the blade needs to have enough lifting force to be able to cause the project to have the ability to fly up to a certain height then once reaching that height, the blades will slow to a speed that in which the project remains in place save for drifting horizontally then after x amount of time the blades will further slow as to make the project descend in a controlled manner. During this process the pi will be taking photos and recording specific data that is yet to be determined.

### Materials
* A High quality motor that is good for what we need??? (lightweight, small, but powerful)
* Pi
* Accelerometer 
* 3D print material / wood (depending on project design)
* Pi camera
* Equipment for measuring data


### pros
* This project is in a class by itself and majestic (thanks to thesaurus.com)
* Challenging but plausible
* We will have more control of where this goes, when it goes back down, and how fast this goes (depending on what type of monocopter) 
### cons
* Not sure how it would work/if it is realistically feasible
* If we choose this we will risk not being able to complete the project by the due date
* We will only have one attempt for printing and stuff as it will be too big to reprint it or change things after the fact (wood will lessen this problem)
 
## Slingshot Launch
### requirements / description

Use one of the slingshots used for the eggdrop project to launch a pi, which could:

Take a picture when it is facing the ground
Graph the path of its flight

### Materials

* Capsule
* Pi
* Accelerometer
* Slingshot 

### pros

* Less complicated launch, more able to focus on what it does in air
* No outside materials needed for launch

### cons

* Needs to be very compact and self-contained
* Would reach lesser altitudes compared to other projects
* The need for it being self-contained could cause complications in the landing process


# Final_Idea_Description
![Balloon Sketch](https://user-images.githubusercontent.com/56133021/153914634-e4c85cc6-e7c0-4b35-9668-a57851be1035.jpg)

The payload will be carried by one or more helium-filled balloons. After a certain amount of time, a valve on one of the balloons will open, allowing helium to escape, causing the balloon to gradually fall back to the ground. 

![Payload Sketch](https://user-images.githubusercontent.com/56133021/153914636-ff04dcfc-bae6-472b-84f4-7edfaefea691.jpg)

The payload will consist of a Raspberry Pi, Raspberry Pi camera, temperature and humidity sensor, servo, battery, and an on/off switch. The payload will be contained by a thin 3D printed casing and attached to the balloon(s) with light netting. During its flight, the Pi will take photos of the ground, record the temperature and humidity, and control the helium levels. The valve will work in one of several ways, but will be controled by a servo (ideas sketched below).

![Valve Ideas](https://user-images.githubusercontent.com/56133021/153914632-c87b205c-47ad-4936-98ec-13a5f4c2b97d.jpg)

# Schedule
* 2/21/2020 through 3/11/2022: Design the valve
* 3/14/2022 through 3/25/2022: Design the capsule
* 3/28/2022 through 4/1/2022: Write the code
* 4/4/2022 through 4/22/2022: Test and revise

# Code

start timer when button is pressed

measure altitude with accelerometer

periodically measure tempature and humidity

save data results along with timestamp and altitude

after a certain time has passed since freed the helium is released

stop helium flow when project begins accelerating downward

turn off pi when button is pressed



# Bill_of_Materials

per one run:
* Latex balloon(s)
* ~ 3 cubic feet of helium (max)
* Light netting
* Raspberry Pi zero
* Battery 
* PowerBoost 500C
* Pi Camera
* Continuous rotation servo
* Temperature/humidity sensor
* Small switch
* 3D printed casing
* Valve to control airflow

We wll need to refill the helium each run.

# Risk_Mitigation

 We will release the balloon in an area with little trees or power lines to mitigate the risk of entanglement. We will test the release mechanism by blowing up the balloons by hand instead of helium. We will test how fast the balloon ascends by tying a string to the balloon and releasing it, and measuring how fast the string is pulled. Because we are limited by weight, there is little we can do in terms of padding to prevent damage if the balloon somehow pops.

