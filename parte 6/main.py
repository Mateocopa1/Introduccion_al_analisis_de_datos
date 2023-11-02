import requests
import pandas as pd
import csv
#solicitud de la url de la api
api_url = input('Ingrese la URL de la api a consultar: /n')
#solicitud de nombre del archivo
archivo = input('la api tiene contraseña: (conteste (Y) para si y (N) para no)')
if archivo == 'Y':
    contraseña = input('Ingrese la contraseña para la api')
    response = requests.get(api_url, headers={'X-Api-Key': contraseña})
elif archivo == 'N':
    response = requests.get(api_url)
else:
    print('compruebe su respuesta solo es valido (Y) y (N)')
#consumo de la api

df = pd.DataFrame()
# verificacion del consumo
if response.status_code == 200:
    #exportacion de la data a csv
    data = response.json()
    df = data
    # caso de que no halla informacion
else:
    print(f'Compruebe la url {api_url}, ya que no esta entregando datos')

print(df)

comprovacion= input('Tus Datos esten en el formato correcto?: (Y) (N): ')

if comprovacion == "Y":
    nombre = input('Ingresa el nombre de tu archivo cvs: ')
    df.to_csv(f'{nombre}.cvs', index=False)
else:
    print('UHSS Aun no tengo ese desarollo')

