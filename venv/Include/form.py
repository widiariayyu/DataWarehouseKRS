import wx
import wx.xrc
import ETL
import GUI
import NILAI

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(239, 202), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        gSizer1 = wx.GridSizer(0, 2, 20, 0)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Proses ETL", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        gSizer1.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button10.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        gSizer1.Add(self.m_button10, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Report 1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        gSizer1.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button11.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        gSizer1.Add(self.m_button11, 0, wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Report 2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        gSizer1.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button12.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        gSizer1.Add(self.m_button12, 0, wx.ALL, 5)

        bSizer2.Add(gSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)
        self.m_button10.Bind(wx.EVT_BUTTON, self.etl)
        self.m_button11.Bind(wx.EVT_BUTTON, self.matkul)
        self.m_button12.Bind(wx.EVT_BUTTON,self.ipk)

    def __del__(self):
        pass

    def etl(self,event):


class MainApp(wx.App):
 def OnInit(self):
  mainFrame = MyFrame1(None)
  mainFrame.Show(True)
  return True

if __name__ == '__main__':
 app = MainApp()
 app.MainLoop()