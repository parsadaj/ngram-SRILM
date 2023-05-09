import json
import numpy as np
import os
from pp_utils import *

HW_path = '/Users/parsa/Daneshgah/Arshad/2/NLP/Homeworks/HW1'

pure_data_path = os.path.join(HW_path, 'data/result.json')
pure_data = open_json(pure_data_path)['messages']

train_path = os.path.join(HW_path, 'data/final_train.txt')
test_path = os.path.join(HW_path, 'data/final_test.txt')

train_count = 0
test_count = 0
for message in pure_data:
    text = get_text(message)
    if text != False:
        text = manual_correction(text)

        choice = np.random.choice(['train', 'test'], p=[10/11,1/11])
        
        command = 'append_to_file(text, {choice}_path)\n{choice}_count += 1'.format(choice=choice)
        exec(command)


print(train_count, test_count)

pass
