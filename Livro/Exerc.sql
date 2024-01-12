CREATE TABLE livro (
    ISBN VARCHAR(255),
    titulo_livro VARCHAR(255),
    autor_livro VARCHAR(255),
    sexo_autor VARCHAR(255),
    paginas_livro INT,
    editora VARCHAR(255),
    ano_publicado INT, 
    estado_publicacao VARCHAR(255),
    valor_venda DECIMAL(10, 2)
);

INSERT INTO livro VALUES('12345678901', 'Cavaleiro Real','Ana Claudia','F',465,'Atlas',2009,'RJ',49.9);
INSERT INTO livro VALUES('19876543219','SQL para leigos','João Nunes','M',450,'Addison',2018,'SP',98);
INSERT INTO livro VALUES('91234567891','Receitas Caseiras','Celia Tavares','F',210,'Atlas',2008,'RJ',45.05);
INSERT INTO livro VALUES('59123456789','Pessoas Efetivas','Eduardo Santos','M',390,'Beta',2018,'RJ',78);
INSERT INTO livro VALUES('31234567890','Habitos Saudáveis','Eduardo Santos','M',630,'Beta',2019,'RJ',150);
INSERT INTO livro VALUES('49123589071','A Casa Marrom','Hermes Macedo','M',250,'Bubba',2016,'MG',60);
INSERT INTO livro VALUES('53467123456','Estacio Querido','Geraldo Francisco','M',310,'Insignia',2015,'ES',100);
INSERT INTO livro VALUES('69128975234','Pra sempre amigas','Leda Silva','F',510,'Insignia',2011,'ES',78.16);
INSERT INTO livro VALUES('57193495189','Copas Inesqueciveis','Marco Alcantara','M',200,'Larson',2018,'RS',130);
INSERT INTO livro VALUES('87642345678','O poder da mente','Clara Mafra','F',120,'Continental',2017,'SP',56);

SELECT * FROM livro;

SELECT titulo_livro, estado_publicacao FROM livro WHERE sexo_autor = 'M';

SELECT titulo_livro, editora FROM livro WHERE sexo_autor = 'F' AND estado_publicacao = 'SP';

SELECT titulo_livro, editora, ano_publicado FROM livro WHERE sexo_autor = 'M' AND (estado_publicacao = 'RJ' OR estado_publicacao = 'SP');