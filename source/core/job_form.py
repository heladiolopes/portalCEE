from wtforms import Form, StringField, validators, TextAreaField
from wtforms.fields.html5 import EmailField


class JobForm(Form):
    title = StringField('Título da vaga', [validators.Length(min=1, max=70)])

    local = TextAreaField('Empresa', [validators.Length(min=4)])

    email = EmailField('Email', [
        validators.DataRequired(),
        validators.Email(message="Email inválido")
    ])

    jobDescription = TextAreaField('Descrição da vaga', [validators.Length(min=3)])