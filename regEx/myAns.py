# %%
import re
# %%

vechcles = ['ships', 'spaceship']


def problem2(searchstring):
    """
    Extract student and ship.

    : param searchstring : string
    : return : tuple
    """
    print(f'runing function: {problem2.__name__}')

    # pattern = r'([A-Z][a-zA-Z\s]*)\s(rides|flies)\s(a\s)?([a-zA-Z\s]+)'
    # match = re.search(pattern, searchstring)
    # if match:
    #     student = match.group(1)
    #     ship = match.group(4)
    #     return (student, ship)
    # else:
    #     return ("nohero", "noname")

    pattern = r'(\w+)'
    # pattern = r'([A-Z][a-zA-Z\s]*)\a'
    word_lst = re.search(pattern, searchstring).group()
    for i, word in enumerate(word_lst):
        word_lst[i].replace(',|.', '')

    print(f'word_lst: {word_lst}')
    word_lst = re.split(' |, ', searchstring)
    print(f'split str: {word_lst}')
    # search_a = re.search(r'[a]', splited_str[2]).group()
    # print(f'search a: {search_a}')
    a_flag_lst = list()
    verb_flag_lst = list()

    for i, word in enumerate(word_lst):
        if is_a(word):
            a_flag_lst.append(i)
        if is_verb(word):
            verb_flag_lst.append(i)
    print(f'a_flags: {a_flag_lst}')
    print(f'verb_flags: {verb_flag_lst}')
    # search 'a'
    # for myStr in splited_str:
    #    if

    return 'xd'


def is_a(word: list):
    pattern = re.compile(r'\ba\b')
    match = pattern.search(word)
    if match == None:
        return False
    else:
        return True


def is_verb(word):
    # pattern = re.compile(r'(\brides\b|\bflies\b)')
    pattern = re.compile(r'(rides)')
    match = pattern.search(word)
    print(word)
    if match == 'rides' or match == 'flies':
        return True
    else:
        return False


# %%
# print("\nProblem 2:")
# testcase21 = "Captain America rides a Harley"
# print("Student answer: ", problem2(testcase21), "\tAnswer correct?",
#       problem2(testcase21) == ("Captain America", "Harley"))

testcase22 = "No one rides a Harley like Ghost Rider, athough Spider Man rides a Harley with some similar expertise"
print("Student answer: ", problem2(testcase22), "\tAnswer correct?",
      problem2(testcase22) == ("Spider Man", "Harley"))

# testcase23 = "Groot rides a spaceship"
# print("Student answer: ", problem2(testcase23), "\tAnswer correct?",
#       problem2(testcase23) == ("Groot", "spaceship"))

# testcase24 = "Starlord flies a Milano"
# print("Student answer: ", problem2(testcase24), "\tAnswer correct?",
#       problem2(testcase24) == ("Starlord", "Milano"))

# testcase25 = "The Starlord flies many ships, but Rocket flies a Warbird Special much faster"
# print("Student answer: ", problem2(testcase25), "\tAnswer correct?",
#       problem2(testcase25) == ("Rocket", "Warbird Special"))

# testcase26 = "Spider Man flies through the city"
# print("Student answer: ", problem2(testcase26), "\tAnswer correct?",
#       problem2(testcase26) == ("nohero", "noname"))
