import mysql.connector

def function_select(sql, mydb):
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult


def function_insert(sql, mydb2):
    cursor = mydb2.cursor()
    cursor.execute(sql)
    mydb2.commit()

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

smt = "SELECT * FROM tb_semester"
matkul = "SELECT * FROM tb_matkul"
pembimbing = "SELECT * FROM tb_PA"
prov = "SELECT * FROM tb_provinsi"
fakultas = "SELECT * FROM tb_fakultas"
prodi = "SELECT id_prodi, nm_prodi, id_fakultas FROM tb_krs INNER JOIN tb_fakultas USING (id_fakultas) INNER JOIN tb_prodi USING (id_prodi) GROUP BY id_fakultas"
kab = "SELECT id_kabupaten, nm_kabupaten, id_provinsi FROM tb_mahasiswa INNER JOIN tb_kabupaten USING (id_kabupaten) INNER JOIN tb_provinsi USING (id_provinsi) GROUP BY id_kabupaten"
mhs = "SELECT id_mahasiswa,NIM,nama,alamat,tgl_lahir,tempat_lahir,id_kabupaten,agama,no_telp,jenis_kelamin,status_perkawinan,status_bekerja,email FROM tb_mahasiswa INNER JOIN tb_kabupaten USING (id_kabupaten) INNER JOIN tb_provinsi USING (id_provinsi) GROUP BY id_mahasiswa"
krs = "SELECT tanggal, kode_matkul,id_mahasiswa,id_semester,jenis_kelamin,id_PA,id_prodi, sks, status_keaktifan FROM tb_detailkrs INNER JOIN tb_krs USING (id_krs) INNER JOIN tb_mahasiswa USING (id_mahasiswa) INNER JOIN tb_pa USING (id_PA) INNER JOIN tb_matkul USING (kode_matkul) INNER JOIN tb_semester USING (id_semester) INNER JOIN tb_prodi USING (id_prodi) "
khs = "SELECT id_semester,id_mahasiswa,kode_matkul,nilai,indeks FROM tb_khs INNER JOIN tb_matkul USING (kode_matkul) INNER JOIN tb_mahasiswa USING (id_mahasiswa) INNER JOIN tb_semester USING (id_semester) GROUP BY id_mahasiswa,id_semester"
ips ="SELECT id_semester,id_mahasiswa,SUM(nilai)/(COUNT(nilai*sks)*sks) FROM tb_khs INNER JOIN tb_matkul USING (kode_matkul) INNER JOIN tb_mahasiswa USING (id_mahasiswa) INNER JOIN tb_semester USING (id_semester) GROUP BY id_mahasiswa,id_semester"
ipk = "SELECT SUM(nilai)/(COUNT(nilai*sks)*sks) FROM tb_khs INNER JOIN tb_matkul USING (kode_matkul) INNER JOIN tb_mahasiswa USING (id_mahasiswa) INNER JOIN tb_semester USING (id_semester)"

myresult = function_select(smt, mydb)
matkul_result = function_select(matkul, mydb)
pa_result = function_select(pembimbing, mydb)
prov_result = function_select(prov, mydb)
fakultas_result = function_select(fakultas,mydb)
prodi_result = function_select(prodi,mydb)
kab_result = function_select(kab, mydb)
mhs_result = function_select(mhs,mydb)
krs_result = function_select(krs, mydb)
khs_result = function_select(khs,mydb)
ips_result = function_select(ips,mydb)
ipk_result = function_select(ipk, mydb)


for x in myresult:
    id = x[0]
    nama = x[1]
    tahun =x[2]
    dim_smt = "INSERT INTO dim_semester(id_semester,nm_semester, tahun_ajaran) VALUES(%d,'%s','%s')" % (id, nama,tahun)
    function_insert(dim_smt, mydb2)

for x in matkul_result:
    kode = x[0]
    nama = x[1]
    sks = x[2]
    dim_matkul = "INSERT INTO dim_matkul(kode_matkul, nama_matkul, sks) VALUES('%s','%s',%d)" % (kode, nama, sks)
    function_insert(dim_matkul, mydb2)

