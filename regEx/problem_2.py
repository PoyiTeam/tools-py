import re


def problem2(searchstring):
    """
    Extract student and ship.

    : param searchstring : string
    : return : tuple
    """
    vechcle_name = 'noname'
    hero_name = 'nohero'
    vechcle_name_idx = None

    pattern = r'(\w+)'
    word_lst = re.findall(pattern, searchstring)
    # print(f'string: {searchstring}')
    print(f'word_lst: {word_lst}')

    name_idx_lst = list()
    verb_idx_lst = list()

    for i, word in enumerate(word_lst):
        if is_first_upper_case(word):
            name_idx_lst.append(i)
        if is_verb(word):
            verb_idx_lst.append(i)
    # print(f'Name index: {name_idx_lst}')
    # print(f'verb indexs: {verb_idx_lst}')

    # --- remain effect verb ---
    effect_verb_idx_lst = list()
    for verb_idx in verb_idx_lst:
        if word_lst[verb_idx + 1] == 'a' and is_first_upper_case(word_lst[verb_idx - 1]):
            effect_verb_idx_lst.append(verb_idx)
    print(f'effect verb index: {effect_verb_idx_lst}')

    # --- process hero name ---
    for verb_idx in effect_verb_idx_lst:
        hero_name_idx = verb_idx - 1

        if is_first_upper_case(word_lst[hero_name_idx]) == False:
            break

        # get last word of hero name
        if is_first_upper_case(word_lst[hero_name_idx]):
            hero_name = word_lst[hero_name_idx]

            # add words if number of hero name words > 2
            for i in range(hero_name_idx-1, -1, -1):
                if is_first_upper_case(word_lst[i]):
                    hero_name = f'{word_lst[i]} {hero_name}'
                else:
                    break

    # --- process vechcle name ---
    for verb_idx in effect_verb_idx_lst:
        vechcle_name_idx = verb_idx+2    # get first index of word after "a"
        if is_first_upper_case(word_lst[vechcle_name_idx]) == False:
            vechcle_name = word_lst[vechcle_name_idx]
            break

        # get first word of vechcle name
        if is_first_upper_case(word_lst[vechcle_name_idx]):
            vechcle_name = word_lst[vechcle_name_idx]

        # add words if number of vechcle name words > 2
        if vechcle_name_idx+1 < len(word_lst):
            for i in range(vechcle_name_idx+1, len(word_lst)):
                if is_first_upper_case(word_lst[i]):
                    vechcle_name = f'{vechcle_name} {word_lst[i]}'
                else:
                    break

    return (hero_name, vechcle_name)


def is_first_upper_case(word):
    pattern = re.compile('[A-Z][a-zA-Z]+')
    match = pattern.search(word)
    if match == None:
        return False
    else:
        return True


def is_verb(word):
    pattern = re.compile('rides|flies')
    match = pattern.search(word)
    if match == None:
        return False
    else:
        match = match.group(0)

    if match == 'rides' or match == 'flies':
        return True
    else:
        return False


print("\nProblem 2:")
testcase21 = "Captain America rides a Harley"
result = problem2(testcase21)
print("Student answer: ", result, "\tAnswer correct?",
      result == ("Captain America", "Harley"))

testcase22 = "No one rides a Harley like Ghost Rider, athough Spider Man rides a Harley with some similar expertise"
result = problem2(testcase22)
print("Student answer: ", result, "\tAnswer correct?",
      result == ("Spider Man", "Harley"))

testcase23 = "Groot rides a spaceship"
result = problem2(testcase23)
print("Student answer: ", result, "\tAnswer correct?",
      result == ("Groot", "spaceship"))

testcase24 = "Starlord flies a Milano"
result = problem2(testcase24)
print("Student answer: ", result, "\tAnswer correct?",
      result == ("Starlord", "Milano"))

testcase25 = "The Starlord flies many ships, but Rocket flies a Warbird Special much faster"
result = problem2(testcase25)
print("Student answer: ", result, "\tAnswer correct?",
      result == ("Rocket", "Warbird Special"))

testcase26 = "Spider Man flies through the city"
result = problem2(testcase26)
print("Student answer: ", result, "\tAnswer correct?",
      result == ("nohero", "noname"))
