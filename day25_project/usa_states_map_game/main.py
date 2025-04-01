import turtle
import pandas as pd
from pencil import Pencil

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. State Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

pencil = Pencil()
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_guessed_states = []
score = 0

while score < 50:

    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer in all_states and answer not in correct_guessed_states:
        state = data[data.state == answer]
        pencil.write_state(answer, state.x.item(), state.y.item())
        correct_guessed_states.append(answer)
        score += 1