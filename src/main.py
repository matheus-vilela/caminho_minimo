import os
import time
import math

cwd = os.getcwd() 
files = os.listdir(cwd) 
print("Files in %r: %s" % (cwd, files))


arquivos = [ 
  'facebook_combined.txt',
  'toy.txt',
  'rg300_4730.txt',
  'rome99c.txt',
  'USA-road-dt.DC.txt',
]

class Caminho():
     origem = ''
     destino = ''
     peso = '' 

def menu():

  while(1):
    print('\n\n\n=======================================\n')
    print('\nDigite o numero do grafo que deseja: \n')
    print('1 - facebook_combined ')
    print('2 - toy ')
    print('3 - rg300_4730 ')
    print('4 - rome99c ')
    print('5 - USA-road-dt.DC ')
    index = int(input('\nOpção desejada: '))
    grafo = open(arquivos[index-1],'r')

    with grafo as arquivo:
      newGrafo = [numero.replace('\n', '') for numero in [linha for linha in arquivo.readlines()]]
      grafo = []


      for index in range(len(newGrafo)):
        if index > 0:
          grafo.append([
            int(newGrafo[index].split(' ')[0]),
            int(newGrafo[index].split(' ')[1]),
            int(newGrafo[index].split(' ')[2]),
            ]) 
        else:
          grafo.append([
            int(newGrafo[index].split(' ')[0]),
            int(newGrafo[index].split(' ')[1]),
            ])         

      while True:
        print('\n\n=======================================\n')
        print('\nDigite a opção desejada:')
        print('1 - Dijkstra')
        print('2 - BellmanFord ')
        print('3 - FloydWarshall ')
        print('\n4 - Voltar ao menu anterior ')
        codigo = int(input('\nOpção desejada: '))

        origem = -1
        destino = -1
        if(codigo == 1 or codigo == 2 or codigo == 3):
          while origem < 0 or origem > int(grafo[0][0]) - 1 or destino < 0 or destino > int(grafo[0][0]) - 1 or origem == destino:
            input1 = input('\nDigite a origem: ')
            input2 = input('Digite o destino: ')
            origem = int(input1 if input1 !=  '' else -1 )
            destino = int(input2 if input2 !=  '' else -1)
            if origem < 0 or origem > int(grafo[0][0]) - 1 or destino < 0 or destino > int(grafo[0][0]) - 1 or origem == destino:
              print('Origem ou destino inválido.')
              
          if codigo == 1:
            dijkstra(grafo, origem, destino)
            input('\n >>>> Aperte ENTER para continuar <<<<\n')
          elif codigo == 2:
            bellmanFord(grafo, origem, destino)
            input('\n >>>> Aperte ENTER para continuar <<<<\n')
          elif codigo == 3:
            floydWarshall(grafo, origem, destino)
            input('\n >>>> Aperte ENTER para continuar <<<<\n')
          elif codigo == 4:
            break
          else:
            print('Opcao inválida!!')
        elif codigo == 4:
          break
        else:
          print('Opcao inválida!!')

def dijkstra(arr, origem, destino):
  inicio = time.time()

  grafo = []
  for _ in arr:
    grafo.append(_)
    
  totalVertices = int(grafo[0][0])
  del(grafo[0])

  dist = []
  pred = []
  listaVertices = []
  dist.clear()
  pred.clear()

  for i in range(totalVertices):
    dist.append(math.inf)
    pred.append(None)
    listaVertices.append(i)

  dist[origem] = 0

  try:
    while len(listaVertices)  != 0:
      verticeMenorDistancia = None
      menorDistancia = math.inf

      for i in range(len(listaVertices)):
        if dist[listaVertices[i]] < menorDistancia:
          menorDistancia = dist[listaVertices[i]]
          verticeMenorDistancia = listaVertices[i]

      del(listaVertices[listaVertices.index(verticeMenorDistancia)])
      
      listaArestas = []
      for caminho in grafo:
        if caminho[0] == verticeMenorDistancia:
          listaArestas.append(caminho)

      for i in range(len(listaArestas)):
        destin = listaArestas[i][1]
        peso = listaArestas[i][2]

        if dist[destin] > dist[verticeMenorDistancia] + peso:
          dist[destin] = dist[verticeMenorDistancia] + peso
          pred[destin] = verticeMenorDistancia

    custo = dist[destino]

    percurso = []
    percurso.insert(0, destino)
    while percurso[0] != origem:
        percurso.insert(0, pred[percurso[0]])
    
    fim = time.time()
    executionTime = float(fim-inicio)
    print('\n\nRESUMO: \nCodigo: DIJKSTRA\nPercurso: ', percurso, '\nCusto total: ',custo, '\nTempo de execução: ', executionTime,'s')
  except Exception as erro:
    print("\n\nNão foi possivel encontrar o percurso\n\n")


def bellmanFord(arr, origem, destino):
    inicio = time.time()
    grafo = []
    for _ in arr:
      grafo.append(_)
      
    totalVertices = int(grafo[0][0])
    del(grafo[0])

    dist = []
    pred = []
    dist.clear()
    pred.clear()

    for i in range(totalVertices):
      dist.append(math.inf)
      pred.append(None)

    dist[origem] = 0

    for i in range(totalVertices):
      melhor = 0
      for j in range(len(grafo)):
        if dist[grafo[j][1]] > dist[grafo[j][0]] + grafo[j][2]:
           dist[grafo[j][1]] = dist[grafo[j][0]] + grafo[j][2]
           pred[grafo[j][1]] = grafo[j][0]
           melhor = 1
      
      if melhor == 0:
        break

    custo = dist[destino]

    percurso = []
    percurso.insert(0, destino)
    while percurso[0] != origem:
        percurso.insert(0, pred[percurso[0]])
    
    fim = time.time()
    executionTime = float(fim-inicio)
    print('\n\nRESUMO: \nCodigo: BELLMANFORD\nPercurso: ', percurso, '\nCusto total: ',custo, '\nTempo de execução: ', executionTime,'s')

def floydWarshall(arr, origem, destino):
  inicio = time.time()
  grafo = []
  for _ in arr:
    grafo.append(_)
    
  totalVertices = int(grafo[0][0])
  del(grafo[0])

  dist = []
  pred = []

  for _ in range(totalVertices):
    dist.append([None,None,None,None,None])
    pred.append([None,None,None,None,None])

  for i in range(totalVertices):
    for j in range(totalVertices):
      if i == j:
        dist[i][j] = 0
        pred[i][j] = None
      else:
        caminho = None
        for item in range(len(grafo)):
          if(grafo[item][0] == i and grafo[item][1] == j):
            caminho = item
      
        if caminho != None:
          dist[i][j] = grafo[item][2]
          pred[i][j] = i    
        else:
          dist[i][j] = math.inf
          pred[i][j] = None         

  for i in range(totalVertices):
    for j in range(totalVertices):
      for k in range(totalVertices):
        if dist[j][k] > dist[j][i] + dist[i][j]:
          dist[j][k] = dist[j][i] + dist[i][j]
          pred[j][k] = dist[i][j]


  custo = dist[origem][destino]

  percurso = []
  percurso.insert(0, destino)
  while percurso[0] != origem:
      percurso.insert(0, pred[origem][percurso[0]])
  
  fim = time.time()
  executionTime = float(fim-inicio)
  print('\n\nRESUMO: \nCodigo: FLOYDWARSHALL\nPercurso: ', percurso, '\nCusto total: ',custo, '\nTempo de execução: ', executionTime,'s')


menu()
