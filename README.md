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

- Flask
- Flask-MySQLdb
- Flask-WTF
- WTForms
- mysqlclient
- passlib
