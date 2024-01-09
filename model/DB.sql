CREATE TABLE cliente (
  id BIGINT, 
  idade INT, 
  sexo CHAR, 
  dependentes INT, 
  escolaridade VARCHAR(20), 
  tipo_cartao VARCHAR(10), 
  limite_credito DOUBLE, 
  valor_transacoes_12m DOUBLE, 
  qtd_transacoes_12m BIGINT
);