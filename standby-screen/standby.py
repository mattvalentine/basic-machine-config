#!/usr/bin/env python3
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio

import socket
from netifaces import interfaces, ifaddresses, AF_INET
from pathlib import Path


def on_activate(app):
    window = Gtk.ApplicationWindow(application=app)
    window.set_default_size(
        window.get_display().get_primary_monitor().get_geometry().width,
        window.get_display().get_primary_monitor().get_geometry().height,
    )
    hostname = socket.gethostname()
    all_addresses = []
    for ifaceName in interfaces():
        addresses = [
            i["addr"]
            for i in ifaddresses(ifaceName).setdefault(
                AF_INET, [{"addr": "No IP addr"}]
            )
        ]
        all_addresses.append(" ".join(addresses))
    addresses_string = "\n".join(
        [
            address
            for address in all_addresses
            if address.find("127.") != 0 and address.find("No IP addr") != 0
        ]
    )
    label = Gtk.Label(label=f"{hostname}\n{addresses_string}")
    window.set_child(label)
    display = Gtk.Widget.get_display(window)
    provider = Gtk.CssProvider.new()
    theme_path = Path(__file__).parent.absolute() / "theme.css"
    fname = Gio.file_new_for_path(str(theme_path))
    provider.load_from_file(fname)
    Gtk.StyleContext.add_provider_for_display(
        display, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
    window.present()


app = Gtk.Application(application_id="com.deeplocal.standby")
app.connect("activate", on_activate)
app.run(None)
