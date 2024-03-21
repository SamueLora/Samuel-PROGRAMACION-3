#SAMUEL LORA GARCÉS

#1
ListaV= []

#2
Lista5= ["Mouse", "Teclado", "Monitor", "Audifonos", "CPU"]

#3
print (len(Lista5))

#4
print(Lista5[0], Lista5[2], Lista5[4])

#5
tipos_datos_mezclados= ["Samuel", 19, 1.82, "soltero", "Mi barrio calle 80"]
print(tipos_datos_mezclados)

#6
it_companies= []
it_companies.insert(1, "Facebook")
it_companies.insert(2, "Google")
it_companies.insert(3, "Microsoft")
it_companies.insert(4, "Apple")
it_companies.insert(5, "IBM")
it_companies.insert(6, "Oracle")
it_companies.insert(7, "Amazon")
print(it_companies)

#7
it_companies.append("Facebook")
print(it_companies)

#8
verificar= "Facebook" in it_companies
print(verificar)

#9
it_companies.sort()
print(it_companies)

#10
it_companies.sort(reverse=True)
print(it_companies)

#11
del it_companies[0]
print(it_companies)

#12
it_companies.clear()
print(it_companies)