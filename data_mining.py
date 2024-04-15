from config import DATASET_PATH, REPO, GITHUB_TOKEN
from utils import crawl_github_repo

repo_collection = []
for repo in REPO:
    print(f"Extracting Data: {repo}")
    try:
        data_repo = crawl_github_repo(repo, False, GITHUB_TOKEN)
        repo_collection.extend(data_repo)
    except Exception as e: 
        print(f"Data Extraction Failed:{repo}")

with open(DATASET_PATH,'w') as f: 
    for item in repo_collection:
        f.write(item + "\n")
        
        
                