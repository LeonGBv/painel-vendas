from processar_csv import processar_csv
from enviar_telegram import enviar_mensagem

try:

    total = processar_csv()

    mensagem = f'''
Sistema atualizado

Registros processados: {total}
'''

    enviar_mensagem(mensagem)

    print('Sistema executado com sucesso!')

except Exception as e:

    erro = f'Erro no sistema:\n{str(e)}'

    enviar_mensagem(erro)

    print(erro)