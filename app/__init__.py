from flask import Flask, request
import os

app = Flask(__name__)
app.debug = True

VERIFY_TOKEN = os.environ['verify_token']

@app.route("/webhook")
def hook():
	print('PETICION REALIZADA')
	print(request)
	if request.method == 'POST':
		print(request.get_json())
	else:
		if request.args.get('hub.verify_token') == VERIFY_TOKEN:
			return request.args.get('hub.challenge')
		else:
			return 'Error, wrong validation token'