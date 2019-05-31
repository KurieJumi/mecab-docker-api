#!/bin/python3
import requests
import json
import MeCab

from flask import Flask, abort, jsonify, request
from pprint import pprint as pp
# log memo : https://www.subarunari.com/entry/2017/10/07/014911

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

messages = ['Success', 'Failed']

@app.route('/mecab/v1/parse-ipadic', methods=['GET'])
def parse():
    sentence = request.args.get('sentence', '')
    option = request.args.get('option', '')

    results = mecab_parse(sentence)

    if option=='Owakati':
        results = mecab_tokenizer(sentence)

    return mecab_response(200, messages[0], results, 'ipadic')


@app.errorhandler(400)
def error400(error):
    return mecab_response(400, messages[1], None, None)


def mecab_response(status, message, results, dic):
    return jsonify({'status': status, 'message': message, 'results': results, 'dict': dic}), status


def mecab_tokenizer(sentence):
    app.logger.info('[mecab_tokenizer] Sample Log')

    dic_dir = "/var/lib/mecab/dic/"
    dic_name = 'ipadic-utf8'

    m = MeCab.Tagger('-Owakati -d ' + dic_dir + dic_name)

    return [m.parse(sentence).splitlines()]


def mecab_parse(sentence):
    app.logger.info('[mecab_parse] Sample Log')

    dic_dir = "/var/lib/mecab/dic/"
    dic_name = 'ipadic-utf8'

    m = MeCab.Tagger('-d ' + dic_dir + dic_name)

    # default output format of mecab
    format = ['表層形', '品詞', '品詞細分類1', '品詞細分類2', '品詞細分類3', '活用形', '活用型','原型','読み','発音']

    return [dict(zip(format, (lambda x: [x[0]]+x[1].split(','))(p.split('\t')))) for p in m.parse(sentence).split('\n')[:-2]]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)