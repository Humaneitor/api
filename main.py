import requests

direccion = "http://www.omdbapi.com/?apikey=e45ea178&i=tt3896198"

respuesta = requests.get(direccion)
if respuesta.status_code == 200:
    datos = respuesta.json()
    print (datos.keys())
else:
    print ("Se ha producido un error", respuesta.status_code)