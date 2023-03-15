-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record display: tv_genres.name
-- Results sorted in ascending order by the genre name
SELECT g.name
  FROM tv_genres AS g
       INNER JOIN tv_show_genres AS s
       ON g.id = s.genre_id

       INNER JOIN tv_shows AS t
       ON t.id = s.show_id
       WHERE t.title = "Dexter"
 ORDER BY g.name ASC;
