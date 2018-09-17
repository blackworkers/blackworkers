CREATE DATABASE bw;

CREATE SCHEMA staging;
CREATE SCHEMA prod;

CREATE TABLE staging.posts_raw (
job_hashtag text,
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

CREATE VIEW staging.posts_filtered AS (SELECT DISTINCT ON (instagram_handle) job_hashtag,
post_id,
scraped_timestamp,
shortcode,
caption,
display_url,
loc_id,
loc_name,
loc_lat,
loc_long,
owner_id,
instagram_handle,
likes,
taken_at_ts,
city,
state,
country,
scraped_job_time
FROM staging.posts_raw
ORDER BY instagram_handle, LIKES DESC);


-- THIS TABLE HAS BEEN MOVED TO THE DJANGO DATA MODEL DEFINITION
-- CREATE TABLE prod.artist_list (
-- shortcode text,
-- caption text,
-- display_url text,
-- loc_name text,
-- loc_lat numeric,
-- loc_long numeric,
-- instagram_handle text,
-- likes bigint,
-- city text,
-- state text,
-- country text,
-- rejected BOOLEAN DEFAULT FALSE;
-- );
