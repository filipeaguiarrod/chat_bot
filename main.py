from src import functions
import json
import os

print('Olá, como posso te ajudar?')

while True:
    message = input()

    if message.lower() == 'sair':
        print('Tchau, até logo!')
        break

    # Checar se temos respostas sem consultar api:

    answer,flag_api = functions.chat_with_bot(message)
    print(answer)

    # Caminho onde vamos armazenar conhecimento do chatgpt e interações.
    data_path = os.path.join(os.getcwd(), r'data\users_knowledge.json')

    if flag_api == True:

        functions.learn_saving(data_path,message=message,answer=answer)