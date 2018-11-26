import wx
import wx.grid
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_akademik"
)

mydb2 = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_simak"
)

# class EtlGui(wx.Dialog):
#     def function_select(sql, mydb):
#         mycursor = mydb.cursor()
#         mycursor.execute(sql)
#         myresult = mycursor.fetchall()
#         return myresult
#
#     def function_insert(sql, mydb2):
#         cursor = mydb2.cursor()
#         cursor.execute(sql)
#         mydb2.commit()
#
#     smt = "SELECT * FROM tb_semester"
#     matkul = "SELECT * FROM tb_matkul"
#     pembimbing = "SELECT * FROM tb_PA"
#     prov = "SELECT * FROM tb_provinsi"
#     fakultas = "SELECT * FROM tb_fakultas"
#     prodi = "SELECT id_prodi, nm_prodi, id_fakultas FROM tb_krs INNER JOIN tb_fakultas USING (id_fakultas) INNER JOIN tb_prodi USING (id_prodi) GROUP BY id_fakultas"
#     kab = "SELECT id_kabupaten, nm_kabupaten, id_provinsi FROM tb_mahasiswa INNER JOIN tb_kabupaten USING (id_kabupaten) INNER JOIN tb_provinsi USING (id_provinsi) GROUP BY id_kabupaten"
#     mhs = "SELECT id_mahasiswa,NIM,nama,alamat,tgl_lahir,tempat_lahir,id_kabupaten,agama,no_telp,jenis_kelamin,status_perkawinan,status_bekerja,email FROM tb_mahasiswa INNER JOIN tb_kabupaten USING (id_kabupaten) INNER JOIN tb_provinsi USING (id_provinsi) GROUP BY id_mahasiswa"
#     krs = "SELECT tanggal, kode_matkul,id_mahasiswa,id_semester,jenis_kelamin,id_PA,id_prodi, sks, status_keaktifan FROM tb_detailkrs INNER JOIN tb_krs USING (id_krs) INNER JOIN tb_mahasiswa USING (id_mahasiswa) INNER JOIN tb_pa USING (id_PA) INNER JOIN tb_matkul USING (kode_matkul) INNER JOIN tb_semester USING (id_semester) INNER JOIN tb_prodi USING (id_prodi) "
#     khs = "SELECT id_semester,id_mahasiswa,kode_matkul,nilai,indeks FROM tb_khs INNER JOIN tb_matkul USING (kode_matkul) INNER JOIN tb_mahasiswa USING (id_mahasiswa) INNER JOIN tb_semester USING (id_semester) GROUP BY id_mahasiswa,id_semester"
#     ips = "SELECT id_semester,id_mahasiswa,SUM(nilai)/(COUNT(nilai*sks)*sks),SUM(nilai)/(COUNT(nilai*sks)*sks) FROM tb_khs INNER JOIN tb_matkul USING (kode_matkul) INNER JOIN tb_mahasiswa USING (id_mahasiswa) INNER JOIN tb_semester USING (id_semester) GROUP BY id_mahasiswa,id_semester"
#     # ipk = "SELECT SUM(nilai)/(COUNT(nilai*sks)*sks) FROM tb_khs INNER JOIN tb_matkul USING (kode_matkul) INNER JOIN tb_mahasiswa USING (id_mahasiswa) INNER JOIN tb_semester USING (id_semester)"
#
#     myresult = function_select(smt, mydb)
#     matkul_result = function_select(matkul, mydb)
#     pa_result = function_select(pembimbing, mydb)
#     prov_result = function_select(prov, mydb)
#     fakultas_result = function_select(fakultas, mydb)
#     prodi_result = function_select(prodi, mydb)
#     kab_result = function_select(kab, mydb)
#     mhs_result = function_select(mhs, mydb)
#     krs_result = function_select(krs, mydb)
#     khs_result = function_select(khs, mydb)
#     ips_result = function_select(ips, mydb)
#     # ipk_result = function_select(ipk, mydb)
#
#     for x in myresult:
#         id = x[0]
#         nama = x[1]
#         tahun = x[2]
#         dim_smt = "INSERT INTO dim_semester(id_semester,nm_semester, tahun_ajaran) VALUES(%d,'%s','%s')" % (
#         id, nama, tahun)
#         function_insert(dim_smt, mydb2)
#
#     for x in matkul_result:
#         kode = x[0]
#         nama = x[1]
#         sks = x[2]
#         dim_matkul = "INSERT INTO dim_matkul(kode_matkul, nama_matkul, sks) VALUES('%s','%s',%d)" % (kode, nama, sks)
#         function_insert(dim_matkul, mydb2)
#
#     for x in pa_result:
#         id = x[0]
#         nama = x[1]
#         alamat = x[2]
#         no_telp = x[3]
#         dim_pa = "INSERT INTO dim_pa (id_PA, nama_PA, alamat, no_telp) VALUES (%d,'%s','%s','%s')" % (
#         id, nama, alamat, no_telp)
#         function_insert(dim_pa, mydb2)
#
#     for x in prov_result:
#         id = x[0]
#         nama = x[1]
#         dim_prov = "INSERT INTO dim_provinsi(id_provinsi,nm_provinsi) VALUES(%d,'%s')" % (id, nama)
#         function_insert(dim_prov, mydb2)
#
#     for x in kab_result:
#         id = x[0]
#         nama = x[1]
#         prov = x[2]
#         dim_kab = "INSERT INTO dim_kabupaten(id_kabupaten,nm_kabupaten,id_provinsi) VALUES(%d,'%s',%d)" % (
#         id, nama, prov)
#         function_insert(dim_kab, mydb2)
#
#     for x in fakultas_result:
#         id = x[0]
#         nama = x[1]
#         fakultas = "INSERT INTO dim_fakultas (id_fakultas, nm_fakultas) VALUES (%d,'%s')" % (id, nama)
#         function_insert(fakultas, mydb2)
#
#     for x in prodi_result:
#         id = x[0]
#         nama = x[1]
#         id_fak = x[2]
#         prodi = "INSERT INTO dim_prodi (id_prodi,nm_prodi,id_fakultas) VALUES (%d,'%s',%d)" % (id, nama, id_fak)
#         function_insert(prodi, mydb2)
#
#     for x in mhs_result:
#         id = x[0]
#         nim = x[1]
#         nama = x[2]
#         tgl = x[3]
#         tempat = x[4]
#         alamat = x[5]
#         kab = x[6]
#         agama = x[7]
#         no_telp = x[8]
#         jk = x[9]
#         status_kawin = x[10]
#         status_kerja = x[11]
#         email = x[12]
#         mahasiswa = "INSERT INTO dim_mahasiswa (id_mhs,NIM,nama_mhs,alamat,tgl_lahir,tempat_lahir,id_kabupaten,agama,no_telp,jenis_kelamin,status_perkawinan,status_bekerja,email) VALUES (%d,'%s','%s','%s','%s','%s',%d,'%s','%s','%s','%s','%s','%s')" % (
#         id, nim, nama, tgl, tempat, alamat, kab, agama, no_telp, jk, status_kawin, status_kerja, email)
#         function_insert(mahasiswa, mydb2)
#
#     for x in krs_result:
#         tanggal = x[0]
#         kode = x[1]
#         id_mhs = x[2]
#         id_smt = x[3]
#         jenis_kelamin = x[4]
#         id_PA = x[5]
#         id_prodi = x[6]
#         total = x[7]
#         status_aktif = x[8]
#         fact_krs = "INSERT INTO fact_krs (tanggal,kode_matkul,id_mhs,id_semester,jenis_kelamin,id_PA,id_prodi,total_sks,status_keaktifan) VALUES ('%s','%s',%d,%d,'%s',%d,%d,%d,'%s')" % (
#         tanggal, kode, id_mhs, id_smt, jenis_kelamin, id_PA, id_prodi, total, status_aktif)
#         function_insert(fact_krs, mydb2)
#
#     for x in khs_result:
#         id_smt = x[0]
#         id_mhs = x[1]
#         matkul = x[2]
#         nilai = x[3]
#         indeks = x[4]
#         fact_khs = "INSERT INTO fact_khs (id_semester,id_mhs,kode_matkul,nilai,indeks) VALUES (%d,%d,'%s',%d,'%s')" % (
#         id_smt, id_mhs, matkul, nilai, indeks)
#         function_insert(fact_khs, mydb2)
#
#     for x in ips_result:
#         id_smt = x[0]
#         id_mhs = x[1]
#         ips = x[2]
#         ipk = x[3]
#         dim_indeks = "INSERT INTO dim_indeks (id_semester,id_mhs,IPS,IPK) VALUES (%d,%d,%f,%f)" % (
#         id_smt, id_mhs, ips, ipk)
#         function_insert(dim_indeks, mydb2)

