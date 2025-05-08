from typing import final
from flask import Flask, send_file, render_template, request
from db import *
import random

from commandengine import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/downloads')
def downloads():
    return render_template('downloads.html', versions=verlist)

@app.route('/documentary')
def documentary():
    return render_template('documentary.html')

@app.route('/download/<version>')
def downloadpage(version):
    print(f'{request.remote_addr} möchte {version} wahrscheinlich herunterladen!')

    print(verinfs[drag[version]])
    return render_template('downloadpage.html', versions=verinfs[drag[version]], version=version)

@app.route('/downloadplease/<file>')
def senddownload(file):
    print(file)
    return send_file(f'./files/{file}')

@app.route('/suggest')
def suggestions():
    return render_template('suggestion.html')

@app.route('/gdata', methods=['POST', 'GET'])
def getdata():
    suggesttext = str(request.form['suggtext'])
    print(suggesttext)
    if len(suggesttext) > 3002:
        return render_template('nothx.html')
    elif len(suggesttext) < 1000:
        with open(f'./suggestions/{str(random.randint(1000000, 999999999))}.txt', 'w', encoding='utf8') as file:
            file.write(suggesttext)
        return render_template('thx.html')
    else:
        return render_template('error.html')


@app.route('/ocengine')
def ocode():
    return render_template('ocengine.html')

@app.route('/gocengined', methods=['POST', 'GET'])
def ggocode():
    code = str(request.form['suggtext'])
    print(code)
    with open('./temp/scriptrunner.txt', 'w', encoding='utf8') as file:
        file.write(f'{code}')
    with open('./temp/scriptrunner.txt', 'r') as coder:
        finalout = []
        for line in coder:
            if not line == '\n':
                print(line)
                lout = commandengine(line)
                finalout.append(lout)
                line = ''
            else:
                pass
        print(finalout)
        return render_template('ocengineout.html', oclist=finalout)


app.run(port=8080, host='0.0.0.0')