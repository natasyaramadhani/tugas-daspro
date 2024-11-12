#Nama: Natasya Ramadhani
#NIM: 2403264   
#Kelas: RPL/1C

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def validasi_input():
    try:
        N = int(input("Masukkan nilai N: "))
        if N > 0:
            return N
        else:
            print("Masukkan bilangan positif.")
            return None
    except ValueError:
        print("Input tidak valid. Harap masukkan angka integer.")
        return None
N = validasi_input()
if N is not None:
    fibonacci(N)