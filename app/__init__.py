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
        session.clear()
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
                SELECT id, name
                FROM students
                ORDER BY name ASC
            """
            params = ()
            students = db.execute(sql, params).fetchall()
    
    return render_template("pages/class-room.jinja", students=students)

#===========================================================
# Student Info - Shows which terms have reports completed 
#===========================================================
@app.get("/student-info/<id>")
def show_student_info(id):
    consistent = 1 if request.form.get("consistent") else 0

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

#=================================================================
# Report Form - Form for student's report for a term get (Page 1)
#=================================================================
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

#=================================================================
# Report Form - Form for student's report for a term get (Page 2)
#=================================================================
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
    
    return render_template("pages/report-form-page-2.jinja", student=student, reports=reports, term=term)

#==================================================================
# Report Form - Form for student's report for a term get (Page 3)
#==================================================================
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
    
    return render_template("pages/report-form-page-3.jinja", student=student, reports=reports, term=term)

#=============================================================
# Report Form - Form for student's report for a term (Page 4)
#=============================================================
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
    
    return render_template("pages/report-form-page-4.jinja", student=student, reports=reports, term=term)

#==============================================================
# Report Form - Form for student's report session post (Page 1)
#==============================================================
@app.post("/student-info/<id>/report-form/<term>")
def post_report_form_1(id, term):
    session["maths_measure"] = request.form.get("measurment-range")
    session["maths_algebra"] = request.form.get("algebra-range")
    session["maths_number"] = request.form.get("number-range")
    session["maths_geometry"] = request.form.get("geometry-range")
    session["maths_statistics"] = request.form.get("statistics-range")

    session["maths_effort"] = 1 if request.form.get("maths-effort") else 0

    return redirect(f"/student-info/{id}/report-form/{term}/2")

#==============================================================
# Report Form - Form for student's report session post (Page 2)
#==============================================================
@app.post("/student-info/<id>/report-form/<term>/2")
def post_report_form_2(id, term):
    session["reading_recognition"] = request.form.get("word-recognition-range")
    session["reading_comprehension"] = request.form.get("comprehension-range")
    session["reading_analysis"] = request.form.get("critical-analysis-range")

    session["reading_effort"] = 1 if request.form.get("reading-effort") else 0

    return redirect(f"/student-info/{id}/report-form/{term}/3")

#===============================================================
# Report Form - Form for student's report session post (Page 3)
#==============================================================
@app.post("/student-info/<id>/report-form/<term>/3")
def post_report_form_3(id, term):
    consistent = 1 if request.form.get("consistent") else 0

    session["writing_transcript"] = request.form.get("transcript-range")
    session["writing_composition"] = request.form.get("composition-range")
    session["writing_process"] = request.form.get("writing-process-range")

    session["writing_effort"] = 1 if request.form.get("writing-effort") else 0

    return redirect(f"/student-info/{id}/report-form/{term}/4")

#=================================================================
# Report Form - Form for student's report post all to db (Page 4)
#=================================================================
@app.post("/student-info/<id>/report-form/<term>/4")
def post_report_form_4(id, term):
    

    maths_measure =         session["maths_measure"]
    maths_algebra =         session["maths_algebra"]
    maths_number =          session["maths_number"]
    maths_geometry =        session["maths_geometry"]
    maths_statistics =      session["maths_statistics"]
    maths_effort =          session["maths_effort"]
    maths_comment =         request.form.get("math-text")


    reading_recognition =   session["reading_recognition"]
    reading_comprehension = session["reading_comprehension"]
    reading_analysis =      session["reading_analysis"]
    reading_effort =        session["reading_effort"]
    reading_comment =       request.form.get("reading-text")

    writing_transcript =    session["writing_transcript"]
    writing_composition =   session["writing_composition"]
    writing_process =       session["writing_process"]
    writing_effort =        session["writing_effort"]
    writing_comment =       request.form.get("writing-text")

    behaviour_comment =     request.form.get("behaviour-text")

    student_id = id
    term_number = term

    with connect_db() as db:
        sql = """
        INSERT INTO reports (student_id, term, maths_meas,  maths_alge, maths_numb, maths_geom, maths_stat, maths_effort, maths_comment, 
                    reading_reco, reading_comp, reading_crit, reading_effort, reading_comment, 
                    writing_tran, writing_comp, writing_proc, writing_effort, writing_comment, 
                    behaviour_comment)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (student_id, term_number, maths_measure, maths_algebra, maths_number, maths_geometry, maths_statistics, maths_effort, maths_comment, reading_recognition, 
                reading_comprehension, reading_analysis, reading_effort, reading_comment, writing_transcript,  writing_composition, writing_process, 
                writing_effort, writing_comment, behaviour_comment)
        
        db.execute(sql, params)
    
    # For Success Message ==================================================== #
    flash(f"Successfully added report for student {id}, for term {term}!", "success")
    return redirect(f"/student-info/{id}",)

