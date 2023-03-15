-- Lists all shows and genres linked to the show from the database hbtn_0d_tvshows.
-- displays NULL in the genre column if a show doesnt have a genre
-- Each record displays: tv_shows.title - tv_genres.name
-- Records are ordered by ascending show title and genre name.
SELECT t.title, g.name
  FROM tv_shows AS t
       LEFT JOIN tv_show_genres AS s
       ON t.id = s.show_id

       LEFT JOIN tv_genres AS g
       ON s.genre_id = g.id
 ORDER BY t.title, g.name ASC;
