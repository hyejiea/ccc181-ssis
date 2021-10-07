from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = 'ajay'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rootroot0305'
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM students")
    data = cur.fetchall()
    return render_template('index2.html', students=data )

@app.route('/course')
def course():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM course")
    data = cur.fetchall()
    return render_template('course.html', course=data)

@app.route('/college')
def college():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM college")
    data = cur.fetchall()
    return render_template('college.html', college=data)

# @app.route('/index')
# def index():
#     return render_template('index2.html')


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        ID = request.form['id']
        Firstname = request.form['firstname']
        Lastname = request.form['lastname']
        Course = request.form['course']
        Year = request.form['year']
        Gender = request.form['gender']
        cur = mysql.connection.cursor()
        cur.execute("INSERT students (Id, firstname, lastname, course, year, gender) VALUES (%s, %s, %s, %s, %s,%s)", (ID, Firstname, Lastname, Course, Year, Gender ))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/insert_course', methods = ['POST'])
def insert_course():

    if request.method == 'POST':
        flash("Data Inserted Successfully")
        code = request.form['code']
        name = request.form['name']
        college = request.form['college']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO course (code, name, college) VALUES (%s, %s, %s)", (code, name, college))
        mysql.connection.commit()
        return redirect(url_for('course'))

@app.route('/insert_college', methods = ['POST'])
def insert_college():

    if request.method == 'POST':
        flash("Data Inserted Successfully")
        code = request.form['code']
        name = request.form['name']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO course (code, name) VALUES (%s, %s)", (code, name))
        mysql.connection.commit()
        return redirect(url_for('college'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))

@app.route('/delete_course', methods = ['GET'])
def delete_course(id_course_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM course WHERE id_course=%s", (id_course_data,))
    mysql.connection.commit()
    return redirect(url_for('course'))

@app.route('/delete_college/<string:id_college_data>', methods = ['GET'])
def delete_college(id_college_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM college WHERE id_college=%s", (id_college_data))
    mysql.connection.commit()
    return redirect(url_for('college'))


@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        ID = request.form['id']
        Firstname = request.form['firstname']
        Lastname = request.form['lastname']
        Course = request.form['course']
        Year = request.form['year']
        Gender = request.form['gender']
        cur = mysql.connection.cursor()
        flash("Data Updated Successfully")
        cur.execute("""
               UPDATE students
               SET firstname=%s,
                Lastname=%s,
                 Course=%s,
                 Year=%s,
                 gender=%s
               WHERE id=%s
            """, (Firstname, Lastname, Course, Year,  Gender, ID ))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/update_course',  methods=['POST', 'GET'])
def update_course(id_course):

    if request.method == 'POST':
        Id_course = request.form['id_course']
        code = request.form['code']
        name = request.form['name']
        college = request.form['college']
        cur = mysql.connection.cursor()
        flash("Data Updated Successfully")

        cur.execute("""
               UPDATE course
               SET code=%s,
                name=%s,
                 college=%s,
               WHERE id_course=%s
            """, (code, name, college, id_course))
        mysql.connection.commit()
        return redirect(url_for('Course'))

@app.route('/update_college',methods=['POST', 'GET'])
def update_college(id_college):

    if request.method == 'POST':
        id = request.form['id_college']
        code = request.form['code']
        name = request.form['name']
        cur = mysql.connection.cursor()
        flash("Data Updated Successfully")

        cur.execute("""
               UPDATE college
               SET code=%s,
                name=%s,
               WHERE id_college=%s
            """, (code, name, id_college))
        mysql.connection.commit()
        return redirect(url_for('College'))

if __name__ == "__main__":
    app.run(debug=True)