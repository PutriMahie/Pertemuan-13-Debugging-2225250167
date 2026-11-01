def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    else:
        return "Tidak lulus"


nilai = 60

print("Nilai:", nilai)
print("Status:", status_lulus(nilai))