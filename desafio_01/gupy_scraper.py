import requests
import json
import os


def salvar_dados(termo= "python"):
    headers = {
            "user-agent": "Mozilla/5.0"
        }
    
    params = {"name":termo,
              "offset":0,
              "limit":10}
    
    url = f"https://portal.api.gupy.io/api/job"
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        dados = response.json()
        os.makedirs("desafio_01/dados/vagas", exist_ok=True) 
        with open(f"desafio_01/dados/vagas_{termo}.json", "w", encoding="utf-8") as f:
             json.dump(dados, f, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso!")
    else:
        print(f"Erro ao acessar a API: {response.status_code}")

salvar_dados("python")