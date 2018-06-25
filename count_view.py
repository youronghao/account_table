# -*- coding:utf-8 -*-
import os
import wx
from my_wxpython import count_action
from my_wxpython.base import *

__author__ = 'you'
__create_time__: '2017/8/25 0:41'


class Panel(wx.Panel, BaseMixin):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(400, 700),
                          style=wx.TAB_TRAVERSAL)

        self.year_choices = []
        config_dir = r"G:\个人账户\账户单"
        for i in os.listdir(config_dir):
            self.year_choices.append(i)

        root = wx.BoxSizer(wx.VERTICAL)

        root.SetMinSize(wx.Size(100, -1))
        # first_sizer = wx.BoxSizer(wx.VERTICAL)

        # first_sizer.AddSpacer(10)

        ex_tool = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"查询功能"), wx.VERTICAL)

        ex_area = wx.FlexGridSizer(8, 6, 0, 0)
        ex_area.SetFlexibleDirection(wx.BOTH)
        ex_area.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # 扩展按钮
        self.static_year = wx.StaticText(ex_tool.GetStaticBox(), wx.ID_ANY, u"查询的账户", wx.DefaultPosition,
                                         wx.Size(60, -1), 0)
        self.static_year.SetForegroundColour((220, 87, 18))
        ex_area.Add(self.static_year, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.year = wx.ComboBox(ex_tool.GetStaticBox(), wx.ID_ANY, u"{}".format(self.year_choices[0]),
                                wx.DefaultPosition,
                                wx.Size(110, -1),
                                self.year_choices, 0)
        ex_area.Add(self.year, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.static_month = wx.StaticText(ex_tool.GetStaticBox(), wx.ID_ANY, u"查询的月份", wx.DefaultPosition,
                                          wx.Size(60, -1),
                                          0)
        self.static_month.SetForegroundColour((220, 87, 18))
        ex_area.Add(self.static_month, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        month_choice = ["1月", "2月", "3月", "4月", "5月", "6月", "7月",
                        "8月", "9月", "10月", "11月", "12月"]
        self.month = wx.ComboBox(ex_tool.GetStaticBox(), wx.ID_ANY, u"{}".format(month_choice[0]), wx.DefaultPosition,
                                 wx.Size(60, -1),
                                 month_choice, 0)
        ex_area.Add(self.month, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.btn_log_tool = wx.Button(ex_tool.GetStaticBox(), wx.ID_ANY, u"查询", wx.DefaultPosition,
                                      wx.Size(60, 28), 0)
        ex_area.Add(self.btn_log_tool, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.Bind(wx.EVT_BUTTON, self.wrapper(count_action.query), self.btn_log_tool)

        self.btn_open_work = wx.Button(ex_tool.GetStaticBox(), wx.ID_ANY, u"打开账户", wx.DefaultPosition,
                                       wx.Size(60, 28), 0)
        ex_area.Add(self.btn_open_work, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.Bind(wx.EVT_BUTTON, self.wrapper(count_action.open_work_dir), self.btn_open_work)

        # 结束扩展
        ex_tool.Add(ex_area, 0, wx.ALIGN_CENTER)

        # first_sizer.Add(ex_tool, 1, wx.EXPAND, 5)

        root.Add(ex_tool, 1, wx.EXPAND, 5)

        # right = wx.BoxSizer(wx.VERTICAL)

        # right.AddSpacer(10)

        control_output_area = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"账户情况"), wx.VERTICAL)

        self.result = wx.TextCtrl(control_output_area.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                  wx.Size(500, 700), wx.TE_MULTILINE)
        control_output_area.Add(self.result, 0, wx.EXPAND, 5)

        # right.Add(control_output_area, 1, wx.EXPAND, 5)

        root.Add(control_output_area, 1, wx.EXPAND, 5)

        self.SetSizer(root)
        self.Layout()
