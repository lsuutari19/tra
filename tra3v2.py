import time
import random



#listan luonti käyttäjän antamalla muuttujalla
def create_list():
    A = []
    p = int(input("Gib number: "))
    for i in range(p):
        A.append(i)
    return A

#shuffle
def RANDPERM(n, A):
    for i in A:  # Taulukon alustus järjestykseen 1,2,..,n 
        A[i] = i + 1
    for i in range(n):
        x = random.randint(0, i) #satunnaisluku väliltä 0, i , i = 1,2,3....n
        A[i], A[x] = A[x], A[i]
    return
 
A = create_list()

start = time.perf_counter() 
RANDPERM(len(A), A)
end = time.perf_counter() - start
print(end)

print(A) 
