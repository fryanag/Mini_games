import random

# Fungsi untuk memeriksa apakah sebuah bilangan prima
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Fungsi utama
def generate_random_list_and_check_primes(n):
    # Membuat list angka random sebanyak n
    random_list = [random.randint(1, 100) for _ in range(n)]
    
    # Mencari bilangan prima dalam list
    prime_numbers = [num for num in random_list if is_prime(num)]
    
    print("List random:", random_list)
    if prime_numbers:
        print("Bilangan prima dalam list:", prime_numbers)
    else:
        print("Tidak ada bilangan prima dalam list.")

# Input angka n
n = int(input("Masukkan jumlah angka yang ingin di-generate: "))
generate_random_list_and_check_primes(n)