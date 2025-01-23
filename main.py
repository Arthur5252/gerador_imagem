from gera_imagem import *
from download_imagem import *
from gera_prompt import *

def main(descricao='BOP'):
    descricao = gera_prompt(descricao)
    url = gera_imagem(descricao)
    download_imagem(url)

main()