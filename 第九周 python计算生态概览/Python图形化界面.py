#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/28 14:24
# @File : Python图形化界面.py
# import wx
# app = wx.App(False)
# frame = wx.Frame(None, wx.ID_ANY, "Hello World")
# frame.Show(True)
# app.MainLoop()
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
window = Gtk.Window(title="Hello World")
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()