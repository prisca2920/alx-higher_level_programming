-- lists all shows
-- in the database
SELECT tv_shows.title tv_show_genres.genre_id
ORDER BY tv_shows.title AND tv_show_genres.genre_id ASC;
