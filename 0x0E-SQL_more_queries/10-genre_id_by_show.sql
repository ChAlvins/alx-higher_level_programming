-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Records are sorted by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT t.title, g.genre_id
  FROM tv_shows AS t
        INNER JOIN tv_show_genres AS g
	ON t.id = g.show_id
 ORDER BY t.title, g.genre_id ASC;
