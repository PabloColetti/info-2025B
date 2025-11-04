-- Esto es un comentario
CREATE TABLE posts (
	id SERIAL PRIMARY KEY,
	titulo VARCHAR(200) NOT NULL,
	contenido TEXT NOT NULL,
	fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM posts;

INSERT INTO posts (titulo, contenido)
VALUES
	('Primer post', 'Contenido del primer post'),
	('Segudo post', 'Contenido del segundo post');

CREATE TABLE usuarios (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	email varchar(150) UNIQUE NOT NULL,
	password TEXT NOT NULL
);

SELECT * FROM usuarios;

INSERT INTO usuarios (nombre, email, password)
VALUES
	('Pablo', 'pablo@emailfalso.com', 'facil123'),
	('Elias', 'elias@emailfalso.com', 'refacil123');



