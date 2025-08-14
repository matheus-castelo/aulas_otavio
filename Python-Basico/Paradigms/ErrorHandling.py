import requests

url = "https://macoratti.net/dados/poesia.txt"

try:
    print(f"Tentando baixar: {url}")
    resposta = requests.get(url, timeout=5)  # tempo limite de 5 segundos
    resposta.raise_for_status()  # dispara exceção se status não for 200 (OK)

    # Mostrando conteúdo
    print("\nArquivo baixado com sucesso!")
    print("-" * 40)
    print(resposta.text)  # conteúdo do arquivo
    print("-" * 40)

except requests.exceptions.HTTPError as erro_http:
    print(f"Erro HTTP: {erro_http}")
except requests.exceptions.ConnectionError:
    print("Erro de conexão. Verifique sua internet ou o site.")
except requests.exceptions.Timeout:
    print("A requisição demorou demais e foi cancelada (timeout).")
except requests.exceptions.RequestException as erro:
    print(f"Erro genérico ao fazer requisição: {erro}")

finally:
    print("Execução finalizada. (try/except/finally)")

# Exemplo adaptado do curso do Macorrati (C#)
