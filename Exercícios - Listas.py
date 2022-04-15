#Separe uma lista de números em grupos de 9 characteres e escreva esses grupos sequencialmente separados por um ponto.

string = "0123657801282731931381738717318937137199647164146198138127316471641819"
cutPosition = 10
pieces = [string[i:i + cutPosition] for i in range(0,len(string),cutPosition)]
result = '.'.join(pieces)
print(result)
