CREATE TABLE user (
                        id serial PRIMARY KEY,
                        user_name varchar(50),
                        password varchar(50)
);

CREATE TABLE result (
                        id serial PRIMARY KEY,
                        ip_adress varchar not null,
                        gender  varchar not null,
                        bju float,
                        water float,
                        callories float
);