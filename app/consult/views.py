from django.shortcuts import render
import requests
from core.settings import MITDB_HOST

def consult(request):
    params = {
        "record": "100",
        "signal": "MLII",
        "signal": "V5",
        "t0": "0",
        "dt": "10",
    }
    
    response = requests.get(MITDB_HOST, params=params)
    if response.status_code == 200:
        datos = response.json()
    
    print(datos)
    return datos