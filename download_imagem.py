import requests

def download_imagem(url):
    response = requests.get(url)
    nome_arquivo = 'imagens/imagem_baixada.jpg'
    with open(nome_arquivo, 'wb') as arquivo:
        arquivo.write(response.content)
    print("Imagem salva!")