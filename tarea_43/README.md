# Aprendamos un poco de SQL

Estas son las consultas SQL. En las explicaciones se utiliza campo como sinónimo de columna, y regsitro como sinónimo de fila:

- SELECT \* FROM users;

Seleccionar todos los campos de todos los registros de la tabla

- SELECT \* FROM mailing_list;

Seleccionar todos los campos de todos los registros de la tabla

- SELECT FirstName, Surname, Downloads FROM users;

Seleccionar los tres campos que se piden de todos los registros de la tabla

- SELECT Usernmae, JoinedOn FROM members;

Seleccionar los dos campos que se piden de todos los registros la tabla

- SELECT DISTINCT Name FROM members;

Seleccionar el campo nombre eliminando duplicados de todos los registros de la tabla

- SELECT \* FROM users ORDER BY Email ASC;

Seleccionar todos los campos de todos los registros de la tabla, ordenados por el campo Email en orden ascendente. Si en el ORDER BY no se especifica el orden (ASC o DESC), es ascendente (ASC)

- SELECT \* FROM subscribers ORDER BY SubscriptionDate DESC;

Seleccionar todos los campos de todos los registros de la tabla, ordenados por el campo SubscriptionDate en orden descendente

- SELECT DISTINCT EmailAddress, LastName, FirstName FROM mailing_list ORDER BY EmailAddress DESC;

Seleccionar los tres campos de todos los registros de la tabla, eliminando duplicados y ordenando por el campo EmailAddress en orden descendente

- SELECT GivenName, Joined FROM mailing_list ORDER BY Joined, GivenName DESC;

Seleccionar los dos campos de todos los registros de la tabla, ordenados primero por el campo Joined en orden ascendente, y luego por el campo GivenName en orden descendente

- SELECT \* FROM mailing_list ORDER BY PromotionsSent, GivenName LIMIT 5;

Seleccionar todos los campos ordenados de los primeros cinco registros de la tabla, ordenados por los campos PromotionsSent y GivenName (ambos en orden ascendente)

- SELECT DISTINCT FamilyName, Email, GivenName FROM users ORDER BY FamilyName DESC, GIvenName LIMIT 3,

Seleccionar los 3 campos especificads, tras elimianr duplicados, de los primeros tres registros de la tabla, ordenados por FamilyName en orden descendete y GivenName en orden ascendente
