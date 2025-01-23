from openai import OpenAI
from helpers import *

def gera_imagem(descricao):
  contexto = carrega('contextos/contexto.txt')
  #client = OpenAI(api_key='chave api aqui')

  response = client.images.generate(
    model="dall-e-3",
    prompt=f"{contexto} Descrição: {descricao}",
    size="1024x1024",
    quality="standard",
    style='natural',
    n=1,
  )

  image_url = response.data[0].url
  print(image_url)
  return image_url