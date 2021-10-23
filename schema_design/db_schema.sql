-- Создание схемы для контента
CREATE SCHEMA IF NOT EXIST content;

-- Создать таблицу film_work
CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    certificate TEXT,
    file_path TEXT,
    rating FLOAT,
    type TEXT not null,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- Создать таблицу genre
CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- Создать таблицу genre_fiml_work
CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    genre_id uuid NOT NULL,
    created_at timestamp with time zone
);

-- Создать таблицу person
CREATE TABLE IF NOT EXISTS content.person (
  id uuid PRIMARY KEY,
  full_name TEXT NOT NULL,
  birth_date DATE,
  created_at timestamp with time zone,
  updated_at timestamp with time zone
);

-- Создать таблицу person_film_work
CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    person_id uuid NOT NULL,
    role TEXT NOT NULL,
    created_at timestamp with time zone
);

-- Создать уникальный композитный индекс для таблицы genre_film_work
CREATE UNIQUE INDEX film_work_genre ON content.genre_film_work (film_work_id, genre_id);

-- Создать уникальный композитный индекс для таблицы person_film_work
CREATE UNIQUE INDEX film_work_person_role ON content.person_film_work (film_work_id, person_id, role);
