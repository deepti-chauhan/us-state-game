import turtle
import pandas as pd 

# turtle only works with gif files which we will use
# as background of our project

# firstly we'll setup our screen size and give it a title.

screen = turtle.Screen()
screen.title("US States Game")

# we can use image as shape of turtle 
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# import our csv file
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
	# popup box for user input
	answer_state = screen.textinput(title = f"{len(guessed_states)}/50 State Guess Correctly.", 
		prompt="What's another states name?").title()

	# to stop the game and exit out of the window instantly.
	if answer_state == "Exit":
		answ = [state for state in all_states if state not in guessed_states]
		'''for ans in all_states:
									if ans not in guessed_states:
										answ.append(ans)'''
		df = pd.DataFrame(answ)
		# csv file for all the remaining answers which user missed to give.
		df.to_csv("your_report.csv")
		break

	if answer_state in all_states:
		guessed_states.append(answer_state)
		pos = turtle.Turtle()
		pos.hideturtle()
		pos.penup()
		state_data = data[data.state == answer_state]
		pos.goto(int(state_data.x), int(state_data.y)) 
		# our csv data is in string format
		# thts why it is important to convert it into correct format 
		# so that we will avoid errors.

		pos.write(f"{answer_state}")

# this is important so that our screen remains open until we close it manually.
# screen.exitonclick() -> because we are using break statement in while loop
# we can avoid exitonclick() method.


