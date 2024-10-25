#Source

import turtle
import math
import random
import winsound
    
#setting up the screen
wn = turtle.Screen()
wn.bgcolor("purple")
wn.bgpic("space invaders.gif")
wn.title("Space Invaders")
border = turtle.Turtle()
border.speed(0)
border.penup()
border.color("white")
border.setposition(-200, 200)
border.pendown()
border.pensize(3)
for i in range(4):
    border.fd(400)
    border.right(90)
border.hideturtle()

#making the player
turtle.register_shape("player.gif")
player = turtle.Turtle()
player.color('white')
player.penup()
player.speed(0)
player.setheading(90)
player.shape('player.gif')
player.setposition(0, -150)

#moving the player left and right
player_speed = 15
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -180:
        x = -   175
    player.setx(x)
def move_right():
    x = player.xcor()
    x += player_speed
    if x > 180:
        x = 175
    player.setx(x)

    
#creating the weapon
wepon = turtle.Turtle()
wepon.color("yellow")
wepon.penup()
wepon.setheading(90)
wepon.speed(0)
state = "ready"
wepon.hideturtle()
wepon_speed = 17
wepon.setposition(1000,1000)

#firing wepon
def shoot():
    global state
    if state == "ready":
        state = "firing"
        x = player.xcor()
        y = player.ycor() + 10
        wepon.setposition(x, y)
        wepon.showturtle()
        winsound.PlaySound("344310__musiclegends__laser-shoot.wav ", winsound.SND_FILENAME)
        
#creating the enemies
turtle.register_shape("Invader.gif")
enemy = turtle.Turtle()
enemy.speed(0)
enemy.penup()
enemy.shape("Invader.gif")
enemy.setheading(270)
enemy.color("red")
enemy.setposition(random.randint(-200, 200), 180)
enemy.shapesize(0.25, 0.25)
descending = 40
enemy_speed = 2

enemy2 = turtle.Turtle()
enemy2.speed(0)
enemy2.penup()
enemy2.shape("Invader.gif")
enemy2.setheading(270)
enemy2.color("red")
enemy2.shapesize(0.25, 0.25)
enemy2.setposition(random.randint(-200, 200), 140)
descending = 40
enemy_speed = 2

enemy3 = turtle.Turtle()
enemy3.speed(0)
enemy3.penup()
enemy3.shape("Invader.gif")
enemy3.setheading(270)
enemy3.color("red")
enemy3.shapesize(0.25, 0.25)
enemy3.setposition(random.randint(-200, 200), 100)
descending = 40
enemy_speed = 2

#collition
def collition(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return turtle
    else:
        return False
collition_count = 0
collitions_required = 5

#scoring
score_pen = turtle.Turtle()
score_pen.penup()
score_pen.color("white")
score_pen.setposition(-180, 180)
score = 0
score_string = "score: %s" %score
score_pen.write(score_string, False, align = "left", font = ("Arial", 10, "normal"))
score_pen.hideturtle()

#win and lose statements
you_lose = turtle.Turtle()
you_lose.penup()
you_lose.hideturtle()
you_lose.color("white")
you_win = turtle.Turtle()
you_win.penup()
you_win.color("white")
you_win.hideturtle()
    
#keyboard setting
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(shoot, "space")

#main game loop
while True:  
    #moving the enemies
    x = enemy.xcor()
    y = enemy.ycor()
    x += enemy_speed
    enemy.setx(x)
    if x < -175:
        enemy_speed *= -1
        y -= descending
        enemy.sety(y)
    elif x > 175:
        enemy_speed *= -1
        y -= descending
        enemy.sety(y)
    elif y < -150:
        you_lose.write("You Lose!", False, align = "center",font = ("AR DARLING", 50, "normal"))
        break
    
    x = enemy2.xcor()
    y = enemy2.ycor()
    x += enemy_speed
    enemy2.setx(x)
    if x < -175:
        enemy_speed *= -1
        y -= descending
        enemy2.sety(y)
    elif x > 175:
        enemy_speed *= -1
        y -= descending
        enemy2.sety(y)
    elif y < -150:
        you_lose.write("You Lose !", False, align = "center",font = ("AR DARLING", 50, "normal"))
        break
    
    x = enemy3.xcor()
    y = enemy3.ycor()
    x += enemy_speed
    enemy3.setx(x)
    if x < -175:
        enemy_speed *= -1
        y -= descending
        enemy3.sety(y)
    elif x > 175:
        enemy_speed *= -1
        y -= descending
        enemy3.sety(y)
    elif y < -150:
        you_lose.write("You Lose!", False, align = "center",font = ("AR DARLING", 50, "normal"))
        break    
    
    #making the wepon move upwards
    y = wepon.ycor()
    y += wepon_speed
    wepon.sety(y)
    
    #stopping the wepon from going out
    if y > 195:
        state = "ready"
        wepon.hideturtle()
    
    #collition calls
    if collition(wepon, enemy):
        global collitions_count
        wepon.hideturtle()
        state = "ready"
        enemy.setposition(random.randint(-100, 100), 180)
        collition_count += 1
        #Score change
        score += 5
        score_string = "Score: %s" %score
        score_pen.clear()
        score_pen.write(score_string, False, align = "left", font = ("Arial", 10, "normal"))
        
    elif collition(wepon, enemy2):
        global collitions_count
        wepon.hideturtle()
        state = "ready"
        enemy2.setposition(random.randint(-100, 100), 180)
        collition_count += 1
        #Score change
        score += 5
        score_string = "Score: %s" %score
        score_pen.clear()
        score_pen.write(score_string, False, align = "left", font = ("Arial", 10, "normal"))
        
    elif collition(wepon, enemy3):
        global collitions_count
        wepon.hideturtle()
        state = "ready"
        enemy3.setposition(random.randint(-100, 100), 180)
        collition_count += 1
        #Score change
        score += 5
        score_string = "Score: %s" %score
        score_pen.clear()
        score_pen.write(score_string, False, align = "left", font = ("Arial", 10, "normal"))
    
    #increasing the enemy speed over time
    if collition_count == collitions_required:
        enemy_speed *= 1.45
        collitions_required += 5
        
    #winning statement
    if score > 200:
        you_win.write("You Win!", False, align = "center", font = ("AR DARLING", 50, "normal"))
        break
       
        
        
        