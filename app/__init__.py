#===========================================================
# PROJECT NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Home page - Show options 
#-----------------------------------------------------------
@app.get("/")
def show_notes():
        flash("Test message")
        flash("Test SUCCESS message", "success")
        flash("Test INFO message", "info")
        flash("Test WARNING message", "warning")
        flash("Test ERROR message", "error")

        return render_template("pages/index.jinja")

#===========================================================
# Import - Shows a text box for easy pasting 
#===========================================================
@app.get("/import-data")
def import_data():   
 return render_template("pages/import-data.jinja")

#===========================================================
# Class List - Shows students in the class
#===========================================================
@app.get("/class-room")
def show_class_list():

    with connect_db() as db:
            sql = """
                SELECT reports.student_id, students.name

                FROM reports

                JOIN students ON reports.student_id = students.id
                
                ORDER BY students.name ASC
            """
            params = ()
            students = db.execute(sql, params).fetchall()
    
    return render_template("pages/class-room.jinja", students=students)

#===========================================================
# Student Info - Shows which terms have reports completed 
#===========================================================
@app.get("/student-info/<id>")
def show_student_info(id):

    with connect_db() as db:
            sql = """
                SELECT id, name
                FROM students
                WHERE id = ?
            """
            params = (id, )
            student = db.execute(sql, params).fetchone()
    
            sql = """
                SELECT term
                FROM reports
                WHERE student_id = ?

            """
            params = (id, )
            reports = db.execute(sql, params).fetchall()
    print(student)
    return render_template("pages/student-info.jinja", student=student, reports=reports)

#===========================================================
# Report Form - Form for student's report for a term (Page 1)
#===========================================================
@app.get("/student-info/<id>/report-form/<term>")
def render_report_form_1(id, term):

    with connect_db() as db:
            sql = """
                SELECT id, name
                FROM students
                WHERE id = ? 
            """
            params = (id,)
            student = db.execute(sql, params).fetchone()
    
            sql = """
                SELECT term
                FROM reports
                WHERE student_id = ? AND term == ?
    

            """
            params = (id, term)
            reports = db.execute(sql, params).fetchall()
    
    return render_template("pages/report-form-page-1.jinja", student=student, reports=reports)

#===========================================================
# Report Form - Form for student's report for a term (Page 2)
#===========================================================
@app.get("/student-info/<id>/report-form/<term>/2")
def render_report_form_2(id, term):

    with connect_db() as db:
            sql = """
                SELECT id, name
                FROM students
                WHERE id = ? 
            """
            params = (id,)
            student = db.execute(sql, params).fetchone()
    
            sql = """
                SELECT term
                FROM reports
                WHERE student_id = ? AND term == ?
            """
            params = (id, term)
            reports = db.execute(sql, params).fetchall()
    
    return render_template("pages/report-form-page-2.jinja", student=student, reports=reports)

#===========================================================
# Report Form - Form for student's report for a term (Page 3)
#===========================================================
@app.get("/student-info/<id>/report-form/<term>/3")
def render_report_form_3(id, term):

    with connect_db() as db:
            sql = """
                SELECT id, name
                FROM students
                WHERE id = ? 
            """
            params = (id,)
            student = db.execute(sql, params).fetchone()
    
            sql = """
                SELECT term
                FROM reports
                WHERE student_id = ? AND term == ?
            """
            params = (id, term)
            reports = db.execute(sql, params).fetchall()
    
    return render_template("pages/report-form-page-3.jinja", student=student, reports=reports)

#===========================================================
# Report Form - Form for student's report for a term (Page 4)
#===========================================================
@app.get("/student-info/<id>/report-form/<term>/4")
def render_report_form_4(id, term):

    with connect_db() as db:
            sql = """
                SELECT id, name
                FROM students
                WHERE id = ? 
            """
            params = (id,)
            student = db.execute(sql, params).fetchone()
    
            sql = """
                SELECT term
                FROM reports
                WHERE student_id = ? AND term == ?
            """
            params = (id, term)
            reports = db.execute(sql, params).fetchall()
    
    return render_template("pages/report-form-page-4.jinja", student=student, reports=reports)

