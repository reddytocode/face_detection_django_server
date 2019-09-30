Face Detection

Run Server:
    - Make avaiable to the world
        - cv_api/settings.py add your server ip to ALLOWED_HOSTS = [server_ip_or_domain]
    - python3 manage.py runserver 0.0.0.0:8000

Run local Test:
    - python3 main.py

Run test from other device with the same project:
    - important files: images/*
    - in the main.py file change the ip of the server and the port
    - python3 main.py
    

