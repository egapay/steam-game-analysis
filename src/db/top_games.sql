-- Table: public.top_games

-- DROP TABLE IF EXISTS public.top_games;

CREATE TABLE IF NOT EXISTS public.top_games
(
    appid integer NOT NULL,
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    positive integer NOT NULL,
    positive_percentage numeric(5,2) NOT NULL,
    negative integer NOT NULL,
    negative_percentage numeric(5,2) NOT NULL,
    total_reviews integer NOT NULL,
    price numeric(10,2) NOT NULL,
    owners character varying(100) COLLATE pg_catalog."default" NOT NULL,
    average_playtime_hours numeric(10,2) NOT NULL,
    median_playtime_hours numeric(10,2) NOT NULL,
    CONSTRAINT top_games_pkey PRIMARY KEY (appid)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.top_games
    OWNER to postgres;