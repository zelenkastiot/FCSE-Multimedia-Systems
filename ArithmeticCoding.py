"""

 Created on 20-Dec-20
 @author: Kiril Zelenkovski

Arithmetic coding in Python 3.7
"""
import itertools
import plotly.graph_objects as go
from simple_colors import *

# Function for getting all combinations of length and list of chars
def get_combinations(list_char, length):
    yield from itertools.product(*([list_char] * length))


# Set probabilities
probability = {'a': 0.8, 'b': 0.2}

# Read string
print("Build interval for string: ")
input_string = str(input())

# Get length for plotly table display
input_length = len(input_string)

# Set interval to 0 (beginning)
interval = 0

# Lists for plotly tables
print_left = []
print_right = []

for x in get_combinations('ab', input_length):
    # Get current string and set probability to 1
    current = ''.join(x)
    prob = 1

    # Calculate prob for current string
    for c in current:
        prob = prob * probability[c]

    # Print values
    interval_new = f'[{interval: .3f}, {(interval+prob): .3f} ]'
    print(f'{current}:'+interval_new)

    if current == input_string:
        result = interval_new

    # Increment probability
    interval += prob

    # For tables
    print_left.append(current)
    print_right.append(interval_new)

print()
print(print_left)
print(print_right)

print_my_string = green(input_string, ['bold'])
print("Interval for " + print_my_string + " is: " + result)

fig = go.Figure(
    data=[go.Table(
        header=dict(values=['Value', 'Interval'],
                    fill_color='lightskyblue',
                    align='center'),
        cells=dict(values=[print_left, print_right],
                   fill_color='lightcyan',
                   align='center'))],
    layout=go.Layout(
        title=f"Interval table for {input_length} character strings",
        title_x=0.5,
        margin=dict(l=10, r=10, t=27, b=20, pad=1),
        width=500,
        height=400,
        annotations=[
            dict(
                showarrow=False,
                text=f"Interval for {input_string} is: " + result,
                xanchor='right',
                x=1,
                yanchor='top',
                y=0.01)]))
fig.show()