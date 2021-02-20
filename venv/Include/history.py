import mysql.connector
import wx
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

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

def function_select(sql,mydb):
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult


def function_insert(sql,mydb2):
    cursor = mydb2.cursor()
    cursor.execute(sql)
    mydb2.commit()

def fun_count(id_table, tb_name,db):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT({0}) FROM {1}".format(id_table,tb_name))
    result = cursor.fetchone()[0]
    return result

class UpdateConfig:

    def get_table_value(self, cursor_args, query_args):
        cursor_args.execute(query_args)
        data = cursor_args
        return data


    def getmax(self,query_args,mydb_args):
        myresult = function_select(query_args, mydb_args)
        if myresult[0][0] is None:
            val = 0
            return val
        return myresult[0][0]

    def getmin(self,query_args,mydb_args):
        result = function_select(query_args,mydb_args)
        if result[0][0] is None:
            val = 0
            return val
        return result[0][0]


def main(self):
    mycursor = mydb2.cursor()
   # UpdateConfig().truncateDatabase(mycursor)
    rel_fak = "SELECT MAX(id_fakultas) FROM tb_fakultas"
    rel_prov = "SELECT MAX(id_provinsi) FROM tb_provinsi"
    rel_kab = "SELECT MAX(id_kabupaten) FROM tb_kabupaten"
    rel_matkul = "SELECT MAX(id_matkul) FROM tb_matkul"
    rel_mhs = "SELECT MAX(id_mahasiswa) FROM tb_mahasiswa"
    rel_pa = "SELECT MAX(id_PA) FROM tb_pa"
    rel_prodi = "SELECT MAX(id_prodi) FROM tb_prodi"
    rel_krs = "SELECT MAX(id_krs) FROM tb_krs"
    rel_khs = "SELECT MAX(id_khs) FROM tb_khs"
    rel_detailkhs = "SELECT MAX(id_detail_khs) FROM tb_detailkhs"
    rel_detailkrs = "SELECT MAX(id_detail) FROM tb_detailkrs"
    rel_smt = "SELECT MAX(id_semester) FROM tb_semester"

    tb_fakultas = "SELECT MAX(id_fakultas) FROM dim_fakultas"
    tb_kabupaten = "SELECT MAX(id_kabupaten) FROM dim_kabupaten"
    tb_mahasiswa = "SELECT MAX(id_mhs) FROM dim_mahasiswa"
    tb_matkul = "SELECT MAX(id_matkul) FROM dim_matkul"
    tb_pa = "SELECT MAX(id_PA) FROM dim_pa"
    tb_prodi = "SELECT MAX(id_prodi) FROM dim_prodi"
    tb_provinsi = "SELECT MAX(id_provinsi) FROM dim_provinsi"
    tb_semester = "SELECT MAX(id_semester) FROM dim_semester"
    fact_khs = "SELECT MAX(id_fact_khs) FROM fact_khs"
    fact_krs = "SELECT MAX(id_fact_krs) FROM fact_krs"

    dim_fak = "SELECT MIN(id_fakultas) FROM dim_fakultas"
    dim_kab = "SELECT MIN(id_kabupaten) FROM dim_kabupaten"
    dim_siswa = "SELECT MIN(id_mhs) FROM dim_mahasiswa"
    dim_matkul = "SELECT MIN(id_matkul) FROM dim_matkul"
    dim_pa = "SELECT MIN(id_PA) FROM dim_pa"
    dim_prodi = "SELECT MIN(id_prodi) FROM dim_prodi"
    dim_prov = "SELECT MIN(id_provinsi) FROM dim_provinsi"
    dim_smt = "SELECT MIN(id_semester) FROM dim_semester"
    dim_khs = "SELECT MIN(id_fact_khs) FROM fact_khs"
    dim_krs = "SELECT MIN(id_fact_krs) FROM fact_krs"


    smt = "SELECT * FROM tb_semester"
    matkul = "SELECT * FROM tb_matkul"
    pembimbing = "SELECT * FROM tb_PA"
    prov = "SELECT * FROM tb_provinsi"
    kab = "SELECT * FROM tb_kabupaten "
    fakultas = "SELECT * FROM tb_fakultas"
    prodi = "SELECT * FROM tb_prodi"
    mhs = "SELECT * FROM tb_mahasiswa " \

    krs = " SELECT  id_matkul,id_mahasiswa,id_semester,sks FROM tb_detailkrs " \
          "INNER JOIN tb_krs USING (id_krs) INNER JOIN tb_mahasiswa USING (id_mahasiswa) " \
          "INNER JOIN tb_matkul USING (id_matkul) " \
          "INNER JOIN tb_semester USING (id_semester)  "
    khs = "SELECT id_semester,id_mahasiswa,id_matkul,nilai,indeks FROM tb_detailkhs " \
          "INNER JOIN tb_khs USING (id_khs) " \
          "INNER JOIN tb_matkul USING (id_matkul) " \
          "INNER JOIN tb_mahasiswa USING (id_mahasiswa) " \
          "ORDER BY id_mahasiswa, id_semester"


    max_fak = UpdateConfig.getmax(UpdateConfig,rel_fak,mydb)
    max_prov = UpdateConfig.getmax(UpdateConfig,rel_prov,mydb)
    max_pa = UpdateConfig.getmax(UpdateConfig,rel_pa,mydb)
    max_mhs = UpdateConfig.getmax(UpdateConfig,rel_mhs,mydb)
    max_kab = UpdateConfig.getmax(UpdateConfig,rel_kab,mydb)
    max_matkul = UpdateConfig.getmax(UpdateConfig,rel_matkul,mydb)
    max_smt = UpdateConfig.getmax(UpdateConfig,rel_smt,mydb)
    max_khs = UpdateConfig.getmax(UpdateConfig,rel_khs,mydb)
    max_krs = UpdateConfig.getmax(UpdateConfig,rel_krs,mydb)
    max_prodi = UpdateConfig.getmax(UpdateConfig,rel_prodi, mydb)
    max_detail_krs = UpdateConfig.getmax(UpdateConfig,rel_detailkrs,mydb)
    max_detail_khs = UpdateConfig.getmax(UpdateConfig,rel_detailkhs,mydb)

    max_fakultas = UpdateConfig.getmax(UpdateConfig,tb_fakultas,mydb2)
    max_provinsi = UpdateConfig.getmax(UpdateConfig,tb_provinsi,mydb2)
    max_pembimbing = UpdateConfig.getmax(UpdateConfig,tb_pa,mydb2)
    max_mahasiswa = UpdateConfig.getmax(UpdateConfig,tb_mahasiswa,mydb2)
    max_kabupaten = UpdateConfig.getmax(UpdateConfig,tb_kabupaten,mydb2)
    max_matakul = UpdateConfig.getmax(UpdateConfig,tb_matkul,mydb2)
    max_semester = UpdateConfig.getmax(UpdateConfig,tb_semester,mydb2)
    max_prodis = UpdateConfig.getmax(UpdateConfig,tb_prodi,mydb2)
    max_fact_krs = UpdateConfig.getmax(UpdateConfig,fact_krs,mydb2)
    max_fact_khs = UpdateConfig.getmax(UpdateConfig,fact_khs,mydb2)

    min_fak = UpdateConfig.getmin(UpdateConfig,tb_fakultas, mydb2)
    min_prov = UpdateConfig.getmin(UpdateConfig,tb_provinsi,mydb2)
    min_pa = UpdateConfig.getmin(UpdateConfig,tb_pa,mydb2)
    min_mhs = UpdateConfig.getmin(UpdateConfig,tb_mahasiswa,mydb2)
    min_kab = UpdateConfig.getmin(UpdateConfig,tb_kabupaten,mydb2)
    min_matkul = UpdateConfig.getmin(UpdateConfig,tb_matkul,mydb2)
    min_smt = UpdateConfig.getmin(UpdateConfig,tb_semester,mydb2)
    min_prodi = UpdateConfig.getmin(UpdateConfig,tb_prodi,mydb2)
    min_fact_krs = UpdateConfig.getmin(UpdateConfig,fact_krs,mydb2)
    min_fact_khs = UpdateConfig.getmin(UpdateConfig,fact_khs,mydb2)

 #==================================================================================#
    countRel_fak = fun_count("id_fakultas", "tb_fakultas", mydb)
    countDim_fak = fun_count("id_fakultas", "dim_fakultas", mydb2)

    add_fakultas = countRel_fak - countDim_fak
    data_fakultas = [1, 'dim_fakultas', add_fakultas]

    for x in range(0, len(data_fakultas)):
        self.m_grid10.SetCellValue(0, x, str(data_fakultas[x]))

    countRel_prov = fun_count("id_provinsi", "tb_provinsi", mydb)
    countDim_prov = fun_count("id_provinsi", "dim_provinsi", mydb2)

    add_prov = countRel_prov - countDim_prov
    data_prov = [2, 'dim_provinsi', add_prov]

    for x in range(0, len(data_prov)):
        self.m_grid10.SetCellValue(1, x, str(data_prov[x]))


    countRel_kab = fun_count("id_kabupaten", "tb_kabupaten", mydb)
    countDim_kab = fun_count("id_kabupaten", "dim_kabupaten", mydb2)

    add_kab = countRel_kab - countDim_kab
    data_kab = [3, 'dim_kabupaten', add_kab]

    for x in range(0, len(data_kab)):
        self.m_grid10.SetCellValue(2, x, str(data_kab[x]))

    countRel_pa = fun_count("id_pa", "tb_pa", mydb)
    countDim_pa = fun_count("id_pa", "dim_pa", mydb2)

    add_pa = countRel_pa - countDim_pa
    data_pa = [4, 'dim_pa', add_pa]

    for x in range(0, len(data_kab)):
        self.m_grid10.SetCellValue(3, x, str(data_kab[x]))

    countRel_smt = fun_count("id_semester", "tb_semester", mydb)
    countDim_smt = fun_count("id_semester", "dim_semester", mydb2)

    add_smt = countRel_smt - countDim_smt
    data_smt = [5, 'dim_semester', add_smt]

    for x in range(0, len(data_smt)):
        self.m_grid10.SetCellValue(4, x, str(data_smt[x]))

    countRel_matkul = fun_count("id_matkul", "tb_matkul", mydb)
    countDim_matkul = fun_count("id_matkul", "dim_matkul", mydb2)

    add_matkul = countRel_matkul - countDim_matkul
    data_matkul = [6, 'dim_matkul', add_matkul]

    for x in range(0, len(data_matkul)):
        self.m_grid10.SetCellValue(5, x, str(data_matkul[x]))

    countRel_prodi = fun_count("id_prodi", "tb_prodi", mydb)
    countDim_prodi = fun_count("id_prodi", "dim_prodi", mydb2)

    add_prodi = countRel_prodi - countDim_prodi
    data_prodi = [7, 'dim_prodi', add_prodi]

    for x in range(0, len(data_prodi)):
        self.m_grid10.SetCellValue(6, x, str(data_prodi[x]))

    countRel_mhs = fun_count("id_mahasiswa", "tb_mahasiswa", mydb)
    countDim_mhs = fun_count("id_mhs", "dim_mahasiswa", mydb2)

    add_mhs = countRel_mhs - countDim_mhs
    data_mhs = [8, 'dim_mahasiswa', add_mhs]

    for x in range(0, len(data_mhs)):
        self.m_grid10.SetCellValue(7, x, str(data_mhs[x]))

    countRel_krs = fun_count("id_detail", "tb_detailkrs", mydb)
    countDim_krs = fun_count("id_fact_krs", "fact_krs", mydb2)

    add_krs = countRel_krs - countDim_krs
    data_krs = [9, 'fact_krs', add_krs]

    for x in range(0, len(data_krs)):
        self.m_grid10.SetCellValue(8, x, str(data_krs[x]))

    countRel_khs = fun_count("id_detail_khs", "tb_detailkhs", mydb)
    countDim_khs = fun_count("id_fact_khs", "fact_khs", mydb2)

    add_khs = countRel_khs - countDim_khs
    data_khs = [10, 'fact_khs', add_khs]

    for x in range(0, len(data_khs)):
        self.m_grid10.SetCellValue(9, x, str(data_khs[x]))
