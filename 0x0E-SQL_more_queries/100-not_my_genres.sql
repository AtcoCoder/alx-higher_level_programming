-- lists all genres linked to that show Dexter, from the
-- database hbtn_0d_tvshows.

SELECT tv_genres.name as name
FROM tv_genres
WHERE tv_genres.id
NOT IN (
	SELECT tv_show_genres.genre_id
    FROM tv_show_genres
    JOIN tv_shows
    ON tv_shows.id=tv_show_genres.show_id
    WHERE tv_shows.title='Dexter'
)
