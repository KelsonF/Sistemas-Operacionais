import os

def criar_e_editar_arquivo():
    nome_arquivo = "meu_arquivo.txt"
    comando = f"echo 'Só alegria hahaha' > {nome_arquivo}"
    os.system(comando)

criar_e_editar_arquivo()
