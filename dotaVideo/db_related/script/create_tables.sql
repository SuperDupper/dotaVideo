use game_db;

CREATE TABLE video_author (
	sid bigint(11) NOT NULL AUTO_INCREMENT,
	nick varchar(64) NOT NULL,
	url' varchar(128) NOT NULL,
	video_type set('dota', 'lol', 'hearthstone'),
	PRIMARY KEY (sid),
	KEY index_name (nick)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE video (
	sid bigint(11) NOT NULL AUTO_INCREMENT,
	url varchar(128) NOT NULL,
	title varchar(128) NOT NULL,
	abstract varchar(512) NOT NULL,
	author_id bigint(11) NOT NULL,
	author varchar(64) NOT NULL,
	release_time datetime NOT NULL,
	hot_index bigint(11) NOT NULL,
	watch_num bigint(11) NOT NULL,
	video_length time NOT NULL,
	tags varchar(128) NOT NULL,
	video_type set('dota', 'lol', 'hearthstone'),
	screenshot mediumblob,
	PRIMARY KEY (sid),
	KEY index_url (url),
	KEY index_author_id (author_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
