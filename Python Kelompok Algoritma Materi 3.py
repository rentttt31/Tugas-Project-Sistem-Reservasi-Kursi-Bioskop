bookings = []

baris = ["A", "B", "C", "D", "E", "F", "G", "H"]
kolom = range(1, 11)
daftar_film = {"1": "AVATAR: FIRE AND ASH", "2": "SPIDERMAN: BRAND NEW DAY", "3": "ZOOTOPIA 2"}
daftar_jam_tayang = {"1": "13:00", "2": "15:00", "3": "19:00"}

def daftar_kursi():
    return [f"{b}{k}" for b in baris for k in kolom]

def generate_kode_booking():
    nomor = len(bookings) + 1
    return f"DS{nomor:03d}"

def harga_tiket_bioskop(hari):
    if hari in ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT"]:
        return 25000
    elif hari in ["SABTU", "MINGGU"]:
        return 35000
    else:
        return 0

def kursi_terisi(no_kursi, judul, jam, hari):
    for b in bookings:
        if b["no_kursi"] == no_kursi and b["judul_film"] == judul and b["jam_tayang"] == jam and b["hari_tayang"] == hari:
            return True
    return False

def create_booking():
    kode = generate_kode_booking()
    nama = input("Nama Penonton: ")

    while nama == "":
        print("❌ Nama tidak boleh kosong!")
        nama = input("Nama Penonton: ")

    print("Daftar Film: ")
    for n, f in enumerate(daftar_film.values(), start=1):
        print(f"{n}. {f}")
    film = input("Judul Film (1/2/3): ").strip()

    while film == "" or film not in daftar_film:
        if film == "":
            print("❌ Judul film tidak boleh kosong!")
            film = input("Judul Film (1/2/3): ").strip()

        elif film not in daftar_film:
            print("❌ Pilihan tidak valid!")
            film = input("Judul Film (1/2/3): ").strip()

    film = daftar_film[film]

    hari = input("Hari: ").upper()

    while hari not in ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU"]:
        print("❌ Hari tidak valid!")
        hari = input("Hari: ").upper()

    print("Daftar Jam Tayang: ")
    for n, f in enumerate(daftar_jam_tayang.values(), start=1):
        print(f"{n}. {f}")
    jam = input("Jam Tayang (1/2/3): ").strip()

    while jam == "" or jam not in daftar_jam_tayang:
        if jam == "":
            print("❌ Jam tidak boleh kosong!")
            jam = input("Jam Tayang (1/2/3): ").strip()
        elif jam not in daftar_jam_tayang:
            print("❌ Pilihan tidak valid!")
            jam = input("Jam Tayang (1/2/3): ").strip()

    jam = daftar_jam_tayang[jam]

    kursi = input("No Kursi: ").upper()

    while kursi not in daftar_kursi() or kursi_terisi(kursi, film, jam, hari):
        if kursi not in daftar_kursi():
            print("❌ Kursi tidak valid!")
            kursi = input("No Kursi: ").upper()

        elif kursi_terisi(kursi, film, jam, hari):
            print("❌ Kursi sudah terisi!")
            kursi = input("No Kursi: ").upper()

    harga = harga_tiket_bioskop(hari)

    bookings.append({
        "kode_booking": kode,
        "nama_penonton": nama,
        "no_kursi": kursi,
        "judul_film": film,
        "hari_tayang": hari,
        "jam_tayang": jam,
        "harga_tiket": harga
    })
    print("\n" + "=" * 40)
    print("        🎬 TIKET BIOSKOP 🎬")
    print("=" * 40)
    print(f"Kode Booking : {kode}")
    print(f"Nama         : {nama}")
    print(f"Film         : {film}")
    print(f"Hari         : {hari}")
    print(f"Jam Tayang   : {jam}")
    print(f"No. Kursi    : {kursi}")
    print("-" * 40)
    print(f"Total Bayar  : Rp {harga:,}")
    print("=" * 40)

