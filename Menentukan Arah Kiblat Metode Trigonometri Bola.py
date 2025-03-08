print('+++++============================================+++++')
print('----Metode Trigonometri Bola Menentukan Arah Kiblat---')
print('------------Mata Kuliah Fisika Komputasi--------------')
print('------------Data Koordinat Google Map-----------------')
print('+++++============================================+++++')

from math import*

#Data koordinat berdasarkan Google Map
#Lintang Masjid Al-Jahidah Batujajar Bandung Barat 
inLL = input('Masukkan lintang lokasi : ') #Lintang dalam Desimal
LL = float(inLL)
Cos_LL = cos(radians(LL)) #Cos Lintang Masjid Al - Jahidah Batujajar Bandung Barat
Sin_LL = sin(radians(LL)) #Sin Lintang Masjid Al - Jahidah Batujajar Bandung Barat

#Bujur Masjid Al - Jahidah Batujajar Bandung Barat
inBL = input('Masukkan bujur lokasi : ') #Bujur dalam Desimal
BL = float(inBL)
Sin_BL = sin(radians(BL)) #Sin Lintang Masjid Al - Jahidah Batujajar Bandung Barat
Cos_BL = cos(radians(BL)) #Cos Lintang Masjid Al - Jahidah Batujajar Bandung Barat

#Lintang Mekkah
LM = 21.422599 #Lintang Mekkah dalam Desimal
Cos_LM = cos(radians(LM)) #Cos Lintang Mekkah
Sin_LM = sin(radians(LM)) #Sin Lintang Mekkah
Tan_LM = Sin_LM/Cos_LM

#Bujur Mekkah
BM = 39.826167 #Bujur Mekkah dalam Desimal
Sin_BM = sin(radians(BM)) #Sin Lintang Mekkah
Cos_BM = cos(radians(BM)) #Cos Lintang Mekkah

#Menentukan Selisih Bujur Lokasi dan Kota Mekkah
BLM = BL - BM
Cos_BLM = cos(radians(BLM))
Sin_BLM = sin(radians(BLM))

#Menentukan Tan Q
A = Sin_BLM #Sinus selisih bujur
B = Cos_LL*Tan_LM #Cosinus lintang lokasi dikali dengan tangan lintang mekah
C = Sin_LL*Cos_BLM #Sinus linta lokasi dikali cosinus bujur lokasi dan mekah

Tan_Q = A/(B-C)
D_Tan_Q = Tan_Q
M_Tan_Q =(D_Tan_Q - int(D_Tan_Q))*60.0
S_Tan_Q = round((M_Tan_Q - int(M_Tan_Q))*60.0)
Tan_Q1 = int(D_Tan_Q),int(M_Tan_Q),int(S_Tan_Q)
print("Tan Q (Desimal) = ", Tan_Q)
print("Tan Q (Sexagesimal) = ", Tan_Q1)

#Menentukan Q
Q = degrees(atan2(A,B-C))
print("Arc Tan 2 Q = ", Q)
D_Q = Q
M_Q = (D_Q - int(D_Q))*60.0
S_Q = round((M_Q - int(M_Q))*60.0)
Qs = int(D_Q),int(M_Q),int(S_Q)
print("Arc Tan 2 Q = ", Qs)

if Q>0:
    kiblat = 360-Q
    D_Q = kiblat
    M_Q = (D_Q - int(D_Q))*60.0
    S_Q = round((M_Q - int(M_Q))*60.0)
    Q1 = int(D_Q),int(M_Q),int(S_Q)
    print("Q (Kiblat Terhadap Utara) = ", kiblat)
    print("Q (Kiblat Terhadap Utara) = ", Q1)

else:
    kiblat = -Q
    D_Q = kiblat
    M_Q = (D_Q - int(D_Q))*60.0
    S_Q = round((M_Q - int(M_Q))*60.0)
    Q1 = int(D_Q),int(M_Q),int(S_Q)
    print("Q (Kiblat Terhadap Utara) = ", kiblat)
    print("Q (Kiblat Terhadap Utara) = ", Q1)

print('+++++=========================================+++++')
