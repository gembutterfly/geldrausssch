#!/usr/bin/python3

# IMPORT ----------------------------------------------------------------------
    # GTK
from gi.repository import Gtk
    # Game Libraries
from geldrausssch import gr_handle_gc
    # Help Dialog
from geldrausssch import help_dialog
    # Highscore
from geldrausssch import highscore
    # Extend
from geldrausssch import extend
    # My own Library
from geldrausssch import beehivelib

# CLASSES ---------------------------------------------------------------------
# CLASS: Main App -------------------------------------------------------------
class GeldRauSSSch(object):
    """
    the main class of the application
    
    USAGE:
    app = GeldRauSSSch()
    app.run()
    """
    def __init__(self):
        """
        initializes the application
        loads GUI with Gtk.Builder from glade file
        declares variables
        """
        # BUILDER - GUI from glade-file --------------------------------- START
        # BUILDER: create new instance
        self.builder = Gtk.Builder()
        self.builder.add_from_file("share/geldrausssch-data/ui/"
                                   "geldrausssch_gui.glade")
        self.builder.connect_signals(self)
        # BUILDER: get objects
            # WINDOWS
        self.window_main =  self.builder.get_object('window_main')
            # BOXES
        self.vbox_start = self.builder.get_object('vbox_start')
        self.vbox_ingame = self.builder.get_object('vbox_ingame')
        self.hbox_ingame = self.builder.get_object('hbox_ingame')
        self.menubar_main =  self.builder.get_object('menubar_main')
        self.notebook_switch =  self.builder.get_object('notebook_switch')
        self.buttonbox_main =  self.builder.get_object('buttonbox_main')
        self.textview_help =  self.builder.get_object('textview_help')
        self.vbox_victory =  self.builder.get_object('vbox_victory')
            # ENTRY
        self.entry_name =  self.builder.get_object('entry_name')
            # IMAGES
        self.image_f7t12 =  self.builder.get_object('image_f7t12')
        self.image_correct =  self.builder.get_object('image_correct')
        self.image_wrong =  self.builder.get_object('image_wrong')
        self.image_level_screen = self.builder.get_object('image_level_screen')
            # LABELS
        self.label_welcome =  self.builder.get_object('label_welcome')
        self.label_comment = self.builder.get_object('label_comment')
        self.label_question =  self.builder.get_object('label_question')
        self.label_answerA =  self.builder.get_object('label_answerA')
        self.label_answerB =  self.builder.get_object('label_answerB')
        self.label_answerC =  self.builder.get_object('label_answerC')
        self.label_answerD =  self.builder.get_object('label_answerD')
        self.label_player = self.builder.get_object('label_player')
        self.label_victory = self.builder.get_object('label_victory')
            # BUTTONS
        self.button_next =  self.builder.get_object('button_next')
        self.button_A =  self.builder.get_object('button_A')
        self.button_B =  self.builder.get_object('button_B')
        self.button_C =  self.builder.get_object('button_C')
        self.button_D =  self.builder.get_object('button_D')
        self.button_start =  self.builder.get_object('button_start')
        self.button_extend =  self.builder.get_object('button_extend')
        self.button_exit =  self.builder.get_object('button_exit')
        self.button_help =  self.builder.get_object('button_help')
        self.button_highscore =  self.builder.get_object('button_highscore')
        self.button_victory = self.builder.get_object('button_victory')
        self.dialog_about = self.builder.get_object('aboutdialog')
        self.button_5050 = self.builder.get_object('button_5050')
        self.button_3366 = self.builder.get_object('button_3366')
        self.button_newq = self.builder.get_object('button_newq')
            # DIALOGS
        self.messagedialog_rank = self.builder.get_object('messagedialog_rank')
        # BUILDER --------------------------------------------------------- END

        # VARIABLES
        self.player_name = ""
        self.level = 0
        self.mlevel = ['0',
                       '100',
                       '1.000',
                       '5.000',
                       '10.000',
                       '50.000',
                       '100.000',
                       '500.000',
                       '1.000.000',
                       '5.000.000',
                       '25.000.000',
                       '50.000.000',
                       '100.000.000',
                       '250.000.000',
                       '500.000.000',
                       '1.000.000.000']
        self.correct_ans = 1
        self.gameover = False
        self.q_a = gr_handle_gc.q_and_a()

    # RUN --------------------------------------------------------------- START
    def run(self):
        """
        shows main window with show_all()
        """
        try:
            self.window_main.show_all()
            Gtk.main()
        except KeyboardInterrupt:
            pass
    # RUN ----------------------------------------------------------------- END

    # QUIT -------------------------------------------------------------- START
    def quit(self):
        """
        quits Gtk main loop
        """
        Gtk.main_quit()
    # QUIT ---------------------------------------------------------------- END

    # FUNCTIONS --------------------------------------------------------- START
    # FUNCTION: ingame -------------------------------------------------- START
    def ingame(self):
        """
        sets answer-buttons sensitive and next-button non-sensitive
        resets commentator, question- and answer-labels
        """
        # set neutral commentator image
        self.image_correct.set_visible(False)
        self.image_f7t12.set_visible(True)
        # set answer-buttons sensitive and next-button insensitive
        self.button_A.set_sensitive(True)
        self.button_B.set_sensitive(True)
        self.button_C.set_sensitive(True)
        self.button_D.set_sensitive(True)
        self.button_next.set_sensitive(False)
        # set comment
        self.label_comment.set_text(
            "Welche Antwort halten Sie für die richtige?")
        # get Q and A string
        self.q_a = gr_handle_gc.q_and_a(self.level + 1)
        #self.q_a.set_level(self.level + 1)
        self.q_a.load_content()
        self.q_a.mix_answers()
        self.label_question.set_text(self.q_a.q_a_container[0])
        self.label_answerA.set_text(self.q_a.q_a_container[1])
        self.label_answerB.set_text(self.q_a.q_a_container[2])
        self.label_answerC.set_text(self.q_a.q_a_container[3])
        self.label_answerD.set_text(self.q_a.q_a_container[4])
        self.correct_ans = int(self.q_a.q_a_container[5])
    # FUNCTION: ingame ---------------------------------------------------- END
        
    # FUNCTION: screen level updater ------------------------------------ START
    def screen_level_upd8(self):
        if self.level == 0:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_1.png')
        elif self.level == 1:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_2.png')
        elif self.level == 2:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_3.png')
        elif self.level == 3:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_4.png')
        elif self.level == 4:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_5.png')
        elif self.level == 5:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_6.png')
        elif self.level == 6:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_7.png')
        elif self.level == 7:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_8.png')
        elif self.level == 8:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_9.png')
        elif self.level == 9:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_10.png')
        elif self.level == 10:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_11.png')
        elif self.level == 11:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_12.png')
        elif self.level == 12:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_13.png')
        elif self.level == 13:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_14.png')
        elif self.level == 14:
            self.image_level_screen.set_from_file(
                'share/geldrausssch-data/img/level_screen_15.png')
    # -------------------------------------------------------------------------

    def handle_answer(self, given_ans):
        """
        handles submitted answer when next-button is clicked
        disables answer-buttons
        checks given answer and shows comment
        raises level when answer correct, ends current game when wrong
        sets gameover variable to TRUE
        reactivates next-button
        """
        # block jokers
        self.button_3366.set_sensitive(False)
        self.button_5050.set_sensitive(False)
        self.button_newq.set_sensitive(False)
        
        # set all answer-buttons to not sensitive
        self.button_A.set_sensitive(False)
        self.button_B.set_sensitive(False)
        self.button_C.set_sensitive(False)
        self.button_D.set_sensitive(False)
        
        if given_ans == self.correct_ans:
            # CORRECT: next answer
            self.level = self.level + 1
            comment_string = gr_handle_gc.get_comment(self.level)
            self.label_comment.set_markup('<b><span color="blue">Richtig! '
                                          '</span></b>' + comment_string)
            # Show commentator image for wrong answer
            self.image_f7t12.set_visible(False)
            self.image_correct.set_visible(True)
            
        else:
            # WRONG: end game
            correct_alpha = ['A', 'B', 'C', 'D']
            gameover_message = (
                beehivelib.get_rnd_txtfile_line('share/geldrausssch'
                    '-data/lang/de/gameover_comments.txt')
                + ' Die richtige Antwort wäre "'
                + correct_alpha[self.correct_ans - 1]
                + '" gewesen. '
                + beehivelib.get_rnd_txtfile_line(
                    'share/geldrausssch-data/lang/de/gameover_'
                    'comments_long.txt'))
            self.label_comment.set_markup(gameover_message)
            
            # Show commentator image for correct answer
            self.image_f7t12.set_visible(False)
            self.image_wrong.set_visible(True)
            # Set gameover-status
            self.gameover = True
        # activate button next
        self.button_next.set_sensitive(True)
        # Give Default to Next Button
        self.button_next.grab_default()

    def gameover_procedure(self):
        """
        resets game in case of gameover and writes to highscore
        """
        # set commentator image neutral
        self.image_wrong.set_visible(False)
        self.image_correct.set_visible(False)
        self.image_f7t12.set_visible(True)
        # set buttons sensitive
        self.button_start.set_sensitive(True)
        self.button_extend.set_sensitive(True)
        # reset jokers
        self.button_3366.set_visible(True)
        self.button_5050.set_visible(True)
        self.button_newq.set_visible(True)
        # go back to welcome screen
        self.notebook_switch.set_current_page(
            self.notebook_switch.page_num(self.vbox_start))
        # blank answers and question for next game
        self.label_question.set_text("")
        self.label_answerA.set_text("")
        self.label_answerB.set_text("")
        self.label_answerC.set_text("")
        self.label_answerD.set_text("")
        # write highscore
        if self.level > 0:
            if self.level == 15:
                # WON - Maximum Highscore reached
                self.player_name = '*' + self.player_name + '*'
                
            gr_handle_gc.highscore(self.level,
                                   self.correct_ans,
                                   self.mlevel[self.level],
                                   self.player_name)
            
        # reset player name
        self.player_name = ""
        # reset game status
        self.gameover = False
        # give "start game" button default
        self.button_start.grab_default()
    
    # CALLBACKS
    # Callback: Close
    def on_window_main_delete_event(self, *args):
        self.quit()
    
    # Callback: Button Start -------------------------------------------- START
    def on_button_start_clicked(self, *args):
        """
        checks entered player name
        resets level
        set player name in status-bar
        """
        # get player name from entry field
        self.player_name = str(self.entry_name.get_text())
        
        # IF: name was entered
        if len(self.player_name) > 0:
            # reset variables
            self.level = 0
            # show player-name in status-bar
            self.label_player.set_text(self.player_name)
            # go to games tab
            self.notebook_switch.set_current_page(
                self.notebook_switch.page_num(self.hbox_ingame))
            # set buttons insensitive
            self.button_start.set_sensitive(False)
            self.button_extend.set_sensitive(False)
            # display welcome comment
            self.label_comment.set_text(
                'Herzlich willkommen zu GeldRau$$$ch, '
                + self.player_name
                + '. Mein Name ist F7-T12. Ich bin der Spielmeister heute. '
                'Ich denke wir werden eine Menge Spaß haben, auf dem Weg zu '
                'einer Milliarde Taler. Los gehts!')
            # Make Next Button Default
            self.button_next.grab_default()
                
        # ELSE: no name provided
        else:
            self.label_welcome.set_markup(
                '<b><span color="red">Bitte Namen eintragen!</span></b>')
    # Callback: Button Start ---------------------------------------------- END

    # Callback: Button Highscore ---------------------------------------- START
    def on_button_highscore_clicked(self, button):
        # Open Highscore Window
        highscore_win = highscore.HighScore()
        highscore_win.run()
    # Callback: Button Highscore ------------------------------------------ END

    # BUTTON: Help ------------------------------------------------------ START
    def on_button_help_clicked(self, button):
        help_win = help_dialog.HelpWindow()
        help_win.configure(window_title = 'GeldRau$$$ch Hilfe')
        help_win.run()
    # BUTTON: Help -------------------------------------------------------- END
    
    # Callback: Button Extend
    def on_button_extend_clicked(self, *args):
        extend_dialog = extend.ExtendWin()
        extend_dialog.run()

    # Callback: Button Exit
    def on_button_exit_clicked(self, *args):
        self.quit()

    # Callback: Button A
    def on_button_A_clicked(self, *args):
        self.handle_answer(1)

    # Callback: Button B
    def on_button_B_clicked(self, *args):
        self.handle_answer(2)

    # Callback: Button C
    def on_button_C_clicked(self, *args):
        self.handle_answer(3)

    # Callback: Button D
    def on_button_D_clicked(self, *args):
        self.handle_answer(4)
        
    # Callback: Button 5050 Joker
    def on_button_5050_clicked(self, *args):
        self.q_a.wizards_card_50_50()
        self.label_answerA.set_text(self.q_a.q_a_container[1])
        self.label_answerB.set_text(self.q_a.q_a_container[2])
        self.label_answerC.set_text(self.q_a.q_a_container[3])
        self.label_answerD.set_text(self.q_a.q_a_container[4])
        self.button_5050.set_visible(False)
        self.button_3366.set_sensitive(False)
        self.button_newq.set_sensitive(False)

    # Callback: Button 3366 Joker
    def on_button_3366_clicked(self, *args):
        self.q_a.wizards_card_33_66()
        self.label_answerA.set_text(self.q_a.q_a_container[1])
        self.label_answerB.set_text(self.q_a.q_a_container[2])
        self.label_answerC.set_text(self.q_a.q_a_container[3])
        self.label_answerD.set_text(self.q_a.q_a_container[4])
        self.button_3366.set_visible(False)
        self.button_5050.set_sensitive(False)
        self.button_newq.set_sensitive(False)

    # Callback: Button New Question Joker
    def on_button_newq_clicked(self, *args):
        self.ingame() # restart level
        self.button_newq.set_visible(False)
        self.button_5050.set_sensitive(False)
        self.button_3366.set_sensitive(False)

    # Callback: Button Next
    def on_button_next_clicked(self, *args):
        # reset jokers
        self.button_3366.set_sensitive(True)
        self.button_5050.set_sensitive(True)
        self.button_newq.set_sensitive(True)
        # check for gameover
        if not self.gameover and self.level < 15:
            # change level screen image
            self.screen_level_upd8()
            # load next level
            self.ingame()
        else:
            if self.level == 15:
                # Switch to victory tab
                self.notebook_switch.set_current_page(
                    self.notebook_switch.page_num(self.vbox_victory))
                # WON, Maximum Highscore reached
                self.label_victory.set_text(
                    'Herzlichen Glückwunsch, '
                    + self.player_name
                    + '! Sie haben die letzte Stufe und '
                    'somit höchste Punktzahl erreicht. Sie haben gezeigt, '
                    'dass Sie ein außergewöhnliches Allgemeinwissen besitzen. '
                    'Ich hoffe wir sehen uns irgendwann einmal wieder, für '
                    'eine weitere spannende Partie "GeldRau$$$ch!')
            else:
                # call gameover procedure
                self.gameover_procedure()
                
    # Callback: Button Victory ------------------------------------------------
    def on_button_victory_clicked(self, *args):
        # call gameover procedure
        self.gameover_procedure()
    # -------------------------------------------------------------------------

    def on_button_about_clicked(self, *args):
        """
        opens the about dialog window
        """
        # start dialog window loop
        self.dialog_about.run()
        # hide dialog
            # if using dialog_about.destroy(), it can be shown only once
        self.dialog_about.hide()

# START APPLICATION
    # if attribute __name__ is __main__, means if application is called,
    # not imported, start app
if __name__ == '__main__':
    app = GeldRauSSSch()
    app.run()
