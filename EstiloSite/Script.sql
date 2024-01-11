CREATE TABLE consumidor (
    nome VARCHAR(50),
    sexo CHAR(1),
    email VARCHAR(50),
    cpf INT(11),
    cpf VARCHAR(14),
    fone VARCHAR(20),
    endereco VARCHAR(100)
);

INSERT INTO consumidor VALUES
    ('JOAO','M','JOAO@GMAIL.COM',988638273,'22923110','MAIA LACERDA - ESTACIO - RIO DE JANEIRO - RJ'), 
    ('CELIA','F','CELIA@GMAIL.COM',541521456,'25078869','RIACHUELO - CENTRO - RIO DE JANEIRO - RJ'),
    ('JORGE','M',NULL,885755896,'58748895','OSCAR CURY - BOM RETIRO - PATOS DE MINAS - MG'),
    ('ANA','F','ANA@GLOBO.COM',85548962,'548556985','PRES ANTONIO CARLOS - CENTRO - SAO PAULO - SP'),
    ('CARLA','F','CARLA@TERATI.COM.BR',7745828,'66587458','SAMUEL SILVA - CENTRO - BELO HORIZONTE - MG');