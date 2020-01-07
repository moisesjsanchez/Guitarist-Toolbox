from flask import jsonify, Blueprint
from Guitarist_Toolbox.model import Chord, Scale, Time, Technique

api = Blueprint('api', __name__)

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

    return jsonify({'Whole Toolbox': output}), 200


@api.route('/music-info/chords', methods=['GET'])
def get_chords():
    chords = Chord.query.all()

    output = []
    for chord in chords:
        all_chords = {}
        all_chords['Chord'] = chord.chord
        output.append(all_chords)

    return jsonify({'Chord Progressions': output}), 200


@api.route('/music-info/scales', methods=['GET'])
def get_scales():
    scales = Scale.query.all()

    output = []
    for scale in scales:
        all_scales = {}
        all_scales['Scale'] = scale.scale
        output.append(all_scales)

    return jsonify({'Scales': output}), 200


@api.route('/music-info/technique', methods=['GET'])
def get_technique():
    techniques = Technique.query.all()

    output = []
    for technique in techniques:
        all_technique = {}
        all_technique['Technique'] = technique.technique
        all_technique['Type'] = technique.tech_type
        output.append(all_technique)

    return jsonify({'Techniques': output}), 200


@api.route('/music-info/time', methods=['GET'])
def get_time():
    times = Time.query.all()

    output = []
    for time in times:
        all_times = {}
        all_times['Time Signature'] = time.time_signature
        all_times['Type'] = time.time_type
        output.append(all_times)

    return jsonify({'Time Signatues': output}), 200

# get a single musical information by critera


@api.route('/music-info/technique/tech_type/both', methods=['GET'])
def get_both():
    current_tech_type = Technique.query.filter_by(tech_type='Both')

    output = []

    for tech_type in current_tech_type:
        all_technique = {}
        all_technique['Technique'] = tech_type.technique
        all_technique['Type'] = tech_type.tech_type
        output.append(all_technique)

    return jsonify({'Techniques': output}), 200


@api.route('/music-info/technique/tech_type/electric', methods=['GET'])
def get_electric():
    current_tech_type = Technique.query.filter_by(tech_type='Electric')

    output = []

    for tech_type in current_tech_type:
        all_technique = {}
        all_technique['Technique'] = tech_type.technique
        all_technique['Type'] = tech_type.tech_type
        output.append(all_technique)

    return jsonify({'Techniques': output}), 200


@api.route('/music-info/technique/tech_type/acoustic', methods=['GET'])
def get_acoustic():
    current_tech_type = Technique.query.filter_by(tech_type='Acoustic')

    output = []

    for tech_type in current_tech_type:
        all_technique = {}
        all_technique['Technique'] = tech_type.technique
        all_technique['Type'] = tech_type.tech_type
        output.append(all_technique)

    return jsonify({'Techniques': output}), 200


@api.route('/music-info/time/time_type/simple', methods=['GET'])
def get_simple():
    current_time_type = Time.query.filter_by(tech_type='Acoustic')

    output = []

    for time_type in current_time_type:
        all_time_signature = {}
        all_time_signature['Time Signature'] = time_type.time_signature
        all_time_signature['Type'] = time_type.time_type
        output.append(all_time_signature)

    return jsonify({'Time Signatures': output}), 200


@api.route('/music-info/time/time_type/compound', methods=['GET'])
def get_compound():
    current_time_type = Technique.query.filter_by(tech_type='Compound')

    output = []

    for time_type in current_time_type:
        all_time_signature = {}
        all_time_signature['Time Signature'] = time_type.time_signature
        all_time_signature['Type'] = time_type.time_type
        output.append(all_time_signature)

    return jsonify({'Time Signatures': output}), 200


@api.route('/music-info/time/time_type/complex', methods=['GET'])
def get_complex():
    current_time_type = Technique.query.filter_by(tech_type='Complex')

    output = []

    for time_type in current_time_type:
        all_time_signature = {}
        all_time_signature['Time Signature'] = time_type.time_signature
        all_time_signature['Type'] = time_type.time_type
        output.append(all_time_signature)

    return jsonify({'Time Signatures': output}), 200


# get random music information based on column selected
'''

@app.route('/music-info/scale/random', methods=['GET'])
def get_random_chord():

'''

'''

@app.route('/music-info/scale/random', methods=['GET'])
def get_random_scale():

'''

'''

@app.route('/music-info/technique/random', methods=['GET'])
def get_random_technique():

'''

'''
@app.route('/music-info/time-signature/random', methods=['GET'])
def get_random_chord():

'''
