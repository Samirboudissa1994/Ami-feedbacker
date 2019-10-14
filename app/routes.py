from flask import render_template, request, url_for, flash, redirect, request
from app import app, db, bcrypt, User
import sqlite3
from sqlite3 import Error
from app.queries import *
from app.forms import *
from app.gen_key import *
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CourseKeyForm()
    if form.validate_on_submit():
        course_id = select_course_by_course_key(form.course_key.data)
        if course_id is None:
            flash('Kurssia ei löydy')
        else:
            return redirect(url_for('feedback_add', key=form.course_key.data))
    return render_template('index.html', title='Amiedu kurssipalautejärjestelmä', form=form)


@app.route('/courses')
def courses():
    res = select_all_courses()
    return render_template('courses.html', title='Kurssit', courses=res)


@app.route('/course_add', methods=['GET', 'POST'])
def course_add():
    conn = create_connection()
    form = NewCourseForm()
    res = select_all_instructors()
    form.instructor_ID.choices = [(i[0], i[2] + " " + i[1]) for i in res]
    if form.validate_on_submit():
        conn = create_connection()
        with conn:
            course_key = gen_key()
            course = new_course(conn, form.instructor_ID.data, form.courseName.data, form.courseInfo.data, form.courseStartDate.data, form.courseEndDate.data, course_key)
        flash('Kurssi luotu: {} Kurssiavain: {}'.format(
            form.courseName.data, course_key))
        return redirect('/index')
    return render_template('course_add.html', title='Uusi kurssi', form=form)


@app.route('/instructor_list')
def instructor_list():
    res = select_all_instructors()
    return render_template('instructor_list.html', title='Kouluttajat', instructors=res)


@app.route('/instructor_add', methods=['GET', 'POST'])
@login_required
def instructor_add():
    form = NewInstructorForm()
    if form.validate_on_submit():
        conn = create_connection()
        with conn:
            res = new_instructor(conn, form.forename.data, form.surname.data)

        flash('Luotiin uusi kouluttaja {} {}'.format(
            form.forename.data, form.surname.data))
        return redirect('/index')

    return render_template('instructor_add.html', title='Uusi kouluttaja', form=form)


@app.route('/feedback_view')
def view_feedback():
    res = select_all_feedback()
    return render_template('feedback_all.html', title='Palaute', feedback=res)


@app.route('/feedback', methods=['GET', 'POST'])
def feedback_add():
    course = select_course_by_course_key(request.args.get('key'))
    if course is None:
        return redirect('/index')

    form = NewFeedbackForm()
    form.feedback_course_ID.data = course[0]
    if form.validate_on_submit():
        conn = create_connection()
        with conn:
            feedback = new_feedback(conn, form.feedback_course_ID.data, form.feedback_grade.data, form.feedback_text.data)
        flash('Palaute vastaanotettu')
        return redirect('/index')
    return render_template('feedback.html', title='Anna palaute', form=form, course_name=course[2], course_info=course[3])


@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        flash('Olet jo kirjautuneena sisään!')
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user)
                next_page = request.args.get('next')
                flash('Kirjautut sisään adminina')
                return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Virheellinen käyttäjänimi tai salasana')
    return render_template('admin_login.html', title='Admin kirjautuminen', form=form)


@app.route('/admin_logout')
def admin_logout():
    logout_user()
    flash('Kirjauduttu ulos')
    return redirect(url_for('index'))
