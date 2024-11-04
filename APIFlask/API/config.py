DEBUG = True

#Dados do BANCO de DADOS
USERNAME = ''
PASSWORD = ''
SERVER = 'localhost'
DB = 'api_flask'

#String de conexão
SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'

#Live Code no BD
SQLALCHEMY_TRACK_MODIFICATIONS = True