#===========================================================
# Report Form - Delete a student from the class list.
#===========================================================
@app.get("/student-info/<id>/delete")
def delete_student_info(id):
    
    with connect_db() as db:
            sql = """
                DELETE FROM students
                WHERE id = ?
            """
            params = (id, )
            student = db.execute(sql, params)

    return redirect("/class-room",)

#=============================================================================================
# Report Form Edit View - Gets the students existing information for the user to edit (Page 1)
#=============================================================================================
@app.get("/student-info/<id>/report-form/<term>/edit")
def render_report_form_1_edit(id, term):

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

            sql = """
                SELECT maths_meas,  maths_alge, maths_numb, maths_geom, maths_stat, maths_effort, 
                maths_comment, reading_reco, reading_comp, reading_crit, reading_effort, reading_comment, 
                writing_tran, writing_comp, writing_proc, writing_effort, writing_comment, behaviour_comment
                FROM reports
                WHERE student_id = ? AND term == ?
            """
            params = (id, term)
            reports = db.execute(sql, params).fetchone()

    return render_template("pages/report-form-page-1-edit.jinja", student=student, reports=reports)

#==============================================================================================
# Report Form Edit View - Gets the students existing information for the user to edit (Page 2)
#==============================================================================================
@app.get("/student-info/<id>/report-form/<term>/2/edit")
def render_report_form_2_edit(id, term):

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

            sql = """
                SELECT maths_meas,  maths_alge, maths_numb, maths_geom, maths_stat, maths_effort, 
                maths_comment, reading_reco, reading_comp, reading_crit, reading_effort, reading_comment, 
                writing_tran, writing_comp, writing_proc, writing_effort, writing_comment, behaviour_comment
                FROM reports
                WHERE student_id = ? AND term == ?
            """
            params = (id, term)
            reports = db.execute(sql, params).fetchone()

    return render_template("pages/report-form-page-2-edit.jinja", student=student, reports=reports)

#=============================================================================================
# Report Form Edit View - Gets the students existing information for the user to edit (Page 3)
#=============================================================================================
@app.get("/student-info/<id>/report-form/<term>/3/edit")
def render_report_form_3_edit(id, term):

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

            sql = """
                SELECT maths_meas,  maths_alge, maths_numb, maths_geom, maths_stat, maths_effort, 
                maths_comment, reading_reco, reading_comp, reading_crit, reading_effort, reading_comment, 
                writing_tran, writing_comp, writing_proc, writing_effort, writing_comment, behaviour_comment
                FROM reports
                WHERE student_id = ? AND term == ?
            """
            params = (id, term)
            reports = db.execute(sql, params).fetchone()

    return render_template("pages/report-form-page-3-edit.jinja", student=student, reports=reports)

#==============================================================================================
# Report Form Edit View - Gets the students existing information for the user to edit (Page 4)
#==============================================================================================
@app.get("/student-info/<id>/report-form/<term>/4/edit")
def render_report_form_4_edit(id, term):

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

            sql = """
                SELECT maths_meas,  maths_alge, maths_numb, maths_geom, maths_stat, maths_effort, 
                maths_comment, reading_reco, reading_comp, reading_crit, reading_effort, reading_comment, 
                writing_tran, writing_comp, writing_proc, writing_effort, writing_comment, behaviour_comment
                FROM reports
                WHERE student_id = ? AND term == ?
            """
            params = (id, term)
            reports = db.execute(sql, params).fetchone()

    return render_template("pages/report-form-page-4-edit.jinja", student=student, reports=reports)

