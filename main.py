from os.path import islink
import pathlib
import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf, Gdk

from config import config
from cmdline import args

user_home = os.path.expanduser("~")

class Window(Gtk.Window):
    """Main window"""

    def __init__(self):
        super().__init__(title="H")
        main_box = Gtk.Grid()
        self.add(main_box)

        row = 0 
        col = 0
        for file in os.listdir(f"{user_home}/.local/pmenu"):
            pixbuf = GdkPixbuf.Pixbuf.new_from_file(
                f"{user_home}/.local/pmenu/{file}"
            )
            img = Gtk.Image.new_from_pixbuf(pixbuf)
            btn = Gtk.Button()
            btn.connect("clicked", self.on_button_clicked, file, f"{user_home}/.local/pmenu/")
            aspect_ratio = pixbuf.get_width() / pixbuf.get_height()
            scaled_width = 240
            scaled_height = int(scaled_width / aspect_ratio)
            scaled_buf = pixbuf.scale_simple(
                scaled_width, scaled_height, GdkPixbuf.InterpType.BILINEAR
            )
            img = Gtk.Image.new_from_pixbuf(scaled_buf)
            btn.add(img)
            main_box.attach(btn, row, col, 1 ,1)
            col = col+1 if col < 3 else 0
            row = row + 1 if col == 0 else row
            

        self.connect("key-press-event", self.on_key_pressed)

    def on_key_pressed(self, widget, event):
        """On clicking q, save the data and quit"""
        if event.keyval == Gdk.KEY_q:
            Gtk.main_quit()

    def on_button_clicked(self, widget, filename, parent):
        print(parent+filename)
        Gtk.main_quit()

    def print_window_size(self, widget, data=None):
        print(widget.get_size)

    def main_quit(self):
        Gtk.main_quit()


def compress_images(directory="Pictures/wp"):
    from PIL import Image

    if not os.path.exists(f"{user_home}/.local/pmenu"):
        os.makedirs(f"{user_home}/.local/pmenu")
    for filename in os.listdir(f"{user_home}/{directory}"):
        print(filename)
        if os.path.islink(f"{user_home}/{directory}/{filename}"):
            continue
        base_width = 240
        image = Image.open(f'{user_home}/Pictures/wp/{filename}')
        width_percent = (base_width / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(width_percent)))
        image = image.resize((base_width, hsize))
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
        image.save(f'{user_home}/.local/pmenu/{filename}')
        

# widget = Gtk.Box()
# print(dir(widget.props))

if not args.compress:
    win = Window()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
else:
    compress_images()