def read_booking():
    ditemukan = False
    if not bookings:
        print("❌ Belum ada data booking!")
        return

    pilihan = int(input("Tampilkan berdasarkan (1) Film (2) Film dan Jam Tayang (3) Film, Jam Tayang, dan Hari: "))
    if pilihan == 1:
        print("Daftar Film: ")
        for n, f in enumerate(daftar_film.values(), start=1):
            print(f"{n}. {f}")

        film = input("Judul Film (1/2/3): ").strip()

        while film == "" or film not in daftar_film:
            if film == "":
                print("❌ Judul film tidak boleh kosong!")
                film = input("Judul Film (1/2/3): ").strip()

            elif film not in daftar_film:
                print("❌ Pilihan tidak valid!")
                film = input("Judul Film (1/2/3): ").strip()

        film = daftar_film[film]

        for b in bookings:
            if b["judul_film"] == film:
                print(f"Kode booking: {b['kode_booking']}, Nama: {b['nama_penonton']}, Film: {b['judul_film']}, Hari: {b['hari_tayang']}, Jam: {b['jam_tayang']}, No. Kursi: {b['no_kursi']}, Harga Tiket: {b['harga_tiket']}")
                ditemukan = True
        if not ditemukan:
            print("❌ Belum ada data booking!")

    elif pilihan == 2:
        print("Daftar Film: ")
        for n, f in enumerate(daftar_film.values(), start=1):
            print(f"{n}. {f}")

        film = input("Judul Film (1/2/3): ").strip()

        while film == "" or film not in daftar_film:
            if film == "":
                print("❌ Judul film tidak boleh kosong!")
                film = input("Judul Film (1/2/3): ").strip()

            elif film not in daftar_film:
                print("❌ Pilihan tidak valid!")
                film = input("Judul Film (1/2/3): ").strip()

        film = daftar_film[film]

        print("Daftar Jam Tayang: ")
        for n, f in enumerate(daftar_jam_tayang.values(), start=1):
            print(f"{n}. {f}")
        jam = input("Jam Tayang (1/2/3): ").strip()

        while jam == "" or jam not in daftar_jam_tayang:
            if jam == "":
                print("❌ Jam tidak boleh kosong!")
                jam = input("Jam Tayang (1/2/3): ").strip()
            elif jam not in daftar_jam_tayang:
                print("❌ Pilihan tidak valid!")
                jam = input("Jam Tayang (1/2/3): ").strip()

        jam = daftar_jam_tayang[jam]

        for b in bookings:
            if b["judul_film"] == film and b["jam_tayang"] == jam:
                print(f"Kode booking: {b['kode_booking']}, Nama: {b['nama_penonton']}, Film: {b['judul_film']}, Hari: {b['hari_tayang']}, Jam: {b['jam_tayang']}, No. Kursi: {b['no_kursi']}, Harga Tiket: {b['harga_tiket']}")
                ditemukan = True
        if not ditemukan:
            print("❌ Belum ada data booking!")

    elif pilihan == 3:
        print("Daftar Film: ")
        for n, f in enumerate(daftar_film.values(), start=1):
            print(f"{n}. {f}")

        film = input("Judul Film (1/2/3): ").strip()

        while film == "" or film not in daftar_film:
            if film == "":
                print("❌ Judul film tidak boleh kosong!")
                film = input("Judul Film (1/2/3): ").strip()

            elif film not in daftar_film:
                print("❌ Pilihan tidak valid!")
                film = input("Judul Film (1/2/3): ").strip()

        film = daftar_film[film]

        print("Daftar Jam Tayang: ")
        for n, f in enumerate(daftar_jam_tayang.values(), start=1):
            print(f"{n}. {f}")
        jam = input("Jam Tayang (1/2/3): ").strip()

        while jam == "" or jam not in daftar_jam_tayang:
            if jam == "":
                print("❌ Jam tidak boleh kosong!")
                jam = input("Jam Tayang (1/2/3): ").strip()
            elif jam not in daftar_jam_tayang:
                print("❌ Pilihan tidak valid!")
                jam = input("Jam Tayang (1/2/3): ").strip()

        jam = daftar_jam_tayang[jam]

        hari = input("Hari: ").upper()
        while hari not in [b["hari_tayang"] for b in bookings if b["judul_film"] == film and b["jam_tayang"] == jam]:
            print("❌ Hari tidak valid!")
            hari = input("Hari: ").upper()

        for b in bookings:
            if b["judul_film"] == film and b["jam_tayang"] == jam and b["hari_tayang"] == hari:
                print(f"Kode booking: {b['kode_booking']}, Nama: {b['nama_penonton']}, Film: {b['judul_film']}, Hari: {b['hari_tayang']}, Jam: {b['jam_tayang']}, No. Kursi: {b['no_kursi']}, Harga Tiket: {b['harga_tiket']}")
                ditemukan = True
        if not ditemukan:
            print("❌ Belum ada data booking!")
    else:
        print("❌ Pilihan tidak valid!")

