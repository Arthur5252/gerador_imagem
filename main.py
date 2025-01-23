from openai import OpenAI
#client = OpenAI(api_key='chave api aqui')

response = client.images.generate(
  model="dall-e-3",
  prompt="Uma imagem altamente detalhada de uma broca tricone amarela usada na perfuração de petróleo e gás, com um acabamento metálico. A broca é compacta e robusta, apresentando cones interligados cobertos com dentes de tungstênio de alta durabilidade e afiados. Os cones estão organizados em um design preciso para esmagar a rocha enquanto a broca gira. O corpo da broca possui uma base metálica rosqueada para fixação a uma coluna de perfuração. O fundo é preto, destacando o design detalhado, a cor e os aspectos mecânicos da broca.",
  size="1024x1024",
  quality="standard",
  style='natural',
  n=1,
)

image_url = response.data[0].url
print(image_url)