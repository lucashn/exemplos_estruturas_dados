try:
    with open("arquivo_inexistente") as arq:
        for linha in arq:
            print(linha)
        
        print("Fim.")

except FileNotFoundError as e:
    print(f"Arquivo não existe: {e}")

except Exception as e:
    print(f"Exceção: {e}")