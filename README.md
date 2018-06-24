# Portal de Vagas CEE

Projeto proposto para a disciplina de CES-22 no ITA. Portal de vagas
para que os alunos de graduação possam localizar mais facilmente
vagas de estágio, summer, emprego...


## Estrutura do diretório.

```
.
└── portalCEE
    ├── documentation           # Uso, guias e organização de arquivos.
    └── source                  # Diretório principal do código.
        ├── core                #
        └── static              # Arquivos auxiliares para construção de páginas
            ├── css                 # Configurações css
            └── img                 # Imagens
        └── templates           # Templates html para páginas
```


## Dependências

Para o correto funionamento do código algumas dependências são necessárias.

- flask
- flask-MySQLdb
- flask-WTF
- wtforms
- mysqlclient
- passlib
- flask-Mail

Para instalar as dependências, execute no terminal

```sh
$ sudo pip install nomeDaDependencia
```

## Execução

Após instalar todas as depêndencias, execute no terminal:

```sh
$ cd source/
$ python3 app.py
```

Em seguida abra em um navegador de sua preferência:

```
http://127.0.0.1:5000/
```
ou
```
http://localhost:5000/
```
