-- lists all the shows
-- that have atleast one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows
ORDER BY tv_shows.title AND tv_show_genres.genre_id ASC;