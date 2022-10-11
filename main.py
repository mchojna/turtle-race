import turtle
import random

race = False
colors = {0:"red", 1:"orange", 2:"yellow", 3:"green", 4:"blue", 5:"purple", 6:"black"}
screen = turtle.Screen()
screen.setup(width=650, height=400)
while True:
    bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a colour: ").lower()
    if bet in colors.values():
        race = True
        break

turtles = []
x_pos = -300
y_pos = -150

for num in range(7):
    race_turtle = turtle.Turtle(shape="turtle")
    race_turtle.color(colors[num])
    race_turtle.penup()
    race_turtle.setposition(x=x_pos, y=y_pos)
    y_pos += 50
    turtles.append(race_turtle)

while race:
    for num in range(7):
        if turtles[num].xcor() >= 300:
            winner = num
            race = False
            break
            
        random_distance = random.randint(0, 10)
        turtles[num].forward(random_distance)


if colors[winner] == bet:
    print("Congratulations! Your turtle has won!")
else:
    print(f"Your turtle has lost! {colors[winner].title()} turtle has won!")
