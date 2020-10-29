import os
import pandas as pd
import xlwt
import lxml
from lxml import etree
from datetime import datetime
from xlwt import *
import xlsxwriter
import math
from os import listdir
import numpy as np
import sys


def generaExcel(carpeta, es, pixeles, unidad, nEsto,medAltura, medAnchura, desvAltura, desvAnchura, numEstoArea, AreaS, numEstoS, altAnch):
    wb = xlsxwriter.Workbook(carpeta+'/'+'stomata.xlsx')
    ws = wb.add_worksheet('Stomata')

    style0 = wb.add_format({'bold': True, 'font_color': 'white', 'fg_color': '0x10'})
    # style0.set_font_color('red')
    # -------------------------------------
    path = carpeta
    lstFiles = []
    lstDir = os.walk(path)  # os.walk()
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if (extension == ".xml"):
                lstFiles.append(nombreFichero + extension)
    i = 1
    col = 0
    lstFiles.sort()
    ws.write(0, 0, 'Image name', style0)
    ws.set_column(0, 0, 25)
    if nEsto == True:
        ws.write(0, 1, 'Number of stomata in total', style0)
        ws.set_column(0, 1, 20)
    else:
        col = col + 1
    if medAltura ==True:
        a = 2-col
        ws.write(0, a, 'Average height', style0)
        ws.set_column(0, 2, 20)
    else:
        col = col + 1
    if medAnchura == True:
        b = 3 - col
        ws.write(0, b, 'Average width', style0)
        ws.set_column(0, 3, 20)
    else:
        col = col + 1
    if desvAltura == True:
        c = 4 - col
        ws.write(0, c, 'Standard height deviation', style0)
        ws.set_column(0, 4, 20)
    else:
        col = col + 1
    if desvAnchura == True:
        d = 5 - col
        ws.write(0, d, 'Standard width deviation', style0)
        ws.set_column(0, 5, 20)
    else:
        col = col + 1
    if numEstoArea == True:
        e = 6-col
        ws.write(0, e, 'Number of surface stomata', style0)
        ws.set_column(0, 6, 20)
    else:
        col = col + 1
    if AreaS==True:
        f =7-col
        ws.write(0, f, 'Surface area ('+unidad+')', style0)
        ws.set_column(0, 7, 20)
    else:
        col = col + 1
    if numEstoS ==  True:
        g = 8 - col
        ws.write(0, g, 'Stomata per surface', style0)
        ws.set_column(0, 8, 20)
    else:
        col = col + 1
    escala = es / pixeles
    for fichero in lstFiles:
        numEstomas = 0
        numEstomasS = 0
        j = 0
        areaS = 0
        k = 0
        # alturaTotal = 0
        # anchuraTotal = 0
        listaAlturas = []
        listaAnchuras = []
        doc = etree.parse(carpeta+'/' + fichero)
        filename = doc.getroot()  # buscamos la raiz de nuestro xml
        nomImagen = filename.find("filename")
        # print(filename.text)  # primer elto del que obtenemos el título de nuestro video
        # ws.write(i, 0, nomImagen.text.split('\\')[len(nomImagen.text.split('/'))-1])
        ws.write(i, 0, nomImagen.text)
        objetos = filename.findall("object")
        while j < len(objetos):
            # ws.set_column(0,8, 10)
            superficie = 0
            if objetos[j].find("name").text == "superficie":
                superficie = 1
                ymaxS = float(objetos[j].find("bndbox").find("ymax").text)
                # print ('superficie'+ str(ymaxS))
                yminS = float(objetos[j].find("bndbox").find("ymin").text)
                xmaxS = float(objetos[j].find("bndbox").find("xmax").text)
                xminS = float(objetos[j].find("bndbox").find("xmin").text)
                areaS = escala * escala * (ymaxS - yminS) * (xmaxS - xminS)
                if AreaS == True:
                    ws.write(i, f, float(areaS))

                break
            j = j + 1

        j = 0
        while j < len(objetos):
            if objetos[j].find("name").text == "stoma":
                # stoma = objetos[j].find("name")
                numEstomas = numEstomas + 1
                ymax = float(objetos[j].find("bndbox").find("ymax").text)
                ymin = float(objetos[j].find("bndbox").find("ymin").text)
                xmax = float(objetos[j].find("bndbox").find("xmax").text)
                xmin = float(objetos[j].find("bndbox").find("xmin").text)
                if superficie != 0 and xminS < xmin and yminS < ymin and xmax < xmaxS and ymax < ymaxS:
                    alturaEstomaActual = (ymax - ymin) * escala
                    ws.write(0, 9 + 2 * k, 'Height' + str(k) + '('+unidad+')', style0)
                    ws.write(i, 9 + 2 * k, float('%.2f' % alturaEstomaActual))
                    listaAlturas.append(alturaEstomaActual)
                    anchuraEstomaActual = (xmax - xmin) * escala
                    ws.write(0, 9 + 2 * k + 1, 'Width' + str(k) + '('+unidad+')', style0)
                    ws.write(i, 9 + 2 * k + 1, float('%.2f' % anchuraEstomaActual))
                    listaAnchuras.append(anchuraEstomaActual)
                    numEstomasS = numEstomasS + 1
                    k = k + 1
                    if len(objetos) != 0:
                        if medAltura == True:
                            ws.write(i, a, float('%.2f' % (np.mean(listaAlturas))))
                        if medAnchura == True:
                            ws.write(i, b, float('%.2f' % (np.mean(listaAnchuras))))
                        if desvAltura == True:
                            ws.write(i, c, float('%.2f' % (np.std(listaAlturas))))
                        if desvAnchura == True:
                            ws.write(i, d, float('%.2f' % (np.std(listaAnchuras))))
                    else:
                        if medAltura == True:
                            ws.write(i, a, 0)
                        if medAnchura == True:
                            ws.write(i, b, 0)
                        if desvAltura == True:
                            ws.write(i, c, 0)
                        if desvAnchura == True:
                            ws.write(i, d, 0)
                        if numEstoS == True:
                            ws.write(i, e, 0)
                        if AreaS == True:
                            ws.write(i, f, 0)
                elif superficie == 0:
                    alturaEstomaActual = (ymax - ymin) * escala
                    ws.write(0, 6 + 2 * j, 'Altura' + str(j)+ '('+unidad+')', style0)
                    ws.write(i, 6 + 2 * j, float('%.2f' % alturaEstomaActual))
                    listaAlturas.append(alturaEstomaActual)
                    anchuraEstomaActual = (xmax - xmin) * escala
                    ws.write(0, 6 + 2 * j + 1, 'Anchura' + str(j)+ '('+unidad+')', style0)
                    ws.write(i, 6 + 2 * j + 1, float('%.2f' % anchuraEstomaActual))
                    listaAnchuras.append(anchuraEstomaActual)
                    #anchuraEstomaActual = (xmax - xmin) * escala
                    #ws.write(0, 6 + 2 * j + 1, 'Anchura' + str(j), style0)
                    #ws.write(i, 6 + 2 * j + 1, float('%.2f' % anchuraEstomaActual))
                    #ws.write(i, 1, len(listaAlturas))
                    if medAltura == True:
                        ws.write(i, a, float('%.2f' % (np.mean(listaAlturas))))
                    if medAnchura == True:
                        ws.write(i, b, float('%.2f' % (np.mean(listaAnchuras))))
                    if desvAltura == True:
                        ws.write(i, c, float('%.2f' % (np.std(listaAlturas))))
                    if desvAnchura == True:
                        ws.write(i, d, float('%.2f' % (np.std(listaAnchuras))))
            j = j + 1
        if superficie == 1:
            if numEstoArea == True:
                ws.write(i, g, float((numEstomasS / areaS)))
            if numEstoS == True:
                ws.write(i, e, numEstomasS)
        if nEsto == True:
            ws.write(i, 1, numEstomas)
        #else:
            #col = col +1

        i = i + 1
    wb.close()
    # wb.save('UsueEstomas.xlsx')