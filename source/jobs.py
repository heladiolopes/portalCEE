# Create just to test the jobs.html file
# In the final version of the project, will be use MySQL database

def Jobs():
    jobs = [
        {
            'id': 1,
            'empresa': "Ambev",
            'tipo': "Estágio",
            'descricao': "Estágio em BI",
            'inscriçao': "Até 17-05-2018"
        },
        {
            'id': 2,
            'empresa': "Rhodia",
            'tipo': "Trainee",
            'descricao': "Programa de Trainee Rhodia",
            'inscriçao': "Até 17-05-2018"
        },
        {
            'id':3,
            'empresa': "Suzano",
            'tipo': "Efetivo",
            'descricao': "Vaga de Efetivo em compras",
            'inscriçao': "Até 17-05-2018"
        }
    ]
    return jobs