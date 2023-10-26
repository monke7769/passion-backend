from ai import ai
airunner=ai('data.csv') # initalizing runner
airunner.preprocess() # formatting all the data and prepping for training
airunner.evalulate() # training the model and outputting the accuracy