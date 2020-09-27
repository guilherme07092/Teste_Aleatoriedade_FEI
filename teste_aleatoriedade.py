import pandas as pd
from bitstring import BitStream, BitArray
from collections import Counter

with open('chaves.txt', 'r') as file:
    chaves=file.read().replace("'",'').split("\n")
    
chavesBin = []
for i in range(20):
    chavesBin.append(BitArray(hex=chaves[i]).bin)

#Verificação 01 Monobit Test

resultadoVerificacao01 = []
soma = 0
for i in range(20):
    soma = 0
    for j in str(chavesBin[i]):
        if j == '0':
            soma = soma + 1
    if soma > 9654 and soma < 10346:
        resultadoVerificacao01.append("True")
    else:
        resultadoVerificacao01.append("False")
print(resultadoVerificacao01)

#Verifiação 02 The Poker Test

resultadoVerificacao02 = []

for chave in chavesBin:
    
    Contador_Chave = []
    Contador = []
    Nibble = ''
    Nibble_Chave = {}          
    Total_Nibble_Chave = []
    i = 0
    
    for Valor in chave:
        if i == 4:
            Contador.append(Nibble)
            i = 0
            Nibble = ''
        Nibble = Nibble + Valor
        i = i + 1
        
    Contador_Chave.append(Contador)
    Contador = []
    Contador_Chave = pd.DataFrame(Contador_Chave)
    
    Nibbles = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111',]
    
    for chave in Contador_Chave.values:           
        for Nibble in Nibbles:
            c = Counter(chave)
            Nibble_Chave[Nibble] = c[Nibble]
        Total_Nibble_Chave.append(Nibble_Chave)
        Nibble_Chave = {}
        
    Total_Nibble_Chave = pd.DataFrame(Total_Nibble_Chave)
    Soma_Chaves = []
    Acumulado = 0
    Conta = 0

    for chave in Total_Nibble_Chave.values:
        for Valor in chave:
            Acumulado = Acumulado + Valor * Valor
        Conta = (16/5000) * Acumulado - 5000
        Soma_Chaves.append(Conta)
        Conta = 0
        Acumulado = 0
        
    Soma_Chaves = pd.DataFrame(Soma_Chaves)
    Verificacao = 0
    
    for chave in Soma_Chaves.values:
        if chave > 1.03 and chave < 57.4:
            Verificacao = Verificacao + 1
    
    if(Verificacao == 0):
        resultadoVerificacao02.append("False")
    else:
        resultadoVerificacao02.append("True")
        
print(resultadoVerificacao02)

#Verificação 03 Runs Test

resultadoVerificacao03 = []
vet01 = []
vet02 = []

for i in range(20):
    
    count01_0 = 0
    count02_0 = 0
    count03_0 = 0
    count04_0 = 0
    count05_0 = 0
    count06_0 = 0
    count01_1 = 0
    count02_1 = 0
    count03_1 = 0
    count04_1 = 0
    count05_1 = 0
    count06_1 = 0

    vet01 = chavesBin[i].split('1')
    vet02 = chavesBin[i].split('0')
    
    for j in range(len(vet01)):
        if vet01[j] != '':
            if len(vet01[j]) == 1:
                count01_0 = count01_0 + 1
            elif len(vet01[j]) == 2:
                count02_0 = count02_0 + 1
            elif len(vet01[j]) == 3:
                count03_0 = count03_0 + 1
            elif len(vet01[j]) == 4:
                count04_0 = count04_0 + 1
            elif len(vet01[j]) == 5:
                count05_0 = count05_0 + 1
            elif len(vet01[j]) >= 6:
                count06_0 = count06_0 + 1   
    for k in range(len(vet02)):
        if vet02[k] != '':
            if len(vet02[k]) == 1:
                count01_1 = count01_1 + 1
            elif len(vet02[k]) == 2:
                count02_1 = count02_1 + 1
            elif len(vet02[k]) == 3:
                count03_1 = count03_1 + 1
            elif len(vet02[k]) == 4:
                count04_1 = count04_1 + 1
            elif len(vet02[k]) == 5:
                count05_1 = count05_1 + 1
            elif len(vet02[k]) >= 6:
                count06_1 = count06_1 + 1
    
    if(count01_0 >= 2267 and count01_0 <= 2773 and count02_0 >= 1079 and count02_0 <= 1421 and count03_0 >= 502 and count03_0 <= 748 and count04_0 >= 223 and count04_0 <= 402 and count05_0 >= 90 and count05_0 <= 223 and count06_0 >= 90 and count06_0 <= 223):
        if(count01_1 >= 2267 and count01_1 <= 2773 and count02_1 >= 1079 and count02_1 <= 1421 and count03_1 >= 502 and count03_1 <= 748 and count04_1 >= 223 and count04_1 <= 402 and count05_1 >= 90 and count05_1 <= 223 and count06_1 >= 90 and count06_1 <= 223):
            resultadoVerificacao03.append("True")
    else:
        resultadoVerificacao03.append("False")
print(resultadoVerificacao03)

#Verificação 04 Long Run Test

resultadoVerificacao04 = []

for i in range(20):
    
    flag_0 = 0
    flag_1 = 0
    
    vet01 = chavesBin[i].split('1')
    vet02 = chavesBin[i].split('0')
    for j in range(len(vet01)):
        if len(vet01[j]) >= 34:
            flag_1 = 1
    for k in range(len(vet02)):
        if len(vet02[k]) >= 34:
            flag_0 = 1
    
    if flag_0 == 1 or flag_1 == 1:
        resultadoVerificacao04.append("False")
    else:
        resultadoVerificacao04.append("True")
print(resultadoVerificacao04)
