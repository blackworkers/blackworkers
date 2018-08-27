CREATE DATABASE bw;

CREATE SCHEMA staging;

CREATE TABLE staging.posts_raw (
post_id text,
scraped_timestamp text,
shortcode text,
caption text,
display_url text,
loc_id bigint,
loc_name text,
loc_lat numeric,
loc_long numeric,
owner_id bigint,
instagram_handle text,
likes bigint,
taken_at_ts text,
city text,
state text,
country text,
scraped_job_time text)
;

INSERT INTO staging.posts_raw VALUES (
