from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__)

# pull in the dev config on init
app.config.from_object('project.config.DevelopmentConfig') #new

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status' : 'success',
        'message': 'pong!'
    })