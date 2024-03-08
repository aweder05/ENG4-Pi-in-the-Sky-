# **ENG4-Pi-in-the-Sky**

### Repository Authors: Sophie Chen, Anton Weder

---
&nbsp;


## Table of Contents

* [Section 1: Planning](Section_1:_Planning)
    * [Initial Ideas](Intitial_Ideas)
    * [Choice of Project](Choice_of_Project)
    * [Diagrams](Diagrams)

&nbsp;

&nbsp;

## **Section_1:_Planning** 
---

### **Initial_Ideas**

Below is a list of possible project ideas, and a list of pros/cons for each to help us reach a consensus on which project idea would be the best fit for us. 
* GPS Tracker on a Balloon
    * Pros: 
    * Cons: 
* Some sort of Projectile Launcher
    * Pros: Easy to Test, not expensive, no forseeable insane-level code
    * Cons: Difficult to Build
* DC Motor Plane
    * Pros: Easy to Test, simple enough electronics
    * Cons: Complicated math, have to account for weight everywhere 

### Choice_of_Project

**PID Steered Flyer**:We are going to make an flyer that is powered by a motor, and uses PID to stay stable. We will use the Rasberry-Pi to collect the tilt data.

**Why**: The airplane will be complicated because we are putting individual aspects of engineering we've learned, together. We chose this project because we are applying what we've learned in our engineering courses to build something really cool.

