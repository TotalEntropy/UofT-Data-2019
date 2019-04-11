import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify
import datetime as dt

###################################################
# Database Setup
###################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite",
        connect_args={'check_same_thread': False}, echo=True)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return """
    <html>
    <h1>Links to all of the available routes</h1><br>
    <ul>
        <li>
            Precipitation values for the last year<br>
            <a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a>
        </li><br>
        <li>
            List of the stations that the values are taken from<br>
            <a href="/api/v1.0/stations">/api/v1.0/stations</a>
        </li><br>
        <li>
            Temperature values for the last year<br>
            <a href="/api/v1.0/tobs">/api/v1.0/tobs</a>
        </li><br>
        <li>
            The min, avg and max temperature values from the date supplied to the max date<br>
            <a href="/api/v1.0/<start>">/api/v1.0/YYYY-MM-DD</a>
        </li><br>
        <li>
            The min, avg and max temperature values between the dates supplied<br>
            <a href="/api/v1.0/<start>/<end>">/api/v1.0/YYYY-MM-DD/YYYY-MM-DD</a>
        </li>
    </ul>
</html>"""

@app.route("/api/v1.0/precipitation")
def Precipitation():

    # Finding the last date
    last_date = str(session.query(Measurement.date).\
                order_by(Measurement.date.desc()).first())\
    # 1 year ago
    year_ago = (dt.datetime.strptime(last_date, "('%Y-%m-%d',)") -
                dt.timedelta(days = 365))            

    # Query
    precipitation = session.query(Measurement.date, Measurement.prcp).\
                    order_by(Measurement.date).\
                    filter(Measurement.date >= year_ago.date()).all()

    # Converting to dictionary
    precipitation_dict = dict(precipitation)

    # Returning as json
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def Stations():

    # Query
    stations = session.query(Measurement.station).\
                group_by(Measurement.station).all()

    # Converting to list
    stations_list = list(np.ravel(stations))

    # Returning as json
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():

    # Finding the last date
    last_date = str(session.query(Measurement.date).\
                order_by(Measurement.date.desc()).first())\
    # 1 year ago
    year_ago = (dt.datetime.strptime(last_date, "('%Y-%m-%d',)") -
                dt.timedelta(days = 365))  

    # Query
    tobs = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.date >= year_ago).all()

    # Listing
    tobs_list = list(tobs)

    # Returning as json
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start(start=None):

    # Query
    temp_start = session.query(func.min(Measurement.tobs),\
                func.avg(Measurement.tobs),\
                func.max(Measurement.tobs)).\
                filter(Measurement.date >= start)

    # Listing
    temp_start_list = list(temp_start)

    # Returning json
    return jsonify(temp_start_list)

@app.route("/api/v1.0/<start>/<end>")
def end(start=None, end=None):

    # Query
    temp_between = session.query(func.min(Measurement.tobs),\
                func.avg(Measurement.tobs),\
                func.max(Measurement.tobs)).\
                filter(Measurement.date >= start,\
                    Measurement.date <= end)

    # List
    temp_between_list = list(temp_between)

    # json
    return jsonify(temp_between_list)

if __name__ == "__main__":
    app.run(debug=True)