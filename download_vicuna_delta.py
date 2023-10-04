from huggingface_hub import snapshot_download

snapshot_download(repo_id="lmsys/vicuna-7b-delta-v0", local_dir='./ckpt/Vicuna/vicuna-7b-delta-v0', cache_dir='.cache/huggingface_hub')