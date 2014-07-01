#! /usr/bin/env python3.2
"""
Copyright (C) 2012 Georg Eckert <eckert.georg@gmx.de>

geldrausssch is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

geldrausssch is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.
 
You should have received a copy of the GNU General Public License along
with this program.  If not, see <http://www.gnu.org/licenses/>.

WHAT IT DOES:
gr_uia provides user interaction modules for the game geldrausssch
"""

from geldrausssch import beehivelib # my own library

def gr_play_again():
    """lets player in case of game over choose whether to quit or to play again"""
    play_again_answer = beehivelib.multiway_question('Möchten Sie sofort noch eine Runde spielen?', ['j','n'])
    print("\n")
    if play_again_answer == "j":
        print("Oh, das freut mich aber!\n")
        game_in_progress = True
    else:
        print("Das kann ich verstehen. Diese Partie war wirklich anstrengend. Auf Wiedersehen.\n")
        game_in_progress = False
    return game_in_progress

def add_game_content():
    """
    use it to add new contant such as questions and answers to the game.
    Structure must be: question;a1;a2;a3;a4;1
    """
    q_or_c = beehivelib.twoway_question('Frage oder Kommentar hinzu fügen?', 'f', 'k')
    if q_or_c == 'f':
        # Add Q and A
        cont_ok = 'n'
        while not(cont_ok == 'j'):
            q_a_cont = ['q', 'a1', 'a2', 'a3', 'a4', 1, 1, 'de']
            input_strings = ['Frage: ', 'Antwort 1: ', 'Antwort 2: ', 'Antwort 3: ', 'Antwort 4: ', 'Nummer korrekte Antwort: ', 'Level: [1 - 15] ', 'Sprache: [de/en/fr] ']
            print('Bitte geben Sie nachfolgend ein:')
            for i in range(8):
                # Loop through List
                q_a_cont[i] = input(input_strings[i])
            q_a_string = q_a_cont[0] + ';' + q_a_cont[1] + ';' + q_a_cont[2] + ';' + q_a_cont[3] + ';' + q_a_cont[4] + ';' + str(q_a_cont[5])
            # Let user check if everything is alright
            print('Frage: ' + q_a_string + '\n' + 'Level: ' + q_a_cont[6] + '\nSprache: ' + q_a_cont[7] + '\n')
            cont_ok = beehivelib.twoway_question('Alles in Ordnung?')
        # Write String to correct file
        cont_fname = q_a_cont[7] + '/' + 'gr_QA_' + str(q_a_cont[6]) + '.txt'
        with open(cont_fname,'a') as cont_file:
            cont_file.write(q_a_string)
    elif q_or_c == 'k':
        # Add Comment
        cont_ok = 'n'
        while not(cont_ok == 'j'):
            comment_lang = input('Sprache: [de/en/fr] ')
            comment_level = input('Level: [1 - 15] ')
            new_comment = input('Neuer Kommentar: ')
            cont_ok = beehivelib.twoway_question('Alles in Ordnung?')
        # Write String to correct file
        cont_fname = comment_lang + '/' + 'gr_comment_' + str(comment_level) + '.txt'
        with open(cont_fname,'a') as cont_file:
            cont_file.write(new_comment)

def gr_answer_menu():
    """gr_answer_menu: offers different options like answer, wizards card a.s.o."""
    pass # has to be implemented
