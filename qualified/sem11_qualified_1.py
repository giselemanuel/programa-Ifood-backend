import requests
retorna_objeto = requests.get("https://indicadores.integrasus.saude.ce.gov.br/api/casos-coronavirus?dataInicio=2021-01-15&dataFim=2021-01-15")
print(retorna_objeto.json())