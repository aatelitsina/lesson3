import requests
from api_settings import api_key

def get_child(adress):
    response = requests.get(adress)
    if response.status_code == 200:
        return resp onse.json()
    else:
        return 'Ошибка!'


if __name__ == "__main__":
    result = get_child('http://api.data.mos.ru/v1/datasets/2009/rows?API_KEY={}'.format(api_key))
<<<<<<< HEAD
    print(result)
=======
    print(result)
>>>>>>> e0b638bd046dc1afb950c7900f88b49c2fecd00a
