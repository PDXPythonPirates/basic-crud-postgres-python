from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class DeletePassenger(FlaskForm):
    id = StringField('id')
    submit = SubmitField("delete passenger")