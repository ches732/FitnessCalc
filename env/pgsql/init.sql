CREATE ROLE habrkirill
    LOGIN
    PASSWORD 'qwerty'
    SUPERUSER
    NOINHERIT
    NOCREATEDB
    NOCREATEROLE
    NOREPLICATION;

ALTER ROLE habrkirill IN DATABASE habrdb SET search_path = habrdb;
CREATE SCHEMA habrdb;

ALTER SCHEMA habrdb
    OWNER TO  habrdb;
