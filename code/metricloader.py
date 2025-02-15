from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from utils import utils
import os
import numpy as np
import pickle

dir_path = os.path.dirname(os.path.realpath(__file__))
#set experiment and model
experiments= ['exp1.1.1']
models = ['fastai_xresnet1d101','random_forest']
for model in models:
    for experiment in experiments:
        base_fp = os.path.join(dir_path,'../output/' + experiment)


        actual_file = os.path.join(base_fp, 'data/y_test.npy')
        predicted_file = os.path.join(base_fp, 'models/' + model + '/y_test_pred.npy')


        y_true = np.load(actual_file, allow_pickle=True)
        y_pred = np.load(predicted_file, allow_pickle=True)
        #apply thresholds to data, converting probabilities tobinary 
        y_pred = utils.apply_thresholds(y_pred, thresholds=utils.find_optimal_cutoff_thresholds(y_true, y_pred))
        #compute accuracy
        accuracy = accuracy_score(y_true, y_pred)
        print(f"Model: {model}, Exp: {experiment}, accuracy:{accuracy}")
        #compute [precision]
        precision = precision_score(y_true, y_pred,average='weighted')
        print("Precision:", precision)

        # Compute recall
        recall = recall_score(y_true, y_pred,average='weighted')
        print("Recall:", recall)

        # Compute F1 score
        f1 = f1_score(y_true, y_pred,average='weighted')
        print("F1 Score:", f1)
