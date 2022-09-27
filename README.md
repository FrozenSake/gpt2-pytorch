# Attribution

This is partially cobbled together from multiple sources on the web, but mostly a sort of frankenstein to get https://github.com/openai/gpt-2 working on more modern video cards.

# Setup


! Unclear if these are needed for this one, I had done them previously to my attempt !
[ ] Install cuda <some version>
[ ] Install cudnn for cuda version you installed
! End unclear section !

[ ] Install Anaconda or Miniconda
[ ] Clone this Repo to some directory
[ ] Open Anaconda's Terminal
[ ] Navigate to where you cloned this folder
[ ] conda create -n gpt2-pytorch python=3.9
[ ] conda activate gpt2-pytorch
[ ] conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
[ ] conda install -c huggingface transformers
[ ] mkdir models/1558MPytorch
[ ] Download: config.json, tokenizer.json, vocab.json, pytorch_model.bin, merges.txt || from: https://huggingface.co/gpt2-xl/tree/main || to: models/1558MPytorch
[ ] Optional: change the `test.txt` file to have a different prompt
[ ] `python ./from_text_file.py`
