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

### **Initial Ideas**

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


### **Success_Statement**

### Diagrams
|  |  |
| :------------ | :------------- |
| <img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/2eb1dab3-be66-484a-af29-30a4690398e1" width="170" >  |  <img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/10bc984d-8906-4312-901a-ed7aba2ddeba" width="300"> |
| <img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/c516aa95-9e0c-4a22-ad81-20b906b10a0d" width="400" > | <img src="https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/1cf55f83-0eb0-4559-90e1-859e643a86b1" width="300" >

----

![sexy flick 1](https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/c04934d3-edcc-4803-aca9-d20b86aa0998)
![sexy flick 2](https://github.com/aweder05/ENG4-Pi-in-the-Sky-/assets/112981481/720cd691-01dd-445a-b89f-15d2ac071839)

### Success_Statement

The project will be considered a success if the flyer is turned on with a switch and will store the tilt data onto the Pico so that it can be presented on the computer. An extra bonus will be having the flyer be controlled with PID so that it can hopefully remain in flight for an extended amount on time.





&nbsp;

&nbsp;

&nbsp;



