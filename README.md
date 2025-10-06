This is a Open CV project. I made this following a mixtue of tutorials from FreeCodeCamp and other places that i dont remeber.

This game is inted to be played 1 player or 2 player. Do note that when you play 2 player you will need to you your right hand for the right side and left for the left side. 
To control the paddles you make your hand into a fist and the paddles will apear. Move your fists up and down to control them.

The Line from your index finger to your thumb helps you see the distance when the distance is small (keep moving your fingers around till it happens sometimes it buggs) it will make the side of the screen for the other player/ side white so that they can not see. 

Nothing happens when te ball goes behind the paddle, it wil just end up bouncing somewhere else. The goal is to hit the ball the most times before the timer runs out. When the timer runs out it will show you who won.

Coins if you hit a coin with the ball both players get 5 coins.


<img width="928" height="749" alt="image" src="https://github.com/user-attachments/assets/783e5d38-5d4f-4eab-8f1b-7ce243c6363b" />

# BUGS
If the window gets stuck press q

If no camera shows that is beacuse it is programed to use your laptop camera, if you really want to play it you can go into the code and change this line 
cap = cv.VideoCapture(0) to something like cap = cv.VideoCapture(1) or 2 this will use your external camera.



