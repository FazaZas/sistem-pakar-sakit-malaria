import os

print("Sistem Pakar Sakit Malaria")

nama = input("nama\t:")
pilihan = input("Hallo"+nama+",\nApakah anda ingin melakukan diagnosa ? (y/n)")

os.system("clear")

while pilihan == "y":
    print("\nApakah anda merasakan gejala berikut ini ?")
    print("1. Demam / suhu badan tinggi")
    print("2. Sakit kepala")
    print("3. Nyeri pada sendi otot dan tulang")
    print("4. Mual dan muntah")
    diag1 = input("Jawab (y/n) :")

    if diag1 == "y":
        print("\nApakah anda juga merasakan gejala berikut ini ?")
        print("1. Hilang nafsu makan")
        print("2. Nyeri pada bagian belakang mata")
        print("3. Ruam kemerahan")
        diag2 = input("Jawab (y/n) :")

        if diag2 == "y":
            print(
                "Hallo"+nama+",\nHasil awal diagnosa kamu adalah gejala malaria, segera periksa ke Dokter !")
        elif diag2 == "n":
            print("\nApakah anda juga merasakan gejala berikut ini ?")
            print("1. Menggigil sedang samapi berat")
            print("2. Tubuh kelelahan")
            print("3. Banyak berkeringat")
            print("4. Diare")
            diag3 = input("Jawab (y/n) :")

            if diag3 == "y":
                print(
                    "Hallo"+nama+",\nHasil awal diagnosa kamu adalah gejala malaria, segera periksa ke Dokter !")
            elif diag3 == "n":
                print("Hallo"+nama+",\nanda sepertinya tidak mengalami gejala malaria")
            else:
                print("\nAnda tidak bersedia untuk periksa")
        else:
            print("\nAnda tidak bergejala covid-19")
    elif diag1 == "n":
        print("\nAnda tidak bergejala malaria")
    else:
        print("\nAnda tidak bergejala malaria")
    pilihan = input(
        "Hallo"+nama+",\nApakah anda ingin melakukan diagnosa ? (y/n)")

    if pilihan == "y":
        os.system("clear")
        print()
