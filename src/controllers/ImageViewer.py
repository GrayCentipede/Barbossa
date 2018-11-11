import glob

class ImageViewer(object):

    directory = 'temp/pictures'
    images_paths = None
    actual = None

    def __init__(self):
        self.images_paths = glob.glob(self.directory + '/**/*.jpg', recursive = True)
        images_png = glob.glob(self.directory + '/**/*.png', recursive = True)
        images_jpeg = glob.glob(self.directory + '/**/*.jpeg', recursive = True)

        self.images_paths.extend(images_png)
        self.images_paths.extend(images_jpeg)

        self.actual = 0

    def get_actual(self):
        return self.images_paths[self.actual]

    def get_previous(self):
        if (self.actual == 0):
            self.actual = len(self.images_paths) - 1
        else:
            self.actual = self.actual - 1

        return self.images_paths[self.actual]

    def get_next(self):
        if (self.actual == len(self.images_paths) - 1):
            self.actual = 0
        else:
            self.actual = self.actual + 1

        return self.images_paths[self.actual]
