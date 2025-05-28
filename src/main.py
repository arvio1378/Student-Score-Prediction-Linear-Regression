import joblib

# import modelnya
model = joblib.load("notebooks\model.pkl")

# ambil intercept dan coef
intercept = model.intercept_
coef = model.coef_

while True:
    print("="*40)
    print("PREDIKSI NILAI UJIAN SISWA DENGAN AI")
    print("="*40)

    try:
        # input dan output
        hours = float(input("Masukkan jumlah jam belajar anda : "))
        # rumus regresi
        scores = intercept + coef[0] * hours
        print(f"Prediksi skor yang didapatkan adalah {scores:.2f}\n")

        # keluar program
        exit = input("Keluar (y/n) ? ")
        if exit == "y":
            break
        elif exit == "n":
            continue
        else:
            print("Pilihan salah !!")

    except ValueError:
        print("Harap masukkan angka !!")