from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from source.core.register_form import RegisterForm
from source.jobs import Jobs

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '070498'
app.config['MYSQL_DB'] = 'ceePortalDB'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MYSQL
mysql = MySQL(app)

# Página do portal de vagas
Jobs = Jobs()


# Redirecionando para homepage
@app.route('/')
def index():
    return redirect(url_for('home'))


# Home page do site
@app.route('/home')
def home():
    return render_template("home.html")


# Página de registro do usuário
# @app.route('/register')
# def register():
#     return render_template("register.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        first = form.first_name.data
        last = form.last_name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        course = form.course.data
        year = form.year.data

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute(
            "INSERT INTO users(first_name, last_name, email, username, password, course, year) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6})".format(
                first, last, email, username, password, course, year))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        # flash('You are now registered and can log in', 'success')

        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/jobs')
def jobs():
    return render_template("jobs.html", jobs=Jobs)


# Página de cada vaga
@app.route('/jobs/<string:empresa>')
def company(empresa):
    return render_template("company.html", empresa=empresa)


if __name__ == '__main__':
    app.secret_key('super motherfucker secret key')
    app.run(debug=True)
