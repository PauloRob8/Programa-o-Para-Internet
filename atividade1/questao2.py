import requests

def main():

    r = requests.get('http://www.databrain.com.br/images/logo/python-logo.png')

    with open('teste.png','wb') as imagem:
        imagem.write(r.content)

if __name__ == '__main__':
    main()