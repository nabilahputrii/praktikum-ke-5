# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:44:36 2021
@judul : Praktikum ke-5
@NIM : 065002100002
@author: Nabilah Putri

@author: nabilah
"""

angka = 0
nilaisiswa = list()
repeat = 0
nomor = 0
while repeat == 0:
    nomor += 1
    enterNilai= str(input("silahkan masukan nilai : "))
    if not enterNilai:
        break
    else:
        if enterNilai == "A":
            angka = float (4.00)
        elif enterNilai == "A-":
            angka = float(3.75)
        elif enterNilai== "B+":
            angka = float(3.50)
        elif enterNilai== "B":
            angka = float(3.00)
        elif enterNilai== "B-":
            angka = float (2.75)
        elif enterNilai== "C+":
            angka = float (2.50)
        elif enterNilai== "C":
            angka = float (2.00)
        elif enterNilai== "C-":
            angka = float (1.75)
        elif enterNilai== "D":
            angka = float (1.50)
        elif enterNilai== "E":
            angka = float (1.25)
        else:
            print("silahkan anda masukan angka yang benar")
            angka = 0
        print((f"Nilai = {angka}"))
        nilaisiswa.append(angka)
        
rata_rata = sum(nilaisiswa) / len(nilaisiswa)
print ("rata-rata angka siswa adalah :", rata_rata)       