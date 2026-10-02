operacao = input("""A: multiplicação
B: divisão """)

a = input("digite o valor de a: ")
b = input("digite o valor de b: ")

if operacao == "A" or operacao == "a":
    linhas_parciais = []
    largura = len(a + b)
    total = 0 

    for posicao, digito in enumerate(reversed(b)):
        if digito == "1":
            linhas_parciais.append((a + posicao*"0").zfill(largura))
        else:
            linhas_parciais.append(("0"*posicao).zfill(largura))

    for linha in linhas_parciais:
        total += int(linha, 2) 

    resultado = format(total, "b").zfill(largura)

    print("A multiplicação de", a, b)
    print(a.rjust(largura))
    print(("x" + b).rjust(largura))
    print("-----")
    for linha in linhas_parciais:
        print(linha)
    print("-----")
    print(resultado)

else: 
    divisor = int(b, 2)
    resto = 0
    quociente = ""

    for posicao, numeros in enumerate(a):
        coluna = posicao + 1
        resto = resto * 2 + int(numeros)

        if resto >= divisor:
            quociente += "1"
            print(format(resto, "b").zfill(coluna))        
            print(format(divisor, "b").zfill(coluna))      
            print("-" * coluna)
            resto -= divisor 
        else: 
            quociente += "0"

    print(a + "|" + b)
    print(format(resto, "b").zfill(len(a)))                
    print("Quociente:", format(int(quociente, 2), "b"))    
    print("Resto:", format(resto, "b"))                    

