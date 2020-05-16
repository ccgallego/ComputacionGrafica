import json

with open('mapa.json') as archivos:
    datos=json.load(archivos)
print datos['layers'][1]['name']
mapa=datos['layers'][1]['data']
print len(mapa)
limite = datos['layers'][1]["width"]
limFilas = datos['layers'][1]["height"]
print limite, type(limite)
con=0
filas=0
inicio=0
for f in range(limFilas):
    cad=''
    for i in range(inicio,f*limite):
        cad= cad+str(mapa[i])
    inicio=(f*limite)+1
    print cad