def update_booking():
    if not bookings:
        print("❌ Belum ada data booking!")
        return

    for b in bookings:
        print(
            f"Kode booking: {b['kode_booking']}, Nama: {b['nama_penonton']}, Film: {b['judul_film']}, Hari: {b['hari_tayang']}, Jam: {b['jam_tayang']}, No. Kursi: {b['no_kursi']}, Harga Tiket: {b['harga_tiket']}")
    kode = input("Masukkan Kode Booking yg ingin diubah: ").upper()

    for b in bookings:
        if b["kode_booking"] == kode:
            nama_baru = input("Nama baru (kosong jika tidak diubah): ")
            kursi_baru = input("Kursi baru (kosong jika tidak diubah): ").upper()

            if kursi_baru:
                while kursi_baru not in daftar_kursi():
                    print("❌ Kursi tidak valid!")
                    kursi_baru = input("Kursi baru: ").upper()

                while kursi_terisi(kursi_baru, b["judul_film"], b["jam_tayang"], b["hari_tayang"]):
                    print("❌ Kursi sudah terisi!")
                    kursi_baru = input("Kursi baru: ").upper()

                b["no_kursi"] = kursi_baru

            if nama_baru:
                b["nama_penonton"] = nama_baru

            print("✅ Booking berhasil diperbarui")
            return

    print("❌ Data booking tidak valid")

def delete_booking():
    if not bookings:
        print("❌ Belum ada data booking!")
        return

    for b in bookings:
        print(f"Kode booking: {b['kode_booking']}, Nama: {b['nama_penonton']}, Film: {b['judul_film']}, Hari: {b['hari_tayang']}, Jam: {b['jam_tayang']}, No. Kursi: {b['no_kursi']}, Harga Tiket: {b['harga_tiket']}")
    kode = input("Masukkan kode booking yang ingin dibatalkan: ").upper()
    while kode not in [b["kode_booking"] for b in bookings]:
        print("❌ Data tidak ditemukan")
        kode = input("Masukkan kode booking yang ingin dibatalkan: ").upper()

    for i, b in enumerate(bookings):
        if b["kode_booking"] == kode:
            bookings.pop(i)
            print("✅ Booking dibatalkan!")
            return

def sorting_booking():
    if not bookings:
        print("❌ Belum ada data booking!")
        return

    pilih = input("Urutkan berdasarkan (1) Kode Booking (2) Kursi (3) Nama: ")
    if pilih == "1":
        bookings.sort(key=lambda x: x["kode_booking"])
    elif pilih == "2":
        bookings.sort(key=lambda x: x["no_kursi"])
    elif pilih == "3":
        bookings.sort(key=lambda x: x["nama_penonton"])
    else:
        print("❌ Pilihan tidak valid!")
        return

    print("Hasil Sorting:")
    for b in bookings:
        print(f"Kode booking: {b['kode_booking']}, Nama: {b['nama_penonton']}, Film: {b['judul_film']}, Hari: {b['hari_tayang']}, Jam: {b['jam_tayang']}, No. Kursi: {b['no_kursi']}, Harga Tiket: {b['harga_tiket']}")

