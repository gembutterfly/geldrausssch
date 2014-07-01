#! /usr/bin/env python3

"""
GUI Highscore
"""

# IMPORT
from gi.repository import Gtk

class HighScore(object):
    """
    Reads Highscore from a textfile, sorts the list descending and displays it

    USAGE:
        app = beehivelibgui.HighScore()
        app.run()

        # optional:
        app.configure(
            highscore_file_name = 'highscore.txt', window_title = 'Highscore')
    """
    def __init__(self):
        """
        Initialize Window
        """
        # INITIALIZE
        # GTK.BUILDER ---------------------------------------------------------
        self.dialog_builder = Gtk.Builder()
        self.dialog_builder.add_from_file(
            "share/geldrausssch-data/ui/highscore.glade")
        self.dialog_builder.connect_signals(self)
        # IMPORT
            # WINDOWS
        self.window_main = self.dialog_builder.get_object('window_main')
            # TEXTVIEW
        self.textview_names = self.dialog_builder.get_object(
            'textview_names')
        self.textview_highscore = self.dialog_builder.get_object(
            'textview_highscore')
        # configure objects
        self.highscore_file_name = 'share/geldrausssch-data/highscore.txt'
        self.window_title = 'Highscore'
        self.names = ""
        self.highscore = ""
        # ---------------------------------------------------------------------

    # RUN ---------------------------------------------------------------------
    def run(self):
        # load from file
        with open(self.highscore_file_name,'r') as hsfile:
            tmp_hs = []
            hs = []
            for line_num, line_cont in enumerate(hsfile, start=1):
                tmp_hs.append(line_cont)
            for i in tmp_hs:
                hs.append(i.split(';'))
            hs.sort(reverse=True)
        names = ''
        points = ''
        for i in hs:
            names = names + i[1] + '\n'
            points = points + i[2]
        textbuffer = self.textview_names.get_buffer()
        textbuffer.set_text(names)
        textbuffer = self.textview_highscore.get_buffer()
        textbuffer.set_text(points)

        # set window title
        self.window_main.set_title(self.window_title)

        # open window
        self.window_main.show_all()
        Gtk.main()
    # -------------------------------------------------------------------------

    # FUNCTIONS ---------------------------------------------------------------
    def configure(
            self,
            highscore_file_name = 
                'share/geldrausssch-data/lang/de/highscore.txt',
            window_title = 'Highscore'):
        self.highscore_file_name = highscore_file_name
        self.window_title = window_title
                    
    # CALLBACKS ---------------------------------------------------------------
    def on_window_main_delete_event(self, *args):
        Gtk.main_quit()
        
# START
if __name__ == '__main__':
    app = HighScore()
    app.run()
