import contextlib

with open('text.txt', 'w') as file:
    with contextlib.redirect_stdout(file):
        print('stream out')
