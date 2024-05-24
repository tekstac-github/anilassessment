version: '2'
 
services:
  web:
    build: .
    image: flask_app
    ports:
      - "5000:5000"
    volumes:
      - .:/code
    environment:
      - FLASK_APP=my_app.py
    command: flask run --host=0.0.0.0 --port=5000
  redis:
    image: redis:alpine
