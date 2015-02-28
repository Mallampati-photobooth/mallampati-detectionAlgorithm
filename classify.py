#!/usr/bin/env python

import numpy as np
import random, os

def classify(filepath):
    # define required data
    MP_SCORES = [1, 2, 3, 4]    
    image_data = np.load(filepath)
    
    # classification algorithm
    mp_score = random.choice(MP_SCORES)  
    
    return mp_score
    
if __name__ == '__main__':
    print(classify('./source_test_files/mallampati.npy',
                     './source_test_files',
                     'mallampati.npy'))
                     