import cv2
import numpy as np
import webbrowser
import pyautogui
import time
import os

def menu():
    escolha=100
    while(escolha!=0):
        print('\n\nMENU\n')
        print('1-Para adicionar créditos do RU')
        print('2-Para retirar créditos do RU')
        print('3-Para mostrar os créditos do RU')
        print('0-Sair')
        escolha = input('Digite sua escolha: ')
        escolha = int(escolha)
        if escolha==1:
            adicionar()
        if escolha==2:
            retirar()
        if escolha==3:
            exibir()

def adicionar():
    add=input("\nDigite quantos creditos adicionar: ")
    add=int(add)
    arq1 = open("auxmeu.txt",'r')
    arq2 = open("dados.txt",'r')
    codigo = arq1.readlines()
    listaDados = arq2.readlines()
    aux3=-1
    for dados in listaDados:
        aux3+=1
        if dados[:14] == codigo[0][:14]:
            aux4=int(dados[15])
            aux4+=add
            dados = dados[:15]+str(aux4)+dados[16:]
            listaDados[aux3]=dados
            break
    arq2.close()
    arq2=open("dados.txt",'w')
    arq2.writelines(listaDados)
    arq2.close()

def retirar():
    add=input("\nDigite quantos creditos retirar: ")
    add=int(add)
    arq1 = open("auxmeu.txt",'r')
    arq2 = open("dados.txt",'r')
    codigo = arq1.readlines()
    listaDados = arq2.readlines()
    aux3=-1
    for dados in listaDados:
        aux3+=1
        if dados[:14] == codigo[0][:14]:
            aux4=int(dados[15])
            aux4-=add
            if aux4<0:
                aux4=0
            dados = dados[:15]+str(aux4)+dados[16:]
            listaDados[aux3]=dados
            break
    arq2.close()
    arq2=open("dados.txt",'w')
    arq2.writelines(listaDados)
    arq2.close()

def exibir():
    arq1 = open("auxmeu.txt",'r')
    arq2 = open("dados.txt",'r')
    codigo = arq1.readlines()
    listaDados = arq2.readlines()
    aux3=-1
    for dados in listaDados:
        aux3+=1
        if dados[:14] == codigo[0][:14]:
            print("Voce tem "+dados[15]+" fichas")
    
def PeB(img,img2,vlr):
    tamY, tamX = img.shape
    for i in range(tamY):
        for j in range(tamX):
            pix0=img2[i,j][0]
            pix1=img2[i,j][1]
            pix2=img2[i,j][2]
            if img[i,j]<vlr:
                pix0=0
                pix1=0
                pix2=0
            else:
                pix0=255
                pix1=255
                pix2=255
            img2[i,j][0]=pix0
            img2[i,j][1]=pix1
            img2[i,j][2]=pix2
    return img2

webbrowser.open("https://web.whatsapp.com/")#abre aba do whatsapp

time.sleep(2)

abaWhatsSpace = pyautogui.locateOnScreen("abaWhats.png")#clica na aba do grupo
while(abaWhatsSpace is None):
    time.sleep(0.5)
    abaWhatsSpace = pyautogui.locateOnScreen("abaWhats.png")
pyautogui.click(abaWhatsSpace[0],abaWhatsSpace[1])

pyautogui.moveTo(2,2)

essaSpace = pyautogui.locateOnScreen("essa.png")#reconhece q tem foto
while(essaSpace is None):
    time.sleep(1)
    essaSpace = pyautogui.locateOnScreen("essa.png")

time.sleep(5)
pyautogui.rightClick(1050,500)
time.sleep(1)
pyautogui.click(1105,540)
time.sleep(1)
pyautogui.typewrite("barra.png")

nomeSpace = pyautogui.locateOnScreen("nome.png")#clica em salvar 
while(nomeSpace is None):
    time.sleep(0.3)
    nomeSpace = pyautogui.locateOnScreen("nome.png")
