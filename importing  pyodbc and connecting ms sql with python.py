import pyodbc
import pandas as pd
import flask,jsonify
from flask import Flask 
from sqlalchemy import create_engine
import datetime
import decimal
import json
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
def default(x):
    if isinstance(x, (datetime.date, datetime.datetime)):
        return x.isoformat()

server  = 'DESKTOP-OC44QC1'
database = 'saipavan'
username = 'sa'
password = 'admin'

conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
)
sql="SELECT * FROM student_table"
mycursor=conn.cursor()
mycursor.execute(sql)
myresult=mycursor.fetchall()
print (myresult)


@app.route('/utresults', methods=['GET'])
def get_tasks3():
    cursor = conn.cursor()
    result = cursor.execute(
        "select top 50 * from student_table")
    query_results = [dict(zip([column[0] for column in result.description], row)) for row in result.fetchall()]

    response = json.dumps({'items': query_results},
                          sort_keys=True,
                          indent=1,
                          default=default, )

    return response

@app.route('/results', methods=['GET'])
def get_tasks4():
    cursor = conn.cursor()

    result = cursor.execute(
        "select top 50 * from student_table")
    query_results = [dict(zip([column[0] for column in result.description], row)) for row in result.fetchall()]

    response = json.dumps({'items': query_results},
                          sort_keys=True,
                          indent=1,
                          default=default, )

    return response

