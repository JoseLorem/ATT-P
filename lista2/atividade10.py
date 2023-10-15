import requests

url = "https://api.hgbrasil.com/weather?key=SUA_CHAVE_DE_API_AQUI&city_name={}"

cidade = input("Digite o nome da cidade: ")

url_cidade = url.format(cidade)

resposta = requests.get(url_cidade).json()

temperatura = resposta["results"]["temp"]
sensacao_termica = resposta["results"]["description"]
descricao = resposta["results"]["description"]

print(f"Previsão do tempo para {cidade}:")
print(f"Temperatura: {temperatura}°C")
print(f"Sensação térmica: {sensacao_termica}")
print(f"Descrição: {descricao}")