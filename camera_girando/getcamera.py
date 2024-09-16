from camera_girando import *
import numpy as np
import itertools
import math

# Instalar a biblioteca cv2 pode ser um pouco demorado. Não deixe para ultima hora!
import cv2 as cv

def criar_indices(min_i, max_i, min_j, max_j):
  L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
  idx_i = np.array([e[0] for e in L])
  idx_j = np.array([e[1] for e in L])
  idx = np.vstack( (idx_i, idx_j) )
  return idx

def matrixt(angulo=0, x=0, y=0, cis=0):     # matrix transformacao
  if angulo == 0 and x == 0 and y == 0 and cis == 0:
    return np.identity(3)
  angulo = np.radians(angulo)
  cos = math.cos(angulo)
  sen = math.sin(angulo)
  width = 320
  height = 240
  t = np.array([
    [cos, -sen, y],
    [sen,  cos, x],
    [0,    0,   1]
  ])
  zero = np.array([
    [1, 0, -(height//2)],
    [0, 1,  -(width//2)],
    [0, 0,            1]
  ])
  normaliza = np.array([
    [1, 0, height//2],
    [0, 1,  width//2],
    [0, 0,         1]
  ])
  cisalhamento = np.array([
    [1,   0,   0],
    [cis, 1,   0],
    [0,   0,   1]
    ])
  matrix = normaliza @ cisalhamento @ t @ zero
  return matrix

def transforma(idx, t):
  transformada = np.linalg.inv(t) @ idx
  transformada = np.round(transformada).astype(int)
  return transformada

def camera():
  # Essa função abre a câmera. Depois desta linha, a luz de câmera (se seu computador tiver) deve ligar.
  cap = cv.VideoCapture(0)

  # Aqui, defino a largura e a altura da imagem com a qual quero trabalhar.
  # Dica: imagens menores precisam de menos processamento!!!
  width = 320
  height = 240

  # Talvez o programa não consiga abrir a câmera. Verifique se há outros dispositivos acessando sua câmera!
  if not cap.isOpened():
    print("Não consegui abrir a câmera!")
    exit()

  # constantes 
  angulo = 0
  x = 0
  y = 0
  cisalhamento = 0
  direcao = ''

  # Esse loop é igual a um loop de jogo: ele encerra quando apertamos '1' no teclado.
  while True:
    # Captura um frame da câmera
    ret, frame = cap.read()

    # A variável `ret` indica se conseguimos capturar um frame
    if not ret:
      print("Não consegui capturar frame!")
      break

    # Mudo o tamanho do meu frame para reduzir o processamento necessário
    # nas próximas etapas
    frame = cv.resize(frame, (width,height), interpolation =cv.INTER_AREA)

    idx = criar_indices(0, width, 0, height)
    idx = np.vstack((idx, np.ones(idx.shape[1])))

    if direcao == '':
      angulo = 0
    if direcao == 'esq':
      angulo += 0.4
    if direcao == 'dir':
      angulo -= 0.4
  
    t = matrixt(angulo, x, y, cisalhamento)

    idx_t = transforma(idx, t)

    idx = np.linalg.inv(t) @ idx_t
    
    idx = idx[:2, :].astype(int) # deixa so as 2 primeira linha
    idx_t = idx_t[:2, :].astype(int)  # deixa so as 2 primeira linha

    # A variável image é um np.array com shape=(width, height, colors)
    image = np.array(frame).astype(float)/255
    image_ = np.zeros_like(image)

    idx_t[0,:] = np.clip(idx_t[0,:], 0, image_.shape[0] - 1)
    idx_t[1,:] = np.clip(idx_t[1,:], 0, image_.shape[1] - 1)

    outofbound = (idx[0, :] < image.shape[0]) & (idx[1, :] < image.shape[1]) & (idx[0, :] >= 0) & (idx[1, :] >= 0)

    idx = idx[:, outofbound]
    idx_t = idx_t[:, outofbound]

    image_[idx[0,:], idx[1,:], :] = image[idx_t[0,:], idx_t[1,:], :] 

    # Agora, mostrar a imagem na tela!
    cv.imshow('', image_)
    
    # Se aperto 'q', encerro o loop
    key = cv.waitKey(10)
    if key == ord('w'):
      y += 5
    if key == ord('s'):
      y -= 5
    if key == ord('a'):
      x += 5
    if key == ord('d'):
      x -= 5
    if key == ord('q'):
      direcao = 'esq'
    if key == ord('e'):
      direcao = 'dir'
    if key == ord('z'):
      cisalhamento -= 0.05
    if key == ord('x'):
      cisalhamento += 0.05
    if key == ord(' '):
      angulo = 0
      x = 0
      y = 0
      cisalhamento = 0
      direcao = ''
    if key == ord('1'):
      break


  # Ao sair do loop, vamos devolver cuidadosamente os recursos ao sistema!
  cap.release()
  cv.destroyAllWindows()

