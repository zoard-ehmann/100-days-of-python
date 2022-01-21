import turtle

import pandas


IMAGE = "Day25/US_States_Game/blank_states_img.gif"
STATES = "./Day25/US_States_Game/50_states.csv"
TO_LEARN = "./Day25/US_States_Game/states_to_learn.csv"


def write_state(state_data):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(int(state_data.x), int(state_data.y))
    pen.write(f"{state_data.state.item()}")


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)
screen.tracer(0)

states_df = pandas.read_csv(STATES)
number_of_states = len(states_df.state)
guessed_states = []
missed_states = {
    "State": []
}

while len(guessed_states) < number_of_states:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{number_of_states} States Correct", prompt="Tell a state's name.").title()
    guess = states_df[states_df.state == answer_state]
    
    if answer_state == "Exit":
        break
    
    if not guess.empty and answer_state not in guessed_states:
        write_state(guess)
        guessed_states.append(answer_state)
        
    screen.update()

# for state in states_df.state.to_list():
#     if state not in guessed_states:
#         missed_states["State"].append(state)

# Alternative solution using List Comprehension
missed_states["State"] = [state for state in states_df.state.to_list() if state not in guessed_states]

df = pandas.DataFrame(missed_states)
df.to_csv(TO_LEARN)
