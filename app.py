from flask import Flask, request, render_template, jsonify, json
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)
    
mysql = MySQL()
   
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'scientic_11bdg'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lihat')
def lihat():
    return render_template('lihat.html')

@app.route("/ajaxfile",methods=["POST","GET"])
def ajaxfile():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        if request.method == 'POST':
            draw = request.form['draw'] 
            row = int(request.form['start'])
            rowperpage = int(request.form['length'])
            searchValue = request.form["search[value]"]
            print(draw)
            print(row)
            print(rowperpage)
            print(searchValue)
 
            ## Total number of records without filtering
            cursor.execute("select count(*) as allcount from siswa")
            rsallcount = cursor.fetchone()
            totalRecords = rsallcount['allcount']
            print(totalRecords) 
 
            ## Total number of records with filtering
            likeString = "%" + searchValue +"%"
            cursor.execute("SELECT count(*) as allcount from siswa WHERE replid LIKE %s OR nis LIKE %s OR nama LIKE %s OR tahunmasuk LIKE %s OR idangkatan LIKE %s OR idkelas LIKE %s OR kelamin LIKE %s OR pinsiswa LIKE %s OR pinortu LIKE %s OR pinortuibu LIKE %s", (likeString, likeString, likeString, likeString, likeString, likeString, likeString, likeString, likeString, likeString))
            rsallcount = cursor.fetchone()
            totalRecordwithFilter = rsallcount['allcount']
            print(totalRecordwithFilter) 
 
            ## Fetch records
            if searchValue=='':
                cursor.execute("SELECT * FROM siswa ORDER BY nama asc limit %s, %s;", (row, rowperpage))
                employeelist = cursor.fetchall()
            else:        
                cursor.execute("SELECT * FROM siswa WHERE replid LIKE %s OR nis LIKE %s OR nama LIKE %s OR tahunmasuk LIKE %s OR idangkatan LIKE %s OR idkelas LIKE %s OR kelamin LIKE %s OR pinsiswa LIKE %s OR pinortu LIKE %s OR pinortuibu LIKE %s limit %s, %s;", (likeString, likeString, likeString, likeString, likeString, likeString, likeString, likeString, likeString, likeString, row, rowperpage))
                employeelist = cursor.fetchall()
 
            data = []
            for row in employeelist:
                data.append({
                    'replid': row['replid'],
                    'nis': row['nis'],
                    'nama': row['nama'],
                    'tahunmasuk': row['tahunmasuk'],
                    'idangkatan': row['idangkatan'],
                    'idkelas': row['idkelas'],
                    'kelamin': row['kelamin'],
                    'pinsiswa': row['pinsiswa'],
                    'pinortu': row['pinortu'],
                    'pinortuibu': row['pinortuibu'],
                })
 
            response = {
                'draw': draw,
                'iTotalRecords': totalRecords,
                'iTotalDisplayRecords': totalRecordwithFilter,
                'aaData': data,
            }
            return jsonify(response)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


if __name__ == "__main__":
    app.run(debug=True)