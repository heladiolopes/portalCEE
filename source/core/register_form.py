from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField, SelectField


class RegisterForm(Form):
    first_name = StringField('Nome', [validators.Length(min=1, max=30)])

    last_name = StringField('Sobrenome', [validators.Length(min=1, max=70)])

    email = StringField('Email', [validators.Length(min=6, max=80)])

    username = StringField('Usuário', [validators.Length(min=4, max=25)])

    password = PasswordField('Senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])

    confirm = PasswordField('Corfirmar senha')

    course = SelectField('Curso', choices=[
        ('aer', 'Engenharia Aeronáutica'),
        ('aesp', 'Engenharia Aeroespacial'),
        ('civil', 'Engenharia Civil-Aeronáuica'),
        ('comp', 'Engenharia de Computaçãp'),
        ('ele', 'Engenharia Eletrônica'),
        ('mec', 'Engenharia Mecânica-Aeronáutica')
    ])

    year = IntegerField('Ano de Formatura', [validators.NumberRange(min=2015, max=2030)])
