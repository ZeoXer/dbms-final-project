/* 教師使用介面：學術、實務與教學貢獻清單 */
/* 需變更 T.teacher_id, item_year */

select item_name, item_year, journal, journal_type, co_worker_in, co_worker_out, scholarship_type, equis
from teacher as T, list as L
where T.teacher_id=L.teacher_id and 
	  T.teacher_id='354008' and 
	  (item_year between 2019 and 2024)
order by item_year, item_name