import wx
import wx.xrc
import wx.grid
import mysql.connector

mydb2 = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_simak"
)

class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(700, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

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

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Masukan NIM", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        gSizer3.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_inputnim = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.m_inputnim, 0, wx.ALL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Lihat", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.m_button1, 0, wx.ALL, 5)

        fgSizer2.Add(gSizer3, 1, wx.EXPAND, 5)

        bSizer4.Add(fgSizer2, 1, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid3 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid3.CreateGrid(10, 5)
        self.m_grid3.EnableEditing(True)
        self.m_grid3.EnableGridLines(True)
        self.m_grid3.EnableDragGridSize(False)
        self.m_grid3.SetMargins(20, 20)

        # Columns
        self.m_grid3.SetColSize(0, 180)
        self.m_grid3.SetColSize(1, 120)
        self.m_grid3.SetColSize(2, 130)
        self.m_grid3.EnableDragColMove(False)
        self.m_grid3.EnableDragColSize(True)
        self.m_grid3.SetColLabelSize(30)
        self.m_grid3.SetColLabelValue(0, u"Kode Matakuliah")
        self.m_grid3.SetColLabelValue(1, u"Matakuliah")
        self.m_grid3.SetColLabelValue(2, u"SKS")
        self.m_grid3.SetColLabelValue(3, u"Indeks")
        self.m_grid3.SetColLabelValue(4, u"Nilai")
        self.m_grid3.SetColLabelValue(5, wx.EmptyString)
        self.m_grid3.SetColLabelValue(6, wx.EmptyString)
        self.m_grid3.SetColLabelValue(7, wx.EmptyString)
        self.m_grid3.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid3.EnableDragRowSize(True)
        self.m_grid3.SetRowLabelSize(50)
        self.m_grid3.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid3.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer5.Add(self.m_grid3, 0, wx.ALL, 5)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"Indeks Prestasi Semester (IPS)", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        gSizer2.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textIPS = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_textIPS, 0, wx.ALL, 5)

        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Indeks Prestasi  Kumulatif (IPK)", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        gSizer2.Add(self.m_staticText51, 0, wx.ALL, 5)

        self.m_textIPK = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_textIPK, 0, wx.ALL, 5)

        bSizer5.Add(gSizer2, 1, wx.EXPAND, 5)

        bSizer4.Add(bSizer5, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        self.m_button1.Bind(wx.EVT_BUTTON, self.submit)

    def __del__(self):
        pass

    def submit(self,event):
        self.m_grid3.ClearGrid()
        tahun = self.m_tahun.GetStringSelection()
        semester = self.m_semester.GetStringSelection()
        total_nilai = 0
        total_sks = 0

        # ipk = self.m_textIPK.AppendText()
        if semester == 'Ganjil':
            semester = 1
        elif semester == 'Genap':
            semester = 2
        elif semester == 'Pendek':
            semester = 3
        else:
            semester = 'Remidi'
        mycursor = mydb2.cursor()
        sql = "SELECT kode_matkul,nama_matkul,sks,indeks,nilai  FROM fact_khs INNER JOIN dim_matkul USING (kode_matkul) INNER JOIN dim_semester USING (id_semester) INNER JOIN dim_mahasiswa USING (id_mhs) WHERE id_semester ='"+str(semester)+"' && YEAR(tahun_ajaran)='"+tahun+"' && NIM LIKE '%"+self.m_inputnim.Value+"%'"
        mycursor.execute(sql)

        rows = mycursor.fetchall()
        for i in range(0, len(rows)):
            total_nilai = total_nilai + rows[i][4]
            total_sks = total_sks + rows[i][2]
            for j in range(0, len(rows[i])):
                self.m_grid3.SetCellValue(i, j, str(rows[i][j]))
        self.m_inputnim.SetFocus()
        self.m_textIPS.Clear()
        self.m_textIPK.Clear()
        self.m_textIPS.AppendText(str(total_nilai / total_sks))

        ipk = "SELECT IPK FROM dim_indeks INNER JOIN dim_mahasiswa USING (id_mhs) INNER JOIN dim_semester USING (id_semester)  WHERE id_semester ='"+str(semester)+"' && YEAR(tahun_ajaran)='"+tahun+"' && NIM LIKE '%"+self.m_inputnim.Value+"%'"
        mycursor.execute(ipk)
        a = mycursor.fetchone()
        self.m_textIPK.AppendText(str(a[0]))

class MainApp(wx.App):
    def OnInit(self):
        mainFrame = MyFrame2(None)
        mainFrame.Show(True)
        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
