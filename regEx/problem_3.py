import re


def problem3(searchstring):
    """
    Replace apprentice with title.

    : param searchstring : string
    : return : string with corrected word
    """

    repl = r'(([A-Z][a-z]*)\s(?=boy|girl|Boy|Girl))(boy|girl|Boy|Girl)'
    # keyword start index
    word_start_idx = re.search(repl, searchstring).start(3)
    print(f'key word start position: {word_start_idx}')
    return 'xd'


def upper_first_letter(word: str):
    word[0].upper()
    return word


print("\nProblem 3:")
testcase31 = 'Spider Boy, I need help!'
result = problem3(testcase31)
print("Student answer: ", result, "\tAnswer correct?",
      result == "Spider Man, I need help!")

testcase32 = 'There is a boy trapped in a burning building Iron Boy'
result = problem3(testcase32)
print("Student answer: ", result, "\tAnswer correct?", result ==
      "There is a boy trapped in a burning building Iron Man")
