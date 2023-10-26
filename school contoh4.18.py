#Atur cara ini menggunakan built-in function random
import random

#User-defined function tambah()
def tambah(a,b):
    return(a+b)
    

#User-defined function semak()
def semak(jawapan,jumlah):
    if jawapan==jumlah:
        print("Betul!")
    else:
        print("Salah!Jawapannya ialah",jumlah)


#Atur cara utama
nombor1=random.randint(1,10)
nombor2=random.randint(1,10)
print("Selesaikan",nombor1,"+",nombor2,".")
jawapan=int(input("Jawapan anda:"))


#Pemanggilan function tambah() dan semak()
jumlah=tambah(nombor1,nombor2)
semak(jawapan,jumlah)
