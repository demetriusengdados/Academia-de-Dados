import subprocess

def chamar_arquivos():
    try:
        # Chama o primeiro arquivo
        resultado1 = subprocess.run(['python', 'arquivo1.py'], capture_output=True, text=True)
        print("Saída do arquivo1.py:")
        print(resultado1.stdout)
        
        # Chama o segundo arquivo
        resultado2 = subprocess.run(['python', 'arquivo2.py'], capture_output=True, text=True)
        print("Saída do arquivo2.py:")
        print(resultado2.stdout)
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    chamar_arquivos()
