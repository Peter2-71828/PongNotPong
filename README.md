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
* [How To Use](#how-to-use)
* [Project Structure](#project-structure)
* [User Stories](#user-stories)
* [Technologies](#technologies)
* [Future Improvements](#future-improvements)

## Description

The MVP for our project is to be able to recognise  
a body part and have it utilise it as a user input for a game

## User Stories

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

## Technologies

Python 3.7.7
Conda 4.8.3
OpenCV

## How to Use

* clone or fork this repo
* ensure you have both python and conda installed and are runing the corect version indicated in the [Technologies](#technologies) section
* navigate to the root directory of the repo, PongNotPong  
* run:   
``conda env create -f environment.yml``  
``conda activate PongNotPong``
* to launch the game run ``python app.py``

## Future Improvements

If the game was to be developed further the following might be a good place to start:

* Maintain aspect ratio while scaling
* Prevent projectile projectile entering scoring area when extreme rescaling
* Improve cpu
* Create two player local and or online multiplayer
* Write tests, especially important if the project was to be progressed any significant amount further
