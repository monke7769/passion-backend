from ai import ai
import pickle
airunner=ai('data.csv') # initalizing runner
airunner.preprocess() # formatting all the data and prepping for training
airunner.train() # training the model and outputting the accuracy
airunner.export()
airunner.evaluate()
# filename = 'finalized_model.sav'
# pickle.dump(airunner.clf, open(filename, 'wb'))
