-- 16
SELECT id_competitor, given_name, family_name, dob_year 
	FROM COMPETITORS c
		LEFT JOIN CONTESTS c2 on c.ID_COMPETITOR = c2.id_winner
	WHERE
		c2.id_winner IS NULL
ORDER BY c.dob_year DESC, c.family_name ASC
LIMIT 5;

-- 2
SELECT GENDER, COUNT(*) AS CNT FROM COMPETITORS c
GROUP BY gender
ORDER BY CNT ASC;

-- 3
SELECT ed.EVENT_NAME, COUNT(EVENT_NAME) AS "obs-count" 
	FROM 
		EVENTS_DETAILS ed
	WHERE 
		ID_GROUP NOT IN (1, 38)
GROUP BY EVENT_NAME
ORDER BY `obs-count` DESC -- type_description ASC
LIMIT 5;

-- 4
SELECT c.ID_COMPETITOR AS ID_COMPETITOR, COUNT(cc.id_winner) AS CNT, c.family_name AS FAMILY_NAME, c.given_name AS GIVEN_NAME, c.country_short AS COUNTRY_SHORT, c.side AS SIDE, c.belt AS BELT, c.club AS CLUB
	FROM
		COMPETITORS c
		LEFT JOIN CONTESTS cc 
			ON c.ID_COMPETITOR = cc.id_winner
GROUP BY c.ID_COMPETITOR, c.family_name, c.given_name, c.country_short, c.side, c.belt, c.club
ORDER BY cnt DESC, FAMILY_NAME ASC
LIMIT 10;

-- 5
SELECT c.ID_COMPETITOR AS ID_COMPETITOR, COUNT(cc.id_winner) AS CNT, c.family_name AS FAMILY_NAME, c.given_name AS GIVEN_NAME, c.country_short AS COUNTRY_SHORT, c.side AS SIDE, c.belt AS BELT, c.club AS CLUB
	FROM
		COMPETITORS c
		LEFT JOIN CONTESTS cc 
			ON c.ID_COMPETITOR = cc.id_winner 
		LEFT JOIN EVENTS e 
			ON cc.id_competition = e.id_event
	WHERE
		cc.round_name = 'Final'
GROUP BY c.ID_COMPETITOR, c.family_name, c.given_name, c.country_short, c.side, c.belt, c.club
ORDER BY cnt DESC, FAMILY_NAME ASC
LIMIT 10;

-- 6
SELECT event_name AS "Teddy's Favorites", COUNT(event_name) AS "obs-count" 
	FROM 
		events_details ed
		INNER JOIN competitors c 
			ON c.ID_competitor = ed.ID_Actor
	WHERE 
		c.family_name = 'RINER' AND 
		c.given_name = "TEDDY" AND 
		ed.id_group NOT IN (1, 38)
GROUP BY event_name
ORDER BY `obs-count` DESC, ed.event_name ASC
LIMIT 5;

-- 12
SELECT c.ID_COMPETITOR, c.family_name, c.given_name, c.dob_year
	FROM
		COMPETITORS c 
		JOIN 



-- 8
SELECT cp.continent_short, count(*) AS TOTAL 
	FROM
		Competitors c
		JOIN CONTESTS cc 
			ON c.ID_competitor = cc.id_winner 
		JOIN EVENTS e 
			ON cc.ID_Competition = e.id_event
		JOIN Competitions cp 
			ON cp.id_competition = e.id_event
	WHERE
		cc.round_name = "Final"
GROUP BY cp.continent_short
ORDER BY TOTAL DESC;

-- 9
SELECT cp.competition_code AS competition_code, c1.family_name as "c1.family_name", c2.family_name as "c2.family_name", c2.country_short as "c1.country_short", c2.country_short as "c2.country_short" 
	FROM
		Competitions cp
		JOIN CONTESTS ct 
			ON ct.id_competition = cp.id_competition
		JOIN COMPETITORS c1 
			ON ct.id_person_blue = c1.ID_COMPETITOR 
		JOIN COMPETITORS c2 
			ON ct.id_person_white = c2.ID_COMPETITOR
	WHERE
		c1.country_short = c2.country_short
ORDER BY cp.date_from DESC, c1.family_name ASC, c2.family_name ASC
LIMIT 5;

-- 10
SELECT ed.event_name AS event_name, et.type_description AS type_description, COUNT(*) AS obs_count
	FROM
		EVENT_TYPES et
		JOIN EVENTS_DETAILS ed 
			ON et.TYPE_CODE = ed.ID_GROUP 
		JOIN EVENTS e 
			ON ed.ID_EVENT = e.ID_EVENT
	WHERE
		et.type_code NOT IN (1, 38)
GROUP BY event_name, et.type_description
ORDER BY obs_count DESC, type_description ASC, event_name ASC
LIMIT 10;

-- 11
SELECT c.country_short, COUNT(DISTINCT e.id_event) AS competition_count
	FROM
		COMPETITIONS c
		JOIN EVENTS e 
			ON c.id_competition = e.id_event
GROUP BY c.country_short
ORDER BY competition_count DESC, c.country_short ASC
LIMIT 5;

-- 14
SELECT c.name, COUNT(DISTINCT c.id_country) AS num_countries FROM COMPETITIONS c
GROUP BY c.name
ORDER BY num_countries DESC, name ASC
LIMIT 5;