from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class AddPassenger(FlaskForm):
    name = StringField('name')
    flightid = StringField('flight id')
    submit = SubmitField("add new passenger")



