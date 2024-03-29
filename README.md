<br />
<div align="center">
  <a href="https://github.com/KevOneRedOne/TopGun_Fighter-Raspberry-Pi">
    <img src="assets/images/TOPGUN.png" alt="Logo" width="250" height="200">
  </a>

  <h3 align="center">TopGun_Fighter</h3>

  <p align="center">
    A small Arcade Game inspired by the movie TOP GUN
    <br />
    <br />
    <a href="https://github.com/KevOneRedOne/TopGun_Fighter-Raspberry-Pi/issues">Report Bug</a>
    ·
    <a href="https://github.com/KevOneRedOne/TopGun_Fighter-Raspberry-Pi/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#explanation-of-the-project">Explanation</a></li>
    <li><a href="#goals-of-the-project">Goals</a></li>
    <li><a href="#top-gun-fighter">TOP GUN FIGHTER</a></li>
    <li><a href="#how-to-play-the-game">How to play ?</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#additional-functionalities">Additional Functionalities</a></li>
    <li><a href="#future-improvements">Future Improvements</a></li>
    <li><a href="#hardware-and-software-requirements">Requirements</a></li>
    <li><a href="#sources">Sources</a></li>
  </ol>
</details>

<br>

<p align="center">
    <a href="https://github.com/KevOneRedOne/TopGun_Fighter-Raspberry-Pi" style="margin-right: 20px">
        <img height=400 align="center" src="assets/screen/game.png" />
    </a>
</p>

<hr>

## Explanation of the project

This project consists of creating a small **Arcade Game** containing a simple **1 VS 1 game**, using a **Raspberry Pi** and **buttons/joystick**.

The Project started on **16/05/2022**, and the submission date was set for on **13/06/2022**.

<hr>

## Goals of the project

First, the **creation of the 1 VS 1 game** with the **language** (I choose **Python and Pygame**) of our choice and with some **functionalities** like :
- **5 screens** :
  - Main menu screen
  - Game screen
  - Score screen
  - Instruction screen
  - Settings screen

- **2 players** with : 
    - Joysticks and Buttons (like PS4 controller)
    - Rotation speed : 360° rotation
    - Movement speed
    - Health 
    - Firepower
    - Shooting time
    - Projectile velocity

Then, importation of **our program into a Raspberry Pi Model 3B+** with the controllers plugged.

<hr>

## TOP GUN FIGHTER

This game is inspired by the **movie TOP GUN** and it is an **Air Battle Game** (player against player) ! 

The Goal for both players will be to destroy the opponent in a **DOG FIGHT**. 
Both Players has **bullets** and **missiles** to shoot and 100 point of health. | **Bullets** = 5 damages / 20 points | **Missiles** = 15 damages / 40 points. |

At the end of the game, the score of the winner will be save in a **json.file** (saves.json) and display on the Score menu.

### Game Screen
<p align="center">
    <a href="https://github.com/KevOneRedOne/TopGun_Fighter-Raspberry-Pi" style="margin-right: 20px">
        <img height=550 align="center" src="assets/screen/game.png" />
    </a>
</p>


### Menu Screen
<p align="center">
    <a href="https://github.com/KevOneRedOne/TopGun_Fighter-Raspberry-Pi" style="margin-right: 20px">
        <img height=550 align="center" src="assets/screen/menu.png" />
    </a>
</p>

<hr>

### How to play the game

To play **TOP GUN Fighter**, you must be **2 players** and have **2 controllers (PS4)**. You can also use the **keyboard !**

> **Note :** In the menu of the game you can find the controls and rules on the Instruction section

#### Player 1 Keyboard :

- **Z** : Move forward 
- **Q** : Rotation Left
- **D** : Rotation Right
- **LEFT SHIFT** : Bullets 
- **SPACE** : Missiles
#### Player 2 Keyboard :
- **UP ARROW** : Move forward 
- **LEFT ARROW** : Rotation Left
- **RIGHT ARROW** : Rotation Right
- **LEFT CTRL** : Bullets 
- **RIGHT SHIFT** : Missiles

#### Players controllers :
- **JOYSTICK_LEFT** : Rotation
    - **JOYSTICK_LEFT LEFT** : Left Rotation
    - **JOYSTICK_LEFT Right** : Right Rotation
