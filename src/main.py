import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .controllers.AppController import AppController

App = AppController()
App.show()
Gtk.main()
