from Guitarist_Toolbox import db

class MusicInformation(db.Model):
    id = db.Column(db.String)
    chord = db.Column(db.String, nullable=False)
    scale = db.Column(db.String, nullable=False)
    time_signature = db.Column(db.String, nullable=False)
    technique = db.Column(db.String, nullable=False)
