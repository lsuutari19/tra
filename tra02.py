#taulukon pitäisi olla syöte muotoa A[0,1....,n-1] n>=1 




A = [0, 1, 2, 3, 4]
n = len(A)  #otetaan listan pituus

def reverse(A, n):
    i = 0
    while i < n/2:  #poistettiin vain yhtäsuuruusmerkki
        temp = A[i]
        A[i] = A[n-i-1]
        A[n-i-1] = temp
        i = i+1
    return

reverse(A, n)
print(A)

