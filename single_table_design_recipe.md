_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
Nouns:

album
title
release year
artist_id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| album                 | title, release year, artist_id |

Table name: `albums`
Column names: `title`, `release_year`, `artist_id`


## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:
id: SERIAL
title: text
release_year: int
artist_id: int
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, column names and types.

-- seeds/albums_table.sql

DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);

-- Add some test data
INSERT INTO albums (title, release_year, artist_id) VALUES ('Doolittle', 1989, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Surfer Rosa', 1988, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Waterloo', 1974, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Super Trouper', 1980, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Bossanova', 1990, 1);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```