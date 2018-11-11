import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
import shutil

class FileHandler(object):

    builder = None
    source_path = None
    media_file_name = None
    target_path = None

    def __init__(self, builder, source_path):
        self.source_path = source_path
        self.media_file_name = os.path.basename(source_path)

    def on_selected(self, widget):
        self.target_path = widget.get_filename()

    def on_save_button_clicked(self, button):
        shutil.move(self.source_path, self.target_path + "/" + self.media_file_name)
        Gtk.main_quit()
