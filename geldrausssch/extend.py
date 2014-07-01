#! /usr/bin/env python3

"""
GUI Extend
"""

# IMPORT
from gi.repository import Gtk

class ExtendWin(object):
    """
    Reads ExtendWin from a textfile, sorts the list descending and displays it

    USAGE:
        app = geldrausssch.ExtendWin()
        app.run()
        shows dialog window to extend game content,
        builds string and saves it to the proper file
    """
    def __init__(self):
        # BUILDER
        self.builder_dialog = Gtk.Builder()
        self.builder_dialog.add_from_file(
            "share/geldrausssch-data/ui/gr_gui_dialog_extend.glade")
            # get objects
        self.dialog_extend = self.builder_dialog.get_object('dialog_extend')
        self.extend_entry_a1 = self.builder_dialog.get_object('extend_entry_a1')
        self.extend_entry_a2 = self.builder_dialog.get_object('extend_entry_a2')
        self.extend_entry_a3 = self.builder_dialog.get_object('extend_entry_a3')
        self.extend_entry_a4 = self.builder_dialog.get_object('extend_entry_a4')
        self.extend_entry_q = self.builder_dialog.get_object('extend_entry_q')
        self.label_extend_description = self.builder_dialog.get_object(
                                      'label_extend_description')
        self.comboboxtext_acorr = self.builder_dialog.get_object('comboboxtext_acorr')
        self.comboboxtext_lang = self.builder_dialog.get_object('comboboxtext_lang')
        self.comboboxtext_level = self.builder_dialog.get_object('comboboxtext_level')
        self.dialog_check = self.builder_dialog.get_object('dialog_check')
        self.messagedialog = self.builder_dialog.get_object('messagedialog')
        self.label_check_string = self.builder_dialog.get_object('label_check_string')

    # RUN ---------------------------------------------------------------------
    def run(self):
        response = self.dialog_extend.run()
        # check response of dialogs run()
        if response == Gtk.ResponseType.APPLY:
            #try:
                q_a_string = self.make_qa_string()
                # refresh label to check entried data
                self.label_check_string.set_text(
                    q_a_string
                    + '\nLevel: '
                    + self.comboboxtext_level.get_active_text()
                    + '\nSprache: '
                    + self.comboboxtext_lang.get_active_text())
                print("QA-String: " + q_a_string)
                
                # show string to user and ask for OK: RUN DIALOG_CHECK
                response_check = self.dialog_check.run()
                if response_check == Gtk.ResponseType.OK:
                    self.write_qa_file(q_a_string)
                else:
                    print('Else')
                    self.messagedialog.run()
                    self.messagedialog.destroy() 
                # DESTROY DIALOG_CHECK
                self.dialog_check.destroy()
            #except:
            #   print('Except')
            #   self.messagedialog.run()
            #   self.messagedialog.destroy()         
        self.dialog_extend.destroy()
        
    def write_qa_file(self, q_a_string):
        # write to file
        cont_fname = ('share/geldrausssch-data/lang/'
                      + self.comboboxtext_lang.get_active_text()
                      + '/'
                      + 'gr_QA_'
                      + self.comboboxtext_level.get_active_text()
                      + '.txt')
        print(cont_fname)
        with open(cont_fname,'r') as cont_file:
            text = cont_file.read()
        qalines = text.splitlines()
        qalines.append(q_a_string)
        newtext = ""
        for qaline in qalines:
            newtext += qaline + "\n"
        print(newtext)
        with open(cont_fname,'w') as cont_file:
            cont_file.write(newtext)
            
    def make_qa_string(self):
        textbuffer = self.extend_entry_q.get_buffer()
        q_a_string = (str(textbuffer.get_text(
            start=textbuffer.get_start_iter(),
            end=textbuffer.get_end_iter(),
            include_hidden_chars=False))
            + ';'
            + str(self.extend_entry_a1.get_text())
            + ';'
            + str(self.extend_entry_a2.get_text())
            + ';'
            + str(self.extend_entry_a3.get_text())
            + ';'
            + str(self.extend_entry_a4.get_text())
            + ';'
            + self.comboboxtext_acorr.get_active_text())
        return q_a_string
    
# START
if __name__ == '__main__':
    app = ExtendWin()
    app.run()
