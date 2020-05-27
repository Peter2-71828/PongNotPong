# HandNotHand
Makers onsite final project    
Cohort: January 2020  
Start: 30/03/2020  
End: 09/04/2020
### Team Members</h3>
<li>Paulo
<li>Ziad
<li>David
<li>Peter

## Table of Contents

* [Description](#description)
  * [Game Play Video](#game-play-video)
  * [Overview](#overview)
  * [MVP](#mvp)
* [How To Use](#how-to-use)
* [Technologies](#technologies)
* [Project Structure](#project-structure)
* [Future Improvements](#future-improvements)

## Description

### Game Play Video
[![Pong](https://img.youtube.com/vi/XgSwKFBHiGE/0.jpg)](https://youtu.be/XgSwKFBHiGE)

### Overview
As a team of 4 we designed and built a simple, single player pong game. The game utilises hand tracking, achieved through computer vision, as the primary means of user input. The project was initially completed in 11 days and no member of the team had previous experience with the primary technologies involved.

### MVP
Build a program that is to be able to recognise  
a body part and  utilise it as a user input for a game

## How to Use

* clone or fork this repo
* ensure you have both python and conda installed and are runing the corect version indicated in the [Technologies](#technologies) section
* navigate to the root directory of the repo, PongNotPong  
* run:   
``conda env create -f environment.yml``  
``conda activate PongNotPong``
* to launch the game run ``python app.py``

## Technologies

Python 3.7.7
Conda 4.8.3
OpenCV

## Project Structure
```
+-- pong_game
|   +-- window.py
|   +-- paddle.py
|   +-- projectile.py
|   +-- player.py
|   +-- user_in.py
|   +-- menu.py
+-- _tracking
|   +-- objectTracker.py
|   +-- centroidTracker.py
+-- _detection
|   +-- model
|   +-- deploy.prototxt
+-- _README.md
+-- _environment.yml
```

## Future Improvements

If the game was to be developed further the following might be a good place to start:

* Maintain aspect ratio while scaling
* Prevent projectile projectile entering scoring area when extreme rescaling
* Improve cpu
* Create two player local and or online multiplayer
* Write tests, especially important if the project was to be progressed any significant amount further
