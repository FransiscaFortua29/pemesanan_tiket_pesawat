from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
dbstring = ('mongodb+srv://fransiscafortuasimamora29:sparta@cluster0.4ftdsad.mongodb.net/?retryWrites=true&w=majority')
client = MongoClient(dbstring)
db = client.db.sertifikasi_miniproject

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk halaman pemesanan tiket
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Proses pemesanan tiket
        nama_penumpang = request.form['nama']
        kelas_tiket = request.form['kelas']
        harga_tiket = float(request.form['harga'])  # Menambah input harga
        jumlah_penumpang = int(request.form['jumlah_penumpang'])  # Menambah input jumlah penumpang

        tiket = {
            'nama': nama_penumpang,
            'kelas': kelas_tiket,
            # 'harga': harga_tiket,
            'jumlah_penumpang': jumlah_penumpang,
            'total': harga_tiket * jumlah_penumpang  # Menambah field total
        }

        # Simpan data ke database
        db.tiket.insert_one(tiket)

    # Ambil data tiket dari database
    tiket_list = db.tiket.find()

    return render_template('booking.html', tiketlist=tiket_list)

# Route untuk halaman footer
@app.route('/footer')
def footer():
    return render_template('footer.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
