import requests


def main():

    r = requests.get('https://github.com/PauloRob8/Programa-o-Para-Internet')
    print(r.status_code)
    print(r.headers)
    print(r.content)
    print(r.text)

if __name__ == '__main__':
    main()