- **JOYSTICK_LEFT** : Acceleration
    - **JOYSTICK_RIGHT UP** : Propulsion
    - **JOYSTICK_RIGHT DOWN** : Reduce Speed
- **L1** : Bullets
- **R1** : Missiles

<hr>

### Installation
In order to use our game, you have to **clone the repo** on the **desktop of the Raspberry Pi**:
#### Clone Repository
```console
git clone https://github.com/KevOneRedOne/TopGun_Fighter-Raspberry-Pi
```
#### Dependencies and Packages :
Make sure that **all dependencies are installed** on your computer or the Raspberry :
- Python 3 : ```python --version ``` or ```py --version ```
- Pip : ```pip --version```

Install **few packages** :
- pygame : ```py -m pip install -U pygame --user```
- pygame_menu : ```pip install pygame-menu -U```
- pygame usb : ```pip install pyusb``` and ```pip install libusb```


#### Run the Game
Then, go to the **file**:
```console
cd TopGun_Fighter-Raspberry-Pi/
```
And let's play the game !!
```console
python .\main.py 
```
Ou
```console
py .\main.py 
```

#### Run on Raspberry
#### Auto-run on Raspberry
On the **Raspberry Pi**, move the **topgun.desktop file** on the file **script** to the execution **shortcuts** :
```console
sudo mv ./topgun.desktop /etc/xdg/autostart/topgun.desktop
```
Then, the program will be executed on the login.

<hr>

### Additional Functionalities
- Score leader board
- Game runs at 100 fps (Adjust to 60 fps on the Raspberry Pi 3B+)
- Json file for the save of the score
- Keyboard and Joystick gameplay

### Future Improvements
- Timer for the Game 
- Improvement of the score system
- Sound Effects
- Settings screen with the personalization of :
    - Planes choices 
    - Speed and Firepower
    - Wallpaper
- Improve UX/UI design 

<hr>

### Hardware and software requirements :
##### Stacks :  <img align="center" alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" /> with <img align="center" alt="Pygame" src="https://img.shields.io/badge/Pygame-3776AB?style=flat&logo=pygame&logoColor=white" /> <img align="center" alt="Pygame-menu" src="https://img.shields.io/badge/Pygame_menu-3776AB?style=flat&logo=pygame&logoColor=white" /> <img align="center" alt="Pyusb" src="https://img.shields.io/badge/Pyusb-3776AB?style=flat&logo=usb&logoColor=white" />
##### Raspberry Pi or PC : <img align="center" alt="Raspberry" src="https://img.shields.io/badge/-RaspberryPi-C51A4A?style=flat&logo=Raspberry-Pi" /> or <img align="center" alt="PC" src="https://img.shields.io/badge/Windows-0078D6?style=flat&logo=windows&logoColor=white" /> <img align="center" alt="PC" src="https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black" /> <img align="center" alt="PC" src="https://img.shields.io/badge/MAC%20OS-000000?style=flat&logo=macos&logoColor=F0F0F0" />

##### Controllers : <img align="center" alt="PS4" src="https://img.shields.io/badge/PS4-%230070D1.svg?style=flat&logo=Playstation&logoColor=white" /> <img align="center" alt="XBOX" src="https://img.shields.io/badge/XBOX-%23107C10.svg?style=flat&logo=xbox&logoColor=white" />


<hr>

### Sources 
To succeed in making our project, we had to resource ourselves on the net, here are some of the resources we used :

- Python docs : https://www.python.org/
- Pygame docs : https://www.pygame.org/docs/
- W3schools : https://www.w3schools.com/python/
- Techwithtim tutorials : https://www.techwithtim.net/tutorials/
- Inspiration for my game : https://andrew-gg.itch.io/spacewar-top-gun
- PS4 Controller Tuto : https://github.com/anubisankh/dualshock4-python
- Pygame Joystick : https://runebook.dev/fr/docs/pygame/ref/joystick
- Pygame Menu : https://pygame-menu.readthedocs.io/en/4.2.8/index.html
- Raspberry Pi Docs : https://www.raspberrypi.com/documentation/