class MhsGui(wx.Dialog):
    def __init__(self):
        # wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
        #                   size=wx.Size(550, 450), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        wx.Dialog.__init__(self, None, title="Report Mahasiswa", size=wx.Size(550, 450))

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

class NilaiGui(wx.Dialog):

    def __init__(self):
        # wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
        #                   size=wx.Size(700, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        wx.Dialog.__init__(self, None, title="Report Nilai Mahasiswa", size=wx.Size(700, 500))

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
            semester = 4
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
        # fileMenu = wx.Menu()
        etl = wx.Menu()
        report = wx.Menu()

        # optionsItem = fileMenu.Append(wx.NewId(), "Options",
        #                               "Show an Options Dialog")
        # self.Bind(wx.EVT_MENU, self.onOptions, optionsItem)

        procetl = etl.Append(wx.NewId(), "Proses ETL",
                                            "Show Proses ETL")
        # self.Bind(wx.EVT_MENU, self.onEtl, procetl)

        exitMenuItem = etl.Append(wx.NewId(), "Exit",
                                       "Exit the application")
        self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)

        mhs = report.Append(wx.NewId(), "Report Mahasiswa",
                            "Show Report Mahasiswa")
        self.Bind(wx.EVT_MENU, self.onMhs, mhs)

        nilai = report.Append(wx.NewId(), "Report Nilai",
                              "Show Report Nilai")
        self.Bind(wx.EVT_MENU, self.onNilai, nilai)

        # menuBar.Append(fileMenu, "&File")
        menuBar.Append(etl, "&ETL")
        menuBar.Append(report, "&Report")
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

    # ----------------------------------------------------------------------
    # def onEtl(self, event):
    #     dlg = EtlGui()
    #     dlg.ShowModal()
    #     dlg.Destroy()

    # ----------------------------------------------------------------------
    def onMhs(self, event):
        dlg = MhsGui()
        dlg.ShowModal()
        dlg.Destroy()

    # ----------------------------------------------------------------------
    def onNilai(self, event):
        dlg = NilaiGui()
        dlg.ShowModal()
        dlg.Destroy()

#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()