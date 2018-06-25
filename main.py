# -*- coding:utf-8 -*-
import sys
import wx
import wx.xrc
from my_wxpython.count_view import Panel
from my_wxpython.myico import ico

__author__ = 'you'
__create_time__: '2017/8/25 0:20'


class MyFrame(wx.Frame):
    def __init__(self, parent, title="账目表"):
        super(MyFrame, self).__init__(parent, title=title, size=(500, 700))

        self.SetIcon(ico.GetIcon())

        self.notebook = wx.Notebook(self)

        self.panel = Panel(self.notebook)
        self.notebook.AddPage(self.panel, "查询")
        # self.SetBackgroundColour(wx.WHITE)

        # self.Centre(wx.BOTH)

    def write(self, astr):
        self.panel.result.AppendText(astr)


if __name__ == '__main__':
    try:
        toolkit = wx.App()
        frame = MyFrame(None)
        frame.Show()
        frame.Refresh()
        sys.stdout = frame
        toolkit.MainLoop()
    except:
        import traceback

        traceback.print_exc()
