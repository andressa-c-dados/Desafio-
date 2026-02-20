
from gupy_scraper import salvar_dados

filter_labels = [
        "analista",
        "dados",
        "python",
        "data",
        "Desenvolvedor",
        "Dev",
        "Front-end",
        "Back-end",
        "Full Stack",
        "FullStack",
        "Software",
        "DevOps",
        "Business Intelligence",
        "Machine Learning",
        "Inteligência Artificial",
    ]

for termo in filter_labels:
    print(f"Buscando vagas para: {termo}")
    salvar_dados(termo)
