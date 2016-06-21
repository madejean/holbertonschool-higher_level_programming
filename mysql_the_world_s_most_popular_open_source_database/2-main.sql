\! echo "\nNumber of season by TVShow ordered by name (A-Z)?"
SELECT TVShow.name, count(Season.tvshow_id) as "nb_seasons" FROM TVShow
JOIN Season on (TVShow.id = Season.tvshow_id)
GROUP BY Season.tvshow_id
ORDER BY name;

\! echo "\nList of Network by TVShow ordered by name (A-Z)?"
SELECT TVShow.name as "TVShow name", Network.name as "Network name" FROM TVShow
JOIN Network on (TVShow.network_id = Network.id)
ORDER BY TVShow.name;

\! echo "\nList of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?"
SELECT TVShow.name FROM TVShow
JOIN Network on (TVShow.network_id = Network.id)
WHERE Network.name = "Fox (US)"
ORDER BY TVShow.name;

\! echo "\nNumber of episodes by TVShows ordered by name (A-Z)?"
SELECT TVShow.name, count(Episode.id) as nb_episodes FROM TVShow
JOIN Season on (TVShow.id = Season.tvshow_id)
JOIN Episode on (Season.id = Episode.season_id)
GROUP BY TVShow.id
ORDER BY TVShow.name;
