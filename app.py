#!/usr/bin/env python3

from flask import Flask, request, Response, jsonify
#from flask import Flask, jsonify, request
#from werkzeug.wrappers import Response
import kubernetes as k8s 
import logging
from logging.handlers import RotatingFileHandler
import json 

#import werkzeug.datastructures.TypeConversionDict as wdt
from werkzeug._compat import iterlists
from werkzeug._compat import itervalues

app = Flask(__name__)

@app.route('/', methods=['GET','POST', 'HEAD', 'PUT', 'PATCH', 'DELETE', 'LIST'])
def webhook_home():
    # http://flask.pocoo.org/docs/1.0/api/#flask.Request
    # https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request
    req_dict = request.__dict__
    #logging.info('Request received home dict: \n%s', req_dict)
    if request.method == 'POST':
        logging.info('POST request payload home: %s', request.get_data())
    else:
        logging.info('%s\n%s', request, request.headers)
        
    x = request.__dict__
    logging.info('type x:%s, type request.get_data():%s', type(x), type(request.get_data()))
    x['kind'] = 'List'
    x['apiVersion'] = 'v1'
    logging.info('Returning jsonify(x) home: %s', str(jsonify(list(x))))
    return jsonify(list(x))

@app.route('/hide-namespace', methods=['GET','POST', 'HEAD', 'PUT', 'PATCH', 'DELETE', 'LIST'])
def hide_namespace():
    # https://tedboy.github.io/flask/generated/generated/werkzeug.EnvironHeaders.html
    # https://werkzeug.palletsprojects.com/en/0.15.x/tutorial/#step-0-a-basic-wsgi-introduction
    h = request.headers
    #logging.info('Request received headers: \n%s', h)
    #logging.info('Request received dict: \n%s', request.__dict__)
    #x = list(h)
    #resp = Response(request.headers, mimetype='text/plain')
    if request.method == 'POST':
        logging.info('POST request payload: %s', request.get_data())
    else:
        logging.info('%s\n%s', request, request.headers)
    logging.info('Returning jsonify(x): %s', str(jsonify(x)))
    return jsonify(x)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    context=('cert.pem', 'key.pem')
    app.run(debug=True, host='0.0.0.0', ssl_context=context)

