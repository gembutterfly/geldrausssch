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

Application-Name: GeldRau$$$ch
Version: 2012-09-25a
Licence: GPvL 3.0
What is still missing:
- Jokers (Telephone, 50%, 33%, new question)
- small hints
- level based comments
"""
# 1 Import Libraries
from geldrausssch import beehivelib # my own library, must be in the same directory
from geldrausssch import gr_disp # geldrausssch game library to display content on screen
from geldrausssch import gr_uia # modules for user interaction
from geldrausssch import gr_handle_gc # handles game content and file i/o

# 2 Initialize Variables
player_name = "Niemand"
mlevel = ['0', '100', '1.000', '5.000', '10.000', '50.000', '100.000', '500.000', '1.000.000', '5.000.000', '25.000.000', '50.000.000', '100.000.000', '250.000.000', '500.000.000', '1.000.000.000']

# 3 Define Functions
def main_menu():
    """main_menu: handles the main menu"""
    # Declare needed variables
    menu_choice = "z"
    # Display menu screen
    # Go back to Main Menu until "option a: Start Game" is chosen
    while not(menu_choice == 'a' or menu_choice == 'e'):
        print("-----------------------------------------------------------------------")
        # Display Menu
        gr_disp.disp_main_menu()
        # Repeat asking while wrong input
        menu_choice = beehivelib.multiway_question('Was möchten Sie tun?', ['a','b','c','d','e'])
        print("-----------------------------------------------------------------------")
        # Start chosen option
        if menu_choice == "a":
            print("Aufgeregt? Los geht's!\n")
            main_game()
        elif menu_choice == "b":
            beehivelib.disp_txtfile("de/manual.txt")
            # reset menu_choice
            menu_choice = "z"
        elif menu_choice == "c":
            # display highscore file
            beehivelib.disp_txtfile("highscore.txt")
            # reset menu_choice
            menu_choice = "z"
        elif menu_choice == "d":
            gr_uia.add_game_content()
            # reset menu_choice
            menu_choice = "z"
        elif menu_choice == "e":
            print("Auf Wiedersehen.\n")

def main_game():
    """ Main Game Code Starts Here """
    # declare variables
    game_in_progress = True

    # 1 - Initialize Game
    # Enter Player's Name
    player_name = str(input("Mit wem habe ich es denn zu tun?\nName: "))
    print("Schön, Sie kennen zu lernen, " + player_name + "\n")

    while game_in_progress:
        # declare variables of every new game
        gameover = False
        gamelevel = 0

        # 2 - Begin Game and resume while "gameover == false"
        while (not(gameover) and gamelevel <= 14):
            # raise gamelevel by 1
            gamelevel = gamelevel + 1
            # display recent moneylevel
            gr_disp.gr_display_levelinfo(gamelevel, mlevel[gamelevel])
            # get random line string from file
            q_a_string = gr_handle_gc.get_question_string(gamelevel)
            # extract question and answers from string
            q_a_container = gr_handle_gc.extract_question(q_a_string)
            # display question
            gr_disp.display_question(q_a_container)
            # Ask for correct answer
            answergiven = beehivelib.multiway_question('Welche Antwort ist richtig?',[1,2,3,4],False)
            # Check given answer
            if int(answergiven) != q_a_container[5]:
                gr_handle_gc.highscore(gamelevel - 1, q_a_container[5], mlevel[gamelevel-1], player_name);
                gameover = True
                game_in_progress = gr_uia.gr_play_again()
            else:
                print("Richtig!\n")

                # check if last level is reached
                if gamelevel < 15:
                    # Display random comment
                    comment_string = gr_handle_gc.get_comment(gamelevel)
                    print(comment_string)	
                    print("Weiter geht es mit Frage Nummer " + str(gamelevel + 1) + ".\n")
                    # Wait for user to press Enter
                    continue_game = beehivelib.twoway_question('Nächste Frage?')
                    if continue_game == 'n':
                        gameover = True
                        game_in_progress = False
                else:
                    # display "you-won" message
                    gr_disp.gr_display_winner()
                    gr_handle_gc.highscore(gamelevel, q_a_container[5], mlevel[gamelevel], player_name)
                    game_in_progress = gr_uia.gr_play_again()

def start_game():
    """ START GAME """
    # Show Welcome Message
    gr_disp.gr_welcome_screen()

    # Start Main Menu Cycle
    procede = beehivelib.twoway_question('Fortsetzen?')
    if procede == 'j':
        main_menu()
