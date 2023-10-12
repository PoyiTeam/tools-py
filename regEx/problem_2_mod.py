import re


def problem2(searchstring):
    """
    Extract student and ship.

    : param searchstring : string
    : return : tuple
    """
    hero_name = 'nohero'
    vechcle_name = 'noname'

    # find hero_name at group(2)
    # find vechcle_name at group(6)
    pattern = r'(([A-Z][a-z]*|[A-Z][a-z]*\s[A-Z][a-z]*)(\s)(?=flies|rides))(flies|rides)\s([a])\s([A-Z][a-z]*\s[A-Z][a-z]*|[A-z][a-z]*|[a-z]*)'
    match = re.search(pattern, searchstring)
    print(f'match : {match}')
    if match != None:
        hero_name = match.group(2)
        vechcle_name = match.group(6)

    return (hero_name, vechcle_name)


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
