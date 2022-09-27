#!/usr/bin/env python3

from transformers import GPT2Tokenizer, GPT2LMHeadModel, trainer_utils
import warnings
import fire
import time
start_time = time.time()


warnings.simplefilter("ignore")


def interact_model():
    tokenizer = GPT2Tokenizer.from_pretrained("./models/1558MPytorch/")
    model = GPT2LMHeadModel.from_pretrained("./models/1558MPytorch/")
    # trainer_utils.set_seed(42069)

    # input sequence
    raw_text = open("test.txt", "r").read()
    inputs = tokenizer(raw_text, return_tensors="pt")

    # output
    outputs = model.generate(**inputs, max_new_tokens=50, top_p=0.98, top_k=500, temperature=1.03, do_sample=True,
                             pad_token_id=50256)  # pad_token_id taken from what the warning said it was setting it to
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))


if __name__ == '__main__':
    fire.Fire(interact_model)

end_time = time.time()
print("" + str(end_time - start_time))
