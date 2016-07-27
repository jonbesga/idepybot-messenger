from flask import Flask, request
import os

app = Flask(__name__)
app.debug = True

VERIFY_TOKEN = os.environ['verify_token']

@app.route("/webhook", methods=['GET','POST'])
def hook():
	if request.method == 'POST':
		print(request.get_json())
		return '200'
	else:
		if request.args.get('hub.verify_token') == VERIFY_TOKEN:
			return request.args.get('hub.challenge')
		else:
			return 'Error, wrong validation token'

	