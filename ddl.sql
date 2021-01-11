-- SEQUENCE: public.user_details_id_seq

-- DROP SEQUENCE public.user_details_id_seq;

CREATE SEQUENCE public.user_details_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.user_details_id_seq
    OWNER TO postgres;
    
-- Table: public.user_details

-- DROP TABLE public.user_details;

CREATE TABLE public.user_details
(
    id integer NOT NULL DEFAULT nextval('user_details_id_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    passwd text COLLATE pg_catalog."default" NOT NULL,
    email text COLLATE pg_catalog."default",
    phone text COLLATE pg_catalog."default",
    CONSTRAINT user_details_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.user_details
    OWNER to postgres;