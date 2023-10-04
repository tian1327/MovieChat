from huggingface_hub import snapshot_download

snapshot_download(repo_id="huggyllama/llama-7b", local_dir='./ckpt/LLaMA/7B_hf', cache_dir='.cache/huggingface_hub')