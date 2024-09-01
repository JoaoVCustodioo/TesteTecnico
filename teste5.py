

palavra = "vasquinho"

palavra_invertida = ""

for i in range(len(palavra) - 1, -1, -1):
    palavra_invertida += palavra[i]
    
print(palavra_invertida)