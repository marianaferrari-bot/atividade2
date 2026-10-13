import datetime
import requests

def cotar():
    cotacoes = []
    hoje = datetime.date.today()

    for i in range(365):
        dia = hoje - datetime.timedelta(days=i)
        data_formatada = dia.strftime("%m-%d-%Y")

        url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_formatada}'&$format=json"

        resposta = requests.get(url)
        dados = resposta.json()

        if dados["value"]:
            cotacoes.append(dados["value"][0]["cotacaoCompra"])
        else:
            cotacoes.append(None)  
    ultimo = None
    for i in range(len(cotacoes) - 1, -1, -1):
        if cotacoes[i] is None:
            cotacoes[i] = ultimo
        else:
            ultimo = cotacoes[i]

    # Caso os dias mais antigos da lista sejam não úteis, repete o valor mais novo ao lado
    for i in range(len(cotacoes)):
        if cotacoes[i] is None and i > 0:
            cotacoes[i] = cotacoes[i - 1]

    return cotacoes
resultado = cotar()
