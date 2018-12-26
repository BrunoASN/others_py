def criar_matriz(num_linha, num_colunas):
    matriz=[]
    for i in range(num_linha):
        linha=[]
        for j in range(num_colunas):
            valor = int(input())
        matriz.append(linha)
    return matriz

def le_matriz():
    lin=int(input())
    col=int(input())
    return criar_matriz(lin,col)
    
