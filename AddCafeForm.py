from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL

class AddCafeForm(FlaskForm):
    name = StringField(label='Cafe Name', validators=[DataRequired(), Length(min=1, max=300)])
    location = StringField(label='Location', validators=[
        DataRequired(),
        Length(min=1, max=300),
        URL(message='Invalid location entry, must be in the form of a URL.')
    ])
    open = SelectField(label='Open', choices=[('6', '6AM'), ('7', '7AM'), ('8', '8AM')], validators=[DataRequired(), Length(min=1, max=300)])
    close = SelectField(label='Open', choices=[('6', '6PM'), ('7', '7PM'), ('8', '8PM')], validators=[DataRequired(), Length(min=1, max=300)])
    coffee = StringField(label='Coffee', validators=[DataRequired(), Length(min=1, max=300)])
    wifi = StringField(label='Wifi', validators=[DataRequired(), Length(min=1, max=300)])
    power = StringField(label='Power', validators=[DataRequired(), Length(min=1, max=300)])
    submit = SubmitField('Submit')