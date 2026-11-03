print("Kelembapan Tanah Dan Status Pompa Air Otomatis")
# Data Inti, 15 data
Data_Inti = [ 22, 28, 34, 41, 55, 
              63, 72, 78, 31, 47,
              67, 81, 19, 58, 69,] 

# Data Uji,  5 data
Data_Uji = [24, 33, 44, 55, 66]

#Apabila data utama hanya ingin di data realistis, maka Data_utama = Data_Realistis,Begitu juga sebaliknya
Data_utama = Data_Uji + Data_Inti

#Fungsi
def Status_sensor(nilai):
    if nilai < 35:
        return "Kering"
    elif nilai < 70:
        return "Normal"
    else:
        return "Basah"

def Status_Pompa(status):
    if status == "Kering":
        return "Pompa Hidup"
    else:
        return "Pompa Mati"

def Rata_rata(data):
    total = sum(data)
    jumlah_data = len(data)
    rata_rata = total / jumlah_data if jumlah_data > 0 else 0
    return round(rata_rata, 2)


print("==================================================")

for i in range(len(Data_utama)):
    nilai = Data_utama[i]
    status = Status_sensor(nilai)
    pompa = Status_Pompa(status)
    print(f"Data ke{i+1}: {nilai}% => Status: {status} => Pompa: {pompa}")
    
print("==================================================")

#print hasil perhitungan
print("jumlah data:", len(Data_utama))
print("Rata-rata:", Rata_rata(Data_utama))
print("Data Maksimum Kelembapan Tanah:", max(Data_utama), "%")
print("Data Minimum Kelembapan Tanah:", min(Data_utama), "%")

statutes = [Status_sensor(nilai) for nilai in Data_utama]
sum_kering = sum(1 for s in statutes if s == "Kering")
sum_basah = sum(1 for s in statutes if s == "Basah")
sum_normal = sum(1 for s in statutes if s == "Normal")
print("Status Kelembapan Tanah:")
print("Kering:", sum_kering)
print("Normal:", sum_normal)
print("Basah:", sum_basah)

statutes_pompa = [Status_Pompa(status) for status in statutes]
sum_pompa_hidup = sum(1 for p in statutes_pompa if p == "Pompa Hidup")
print("Status Pompa Hidup:")
print("Pompa Hidup:", sum_pompa_hidup)
print("Pompa Mati:", len(Data_utama) - sum_pompa_hidup) 