from flask import Flask, g, redirect, render_template, request, url_for
import sqlite3
app = Flask(__name__)

db_location = 'var/cw.db'

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect(db_location)
        g.db = db
    return db

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

class Driver:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class Blade:
    def __init__(self, role, name, element, weapon, desc):
        self.role = role
        self.name = name
        self.element = element
        self.weapon = weapon
        self.desc = desc

@app.route('/')
def index ():
    db = get_db()
    test = Driver("Rex", "Test driver")

    return render_template('home.html')

@app.route('/drivers')
def drivers():
    drivernames = []
    db = get_db()
    sql = "SELECT name FROM drivers"
    for row in db.cursor().execute(sql):
        drivernames.append(row[0])

    return render_template('driverList.html', names=drivernames)

@app.route('/drivers/<drivername>')
def drivername(drivername):
    db = get_db()
    sql = "SELECT * FROM drivers WHERE name=:name"
    result = db.cursor().execute(sql, {"name":drivername}).fetchone()
    thisDriver = Driver(result[0], result[1])

    return render_template('DriverDesc.html', driver=thisDriver)


@app.route('/blades')
def blades():
    bladenames = []
    db = get_db()
    sql = "SELECT name FROM blades"
    for row in db.cursor().execute(sql):
        bladenames.append(row[0])

    return render_template('bladenames.html', names=bladenames)


@app.route('/blades/<bladename>')
def blade_name(bladename):
    db = get_db()
    sql = "SELECT * FROM blades WHERE name=:name"
    result = db.cursor().execute(sql, {"name":bladename}).fetchone()
    thisBlade = Blade(result[0], result[1], result[2], result[3], result[4])

    return render_template('BladeDesc.html', blade=thisBlade)

@app.route('/blades/roles')
def roles():
    roles = set()
    db = get_db()
    sql = "SELECT role FROM blades"
    for row in db.cursor().execute(sql):
        roles.add(row[0])

    return render_template("roleList.html", names=roles)

@app.route('/blades/roles/<role>')
def rolelist(role):
    blades = []
    db = get_db()
    sql = "SELECT name FROM blades WHERE role=:role"
    result = db.cursor().execute(sql, {"role": role })
    for row in result:
        blades.append(row[0])

    return render_template("bladenames.html", names=blades)

@app.route('/blades/weapons')
def weapons():
    weapon = set()
    db = get_db()
    sql = "SELECT weapon FROM blades"
    for row in db.cursor().execute(sql):
        weapon.add(row[0])

    return render_template("weaponList.html", names=weapon)

@app.route('/blades/weapons/<weapon>')
def weaponlist(weapon):
    blades = []
    db = get_db()
    sql = "SELECT name FROM blades WHERE weapon=:weapon"
    result = db.cursor().execute(sql, {"weapon": weapon })
    for row in result:
        blades.append(row[0])

    return render_template("bladenames.html", names=blades)


@app.route('/blades/element')
def element():
    elements = set()
    db = get_db()
    sql = "SELECT element FROM blades"
    for row in db.cursor().execute(sql):
        elements.add(row[0])

    return render_template("elementList.html", names=elements)

@app.route('/blades/element/<element>')
def elementlist(element):
    blades = []
    db = get_db()
    sql = "SELECT name FROM blades WHERE element=:element"
    result = db.cursor().execute(sql, {"element": element })
    for row in result:
        blades.append(row[0])

    return render_template("bladenames.html", names=blades)

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        bladeName = request.form['bladename']
        bladeRole = request.form['role']
        bladeElement = request.form['element']
        bladeWeapon = request.form['weapon']
        bladeDesc = request.form['description']
        print(bladeName, bladeRole, bladeElement, bladeWeapon, bladeDesc)


        db = get_db()
        sql = "INSERT INTO blades VALUES(?,?,?,?,?)"
        db.cursor().execute(sql,(bladeRole, bladeName, bladeElement, bladeWeapon, bladeDesc))
        db.commit()



        return redirect(url_for('index'))

    return render_template('input.html')
