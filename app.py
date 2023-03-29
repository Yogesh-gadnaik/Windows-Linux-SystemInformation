
from flask import Flask, render_template, request
from logic.getsysinfo import sys_windows, sys_linux
import platform


apk = Flask(__name__)
system = platform.system()


@apk.route('/')
def root():
    data = False
    if system == 'Windows':
        data = True
    return render_template('index.html', data=data)


@apk.route('/home', methods=['POST', 'GET'])
def load_home():
    if system == 'Windows':
        system_info = request.form['select_val']
        response = sys_windows(system_info)
        return render_template('response.html', result=response)
    else:
        system_info = request.form['select_val']
        response = sys_linux(system_info)
        if system_info == "allinfo":
            return render_template('all_info_response.html', result=response)
        else:
            return render_template('response.html', result=response)


if __name__ == '__main__':
    apk.run(debug=True, port=5001)
