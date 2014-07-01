#! /usr/bin/env python3.2
"""
BEEHIVELIB open source Python3 Library

Copyright (C) 2012 Georg Eckert, BeeHive Soft <eckert.georg@gmx.de>

beehivelib is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

beehivelib is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.
 
You should have received a copy of the GNU General Public License along
with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

def pythagoras(a, b, unknown):
    """
    pythagoras:
    lets you calculate hypothenuse of a right-angle triangle

    theory:
    hypothenuse² = kathete² * ankathete²

    how to use:
    x = pythagoras(y, z, 'unknown')

    'unknown' tells which side of the triangle is unknown:
    'h' - hypothenuse unknown
    'k' - kathete unknown
    'a' - ankathete unknown
    """
    if unknown == 'h':
    	c = (a**2 + b**2)**(1/2)
    elif unknown == 'k' or unknown == 'a':
        if a > b:
            c = (a**2 - b**2)**(1/2)
        elif b > a:
            c = (b**2 - a**2)**(1/2)
        else:
            print("Error: Hypothenuse and An-/Kathete cannot be the same length.\n")
            c = False
    else:
        print("Error: Method not available, please choose 'h', 'k' or 'a' next time.\
 If you need help, call 'help(beehivelib.pythagoras)'\n")
        c = False
    return c

def disp_txtfile(txtfilename):
    """
    disp_txtfile:
    displays a given textfile on screen without newline characters

    usage:
    disp_txtfile("name.txt")
    """
    with open(txtfilename,'r') as txtfile:
        text = txtfile.read()
    print(text)

def get_txt_from_file(txtfilename):
    """
    saves text from textfile with newline-characters in a string variable

    usage:
    text = get_txt_from_file("name.txt")
    """
    with open(txtfilename,'r') as txtfile:
        text = txtfile.read()
    return text

def get_rnd_txtfile_line(txtfilename):
    """
    opens given textfile and returns a random line as a string
    
    usage:
    rnd_line = get_rnd_txtfile_line("name.txt")
    """
    # import random
    import random
    # count lines of file
    file_length = txtfile_length(txtfilename)
    # get a pseudo-random integer
    rnd_int = random.randint(1, file_length)
    # get line number rnd_int from file
    rnd_txtfile_line = get_def_txtfile_line(txtfilename, rnd_int)
    # return string
    return rnd_txtfile_line

def get_def_txtfile_line(txtfilename, line_num_def):
    """
    opens given textfile and returns line with the given number

    usage:
    def_line = get_def_txtfile_line("name.txt", 2)

    returns line number 2 of file "name.txt"
    """
    # check length of file
    file_length = txtfile_length(txtfilename)
    if file_length < line_num_def:
        print("ERROR: ", line_num_def, " exeeds file length.")
        def_txtfile_line = ""
    else:
        text = get_txt_from_file(txtfilename)
        def_txtfile_line = text.splitlines()[line_num_def - 1]
    return def_txtfile_line

def fuel_calc(mode):
    """
    EN:
    calculates simple fuel consumption and duration values for you

    MODE:
    'c' - Consumption
    'd' - Duration
    'p' - Prediction

    DE:
    Führt einfache Treibstoff-Berechnungen durch

    MODE:
    'c' - Verbrauch
    'd' - Reichweite
    'p' - Benötigt
    """
    if mode == 'c':
        way = float(input("Wie weit hat die letzte Tankladung gereicht? [km] "))
        amount = float(input("Wie viele Liter Treibstoff wurden dafür verbraucht? [l] "))
        consumption = amount/way*100
        print("Der Verbrauch betrug ", consumption, " l/100km.\n")
    elif mode == 'd':
        consumption = float(input("Wie hoch ist der durchschnittliche Verbrauch? [l/100km] "))
        amount = float(input("Wie viele Liter Treibstoff stehen zur Verfügung? [l] "))
        duration = amount/consumption*100
        print("Der Treibstoff wird für etwa ", duration, " km reichen.\n")
    elif mode == 'p':
        consumption = float(input("Wie hoch ist der durchschnittliche Verbrauch? [l/100km] "))
        way = float(input("Wie weit soll die Ausfahrt sein? [km] "))
        prediction = consumption*way/100
        print("Es werden etwa ", prediction, " l Treibstoff benötigt.\n\
Für Hin- und Rückweg sollten ", prediction*2, " l Treibstoff eingeplant werden.\n")
    else:
        print("FEHLER: Die angegebene Methode existiert nicht. Wenn Sie Hilfe\
 benötigen rufen Sie 'help(beehivelib.fuel_calc)' auf.\n")

def txtfile_length(txtfilename):
    """
    returns number of lines in a textfile
    """
    with open(txtfilename) as txtfile:
        text = txtfile.read()
        line_count = len(text.splitlines())
    return line_count
        
def twoway_question(q_string = 'Ja oder Nein?', a1 = 'j', a2 = 'n', o_string = 'Option'):
    """
    EN:
    Is used to get an answer to a question with two possible answers.
    It will ask again and again until proper input is given.

    DE:
    Wird genutzt um Fragen mit zwei möglichen Antworten zu stellen.
    Fragt immer wieder bis eine der möglichen Antworten eingegeben wird.

    USAGE / NUTZUNG:
        >>> answer = twoway_question()
        >>> Ja oder Nein? 
        >>> Option: [j/n]

        >>> answer = twoway_question('Procede?')
        >>> Procede? 
        >>> Option: [j/n]

        >>> answer = twoway_question('A or B?', 'A', 'B')
        >>> A or B?
        >>> Option: [A/B]

        >>> answer = twoway_question('Doctor: How are you?', 'good', 'bad', 'Patient')
        >>> Doctor: How are you?
        >>> Patient: [good/bad]
    
    # is not possible as answer
    """

    # Be sure that every input is treated as strings
    a1, a2, q_string, o_string = str(a1), str(a2), str(q_string), str(o_string)
    print(q_string)
    answer = '#'
    while not(answer == a1 or answer == a2):
        answer = str(input(o_string + ': [' + a1 + '/' + a2 + '] '))
    return answer

def multiway_question(question = 'Yes or No?', ans_list = ['Yes', 'No', 'y', 'n'], show_opt = True):
    """
    Offers a way to verify user-input for questions with multiple possible answers and returns answer.
    
    USAGE:
        >>> answer = multiway_question('How are you?', ['good', 'bad', 'g', 'b', '+', '-'])
        >>> How are you?
        >>> Option: [good/bad/g/b/+/-]

        >>> answer = multiway_question()
        >>> Yes or No?
        >>> Option: [Yes/No/y/n]

        >>> a = multiway_question('A or B?', ['A', 'B'], False)
        >>> A or B?
        >>>

    The Option "False" hides the option-string.
    """

    # set initial values
    ans_ok = False

    # display defined question
    print(question)

    # build option-string with possible answers
    if show_opt:
        o_string = 'Option: ['
        for i in range(len(ans_list)):
            o_string = o_string + str(ans_list[i])
            if i < (len(ans_list) - 1):
                o_string = o_string + '/'
        o_string = o_string + '] '
    else:
        o_string = ''

    # ask for user-input while given answer is not part of pre-defined answers
    while not(ans_ok):
        ans_given = str(input(o_string))
        for i in range(len(ans_list)):
            if ans_given == str(ans_list[i]):
                ans_ok = True

    # return correct answer as string
    return ans_given
