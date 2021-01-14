import pandas
import turtle

data = pandas.read_csv("./50_states.csv")
all_state = data.state.to_list()
answer = input("Enter answer : ")

if answer in all_state:
          state_data = data[data.state == answer]
          print(state_data.x.item())
          print(state_data.y.item())
          print(state_data.state.item())

