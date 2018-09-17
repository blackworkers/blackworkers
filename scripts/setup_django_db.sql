
-- Invoke with `psql -U postgres -d bw -f setup_django_db.sql`
CREATE DATABASE dj;

CREATE USER django WITH PASSWORD 'django';

ALTER ROLE django SET client_encoding TO 'utf8';
ALTER ROLE django SET default_transaction_isolation TO 'read committed';
ALTER ROLE django SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE dj TO django;
