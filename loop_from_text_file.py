#!/usr/bin/env python3

import fire
import time
import torch
start_time = time.time()

import warnings
import random
from transformers import GPT2Tokenizer, GPT2LMHeadModel#, trainer_utils

device = "cuda"
torch.cuda.set_per_process_memory_fraction(0.3)

warnings.simplefilter("ignore")

def interact_model():
    tokenizer = GPT2Tokenizer.from_pretrained("./models/1558MPytorch/")
    model = GPT2LMHeadModel.from_pretrained("./models/1558MPytorch/").to(device)
   
    raw_text = open("test.txt", "r").read()
    input = raw_text
    n_samples = 5
    print (input,end='')

    for x in range(n_samples):
        # input sequence
        inputs = tokenizer(input, return_tensors="pt").to(device)
        
        # output
        outputs = model.generate(**inputs, num_beams=1, max_new_tokens=50, top_p=0.98, top_k=500, temperature=1.03, do_sample=True, pad_token_id=50256)
        print (tokenizer.decode(outputs[0], skip_special_tokens=False).replace(input,""),end='')
        input = tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == '__main__':
    fire.Fire(interact_model)

end_time = time.time()
print("" + str(end_time - start_time))
