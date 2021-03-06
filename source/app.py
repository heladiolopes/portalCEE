# Dependências externas
from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mail import Mail, Message

# Dependências do código
from source.core.register_form import RegisterForm, cursos
from source.core.job_form import JobForm

app = Flask(__name__)
app.secret_key = 'super motherfucker secret key'

# Configuração MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '070498'
app.config['MYSQL_DB'] = 'ceePortalDB'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

# Configuração do E mail
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='ceeportalces22@gmail.com',
    MAIL_PASSWORD='ceeportal123',
)

mail = Mail(app)


# Redirecionando para homepage
@app.route('/')
def index():
    return redirect(url_for('home'))


# Homepage do site
@app.route('/home')
def home():
    return render_template("home.html")


# Página do registro de usuários
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
        linkedin = form.linkedIn.data
        year = form.year.data

        # Create cursor
        cur = mysql.connection.cursor()

        # Checking if email already exists
        if cur.execute("SELECT * FROM users WHERE email = '{0}'".format(email)) > 0:
            flash('Email already registered.', 'danger')
            return redirect(url_for('register'))

        # Sending email
        msg = mail.send_message(
            'Confirmação',
            sender='ceeportalces22@gmail.com',
            recipients=[email],
            html="<h4>Confirmação de cadastro</h4>"
                 "<hr>"
                 "<p>Olá {0},</p>"
                 "<p>Seu cadastro foi realizado com sucesso!</p>".format(first)
        )

        # Execute query
        cur.execute(
            "INSERT INTO users(first_name, last_name, email, username, password, course, year, linkedin) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6}, '{7}')".format(
                first, last, email, username, password, course, year, linkedin))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('index'))
    return render_template('register.html', form=form)


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form fields
        email = request.form['email']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user username
        result = cur.execute("SELECT * FROM users WHERE email = '{0}'".format(email))
        if result > 0:
            data = cur.fetchone()
            password = data['password']
            # Close connection
            cur.close()

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['f_name'] = data['first_name']
                session['l_name'] = data['last_name']
                session['email'] = data['email']
                session['username'] = data['username']
                for c in cursos:
                    if c[0] == data['course']:
                        session['course'] = c[1]

                session['linkedin'] = data['linkedin']
                session['year'] = data['year']

                flash('You are now logged in', 'success')
                return redirect(url_for('profile'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)

        else:
            error = "Username not found"
            return render_template('login.html', error=error)

    return render_template('login.html')


# Add job
@app.route('/sendjob', methods=['GET', 'POST'])
def sendjob():
    form = JobForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        local = form.local.data
        email = form.email.data
        jobDescription = form.jobDescription.data

        # Create a cursor
        cur = mysql.connection.cursor()

        # execute
        cur.execute(
            "INSERT INTO companies(title, local, email, job_description) VALUES('{0}', '{1}', '{2}', '{3}')".format(
                title, local, email, jobDescription))

        # commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Thank you to send your opportunity to ITA', 'success')

        return redirect(url_for('index'))

    return render_template('sendjob.html', form=form)


# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))

    return wrap


# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


@app.route('/profile')
@is_logged_in
def profile():
    return render_template('profile.html')


# Show the available jobs
@app.route('/jobs')
@is_logged_in
def jobs():
    # Create a cursor
    cur = mysql.connection.cursor()

    # Get jobs
    result = cur.execute("SELECT * FROM companies ORDER BY register_date ASC")

    Jobs = cur.fetchall()

    if result > 0:
        return render_template("jobs.html", jobs=Jobs)
    else:
        msg = 'There no jobs available right now'
        return render_template("jobs.html", msg=msg)

    cur.close()


# Show a specific job
@app.route('/jobs/<string:vaga>')
@is_logged_in
def company(vaga):
    # Create a cursor
    cur = mysql.connection.cursor()

    # Get job
    result = cur.execute("SELECT * FROM companies WHERE title = %s", [vaga])

    job = cur.fetchone()

    return render_template("company.html", company=job)


if __name__ == '__main__':
    app.run(debug=True)
