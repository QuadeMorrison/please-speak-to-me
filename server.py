#!/usr/bin/env python3
from __future__ import print_function
from flask import Flask, request, send_from_directory
from os import listdir, environ
from os.path import isfile, join
import os
import time
from pydub import AudioSegment
import sys
sys.path.append("../tacotron")
from synthesize import synthesize

app = Flask(__name__, static_folder='./dist/static')

@app.route('/')
def root():
    return app.send_static_file('index.html')

def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms

@app.route("/voice", methods = ['POST'])
def voice():
    if request.method == 'POST':
        req_json = request.get_json()
        if req_json['text'] is not None:
            sentences = [str(sent) for sent in req_json['text'].split(".")]
            synthesize(sentences)
            mypath = "../tacotron/samples/"
            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            onlyfiles.sort()
            wavs = [AudioSegment.from_wav(join(mypath, wavpath)) for wavpath in onlyfiles]
            wavs = [wav[0:len(wav)-detect_leading_silence(wav.reverse())] for wav in wavs]
            combined_sounds = reduce(lambda sound1, sound2: sound1 + sound2, wavs)
            combined_sounds.export("../tacotron/samples/1.wav", format="wav")
            return send_from_directory('../tacotron/samples', '1.wav', as_attachment=True)
        else:
            return "No bueno..."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
