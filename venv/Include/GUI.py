import wx
import wx.grid
import mysql.connector
# from loop.py import function

mydb2 = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_simak"
)


class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(550, 450), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        gSizer3 = wx.GridSizer(0, 2, 0, 0)


        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Tahun", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        gSizer3.Add(self.m_staticText5, 0, wx.ALL, 5)

        m_tahunChoices = [u"2018", u"2017", u"2016"]
        self.m_tahun = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_tahunChoices, 0)
        self.m_tahun.SetSelection(0)
        gSizer3.Add(self.m_tahun, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Semester", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        gSizer3.Add(self.m_staticText6, 0, wx.ALL, 5)

        m_semesterChoices = [u"Ganjil", u"Genap", u"Pendek", u"Remidi"]
        self.m_semester = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_semesterChoices, 0)
        self.m_semester.SetSelection(0)
        gSizer3.Add(self.m_semester, 0, wx.ALL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Lihat", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.m_button1, 0, wx.ALL, 5)

        fgSizer2.Add(gSizer3, 1, wx.EXPAND, 5)

        bSizer4.Add(fgSizer2, 1, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid2 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid2.CreateGrid(10, 3)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(20, 20)

        # Columns
        self.m_grid2.SetColSize(0, 180)
        self.m_grid2.SetColSize(1, 120)
        self.m_grid2.SetColSize(2, 130)
        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelSize(30)
        self.m_grid2.SetColLabelValue(0, u"Matakuliah")
        self.m_grid2.SetColLabelValue(1, u"SKS")
        self.m_grid2.SetColLabelValue(2, u"Jumlah Mahasiswa")
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelSize(80)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer5.Add(self.m_grid2, 0, wx.ALL, 5)

        bSizer4.Add(bSizer5, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)


        self.m_button1.Bind(wx.EVT_BUTTON, self.submit)

    def __del__(self):
        pass


    def submit(self,event):
        self.m_grid2.ClearGrid()
        tahun = self.m_tahun.GetStringSelection()
        semester = self.m_semester.GetStringSelection()
        if semester == 'Ganjil':
            semester = 1
        elif semester == 'Genap':
            semester = 2
        elif semester == 'Pendek':
            semester = 3
        else:
            semester = 'Remidi'
        mycursor = mydb2.cursor()
        sql = "SELECT nama_matkul,sks,COUNT(nama_mhs) AS total FROM fact_krs INNER JOIN dim_matkul USING (kode_matkul)INNER JOIN dim_mahasiswa USING (id_mhs)WHERE id_semester = '"+str(semester)+"' && YEAR(tanggal)='"+tahun+"' GROUP BY nama_matkul"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for i in range(0, len(rows)):
            for j in range(0, len(rows[i])):
                self.m_grid2.SetCellValue(i, j, str(rows[i][j]))

class MainApp(wx.App):
 def OnInit(self):
  mainFrame = MyFrame1(None)
  mainFrame.Show(True)
  return True

if __name__ == '__main__':
 app = MainApp()
 app.MainLoop()