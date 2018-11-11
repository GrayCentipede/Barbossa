import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from .handlers.FileHandler import FileHandler

class FileChooserController(object):

    def __init__(self, media_path):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('./src/views/FileChooser.glade')
        self.file_chooser_handler = FileHandler(self.builder, media_path)
        self.window = self.builder.get_object('FileChooser')
        self.builder.connect_signals(self.file_chooser_handler)

    def show(self):
        self.window.show_all()
