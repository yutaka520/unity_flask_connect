# unity_flask_connect
A program for connecting Unity and the flask server.

# Execution environment
Unity version 2019.3.13f1 or more
docker version 19.03.12 or more
compose version 1.27.2 or more
  
windows or ubuntu ok

# Usage
## server side
1, build docker virtual environment. Then enter the virtual environment.

```bash
cd json_flask
docker-compose up -d --build
docker-compose exec json_flask bash
```

2, Start the program and wait.

```bash
cd opt/src
python3 engine.py
```

## client side
1, Create a unity project and load "ConnectFlaskServer.unitypackage".  
2, Run the project. Then you will see the word "success".
