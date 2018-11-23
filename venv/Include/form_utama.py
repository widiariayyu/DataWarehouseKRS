import wx
class MyDialog(wx.Dialog):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="Options")

        radio1 = wx.RadioButton( self, -1, " Radio1 ", style = wx.RB_GROUP )
        radio2 = wx.RadioButton( self, -1, " Radio2 " )
        radio3 = wx.RadioButton( self, -1, " Radio3 " )

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(radio1, 0, wx.ALL, 5)
        sizer.Add(radio2, 0, wx.ALL, 5)
        sizer.Add(radio3, 0, wx.ALL, 5)

        for i in range(3):
            chk = wx.CheckBox(self, label="Checkbox #%s" % (i+1))
            sizer.Add(chk, 0, wx.ALL, 5)
        self.SetSizer(sizer)


########################################################################
class MyForm(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Form Utama")

        # Add a panel so it looks the correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)

        menuBar = wx.MenuBar()
        menuBar2 = wx.MenuBar()
        fileMenu = wx.Menu()

        optionsItem = fileMenu.Append(wx.NewId(), "Options",
                                      "Show an Options Dialog")
        self.Bind(wx.EVT_MENU, self.onOptions, optionsItem)

        exitMenuItem = fileMenu.Append(wx.NewId(), "Exit",
                                       "Exit the application")
        self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)

        menuBar.Append(fileMenu, "&File")
        menuBar2.Append(fileMenu, "&Report")
        self.SetMenuBar(menuBar)

    #----------------------------------------------------------------------
    def onExit(self, event):
        """"""
        self.Close()

    #----------------------------------------------------------------------
    def onOptions(self, event):
        """"""
        dlg = MyDialog()
        dlg.ShowModal()
        dlg.Destroy()

#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()