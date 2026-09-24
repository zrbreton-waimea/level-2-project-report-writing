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
@app.get("/report-preview")
def show_example():

    with connect_db() as db:
            sql = """
                SELECT student_id, term, maths_meas, maths_alge, maths_numb, 
                maths_geom, maths_stat, maths_behaviour, maths_comment

                FROM reports

            """
            params = ()
            list = db.execute(sql, params).fetchall()
    
    return render_template("pages/report-preview.jinja", list=list)

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

