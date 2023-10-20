--list all shows contained in hbtn_0d_tvshows that have atleast one genre
-- list all rows of db that have col in common
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_shows_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
