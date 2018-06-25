#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import functools
import time
import wx


class BaseMixin(object):

    def wrapper(self, func):
        return functools.partial(func, view=self)

class PopupMenu(object):
    def __init__(self, view):
        self._view = view
        self._popup = wx.Menu()

    def add_item(self, desc, bind_func):
        popup_item = self._popup.Append(-1, desc)
        self._view.Bind(wx.EVT_MENU, bind_func, popup_item)

    def show(self):
        self._view.Bind(wx.EVT_CONTEXT_MENU, self._on_show_popup)

    def _on_show_popup(self, evt):
        pos = evt.GetPosition()
        pos = self._view.ScreenToClient(pos)
        self._view.PopupMenu(self._popup, pos)


class TextCtrlFileDrop(wx.FileDropTarget):
    def __init__(self, target):
        wx.FileDropTarget.__init__(self)
        self.target = target

    def OnDropFiles(self, *args):
        self.target.SetValue(args[-1][0])
        return 1
