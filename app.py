from flask import Flask, render_template, redirect, request, url_for
import pandas as pd
import psycopg2
from backend.config import config, skconfig
from backend.apf import AddPassenger
from backend.dpf import DeletePassenger


app = Flask(__name__)
thekey = skconfig()
app.secret_key = thekey.get('secretkey')


params = config()
conn = psycopg2.connect(**params)


@app.route('/')
@app.route('/main')
def main():
    with open("backend/getflights.sql", 'r') as f:
        df = pd.read_sql(f.read(), conn)
    with open("backend/getpassengers.sql", 'r') as f2:
        df2 = pd.read_sql(f2.read(), conn)
    return render_template('main.html', tables = [df.to_html(classes='data', index=False)], tables2 = [df2.to_html(classes='data', index=False)])

@app.route('/flights')
def flights():
    with open("backend/getflights.sql", 'r') as f:
        df = pd.read_sql(f.read(), conn)
    return render_template('flights.html', tables=[df.to_html(classes='data')])


@app.route('/gfm')
def gfm():
    with open("backend/gfm.sql", 'r') as f:
        df = pd.read_sql(f.read(), conn)
    return render_template('getflightmanifest.html', tables=[df.to_html(classes='data', index=False)])


@app.route('/gpm')
def gpm():
    with open("backend/gpm.sql", 'r') as f:
        df = pd.read_sql(f.read(), conn)
    return render_template('getpassengermanifest.html', tables=[df.to_html(classes='data', index=False)])


@app.route('/passengers')
def passengers():
    with open("backend/getpassengers.sql", 'r') as f:
        df = pd.read_sql(f.read(), conn)
    return render_template('passengers.html', tables=[df.to_html(classes='data', index=False)])


@app.route('/addpass', methods=['GET','POST'])
def addpass():
    form = AddPassenger()
    with open("backend/getpassengers.sql", 'r') as f:
        df = pd.read_sql(f.read(), conn)
    if request.method == 'GET':
        return render_template("addpass.html", form= form, tables=[df.to_html(classes='data', index=False)])
    elif request.method == 'POST':
        if form.validate_on_submit():
            name = request.form['name']
            flightid = request.form['flightid']
            query = "Insert into passengers(name, flight_id) values ('%s','%s')"  %(name, flightid)
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
        return redirect('/')
    else:
        return render_template("addpass.html", form= form, tables=[df.to_html(classes='data')])

@app.route('/deletepass', methods=['GET','POST'])
def deletepass():
    form2 = DeletePassenger()
    with open("backend/getpassengers.sql", 'r') as f:
        df = pd.read_sql(f.read(), conn)
    if request.method == 'GET':
        return render_template("deletepass.html", form= form2, tables=[df.to_html(classes='data', index=False)])
    elif request.method == 'POST':
        if form2.validate_on_submit():
            value = request.form['id']
            query = "Delete from passengers where id =  ('%s')"  %(value)
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
        return redirect('/')
    else:
        return render_template("deletepass.html", form= form, tables=[df.to_html(classes='data')])


if __name__ == '__main__':
    app.run(debug=True)
