import re
max_correos = {}
max_horas = {}
mayor_envios = []
correo_max = 0
envios_max = 0

while True:
    archivo = input("Escriba el nombre del archivo: ")
    try: 
        txt = open(archivo) 
        break
    except: print("NO se encontró el archivo\nIntente nuevamente\n")
print("********** Las estadísticas **********\n")
print("Emails encontrados: \n")
for line in txt:
    line = line.rstrip()
    if re.findall('^From ', line):
        lines = line.split()
        emails = lines[1]
        hora = lines[5]
        hora = hora[0:2]
        max_correos[emails] = max_correos.get(emails, 0)+ 1
        max_horas[hora] = max_horas.get(hora, 0) + 1
        print(emails)
max_envios = max(max_correos.values())
for e,c in max_correos.items():
    if c == max_envios:
        mayor_envios.append((e,c))
for k,v in mayor_envios:
    print("\nCantidad máxima de correos enviados:",v,", | Remitente:",k,"\n")     
for x,y in max_correos.items():
   print("Email:",x,"| Envíos que realizó: ",y,)
print("")
for a,b in max_horas.items():
    print("Hora: ",a,"Correos enviados por hora: ",b,)


      





