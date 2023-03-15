-- Lists all shows in the database hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Records are ordered by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT t.title, g.genre_id
  FROM tv_shows AS t
       LEFT JOIN tv_show_genres AS g
       ON t.id = g.show_id
       WHERE g.genre_id IS NULL
 ORDER BY t.title, g.genre_id ASC;