pyautogui.click(nomeSpace[0]+1,nomeSpace[1])
time.sleep(0.5)
pyautogui.press('left')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(3)
webbrowser.open("http://www.onlinebarcodereader.com/")#abre site de codigo de barras
vlr=20
while(vlr<40):
    sair=0
    vlr+=1
    img = cv2.imread('barra.png',0)#le a imagem em escala de cinza
    img2 = cv2.imread('barra.png',1)# le a mesma imagem colorida
    img3 = PeB(img,img2,vlr)
    cv2.imwrite('pretoEbranco.png',img3)#salva a img preto e branco

    escSpace = pyautogui.locateOnScreen("escolherArquivo.png")
    while(escSpace is None):#clico em escolher arquivo no site
        time.sleep(0.5)
        escSpace = pyautogui.locateOnScreen("escolherArquivo.png")
    pyautogui.click(escSpace[0],escSpace[1])

    time.sleep(1)
    pyautogui.click(390,50)
    pyautogui.typewrite("C:\\Users\\camil\\Desktop\\projeto esof final")
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.click(435,415)
    time.sleep(0.5)
    pyautogui.typewrite("pretoEbranco.png")

    abrirSpace = pyautogui.locateOnScreen("abrir.png")
    while(abrirSpace is None):
        time.sleep(0.5)
        abrirSpace = pyautogui.locateOnScreen("abrir.png")
    pyautogui.click(abrirSpace[0]+50,abrirSpace[1]+10)
    
    startSpace = pyautogui.locateOnScreen("start.png")
    while(startSpace is None):
        time.sleep(0.5)
        startSpace = pyautogui.locateOnScreen("start.png")
    pyautogui.moveTo(startSpace[0],startSpace[1])
    time.sleep(2)
    pyautogui.click()

    contentSpace = pyautogui.locateOnScreen("content.png")
    aux=0
    while(contentSpace is None and sair!=1):
        time.sleep(0.5)
        aux=aux+1
        contentSpace = pyautogui.locateOnScreen("content.png")
        if(aux>10):
            sair=1
            startSpace = None
            abrirSpace = None
            escSpace = None
            backSpace = pyautogui.locateOnScreen("back.png")
            while(backSpace is None):
                time.sleep(0.5)
                backSpace = pyautogui.locateOnScreen("back.png")
            pyautogui.click(backSpace[0],backSpace[1])
            time.sleep(3)

    if sair!=1:
        pyautogui.click(contentSpace[0]+20,contentSpace[1]+30)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl','a')#seleciona tudo
        time.sleep(0.5)
        pyautogui.hotkey('ctrl','c')
        pyautogui.hotkey('ctrl','c')#copia
        break
    
os.startfile(r'C:\Users\camil\Desktop\projeto esof final\auxmeu.txt')
time.sleep(2)
pyautogui.click(500,500)
pyautogui.hotkey('ctrl','a')#seleciona tudo
#pyautogui.press('delete')
pyautogui.hotkey('ctrl','v')#cola
pyautogui.hotkey('ctrl','s')#salva
time.sleep(0.5)
arqxSpace = pyautogui.locateOnScreen("Xarq.png")
while(arqxSpace is None):
    time.sleep(0.5)
    arqxSpace = pyautogui.locateOnScreen("Xarq.png")
pyautogui.click(arqxSpace[0]+90,arqxSpace[1]+3)

pyautogui.click(1360,5)

arq1 = open("auxmeu.txt",'r')
arq2 = open("dados.txt",'r')
codigo = arq1.readlines()
listaDados = arq2.readlines()
aux2=0
for dados in listaDados:
    if dados[:14] == codigo[0][:14]:
        aux2=1
        print("Ola "+dados[17:]+", voce tem "+dados[15]+" fichas, o que quer fazer?")
        menu()
if aux2==0:
    print("Nao encontramos este usuario")


















