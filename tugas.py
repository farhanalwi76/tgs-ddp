#1
mobil = ["Tytot","mobil","7000","Silver","4"]
mobil.append("100.000.000")
mobil.append("mobil")
mobil.insert(2,"Bmw")
print(mobil)

#2
pilih = int(input ("mau hitung apa? 10 untuk persegi, 12 untuk lingkaran, 5 segitiga"))

match pilih:
 case 10:
  print(int(input ("berapa sisinya?")) ** 2)
 case 12:
  print(3.14 * int(input ("berapa jari jari nya?")) **2)
 case 5:
  print(1/2 * int(input("berapa alasnya? ")) * int(input("berapa tingginya?")))
 case _:
  print("salah angka")

  bilangan = int(input("Masukkan bilangan: "))

if bilangan % 2 == 0:
    print("Bilangan", bilangan, "adalah bilangan genap.")
else:
    print("Bilangan", bilangan, "adalah bilangan ganjil.")