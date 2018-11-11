import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, GdkPixbuf
from gi.repository.GdkPixbuf import Pixbuf
from threading import Thread
import glob

from ...models.Downloader import Downloader
from ...models.ImageMiner import ImageMiner
from ...models.Media import Media

from ..FileChooserController import FileChooserController

from ..ImageViewer import ImageViewer

class Handler(object):

    builder = None
    app_downloader = None
    image_miner = None
    media = None
    viewer = None

    def __init__(self, builder):
        self.builder = builder

    def set_text(self, msg):
        text_view = self.builder.get_object('log')
        if (msg):
            buffer = Gtk.TextBuffer()
            buffer.set_text(msg)
            text_view.set_buffer(buffer)

    def set_image(self, img_path):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = img_path,
                                                         width=200, height=200,
                                                         preserve_aspect_ratio=True)

        self.builder.get_object('album_image').set_from_pixbuf(pixbuf)

    def update_log(self, msg):
        GLib.idle_add(self.set_text, msg)

    def update_img(self, img_path):
        GLib.idle_add(self.set_image, img_path)

    def on_download_complete(self):
        self.update_log('Downloading images...')
        self.media = Media()
        self.media.load(glob.glob('temp/**/*.mp3', recursive = True)[0])
        self.set_image_miner(self.app_downloader.title + ' ' + self.app_downloader.uploader)
        Thread(target = self.image_miner.mine).start()

    def enable_buttons(self):
        self.builder.get_object('prev_img').set_sensitive(True)
        self.builder.get_object('next_img').set_sensitive(True)
        self.builder.get_object('save_button').set_sensitive(True)
        self.builder.get_object('artist_entry').set_sensitive(True)
        self.builder.get_object('album_entry').set_sensitive(True)
        self.builder.get_object('title_entry').set_sensitive(True)
        self.builder.get_object('year_entry').set_sensitive(True)
        self.builder.get_object('track_entry').set_sensitive(True)
        self.builder.get_object('genre_entry').set_sensitive(True)
        self.builder.get_object('search_entry').set_sensitive(True)
        self.builder.get_object('search_button').set_sensitive(True)

    def disable_buttons(self):
        self.builder.get_object('prev_img').set_sensitive(False)
        self.builder.get_object('next_img').set_sensitive(False)
        self.builder.get_object('save_button').set_sensitive(False)
        self.builder.get_object('search_entry').set_sensitive(False)
        self.builder.get_object('search_button').set_sensitive(False)

    def on_images_download_complete(self):
        self.update_log('Download complete.')
        self.enable_buttons()

        self.builder.get_object('artist_entry').set_text(self.app_downloader.uploader)
        self.builder.get_object('title_entry').set_text(self.app_downloader.title)

        self.viewer = ImageViewer()

        self.update_img(self.viewer.get_actual())

    def set_downloader(self):
        self.app_downloader = Downloader()
        self.app_downloader.set_listener(self.update_log)
        self.app_downloader.set_on_download_complete_action(self.on_download_complete)

    def set_image_miner(self, query):
        if (self.image_miner is not None):
            self.image_miner.clean_dir()

        self.image_miner = ImageMiner(query, 10)
        self.image_miner.set_on_download_complete_action(self.on_images_download_complete)

    def set_media(self, media):
        self.media = media

    def on_download_button_clicked(self, button):
        url = self.builder.get_object('url_entry').get_text()
        Thread(target = self.app_downloader.download, args = (url,)).start()

    def on_prev_img_clicked(self, button):
        self.update_img(self.viewer.get_previous())

    def on_next_img_clicked(self, button):
        self.update_img(self.viewer.get_next())

    def on_search_button_clicked(self, button):
        query = self.builder.get_object('search_entry').get_text()
        GLib.idle_add(self.disable_buttons)
        self.update_log('Downloading images...')
        self.set_image_miner(query)
        Thread(target = self.image_miner.mine).start()

    def on_save_button_clicked(self, button):
        self.media.set_artist(self.builder.get_object('artist_entry').get_text())
        self.media.set_album(self.builder.get_object('album_entry').get_text())
        self.media.set_title(self.builder.get_object('title_entry').get_text())
        self.media.set_year(self.builder.get_object('year_entry').get_text())
        self.media.set_track(self.builder.get_object('track_entry').get_text())
        self.media.set_genre(self.builder.get_object('genre_entry').get_text())
        self.media.set_image(self.viewer.get_actual())

        self.media.save_changes()

        GLib.idle_add(FileChooserController(self.media.get_path()).show())