for x in pa_result:
    id = x[0]
    nama = x[1]
    alamat = x[2]
    no_telp = x[3]
    dim_pa = "INSERT INTO dim_pa (id_PA, nama_PA, alamat, no_telp) VALUES (%d,'%s','%s','%s')" % (id,nama,alamat,no_telp)
    function_insert(dim_pa, mydb2)

for x in prov_result:
    id = x[0]
    nama = x[1]
    dim_prov = "INSERT INTO dim_provinsi(id_provinsi,nm_provinsi) VALUES(%d,'%s')" % (id, nama)
    function_insert(dim_prov, mydb2)

for x in kab_result:
    id = x[0]
    nama = x[1]
    prov = x[2]
    dim_kab = "INSERT INTO dim_kabupaten(id_kabupaten,nm_kabupaten,id_provinsi) VALUES(%d,'%s',%d)" % (id, nama,prov)
    function_insert(dim_kab, mydb2)

for x in fakultas_result:
    id = x[0]
    nama = x[1]
    fakultas = "INSERT INTO dim_fakultas (id_fakultas, nm_fakultas) VALUES (%d,'%s')" % (id, nama)
    function_insert(fakultas,mydb2)

for x in prodi_result:
    id = x[0]
    nama = x[1]
    id_fak =x[2]
    prodi = "INSERT INTO dim_prodi (id_prodi,nm_prodi,id_fakultas) VALUES (%d,'%s',%d)" % (id, nama, id_fak)
    function_insert(prodi,mydb2)

for x in mhs_result:
    id = x[0]
    nim = x[1]
    nama = x[2]
    tgl = x[3]
    tempat = x[4]
    alamat = x[5]
    kab = x[6]
    agama = x[7]
    no_telp = x[8]
    jk = x[9]
    status_kawin = x[10]
    status_kerja = x[11]
    email = x[12]
    mahasiswa ="INSERT INTO dim_mahasiswa (id_mhs,NIM,nama_mhs,alamat,tgl_lahir,tempat_lahir,id_kabupaten,agama,no_telp,jenis_kelamin,status_perkawinan,status_bekerja,email) VALUES (%d,'%s','%s','%s','%s','%s',%d,'%s','%s','%s','%s','%s','%s')" % (id,nim,nama,tgl,tempat,alamat,kab,agama,no_telp,jk,status_kawin,status_kerja,email)
    function_insert(mahasiswa, mydb2)

for x in krs_result:
    tanggal = x[0]
    kode = x[1]
    id_mhs = x[2]
    id_smt = x[3]
    jenis_kelamin = x[4]
    id_PA = x[5]
    id_prodi = x[6]
    total =x[7]
    status_aktif = x[8]
    fact_krs = "INSERT INTO fact_krs (tanggal,kode_matkul,id_mhs,id_semester,jenis_kelamin,id_PA,id_prodi,total_sks,status_keaktifan) VALUES ('%s','%s',%d,%d,'%s',%d,%d,%d,'%s')" % (tanggal,kode, id_mhs, id_smt, jenis_kelamin, id_PA, id_prodi, total, status_aktif)
    function_insert(fact_krs, mydb2)

for x in khs_result:
    id_smt = x[0]
    id_mhs = x[1]
    matkul = x[2]
    nilai = x[3]
    indeks = x[4]
    fact_khs = "INSERT INTO fact_khs (id_semester,id_mhs,kode_matkul,nilai,indeks) VALUES (%d,%d,'%s',%d,'%s')" %(id_smt,id_mhs,matkul,nilai,indeks)
    function_insert(fact_khs, mydb2)

for x in ips_result:
    id_smt = x[0]
    id_mhs = x[1]
    ips = x[2]
    dim_indeks = "INSERT INTO dim_indeks (id_semester,id_mhs,IPS) VALUES (%d,%d,%f)" %(id_smt,id_mhs,ips)
    function_insert(dim_indeks,mydb2)

for x in ipk_result:
    ipk = x[0]
    ipk_field = "INSERT INTO dim_indeks (IPK) VALUES (%f)" %(ipk)
    function_insert(ipk_field,mydb2)






