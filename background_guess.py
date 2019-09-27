import sys  # System bindings
import cv2  # OpenCV bindings
import numpy as np
from collections import Counter
from sklearn.cluster import KMeans
def get_color(img,data):
    #return np.array([255,255,255,255]).astype(np.uint8)
    n_boxes = len(data['level'])
    mask = np.full((img.shape[0], img.shape[1]), True, dtype=np.uint8)
    for i in range(n_boxes):
        if(data['text'][i]!=''):
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            cv2.rectangle(mask, (x, y), (x + w, y + h), False, cv2.FILLED)
    clt = KMeans(n_clusters=4)
    img2=img.reshape(-1, 4)
    mask= mask.reshape(-1,1)
    clt.fit([ i for(i,m) in zip(img2,mask) if m])
    #mask2 = np.full((img.shape[0], img.shape[1],4), clt.cluster_centers_[0].astype(np.uint8), dtype=np.uint8)
    return clt.cluster_centers_[0].astype(np.uint8)