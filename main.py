import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os

class Handler:
    def on_rokuWindow_destroy(self, *args):
        Gtk.main_quit()
  
    def on_rokuWindow_destroy_event(self, *args):
        Gtk.main_quit()

    def on_powerButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/Power"
        os.system(command)
        print("POWER\n")

    def on_backButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/Back"
        os.system(command)
        print("back\n")

    def on_homeButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/Home"
        os.system(command)
        print("home\n")

    def on_vupButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/VolumeUp"
        os.system(command)
        print("VolUP\n")

    def on_vdwnButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/VolumeDown"
        os.system(command)
        print("VolDWNP\n")

    def on_muteButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/VolumeMute"
        os.system(command)
        print("mute\n")

    def on_downButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/Down"
        os.system(command)
        print("down\n")

    def on_upButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/Up"
        os.system(command)
        print("up\n")

    def on_leftButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/Left"
        os.system(command)
        print("left\n")

    def on_rightButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/Right"
        os.system(command)
        print("right\n")

    def on_selectButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/Select"
        os.system(command)
        print("select\n")

    def on_playButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/Play"
        os.system(command)
        print("play\n")

    def on_revButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/Rev"
        os.system(command)
        print("reverse\n")

    def on_fwdButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/Fwd"
        os.system(command)
        print("forward\n")

    def on_hdmi1Button_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/InputHDMI1"
        os.system(command)
        print("hdmi 1\n")

    def on_hdmi2Button_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/InputHDMI2"
        os.system(command)
        print("hdmi 2\n")

    def on_hdmi3Button_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/InputHDMI3"
        os.system(command)
        print("hdmi 3\n")

    def on_antButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/keypress/InputTuner"
        os.system(command)
        print("antenna\n")

    def on_netflixButton_clicked(self, button):
        command = "curl -d '' http://192.168.1.142:8060/launch/12"
        os.system(command)
        print("netflix\n")

builder = Gtk.Builder()
builder.add_from_file("main.glade")
builder.connect_signals(Handler())

window = builder.get_object("rokuWindow")
window.show_all()

Gtk.main()
