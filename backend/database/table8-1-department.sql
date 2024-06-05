/* AACSB: TABLE 8-1 分系所 */
/* 需變更 item_year, facultytype.year */

DROP VIEW IF EXISTS all_list, all_list_with_aacsb, teacher_list, all_class, all_class_with_contri;

-- about list

create view all_list as
select 
	T.teacher_id,
    T.dep_id,
    scholarship_type, 
    equis,
    CASE 
        WHEN T.teacher_id IN (
            SELECT teacher_id 
            FROM facultytype 
            WHERE (year = 112 AND semester = 1 AND teacher_type = '專任') 
              AND teacher_id IN (
                SELECT teacher_id 
                FROM facultytype 
                WHERE year = 112 AND semester = 2 AND teacher_type = '專任'
              )
        ) THEN 1
        ELSE 0
    END AS full_time
from teacher as T, list as L
where T.teacher_id=L.teacher_id and 
      (item_year between 2019 and 2024);
      
CREATE VIEW all_list_with_aacsb AS
SELECT 
    *,
    CASE 
        WHEN equis = 'E1:Academic Research Articles' THEN 'A1:Peer-Reviewed Journals Articles'
        WHEN equis = 'E2:Practices-oriented Articles' THEN 'A1:Peer-Reviewed Journals Articles'
        WHEN equis = 'E3:Studies and Reports commissioned by companies and gov\'t agencies(企業、政府、科技部產學合作計畫)' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
        WHEN equis = 'E4:Papers in Academic conferences' THEN 'A1:Peer-Reviewed Journals Articles'
        WHEN equis = 'E5:Papers in Professional conferences' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
        WHEN equis = 'E6:Published Case Studies' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
        WHEN equis = 'E7:Books (e.g. research monographs)' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
        WHEN equis = 'E8:Chapters in books' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
        WHEN equis = 'E9:Textbooks' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
        WHEN equis = 'E10:Chapters in textbooks' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
        WHEN equis = 'E11:Articles on Pedagogic Development and Innovation' THEN 'A3:All other intellectual contributions'
        WHEN equis = 'E12:Studies and Reports produced as part of an int\'l network' THEN 'A3:All other intellectual contributions'
        WHEN equis = 'E13:Published Teaching Materials' THEN 'A3:All other intellectual contributions'
        WHEN equis = 'E14:Doctoral theses completed-supervised by core faculty' THEN 'A3:All other intellectual contributions'
        WHEN equis = 'E15:Other(Competitive Research Awards Received)獲重要研究獎項次數' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
        WHEN equis = 'E15:Other(Please describe)其他(科技部學術型計畫 MOST Research Project)' THEN 'A3:All other intellectual contributions'
        ELSE NULL
    END AS aacsb
FROM 
    all_list;

create view teacher_list as
SELECT 
    teacher_id,
    dep_id,
    SUM(CASE WHEN scholarship_type = 'Basic_or_Discovery_Scholarship' THEN 1 ELSE 0 END) AS Basic_or_Discovery_Scholarship,
    SUM(CASE WHEN scholarship_type = 'Applied_or_Integration_Application_Scholarship' THEN 1 ELSE 0 END) AS Applied_or_Integration_Application_Scholarship,
    SUM(CASE WHEN scholarship_type = 'Teaching_and_Learning_Scholarship' THEN 1 ELSE 0 END) AS Teaching_and_Learning_Scholarship,
    SUM(CASE WHEN scholarship_type = 'Basic_or_Discovery_Scholarship' THEN 1 ELSE 0 END) +
    SUM(CASE WHEN scholarship_type = 'Applied_or_Integration_Application_Scholarship' THEN 1 ELSE 0 END) +
    SUM(CASE WHEN scholarship_type = 'Teaching_and_Learning_Scholarship' THEN 1 ELSE 0 END) AS BAT_Total,
    SUM(CASE WHEN aacsb = 'A1:Peer-Reviewed Journals Articles' THEN 1 ELSE 0 END) AS `Peer-Reviewed Journals Articles`,
    SUM(CASE WHEN aacsb = 'A2:Additional peer- or editorial-reviewed intellectual contributions' THEN 1 ELSE 0 END) AS `Additional peer-or-editorial-reviewed intellectual contributions`,
    SUM(CASE WHEN aacsb = 'A3:All other intellectual contributions' THEN 1 ELSE 0 END) AS `All other intellectual contributions`,
    SUM(CASE WHEN aacsb = 'A1:Peer-Reviewed Journals Articles' THEN 1 ELSE 0 END) +
    SUM(CASE WHEN aacsb = 'A2:Additional peer- or editorial-reviewed intellectual contributions' THEN 1 ELSE 0 END) +
    SUM(CASE WHEN aacsb = 'A3:All other intellectual contributions' THEN 1 ELSE 0 END) AS PAA_Total,
    full_time
