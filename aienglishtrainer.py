from aienglish import aienglish
import pickle
airunner=aienglish() # initalizing runner
airunner.preprocess() # formatting all the data and prepping for training
airunner.train() # training the model and outputting the accuracy
airunner.export()
# filename = 'finalized_model.sav'
# pickle.dump(airunner.clf, open(filename, 'wb'))
