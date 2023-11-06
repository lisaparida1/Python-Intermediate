import turtle
import pandas

scr = turtle.Screen()
scr.title('US STATES QUIZ')
image = "blank_states_img.gif"
scr.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
states_to_learn = []

while len(guessed_states) < 50:
    which_state = scr.textinput(title=f"{len(guessed_states)}/50 guessed right!", prompt="Enter the state's name:").title()

    if which_state == 'Exit':
        # Using for loop

        # for i in all_states:
        #     if i not in guessed_states:
        #         states_to_learn.append(i)
        #     else:
        #         pass

        # Using List Comprehension

        states_to_learn = [i for i in all_states if i not in guessed_states]

        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    if which_state in all_states:
        if which_state in guessed_states:
            pass
        else:
            guessed_states.append(which_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == which_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(state_data.state.item())