#===========================================================
# Report Form - Form for student's report post (Page 1)
#===========================================================
@app.post("/student-info/<id>/report-form/<term>")
def post_report_form_1(id, term):
    session["maths_measure"] = request.form.get("measurment-range")
    session["maths_algebra"] = request.form.get("algebra-range")
    session["maths_number"] = request.form.get("number-range")
    session["maths_geometry"] = request.form.get("geometry-range")
    session["maths_statistics"] = request.form.get("statistics-range")

    return redirect(f"/student-info/{id}/report-form/{term}/2")

#===========================================================
# Report Form - Form for student's report post (Page 2)
#===========================================================
@app.post("/student-info/<id>/report-form/<term>/2")
def post_report_form_2(id, term):
    session["reading_recognition"] = request.form.get("word-recognition-range")
    session["reading_comprehension"] = request.form.get("comprehension-range")
    session["reading_analysis"] = request.form.get("critical-analysis-range")

    return redirect(f"/student-info/{id}/report-form/{term}/3")

#===========================================================
# Report Form - Form for student's report post (Page 3)
#===========================================================
@app.post("/student-info/<id>/report-form/<term>/3")
def post_report_form_3(id, term):
    session["writing_transcript"] = request.form.get("transcript-range")
    session["writing_composition"] = request.form.get("composition-range")
    session["writing_process"] = request.form.get("writing-process-range")

    return redirect(f"/student-info/{id}/report-form/{term}/4")

#===========================================================
# Report Form - Form for student's report post (Page 4)
#===========================================================
@app.post("/student-info/<id>/report-form/<term>/4")
def post_report_form_4(id, term):

    session["maths_measure"] = request.form.get("measurment-range")
    session["maths_algebra"] = request.form.get("algebra-range")
    session["maths_number"] = request.form.get("number-range")
    session["maths_geometry"] = request.form.get("geometry-range")
    session["maths_statistics"] = request.form.get("statistics-range")

    session["reading_recognition"] = request.form.get("word-recognition-range")
    session["reading_comprehension"] = request.form.get("comprehension-range")
    session["reading_analysis"] = request.form.get("critical-analysis-range")

    session["writing_transcript"] = request.form.get("transcript-range")
    session["writing_composition"] = request.form.get("composition-range")
    session["writing_process"] = request.form.get("writing-process-range")

    session["maths_comment"] = request.form.get("math-text")
    session["reading_comment"] = request.form.get("reading-text")
    session["writing_comment"] = request.form.get("writing-text")
    session["behaviour_comment"] = request.form.get("behaviour-text")



    sql = """
    INSERT INTO reports (maths_meas,  maths_alge, maths_numb, maths_geom, maths_stat, maths_behaviour, maths_comment, 
                reading_reco, reading_comp, reading_crit, reading_behaviour, reading_comment, 
                writing_tran, writing_comp, writing_proc, writing_behaviour, writing_comment, 
                behaviour_comment)
    VALUES()
    """
    params = ()
    # For Success Message ==================================================== #
    with connect_db() as db:
                sql = """
                    SELECT name,
                    FROM students
                    WHERE id = ? 
                """
                params = ()
                student = db.execute(sql, params).fetchone()

                sql = """
                    SELECT term
                    FROM reports
                    WHERE student_id = ? AND term == ?
                """
                params = (id, term)
                reports = db.execute(sql, params).fetchall()

    flash(f"Successfully added report to {student.name} for term {reports.term}", "success")
    return redirect(f"/student-info/{id}", student=student, reports=reports)

#===============================================================
# Report Preview editing - Allows the user to edit student info UNFINISHED
#===============================================================
@app.post("/class/update")
def process_student_report_form():
    #Get the form data
    maths_measure    = request.form.get("maths_meas", "unknown").strip()
    maths_algebra    = request.form.get("maths_alge ", "unknown").strip()
    maths_number     = request.form.get("maths_numb", "unknown").strip()
    maths_geometry   = request.form.get("maths_geom", "unknown").strip()
    maths_statistics = request.form.get("maths_stat", "unknown").strip()
    maths_behaviour  = request.form.get("maths_behaviour", "unknown").strip()

    student_id = request.form.get("id", "unknown").strip()

    #Connect to the database
    with connect_db() as db:
        sql = """ 
            INSERT INTO reports ()
            VALUES (?, ?)
        """

        params = (maths_measure, maths_algebra, maths_number, maths_geometry, maths_statistics, maths_behaviour)        
        
        #Run the query
        db.execute(sql, params)

        flash(f"{ name } info updated successfully!")
        
    #done, redirect to the creature list page
    return redirect("/report-preview")   

#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

