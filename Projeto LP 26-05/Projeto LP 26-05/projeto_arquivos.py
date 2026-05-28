def salvar(texto_salvar):
    with open(r".\arquivo_EC.txt" , "a") as arquivo:
        arquivo.write(texto_salvar)