FROM 
    all_list_with_aacsb
WHERE 
    dep_id != 300
GROUP BY 
    teacher_id,
    dep_id
ORDER BY 
    dep_id,
    teacher_id;

-- about class

create view all_class as
select 
	T.teacher_id,
    T.dep_id,
    SUM(CASE WHEN C.year=112 and C.semester=1 THEN C.num_class ELSE 0 END) as s1_num_class,
    SUM(CASE WHEN C.year=112 and C.semester=2 THEN C.num_class ELSE 0 END) as s2_num_class,
    CASE 
        WHEN T.teacher_id IN (
            SELECT teacher_id 
            FROM facultytype 
            WHERE (year = 112 AND semester = 1 AND teacher_type = '專任') 
        ) THEN 1*0.5
        ELSE 0.05*0.5
    END AS s1_type,
    CASE 
        WHEN T.teacher_id IN (
            SELECT teacher_id 
            FROM facultytype 
            WHERE (year = 112 AND semester = 2 AND teacher_type = '專任') 
        ) THEN 1*0.5
        ELSE 0.05*0.5
    END AS s2_type
from 
	teacher as T,
    class as C
where
	T.teacher_id=C.teacher_id and
    T.dep_id != 300
group by
	T.teacher_id,
    T.dep_id;

CREATE VIEW all_class_with_contri AS
SELECT 
    *,
    (CASE WHEN s1_type=0.5 THEN s1_type ELSE s1_type * s1_num_class END) +
    (CASE WHEN s2_type=0.5 THEN s2_type ELSE s2_type * s2_num_class END) as contri
FROM
	all_class
ORDER BY 
    dep_id,
    teacher_id;
    
-- group by department

select 
	department_Ename, SUM(Basic_or_Discovery_Scholarship), SUM(Applied_or_Integration_Application_Scholarship), SUM(Teaching_and_Learning_Scholarship), SUM(BAT_Total), 
    SUM(`Peer-Reviewed Journals Articles`), SUM(`Additional peer-or-editorial-reviewed intellectual contributions`), SUM(`All other intellectual contributions`), SUM(PAA_Total), 
    ROUND(SUM(CASE WHEN full_time = 1 THEN 1 ELSE 0 END) / 
    SUM(CASE WHEN full_time >=0 THEN 1 ELSE 0 END),4) AS `Percent of Participating Faculty Producing ICs`,
    ROUND(SUM(contri * BAT_Total) / SUM(BAT_Total),4) AS `Percentage of Total Full Time Equivalent (FTE) Faculty Producing ICs`
from (teacher_list
	join(
		select teacher_id as t_id, dep_id as d_id, contri
        from all_class_with_contri) as teacher_class
	on 
		teacher_list.teacher_id=teacher_class.t_id and
        teacher_list.dep_id=teacher_class.d_id ),
	department as D
where 
	dep_id=D.department_id
group by
	department_Ename
order by
	department_Ename

