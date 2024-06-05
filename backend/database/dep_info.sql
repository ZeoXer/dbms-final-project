/* 各系助教使用介面：基本資料與近一年社會影響力 */
/* 需變更 D.department_id */

select T.teacher_id, T.Cname, T.Ename, T.job_title, T.year, D.department_Cname, R.discipline, highest_edu_degree, highest_edu_department, highest_edu_school, highest_edu_graduation_year, experience, teaching_interests, research_interests, ADM, ED, SER, `PA1-1&IP1-1`, `PA1-2`, `PA1-3`, `PA1-4`, `PA1-5`, `PA1-6`, `PA1-7&IP1-3`, `PA1-8&SP1-3`, `SP1-1`, `SP1-2`, IP1a, `IP1-2`, `IP1-4`, `IP1-5`, resume_year
from teacher as T, resume as R, department as D
where T.teacher_id=R.teacher_id and 
	  T.dep_id=D.department_id and 
	  D.department_id='301'
order by teacher_id