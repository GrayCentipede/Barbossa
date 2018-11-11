from mutagen.id3 import ID3, TPE1, TALB, TIT2, TDRC, TCON, TRCK, APIC

class Media(object):

    media = None
    cover = None
    path = None

    def load(self, filename):
        self.media = ID3(filename)
        self.path = filename

    def get_path(self):
        return self.path

    def set_artist(self, artist_name):
        self.media['TPE1'] = TPE1(encoding = 3, text = artist_name)

    def set_album(self, album_name):
        self.media['TALB'] = TALB(encoding = 3, text = album_name)

    def set_title(self, title):
        self.media['TIT2'] = TIT2(encoding = 3, text = title)

    def set_year(self, year):
        self.media['TDRC'] = TDRC(encoding = 3, text = year)

    def set_genre(self, genre):
        self.media['TCON'] = TCON(encoding = 3, text = genre)

    def set_track(self, track):
        self.media['TRCK'] = TRCK(encoding = 3, text = track)

    def set_image(self, img_path):
        with open(img_path, 'rb') as img_bytes:
            self.media['APIC'] = APIC(encoding = 3, mime= 'image/jpeg',
                                      type = 3, desc = u'Cover', data = img_bytes.read())

    def save_changes(self):
        self.media.save()

    def get_info(self):
        total = []
        string = ''
        if self.media is None:
            return '{}'

        for key in self.media.keys():
            total.append( str((key, self.media[key])) )

        return ' '.join(total)