def search_booking():
    if not bookings:
        print("❌ Belum ada data booking!")
        return

    for b in bookings:
        print(f"Kode booking: {b['kode_booking']}, Nama: {b['nama_penonton']}, Film: {b['judul_film']}, Hari: {b['hari_tayang']}, Jam: {b['jam_tayang']}, No. Kursi: {b['no_kursi']}, Harga Tiket: {b['harga_tiket']}")
    kode = input("Kode Booking: ").upper()
    for b in bookings:
        if b["kode_booking"] == kode:
            print(b)
            return
    print("❌ Data tidak ditemukan!")

def tampilkan_kursi():
    print("Daftar Film: ")
    for n, f in enumerate(daftar_film.values(), start=1):
        print(f"{n}. {f}")

    film = input("Judul Film (1/2/3): ").strip()

    while film == "" or film not in daftar_film:
        if film == "":
            print("❌ Judul film tidak boleh kosong!")
            film = input("Judul Film (1/2/3): ").strip()

        elif film not in daftar_film:
            print("❌ Pilihan tidak valid!")
            film = input("Judul Film (1/2/3): ").strip()

    film = daftar_film[film]

    print("Daftar Jam Tayang: ")
    for n, f in enumerate(daftar_jam_tayang.values(), start=1):
        print(f"{n}. {f}")
    jam = input("Jam Tayang (1/2/3): ").strip()

    while jam == "" or jam not in daftar_jam_tayang:
        if jam == "":
            print("❌ Jam tidak boleh kosong!")
            jam = input("Jam Tayang (1/2/3): ").strip()
        elif jam not in daftar_jam_tayang:
            print("❌ Pilihan tidak valid!")
            jam = input("Jam Tayang (1/2/3): ").strip()

    jam = daftar_jam_tayang[jam]

    hari = input("Hari: ").upper()
    while hari not in ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU"]:
        print("❌ Hari tidak valid!")
        hari = input("Hari: ").upper()

    terisi = [b["no_kursi"] for b in bookings if b["judul_film"] == film and b["jam_tayang"] == jam and b["hari_tayang"] == hari]
    if not terisi:
        print("❌ Belum ada booking!")

    print("\n                     L A Y A R")
    print("               =====================")
    print("\n     " + "   ".join(str(k) for k in kolom[:5]) + "       " + "   ".join(str(k) for k in kolom[5:]))

    for b in baris:
        print(f"{b} |", end=" ")
        for i, k in enumerate(kolom, start=1):
            kursi = f"{b}{k}"
            print("[X]" if kursi in terisi else "[ ]", end=" ")

            if i == 5:
                print("   ", end=" ")
        print(f"| {b}")

