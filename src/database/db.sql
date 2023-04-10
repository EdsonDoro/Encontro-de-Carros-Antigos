CREATE DATABASE IF NOT EXISTS ENCONTRO;
use ENCONTRO;

CREATE TABLE IF NOT EXISTS veiculos(
    codigo int(4) not null,
    placa char(7) not null,
    modelo char(30) not null,
    responsavel char(15) not null,
    id_encontro tinyint null,
    primary key(codigo)
);

CREATE TABLE IF NOT EXISTS encontro(
    id_encontro tinyint not null,
    nome_encontro char(30) not null,
    descricao char(200) not null,
    data_encontro date not null,
    primary key(id_encontro)
);

alter table veiculos add foreign key (id_encontro) references encontro(id_encontro);