#====================================================================================#
    if max_fak > max_fakultas:
        print(min_fak)
        end_row_add_fak = 0
        start_row_add_fak = 0
        if min_fak == 0:
            fakultas_result = function_select(fakultas, mydb)
            mycursor = mydb.cursor()
            mycursor.execute(fakultas)
            get_data = mycursor.fetchall()
            length_add_fak = len(get_data)
            end_row_add_fak = get_data[length_add_fak - 1][0]
            start_row_add_fak = get_data[0][0]
            for x in fakultas_result:
                id = x[0]
                nama = x[1]
                fak = "INSERT INTO dim_fakultas (id_fakultas, nm_fakultas) VALUES (%d,'%s')" % (id, nama)
                function_insert(fak, mydb2)
            mysql_insert = (
                    "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
                formatted_date, 1, 'dim_fakultas', start_row_add_fak, end_row_add_fak))
            function_insert(mysql_insert, mydb2)

        else:

            fakultas_result = function_select(fakultas+" WHERE id_fakultas > {0}".format(max_fakultas), mydb)
            max_min_fak = "SELECT update_log.`end_row` FROM update_log WHERE main_id = 1 ORDER BY update_log.`date` DESC LIMIT 1;"

            cursor = mydb.cursor()
            mycursor = mydb2.cursor()
            mycursor.execute(max_min_fak)
            count_end_row = mycursor.fetchall()
            end_row_fak = count_end_row[0][0]
            mysql_cek_db_fak = ("SELECT * FROM tb_fakultas WHERE id_fakultas > %d" % (end_row_fak))
            cursor.execute(mysql_cek_db_fak)
            get_data = cursor.fetchall()
            lenght_add_fak = len(get_data)
            if lenght_add_fak == 0:
                print("Tidak ada data baru")
            else:
                end_row_add_fak = get_data[lenght_add_fak - 1][0]
                start_row_add_fak = get_data[0][0]
                for x in fakultas_result:
                    id = x[0]
                    nama = x[1]
                    fak = "INSERT INTO dim_fakultas (id_fakultas, nm_fakultas) VALUES (%d,'%s')" % (id, nama)
                    function_insert(fak, mydb2)
                mysql_insert = (
                        "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
                formatted_date, 1, 'dim_fakultas', start_row_add_fak, end_row_add_fak))
                function_insert(mysql_insert, mydb2)


    if max_prov > max_provinsi:
        end_row_add_prov = 0
        start_row_add_prov = 0
        if min_prov == 0:
            prov_result = function_select(prov, mydb)
            mycursor = mydb.cursor()
            mycursor.execute(prov)
            get_data = mycursor.fetchall()
            length_add_prov = len(get_data)
            end_row_add_prov = get_data[length_add_prov - 1][0]
            start_row_add_prov = get_data[0][0]
            for x in prov_result:
                id = x[0]
                nama = x[1]
                dim_prov = "INSERT INTO dim_provinsi(id_provinsi,nm_provinsi) VALUES(%d,'%s')" % (id, nama)
                function_insert(dim_prov, mydb2)

            mysql_insert = (
                    "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
                formatted_date, 2, 'dim_provinsi', start_row_add_prov, end_row_add_prov))
            function_insert(mysql_insert, mydb2)
        else:
            prov_result = function_select(prov + " WHERE id_provinsi > {0}".format(max_provinsi), mydb)
            max_min_prov = "SELECT update_log.`end_row` FROM update_log WHERE main_id = 2 ORDER BY update_log.`date` DESC LIMIT 1;"

            cursor = mydb.cursor()
            mycursor = mydb2.cursor()
            mycursor.execute(max_min_prov)
            count_end_row = mycursor.fetchall()
            end_row_prov = count_end_row[0][0]
            mysql_cek_db_prov = ("SELECT * FROM tb_provinsi WHERE id_provinsi > %d" % (end_row_prov))
            cursor.execute(mysql_cek_db_prov)
            get_data = cursor.fetchall()
            lenght_add_prov = len(get_data)
            if lenght_add_prov == 0:
                print("Tidak ada data baru")
            else:
                end_row_add_prov = get_data[lenght_add_prov - 1][0]
                start_row_add_prov= get_data[0][0]
                for x in prov_result:
                    id = x[0]
                    nama = x[1]
                    dim_prov = "INSERT INTO dim_provinsi(id_provinsi,nm_provinsi) VALUES(%d,'%s')" % (id, nama)
                    function_insert(dim_prov, mydb2)

                mysql_insert = (
                        "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
                    formatted_date, 2, 'dim_provinsi', start_row_add_prov, end_row_add_prov))
                function_insert(mysql_insert, mydb2)


    if max_kab > max_kabupaten:
        end_row_add_kab = 0
        start_row_add_kab = 0
        if min_kab == 0:
            kab_result = function_select(kab, mydb)
            mycursor = mydb.cursor()
            mycursor.execute(kab)
            get_data = mycursor.fetchall()
            length_add_kab = len(get_data)
            end_row_add_kab = get_data[length_add_kab - 1][0]
            start_row_add_kab = get_data[0][0]
            for x in kab_result:
                id = x[0]
                nama = x[1]
                prov = x[2]
                dim_kab = "INSERT INTO dim_kabupaten(id_kabupaten,nm_kabupaten,id_provinsi) VALUES(%d,'%s',%d)" % (
                id, nama, prov)
                function_insert(dim_kab, mydb2)

            mysql_insert = (
                    "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
                formatted_date, 3, 'dim_kabupaten', start_row_add_kab, end_row_add_kab))
            function_insert(mysql_insert, mydb2)
        else:
            kab_result = function_select(kab + " WHERE id_kabupaten > {0}".format(max_kabupaten), mydb)
            max_min_kab = "SELECT update_log.`end_row` FROM update_log WHERE main_id = 3 ORDER BY update_log.`date` DESC LIMIT 1;"

            cursor = mydb.cursor()
            mycursor = mydb2.cursor()
            mycursor.execute(max_min_kab)
            count_end_row = mycursor.fetchall()
            end_row_kab = count_end_row[0][0]
            mysql_cek_db_kab = ("SELECT * FROM tb_kabupaten WHERE id_kabupaten > %d" % (end_row_kab))
            cursor.execute(mysql_cek_db_kab)
            get_data = cursor.fetchall()
            lenght_add_kab = len(get_data)
            if lenght_add_kab == 0:
                print("Tidak ada data baru")
            else:
                end_row_add_kab = get_data[lenght_add_kab - 1][0]
                start_row_add_kab = get_data[0][0]
                for x in kab_result:
                    id = x[0]
                    nama = x[1]
                    prov = x[2]
                    dim_kab = "INSERT INTO dim_kabupaten(id_kabupaten,nm_kabupaten,id_provinsi) VALUES(%d,'%s',%d)" % (
                    id, nama, prov)
                    function_insert(dim_kab, mydb2)

                mysql_insert = (
                        "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
                    formatted_date, 3, 'dim_kabupaten', start_row_add_kab, end_row_add_kab))
                function_insert(mysql_insert, mydb2)

    if max_pa > max_pembimbing:
        end_row_add_pa = 0
        start_row_add_pa = 0
        if min_pa== 0:
            pa_result = function_select(pembimbing, mydb)
            mycursor = mydb.cursor()
            mycursor.execute(pembimbing)
            get_data = mycursor.fetchall()
            length_add_pa = len(get_data)
            end_row_add_pa = get_data[length_add_pa - 1][0]
            start_row_add_pa = get_data[0][0]
            for x in pa_result:
                id = x[0]
                nama = x[1]
                alamat = x[2]
                no_telp = x[3]
                dim_pa = "INSERT INTO dim_pa (id_PA, nama_PA, alamat, no_telp) VALUES (%d,'%s','%s','%s')" % (
                    id, nama, alamat, no_telp)
                function_insert(dim_pa, mydb2)
            mysql_insert = (
                    "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
                formatted_date, 4, 'dim_pa', start_row_add_pa, end_row_add_pa))
            function_insert(mysql_insert, mydb2)

        else:
            pa_result = function_select(pembimbing + " WHERE id_pa > {0}".format(max_pembimbing), mydb)
            max_min_pa = "SELECT update_log.`end_row` FROM update_log WHERE main_id = 4 ORDER BY update_log.`date` DESC LIMIT 1;"

            cursor = mydb.cursor()
            mycursor = mydb2.cursor()
            mycursor.execute(max_min_pa)
            count_end_row = mycursor.fetchall()
            end_row_pa = count_end_row[0][0]
            mysql_cek_db_pa = ("SELECT * FROM tb_pa WHERE id_pa > %d" % (end_row_pa))
            cursor.execute(mysql_cek_db_pa)
            get_data = cursor.fetchall()
            lenght_add_pa = len(get_data)
            if lenght_add_pa == 0:
                print("Tidak ada data baru")
            else:
                end_row_add_pa= get_data[lenght_add_pa - 1][0]
                start_row_add_pa = get_data[0][0]

                for x in pa_result:
                    id = x[0]
                    nama = x[1]
                    alamat = x[2]
                    no_telp = x[3]
                    dim_pa = "INSERT INTO dim_pa (id_PA, nama_PA, alamat, no_telp) VALUES (%d,'%s','%s','%s')" % (
                        id, nama, alamat, no_telp)
                    function_insert(dim_pa, mydb2)
                mysql_insert = (
                        "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
                    formatted_date, 4, 'dim_pa', start_row_add_pa, end_row_add_pa))
                function_insert(mysql_insert, mydb2)


    if max_smt > max_semester:
        end_row_add_smt = 0
        start_row_add_smt = 0
        if min_smt== 0:
             smt_result = function_select(smt, mydb)
             mycursor = mydb.cursor()
             mycursor.execute(smt)
             get_data = mycursor.fetchall()
             length_add_smt = len(get_data)
             end_row_add_smt = get_data[length_add_smt - 1][0]
             start_row_add_smt = get_data[0][0]

             for x in smt_result:
                 id = x[0]
                 nama = x[1]
                 tahun = x[2]
                 dim_smt = "INSERT INTO dim_semester(id_semester,nm_semester, tahun_ajaran)  VALUES (%d,'%s','%s')" % (
                     id, nama, tahun)
                 function_insert(dim_smt, mydb2)
             mysql_insert = (
                     "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
                 formatted_date, 5, 'dim_semester', start_row_add_smt, end_row_add_smt))
             function_insert(mysql_insert, mydb2)
        else:
            smt_result = function_select(smt + " WHERE id_semester > {0}".format(max_semester), mydb)
            max_min_smt = "SELECT update_log.`end_row` FROM update_log WHERE main_id = 5 ORDER BY update_log.`date` DESC LIMIT 1;"

            cursor = mydb.cursor()
            mycursor = mydb2.cursor()
            mycursor.execute(max_min_smt)
            count_end_row = mycursor.fetchall()
            end_row_smt = count_end_row[0][0]
            mysql_cek_db_smt = ("SELECT * FROM tb_semester WHERE id_semester > %d" % (end_row_smt))
            cursor.execute(mysql_cek_db_smt)
            get_data = cursor.fetchall()
            lenght_add_smt = len(get_data)
            if lenght_add_smt == 0:
                print("Tidak ada data baru")
            else:
                end_row_add_smt = get_data[lenght_add_smt- 1][0]
                start_row_add_smt = get_data[0][0]

                for x in smt_result:
                    id = x[0]
                    nama = x[1]
                    tahun = x[2]
                    dim_smt = "INSERT INTO dim_semester(id_semester,nm_semester, tahun_ajaran)  VALUES (%d,'%s','%s')" % (
                        id, nama, tahun)
                    function_insert(dim_smt, mydb2)
                mysql_insert = (
                        "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
                    formatted_date, 5, 'dim_semester', start_row_add_smt, end_row_add_smt))
                function_insert(mysql_insert, mydb2)



    if max_matkul > max_matakul:
        end_row_add_matkul = 0
        start_row_add_matkul = 0
        if min_matkul == 0:
            matkul_result = function_select(matkul,mydb)
            mycursor = mydb.cursor()
            mycursor.execute(matkul)
            get_data = mycursor.fetchall()
            length_add_matkul = len(get_data)
            end_row_add_matkul = get_data[length_add_matkul - 1][0]
            start_row_add_matkul = get_data[0][0]

            for x in matkul_result:
                id = x[0]
                kode = x[1]
                nama = x[2]
                sks = x[3]
                dim_matkul = "INSERT INTO dim_matkul(id_matkul,kode_matkul, nama_matkul, sks) VALUES(%d,'%s','%s',%d)" % (
                    id, kode, nama, sks)
                function_insert(dim_matkul, mydb2)
            mysql_insert = (
                    "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
                formatted_date, 6, 'dim_matkul', start_row_add_matkul, end_row_add_matkul))
            function_insert(mysql_insert, mydb2)

        else:
            matkul_result = function_select(matkul + " WHERE id_matkul > {0}".format(max_matakul),mydb)
            max_min_matkul = "SELECT update_log.`end_row` FROM update_log WHERE main_id = 6 ORDER BY update_log.`date` DESC LIMIT 1;"

            cursor= mydb.cursor()
            mycursor = mydb2.cursor()
            mycursor.execute(max_min_matkul)
            count_end_row = mycursor.fetchall()
            end_row_matkul = count_end_row[0][0]
            mysql_cek_db_matkul = ("SELECT * FROM tb_matkul WHERE id_matkul > %d" % (end_row_matkul))
            cursor.execute(mysql_cek_db_matkul)
            get_data = cursor.fetchall()
            lenght_add_matkul = len(get_data)
            if lenght_add_matkul == 0:
                print("Tidak ada data baru")
            else:
                end_row_add_matkul = get_data[lenght_add_matkul - 1][0]
                start_row_add_matkul = get_data[0][0]

                for x in get_data:
                    id = x[0]
                    kode = x[1]
                    nama = x[2]
                    sks = x[3]
                    dim_matkul = "INSERT INTO dim_matkul(id_matkul,kode_matkul, nama_matkul, sks) VALUES(%d,'%s','%s',%d)" % (
                        id, kode, nama, sks)
                    function_insert(dim_matkul, mydb2)

                mysql_insert = (
                        "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
                    formatted_date, 6, 'dim_matkul', start_row_add_matkul, end_row_add_matkul))
                function_insert(mysql_insert, mydb2)



    if max_prodi > max_prodis:
        end_row_add_prodi = 0
        start_row_add_prodi= 0
        if min_prodi == 0:
            prodi_result = function_select(prodi, mydb)
            mycursor = mydb.cursor()
            mycursor.execute(prodi)
            get_data = mycursor.fetchall()
            length_add_prodi = len(get_data)
            end_row_add_prodi = get_data[length_add_prodi - 1][0]
            start_row_add_prodi = get_data[0][0]

            for x in prodi_result:
                id = x[0]
                nama = x[1]
                id_fak = x[2]
                prodi_s = "INSERT INTO dim_prodi (id_prodi,nm_prodi,id_fakultas) VALUES (%d,'%s',%d)" % (
                id, nama, id_fak)
                function_insert(prodi_s, mydb2)
            mysql_insert = (
                    "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
                formatted_date, 7, 'dim_prodi', start_row_add_prodi, end_row_add_prodi))
            function_insert(mysql_insert, mydb2)
        else:
            prodi_result = function_select(prodi + " WHERE id_prodi > {0}".format(max_prodis), mydb)
            max_min_prodi = "SELECT update_log.`end_row` FROM update_log WHERE main_id = 7 ORDER BY update_log.`date` DESC LIMIT 1;"

            cursor = mydb.cursor()
            mycursor = mydb2.cursor()
            mycursor.execute(max_min_prodi)
            count_end_row = mycursor.fetchall()
            end_row_prodi = count_end_row[0][0]
            mysql_cek_db_prodi = ("SELECT * FROM tb_prodi WHERE id_prodi> %d" % (end_row_prodi))
            cursor.execute(mysql_cek_db_prodi)
            get_data = cursor.fetchall()
            lenght_add_prodi = len(get_data)
            if lenght_add_prodi == 0:
                print("Tidak ada data baru")
            else:
                end_row_add_prodi = get_data[lenght_add_prodi - 1][0]
                start_row_add_prodi = get_data[0][0]
                for x in prodi_result:
                    id = x[0]
                    nama = x[1]
                    id_fak = x[2]
                    prodi_s = "INSERT INTO dim_prodi (id_prodi,nm_prodi,id_fakultas) VALUES (%d,'%s',%d)" % (
                    id, nama, id_fak)
                    function_insert(prodi_s, mydb2)
                mysql_insert = (
                        "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
                    formatted_date, 7, 'dim_prodi', start_row_add_prodi, end_row_add_prodi))
                function_insert(mysql_insert, mydb2)



    if max_mhs > max_mahasiswa:
        end_row_add_mhs = 0
        start_row_add_mhs= 0
        if min_mhs == 0:
            mhs_result = function_select(mhs, mydb)
            mycursor = mydb.cursor()
            mycursor.execute(mhs)
            get_data = mycursor.fetchall()
            length_add_mhs = len(get_data)
            end_row_add_mhs = get_data[length_add_mhs - 1][0]
            start_row_add_mhs = get_data[0][0]

        else:
            mhs_result = function_select(mhs + " WHERE id_mahasiswa> {0}".format(max_mahasiswa), mydb)

            max_min_mhs = " SELECT MIN(id_mahasiswa), MAX(id_mahasiswa) FROM tb_mahasiswa" \
                          " WHERE id_mahasiswa > " + format(max_mahasiswa)

            mycursor = mydb.cursor()
            mycursor.execute(max_min_mhs)
            get_data = mycursor.fetchone()

            length_add_mhs = len(get_data)
            # print(lenght_add_member)
            end_row_add_mhs = get_data[1]
            # print(end_row_add_member)
            start_row_add_mhs = get_data[0]
            mhs_result = function_select(mhs, mydb)

        for x in mhs_result:

            id = x[0]
            nim = x[1]
            nama = x[2]
            alamat = x[3]
            tgl = str(x[4])
            tempat = x[5]
            no_telp = x[6]
            agama = x[7]
            jk = x[8]
            status_kerja = x[9]
            status_kawin = x[10]
            email = x[11]
            id_kab = x[12]
            id_pa = x[13]
            id_prodi = x[14]

            mahasiswa = "INSERT INTO dim_mahasiswa (NIM,nama_mhs,alamat,tgl_lahir,tempat_lahir,no_telp,agama,jenis_kelamin,status_bekerja,status_perkawinan,email,id_kabupaten,id_pa,id_prodi)VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%d,%d,%d) " \
                        % (nim, nama, alamat, tgl, tempat, no_telp, agama, jk, status_kerja, status_kawin, email,
                           id_kab, id_pa, id_prodi)
            function_insert(mahasiswa, mydb2)

        mysql_insert = (
                "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
            formatted_date, 8, 'dim_mahasiswa', start_row_add_mhs, end_row_add_mhs))
        function_insert(mysql_insert, mydb2)

    if max_detail_krs > max_fact_krs:
        end_row_add_krs = 0
        start_row_add_krs = 0
        if min_fact_krs == 0:
            krs_result = function_select(krs, mydb)
            mycursor = mydb.cursor()
            mycursor.execute(krs)
            get_data = mycursor.fetchall()
            length_add_krs = len(get_data)
            end_row_add_krs = get_data[length_add_krs - 1][0]
            start_row_add_krs = get_data[0][0]

        else:
            krs = " SELECT  id_matkul,id_mahasiswa,id_semester,sks FROM tb_detailkrs " \
                  "INNER JOIN tb_krs USING (id_krs) INNER JOIN tb_mahasiswa USING (id_mahasiswa) " \
                  "INNER JOIN tb_matkul USING (id_matkul) " \
                  "INNER JOIN tb_semester USING (id_semester) WHERE id_detail > "+format(max_fact_krs)+" "
            max_min_krs = " SELECT MIN(id_detail), MAX(id_detail) FROM tb_detailkrs" \
                          " WHERE id_detail > " + format(max_fact_krs)


            mycursor = mydb.cursor()
            mycursor.execute(max_min_krs)
            get_data = mycursor.fetchone()
            length_add_krs = len(get_data)
            end_row_add_krs = get_data[1]
            start_row_add_krs = get_data[0]
            krs_result = function_select(krs, mydb)

        for x in krs_result:

            kode = x[0]
            id_mhs = x[1]
            id_smt = x[2]
            total = x[3]
            fact_krs = "INSERT INTO fact_krs (id_matkul,id_mhs,id_semester,total_sks) VALUES (%d,%d,%d,%f)" % (
                kode, id_mhs, id_smt, total)
            function_insert(fact_krs, mydb2)

        krs_insert = (
                "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
            formatted_date, 9, 'fact_krs', start_row_add_krs, end_row_add_krs))
        function_insert(krs_insert, mydb2)

    if max_detail_khs > max_fact_khs:
        end_row_add_khs = 0
        start_row_add_khs = 0
        if min_fact_khs == 0:
            khs_result = function_select(khs, mydb)
            mycursor = mydb.cursor()
            mycursor.execute(khs)
            get_data = mycursor.fetchall()
            length_add_khs = len(get_data)
            end_row_add_khs = get_data[length_add_khs - 1][0]
            start_row_add_khs = get_data[0][0]


        else:
            khs = " SELECT id_semester,id_mahasiswa,id_matkul,nilai,indeks FROM tb_detailkhs           " \
                  "INNER JOIN tb_khs USING (id_khs) " \
                  "INNER JOIN tb_matkul USING (id_matkul) " \
                  "INNER JOIN tb_mahasiswa USING (id_mahasiswa) " \
                  "WHERE id_detail_khs > "+format(max_fact_khs)+" ORDER BY id_mahasiswa,id_semester"

            max_min_khs = " SELECT MIN(id_detail_khs), MAX(id_detail_khs) FROM tb_detailkhs" \
                  " WHERE id_detail_khs > " + format(max_fact_khs)


            mycursor = mydb.cursor()
            mycursor.execute(max_min_khs)
            get_data = mycursor.fetchone()
            length_add_khs = len(get_data)
            end_row_add_khs = get_data[1]
            start_row_add_khs = get_data[0]
            khs_result = function_select(khs, mydb)

        for x in range(len(khs_result)):
            id_smt = khs_result[x][0]
            id_mhs = khs_result[x][1]
            matkul = khs_result[x][2]
            nilai = khs_result[x][3]
            indeks = khs_result[x][4]

            IPS = 	"SELECT SUM(nilai)/SUM(sks) " \
                     "FROM tb_detailkhs " \
                     "INNER JOIN tb_khs USING (id_khs) " \
                     "INNER JOIN tb_matkul USING (id_matkul) " \
                     "INNER JOIN tb_mahasiswa USING (id_mahasiswa) " \
                     "WHERE id_mahasiswa = "+str(id_mhs)+" AND id_semester ="+str(id_smt)+" GROUP BY id_semester,id_mahasiswa"
            IPS_result = function_select(IPS,mydb)
            IPS = IPS_result[0][0]

            if x == 0 :
                tmp_mhs =  id_mhs
                tmp_smt = id_smt
                IPK = IPS
            elif id_mhs == tmp_mhs and id_smt == tmp_smt :
                tmp_mhs =  id_mhs
                tmp_smt = id_smt
                IPK = IPK
            elif id_mhs == tmp_mhs and id_smt != tmp_smt :
                IPK = (IPK + IPS)/id_smt
                tmp_smt = id_smt
            else :
                tmp_mhs =  id_mhs
                tmp_smt = id_smt
                IPK = IPS

            fact_khs = "INSERT INTO fact_khs (id_semester,id_mhs,id_matkul,nilai,indeks,IPS,IPK) VALUES (%d,%d,%d,%f,'%s',%f, %f)" %(id_smt, id_mhs, matkul, nilai, indeks, IPS, IPK)
            function_insert(fact_khs, mydb2)

        khs_insert = (
                "INSERT INTO update_log (date,main_id,main_name,start_row,end_row) VALUES ('%s',%d,'%s',%d,%d)" % (
            formatted_date, 10, 'fact_khs', start_row_add_khs, end_row_add_khs))
        function_insert(khs_insert, mydb2)

    mydb.rollback()
    mydb2.rollback()
