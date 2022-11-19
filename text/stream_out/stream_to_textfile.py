import contextlib

with open('./stream out/text.txt', 'w') as file:
    with contextlib.redirect_stdout(file):
        print('stream out')
