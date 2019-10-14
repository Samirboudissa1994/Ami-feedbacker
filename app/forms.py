from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, RadioField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, NumberRange, Length


class CourseKeyForm(FlaskForm):
    '''course_key = StringField('Kurssiavain', validators=[DataRequired(message=None), Length(min=6, max=6, message="Kurssiavain on kuusi(6) merkkiä")])'''
    course_key = StringField('Kurssiavain', validators=[])
    submit = SubmitField('Lähetä')


class NewInstructorForm(FlaskForm):
    forename = StringField('Etunimi', validators=[DataRequired()])
    surname = StringField('Sukunimi', validators=[DataRequired()])
    submit = SubmitField('Lisää')


class NewCourseForm(FlaskForm):
    instructor_ID = SelectField('kouluttaja', default=1, coerce=int, validators=[NumberRange(min=2, max=99999, message="Valitse kouluttaja")])
    courseName = StringField('Kurssin nimi', validators=[DataRequired()])
    courseInfo = StringField('Kurssin tietoa', validators=[DataRequired()])
    courseStartDate = StringField('Alkamispäivä', validators=[DataRequired()])
    courseEndDate = StringField('Päättymispäivä', validators=[DataRequired()])
    submit = SubmitField('lisää')


class NewFeedbackForm(FlaskForm):
    feedback_course_ID = HiddenField()
    feedback_grade = RadioField('Grade', coerce=int, choices=[(int(1), '1'), (int(2), '2'), (int(3), '3'), (int(4), '4'), (int(5), '5')], validators=[DataRequired(message="x")])
    feedback_text = TextAreaField('Vapaa palaute', validators=[DataRequired(message="x")])
    submit = SubmitField('Lähetä')


class LoginForm(FlaskForm):
    username = StringField('Käyttäjä', validators=[DataRequired()])
    password = StringField('Salasana', validators=[DataRequired()])
    submit = SubmitField('Kirjaudu')
