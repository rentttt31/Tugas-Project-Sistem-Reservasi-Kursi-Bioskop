bookings = []

baris = ["A", "B"]
kolom = range(1, 11)

def daftar_kursi():
    return [f"{b}{k}" for b in baris for k in kolom]

def generate_kode_booking():
    nomor = len(bookings) + 1
    return f"ID{nomor:03d}"

def harga_tiket_bioskop(hari):
    if hari in ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT"]:
        return 20000
    elif hari in ["SABTU", "MINGGU"]:
        return 30000
    else:
        return 0

def kode_booking_terdaftar(kode):
    for b in bookings:
        if b["kode_booking"] == kode:
            return True
    return False

def kursi_terisi(no_kursi, judul, jam):
    for b in bookings:
        if b["no_kursi"] == no_kursi and b["judul_film"] == judul and b["jam_tayang"] == jam:
            return True
    return False

def create_booking():
    kode = generate_kode_booking()
    nama = input("Nama Penonton: ")
    film = input("Judul Film: ")
    hari = input("Hari: ").upper()

    if hari not in ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU"]:
        print("Hari tidak valid!")
        return

    jam = input("Jam Tayang: ")
    kursi = input("No Kursi: ").upper()
    harga = harga_tiket_bioskop(hari)

    if kursi_terisi(kursi, film, jam):
        print("❌ Kursi sudah terisi")
        return

    bookings.append({
        "kode_booking": kode,
        "nama_penonton": nama,
        "no_kursi": kursi,
        "judul_film": film,
        "hari": hari,
        "jam_tayang": jam,
        "harga_tiket": harga
    })
    print("✅ Booking berhasil")
    print(f"Kode Booking: {kode}")
    print(f"Nama: {nama}")
    print(f"Film: {film}")
    print(f"Hari: {hari}")
    print(f"Jam: {jam}")
    print(f"Harga: {harga}")

def read_booking():
    film = input("Judul Film: ")
    jam = input("Jam Tayang: ")

    for b in bookings:
        if b["judul_film"] == film and b["jam_tayang"] == jam:
            print(b)

def update_booking():
    kode = input("Kode Booking: ")
    film = input("Judul Film: ")
    jam = input("Jam Tayang: ")

    for b in bookings:
        if (
            b["kode_booking"] == kode and
            b["judul_film"] == film and
            b["jam_tayang"] == jam
        ):
            nama_baru = input("Nama baru (kosong jika tidak diubah): ")
            kursi_baru = input("Kursi baru (kosong jika tidak diubah): ").upper()

            if kursi_baru:
                if kursi_terisi(kursi_baru, film, jam):
                    print("❌ Kursi sudah terisi di jam tayang ini")
                    return
                b["no_kursi"] = kursi_baru

            if nama_baru:
                b["nama_penonton"] = nama_baru

            print("✅ Booking berhasil diperbarui")
            return

    print("❌ Data booking tidak ditemukan")

def delete_booking():
    kode = input("Kode Booking: ")
    for i, b in enumerate(bookings):
        if b["kode_booking"] == kode:
            bookings.pop(i)
            print("✅ Booking dibatalkan")
            return
    print("❌ Data tidak ditemukan")

def sorting_booking():
    pilih = input("Urutkan berdasarkan (1) Kursi (2) Nama: ")
    if pilih == "1":
        bookings.sort(key=lambda x: x["no_kursi"])
    elif pilih == "2":
        bookings.sort(key=lambda x: x["nama_penonton"])

def search_booking():
    kode = input("Kode Booking: ")
    for b in bookings:
        if b["kode_booking"] == kode:
            print(b)
            return
    print("❌ Data tidak ditemukan")

def tampilkan_kursi():
    film = input("Judul Film: ")
    jam = input("Jam Tayang: ")

    terisi = [
        b["no_kursi"] for b in bookings
        if b["judul_film"] == film and b["jam_tayang"] == jam
    ]

    for b in baris:
        for k in kolom:
            kursi = f"{b}{k}"
            print("[X]" if kursi in terisi else "[ ]", end=" ")
        print()

def laporan_pendapatan():
    film = input("Judul Film: ")
    jam = input("Jam Tayang: ")

    total = sum(
        b["harga_tiket"] for b in bookings
        if b["judul_film"] == film and b["jam_tayang"] == jam
    )
    print("Total Pendapatan:", total)

def menu_utama():
    while True:
        print("""
1. Pesan Kursi
2. Tampilkan Booking
3. Ubah Booking
4. Batalkan Booking
5. Urutkan Booking
6. Cari Booking
7. Visual Kursi
8. Laporan Pendapatan
0. Keluar
""")
        pilih = input("Pilih menu: ")

        if pilih == "1": create_booking()
        elif pilih == "2": read_booking()
        elif pilih == "3": update_booking()
        elif pilih == "4": delete_booking()
        elif pilih == "5": sorting_booking()
        elif pilih == "6": search_booking()
        elif pilih == "7": tampilkan_kursi()
        elif pilih == "8": laporan_pendapatan()
        elif pilih == "0": break

menu_utama()
