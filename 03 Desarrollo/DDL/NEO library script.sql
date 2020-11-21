create database NEO_LIBRARY;
use  NEO_LIBRARY;
CREATE TABLE genre (
    id_genre INT(7) NOT NULL PRIMARY KEY,
    name_genre VARCHAR(20) NOT NULL
);
CREATE TABLE Editorial (
    id_editorial INT(7) NOT NULL PRIMARY KEY,
    name_editorial VARCHAR(20) NOT NULL
);
CREATE TABLE writer (
    id_writer INT(10) NOT NULL PRIMARY KEY,
    name_writer VARCHAR(25) NOT NULL
);
CREATE TABLE document_type (
    id_type_document INT(5) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nomb_type_document VARCHAR(20) NOT NULL,
    acronym_doc VARCHAR(10) NOT NULL
);
CREATE TABLE useer (
    ID_user INT(8) NOT NULL,
    document_user INT(19) NOT NULL,
    fk_type_document INT(5) NOT NULL,
    first_name VARCHAR(12) NOT NULL,
    sec_name VARCHAR(12),
    surname VARCHAR(15) NOT NULL,
    sec_surname VARCHAR(15),
    cell_phone VARCHAR(16) NOT NULL,
    PRIMARY KEY (ID_user , document_user , fk_type_document)
);
CREATE TABLE cliient (
    id_client INT(8) NOT NULL,
    fk_id_user INT(8) NOT NULL,
    observation TEXT,
    PRIMARY KEY (id_client , fk_id_user)
);
CREATE TABLE admin (
    id_admin INT(8) NOT NULL,
    fk_id_user INT(8) NOT NULL,
    password_ad VARCHAR(20) NOT NULL,
    PRIMARY KEY (id_admin , fk_id_user)
);
CREATE TABLE loan (
    id_loan INT(11) NOT NULL PRIMARY KEY,
    date_loan DATETIME NOT NULL,
    return_date DATETIME NOT NULL,
    current_stade TINYINT(5) NOT NULL,
    coment TEXT,
    fk_id_client INT(8) NOT NULL
);
CREATE TABLE book (
    id_book INT(12) NOT NULL PRIMARY KEY,
    title VARCHAR(45) NOT NULL,
    availability TINYINT(4) NOT NULL,
    physical_conditions TEXT NOT NULL,
    fk_Editorial INT(7) NOT NULL
);
CREATE TABLE book_loan (
    fk_id_loan INT(11) NOT NULL,
    fk_id_book INT(12) NOT NULL,
    PRIMARY KEY (fk_id_loan , fk_id_book)
);
CREATE TABLE book_genre (
    fk_id_genre INT(7) NOT NULL,
    fk_id_book INT(12) NOT NULL,
    PRIMARY KEY (fk_id_genre , fk_id_book)
);
CREATE TABLE book_writer (
    fk_id_writer INT(10) NOT NULL,
    fk_id_book INT(12) NOT NULL,
    PRIMARY KEY (fk_id_writer , fk_id_book)
);
alter table useer add foreign key (fk_type_document) references document_type (id_type_document);
alter table cliient add foreign key (fk_id_user) references useer (ID_user);
alter table admin add foreign key (fk_id_user) references useer (ID_user);
alter table loan add foreign key (fk_id_client) references cliient (id_client);
alter table book add foreign key (fk_Editorial) references Editorial (id_editorial);
alter table book_loan add foreign key (fk_id_loan) references loan (id_loan);
alter table book_loan add foreign key (fk_id_book) references book (id_book);
alter table book_genre add foreign key (fk_id_genre) references genre (id_genre);
alter table book_genre add foreign key (fk_id_book) references book (id_book);
alter table book_writer add foreign key (fk_id_writer) references writer (id_writer);
alter table book_writer add foreign key (fk_id_book) references book (id_book);