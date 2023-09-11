from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Retrieve query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    github_file_url = request.args.get('github_file_url')
    github_repo_url = request.args.get('github_repo_url')

    # Get the current day of the week
    current_day = datetime.datetime.now().strftime('%A')

    # Get the current UTC time with a +/- 2 minute window
    current_time = datetime.datetime.utcnow()

    # Prepare the JSON response
    response_data = {
        "slack_name": "Jayneey",
        "current_day": "Monday",
        "utc_time": current_time.strftime('%Y-%m-%d Time:%H:%M:%S'),
        "track": "Backend",
        "github_file_url": "https://github.com/Jayneey/hngx-stage1.git/app.py",
        "github_repo_url": "https://github.com/Jayneey/hngx-stage1.git",
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
