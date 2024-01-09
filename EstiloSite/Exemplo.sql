CREATE TABLE cliente(
	id INT,
  	nome VARCHAR(80),
  	matricula INT,
  	turno CHAR
);

DESC cliente;

DROP TABLE cliente;

CREATE TABLE cliente (
	id BIGINT, 
	idade BIGINT, 
	sexo CHAR, 
	dependentes INT, 
	escolaridade VARCHAR(20), 
	tipo_cartao VARCHAR(10), 
	limite_credito DOUBLE, 
	valor_transacoes_12m DOUBLE, 
	qtd_transacoes_12m BIGINT
);

INSERT INTO cliente VALUES (768805383, 45, 'M', 3, 'ensino medio', 'blue', 12691.51, 1144.90, 42);
INSERT INTO cliente VALUES (818770008, 49, 'F', 5, 'mestrado', 'blue', 8256.96, 1291.45, 33);
INSERT INTO cliente VALUES (713982108, 51, 'M', 3, 'mestrado', 'blue', 3418.56, 1887.72, 20);

SELECT * FROM cliente;