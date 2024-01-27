CREATE TABLE IF NOT EXISTS COMPETITIONS
(
    id_competition   INT,
    date_from        TIMESTAMP,
    date_to          TIMESTAMP,
    name             TEXT,
    has_results      INT,
    city             TEXT,
    street           INT,
    street_no        INT,
    comp_year        INT,
    prime_event      INT,
    continent_short  TEXT,
    has_logo         INT,
    competition_code TEXT,
    updated_at_ts    INT,
    updated_at       TIMESTAMP,
    tz               TEXT,
    id_live_theme    INT,
    code_live_theme  TEXT,
    country_short    TEXT,
    country          TEXT,
    id_country       INT,
    is_teams         INT,
    status           INT,
    ages             TEXT,
    rank_name        TEXT
);


CREATE TABLE COMPETITORS
(
    id_competitor INT,
    family_name   VARCHAR(255),
    given_name    VARCHAR(255),
    country_short VARCHAR(255),
    club          VARCHAR(255),
    dob_year      INT,
    coach         VARCHAR(255),
    gender        VARCHAR(255),
    side          CHAR,
    belt          VARCHAR(255),
    height        INT,
    id_weight     VARCHAR(255)
);

CREATE TABLE CONTESTS
(
    id_competition    INT,
    id_fight          INT NOT NULL,
    id_person_blue    INT,
    id_person_white   INT,
    ippon_b           INT,
    waza_b            INT,
    yuko_b            INT,
    penalty_b         INT,
    ippon_w           INT,
    waza_w            INT,
    yuko_w            INT,
    penalty_w         INT,
    id_winner         INT,
    duration          INT,
    round             INT,
    round_name        VARCHAR(255),
    weight            VARCHAR(255),
    contest_code_long VARCHAR(300)
);


CREATE TABLE EVENTS_DETAILS
(
    id_actor   INT,
    id_event   INT,
    event_name VARCHAR(255),
    id_group   INT
);


CREATE TABLE EVENT_TYPES
(
    type_code INT,
    type_description VARCHAR(255)
);


CREATE TABLE EVENTS
(
    contest_code_long VARCHAR(355),
    time_real         DECIMAL,
    id_event          INT
);

CREATE TABLE IF NOT EXISTS CATEGORIES
(
    id_weight INT,
    name      VARCHAR(5),
    gender    CHAR
);