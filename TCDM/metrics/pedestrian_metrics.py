import time

import numpy as np
from easydict import EasyDict
import torch
from sklearn.metrics import mean_squared_error,mean_absolute_error


def generate_predatrrlist(gt_label, pred_label):
    pred_attlabel = []
    for row1, row2 in zip(gt_label, pred_label):
        row_temp = []
        for value1, value2 in zip(row1, row2):
            if (value2 == False) and (value1 == 0.0):
                row_temp.append(1)
            elif (value2 == True) and (value1 == 0.0):
                row_temp.append(0)
            elif (value2 == False) and (value1 == 1.0):
                row_temp.append(0)
            elif (value2 == True) and (value1 == 1.0):
                row_temp.append(1)
        pred_attlabel.append(row_temp)
    return np.array(pred_attlabel)


def generate_score(list):

    score_list = []
    nevattrid_list = [5,6,9,11,13,18,20]
    posattrid_list = [4,7,9,10,13,17,19]
    for row_num, row in enumerate(list):
        valuesis1_list=[]
        for idx, value in enumerate(row):
            if value == 1.0:
                valuesis1_list.append(idx)

        nev_score = sum(2 for x in valuesis1_list if x in nevattrid_list)
        pos_score = sum(2 for x in valuesis1_list if x in posattrid_list)
        sample_score = 10 - nev_score + pos_score
        score_list.insert(row_num,sample_score)
    return score_list





def get_pedestrian_metrics(gt_label, preds_probs, threshold=0.8, index=None, cfg=None):
    """
    index: evaluated label index
    """
    pred_label = preds_probs > threshold

    eps = 1e-20
    result = EasyDict()

    # SCORE
    pred_attrlabel = generate_predatrrlist(gt_label, pred_label)  
    true_scores = np.array(generate_score(gt_label))
    pred_scores =  np.array(generate_score(pred_attrlabel))
    print("true_scores:", true_scores)
    print("pred_scores:", pred_scores)
    mae=mean_absolute_error(pred_scores,true_scores)
    rmse=np.sqrt(mse)
    result.mae = mae
    result.rmse = rmse

    if index is not None:
        pred_label = pred_label[:, index]
        gt_label = gt_label[:, index]

    return result
