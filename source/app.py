
from flask import Flask, render_template
from jobs import Jobs



app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

#Página do portal de vagas
Jobs = Jobs()
@app.route('/jobs')
def jobs():
    return render_template("jobs.html", jobs = Jobs)

#Página de cada vaga
@app.route('/jobs/<string:empresa>')
def company(empresa):
    return render_template("company.html", empresa=empresa)

if __name__ == '__main__':
    app.run(debug=True)
