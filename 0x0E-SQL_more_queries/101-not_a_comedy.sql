-- lists all genres linked to that show Dexter, from the
-- database hbtn_0d_tvshows.

SELECT tv_shows.title AS title
FROM tv_shows
WHERE tv_shows.id
NOT IN (
	SELECT tv_show_genres.show_id
    FROM tv_show_genres
    JOIN tv_genres
    ON tv_show_genres.genre_id=tv_genres.id
    WHERE tv_genres.name="Comedy"
);
