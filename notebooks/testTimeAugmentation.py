import abc
from abc import ABC

#abstract class
class IPredictor(ABC):
    #constructor
    def __init__(self, weightPath):
        self.pathPesos = weightPath

    @abc.abstractmethod
    def predict(self,imgPath):
        pass

#heritage
class DarknetYoloPred(IPredictor):
    
    def __init__(self,weightPath,fichNames, fichCfg):
        IPredictor.__init__(self, weightPath)
        self.fichNames = fichNames
        self.fichCfg = fichCfg

    def predict(self, imgPath, output, conf):
        import predict.detect
        predict.detect.mainDataset(imgPath, output, conf, self.pathPesos, self.fichNames, self.fichCfg)


class MXnetYoloPred(IPredictor):

    def __init__(self,weightPath,classes):
        IPredictor.__init__(self, weightPath)
        self.classes=classes

    def predict(self, imgPath, output, conf):
        import predict.predict_batch
        predict.predict_batch.mainDataset(imgPath, output, conf,'yolo3_darknet53_custom', self.pathPesos, self.classes)

class MXnetSSD512Pred(IPredictor):

    def __init__(self,weightPath,classes):
        IPredictor.__init__(self, weightPath)
        self.classes=classes

    def predict(self, imgPath, output, conf):
        import predict.predict_batch
        predict.predict_batch.mainDataset(imgPath, output, conf,'ssd_512_resnet50_v1_custom',self.pathPesos, self.classes)

class MXnetFasterRCNNPred(IPredictor):
    
    def __init__(self,weightPath,classes):
        IPredictor.__init__(self, weightPath)
        self.classes=classes

    def predict(self, imgPath, output, conf):
        import predict.predict_batch
        predict.predict_batch.mainDataset(imgPath, output, conf,'faster_rcnn_resnet50_v1b_custom', self.pathPesos, self.classes)

class RetinaNetResnet50Pred(IPredictor):
    
    def __init__(self,weightPath,classes):
        IPredictor.__init__(self, weightPath)
        self.classes=classes

    def predict(self, imgPath, output, conf):
        import predict.predict_batch_retinanet
        predict.predict_batch_retinanet.mainDataset(imgPath, output, conf,'resnet50_v1', self.pathPesos, self.classes)

class MaskRCNNPred(IPredictor):
    
    def __init__(self,weightPath,classes):
        IPredictor.__init__(self, weightPath)
        self.classes=classes

    def predict(self, imgPath, output, conf):
        import predict.predict_batch_rcnn
        predict.predict_batch_rcnn.mainDataset(imgPath, output, conf, self.pathPesos, self.classes)


class Efficient(IPredictor):

    def __init__(self, weightPath, classes):
        IPredictor.__init__(self, weightPath)
        self.classes = classes

    def predict(self, imgPath, output, conf):
        import predict.predict_batch_efficient
        predict.predict_batch_efficient.mainDataset(imgPath, output, conf, self.pathPesos, self.classes)

class FSAF(IPredictor):

    def __init__(self, weightPath, classes):
        IPredictor.__init__(self, weightPath)
        self.classes = classes

    def predict(self, imgPath, output, conf):
        import predict.predict_batch_FSAF
        predict.predict_batch_FSAF.mainDataset(imgPath, output, conf, self.pathPesos, self.classes)

class FCOS(IPredictor):

    def __init__(self, weightPath, classes):
        IPredictor.__init__(self, weightPath)
        self.classes = classes

    def predict(self, imgPath, output, conf):
        import predict.predict_batch_FCOS
        predict.predict_batch_FCOS.mainDataset(imgPath, output, conf, self.pathPesos, self.classes)