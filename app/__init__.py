from flask import Flask

server = Flask(__name__)
server.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
server.config['CORS_HEADERS'] = 'Content-Type'

from app import views