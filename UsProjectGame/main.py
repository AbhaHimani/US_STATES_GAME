import turtle
from turtle import Turtle
import pandas
screen= turtle.Screen()
screen.title("US STATE GAMES")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data= pandas.read_csv("50_states.csv")
all_states= data.state.to_list()
guessed_state=[]
while len(guessed_state) < 50:
 answer_state= screen.textinput(title=f"Guess the state {len(guessed_state)}/50 ", prompt="What's another state's name?").title()
 if answer_state=="Exit":
     break
 if answer_state in all_states:
   guessed_state.append(answer_state)
   dino = Turtle()
   dino.hideturtle()
   dino.penup()
   state_data= data[data.state == answer_state]
   dino.goto(int(state_data.x), int(state_data.y))
   dino.write(answer_state)




turtle.mainloop()
