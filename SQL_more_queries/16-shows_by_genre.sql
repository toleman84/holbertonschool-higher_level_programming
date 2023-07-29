-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows

SELECT tv_shows.title, tv_genres.name
FROM tv_shows

INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id

INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id

WHERE tv_show_genres.genre_id IS NULL

ORDER BY tv_show.title ASC, tv_genres.name ASC;
