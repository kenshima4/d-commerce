## Steps to run

### Activate Python Virtual Environment
1. From d-commerce root in terminal  
- ```python -m venv venv``` (windows)  
- ```python3 -m venv venv``` (mac)  
- ```pip install -r requirements.txt```  

### Clone Git Repo
1. Clone Repo:  
```git clone git@github.com:kenshima4/d-commerce.git```

### Run App
1. Run Python server (in one terminal):
- ```cd backend```
- ```python manage.py runserver```
2. Run Vue server (in another terminal):
- ```cd frontend```
- ```npm run serve```
3. Open browser at: 127.0.0.1:8080 to use app