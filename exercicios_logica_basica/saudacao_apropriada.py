hora = input('Que horas são agora?: ')

try:
    hora = int(hora)
    if hora in range(0, 12):
        print('Bom dia!')
    elif hora in range(12, 18):
        print('Boa tarde!')
    else:
        print('Boa noite!')    
except: 
    print('Digite um horário válido!')