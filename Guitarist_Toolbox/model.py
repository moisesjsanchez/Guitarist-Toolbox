from Guitarist_Toolbox import db


class Chord(db.Model):
    id = db.Column(db.String, primary_key=True)
    chord = db.Column(db.String, nullable=False)


class Scale(db.Model):
    id = db.Column(db.String, primary_key=True)
    scale = db.Column(db.String, nullable=False)


class Time(db.Model):
    id = db.Column(db.String, primary_key=True)
    time_signature = db.Column(db.String, nullable=False)
    time_type = db.Column(db.String)


class Technique(db.Model):
    id = db.Column(db.String, primary_key=True)
    technique = db.Column(db.String, nullable=False)
    tech_type = db.Column(db.String)
