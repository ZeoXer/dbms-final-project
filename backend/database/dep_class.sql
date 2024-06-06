/* 各系助教使用介面：教學科目數 */
/* 需變更 F.year, F.semester, D.department_id */

select distinct 
	T.teacher_id, 
    T.Cname, 
    F.teacher_type,
    sum(CASE WHEN c.degree = '學士班' THEN num_class ELSE 0 END) AS `學士班`,
    sum(CASE WHEN c.degree = '一般碩士班' THEN num_class ELSE 0 END) AS `一般碩士班`,
    sum(CASE WHEN c.degree = '博士班' THEN num_class ELSE 0 END) AS `博士班`,
    sum(CASE WHEN c.degree = 'MBA' THEN num_class ELSE 0 END) AS MBA,
    sum(CASE WHEN c.degree = 'IMBA' THEN num_class ELSE 0 END) AS IMBA,
    sum(CASE WHEN c.degree = 'EMBA' THEN num_class ELSE 0 END) AS EMBA,
    sum(CASE WHEN c.degree = 'DBA' THEN num_class ELSE 0 END) AS DBA
from teacher as T, facultytype as F, class as C, department as D
where T.teacher_id=F.teacher_id and 
	  F.year=112 and F.semester=1 and 
	  F.teacher_id=C.teacher_id and 
	  F.year=C.year and 
      F.semester=C.semester and 
	  T.dep_id=D.department_id and 
      D.department_id='301'
GROUP BY 
    T.teacher_id, T.Cname, F.teacher_type
order by Cname