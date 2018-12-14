import xlsxwriter
import mysql.connector

mydb2 = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_simak"
)

def excel_nilai(self):
    excel_file = xlsxwriter.Workbook('nilai.xlsx')
    sheet = excel_file.add_worksheet('sheet_month')
    # Header
    sheet.write(0, 0, "No")
    sheet.write(0, 1, "Tahun")
    sheet.write(0, 2, "Semester")
    sheet.write(0, 3, "Matakuliah")
    sheet.write(0, 4, "NIM")
    sheet.write(0, 5, "Nama")
    sheet.write(0, 6, "Nilai")

    # Body
    row = 1
    col = 0
    tahun = self.m_choice71.GetStringSelection()
    semester = self.m_choice8.GetStringSelection()

    # ipk = self.m_textIPK.AppendText()
    mycursor = mydb2.cursor()

    semester_query = "SELECT id_semester FROM dim_semester WHERE  nm_semester LIKE '%" + semester + "%'"
    mycursor.execute(semester_query)
    id_semester = mycursor.fetchone()
    id_semester = id_semester[0]


    sql = "SELECT dim_mahasiswa.`NIM`,dim_mahasiswa.`nama_mhs`,indeks FROM fact_khs INNER JOIN dim_mahasiswa USING (id_mhs)" \
          "INNER JOIN dim_matkul USING (id_matkul)" \
          "INNER JOIN dim_semester USING (id_semester) " \
          "WHERE id_semester = '" + str(
        id_semester) + "' && YEAR(tahun_ajaran)='" + tahun + "' && dim_matkul.`nama_matkul`LIKE '%" + self.m_textCtrl1.Value + "%'"
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    for val_a, val_b, val_c in (rows):
        sheet.write(row, col, row)
        sheet.write(row, col + 1, tahun)
        sheet.write(row, col + 2, semester)
        sheet.write(row, col + 3, self.m_textCtrl1.Value)
        sheet.write(row, col + 4, val_a)
        sheet.write(row, col + 5, val_b)
        sheet.write(row, col + 6, val_c)

        row += 1
    excel_file.close()

def excel_mahasiswa(self):
    excel_file = xlsxwriter.Workbook('mahasiswa.xlsx')
    sheet = excel_file.add_worksheet('sheet_month')
    # Header
    sheet.write(0, 0, "No")
    sheet.write(0, 1, "Matakuliah")
    sheet.write(0, 2, "SKS")
    sheet.write(0, 3, "Mahasiswa")

    # Body
    row = 1
    col = 0

    mycursor = mydb2.cursor()

    tahun = self.m_tahun.GetStringSelection()
    semester = self.m_semester.GetStringSelection()

    mycursor = mydb2.cursor()

    semester_query = "SELECT id_semester FROM dim_semester WHERE  nm_semester LIKE '%" + semester + "%'"
    mycursor.execute(semester_query)
    id_semester = mycursor.fetchone()
    id_semester = id_semester[0]

    sql = "SELECT nama_matkul,sks,COUNT(nama_mhs) AS total FROM fact_krs INNER JOIN dim_matkul USING (id_matkul)" \
          "INNER JOIN dim_mahasiswa USING (id_mhs) INNER JOIN dim_semester USING (id_semester) " \
          "WHERE id_semester = '" + str(id_semester) + "' && YEAR(tahun_ajaran)='" + tahun + "' GROUP BY nama_matkul"
    mycursor.execute(sql)
    rows = mycursor.fetchall()

    for val_a, val_b, val_c in (rows):
        sheet.write(row, col, row)
        sheet.write(row, col + 1, val_a)
        sheet.write(row, col + 2, val_b)
        sheet.write(row, col + 3, val_c)

        row += 1
    excel_file.close()

def excel_KHS(self):
    excel_file = xlsxwriter.Workbook('KHS ('+self.m_inputnim.Value+').xlsx')
    sheet = excel_file.add_worksheet('sheet_month')
    # Header
    sheet.write(0, 0, "No")
    sheet.write(0, 1, "NIM")
    sheet.write(0, 2, "Kode Matakuliah")
    sheet.write(0, 3, "Matakuliah")
    sheet.write(0, 4, "SKS")
    sheet.write(0, 5, "Indeks")
    sheet.write(0, 6, "Nilai")
    sheet.write(0, 7, "IPS")
    sheet.write(0, 8, "IPK")

    # Body
    row = 1
    col = 0

    mycursor = mydb2.cursor()

    tahun = self.m_tahun1.GetStringSelection()
    semester = self.m_semester1.GetStringSelection()
    total_nilai = 0
    total_sks = 0

    # ipk = self.m_textIPK.AppendText()
    # perlu revisi

    mycursor = mydb2.cursor(buffered=True)

    semester_query = "SELECT id_semester FROM dim_semester WHERE  nm_semester LIKE '%" + semester + "%'"
    mycursor.execute(semester_query)
    id_semester = mycursor.fetchone()
    id_semester = id_semester[0]

    mhs = "SELECT id_mhs FROM dim_mahasiswa WHERE  NIM LIKE '%" + self.m_inputnim.Value + "%'"
    mycursor.execute(mhs)
    id_mhs = mycursor.fetchone()
    id_mhs = id_mhs[0]

    sql = "SELECT dim_matkul.kode_matkul,nama_matkul,sks,indeks,nilai FROM fact_khs INNER JOIN dim_matkul USING (id_matkul) " \
          "INNER JOIN dim_semester USING (id_semester) INNER JOIN dim_mahasiswa USING (id_mhs) WHERE id_semester ='" + str(
        id_semester) + \
          "' && YEAR(tahun_ajaran)='" + tahun + "' && NIM LIKE '%" + self.m_inputnim.Value + "%'"
    mycursor.execute(sql)
    rows = mycursor.fetchall()

    ipk = "SELECT IPS,IPK FROM fact_khs INNER JOIN dim_semester USING (id_semester) WHERE  YEAR(tahun_ajaran) = '" + tahun + "' && id_mhs = '" + str(
        id_mhs) + "' GROUP BY id_semester"
    mycursor.execute(ipk)
    a = mycursor.fetchall()

    for val_a, val_b, val_c, val_d, val_e in (rows):
        sheet.write(row, col, row)
        sheet.write(row, col + 1, self.m_inputnim.Value)
        sheet.write(row, col + 2, val_a)
        sheet.write(row, col + 3, val_b)
        sheet.write(row, col + 4, val_c)
        sheet.write(row, col + 5, val_d)
        sheet.write(row, col + 6, val_e)
        sheet.write(row, col + 7, a[0][0])
        sheet.write(row, col + 8, a[0][1])

        row += 1
    excel_file.close()
