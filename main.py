import gi


gi.require_version("Gtk" ,"3.0")
from gi.repository import Gtk, GdkPixbuf, Gdk

class Window(Gtk.Window):
    """Main window"""
    def __init__(self ):
        super().__init__(title="H")
        self.pixbuf = GdkPixbuf.Pixbuf.new_from_file("../../../Pictures/wp/od_abstract.png")
        self.img = Gtk.Image.new_from_pixbuf(self.pixbuf)
        self.btn = Gtk.Button()
        self.btn.add(self.img)
        self.add(self.btn)
    def on_button_clicked(self, widget):
        print("hello world")

    # handler_id = widget.connect("event",callback, data)
# widget = Gtk.Box()
# print(dir(widget.props))

win = Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
