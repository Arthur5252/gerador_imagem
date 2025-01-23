from openai import OpenAI
from helpers import *

def gera_prompt(descricao):
    contexto = carrega('contextos/contexto_prompt.txt')
    print(f'contexto do prompt:\n{contexto}')
    #client = OpenAI(api_key = 'chave api aqui')

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": f"{contexto}"},
            {
                "role": "user",
                "content": f"{descricao}"
            }
        ]
    )
    resposta = completion.choices[0].message.content
    print(f"Prompt gerado: \n{resposta}")
    return completion.choices[0].message.content