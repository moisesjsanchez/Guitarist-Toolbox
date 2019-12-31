from flask import Flask, jsonify, request, Blueprint
from Guitarist_Toolbox import db
from Guitarist_Toolbox.model import Chord,Scale,Time,Technique

api = Blueprint('api', __name__)

#get all music information

@api.route('/music-info/chords', methods=['GET'])
def get_chords():
    music_info = request.get_json()
    chords = Chord.query.all()

    output = []
    for chord in chords:
        all_chords = {}
        all_chords['chord'] = chord.chord
        output.append(all_chords)
    
    return jsonify({'Chord Progressions': output}), 200

@api.route('/music-info/scales', methods=['GET'])
def get_scales():
    music_info = request.get_json()
    scales = Scale.query.all()

    output = []
    for scale in scales:
        all_scales = {}
        all_scales['scale'] = scale.scale
        output.append(all_scales)
    
    return jsonify({'Scales': output}), 200

@api.route('/music-info/technique', methods=['GET'])
def get_technique():
    music_info = request.get_json()
    techniques = Technique.query.all()

    output = []
    for technique in techniques:
        all_technique = {}
        all_technique['technique'] = technique.technique
        output.append(all_technique)
    
    return jsonify({'Techniques': output}), 200

@api.route('/music-info/time', methods=['GET'])
def get_time():
    music_info = request.get_json()
    times = Time.query.all()

    output = []
    for time in times:
        all_times = {}
        all_times['time_signature'] = time.time_signature
        output.append(all_times)
    
    return jsonify({'Time Signatues': output}), 200

#get a single musical information
'''
@app.route('/music-info/chord/<chord>', methods=['GET'])
def get_chords():
    request.get_json()
    music_info = MusicInfo()
'''

'''
@app.route('/music-info/technique'/<technique>', methods=['GET'])
def get_chords():
    request.get_json()
    music_info = MusicInfo()
'''

'''
@app.route('/music-info/time-signature/<time-signature>', methods=['GET'])
def get_chords():
    request.get_json()
    music_info = MusicInfo()
'''

'''
@app.route('/music-info/scale/<scale>', methods=['GET'])
def get_chords():
    request.get_json()
    music_info = MusicInfo()
'''
