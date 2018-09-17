INSERT INTO public.artists_artistsraw
(shortcode ,
caption ,
display_url ,
loc_name ,
loc_lat ,
loc_long ,
instagram_handle ,
likes ,
city ,
state ,
country)
SELECT shortcode,
caption,
display_url,
loc_name,
loc_lat,
loc_long,
instagram_handle,
likes,
city,
state,
country FROM staging.posts_filtered
WHERE instagram_handle NOT IN (
SELECT instagram_handle
    FROM public.artists_artistsraw
    WHERE instagram_handle IS NOT NULL)
;
