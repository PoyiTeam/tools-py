import re


def problem1(searchstring):
    """
    Match emails.

    : param searchstring : string
    : return : ' valid ' or ' invalid '
    """
    pattern = r'^([1-7][0-9]{2})\.[a-zA-Z]{1,10}\d*@(sheild\.gov|avengers\.com)$'
    if re.fullmatch(pattern, searchstring):
        return 'valid '
    else:
        return 'invalid '


def problem2(searchstring):
    """
    Extract student and ship.

    : param searchstring : string
    : return : tuple
    """

    pattern = r'([A-Z][a-zA-Z\s]*)\s(rides|flies)\s(a\s)?([a-zA-Z\s]+)'
    match = re.search(pattern, searchstring)
    print(match)
    if match:
        student = match.group(1)
        ship = match.group(4)
        return (student, ship)
    else:
        return ("nohero", "noname")


def problem3(searchstring):
    """
    Replace apprentice with title.

    : param searchstring : string
    : return : string with corrected word
    """
    def reply(m):
        name = m.group(1)
        if name[0].isupper():
            return name + " " + m.group(2).capitalize()
        else:
            return m.group(0)
    # replacements = { 'Spider Boy': 'Spider Man', 'Iron Boy': 'Iron Man','Spider Girl': 'Spider Woman','Invisible Girl': 'Invisible Woman'}

    pattern = r'([A-Z][a-zA-Z]*) (Boy|Girl|boy|girl)'

    return re.sub(pattern, reply, searchstring)


if __name__ == '__main__':
    # Added nomatch test cases for Problem 2 and 3
    print("\nProblem 1:")
    # ... (test cases for problem1)
    testcase11 = '123.iamironman@avengers.com'
    print("Student answer: ", problem1(testcase11),
          "\tAnswer correct?", problem1(testcase11) == 'valid')
    testcase12 = '250.Srogers1776@avengers.com'
    print("Student answer: ", problem1(testcase12),
          "\tAnswer correct?", problem1(testcase12) == 'valid')

    print("\nProblem 2:")
    # ... (test cases for problem2)
    testcase21 = "Captain America rides a Harley"
    print("Student answer: ", problem2(testcase21), "\tAnswer correct?",
          problem2(testcase21) == ("Captain America", "Harley"))
    testcase22 = "No one rides a Harley like Ghost Rider, athough Spider Man rides a Harley with some similar expertise"
    print("Student answer: ", problem2(testcase22), "\tAnswer correct?",
          problem2(testcase22) == ("Spider Man", "Harley"))

    print("\nProblem 3:")
    # ... (test cases for problem3)
    testcase31 = 'Spider Boy, I need help!'
    print("Student answer: ", problem3(testcase31), "\tAnswer correct?",
          problem3(testcase31) == "Spider Man, I need help!")
    testcase32 = 'There is a boy trapped in a burning building Iron Boy'
    print("Student answer: ", problem3(testcase32), "\tAnswer correct?", problem3(
        testcase32) == "There is a boy trapped in a burning building Iron Man")
