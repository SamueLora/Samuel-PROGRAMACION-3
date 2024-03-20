#SAMUEL LORA GARCÉS

vuelo = {
    'Aerolinea': 'Avianca',
    'Vuelo': 'AV3102',
    'Origen': 'CTG',
    'Destino': 'MDE',
    'Tipo_Maleta': ['Cabina', 'Mano', 'Bodega']
}


for key, value in vuelo.items():
    print(f"{key}: {value}")

print(" ")
print("Valores del tipo de maleta:")
for tipo_maleta in vuelo['Tipo_Maleta']:
    print(tipo_maleta)