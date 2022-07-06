from os import path as ospath, environ, execl as osexecl
from subprocess import run as srun
from requests import get as rget
from dotenv import load_dotenv
from sys import executable

# CONFIG_FILE_URL = environ.get('CONFIG_FILE_URL')
# try:
#     if len(CONFIG_FILE_URL) == 0:
#         raise TypeError
#     try:
#         res = rget(CONFIG_FILE_URL)
#         if res.status_code == 200:
#             with open('config.env', 'wb+') as f:
#                 f.write(res.content)
#         else:
#             pass
#     except:
#         pass
# except:
#     pass

# load_dotenv('config.env', override=True)

UPSTREAM_REPO = environ.get('UPSTREAM_REPO')
UPSTREAM_BRANCH = environ.get('UPSTREAM_BRANCH')
try:
    if len(UPSTREAM_REPO) == 0:
       raise TypeError
except:
    UPSTREAM_REPO = "https://github.com/adnansid99/Sid-Tor-Api"
try:
    if len(UPSTREAM_BRANCH) == 0:
       raise TypeError
except:
    UPSTREAM_BRANCH = 'main'

if ospath.exists('.git'):
    srun(["rm", "-rf", ".git"])

update = srun([f"git init -q \
                 && git config --global user.email asr3012003@gmail.com \
                 && git config --global user.name adnansid99 \
                 && git add . \
                 && git commit -sm update -q \
                 && git remote add origin {UPSTREAM_REPO} \
                 && git fetch origin -q \
                 && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)
