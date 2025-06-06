with open("saida.txt", "w") as arq:
    a = 10
    b = 8
    res = a * b

    arq.write(f"{a} x {b} = {res}\n")
    arq.write("Fim.\n")