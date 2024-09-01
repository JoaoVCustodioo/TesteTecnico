def fibonacci(n):
    n0, n1 = 0, 1
    while n0 <= n:
        if n0 == n:
            return True
        n0, n1 = n1, n0 + n1
    return False

num = int(input("informe o numero: "))
    
if fibonacci(num):
    print("nao pertence")
else: 
    print("pertence")