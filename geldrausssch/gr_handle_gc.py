#! /usr/bin/env python3
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
gr_handle_gc provides functions to handle game content und file input/output
"""

# IMPORT
from geldrausssch import beehivelib
import random

# FUNCTIONS
def get_comment(level):
    """gets a random comment-string from comment-file"""
    comment_file = ("share/geldrausssch-data/lang/de/gr_comment_"
                   + str(level) + ".txt")
    # get q_a_string
    comment_string = beehivelib.get_rnd_txtfile_line(comment_file)
    return comment_string

def highscore(level, answercorrect, mlevel, player_name):
    """highscore: will be called in case of game over or win"""
    if level < 15:
        # Display GameOver Message
        print('Die Antwort war leider falsch.'
              'Die richtige Antwort wäre Antwort '
              + str(answercorrect)
              + ' gewesen. Es war trotzdem schön, dass sie mitgespielt '
              ' haben. Ihr Name und die erreichte Punktzahl werden in '
              'einer Rangliste abgespeichert, die Sie aus dem '
              'Hauptmenü abrufen können.\n')
    # Write to HighScore
    with open("share/geldrausssch-data/highscore.txt",'a') as highscore_file:
        highscore_file.write(str(level)
                             + ";"
                             + player_name
                             + ";"
                             + mlevel
                             + "\n")

# CLASSES
class q_and_a:
    """
    q_and_a is an 'question and answer' object. After creating it, it
    is possible to set the level (1 - 15), fetch a random question and
    matching answers from a textfile.

    USAGE:
        a = q_and_a()
        a.set_level = 1

        or
   
        a = q_and_a(1)
    """
    def __init__(self, level=1):
        self.level = level
        self.q_a_container = []
        self.q_a_string = ''
        self.correct = 1
	
    def set_level(self, level):
        """
        set the level of the q/a object
        """
        self.level = level
		
    def load_content(self):
        """
        load question and matching answers from text-file,
        'set_level' should be used first
        """
        self.get_question_string()
        self.extract_question()
        self.correct = self.q_a_container[5]
		
    def get_question_string(self):
        """
        function that gets random string from textfile, where questions and
        answers are stored
        """
        qa_file = "share/geldrausssch-data/lang/de/gr_QA_" + str(self.level) + ".txt"
        # get q_a_string
        self.q_a_string = beehivelib.get_rnd_txtfile_line(qa_file)

    def extract_question(self):
        """
        extracts question and answers from string and returns Q and A Container
        List string must have the following structure
        (1 is number of correctanswer):
        question;answer1;answer2;answer3;answer4;1
        """
        self.q_a_container = self.q_a_string.split(';')
        self.q_a_container[5] = int(self.q_a_container[5])
		
    def mix_answers(self):
        """
        mixes fields [1] to [5] of the q_a_container array and
        corrects [6], which is the number of the correct answer
        """
        mix = [1,2,3,4]
        # shuffle, e.g. mix = [4,1,3,2]
        random.shuffle(mix)
        pos_correct = 0
        for i in mix:
            if i == self.correct:
                correct = pos_correct
            pos_correct += 1
        # add 1 because container starts with question
        self.correct = correct + 1
        self.q_a_container[5] = self.correct
        tmp_q_a = ['','','','']
        number = 0
        for i in mix:
            tmp_q_a[number] = self.q_a_container[i]
            number += 1
        number = 1
        for i in tmp_q_a:
            self.q_a_container[number] = i
            number += 1     
        
    def wizards_card_50_50(self, wizard33=False):
        """
        wizards_card_50_50: deletes two randomly chosen wrong answers
        """
        tmp = [1,2,3,4]
        # remove correct answer from list
        tmp.remove(self.correct)
        # shuffle list
        random.shuffle(tmp)
        # remove to items
        tmp.pop()
        if wizard33:
            tmp.pop()
        # refresh Q/A container
        for i in tmp:
            self.q_a_container[i] = ''

    def wizards_card_33_66(self):
        """
        wizards_card_33_66: deletes one randomly chosen wrong answer
        """
        self.wizards_card_50_50(True)
