# PI_Sky
Pi in the sky project
.

## Materials used
Because the goal of this project was to lift a payload into the sky, we had to aim to keep our payload as light as possible. A light payload minimizes the amount of work our design has to do to overcome gravity. Therefore, we were conscientious about materials we used and what we were adding to our payload. We made our payload container out of 3D printed material as opposed to acrylic because the 3D printed filament is lighter than acrylic and having a more customizable box can lower the amount of material needed in its thickness and shape. Our payload container holds all of our necessary electronics: the Raspberry Pi, battery, Pi camera, servo, accelerometer, on/off switch, and wiring. It also houses a 3D printed spool and string as well as a 3D printed plug. To lift the payload, we are using a large latex balloon and helium. 

## CAD renderings

![balloon_](https://user-images.githubusercontent.com/56924009/170523966-5f947796-b087-4268-bb39-d09f454969da.PNG)





![Balloon_2](https://user-images.githubusercontent.com/56924009/170523982-3d9e8043-6101-4f8d-a412-942f798ea53d.PNG)


## Actual photos and/or video (well lit and in focus)

## A diagram of your circuit

![Circuit](https://user-images.githubusercontent.com/60944294/170525997-beada2d2-2537-4bdd-9b0a-c7a35084f0e8.PNG)

## Commented code

## Description of the planning that went into the project, design decisions, and engineering details
Our biggest initial decision was how to design the valve which controls the flow of helium out of the balloon. The valve had to balance being light, fairly simple, easy to control, and reliable. It also had to be able to open AND close. We came up with many designs and after creating three of them in CAD, we decided to go with a plug design which would be pulled down by a string and held in place by some sort of elastic or spring force. 


## Your process or a schedule of how you spent your time


* 2/21/2020 through 3/11/2022: Design the valve: We created and discarded multiple different disigns of valvles in order to find something that fufills all of our needs. This was one of the harder and more time consuming. 
* 3/14/2022 through 3/25/2022: Design the capsule
* 3/28/2022 through 4/1/2022: Write the code
* 4/4/2022 through 4/22/2022: Test and revise

## Discussion of problems, errors, miscalculations, and missteps and how you overcame them

Our first big roadblock was designing a valve that would fit all of our needs.  We came up with a bunch of individual valve ideas that used different methods of holding the air inside of the balloon, but a lot of them we found flaws that would make them impossible for us to set it up, unable to retain the helium, or they couldn't reseal after we release an amount of air (Which was a requirement for them to be usable for us). 

The big overarching problem with our whole porject was that there was a severe weight limit since a helium balloon can only lift a tiny amount of weight. because of this problem we got larger balloons so that they could lift more, while at the same time we minimized the additional weight added by the unessential peices of our project. after making everything as small as possible we still discovered we would need an extra balloon to be able to lift our payload. This also brought another problem, when we reduced the materials we made everything as thin as was prudent and this caused our wall and supports to be thin, flexible, and weak. This meant some of our peices immeadiatly snapped off before we even got our hands on the actual 3D print. The way we overcame this was by thickening points that were especially weak, adding ribbing accross the roof where the rubber bands were adding strain, and making more secure backup features to the box that would function to keep everything together in case peices of our box failed.
