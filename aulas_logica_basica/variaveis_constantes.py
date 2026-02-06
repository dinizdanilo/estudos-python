"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância que o radar pega

velocidade_passou_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_passou_radar_1 = carro_multado_radar_1 and velocidade_passou_radar_1

if velocidade_passou_radar_1:
    print('O carro ultrapassou a velocidade máxima.')
    
if carro_passou_radar_1:
    print('Carro passou no radar 1.') 
    
if carro_multado_radar_1:
    print('Carro multado em radar 1.')             