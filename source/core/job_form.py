from wtforms import Form, StringField, PasswordField, validators, IntegerField, TextAreaField

class JobForm(Form):
    name = StringField('Empresa', [validators.Length(min=1, max=30)])

    job = TextAreaField('Vaga', [validators.Length(min=10)])

    yearInUniversity = TextAreaField('Ano de Formação', [validators.Length(min=3)])

    jobDescription = TextAreaField('Descrição da vaga', [validators.Length(min=3)])
