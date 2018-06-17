from wtforms import Form, StringField, PasswordField, validators, IntegerField, SelectField
from wtforms.fields.html5 import EmailField


cursos = [
        ('aer', 'Engenharia Aeronáutica'),
        ('aesp', 'Engenharia Aeroespacial'),
        ('civil', 'Engenharia Civil-Aeronáuica'),
        ('comp', 'Engenharia de Computaçãp'),
        ('ele', 'Engenharia Eletrônica'),
        ('mec', 'Engenharia Mecânica-Aeronáutica')
    ]


class RegisterForm(Form):
    first_name = StringField('Nome', [validators.Length(min=1, max=30)])

    last_name = StringField('Sobrenome', [validators.Length(min=1, max=70)])

    email = EmailField('Email', [
        validators.DataRequired(),
        validators.Email(message="Email inválido")
    ])

    username = StringField('Usuário', [validators.Length(min=4, max=25)])

    password = PasswordField('Senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Senhas não correspondem')
    ])

    confirm = PasswordField('Corfirmar senha')

    course = SelectField('Curso', choices=cursos)

    year = IntegerField('Ano de Formatura', [validators.NumberRange(min=2015, max=2030)])
