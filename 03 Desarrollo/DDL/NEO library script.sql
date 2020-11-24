create database NEO_LIBRARY;
use  NEO_LIBRARY;
CREATE TABLE genre (
    id_genre INT(7) NOT NULL PRIMARY KEY,
    name_genre VARCHAR(20) NOT NULL
);
CREATE TABLE Editorial (
    id_editorial INT(7) NOT NULL PRIMARY KEY,
    name_editorial VARCHAR(45) NOT NULL
);
CREATE TABLE writer (
    id_writer INT(10) NOT NULL PRIMARY KEY,
    name_writer VARCHAR(35) NOT NULL
);
CREATE TABLE document_type (
    id_type_document INT(5) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nomb_type_document VARCHAR(39) NOT NULL,
    acronym_doc VARCHAR(10) NOT NULL
);
CREATE TABLE useer (
    document_user INT(19) NOT NULL,
    fk_type_document INT(5) NOT NULL,
    first_name VARCHAR(12) NOT NULL,
    sec_name VARCHAR(12),
    surname VARCHAR(15) NOT NULL,
    sec_surname VARCHAR(15),
    password_ad VARCHAR(41) NOT NULL,
    email VARCHAR(40) NOT NULL,
    address VARCHAR(25) NOT NULL,
    cell_phone bigint(16) NOT NULL,
    PRIMARY KEY (document_user , fk_type_document)
);
CREATE TABLE cliient (
    id_client INT(8) NOT NULL,
    fk_id_user INT(19) NOT NULL,
    observation TEXT,
    PRIMARY KEY (id_client , fk_id_user)
);
CREATE TABLE admin (
    id_admin INT(8) NOT NULL,
    fk_id_user INT(19) NOT NULL,
    PRIMARY KEY (id_admin , fk_id_user)
);
CREATE TABLE loan (
    id_loan INT(11) NOT NULL PRIMARY KEY,
    date_loan DATETIME NOT NULL,
    return_date DATE NOT NULL,
    current_state TINYINT(5) NOT NULL,
    coment TEXT,
    fk_id_client INT(8) NOT NULL
);
CREATE TABLE book (
    id_book VARCHAR(20) NOT NULL PRIMARY KEY,
    barcode VARCHAR(20),
    title VARCHAR(75) NOT NULL,
    availability TINYINT(4) NOT NULL,
    coments TEXT,
    fk_Editorial INT(7) NOT NULL
);
CREATE TABLE book_loan (
    fk_id_loan INT(11) NOT NULL,
    fk_id_book VARCHAR(20) NOT NULL,
    PRIMARY KEY (fk_id_loan , fk_id_book)
);
CREATE TABLE book_genre (
    fk_id_genre INT(7) NOT NULL,
    fk_id_book VARCHAR(20) NOT NULL,
    PRIMARY KEY (fk_id_genre , fk_id_book)
);
CREATE TABLE book_writer (
    fk_id_writer INT(10) NOT NULL,
    fk_id_book VARCHAR(20) NOT NULL,
    PRIMARY KEY (fk_id_writer , fk_id_book)
);
alter table useer add foreign key (fk_type_document) references document_type (id_type_document) on update cascade;
alter table cliient add foreign key (fk_id_user) references useer (document_user) on update cascade;
alter table admin add foreign key (fk_id_user) references useer (document_user) on update cascade;
alter table loan add foreign key (fk_id_client) references cliient (id_client) on update cascade;
alter table book add foreign key (fk_Editorial) references Editorial (id_editorial) on update cascade;
alter table book_loan add foreign key (fk_id_loan) references loan (id_loan) on update cascade;
alter table book_loan add foreign key (fk_id_book) references book (id_book) on update cascade;
alter table book_genre add foreign key (fk_id_genre) references genre (id_genre) on update cascade;
alter table book_genre add foreign key (fk_id_book) references book (id_book) on update cascade;
alter table book_writer add foreign key (fk_id_writer) references writer (id_writer) on update cascade;
alter table book_writer add foreign key (fk_id_book) references book (id_book) on update cascade;
CREATE TABLE log_error (
    id_error VARCHAR(15) PRIMARY KEY NOT NULL,
    description_error VARCHAR(80)
);
CREATE TABLE server_mail (
    id_mail INT(10) PRIMARY KEY NOT NULL,
    mail VARCHAR(25) NOT NULL
);