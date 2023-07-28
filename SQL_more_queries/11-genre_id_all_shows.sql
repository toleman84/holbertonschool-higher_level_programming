-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- If a show doesn’t have a genre, display NULL
SELECT tv_shows.title, tv_show_genres.genre_id,
IFNULL(tv_show_genres.genre_id, NULL)
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