#==============================================================================
# Report Form Edit View - Edit Form for student's report for a term (Page 1)
#==============================================================================
@app.post("/student-info/<id>/report-form/<term>/edit")
def post_report_form_1_edit(id, term):
    session["maths_measure"] = request.form.get("measurment-range")
    session["maths_algebra"] = request.form.get("algebra-range")
    session["maths_number"] = request.form.get("number-range")
    session["maths_geometry"] = request.form.get("geometry-range")
    session["maths_statistics"] = request.form.get("statistics-range")

    session["maths_effort"] = 1 if request.form.get("maths-effort") else 0

    return redirect(f"/student-info/{id}/report-form/{term}/2/edit")

#==============================================================================
# Report Form Edit View - Edit Form for student's report for a term (Page 2)
#==============================================================================
@app.post("/student-info/<id>/report-form/<term>/2/edit")
def post_report_form_2_edit(id, term):
    session["reading_recognition"] = request.form.get("word-recognition-range")
    session["reading_comprehension"] = request.form.get("comprehension-range")
    session["reading_analysis"] = request.form.get("critical-analysis-range")

    session["reading_effort"] = 1 if request.form.get("reading-effort") else 0

    return redirect(f"/student-info/{id}/report-form/{term}/3/edit")

#==============================================================================
# Report Form Edit View - Edit Form for student's report for a term (Page 3)
#==============================================================================
@app.post("/student-info/<id>/report-form/<term>/3/edit")
def post_report_form_3_edit(id, term):
    session["writing_transcript"] = request.form.get("transcript-range")
    session["writing_composition"] = request.form.get("composition-range")
    session["writing_process"] = request.form.get("writing-process-range")
    
    session["writing_effort"] = 1 if request.form.get("writing-effort") else 0

    return redirect(f"/student-info/{id}/report-form/{term}/4/edit")

#==============================================================================
# Report Form Edit View - Edit Form for student's report for a term (Page 4)
#==============================================================================
@app.post("/student-info/<id>/report-form/<term>/4/edit")
def post_report_form_4_edit(id, term):
    
    maths_measure =         session["maths_measure"]
    maths_algebra =         session["maths_algebra"]
    maths_number =          session["maths_number"]
    maths_geometry =        session["maths_geometry"]
    maths_statistics =      session["maths_statistics"]
    maths_effort =          session["maths_effort"]
    maths_comment =         request.form.get("math-text")


    reading_recognition =   session["reading_recognition"]
    reading_comprehension = session["reading_comprehension"]
    reading_analysis =      session["reading_analysis"]
    reading_effort =        session["reading_effort"]
    reading_comment =       request.form.get("reading-text")

    writing_transcript =    session["writing_transcript"]
    writing_composition =   session["writing_composition"]
    writing_process =       session["writing_process"]
    writing_effort =        session["writing_effort"]
    writing_comment =       request.form.get("writing-text")

    behaviour_comment =     request.form.get("behaviour-text")

    student_id = id
    term_number = term

    with connect_db() as db:
        sql = """
        UPDATE reports
            SET maths_meas = ?, maths_alge = ?, maths_numb = ?, maths_geom = ?, maths_stat = ?,
                maths_effort = ?, maths_comment = ?, reading_reco = ?, reading_comp = ?, reading_crit = ?,
                reading_effort = ?, reading_comment = ?, writing_tran = ?, writing_comp = ?, writing_proc = ?,
                writing_effort = ?, writing_comment = ?, behaviour_comment = ?

            WHERE student_id = ? AND term = ?
        """
        params = (maths_measure, maths_algebra, maths_number, maths_geometry, maths_statistics, maths_effort, maths_comment, reading_recognition, 
                reading_comprehension, reading_analysis, reading_effort, reading_comment, writing_transcript,  writing_composition, writing_process, 
                writing_effort, writing_comment, behaviour_comment, student_id, term_number )
        
        db.execute(sql, params)

# For Success Message ==================================================== #
    flash(f"Successfully edited report for student {id}, for term {term}!", "success")
    return redirect(f"/student-info/{id}",)


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

