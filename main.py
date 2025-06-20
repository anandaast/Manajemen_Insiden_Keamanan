# brute_force_full.py

# Data login valid
valid_username = "admin"
valid_password = "admin123"

# Simulasi percobaan login
attempts = [
    ("admin", "12345"),
    ("admin", "admin"),
    ("admin", "password"),
    ("admin", "admin123"),  # berhasil
]

# Logging hasil login
logs = []
fail_count = 0

print("=== Simulasi Login ===")
for i, (u, p) in enumerate(attempts):
    if p == valid_password:
        log = f"Attempt {i+1}: LOGIN SUCCESS from user={u}, password={p}"
        print(f"{log} ✅")
    else:
        log = f"Attempt {i+1}: LOGIN FAILED from user={u}, password={p}"
        print(f"{log} ❌")
        fail_count += 1
    logs.append(log)

# Simpan ke file log
with open("login_log.txt", "w") as f:
    for l in logs:
        f.write(l + "\n")

# Deteksi brute force
print("\n=== Analisis Keamanan ===")
if fail_count >= 3:
    print(f"WARNING: Potensi brute force terdeteksi! Total gagal: {fail_count}")
    print("AKSI: IP pelaku dikarantina (simulasi), Admin telah diberitahu 🚨")
else:
    print("Login normal. Tidak ada indikasi brute force.")
