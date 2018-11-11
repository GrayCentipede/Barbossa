import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from .handlers.AppHandler import Handler

class AppController(object):

    builder = None
    app_handler = None

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('./src/views/MainApp.glade')
        self.app_handler = Handler(self.builder)
        self.window = self.builder.get_object('App')
        self.app_handler.set_downloader()
        self.builder.connect_signals(self.app_handler)
        self.window.connect('destroy', Gtk.main_quit)

    def show(self):
        self.window.show_all()
