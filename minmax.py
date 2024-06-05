def hitung_statistik(data):
    # Nilai maksimum
    max_value = max(data)
    
    # Nilai minimum
    min_value = min(data)
    
    # Jangkauan data
    range_data = max_value - min_value
    
    # Mean (rata-rata)
    mean = sum(data) / len(data)
    
    # Median
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    
    # Modus
    from collections import Counter
    counts = Counter(data)
    modus = [k for k, v in counts.items() if v == max(counts.values())]
    
    # Varians
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    
    # Standar deviasi
    std_dev = variance ** 0.5
    
    return {
        "max": max_value,
        "min": min_value,
        "range": range_data,
        "mean": mean,
        "median": median,
        "modus": modus,
        "varians": variance,
        "standard_deviasi": std_dev
    }

def input_data():
    data = []
    i = 0
    while i < 10:
        input_value = input(f"Masukkan angka ke-{i+1}: ")
        if input_value.replace('.', '', 1).isdigit():
            angka = float(input_value)
            data.append(angka)
            i += 1
        else:
            print("Input tidak valid. Masukkan angka.")
    return data

# Input data dari pengguna
data_angka = input_data()

# Hitung statistik
hasil_statistik = hitung_statistik(data_angka)

# Print hasil
print("Hasil Statistik:")
print("Nilai maksimum:", hasil_statistik["max"])
print("Nilai minimum:", hasil_statistik["min"])
print("Jangkauan data:", hasil_statistik["range"])
print("Mean:", hasil_statistik["mean"])
print("Median:", hasil_statistik["median"])
print("Modus:", hasil_statistik["modus"])
print("Varians:", hasil_statistik["varians"])
print("Standard Deviasi:", hasil_statistik["standard_deviasi"])
