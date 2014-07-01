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
gr_disp provides modules to display game content of geldrausssch on screen.
"""

def display_question(q_a_container):
    """
    displays a question & answers layout
    
    USAGE:
        display_question(['Question?', 'Answer1', 'Answer2', 'Answer3', 'Answer4', 2])
    """
    print("Frage: " + q_a_container[0] + "\n")
    print("-----------------------------------------------------------------------\n")
    print("1: " + q_a_container[1] + "\n")
    print("2: " + q_a_container[2] + "\n")
    print("3: " + q_a_container[3] + "\n")
    print("4: " + q_a_container[4] + "\n")
    print("-----------------------------------------------------------------------\n")

def gr_display_levelinfo(gamelevel, moneylevel):
    """
    draws header with money and gamelevel
    """
    print("=======================================================================\n")
    print(" Spiel um: " + moneylevel + " Taler\n")
    print(" Level ", gamelevel, "\n")
    print("=======================================================================\n")

def gr_welcome_screen():
    """displays a welcome message"""
    # Display Welcome-Header
    print("===============================")
    print("|         Geldrau$$$ch        |")
    print("===============================")
    print("  Ein Spiel von: Georg Eckert  ")
    print("----   BeeHIVE Soft 2012   ----\n")
    # Display Welcome-Message
    print("Herzlich Willkommen bei GeldRau$$$ch. Mein Name ist\n\
F7-T12. Ich bin der Spielmeister heute.\n\
Ich denke wir werden eine Menge Spaß haben,\n\
auf dem Weg zu einer Milliarde Taler!\n")

def gr_display_winner():
    """displays a gratulation-message if level15 is won"""
    print("Herzlichen Glückwunsch!\n")
    print("Sie sind nun virtueller Milliardär!\n")
    print('Ich hoffe Sie hatten genau so viel Spaß wie ich und\
 vielleicht sehen wir uns ja bald wieder für eine weitere Partie\
 "GeldRau$$$ch!\n')

def disp_main_menu():
    print("Was möchten Sie als nächstes tun?")
    print("-------------------------")
    print("| a: Spiel starten      |")
    print("| b: Anleitung anzeigen |")
    print("| c: Highscore anzeigen |")
    print("| d: Spiel erweitern    |")
    print("| e: Spiel beenden      |")
    print("-------------------------")
