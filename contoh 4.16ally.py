#Mengira isi padu piramid bertapak segi empat sama
def kira_Isipadu_piramid(sisi,tinggi):
    isipadu_piramid=(1/3)*(sisi*sisi)*tinggi
    return (isipadu_piramid)

#Atur cara utama
print("Kira Isi Padu Piramid")
a=int(input("Masukkan ukuran sisi tapak piramid:"))
b=int(input("Masukkan tinggi piramid:"))

#Pemanggilan function dan pemulangan nilai
print("Isi Padu Piramid=",kira_Isipadu_piramid(a,b)) 
