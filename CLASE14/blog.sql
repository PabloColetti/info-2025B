-- Esto es un comentario
CREATE TABLE posts (
	id SERIAL PRIMARY KEY,
	titulo VARCHAR(200) NOT NULL,
	contenido TEXT NOT NULL,
	fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	-- usuario_id INT NOT NULL REFERENCES usuarios(id)
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

ALTER TABLE posts
ADD COLUMN usuario_id INT REFERENCES usuarios(id);

ALTER TABLE posts
DROP COLUMN usuario_id;

SELECT * FROM posts;

UPDATE posts
SET usuario_id = 1
WHERE id = 3;

INSERT INTO posts (titulo, contenido)
VALUES
	('Tercer post', 'Contenido del tercer post');

ALTER TABLE posts
ALTER COLUMN usuario_id SET NOT NULL;

INSERT INTO posts (titulo, contenido, usuario_id)
VALUES
	('Cuarto post', 'Contenido del cuarto post', 2);




SELECT * FROM usuarios;

CREATE TYPE user_status_enum AS ENUM ('ACTIVE', 'INACTIVE');

ALTER TABLE usuarios
ADD COLUMN estado user_status_enum DEFAULT 'ACTIVE';

ALTER TYPE user_status_enum ADD VALUE 'PENDING';


