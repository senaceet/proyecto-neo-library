-- 1 listado de clientes
SELECT 
    document_user AS Documento,
    first_name AS Nombre1,
    sec_name AS Nombre2,
    surname AS apellido1,
    sec_surname AS apellido2,
    email AS correo,
    cell_phone AS telefono
FROM
    neo_library.cliient c
        JOIN
    neo_library.useer u ON c.fk_id_user = u.document_user;
-- 2 todos los libros  con sus editoriales
SELECT 
    title AS titulo,
    availability AS diponivilidad,
    coments AS comentarios,
    name_editorial AS editorial
FROM
    neo_library.book b
        JOIN
    neo_library.editorial e ON b.fk_Editorial = e.id_editorial;
--  3 libros por editorial
SELECT 
    title AS titulo,
    availability AS diponivilidad,
    coments AS comentarios,
    name_editorial AS editorial
FROM
    neo_library.book b
        JOIN
    neo_library.editorial e ON b.fk_Editorial = e.id_editorial
WHERE
    b.fk_Editorial = 01;
-- 4 Libros con todos sus datos
SELECT 
    id_book AS id_libro,
    barcode AS codigo_barras,
    title AS titulo,
    availability AS disponivilidad,
    coments AS comentarios,
    name_editorial editorial,
    name_writer AS escritor
FROM
    neo_library.book b
        JOIN
    neo_library.book_writer bw ON b.id_book = bw.fk_id_book
        JOIN
    neo_library.writer w ON bw.fk_id_writer = w.id_writer
        JOIN
    neo_library.editorial e ON b.fk_Editorial = e.id_editorial;
-- 5 prestamos activos 
SELECT 
    id_loan, date_loan, return_date, coment, document_user
FROM
    neo_library.loan l
        JOIN
    neo_library.cliient c ON l.fk_id_client = c.id_client
        JOIN
    neo_library.useer u ON c.fk_id_user = u.document_user
WHERE
    l.current_state = 1;
-- 6 prestamos No activos
SELECT 
    id_loan, date_loan, return_date, coment, document_user
FROM
    neo_library.loan l
        JOIN
    neo_library.cliient c ON l.fk_id_client = c.id_client
        JOIN
    neo_library.useer u ON c.fk_id_user = u.document_user
WHERE
    l.current_state = 2;
-- 7 clientes prestamos
SELECT 
    id_loan, date_loan, return_date, coment, document_user
FROM
    neo_library.loan l
        RIGHT JOIN
    neo_library.cliient c ON l.fk_id_client = c.id_client
        RIGHT JOIN
    neo_library.useer u ON c.fk_id_user = u.document_user;
-- 8 libros disponibles
SELECT 
    title AS libro, coments AS comentario
FROM
    neo_library.book
WHERE
    availability = 1;
-- 9 libros no disponibles
SELECT 
    title AS libro, coments AS comentario
FROM
    neo_library.book
WHERE
    availability = 2;
-- 10 libros - prestamo
SELECT 
    title, id_loan
FROM
    neo_library.book b
        JOIN
    neo_library.book_loan bl ON b.id_book = bl.fk_id_book
        JOIN
    neo_library.loan l ON bl.fk_id_loan = l.id_loan;
-- 11 libros - prestamo aunque no esten en ningun prestamo
SELECT 
    title, id_loan
FROM
    neo_library.book b
        LEFT JOIN
    neo_library.book_loan bl ON b.id_book = bl.fk_id_book
        LEFT JOIN
    neo_library.loan l ON bl.fk_id_loan = l.id_loan;
-- 12 prestamos vencidos
SELECT 
    id_loan, document_user, title
FROM
    neo_library.loan l
        JOIN
    neo_library.cliient c ON l.fk_id_client = c.id_client
        JOIN
    neo_library.useer u ON c.fk_id_user = u.document_user
        JOIN
    neo_library.book_loan bl ON l.id_loan = bl.fk_id_loan
        JOIN
    neo_library.book b ON bl.fk_id_book = b.id_book
WHERE
    l.current_state = 1
        AND l.return_date < '2020-10-01';
