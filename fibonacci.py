#Nama: Natasya Ramadhani
#NIM: 2403264   
#Kelas: RPL/1C

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b
N = int(input("Masukkan nilai N: "))
if N > 0:
    fibonacci(N) 
else:
    print("Masukkan bilangan positif.")