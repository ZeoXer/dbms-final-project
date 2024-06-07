# Data Description

## Department(系所)

department_id(系所代碼)、department_Ename(系所英文名稱)、department_Cname(系所中文名稱)

## Teacher(教師)

teacher_id(教師編號)、Cname(中文姓名)、Ename(英文姓名)、job_title(職稱)、year(到職年)、dep_id(系所代碼)

## Resume(教師履歷)

teacher_id(教師編號)、resume_year(填寫年份)、highest_edu_degree(最高學歷學位)、highest_edu_department(最高學歷系所)、highest_edu_school(最高學歷學校)、highest_edu_graduation_year(最高學歷取得學位年份)、experience(經歷)、teaching_interests(教學興趣)、research_interests(研究興趣)、discipline(學群)、(近一年…)[AMD(擔任行政職務), ED(教授高管班), SER(其他服務如借調、期刊編輯、主編、審稿), PA1-1&IP1-1(借調至產學界或政府機關), PA1-2(參與產業界的活動或與產業界主管有聯繫互動), PA1-3(參與產業經營或擔任專業職務), PA1-4(於學會/協會組織擔任高階職務), PA1-5(參與學會/協會團體組織之活動), PA1-6(長期提供企業諮詢（一年以上）), PA1-7&IP1-3(擔任董事會（理事會）/監察人（監事）相關職務), PA1-8&SP1-3(具商管教育經歷並持續累積中), SP1-1(參與學術/業界相關之活動/社群/學會/協會), SP1-2(於業界擔任重要職務), IP1a(具有產業界全職或兼職之工作), IP1-2(企業主、合夥人、或專業經理人), IP1-4(業界活躍人士), IP1-5(會計師、律師或擁有其他專業證照)]

## PartTime(校外兼職)

teacher_id(教師編號)、pt_company(兼職機關)、pt_department(兼職單位)、pt_position(兼職職稱)、pt_start(兼職起日)、pt_end(兼職迄日)

## List(學術、實務與教學貢獻清單)

item_name(篇名/獎項/政策法案名稱/論文題目/計畫名稱)、item_year(年度)、item_type(類別)、journal(期刊名)、journal_type(期刊屬SSCI/SCI/TSSCI or equivalent)、co_worker_in(與本院教授共同創作姓名)、co_worker_out(與本院學生或本校外院師生或校外人士共同創作姓名)、scholarship_type(屬性)、equis(EQUIS分類)

## FacultyType(專兼別)

teacher_id(教師編號)、year(學年度)、semester(學期)、teacher_type(專兼別)

## Class(開課時數)

teacher_id(教師編號)、year(學年度)、semester(學期)、degree(學制)、num_class(科目數)