-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- First column is called genre
-- Second column is called number_of_shows
-- Doesn’t display a genre that doesn’t have any shows linked
-- Records are sorted in descending order by the number of shows linked
SELECT g.name AS genre,
       COUNT(*) AS number_of_shows
  FROM tv_genres AS g
       INNER JOIN tv_show_genres AS t
       ON g.id = t.genre_id
 GROUP BY g.name
 ORDER BY number_of_shows DESC;
