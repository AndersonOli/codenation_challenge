import requests, json, hashlib

def main():
    # Meu token para o request
    token = '705f56105c0dd7e6a15f78af7d83c7f32239f0be'
    # Request
    request_cifra = requests.get(
        'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + token)

    # String do request passando para json
    str_request = json.loads(request_cifra.content)

    # Numero de casas da cifra
    numero_casas = str_request['numero_casas']

    # Texto cifrado
    cifrado = str_request['cifrado']

    # Variavel para o texto decifrado
    decifrado = str_request['decifrado']

    # Araay com o alfabeto
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for caracter in cifrado:
        if (caracter in alfabeto):
            decrypt = alfabeto.index(caracter) - numero_casas
            decifrado += alfabeto[decrypt]
        else:
            decifrado += ' '

    # Atribui o texto decifrado ao json original
    str_request['decifrado'] = decifrado
    # Atribui o resumo criptográfico ao json original
    str_request['resumo_criptografico'] = hashlib.sha1(decifrado.encode('utf-8')).hexdigest()

    # Salva o json em answer.json
    arquivo = open('answer.json', 'w')
    arquivo.write(str(str_request).replace("'", '"'))
    arquivo.close()

    # Envia o arquivo via POST
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=' + token
    files = {'answer': ('answer.json', open('answer.json', 'rb'))}
    send_request = requests.post(url, files=files)
    print(send_request.content)

if __name__ == '__main__':
    main()