from flask import jsonify, Blueprint, render_template
from Guitarist_Toolbox.model import Chord, Scale, Time, Technique
import random

api = Blueprint('api', __name__)

# homepage with information about API service
@api.route('/')
def index():
    return render_template('index.html')

# get all music information
@api.route('/music-info/all', methods=['GET'])
def get_all():
    chords = Chord.query.all()
    scales = Scale.query.all()
    techniques = Technique.query.all()
    times = Time.query.all()

    output = []

    for chord in chords:
        all_chords = {}
        all_chords['Chord'] = chord.chord
        output.append(all_chords)

    for scale in scales:
        all_scales = {}
        all_scales['Scale'] = scale.scale
        output.append(all_scales)

    for technique in techniques:
        all_technique = {}
        all_technique['Technique'] = technique.technique
        all_technique['Type'] = technique.tech_type
        output.append(all_technique)

    for time in times:
        all_times = {}
        all_times['Time Signature'] = time.time_signature
        all_times['Type'] = time.time_type
        output.append(all_times)

    return jsonify(output), 200


@api.route('/music-info/chords', methods=['GET'])
def get_chords():
    chords = Chord.query.all()

    output = []
    for chord in chords:
        all_chords = {}
        all_chords['Chord'] = chord.chord
        output.append(all_chords)

    return jsonify(output), 200


@api.route('/music-info/scales', methods=['GET'])
def get_scales():
    scales = Scale.query.all()

    output = []
    for scale in scales:
        all_scales = {}
        all_scales['Scale'] = scale.scale
        output.append(all_scales)

    return jsonify(output), 200


@api.route('/music-info/techniques', methods=['GET'])
def get_technique():
    techniques = Technique.query.all()

    output = []
    for technique in techniques:
        all_technique = {}
        all_technique['Technique'] = technique.technique
        all_technique['Type'] = technique.tech_type
        output.append(all_technique)

    return jsonify(output), 200


@api.route('/music-info/times', methods=['GET'])
def get_time():
    times = Time.query.all()

    output = []
    for time in times:
        all_times = {}
        all_times['Time Signature'] = time.time_signature
        all_times['Type'] = time.time_type
        output.append(all_times)

    return jsonify(output), 200

# get a single musical information by critera


@api.route('/music-info/techniques/both', methods=['GET'])
def get_both():
    current_tech_type = Technique.query.filter_by(tech_type='Both')

    output = []

    for tech_type in current_tech_type:
        all_technique = {}
        all_technique['Technique'] = tech_type.technique
        all_technique['Type'] = tech_type.tech_type
        output.append(all_technique)

    return jsonify(output), 200


@api.route('/music-info/techniques/electric', methods=['GET'])
def get_electric():
    current_tech_type = Technique.query.filter_by(tech_type='Electric')

    output = []

    for tech_type in current_tech_type:
        all_technique = {}
        all_technique['Technique'] = tech_type.technique
        all_technique['Type'] = tech_type.tech_type
        output.append(all_technique)

    return jsonify(output), 200


@api.route('/music-info/techniques/acoustic', methods=['GET'])
def get_acoustic():
    current_tech_type = Technique.query.filter_by(tech_type='Acoustic')

    output = []

    for tech_type in current_tech_type:
        all_technique = {}
        all_technique['Technique'] = tech_type.technique
        all_technique['Type'] = tech_type.tech_type
        output.append(all_technique)

    return jsonify(output), 200


@api.route('/music-info/times/simple', methods=['GET'])
def get_simple():
    current_time_type = Time.query.filter_by(time_type='Acoustic')

    output = []

    for time_type in current_time_type:
        all_time_signature = {}
        all_time_signature['Time Signature'] = time_type.time_signature
        all_time_signature['Type'] = time_type.time_type
        output.append(all_time_signature)

    return jsonify(output), 200


@api.route('/music-info/times/compound', methods=['GET'])
def get_compound():
    current_time_type = Time.query.filter_by(time_type='Compound')

    output = []

    for time_type in current_time_type:
        all_time_signature = {}
        all_time_signature['Time Signature'] = time_type.time_signature
        all_time_signature['Type'] = time_type.time_type
        output.append(all_time_signature)

    return jsonify(output), 200


@api.route('/music-info/times/complex', methods=['GET'])
def get_complex():
    current_time_type = Time.query.filter_by(time_type='Complex')

    output = []

    for time_type in current_time_type:
        all_time_signature = {}
        all_time_signature['Time Signature'] = time_type.time_signature
        all_time_signature['Type'] = time_type.time_type
        output.append(all_time_signature)

    return jsonify(output), 200


# get random music information based on column selected
@api.route('/music-info/chords/random', methods=['GET'])
def get_random_chords():
    chords = Chord.query.all()

    output = []
    for chord in chords:
        all_chords = {}
        all_chords['Chord'] = chord.chord
        output.append(all_chords)

    return jsonify(random.choice(output)), 200


@api.route('/music-info/scales/random', methods=['GET'])
def get_random_scales():
    scales = Scale.query.all()

    output = []
    for scale in scales:
        all_scales = {}
        all_scales['Scale'] = scale.scale
        output.append(all_scales)

    return jsonify(random.choice(output)), 200


@api.route('/music-info/techniques/random', methods=['GET'])
def get_random_technique():
    techniques = Technique.query.all()

    output = []
    for technique in techniques:
        all_technique = {}
        all_technique['Technique'] = technique.technique
        all_technique['Type'] = technique.tech_type
        output.append(all_technique)

    return jsonify(random.choice(output)), 200


@api.route('/music-info/times/random', methods=['GET'])
def get_random_time():
    times = Time.query.all()

    output = []
    for time in times:
        all_times = {}
        all_times['Time Signature'] = time.time_signature
        all_times['Type'] = time.time_type
        output.append(all_times)

    return jsonify(random.choice(output)), 200
