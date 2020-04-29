import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
import ssdp

class Handler:
    def on_rokuWindow_destroy(self, *args):
        Gtk.main_quit()
  
    def on_rokuWindow_destroy_event(self, *args):
        Gtk.main_quit()

    def on_powerButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/Power"
        os.system(command)
        print("POWER\n")

    def on_backButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/Back"
        os.system(command)
        print("back\n")

    def on_homeButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/Home"
        os.system(command)
        print("home\n")

    def on_vupButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/VolumeUp"
        os.system(command)
        print("VolUP\n")

    def on_vdwnButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/VolumeDown"
        os.system(command)
        print("VolDWNP\n")

    def on_muteButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/VolumeMute"
        os.system(command)
        print("mute\n")

    def on_downButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/Down"
        os.system(command)
        print("down\n")

    def on_upButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/Up"
        os.system(command)
        print("up\n")

    def on_leftButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/Left"
        os.system(command)
        print("left\n")

    def on_rightButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/Right"
        os.system(command)
        print("right\n")

    def on_selectButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/Select"
        os.system(command)
        print("select\n")

    def on_playButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/Play"
        os.system(command)
        print("play\n")

    def on_revButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/Rev"
        os.system(command)
        print("reverse\n")

    def on_fwdButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/Fwd"
        os.system(command)
        print("forward\n")

    def on_hdmi1Button_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/InputHDMI1"
        os.system(command)
        print("hdmi 1\n")

    def on_hdmi2Button_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/InputHDMI2"
        os.system(command)
        print("hdmi 2\n")

    def on_hdmi3Button_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/InputHDMI3"
        os.system(command)
        print("hdmi 3\n")

    def on_antButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "keypress/InputTuner"
        os.system(command)
        print("antenna\n")

    def on_netflixButton_clicked(self, button):
        command = "curl -d '' " + mylocation + "launch/12"
        os.system(command)
        print("netflix\n")

    def on_scanButton_clicked(self, button, *args):
        mylocation = ssdp.discover("roku:ecp")
        Foundlabel.set_text(mylocation)
        with open("IPADDRESS.txt", "w") as text_file:
            print(mylocation, file=text_file)
        print(mylocation + "\n")

mylocation = "none"
try:
    with open('IPADDRESS.txt', 'r') as myfile:
        mylist=myfile.readline().split("\n")
        mylocation=mylist[0]
        print(type(mylocation))
except:
    print("no device address file found\n")

builder = Gtk.Builder()
builder.add_from_file("/home/pyplot/roku_remote_replacement/roku_remote_replacement/main.glade")
builder.connect_signals(Handler())

window = builder.get_object("rokuWindow")
window.show_all()

Foundlabel = builder.get_object("foundLabel")
Foundlabel.set_text(mylocation)



Gtk.main()
