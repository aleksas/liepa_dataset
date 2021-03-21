import requests

def download(url, dst_path=None):
    local_filename = url.split('/')[-1] if not dst_path else dst_path
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
                
    return local_filename