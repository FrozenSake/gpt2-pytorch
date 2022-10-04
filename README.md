# Attribution

This is partially cobbled together from multiple sources on the web, but mostly a sort of frankenstein to get https://github.com/openai/gpt-2 working on more modern video cards.

# Setup


! Unclear if these are needed for this one, I had done them previously to my attempt !


- [ ] Install cuda, 11.2 worked for my card
- [ ] Install cudnn for cuda version you installed


! End unclear section !


- [ ] Install Anaconda or Miniconda
- [ ] Clone this Repo to some directory
- [ ] Open Anaconda's Terminal
- [ ] Navigate to where you cloned this folder
- [ ] conda create -n gpt2-pytorch python=3.9
- [ ] conda activate gpt2-pytorch
- [ ] conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
- [ ] conda install -c huggingface transformers
- [ ] `pip install -r requirements.txt`
- [ ] mkdir models/1558MPytorch
- [ ] Download: config.json, tokenizer.json, vocab.json, pytorch_model.bin, merges.txt || from: https://huggingface.co/gpt2-xl/tree/main || to: models/1558MPytorch
- [ ] Optional: change the `test.txt` file to have a different prompt
- [ ] `python ./from_text_file.py`

# Changing up functionality 

The main line which determins how your results will be have is this one:
```
 outputs = model.generate(**inputs, max_new_tokens=50, top_p=0.98, top_k=500, temperature=1.03, do_sample=True,
                             pad_token_id=50256)  # pad_token_id taken from what the warning said it was setting it to
```

The `max_new_tokens` setting is a good lever to pull for longer or shorter results, while `top_p, top_k, temperature` can be fiddled with for some measure of control over the randomness or cohesion of the results. `do_sample` can be flipped to false, which will enable greedy mode, and generally result in the highest probability tokens all the time.

Similarly one can use `loop_from_text_file.py` which will take the output from one run and feed it back into itself, this generally provides more enjoyable and consistent length long-form output than simply increasing the `max_new_tokens`.
