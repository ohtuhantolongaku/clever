import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_commands', methods=['POST'])
def run_commands():
    github_link = request.form['github_link']
    app_name = request.form['app_name']

    # Run the 'clever login' command
    login_command = 'clever login'
    login_process = subprocess.Popen(login_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Run the 'clever create' command with GitHub link and app name
    create_command = f'clever create -t docker --github {github_link} -a {app_name}'
    create_process = subprocess.Popen(create_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Collect command output
    output, errors = [], []
    for process in [login_process, create_process]:
        while True:
            line = process.stdout.readline()
            if not line:
                break
            output.append(line.decode('utf-8').strip())
        while True:
            line = process.stderr.readline()
            if not line:
                break
            errors.append(line.decode('utf-8').strip())

    return jsonify({'output': output, 'errors': errors})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