### Research
* [How to Make Cheap Single Cell Battery Powered RC Airplane.. Homemade Airplane
](https://www.youtube.com/watch?v=JX_KkInFhow)

### Important_Resources
[Crash Avoidence Light + Power](https://github.com/sechen12/Engineering_4_Notebook/blob/main/raspberry-pi/Crash_Avoidance_Light%20%2B%20Power.py) - Code for the calculating the tilt with an MPU, and the Pico sending an output depending on the conditions.

[Data Storage](https://github.com/sechen12/Engineering_4_Notebook/blob/main/raspberry-pi/Data_Storage) - Code for storing the data

### Schedule 
[Google Calendar](https://calendar.google.com/calendar/u/0/r/month/2023/12/1?pli=1)

### Materials
**Hardware:**
- 9gr Micro servos
- 5gr Micro servo
- 18650 3.7V Battery
- 18650 Charger

**Non-electronics:**
- 5mm kraft foam board
- 3mm insulation foam
- 2mm balsa sheet
- 108mm Propellers (CW&CCW)
- Hot melt Glue Gun
- Cable Tie
- 1.2mm Pushrods
- Servo control horn

**5mm kraft foam board**
- Body
- Horizontal stabilizer
- Vertical stabilizer

&nbsp;
-----

## Code Criteria

Setup: 
- Define pins MPU Accelerometer
- Define pins for DC Motor 

Loop:
- Create Switch for DC Motor 
- Run DC Motor When Switch is turned on
- Run DC Motor for set time (acting as a booster for the glider)
- Collect Data from the Accelerometer and store it on the PicoW

## Code Flow Chart

Here is a flowchart to help us with our coding: 
##### Note, the PID Section is not part of our success statement, and this Flow Chart will most likely change over the course of our project

<img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/blob/main/media/Screenshot%202023-12-15%20102348.png?raw=true" >

### Diagrams
|  |  |
| :------------ | :------------- |
| <img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/2eb1dab3-be66-484a-af29-30a4690398e1" width="170" >  |  <img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/10bc984d-8906-4312-901a-ed7aba2ddeba" width="300"> |
| <img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/c516aa95-9e0c-4a22-ad81-20b906b10a0d" width="400" > | <img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/1cf55f83-0eb0-4559-90e1-859e643a86b1" width="300" >

----



### Success_Statement

The project will be considered a success if the flyer is turned on with a switch and will store the tilt data onto the Pico so that it can be presented on the computer. An extra bonus will be having the flyer be controlled with PID so that it can hopefully remain in flight for an extended amount on time.

----

# **Log of Documentation**
---- 
----
### **CAD Basics** 01 / 03 / 2024

Although part of the project will be fabricated using the laser cutter machine, most of the project will be handmade. We rendered our project in CAD with the intent of visualising what our final project will look like, and to find the mass of the projectile (without the electronics). The CAD was simple to design; sketches, extrudes and mate connections were the only tools used to render the plane. We plan on laser cutting the supports found under the wing that have the functions of both catching air, and providing a frame to the foam.

| | | 
|--|--|
|<img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/c04934d3-edcc-4803-aca9-d20b86aa0998" width="400">|<img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/720cd691-01dd-445a-b89f-15d2ac071839" width="400">
|


### **Early Prototypes and Fabrication** 01 / 03 / 2024
---

Today was the first day back from break, and we knew that we needed to get to work as quickly as possible. On our to do list for this week was to begin fabricating our project. The first thing that we did when coming into class was to look for building materials for our plane. Building a plane, we knew that materials needed to be light, flexible, and easily cut to exact specifications.

| | | |
|:---|:---|:---|
|<img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/b62c4b89-db32-438e-b277-32ca9b496c0c" width="200"> | <img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/b9ebb8d3-4bc0-4992-8942-df8d15c81e0d" width="105"> | <img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/3b065b6e-d142-4e0f-b96c-e14e6fe33f28" width="200"> | 

The above images show our first attempt at creating the inner structure of the wing. I took some inspiration from Dylan Halbert and Grant Gastinger's project where they used the same building techniques. These techniques involved putting holes into the wing supports in order to make them more sturdy and rigid, but still horizontally flexible, with respect to the wingspan. 

Our first attempt at fabricating this was using balsawood, since is light and relatively flexible and sturdy, especially when only cutting a small area such as ours. This turned out to unfortunately not work in our favor as the balsawood burned a lot more under the laser. We then decided to still use wood, but a more dense wood and wood that would not as easily burn up.

----

### **Coding** 01 / 17 / 2024

Coding so far has been difficult. The code currently doesn't work, but one thing that was probably important was having the proper libraries imported into our lib folder so that we don't have to write all the code from scratch.

*two minutes later*

Anton got the code working! After deleting the line ``sensor.sealevel_pressure = 1013.2``, the code started printing the tempature, pressure and altitude values. The line Anton deleted states what the pressure at sea level is so that the computer could be calibrated to calculate the altitude, therefore the altitude that is being printed is wrong - this is our next problem to figure out.

### **Coding and wiring** 01 / 18 / 2024

Today Anton and Mr. Miller figured out why the code wasn't working: the altimiter is able to detect a change in altitude, but is incapable of printing exact altitude values. 

We also soldered the battery, motor, and switch together so that we could build our prototype. We have no control over the motor, but our next steps are assembling the prototype, and start fabricating the final project!

### **Prototype creation** 01 / 24 / 2024

| | | |
|:---|:---|:---|
|<img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/e110b571-a278-454b-839d-19cfaf43fc82" width="200"> | <img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/90e3dc50-67a0-43b3-94af-f94d4892da26" width="200"> | <img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/3008a10c-71ac-4544-830c-2221f8cc52d0" width="200"> |

###### In the above image, you can see how we mounted our three components (battery, switch, and motor) to the plane. The battery and all of the wiring is encased under the hollowed out black section of the cockpit.)

&nbsp;


Today we finished creating the prototype. We used a pre-made plane from Anton, and carved the cockpit out so that the wiring and batter could fit. We then mounted the motor and switch, and taped everything neatly. Finally, we attached the propellor. Before we taped everything down, we had to solder the motor, battery and swich together (the direction didn't matter, just that it creates a complete circuit). Our next steps are getting the foam, and starting to fabricate the final project. It is also important to note before the end of this entry that we will have to figure out a way to reverse the direction of our motor, so that it doesn't end up going in the wrong direction or so that it doesn't crash completely. We will also have to pay great attention to detail when distributing the weight accross our aircraft. The original toy plane had a small metal ball in the front of the plane, in order to keep a consistent direction, but the addition of the battery and the motor is of course greater than this initial metal ball, so we will have to adjust the weight of the rest of the plane accordingly when going through the final fabrication process. 

&nbsp;

----

### **Altimeter Test Code 90% Working** 01/24/2024

Today, we finally accepted that the altimeter not being able to pinpoint our exact altitude would not be a huge problem for us. It is able to detect changes in altitude perfectly, and to a degree that will satisfy our needs. The only place where we "cheated" a little bit was when I added the `+150` on top of     `print(f"Altitude: {sensor.altitude +150}")` so that it would match the altitude of Charlottesville High School. This "+" value will most likely change day to day because of how the altitude is calculated through pressure, and because pressure can change due to a number of various factors, including weather. (When humidity increases, air pressure decreases, and vice versa.)

**Here is a link to the [altimertest.py](https://github.com/aweder05/ENG4-Pi-in-the-Sky-/blob/main/code/altimitertest.py) code.**
###### For space management purposes, this code can be accessed by pressing the link provided above. 


## **Altimer Data Storage Locally on Pico** 1/25/24

After we've completed the test code for the altimeter, to make sure that we could actually use the altimeter in our final project. The tricky part that we had in front of us, after completing the test code, was to make sure that we would be able to store all of the data locally on the pico. This is a necessity since our project will of course not be connected to a computer, so everything will have to be battery powered and independent. The tricky part initially was to go through the whole process of Data Storage Part 1 and to recycle it for the altimeter. Where we ran into issues was when we couldn't find the data.csv file in our CircuitPy folder on the computer's file explorer. At first, we were confused, since the line `with open("/data.csv", "a") as datalog:` should actually create a new data.csv file in the Pico's storage. 

Eventually we figured out that the reason out program wasn't working properly was we WEREN'T RUNNING IT THROUGH CODE.PY!!! This is by far the most frustrating reason your code may not run. The battery was also on while we were in "code mode", so that computer was getting confused as to where the power source was coming from. I also had to restart my computer so that the code would run. There is also a process of saving the code to the board, so that when the Pico is switched into "data mode", the Pico will save the data onto the board, so that when switched *back* into "code mode", we can go into our data file, that should be stored in you Circuit Python D-drive, the data will be displayed in a table.

**Here is the process from saving the code to the board, to then seeing the data stored in you D-drive:**
- Switch board into "code-mode, so that *you* are in control - the Pico should blink 3 times, slowly (this signals that the board is in "code mode")
    - The board should be plugged into your computer at this point, and the battery should be off. If the battery is on, sometimes the computer gets confused as to where the power source is coming from
- Do you code and run it so that the code is stored onto the board
- Unplug the Pico from the computer, turn on the battery. and move the Pico in a motion that the sensor is designed to detect
    - The Pico shoudl reset and blink quickly 10 times. This signals the board is in "data mode"
- Before plugging the Pico back into the computer, turn your battery off, and switch back into "code mode" (you cannot open you D-drive without being in "code mode")
- The data file should be in you D-drive, and when you open it, the values you wrote to store should appear

Code link is [**here**](https://github.com/aweder05/ENG4-Pi-in-the-Sky-/blob/main/code/altimitertest%20copy.py)

Now that we have our base code working, we are going to start working on fabrication. We went to Michael's and bought thin foam to use as the material to go onto the wings. We have pretty much finalized the desgins for the final project, so we just have to build it.

## **Wing Frames** 2/2/24


| | | 
|:--:|:--:|
|<img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/ed813621-dbd2-405c-afb9-a3c058ee1313" width="300"> |<img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/e8d68e13-61f1-43c9-8ded-4aed2ef74ce7" width = "400">
 | 

Today we finished fabricating the frames for the wings. Unfortunately, we used hot glue to adhere the wing supports to the laser-cut wood pieces. We could have used friction fit to keep the wood pieces in place, but the quickest, most effective way to adhere the pieces was using hot glue.

----
&nbsp;

## **02/07/2024 Wiring Diagram completed to begin soldering final circuit** 

Today was a very productive day, as we finally were able to get an idea of how our final wiring would look like. Using fritzing, we were able to get our exact components imported into the program, and provide ourselves with an accurate template to use while we solder on the headers, switch, altimeter, and battery accessories onto the Pico Cowbell attachment. 

Here is an image of the wiring diagram:

<img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/blob/main/media/finalwiring.png?raw=true" width="600">

Once we start soldering, we can get a good idea of how all of the components fit onto our plane, and we can finally begin fabricating the fuselage.

## **02/14/2024 Soldering Progress and final CAD Planning** 

One week later, and we've made some good progress. Soldering is almost complete, and testing of the final circuit will hopefully start next week. If the circuit doesn't work, it'll suck, but we still have plenty of time to fix any possible issues. While soldering, we started to get a good idea of how we will implement the electronics into our plane. After doing some research, we've noticed how important it is to find our plane's center of mass, lift, and gravity, in order to make sure that it doesn't stall or go into a nosedive straight into the floor. 

The tricky thing about soldering on such a small circuit board, along with integrating multiple components, is that at a certain point wires will begin to overlap and make it hard to fit anything new onto the PiCowbell module. Even though we didn't have a ton of components, it was enough to where we had to be really careful with our soldering, and make sure we wouldn't blow everything up. Soldering takes a substancial amount of concentration, so it's good that at least one person in our group is good at it.

## **3/7/24 Soldering Update and last CAD polishing planned** 

Unfortutely, with our project coming along so well, we were bound to run into an obstacle at some point. For us, that obstacle came in the form of soldering. Our lack of experience soldering such circuits really proved to be our greatest issue, as we spent multiple class periods which would've been better suited for other work. 

As we started soldering, things were going very well, but then once we had to start testing the different components, we kept running into little problems that ultimately cost us a lot of valuable time fixing. Our main issue was with wiring some components, such as the battery, to the wrong power input/output. Fixing this was not super hard, but all of the little fixes built up after time, and we had to eventually scrap our first prototyping PiCowbell and start again on a new one. 

Today is a very special day for our soldering journey, as we finally got the board t switch between code and data mode; something that we had really struggled with in the past. The fix for this problem was really, really stupid. On VS Code, we had a boot.py file open for a different board than the one that we were using. This meant that that on the actual board that we were using, the switch that was wired to GP0 was coded to be wired to GP1. Fortunately, this was a very easy fix, but frustrating nonetheless.

## **3/8/24 Final Soldering**

![unnamed](https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/a99a0d29-159e-4f6e-86e4-6746853eca4f)
![unnamed](https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/c289cb91-58e6-45d3-ba06-5bc50a24df75)
![0](https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/863dfc89-9e25-4524-a785-f477e01fd8fe)

