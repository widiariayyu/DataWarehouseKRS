import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "db_klinik"
)
mydb2 = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "dwh_klinik"
)

def function_select(sql, mydb):
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def function_insert(sql,mydb2):
    cursor_dwh = mydb2.cursor()
    cursor_dwh.execute(sql)
    mydb2.commit()

def function_etl():
    etl_riwayat = "INSERT INTO tb_riwayat (tanggal) VALUES(NOW())"
    function_insert(etl_riwayat, mydb2)
    sql = "SELECT MAX(id_riwayat) FROM tb_riwayat LIMIT 1"
    cursor2 = mydb2.cursor()
    cursor2.execute(sql)
    data = cursor2.fetchall()
    lastRiwayat = 0
    lastRiwayat = data[0][0]

    cekDatabase = mydb2.cursor()
    cekDatabase.execute("SELECT * FROM tb_dim_pasien")
    cek = cekDatabase.fetchall()
    if len(cek) == 0:
        selectPasien = "SELECT * FROM tb_pasien"
        resultPasien = function_select(selectPasien, mydb)
        sql = "SELECT MAX(id_pasien) FROM tb_pasien"
        cursor = mydb.cursor()
        cursor.execute(sql)
        lastId = cursor.fetchall()
        lastId = lastId[0][0]
        etl_riwayat ="INSERT INTO tb_det_riwayat (id_riwayat, tabel, start_row, end_row) VALUES(%d, 'tb_pasien', 1, %d)" %(lastRiwayat, lastId)
        for x in resultPasien:
            insert_pasien = "INSERT INTO tb_dim_pasien (id_pasien_oltp, nama_pasien, tempat_lahir, tgl_lahir, jk, alamat, telp) VALUES(%d, '%s', '%s', '%s', '%s','%s','%s')" % (x[0], x[1], x[2], x[3], x[4], x[5], x[6])
            function_insert(insert_pasien, mydb2)
        function_insert(etl_riwayat, mydb2)

    else:
        sql = "SELECT max(end_row) FROM tb_det_riwayat where tabel = 'tb_pasien'"
        cursor2 = mydb2.cursor()
        cursor2.execute(sql)
        data = cursor2.fetchall()
        rowPasien = data[0][0]
        rowPasien = rowPasien+1
        sql = "SELECT MAX(id_pasien) FROM tb_pasien"
        cursor = mydb.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        lastId = 0
        lastId = data[0][0]
        if(lastId>(rowPasien - 1)):
            selectPasien = "SELECT id_pasien, nama_pasien, tempat_lahir, tgl_lahir, jk, alamat, telp FROM tb_pasien where id_pasien BETWEEN %d and %d" %( rowPasien, lastId)
            resultPasien = function_select(selectPasien, mydb)

            etl_riwayat = "INSERT INTO tb_det_riwayat (id_riwayat, tabel, start_row, end_row) VALUES(%d, 'tb_pasien', %d, %d)" % (lastRiwayat, rowPasien, lastId)
            for x in resultPasien:
                insert_pasien = "INSERT INTO tb_dim_pasien (id_pasien_oltp, nama_pasien, tempat_lahir, tgl_lahir, jk, alamat, telp) VALUES(%d, '%s', '%s', '%s', '%s','%s','%s')" % (x[0], x[1], x[2], x[3], x[4], x[5], x[6])
                function_insert(insert_pasien, mydb2)
            function_insert(etl_riwayat,mydb2)

    cekDatabase = mydb2.cursor()
    cekDatabase.execute("SELECT * FROM tb_dim_poli")
    cek = cekDatabase.fetchall()
    if len(cek) == 0:
        selectPoli = "SELECT * FROM tb_poli"
        resultPoli= function_select(selectPoli, mydb)
        sql = "SELECT MAX(id_poli) FROM tb_poli"
        cursor = mydb.cursor()
        cursor.execute(sql)
        lastId = cursor.fetchall()
        lastId = lastId[0][0]
        etl_riwayat = "INSERT INTO tb_det_riwayat (id_riwayat, tabel, start_row, end_row) VALUES(%d, 'tb_poli', 1, %d)" % (
        lastRiwayat, lastId)
        for x in resultPoli:
            insert_poli = "INSERT INTO tb_dim_poli(id_poli_oltp, nama_poli) VALUES(%d, '%s')" % (x[0], x[1])
            function_insert(insert_poli, mydb2)
        function_insert(etl_riwayat, mydb2)

    else:
        sql = "SELECT max(end_row) FROM tb_det_riwayat where tabel = 'tb_poli'"
        cursor2 = mydb2.cursor()
        cursor2.execute(sql)
        data = cursor2.fetchall()
        rowPoli= data[0][0]
        rowPoli = rowPoli + 1
        sql = "SELECT MAX(id_poli) FROM tb_poli"
        cursor = mydb.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        lastId = 0
        lastId = data[0][0]
        if (lastId > (rowPoli- 1)):
            selectPoli= "SELECT id_poli, nama_poli FROM tb_poli where id_poli BETWEEN %d and %d" % (rowPoli, lastId)
            resultPoli= function_select(selectPoli, mydb)

            etl_riwayat = "INSERT INTO tb_det_riwayat (id_riwayat, tabel, start_row, end_row) VALUES(%d, 'tb_poli', %d, %d)" % (
            lastRiwayat, rowPoli, lastId)
            for x in resultPoli:
                insert_poli= "INSERT INTO tb_dim_poli(id_poli_oltp, nama_poli) VALUES(%d, '%s')" % (x[0], x[1])
                function_insert(insert_poli, mydb2)
            function_insert(etl_riwayat, mydb2)

    cekDatabase = mydb2.cursor()
    cekDatabase.execute("SELECT * FROM tb_dim_dokter")
    cek = cekDatabase.fetchall()
    if len(cek) == 0:
        selectDokter = "SELECT * FROM tb_dokter"
        resultDokter= function_select(selectDokter, mydb)
        sql = "SELECT MAX(id_dokter) FROM tb_dokter"
        cursor = mydb.cursor()
        cursor.execute(sql)
        lastId = cursor.fetchall()
        lastId = lastId[0][0]
        etl_riwayat ="INSERT INTO tb_det_riwayat (id_riwayat, tabel, start_row, end_row) VALUES(%d, 'tb_dokter', 1, %d)" %(lastRiwayat, lastId)
        for x in resultDokter:
            insert_dokter= "INSERT INTO tb_dim_dokter(id_dokter_oltp, nama_dokter, id_poli) VALUES(%d, '%s', '%d')" % (x[0], x[1], x[2])
            function_insert(insert_dokter, mydb2)
        function_insert(etl_riwayat, mydb2)

    else:
        sql = "SELECT max(end_row) FROM tb_det_riwayat where tabel = 'tb_dokter'"
        cursor2 = mydb2.cursor()
        cursor2.execute(sql)
        data = cursor2.fetchall()
        rowDokter = data[0][0]
        rowDokter = rowDokter+1
        sql = "SELECT MAX(id_dokter) FROM tb_dokter"
        cursor = mydb.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        lastId = 0
        lastId = data[0][0]
        if(lastId>(rowDokter -1)):
            selectDokter= "SELECT id_dokter, nama_dokter, id_poli, id_jadwal FROM tb_dokter where id_dokter BETWEEN %d and %d" %( rowDokter, lastId)
            resultDokter= function_select(selectDokter, mydb)

            etl_riwayat = "INSERT INTO tb_det_riwayat (id_riwayat, tabel, start_row, end_row) VALUES(%d, 'tb_dokter', %d, %d)" % (lastRiwayat, rowDokter, lastId)
            for x in resultDokter:
                insert_dokter= "INSERT INTO tb_dim_dokter(id_dokter_oltp, nama_dokter, id_poli) VALUES(%d, '%s', '%d')" % (x[0], x[1], x[2])
                function_insert(insert_dokter, mydb2)
            function_insert(etl_riwayat,mydb2)

    cekDatabase = mydb2.cursor()
    cekDatabase.execute("SELECT * FROM tb_dim_diagnosa")
    cek = cekDatabase.fetchall()
    if len(cek) == 0:
        selectDiagnosa = "SELECT * FROM tb_diagnosa"
        resultDiagnosa = function_select(selectDiagnosa, mydb)
        sql = "SELECT MAX(id_diagnosa) FROM tb_diagnosa"
        cursor = mydb.cursor()
        cursor.execute(sql)
        lastId = cursor.fetchall()
        lastId = lastId[0][0]
        etl_riwayat = "INSERT INTO tb_det_riwayat (id_riwayat, tabel, start_row, end_row) VALUES(%d, 'tb_diagnosa', 1, %d)" % (lastRiwayat, lastId)
        for x in resultDiagnosa:
            insert_diagnosa = "INSERT INTO tb_dim_diagnosa(id_diagnosa_oltp, nama_diagnosa) VALUES(%d, '%s')" % (x[0], x[1])
            function_insert(insert_diagnosa, mydb2)
        function_insert(etl_riwayat, mydb2)

    else:
        sql = "SELECT max(end_row) FROM tb_det_riwayat where tabel = 'tb_diagnosa'"
        cursor2 = mydb2.cursor()
        cursor2.execute(sql)
        data = cursor2.fetchall()
        rowDiagnosa = data[0][0]
        rowDiagnosa = rowDiagnosa + 1
        sql = "SELECT MAX(id_diagnosa) FROM tb_diagnosa"
        cursor = mydb.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        lastId = 0
        lastId = data[0][0]
        if (lastId > (rowDiagnosa - 1)):
            selectDiagnosa= "SELECT id_diagnosa, nama_diagnosa FROM tb_diagnosa where id_diagnosa BETWEEN %d and %d" % (rowDiagnosa, lastId)
            resultDiagnosa= function_select(selectDiagnosa, mydb)

            etl_riwayat = "INSERT INTO tb_det_riwayat (id_riwayat, tabel, start_row, end_row) VALUES(%d, 'tb_diagnosa', %d, %d)" % (
            lastRiwayat, rowDiagnosa, lastId)
            for x in resultDiagnosa:
                insert_diagnosa= "INSERT INTO tb_dim_diagnosa(id_diagnosa_oltp, nama_diagnosa) VALUES(%d, '%s')" % (x[0], x[1])
                function_insert(insert_diagnosa, mydb2)
            function_insert(etl_riwayat, mydb2)

    cekDatabase = mydb2.cursor()
    cekDatabase.execute("SELECT * FROM tb_dim_obat")
    cek = cekDatabase.fetchall()
    if len(cek) == 0:
        selectObat = "SELECT * FROM tb_obat"
        resultObat = function_select(selectObat, mydb)
        sql = "SELECT MAX(id_obat) FROM tb_obat"
        cursor = mydb.cursor()
        cursor.execute(sql)
        lastId = cursor.fetchall()
        lastId = lastId[0][0]
        etl_riwayat = "INSERT INTO tb_det_riwayat (id_riwayat, tabel, start_row, end_row) VALUES(%d, 'tb_obat', 1, %d)" % (
        lastRiwayat, lastId)
        for x in resultObat:
            insert_obat= "INSERT INTO tb_dim_obat(id_obat_oltp, nama_obat, satuan, harga_satuan) VALUES(%d, '%s', '%s', %d)" % (x[0], x[1], x[2], x[3])
            function_insert(insert_obat, mydb2)
        function_insert(etl_riwayat, mydb2)

    else:
        sql = "SELECT max(end_row) FROM tb_det_riwayat where tabel = 'tb_obat'"
        cursor2 = mydb2.cursor()
        cursor2.execute(sql)
        data = cursor2.fetchall()
        rowObat = data[0][0]
        rowObat = rowObat+ 1
        sql = "SELECT MAX(id_obat) FROM tb_obat"
        cursor = mydb.cursor