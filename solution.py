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
            cotacao = dados["value"][0]["cotacaoCompra"]
            cotacoes.append(cotacao)

    return cotacoes