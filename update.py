from os import path as ospath, environ, execl as osexecl
from subprocess import run as srun
from requests import get as rget
from dotenv import load_dotenv
from sys import executable

UPSTREAM_REPO = environ.get('UPSTREAM_REPO')
UPSTREAM_BRANCH = environ.get('UPSTREAM_BRANCH')
try:
    if len(UPSTREAM_REPO) == 0:
       raise TypeError
except:
    UPSTREAM_REPO = "https://github.com/adnansidd99/test-purpose"
try:
    if len(UPSTREAM_BRANCH) == 0:
       raise TypeError
except:
    UPSTREAM_BRANCH = 'code-patch1'

if ospath.exists('.git'):
    srun(["rm", "-rf", ".git"])

update = srun([f"git init -q \
                 && git config --global user.email asr3012003@gmail.com \
                 && git config --global user.name adnansidd99 \
                 && git add . \
                 && git commit -sm update -q \
                 && git remote add origin {UPSTREAM_REPO} \
                 && git fetch origin -q \
                 && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)
