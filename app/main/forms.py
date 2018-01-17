from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, Length


class EditProfileForm(FlaskForm):
    name - StringField('Reale name', validators=[length(0,64)])
    location = StringField('location', validators=[length(0,64)])
    about_me = TextAreaField('Aboute me')
    submit = SubmitField('Submit')