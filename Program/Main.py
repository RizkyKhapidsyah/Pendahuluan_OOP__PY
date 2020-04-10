class Pahlawan:
    pass


Pahlawan1 = Pahlawan()
Pahlawan2 = Pahlawan()
Pahlawan3 = Pahlawan()

Pahlawan1.Nama = "Sisingamangaraja"
Pahlawan1.JenisKelamin = "Laki-Laki"

Pahlawan2.Nama = "Teuku Umar"
Pahlawan2.JenisKelamin = "Laki-Laki"

Pahlawan3.Nama = "Cut Nyak Dien"
Pahlawan3.JenisKelamin = "Perempuan"

print("PAHLAWAN 1")
print("Jenis Pahlawan 1  : ", Pahlawan1)
print("Atribut           : ", Pahlawan1.__dict__)
print("Nama Pahlawan 1   : ", Pahlawan1.Nama)
print("Jenis Kelamin     : ", Pahlawan1.JenisKelamin + "\n")

print("PAHLAWAN 2")
print("Jenis Pahlawan 2  : ", Pahlawan2)
print("Atribut           : ", Pahlawan2.__dict__)
print("Nama Pahlawan 2   : ", Pahlawan2.Nama)
print("Jenis Kelamin     : ", Pahlawan2.JenisKelamin + "\n")

print("PAHLAWAN 3")
print("Jenis Pahlawan 3  : ", Pahlawan3)
print("Atribut           : ", Pahlawan3.__dict__)
print("Nama Pahlawan 3   : ", Pahlawan3.Nama)
print("Jenis Kelamin     : ", Pahlawan3.JenisKelamin + "\n")