-- 13 libros que comienzen por una letra especifica
SELECT 
    title AS libro
FROM
    neo_library.book
WHERE
    title LIKE 'E%';
-- 14 libros por genero
SELECT 
    title AS libro, name_genre AS genero
FROM
    neo_library.book b
        JOIN
    neo_library.book_genre bg ON b.id_book = bg.fk_id_book
        JOIN
    neo_library.genre g ON bg.fk_id_genre = g.id_genre;
-- 15 prestamos hechos en una fecha en un mes especifico
SELECT 
    id_loan, id_client, title, date_loan, return_date
FROM
    neo_library.loan l
        JOIN
    neo_library.book_loan bl ON l.id_loan = bl.fk_id_loan
        JOIN
    neo_library.book b ON bl.fk_id_book = b.id_book
        JOIN
    neo_library.cliient c ON l.fk_id_client = c.id_client
WHERE
    l.date_loan LIKE '2020-07%';
-- 16 prestamos de un cliente
SELECT 
    id_loan, id_client, title, date_loan, return_date
FROM
    neo_library.loan l
        JOIN
    neo_library.book_loan bl ON l.id_loan = bl.fk_id_loan
        JOIN
    neo_library.book b ON bl.fk_id_book = b.id_book
        JOIN
    neo_library.cliient c ON l.fk_id_client = c.id_client
WHERE
    c.id_client = 1005;
-- 17 prestamos por tipo de documento cc
SELECT 
    id_loan,
    document_user,
    acronym_doc,
    title,
    date_loan,
    return_date
FROM
    neo_library.loan l
        JOIN
    neo_library.book_loan bl ON l.id_loan = bl.fk_id_loan
        JOIN
    neo_library.book b ON bl.fk_id_book = b.id_book
        JOIN
    neo_library.cliient c ON l.fk_id_client = c.id_client
        JOIN
    neo_library.useer u ON c.fk_id_user = u.document_user
        JOIN
    neo_library.document_type d ON u.fk_type_document = d.id_type_document
WHERE
    u.fk_type_document = 01;
-- 18 prestamos por tipo de documento TI
SELECT 
    id_loan,
    document_user,
    acronym_doc,
    title,
    date_loan,
    return_date
FROM
    neo_library.loan l
        JOIN
    neo_library.book_loan bl ON l.id_loan = bl.fk_id_loan
        JOIN
    neo_library.book b ON bl.fk_id_book = b.id_book
        JOIN
    neo_library.cliient c ON l.fk_id_client = c.id_client
        JOIN
    neo_library.useer u ON c.fk_id_user = u.document_user
        JOIN
    neo_library.document_type d ON u.fk_type_document = d.id_type_document
WHERE
    u.fk_type_document = 02;
-- 19 prestamos por tipo de documento CE
SELECT 
    id_loan,
    document_user,
    acronym_doc,
    title,
    date_loan,
    return_date
FROM
    neo_library.loan l
        JOIN
    neo_library.book_loan bl ON l.id_loan = bl.fk_id_loan
        JOIN
    neo_library.book b ON bl.fk_id_book = b.id_book
        JOIN
    neo_library.cliient c ON l.fk_id_client = c.id_client
        JOIN
    neo_library.useer u ON c.fk_id_user = u.document_user
        JOIN
    neo_library.document_type d ON u.fk_type_document = d.id_type_document
WHERE
    u.fk_type_document = 03;
-- 20 prestamos por tipo de documento PAS
SELECT 
    id_loan,
    document_user,
    acronym_doc,
    title,
    date_loan,
    return_date
FROM
    neo_library.loan l
        JOIN
    neo_library.book_loan bl ON l.id_loan = bl.fk_id_loan
        JOIN
    neo_library.book b ON bl.fk_id_book = b.id_book
        JOIN
    neo_library.cliient c ON l.fk_id_client = c.id_client
        JOIN
    neo_library.useer u ON c.fk_id_user = u.document_user
        JOIN
    neo_library.document_type d ON u.fk_type_document = d.id_type_document
WHERE
    u.fk_type_document = 04;