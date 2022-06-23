create table "Members"
(
    beatle_id      serial constraint beatle_id_pk primary key,
    name    varchar,
    age     integer,
    custom_information jsonb
);

alter table "Members"
    owner to postgres;

create unique index users_id_uindex
    on "Members" (beatle_id);

INSERT INTO public."Members" VALUES (1, 'John Lennon', 82, '{ "favoriteNumber": 3, "height": 182 }');
INSERT INTO public."Members" VALUES (2, 'Paul McCartney', 80, '{ "height": 180 }');
INSERT INTO public."Members" VALUES (3, 'George Harrison', 79, '{ "height": 181 }');
INSERT INTO public."Members" VALUES (4, 'Ringo Starr', 82, '{ "height": 172 }');