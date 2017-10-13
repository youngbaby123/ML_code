#-*-coding:utf-8-*-
import numpy as np
from sklearn.svm import SVC


def img_pose_score(feature, model):
    score = model.predict_proba(feature)[:,0]
    score = max(score)
    return score
