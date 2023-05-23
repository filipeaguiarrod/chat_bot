import openai
import os
import json

def consulting_knwoldge():
    return

# Função para obter a resposta a partir da pergunta
def obter_resposta(pergunta):
    # Verificar se a pergunta está no JSON de perguntas e respostas
    if pergunta in perguntas_respostas:
        return perguntas_respostas[pergunta]
    

def chat_with_bot(message):
    # Receber mensagens e entender se tenho alguma resposta para isso.
    lower_message = message.lower()

    # Abrir json onde conheço respostas
    data_known_path = os.path.join(os.getcwd(), r'data\self_knowledge.json')
    data_path = os.path.join(os.getcwd(), r'data\users_knowledge.json')

    with open(data_known_path, 'r', encoding='utf-8') as file:
        data = json.load(file)  

    with open(data_path, 'r', encoding='utf-8') as file:
        data2 = json.load(file)

    merged_data = {**data,**data2}

   # Olha para os dados e retorna possíveis perguntas - retorna se encontrou algo
   # Espaço para melhoria através se similaridade de sentenças (DS)

    possible_answers = []

    for pergunta in merged_data.keys():

        if message in pergunta:

            possible_answers.append(pergunta)

    # Caso encontre algo parecido retorna 
    
    if len(possible_answers)>0:

        flag_api=False
        return merged_data[possible_answers[0]],flag_api

    else:
        flag_api=True
        return enviar_mensagem(message),flag_api
    

def learn_saving(json_file_path,message,answer):

    """
    A partir do momento que não temos repostas já conhecidas iremos
    buscar na api do chatgpt e salvar a iteração dos usuários e a resposta do chatgpt.
    Recebe: arquivo json
    Retorna: mesmo arquivo + append de perguntas
    """ 

    # Abrir onde vou salvar os dados e ler 
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Adicionar a chave e valor no json lowercased
    new_key = message.lower()
    new_value = answer.lower()
    data[new_key] = new_value

    # Salvar os dados completos
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file,indent=4)

def enviar_mensagem(message):
    # Enviar a mensagem para o ChatGPT e receber a resposta

    openai.api_key = os.environ['CHAT_GPT']

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Especificar a versão do modelo
        messages=[
            {"role": "system", "content": "Você é um assistente que fala português."},
            {"role": "user", "content": message}
        ],
        max_tokens=None,  # Limitar o tamanho da resposta
        temperature=0.7,  # Controlar a criatividade da resposta
        n=1  # Número de respostas a serem geradas
    )

    # Extrair e retornar a resposta do ChatGPT

    answer = resposta.choices[0].message['content'].strip()
    
    return answer
