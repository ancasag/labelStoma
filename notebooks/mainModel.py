import notebooks.testTimeAugmentation
import sys
try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    # needed for py3+qt4
    # Ref:
    # http://pyqt.sourceforge.net/Docs/PyQt4/incompatible_apis.html
    # http://stackoverflow.com/questions/21217399/pyqt4-qtcore-qvariant-object-instead-of-a-string
    if sys.version_info.major >= 3:
        import sip
        sip.setapi('QVariant', 2)
    #from PyQt4.QtGui import *
    #from PyQt4.QtCore import *

from libs.utils import *
from libs.ustr import ustr
from os import listdir
import glob

listaModels=[]
def selectTecniques(self, avg, bila,blur,chanhsv,chanlab,crop,drop,elas,histo,vflip,hflip,hvflip,gamma,blurGa,gaunoise,
                    invert,median, none, raiseB, raiseGreen, raiseHue, raisered, raisesatu, raiseval,resize, rot10,
                    rot90, rot180, rot270, saltpe, sharpen, sift, shear, trans):
    listaModels=[]
    if avg == True:
        listaModels.append("avgBlur")
    if bila == True:
        listaModels.append("bilaBlur")
    if blur == True:
        listaModels.append("blur")
    if chanhsv == True:
        listaModels.append("chanHsv")
    if chanlab == True:
        listaModels.append("chanLab")
    if crop == True:
        listaModels.append("crop")
    if drop == True:
        listaModels.append("dropOut")
    if elas == True:
        listaModels.append("elastic")
    if histo == True:
        listaModels.append("histo")
    if vflip == True:
        listaModels.append("vflip")
    if hflip == True:
        listaModels.append("hflip")
    if hvflip == True:
        listaModels.append("hvflip")
    if gamma == True:
        listaModels.append("gamma")
    if blurGa == True:
        listaModels.append("blurGau")
    if gaunoise == True:
        listaModels.append("avgNoise")
    if invert == True:
        listaModels.append("invert")
    if median == True:
        listaModels.append("medianblur")
    if none == True:
        listaModels.append("none")
    if raiseB == True:
        listaModels.append("raiseBlue")
    if raiseGreen == True:
        listaModels.append("raiseGreen")
    if raiseHue == True:
        listaModels.append("raiseHue")
    if raisered == True:
        listaModels.append("raiseRed")
    if raisesatu == True:
        listaModels.append("raiseSatu")
    if raiseval == True:
        listaModels.append("raiseValue")
    if resize == True:
        listaModels.append("resize")
    if rot10 == True:
        listaModels.append("rotation10")
    if rot90 == True:
        listaModels.append("rotation90")
    if rot180 == True:
        listaModels.append("rotation180")
    if rot270 == True:
        listaModels.append("rotation270")
    if saltpe == True:
        listaModels.append("saltPeper")
    if sharpen == True:
        listaModels.append("sharpen")
    if sift == True:
        listaModels.append("shiftChannel")
    if shear == True:
        listaModels.append("shearing")
    if trans == True:
        listaModels.append("translation")
    return listaModels


def selectModel(self,rb_1):
    model = None
    #pesos = False
    #comprobamos cual es la red que se ha elegido
    targetDirPath = ustr(QFileDialog.getExistingDirectory(self, 'Select the directory of the weights', '',
                                                          QFileDialog.ShowDirsOnly ))
    if rb_1 == True:
        #se ha elegido la red YOLO por lo que necesitamos tres ficheros de configuracion
        listFich = listdir(targetDirPath)
        if len(listFich) == 3:
            fichWeights = glob.glob(targetDirPath+'/*.weights', recursive=False)
            fichNames = glob.glob(targetDirPath+'/*.names', recursive=False)
            fichCfg = glob.glob(targetDirPath+'/*.cfg', recursive=False)
            if (len(fichWeights)==1 and len(fichNames)==1 and len(fichCfg)==1 ):
                model = yoloDarknet = notebooks.testTimeAugmentation.DarknetYoloPred(fichWeights[0], fichNames[0],fichCfg[0])
                #pesos = True
            else:
                QMessageBox.about(self, "Error", 'The files are not correct. You need this files: .weight, .names and .cfg.')
            #path = os.path.dirname(ustr(self.filePath)) if self.filePath else '.'
            #yoloDarknet.predict(path,path)

        else:
            QMessageBox.about(self, "Error", 'This directory does not contain three files.')

    return model

def selectOption(aff, con, una):
    if aff == True:
        option = 'affirmative'
    elif con == True:
        option = 'consensus'
    elif una == True:
        option = 'unanimous'
    return option
