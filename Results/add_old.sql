ALTER TABLE `educations` CHANGE `graduate_year` `graduate_year` INT NULL DEFAULT NULL;
ALTER TABLE educations ADD born int null;
ALTER TABLE work_experiences ADD born int null;

update educations
set born = graduate_year - 24
where legal_name REGEXP 'Унив*|Акад*|Инст*|унив*|акад*|инст*'
and qualification REGEXP 'Лечебн*|лечебн*|Магистр*|магистр*';

update educations
set born = graduate_year - 23
where legal_name REGEXP 'Унив*|Акад*|Инст*|унив*|акад*|инст*'
and qualification REGEXP 'Специал*|специал*';

update educations
set born = graduate_year - 22
where legal_name REGEXP 'Унив*|Акад*|Инст*|унив*|акад*|инст*'
and born = 0;

update educations
set born = graduate_year - 20
where legal_name REGEXP 'Колледж*|колледж*|Техник*|техник*|Училищ*|училищ*';

update educations
set born = graduate_year - 16
where legal_name REGEXP 'Школ*|школ*'
And born = 0;

update educations
set born = graduate_year - 20
where born = 0;


update work_experiences t1,
(select id_cv, start_work-18 born
from (select id_cv, min(year(date_from)) start_work, year-2 start_mag
from work_experiences,
(select educations.id_cv id, graduate_year year from educations, (SELECT id_cv, min(graduate_year) year FROM `educations`group by id_cv) min_graduate where educations.id_cv = min_graduate.id_cv and educations.graduate_year = min_graduate.year and qualification REGEXP 'Магистр*|магистр*') t
where id_cv = t.id
group by id_cv
) years
where start_work+4<start_mag and start_work!=0) t2
set t1.born = t2.born
where t1.id_cv = t2.id_cv;


create table old (id_cv int, born int);

insert into old(id_cv, born)
SELECT id_cv, min(born) FROM `work_experiences` where born !=0 group by id_cv;

insert into old(id_cv, born)
SELECT id_cv, min(born) FROM `educations` 
where born !=0 
and id_cv not in (select id_cv from old)
group by id_cv;

insert into old(id_cv, born)
SELECT id_cv, min(year(date_from))-18 FROM `work_experiences` where id_cv not in (select id_cv from old)
group by id_cv;

delete from old where born<1940;