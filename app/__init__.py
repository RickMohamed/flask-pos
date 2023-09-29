from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b413ad06801c880e897865c2a4c63766cbc5767e6c5d8940ghjmftreer78io'


from app import routes