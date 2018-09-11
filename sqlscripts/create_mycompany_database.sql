-- Database: MyCompany

-- DROP DATABASE "MyCompany";

CREATE DATABASE "MyCompany"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Table: public.product

-- DROP TABLE public.product;

CREATE TABLE public.product
(
    deleted boolean NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    id integer NOT NULL DEFAULT nextval('product_id_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    active boolean NOT NULL,
    product_type_id integer,
    CONSTRAINT product_pkey PRIMARY KEY (id),
    CONSTRAINT product_type_fk FOREIGN KEY (product_type_id)
        REFERENCES public.product_type (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.product
    OWNER to postgres;

-- Index: fki_ProductTypeFK

-- DROP INDEX public."fki_ProductTypeFK";

CREATE INDEX "fki_ProductTypeFK"
    ON public.product USING btree
    (product_type_id)
    TABLESPACE pg_default;

-- Table: public.product_type

-- DROP TABLE public.product_type;

CREATE TABLE public.product_type
(
    id integer NOT NULL DEFAULT nextval('product_type_id_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    deleted boolean NOT NULL,
    CONSTRAINT product_type_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.product_type
    OWNER to postgres;


-- Database: MyCompanyWarehouse

-- DROP DATABASE "MyCompanyWarehouse";

CREATE DATABASE "MyCompanyWarehouse"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;


 -- Table: public.dim_product

-- DROP TABLE public.dim_product;

CREATE TABLE public.dim_product
(
    id integer NOT NULL DEFAULT nextval('dim_product_id_seq'::regclass),
    application_product_id integer,
    application_product_type_id integer,
    product_type_name text COLLATE pg_catalog."default",
    product_type_description text COLLATE pg_catalog."default",
    product_name text COLLATE pg_catalog."default",
    product_description text COLLATE pg_catalog."default",
    CONSTRAINT dim_product_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.dim_product
    OWNER to postgres;

CREATE USER "Gene" WITH
  LOGIN
  SUPERUSER
  INHERIT
  CREATEDB
  CREATEROLE
  REPLICATION;