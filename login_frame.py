#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.5 on Mon Oct 21 10:09:44 2013

import wx
import time
# begin wxGlade: extracode
# end wxGlade

#TODO implement autoclose and updates.

class my_login_frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: my_login_frame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, -1, "login:", style=wx.ALIGN_CENTRE)
        self.text_ctrl_2 = wx.TextCtrl(self, -1, "")
        self.label_2 = wx.StaticText(self, -1, "password:")
        self.text_ctrl_3 = wx.TextCtrl(self, -1, "")
        self.button_1 = wx.Button(self, -1, "Submit")
        self.label_3 = wx.StaticText(self, -1, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.getvals, self.button_1)
        # end wxGlade

        self.login_info = "" #login info for user

    def __set_properties(self):
        # begin wxGlade: my_login_frame.__set_properties
        self.SetTitle("log info")
        self.button_1.SetMinSize((85, 33))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: my_login_frame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add((10, 20), 0, 0, 0)
        sizer_3.Add(self.label_1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add((49, 20), 0, 0, 0)
        sizer_3.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_3, 1, 0, 0)
        sizer_4.Add((10, 20), 0, 0, 0)
        sizer_4.Add(self.label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add((20, 20), 0, 0, 0)
        sizer_4.Add(self.text_ctrl_3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_4, 1, 0, 0)
        sizer_5.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_5.Add(self.label_3, 0, wx.SHAPED, 0)
        sizer_2.Add(sizer_5, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

    def get_text(self):
        return self.login_info

    def getvals(self, event):  # wxGlade: my_login_frame.<event_handler>
        self.login_info = self.text_ctrl_2.GetValue() + "\n" + self.text_ctrl_3.GetValue() + "\n"
        #TODO add server declaration
            #checks to see either string has anything in them besides whitespace
        if (self.text_ctrl_2.GetValue().strip() and self.text_ctrl_3.GetValue().strip()):
            self.label_3.SetLabel("waiting...\nsuccess!")
            #TODO add server resulsts here.
            self.config = open("config.cfg", "w")
            self.config.write(self.get_text())
            self.config.close()

        else:
            self.label_3.SetLabel("Error with \nlogin/pass")


# end of class my_login_frame
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    login = my_login_frame(None, -1, "")
    app.SetTopWindow(login)
    login.Show()
    app.MainLoop()
