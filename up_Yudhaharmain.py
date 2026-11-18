print("==========================================")
print("     PROGRAM KASIR KANTIN KAMPUS  ")
print("==========================================")

# Inisialisasi variabel total belanja awal
total_belanja = 0

# 4. Gunakan Perulangan (Agar pengguna dapat memasukkan lebih dari satu jenis makanan)
while True:
    print("\n--- Masukkan Data Makanan ---")
    nama_makanan = input("Masukkan nama makanan : ")
    
    # Validasi input harga dan jumlah berupa angka
    try:
        harga = float(input("Masukkan harga satuan : Rp "))
        jumlah = int(input("Masukkan jumlah beli   : "))
    except ValueError:
        print("Input harga atau jumlah harus berupa angka! Silakan ulangi.")
        continue

    # 2. Hitung Total harga setiap transaksi
    subtotal = harga * jumlah
    total_belanja += subtotal
    
    print(f"Subtotal untuk {nama_makanan}: Rp {subtotal:,.2f}")

    # Konfirmasi apakah ingin menambah transaksi lagi
    tanya = input("\nIngin menambah makanan lain? (y/t): ").strip().lower()
    if tanya != 'y':
        break

print("\n==========================================")
print("              STRUK PEMBELAJARAN          ")
print("==========================================")
print(f"Total Belanja Awal : Rp {total_belanja:,.2f}")

# 3. Tentukan Diskon (Gunakan percabangan untuk diskon 10% jika > Rp100.000)
if total_belanja > 100000:
    diskon = 0.10 * total_belanja
    total_pembayaran = total_belanja - diskon
    print("Status Diskon      : Selamat! Anda Mendapat Diskon 10%")
    print(f"Besar Diskon       : Rp {diskon:,.2f}")
else:
    diskon = 0
    total_pembayaran = total_belanja
    print("Status Diskon      : Tidak ada diskon (Belanja <= Rp100.000)")

# 5. Tampilkan Hasil (Total belanja dan total pembayaran setelah diskon)
print("------------------------------------------")
print(f"TOTAL PEMBAYARAN   : Rp {total_pembayaran:,.2f}")
print("==========================================")
print("Terima kasih sudah berbelanja di Kantin Kampus!")