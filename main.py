import requests as req
import json


def buscar_cep(cep):
    """
    Busca informações de um CEP usando a API ViaCEP.
    
    Args:
        cep (str): CEP no formato '00000000' ou '00000-000'
    
    Returns:
        dict: Dados do CEP em formato JSON, ou None em caso de erro
    """
    # Remove caracteres não numéricos do CEP
    cep = ''.join(filter(str.isdigit, cep))
    
    # Valida se o CEP tem 8 dígitos
    if len(cep) != 8:
        print("CEP inválido! O CEP deve conter 8 dígitos.")
        return None
    
    # URL da API ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        # Faz a requisição GET
        resposta = req.get(url, timeout=10)
        
        # Verifica se a requisição foi bem-sucedida
        resposta.raise_for_status()
        
        # Converte a resposta para JSON
        dados = resposta.json()
        
        # Verifica se o CEP foi encontrado (a API retorna 'erro': true se não encontrar)
        if dados.get('erro'):
            print(f"CEP {cep} não encontrado!")
            return None
        
        return dados
    
    except req.exceptions.RequestException as e:
        print(f"Erro ao fazer requisição: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return None


if __name__ == "__main__":
    # Exemplo de uso
    cep = input("Digite o CEP (formato: 00000000 ou 00000-000): ")
    
    resultado = buscar_cep(cep)
    
    if resultado:
        print("\n=== Dados do CEP ===")
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
