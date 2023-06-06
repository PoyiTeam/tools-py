from contextlib import redirect_stdout


with open('myfile.txt', 'w') as file:
    with redirect_stdout(file):
        print('hello print')
