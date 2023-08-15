import gi
import os


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf, Gdk

from config import config


class Window(Gtk.Window):
    """Main window"""

    def __init__(self):
        super().__init__(title="H")
        main_box = Gtk.Grid()
        self.add(main_box)
        # for filename in os.listdir("/home/nitin/Pictures/wp/"):
        #     print(f"/home/nitin/Pictures/wp/{filename}")
        #     pixbuf = GdkPixbuf.Pixbuf.new_from_file(f"/home/nitin/Pictures/wp/{filename}")
        #     img = Gtk.Image.new_from_pixbuf(pixbuf)
        #     btn = Gtk.Button()
        #     aspect_ratio = pixbuf.get_width() / pixbuf.get_height()
        #     scaled_width = 240
        #     scaled_height = int(scaled_width / aspect_ratio)
        #     scaled_buf = pixbuf.scale_simple(scaled_width, scaled_height, GdkPixbuf.InterpType.BILINEAR)
        #     img = Gtk.Image.new_from_pixbuf(scaled_buf)
        #     btn.add(img)
        #     main_box.add(btn)

        row = 0 
        col = 0
        for file in os.listdir("/home/nitin/Pictures/wp/"):
            pixbuf = GdkPixbuf.Pixbuf.new_from_file(
                f"/home/nitin/Pictures/wp/{file}"
            )
            img = Gtk.Image.new_from_pixbuf(pixbuf)
            btn = Gtk.Button()
            btn.connect("clicked", self.on_button_clicked, file, "/home/nitin/Pictures/wp/")
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

    def main_quit():
        Gtk.main_quit()



# widget = Gtk.Box()
# print(dir(widget.props))

win = Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
