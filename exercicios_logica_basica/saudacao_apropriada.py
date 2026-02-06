hora = input('Que horas são agora?: ')

# try:
#     hora = int(hora)
#     if hora in range(0, 12):
#         print('Bom dia!')
#     elif hora in range(12, 18):
#         print('Boa tarde!')
#     elif hora in range(18, 24):
#         print('Boa noite!')    
# except ValueError: 
#     print('Digite um horário válido!')
    
try:
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Digite um horário válido!')        
except ValueError: 
    print('Digite um horário válido!')    