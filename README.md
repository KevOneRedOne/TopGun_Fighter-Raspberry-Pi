# TopGun_Fighter--Raspberry-Pi

## Explination of the project

This project consists of creating a small **Arcade Game** containing a simple **1 VS 1 game**, using a **Raspberry Pi** and **buttons/joystick**.

The Project started on **16/05/2022**, and the submission date was set for on **13/06/2022**.

<hr>

## Objectifs

First, the **creation of the 1 VS 1 game** with the **language** (I choose **Python and Pygame**) of our choice and with some **functionalities** like :
- **5 screens** :
  - Main menu screen
  - Game screen
  - Score screen
  - Instrucion screen
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

## The game : TOP GUN FIGHTER

This game is inspired by the **movie TOP GUN** and it is an **Air Battle Game** (player against player) ! 

The Goal for both players will be to destroy the opponent in a **DOG FIGHT**. 
Both Players has **bullets** and **missiles** to shoot and 100 point of health. | **Bullets** = 5 damages / 20 points | **Missiles** = 15 damages / 40 points. |

At the end of the game, the score of the winner will be save in a **json.file** (saves.json) and display on the Score menu.

### Game Screen
![image](assets/screen/Screen1.png)
### Menu Screen
![image](assets/screen/menu.png)




### How to play the Game ?

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

#### Players contollers :
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
#### Dependancies and Packages :
Make sure that **all dependancies are installed** on your computer or the Rasberry :
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

#### Autorun on Raspberry
On the **Raspberry Pi**, move the **topgun.desktop file** on the file **script** to the execution **shortcuts** :
```console
sudo mv ./topgun.desktop /etc/xdg/autostart/topgun.desktop
```
Then, the program will be executed on the login.

<hr>

### Additionnal Functionalities
- Score leaderboard
- Game runs at 60 fps
- Json file for the save of the score
- Keyboard and Joysick gameplay

### Future Improvements
- Timer for the Game 
- Improvement of the score calcul
- Sound Effects
- Settings screen with the personnalization of :
    - Planes choices 
    - Speed and Firepower
    - Wallpaper
- Improve UX/UI design 

<hr>

### Hardware and software requirements :
#### Object-oriented programming language :
![image](assets/screen/python.png)

#### Raspberry Pi Model 3B+ or later :
![image](assets/screen/Raspberry.png)

#### PS4 Controller or XBOX controller :
![image](assets/screen/ps4.png)

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



