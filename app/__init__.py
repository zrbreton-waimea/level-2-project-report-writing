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
# Report Preview - Shows seed data
#===========================================================
@app.get("/class")
def show_example():

    with connect_db() as db:
            sql = """
                SELECT reports.student_id, students.name

                FROM reports

                JOIN students ON reports.student_id = students.id

            """
            params = ()
            list = db.execute(sql, params).fetchall()
    
    return render_template("pages/class-room.jinja", list=list)

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

        flash(f"{student_id} info updated successfully!")
        
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