def laporan_pendapatan():
    if not bookings:
        print("❌ Belum ada data booking!")
        return

    print("Pendapatan berdasarkan:")
    print("1. Film")
    print("2. Film & Jam Tayang")
    print("3. Film, Jam Tayang & Hari")
    pilihan = int(input("Pilihan: "))
    if pilihan == 1:
        print("Daftar Film: ")
        for n, f in enumerate(daftar_film.values(), start=1):
            print(f"{n}. {f}")

        film = input("Judul Film (1/2/3): ").strip()

        while film == "" or film not in daftar_film:
            if film == "":
                print("❌ Judul film tidak boleh kosong!")
                film = input("Judul Film (1/2/3): ").strip()

            elif film not in daftar_film:
                print("❌ Pilihan tidak valid!")
                film = input("Judul Film (1/2/3): ").strip()

        film = daftar_film[film]

        total1 = sum(b["harga_tiket"] for b in bookings if b["judul_film"] == film)
        data = [b for b in bookings if b["judul_film"] == film]
        total_tiket = len(data)
        print("----Laporan Pendapatan---")
        print("Film:", film)
        print("Total Tiket Terjual:", total_tiket)
        print("Total Pendapatan per Film:", total1)

    elif pilihan == 2:
        print("Daftar Film: ")
        for n, f in enumerate(daftar_film.values(), start=1):
            print(f"{n}. {f}")

        film = input("Judul Film (1/2/3): ").strip()

        while film == "" or film not in daftar_film:
            if film == "":
                print("❌ Judul film tidak boleh kosong!")
                film = input("Judul Film (1/2/3): ").strip()

            elif film not in daftar_film:
                print("❌ Pilihan tidak valid!")
                film = input("Judul Film (1/2/3): ").strip()

        film = daftar_film[film]

        print("Daftar Jam Tayang: ")
        for n, f in enumerate(daftar_jam_tayang.values(), start=1):
            print(f"{n}. {f}")
        jam = input("Jam Tayang (1/2/3): ").strip()

        while jam == "" or jam not in daftar_jam_tayang:
            if jam == "":
                print("❌ Jam tidak boleh kosong!")
                jam = input("Jam Tayang (1/2/3): ").strip()
            elif jam not in daftar_jam_tayang:
                print("❌ Pilihan tidak valid!")
                jam = input("Jam Tayang (1/2/3): ").strip()

        jam = daftar_jam_tayang[jam]

        total2 = sum(b["harga_tiket"] for b in bookings if b["judul_film"] == film and b["jam_tayang"] == jam)
        data = [b for b in bookings if b["judul_film"] == film and b["jam_tayang"] == jam]
        total_tiket = len(data)
        print("----Laporan Pendapatan---")
        print("Film:", film)
        print("Jam Tayang:", jam)
        print("Total Tiket Terjual:", total_tiket)
        print("Total Pendapatan per Film:", total2)

    elif pilihan == 3:
        print("Daftar Film: ")
        for n, f in enumerate(daftar_film.values(), start=1):
            print(f"{n}. {f}")

        film = input("Judul Film (1/2/3): ").strip()

        while film == "" or film not in daftar_film:
            if film == "":
                print("❌ Judul film tidak boleh kosong!")
                film = input("Judul Film (1/2/3): ").strip()

            elif film not in daftar_film:
                print("❌ Pilihan tidak valid!")
                film = input("Judul Film (1/2/3): ").strip()

        film = daftar_film[film]

        print("Daftar Jam Tayang: ")
        for n, f in enumerate(daftar_jam_tayang.values(), start=1):
            print(f"{n}. {f}")
        jam = input("Jam Tayang (1/2/3): ").strip()

        while jam == "" or jam not in daftar_jam_tayang:
            if jam == "":
                print("❌ Jam tidak boleh kosong!")
                jam = input("Jam Tayang (1/2/3): ").strip()
            elif jam not in daftar_jam_tayang:
                print("❌ Pilihan tidak valid!")
                jam = input("Jam Tayang (1/2/3): ").strip()

        jam = daftar_jam_tayang[jam]

        hari = input("Hari: ").upper()
        while hari not in ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU"]:
            print("❌ Hari tidak valid!")
            hari = input("Hari: ").upper()

        total3 = sum(b["harga_tiket"] for b in bookings if b["judul_film"] == film and b["jam_tayang"] == jam and b["hari_tayang"] == hari)
        data = [b for b in bookings if b["judul_film"] == film and b["jam_tayang"] == jam and b["hari_tayang"] == hari]
        total_tiket = len(data)
        print("----Laporan Pendapatan---")
        print("Film:", film)
        print("Jam Tayang:", jam)
        print("Hari Tayang:", hari)
        print("Total Tiket Terjual:", total_tiket)
        print("Total Pendapatan per Film:", total3)
    else:
        print("❌ Pilihan tidak valid!")

def menu_utama():
    while True:
        print("""
MENU RESERVASI KURSI BIOSKOP
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

        if pilih == "1":
            create_booking()
        elif pilih == "2":
            read_booking()
        elif pilih == "3":
            update_booking()
        elif pilih == "4":
            delete_booking()
        elif pilih == "5":
            sorting_booking()
        elif pilih == "6":
            search_booking()
        elif pilih == "7":
            tampilkan_kursi()
        elif pilih == "8":
            laporan_pendapatan()
        elif pilih == "0":
            break
        else:
            print("❌ Pilihan tidak valid!")


menu_utama()
