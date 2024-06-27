import sqlite3

conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

comandos_sql = [
    """
    CREATE TABLE IF NOT EXISTS ALUNO (
        ID INT PRIMARY KEY,
        Nome VARCHAR(100),
        Matricula INT,
        Email VARCHAR(100),
        Endereco VARCHAR(255),
        Telefone VARCHAR(20)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS LIVRO (
        Cod_Livro INT PRIMARY KEY,
        Titulo VARCHAR(255),
        Autor VARCHAR(100),
        Cod_Sessao INT,
        FOREIGN KEY (Cod_Sessao) REFERENCES SESSAO(Codigo)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS SESSAO (
        Codigo INT PRIMARY KEY,
        Descricao VARCHAR(100),
        Localizacao VARCHAR(100)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS EMPRESTIMO (
        Codigo INT PRIMARY KEY,
        Data_hora DATETIME,
        Matric_Aluno INT,
        Data_devolucao DATE,
        FOREIGN KEY (Matric_Aluno) REFERENCES ALUNO(Matricula)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS LIVRO_EMPRESTIMO (
        Cod_Livro INT,
        Cod_Emprestimo INT,
        PRIMARY KEY (Cod_Livro, Cod_Emprestimo),
        FOREIGN KEY (Cod_Livro) REFERENCES LIVRO(Cod_Livro),
        FOREIGN KEY (Cod_Emprestimo) REFERENCES EMPRESTIMO(Codigo)
    );
    """
]

for comando in comandos_sql:
    cursor.execute(comando)

conexao.commit()

conexao.close()

#final
