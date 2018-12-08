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

def function_select(sql,mydb):
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult


def function_insert(sql,mydb2):
    cursor = mydb2.cursor()
    cursor.execute(sql)
    mydb2.commit()

class UpdateConfig:

    def get_table_value(self, cursor_args, query_args):
        cursor_args.execute(query_args)
        data = cursor_args
        return data


    def getmax(self,query_args,mydb_args):
        myresult = function_select(query_args, mydb_args)
        #for x in myresult:
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
        #return x[0]


def main():
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
    khs = "SELECT id_semester,id_mahasiswa,id_matkul,nilai,indeks,SUM(nilai)/(COUNT(nilai*sks)*sks) AS IPS FROM tb_detailkhs " \
          " INNER JOIN tb_khs USING (id_khs) INNER JOIN tb_matkul USING (id_matkul) " \
          "INNER JOIN tb_mahasiswa USING (id_mahasiswa) " \
          "INNER JOIN tb_semester USING (id_semester)"

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

    if max_fak > max_fakultas:
        if min_fak == 0:
            fakultas_result = function_select(fakultas, mydb)
            (fakultas_result)
        else:
            fakultas_result = function_select(fakultas+" WHERE id_fakultas > {0}".format(max_fakultas), mydb)

        for x in fakultas_result:
            id = x[0]
            nama = x[1]
            fak = "INSERT INTO dim_fakultas (id_fakultas, nm_fakultas) VALUES (%d,'%s')" % (id, nama)

            function_insert(fak, mydb2)

    if max_prov > max_provinsi:
        if min_prov == 0:
            prov_result = function_select(prov, mydb)

        else:
            prov_result = function_select(prov + " WHERE id_provinsi > {0}".format(max_provinsi), mydb)

        for x in prov_result:
            id = x[0]
            nama = x[1]
            dim_prov = "INSERT INTO dim_provinsi(id_provinsi,nm_provinsi) VALUES(%d,'%s')" % (id, nama)
            function_insert(dim_prov, mydb2)

    if max_kab > max_kabupaten:
        if min_kab == 0:
            kab_result = function_select(kab, mydb)

        else:
            kab_result = function_select(kab + "WHERE id_kabupaten > {0}".format(max_kabupaten), mydb)

        for x in kab_result:
            id = x[0]
            nama = x[1]
            prov = x[2]
            dim_kab = "INSERT INTO dim_kabupaten(id_kabupaten,nm_kabupaten,id_provinsi) VALUES(%d,'%s',%d)" % (id, nama, prov)
            function_insert(dim_kab, mydb2)


    if max_pa > max_pembimbing:
        print("masuk")
        if min_pa== 0:
            pa_result = function_select(pembimbing, mydb)

        else:
            pa_result = function_select(pembimbing + " WHERE id_pa > {0}".format(max_pembimbing), mydb)
            print("gg")
        for x in pa_result:
            id = x[0]
            nama = x[1]
            alamat = x[2]
            no_telp = x[3]
            dim_pa = "INSERT INTO dim_pa (id_PA, nama_PA, alamat, no_telp) VALUES (%d,'%s','%s','%s')" % (
            id, nama, alamat, no_telp)
            function_insert(dim_pa, mydb2)

    if max_smt > max_semester:
        if min_smt== 0:
             smt_result = function_select(smt, mydb)

        else:
            smt_result = function_select(smt + "WHERE id_semester > {0}".format(max_semester), mydb)

        for x in smt_result:
            id = x[0]
            nama = x[1]
            tahun = x[2]
            dim_smt = "INSERT INTO dim_semester(id_semester,nm_semester, tahun_ajaran)  VALUES (%d,'%s','%s')" % (
            id, nama, tahun)
            function_insert(dim_smt, mydb2)

    if max_matkul > max_matakul:

        if min_matkul == 0:
            matkul_result = function_select(matkul,mydb)
        else:
            matkul_result = function_select(matkul + "WHERE id_matkul > {0}".format(max_matakul),mydb)
        # print ("x")
        for x in matkul_result:
            id = x[0]
            kode = x[1]
            nama = x[2]
            sks = x[3]
            dim_matkul = "INSERT INTO dim_matkul(id_matkul,kode_matkul, nama_matkul, sks) VALUES(%d,'%s','%s',%d)" % (
            id, kode, nama, sks)
            function_insert(dim_matkul, mydb2)

    if max_prodi > max_prodis:

        if min_prodi == 0:
            prodi_result = function_select(prodi, mydb)

        else:
            prodi_result = function_select(prodi + "WHERE id_prodi > {0}".format(max_prodis), mydb)
        print("x")
        for x in prodi_result:
            id = x[0]
            nama = x[1]
            id_fak = x[2]
            prodi_s = "INSERT INTO dim_prodi (id_prodi,nm_prodi,id_fakultas) VALUES (%d,'%s',%d)" % (id, nama, id_fak)
            function_insert(prodi_s, mydb2)



    if max_mhs > max_mahasiswa:
        if min_mhs == 0:
            mhs_result = function_select(mhs, mydb)
        else:
            mhs_result = function_select(mhs + "WHERE id_mahasiswa> {0}".format(max_mahasiswa), mydb)

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

    if max_detail_krs > max_fact_krs:
        if min_fact_krs == 0:
            krs_result = function_select(krs, mydb)
        else:
            krs_result = function_select(krs + "WHERE id_detail> {0}".format(max_detail_krs), mydb)
        for x in krs_result:

            kode = x[0]
            id_mhs = x[1]
            id_smt = x[2]
            total = x[3]
            fact_krs = "INSERT INTO fact_krs (id_matkul,id_mhs,id_semester,total_sks) VALUES (%d,%d,%d,%f)" % (
                kode, id_mhs, id_smt, total)
            function_insert(fact_krs, mydb2)


    if max_detail_khs > max_fact_khs:
        if min_fact_khs == 0:
            khs_result = function_select(khs, mydb)

        else:
            khs_result = function_select(khs + "WHERE id_detail_khs> {0}".format(max_detail_khs), mydb)
            print(khs_result)
        ipk =0
        for x in range(len(khs_result)):
            id_smt = khs_result[x][0]
            id_mhs = khs_result[x][1]
            matkul = khs_result[x][2]
            nilai = khs_result[x][3]
            indeks = khs_result[x][4]
            ips = khs_result[x][5]

            if x != 0 and x < (len(ips_result) - 1) and ips_result[x - 1][5] == ips[x][5]:
                ipk = ipk + ips[x][5];
                result = ipk / id_smt
                # print(result)
            elif id_smt == 1:
                ipk = 0
                result = 0
                ipk = ipk + ips
                result = ipk / id_smt
                # print(result)
            else:
                ipk = 0
                result = 0

            fact_khs = "INSERT INTO fact_khs (id_semester,id_mhs,id_matkul,nilai,indeks,IPS,IPK) VALUES (%d,%d,%d,%f,'%s',%f,%f)" %(id_smt, id_mhs, matkul, nilai, indeks, ips, result)
            function_insert(fact_khs, mydb2)


