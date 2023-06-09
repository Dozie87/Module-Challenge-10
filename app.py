import numpy as np
import datetime as dt

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


engine = create_engine("sqlite:////Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine)

measurement = Base.classes.measurement
station = Base.classes.station

session = session(engine)

app =Flask(_name_)

@app.route ("/")
def welcome():
    return(
        f"Welcome to Hawaii Climate Analysis API<br/>",
        f"Available Routes:<br/>",
        f"/api/v1.0/precipitation<br/>",
        f"/api/v1.0/stations<br/>",
        f"/api/v1.0/tobs<br/>",
        f"/api/v1.0/temp/start<br/>",
        f"/api/v1.0/temp/start/end<br/>",
        f"<p>'start' and 'end' date should be in the format MMDDYYYY.</P>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year =dt.date(2017,8,23) - dt.timedelta(days=365)

    precipitation = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= prev_year).all()

    session.close()
    precip = {date: prcp for date, prcp in precipitation}

    return jsonify(precip)


if _name_ == "_main_":
    app.run(debug=True)

