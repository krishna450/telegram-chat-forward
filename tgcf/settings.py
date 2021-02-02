from dotenv import load_dotenv
import os
import logging
import dotenv
from github import Github
load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
STRING_SESSION = os.getenv('STRING_SESSION')
GITHUB_GIST_ID = os.getenv('GITHUB_GIST_ID')
GITHUB_TOKEN = os.getenv('GITHUB_GIST_TOKEN')


gh = Github(GITHUB_TOKEN)

assert API_ID and API_HASH



def get_config():
    if not GITHUB_GIST_ID:
        with open('config.yml') as file:
            CONFIG_STRING = file.read()
    else:
        gist = gh.get_gist(GITHUB_GIST_ID)









def update_config(config):
    if not GITHUB_GIST_ID:
        with open('config.yml','w') as file:
            file.write(config)
    else:
        gist = gh.get_gist(GITHUB_GIST_ID)
        gist.edit()






# if __name__ == "__main__":
#     # testing
#     for forward in forwards:
#         print(forward, get_forward(forward))
