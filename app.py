from flask import Flask, jsonify, render_template

app = Flask(__name__)

click_count = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def click():
    global click_count
    click_count += 1
    return jsonify({'count': click_count})

@app.route('/get_count', methods=['GET'])
def get_count():
    return jsonify({'count': click_count})


# For Vercel: Create a callable handler
def handler(event, context):
    from flask import request
    return app(environ=event, start_response=context)
