from clodsa.augmentors.augmentorFactory import createAugmentor
from clodsa.transformers.transformerFactory import transformerGenerator
from clodsa.techniques.techniqueFactory import createTechnique

# Para clasificacion 
augmentor = createAugmentor("classification","folders","folders","linear","images/",{"outputPath":"flip/"})
transformer = transformerGenerator("classification")
vFlip = createTechnique("flip",{"flip":0})
augmentor.addTransformer(transformer(vFlip))
augmentor.applyAugmentation()

# Para detección
augmentor = createAugmentor("detection","pascalvoc","pascalvoc","linear","images/",{"outputPath":"flip/"})
transformer = transformerGenerator("classification")
vFlip = createTechnique("flip",{"flip":0})
augmentor.addTransformer(transformer(vFlip))
augmentor.applyAugmentation()