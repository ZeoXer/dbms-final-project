/* 各系助教使用介面：學術、實務與教學貢獻清單 */
/* 需變更 D.department_id, item_year */

select Cname, item_name, item_year, journal, journal_type, co_worker_in, co_worker_out, scholarship_type, equis
from teacher as T, list as L, department as D
where T.teacher_id=L.teacher_id and 
	  T.dep_id=D.department_id and 
      D.department_id='301' and 
      (item_year between 2019 and 2024)
order by Cname, item_year, item_name