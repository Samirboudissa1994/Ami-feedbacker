import sqlite3
from sqlite3 import Error

db_file = r"./data/data.sqlite"


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def check_course_key(key):
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM course WHERE course_key=? LIMIT 1", (key,))
        key_exists = cur.fetchone() is not None
    return key_exists


def select_course_by_course_key(key):
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM course WHERE course_key=?", (key,))
        course_ID = cur.fetchone()
    return course_ID


def select_all_courses():
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM course INNER JOIN instructor ON course.course_instructor_ID=instructor.instructor_ID;")
        rows = cur.fetchall()
    return rows


def select_all_feedback():
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM feedback;")
        rows = cur.fetchall()
    return rows


def select_all_instructors():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM instructor WHERE instructor_ID > 0 ORDER BY instructor_surname ;")

    rows = cur.fetchall()
    return rows


def new_instructor(conn, forename, surname):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO instructor (instructor_forename, instructor_surname) VALUES (?,?)", (forename, surname))
    ###cur.commit()###
    return cur.lastrowid


def new_course(conn, instructor_ID, courseName, courseInfo, courseStartDate, courseEndDate, course_key):
    cur = conn.cursor()
    cur.execute("INSERT INTO course (course_instructor_ID, course_name, course_info, course_start_date, course_end_date, course_key) VALUES (?,?,?,?,?,?)",
                (instructor_ID, courseName, courseInfo, courseStartDate, courseEndDate, course_key))
    ###cur.commit()###
    return cur.lastrowid


def new_feedback(conn, feedback_course_ID, feedback_grade, feedback_text):
    cur = conn.cursor()
    cur.execute("INSERT INTO feedback (feedback_course_ID, feedback_grade, feedback_text) VALUES (?,?,?)",
                (feedback_course_ID, feedback_grade, feedback_text))
    ###cur.commit()###
    return cur.lastrowid


def create_tables():
    sql_create_feedback_table = """ CREATE TABLE IF NOT EXISTS "feedback" (
    `feedback_ID`   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `feedback_course_ID`    INTEGER,
    `feedback_grade`    INTEGER,
    `feedback_text` TEXT,
    `feedback_11`   INTEGER,
    `feedback_12`   INTEGER,
    `feedback_13`   INTEGER,
    FOREIGN KEY("feedback_course_ID") REFERENCES "instructor"("instructor_ID")
    ); """

    sql_create_instructor_table = """
    CREATE TABLE IF NOT EXISTS "instructor" (
    "instructor_ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "instructor_forename"   TEXT NOT NULL,
    "instructor_surname"    TEXT NOT NULL
    );"""

    sql_create_course_table = """ CREATE TABLE IF NOT EXISTS "course" (
    "course_ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "course_instructor_ID"  INTEGER NOT NULL,
    "course_name"   TEXT NOT NULL,
    "course_info"   TEXT NOT NULL,
    "course_start_date" TEXT NOT NULL,
    "course_end_date"   TEXT NOT NULL,
    "course_key"    TEXT NOT NULL,
    FOREIGN KEY("course_instructor_ID") REFERENCES "course"("course_ID")
    ); """

    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql_create_instructor_table)
    cur.execute(sql_create_course_table)
    cur.execute(sql_create_feedback_table)

    if cur.execute("SELECT COUNT(*) FROM instructor").fetchone()[0] == 0:
        with conn:
            new_instructor(conn, "kurssi:", "! Valitse ")
