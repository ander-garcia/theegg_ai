# Aprendamos un poco de SQL

Theegg AI Academy

# Tareas realizadas

-SELECT \* FROM users;

Seleccionar todos los registros de la tabla

-SELECT \* FROM mailing_list;

Seleccionar todos los registros de la tabla

-SELECT FirstName, Surname, Downloads FROM users;

Seleccionar los tres campos que se piden de la tabla

-SELECT Usernmae, JoinedOn FROM members;

Seleccionar los dos campos que se piden de la tabla

-SELECT DISTINCT Name FROM members;

Seleccionar el campo nombre sin valores duplicados

-SELECT \* FROM users ORDER BY Email;

Seleccioanr todos los regsitros ordenados por el campo Email

--SELECT \* FROM subscribers ORDER BY SubscriptionDate DESC;

Seleccioanr todos los regsitros ordenados por el campo SubscriptionDate en orden descendente

-SELECT DISTINCT EmailAddress, LastName, FirstName FROM mailing_list ORDER BY EmailAddress DESC;

Seleccionar los tres campos eliminando duplicados y ordenando por el campo EmailAddress en orden descendente

-SELECT GivenName, Joined FROM mailing_list ORDER BY Joined, GivenName DESC;

Seleccionar los dos campos ordenados primero por el campo Joined en orden ascendente, y luego por el campo GivenName en orden descendente
