# ml_project

# software and account requirements.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [Git cli](https://git-scm.com/downloads)
5. [Git Documentation](https://git-scm.com/docs/gittutorial)

## creating conda environment
```
conda create -p venv python==3.7 -y
```
## Activating conda environment
```
conda activate venv/
```
or
```
conda activate venv
```
## To install all the dependencies in requirements
```
pip install -r requirements.txt
```
## To add/stack file in git
for all file
```
git add .  
```
for specific file
```
git add <file name> --for specific file
```
## To check git status
```
git status
```
## To check all version maintained by git
```
git log
```
## To create version/commit all changes to git
```
git commit -m "message"
```
To send version change to github
```
git push origin main
```
To check remote url
```
git remote -v
```
# To setup CI/CD pipeline in heroku
3 requirements
1. HEROKU_EMAIL = <"Your Email ID">
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ML-P

## Build Docker Image
```
docker build -t <image_name>:<tagname>
```
> Note: image name of docker must be lower case

To list Docker Image
```
docker images
```
Run Docker Image
```
docker run -p 5000:5000 -e PORT=5000 <Image ID>
```
To check running container in docker
```
docker ps
```
To Stop Docker Container
```
docker stop <container_id>
python setup.py install
```
Install ipykernel
```
pip install ipykernel
```
Data Drift: When your dataset stats change we call it data drift