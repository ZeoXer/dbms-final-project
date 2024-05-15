# 教師履歷管理系統資料需求

## 為何需要教師履歷管理系統？

教師履歷為學校教師各樣論著、研究、獎項等事蹟紀錄，是衡量教師們於研究和教學貢獻的指標之一，更是AACSB與EQUIS等國際認證審查的內容。為了更有效率地搜集教師履歷資料，此系統旨在簡化資料彙整流程，並自動化產生國際認證所需的報表，提供學院參考。

## 蒐集對象

2019年至2023年內，下述定義的老師皆須填入：

1. 單位內專任老師
2. 單位內兼任老師
3. 外院專兼任老師支援開課請填入，視為兼任老師
4. 院內合聘老師由主系所填寫，視為專任
5. 跨院合聘需填入，視為專任老師
6. MBA、IMBA、EMBA的院內外系支援專任老師需要填入，視為專任
7. 跨校合聘(非主聘)視為兼任，跨校合聘(主聘)視為專任

## 過往的教師履歷彙整流程

``` mermaid
graph TD;

電算中心--1.提供各教師著作與開課資料-->認證辦公室;
認證辦公室--2.將教師資料拆分成各系單獨的檔案-->各系助教;
各系助教--3.協助系上教師填寫部分欄位-->系上各教師;

系上各教師--4.新增、修改與刪除資料-->各系助教;
各系助教--5.彙整系上各教師資料 \n (產生各系報表)-->認證辦公室;
認證辦公室--6.彙整各系教師資料 \n (產生全院報表)-->學院;
學院--7.進行最後確認-->國際認證單位
```

### 1.電算中心提供各教師著作與開課資料

| 資料表名稱 | 欄位                                                                     |
|----------|------------------------------------------------------------------------|
| 教師清單   | 教師編號, 姓名, 系所代碼, 系所名稱, 職稱, 專兼別                         |
| 獎項       | 單位代碼, 單位名稱, 序號, 教師代號, 教師姓名, 年度, 頒獎單位, 獎項, 備註 |
| 研究計畫 | 系所代碼, 系所名稱, 教師代號, 教師姓名, 計畫職稱, 核定年度, 起始年度, 主持人代碼, 主持人, 校內編號, 計畫名稱, 委託單位, 計畫類別	, 起迄日期
| 論著資料 | 系所代碼, 系所名稱, 教師編號, 教師姓名, 論著編號, 論著名稱, 論著名稱二, 論著日期, 論著類別, 期刊名, 期刊資料庫所屬, 審查制度, 專書性質, 著作人數, 合著者1, 合著者2, 合著者3, 合著者4, 合著者5, 合著者6, 合著者7, 合著者8, 合著者9, 合著者10, 合著者11	, 合著者12 |


### 2.認證辦公室將教師資料拆分成各系單獨的檔案

認證辦公室依據電算中心資料拆分成各系單獨的檔案，同時製作每位教師空白的A1-A3清單檔，使各系助教收到一份「全系教師的電算中心資料」，以及全系教師每人一份的「A1-A3清單檔」，並將上述所有資料寄給相對應系所的系助教。

例如：全院共有五個系所，每個系都有十位教師，則認證辦公室要將電算中心資料拆分成各系所一份的「全系教師的電算中心資料」，共五個檔案；接著再以個別教師為單位，每個系所各有十位教師的「A1-A3清單檔」，共五十個檔案。由此可知，每位系助教會收到屬於自己系的十一份檔案。

#### ➤此階段資料處理需求：

1. 篩選與貼上的步驟十分繁瑣且一致，是否能直接透過指令一次性輸出所有檔案？
2. 抑或是不輸出檔案，改成讓各系助教與教師能自行登入網站進行填寫與確認的動作，唯各系助教的修改權限為系上教師，個別教師只能編輯個人。

### 3.各系助教協助系上教師填寫部分欄位

各系助教需要先協助系上教師填寫「A1-A3清單」，需參考「全系教師的電算中心資料」後填入以下內容：

* 論著目錄清單：期刊、會議論文、專書、個案、教學教材
* 重要研究獎項(E15=A4)
* 參與專業/公共政策制訂法案名稱(E3=A8)
* 指導畢業的博士論文(E14=A9)
* 政府或產業計畫、國科會計畫(E15=A9)


| 欄位名稱                          | 欄位選項                                                                                                              | 欄位說明                                                |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| 系所                            | Accounting, BA, DBA, EMBA, Finance, Intl Buss, IMBA, MBA, MIS, M & B, RMI, Statistics, TIM & IIP                  |                                                     |
| 姓名(中文)                        |                                                                                                                   |名字中間請勿空格                                     |
| 姓名(英文)                        |                                                                                                                   |                                                     |
| 年度(西元)                        | 2019-2023                                                                                                         | 以起始年度為準                                             |
| SSCI/ SCI/TSSCI or equivalent | O,X                                                                                                               | 是期刊論文資料才需要判別此欄，其他資料皆為X                              |
| 與本院教授共同創作                     |                                                                                                                   | 註明合著作者姓名                                          |
| 與本院學生、本校外院師生、校外人士共同創作     |                                                                                                                   | 註明合著作者姓名                                          |
| 篇名                            |                                                                                                                   | 若為期刊、會議論文、專書、個案、教學教材，請 key 篇名；若為重要研究獎項，請 key 獎項名稱；若為參與專業/公共政策制訂法案名稱，請 key 政策法案名稱；若為指導畢業的博士論文，請 key 論文題目；若為政府或產業計畫、國科會計畫，請 key 計畫名稱。|
| Journal名稱                     |                                                                                                                   | 是期刊論文資料才需要填寫此欄，其他資料勿貼，如：研討會論文、專書、篇章、個案、研究獎項等，不用填寫此欄 |
| 屬性                            | Basic_or_Discovery_Scholarship, Applied_or_Integration_Application_Scholarship, Teaching_and_Learning_Scholarship | 依序為學術、實務、教學三種                                       |
| EQUIS的分類                      | E1-E15                                                                                                            | 見「屬性與EQUIS分類」表格，不同屬性會有不同的EQUIS分類可選擇                 |
| AACSB的分類                      | A1-A10                                                                                                            | 見「EQUIS與AACSB分類對照」表格，可用公式對照自動產生                     |


**屬性與EQUIS分類：**

| Basic_or_Discovery_Scholarship                                         | Applied_or_Integration_Application_Scholarship                                                    | Teaching_and_Learning_Scholarship                    |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------|
| E1:Academic Research Articles                                          | E2:Practices-oriented Articles                                                                    | E1:Academic Research Articles                        |
| E4:Papers in Academic conferences                                      | E3:Studies and Reports commissioned by companies and gov't agencies(企業、政府、科技部產學合作計畫) | E4:Papers in Academic conferences                    |
| E7:Books (e.g. research monographs)                                    | E5:Papers in Professional conferences                                                             | E5:Papers in Professional conferences                |
| E8:Chapters in books                                                   | E6:Published Case Studies                                                                         | E6:Published Case Studies                            |
| E12:Studies and Reports produced as part of an int'l network           | E7:Books (e.g. research monographs)                                                               | E7:Books (e.g. research monographs)                  |
| E14:Doctoral theses completed-supervised by core faculty               | E8:Chapters in books                                                                              | E8:Chapters in books                                 |
| E15:Other(Competitive Research Awards Received)獲重要研究獎項次數      | E9:Textbooks                                                                                      | E9:Textbooks                                         |
| E15:Other(Please describe)其他(科技部學術型計畫 MOST Research Project) | E10:Chapters in textbooks                                                                         | E10:Chapters in textbooks                            |
|                                                                        | E12:Studies and Reports produced as part of an int'l network                                      | E11:Articles on Pedagogic Development and Innovation |
|                                                                        | E15:Other(Competitive Research Awards Received)獲重要研究獎項次數                                 | E13:Published Teaching Materials                     |


**EQUIS的分類定義說明:**

* E1: 期刊論文
* E3: Studies and Reports commissioned by companies and gov't agencies(企業、政府、科技部產學合作計畫)，務必完整填寫有報告產出的案件 / 非科技部研究計劃
* E4: 會議論文
* E7: 專書
* E8: 專書篇章
* E12: 研究報告
* E15: Other(Competitive Research Awards Received)獲重要研究獎項次數
* E15: Other(Please describe)其他(科技部學術型計畫 MOST Research Project)


**EQUIS與AACSB分類對照：**

| EQUIS分類                                                                                         | AACSB分類                                                  |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| E1:Academic Research Articles                                                                     | A10:Editorial-Reviewed Journals and Articles               |
| E2:Practices-oriented Articles                                                                    | A1:Peer-Reviewed Journals                                  |
| E3:Studies and Reports commissioned by companies and gov't agencies(企業、政府、科技部產學合作計畫) | A8:Professional Practice Standards or Public Policy        |
| E4:Papers in Academic conferences                                                                 | A2:Peer-Reviewed Academic/Professional Meeting Proceedings |
| E5:Papers in Professional conferences                                                             | A3:Academic/Professional Meeting Presentations             |
| E6:Published Case Studies                                                                         | A6:Case Studies                                            |
| E7:Books (e.g. research monographs)                                                               | A5:Textbooks                                               |
| E8:Chapters in books                                                                              | A5:Textbooks                                               |
| E9:Textbooks                                                                                      | A5:Textbooks                                               |
| E10:Chapters in textbooks                                                                         | A5:Textbooks                                               |
| E11:Articles on Pedagogic Development and Innovation                                              | A9:Other IC Type Selected by the School                    |
| E12:Studies and Reports produced as part of an int'l network                                      | A9:Other IC Type Selected by the School                    |
| E13:Published Teaching Materials                                                                  | A9:Other IC Type Selected by the School                    |
| E14:Doctoral theses completed-supervised by core faculty                                          | A9:Other IC Type Selected by the School                    |
| E15:Other(Competitive Research Awards Received)獲重要研究獎項次數                                 | A4:Competitive Research Awards Received                    |
| E15:Other(Please describe)其他(科技部學術型計畫 MOST Research Project)                            | A9:Other IC Type Selected by the School                    |


#### ➤此階段資料處理需求：

1. 「與本院教授共同創作」與「與本院學生、本校外院師生、校外人士共同創作」在原始資料中無細分，還有寫法或中英文不一致而難以查找的問題，需要另外判斷或是新增填寫欄位讓老師填寫
2. 可否在教師填寫時，初步判別EQUIS的分類？選項跳出後再由教師進一步確認


### 4.各教師新增、修改與刪除資料

當系所助教完成「A1-A3清單」填寫後，會寄給系上各教師確認內容是否需要修改，同時附上以下「教師履歷表單」請每位教師填寫：

| 欄位名稱                                    | 欄位說明                          |
|-----------------------------------------|-------------------------------|
| 姓名(中文)                                  |                               |
| 姓名(英文)                                  |                               |
| 教育背景 Education                          | 請填英文，包含修業起訖年月、學校與科系|
| 經歷 Teaching and Prefessional Experience | 請填英文                          |
| 教學興趣 Teaching Interests                 | 請填英文                          |
| 研究興趣 Research Interests                 | 請填英文                          |
| 【2024年】近一年教授高管班(指無學位的課程)，如：企家班。         | 有請填1，無請填0                     |
| 【2024年】近一年教學責任-其他服務，如：借調、期刊編輯、主編、審稿     | 有請填1，無請填0                     |
| 【2024年】近一年借調至產學界或政府機關                   | 有請填1，無請填0                     |
| 【2024年】近一年參與產業界的活動或與產業界主管有聯繫互動          | 有請填1，無請填0                     |
| 【2024年】近一年參與產業經營或擔任專業職務                 | 有請填1，無請填0                     |
| 【2024年】近一年於學會/協會組織擔任高階職務                | 有請填1，無請填0                     |
| 【2024年】近一年參與學會/協會團體組織之活動                | 有請填1，無請填0                     |
| 【2024年】近一年長期提供企業諮詢（一年以上）                | 有請填1，無請填0                     |
| 【2024年】近一年擔任董事會（理事會）/監察人（監事）相關職務        | 有請填1，無請填0                     |
| 【2024年】近一年具商管教育經歷並持續累積中                 | 有請填1，無請填0                     |
| 【2024年】近一年參與學術/業界相關之活動/社群/學會/協會         | 有請填1，無請填0                     |
| 【2024年】近一年於業界擔任重要職務                     | 有請填1，無請填0                     |
| 【2024年】近一年具有產業界全職或兼職之工作                 | 有請填1，無請填0                     |
| 【2024年】近一年企業主、合夥人、或專業經理人                | 有請填1，無請填0                     |
| 【2024年】近一年業界活躍人士                        | 有請填1，無請填0                     |
| 【2024年】會計師、律師或擁有其他專業證照                  | 有請填1，無請填0                     |
| 其他職務1                                   | 填寫年份、職務名稱(中文)、職務名稱(英文)、擔任起訖時間 |
| 其他職務2                                   | 填寫年份、職務名稱(中文)、職務名稱(英文)、擔任起訖時間 |
| 其他職務3                                   | 填寫年份、職務名稱(中文)、職務名稱(英文)、擔任起訖時間 |

#### ➤此階段資料處理需求：

1. 與前面的情況類似，每位教師各填一份檔案，就需要有助教另外彙整，是否能建構系統讓教師登入填寫，資料庫便能及時取得相對應的資料，不用人力一一複製貼上。
2. 電算中心檔案「科目與教職員資料」有教師校外兼職名冊，是否使用？

### 5.各系助教彙整系上各教師資料 (產生各系報表)

教師們完成「A1-A3清單」確認與「教師履歷表單」填寫後，由系所助教回收所有教師的個別檔案，並確認資料皆已填上且無誤，即可將每位教師的個別資料匯入系所總表「統整表格」，包括以下三個部分：

#### (1) A1-A3清單總表

注意：調查期間才聘入的老師不需填寫，下年度再填即可

直接將每位教師的「A1-A3清單」貼入總表，讓Excel公式自動計算後續內容。（「學群」與「系所」對照？）

#### (2) 教師履歷總表

注意：調查期間才聘入的老師不需填寫，下年度再填即可

##### a. 第一部分資料：

| 輸入方式 | 欄位名稱      | 欄位說明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 手動   | 員工編號      | 上學期專任，下學期兼任，請一格內填入2個員工編號                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 連結   | 姓名(中文)    | 符合「蒐集對象」的教師皆需填入（無空格），可參照教師履歷                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 連結   | 姓名(英文)    | 請依英文姓氏字母排列，可參照教師履歷                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 手動   | 到職日       | 西元年                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 手動   | 最高學位      | PhD 博士, TAX 稅法碩士, A+L 會計及法律雙碩士, ABD 博士候選人, Master 碩士, Bachelor 學士, Other 其他                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 手動   | 取得最高學位年度  | 西元年                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 手動   | 系所        | Accounting, BA, DBA, EMBA, Finance, Intl Buss, IMBA, MBA, MIS, M & B, RMI, Statistics, TIM & IIP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 手動   |  學群       | Accounting, Actuarial Science, Behavioral Science / Organizational Behavior, Business Communication, Business Education, Business Ethics - incl Corporate Social Responsibility, Business Law / Legal Enviroment, Computer or, Management Information Systems, Consulting, Data Analytics, E-Business - inxl Economics, Economics / Mnagerial Economics, Entrepreneurship / Small Business Admin, Finance - incl Banking, General Business, HR Mgt - incl, Personnel & Ind / Labor Relations, Insurance, Intellectual Property, International Business, Management, Manufacturing and Technology Management, Marketing, Operations Research, Production / Operations Management, Public Administration, Quantitative Methods, Real Estate, Statistics, Strategic Management, Supply Chian / Transport / Logistics, Taxation |
| 手動   | 1121專任/兼任 | 專任, 兼任, (空白，該學期無授課)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 手動   | 1122專任/兼任 | 專任, 兼任, (空白，該學期無授課)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 手動   | Job Title | Professor 教授, Associate Professor 副教授, Assistant Professor 助理教授, Instructor 講師                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |


##### b. 第二部分資料：

| 輸入方式 | 欄位名稱                                       | 欄位說明                               |
|------|--------------------------------------------|------------------------------------|
| 自動   | 授課科目數_1121                                 | 1121科目數加總                          |
| 自動   | 授課科目數_1122                                 | 1122科目數加總                          |
| 手動   | 學士班教學科目數1121                               |                                    |
| 手動   | 學士班教學科目數1122                               |                                    |
| 手動   | MBA教學科目數1121                               |                                    |
| 手動   | MBA教學科目數1122                               |                                    |
| 手動   | IMBA教學科目數1121                              |                                    |
| 手動   | IMBA教學科目數1122                              |                                    |
| 手動   | 一般碩士班教學科目數1121                             |                                    |
| 手動   | 一般碩士班教學科目數1122                             |                                    |
| 手動   | 博士班PhD教學科目數1121                            |                                    |
| 手動   | 博士班PhD教學科目數1122                            |                                    |
| 手動   | EMBA教學科目數1121                              |                                    |
| 手動   | EMBA教學科目數1122                              |                                    |
| 手動   | 博士班DBA教學科目數1121                            |                                    |
| 手動   | 博士班DBA教學科目數1122                            |                                    |
| 自動   | 貢獻度<br/>Percent of Time Devoted to Mission |                                    |
| 自動   | UT                                         | 教授學士班，有為1，無為0                      |
| 自動   | MT                                         | 教授碩士班(含一般碩士、MBA、IMBA、EMBA)，有為1，無為0 |
| 自動   | DT                                         | 教授博士班(含PhD、DBA)，有為1，無為0            |

教學科目數說明：

* 學碩合開課，學0.5、碩0.5；碩博合開課，碩0.5、博0.5。
* 多位教師合授，需乘上實授學分數權重。EX：1門課學碩合開、A老師(1學分)與B老師(2學分)兩位老師合授3學分，A老師的學士班教學科目數 = 1 * 0.5 * (1/3) = 0.17
* 本系老師支援本院外系(除MBA、IMBA、EMBA、DBA)的課要算，但MBA、IMBA、EMBA、DBA由專責辦公室/助教自己算，支援外院的課都不算。
* 只計算有真正實際授課且有學分的課程，如：服務課、外語檢定、教學實習與實務等課程不算。
* 教學科目數另有電算中心檔案「科目與教職員資料」可參考，是否使用？

貢獻度說明：

* 上學期權重50%、下學期權重50%
* 專任填1
* 兼任依範例填寫：開設1門課，填 0.05 * 1門。開設2門課，填 0.05 * 2門
* 如：上學期專任，下學期轉兼任教2門課：1 * 50% + ( 0.05 * 2 ) * 50%


##### c. 第三部分資料：

| 輸入方式 | 欄位名稱                                                            | 欄位說明                                            |
|------|-----------------------------------------------------------------|-------------------------------------------------|
| 連結   | ADM                                                             | 教師履歷：近一年擔任行政職務。                                      |
| 自動   | RES                                                             | 有研究產出，此表：總著作篇數小計>0                              |
| 連結   | ED                                                              | 教師履歷：近一年教授高管班(指無學位的課程)，如：企家班。                   |
| 連結   | SER                                                             | 教師履歷：近一年教學責任-其他服務，如：借調、期刊編輯、主編、審稿               |
| 自動   | 合併教學責任                                                          | 此表UT, MT, DT, ADM, RES, ED, SER，有1者顯示，否則該位置NULL |
| 自動   | Basic or Discovery Scholarship                                  | 學術相關著作個數，計算A1-A3清單：屬性                           |
| 自動   | Applied or Integration/Application Scholarship                  | 實務相關著作個數，計算A1-A3清單：屬性                           |
| 自動   | Teaching and Learning Scholarship                               | 教學相關著作個數，計算A1-A3清單：屬性                           |
| 自動   | 總著作篇數小計                                                         | 前三個欄位相加                                         |
| 自動   | 總著作篇數*貢獻度                                                       | For TABLE2-1                                    |
| 自動   | PRJ                                                             | A1-有審閱制度期刊篇數，A1-A3清單：AACSB分類為A1的加總              |
| 自動   | Additional Peer- or Editorial-Review Intellectual Contributions | A2-有審閱制度會議論文篇數，A1-A3清單：AACSB分類為A2的加總            |
| 自動   | All Other Intellectual Contributions                            | A3-有審閱制度會議發表篇數，A1-A3清單：AACSB分類為A3的加總            |
| 自動   | 驗算欄                                                             | 前三欄加總減去總著作篇數小計，正確應該等於0。                         |

註：欄位ADM「教師履歷：近一年擔任行政職務。」不太確定，沒對應到

##### d. 第四部分資料：

| 輸入方式 | 欄位名稱      | 欄位說明                                                                                                                                                                                                            |
|------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 自動   | 教師分類SA    | 學術導向學者﻿: ﻿若﻿此表SA0>0﻿或(SA1==1﻿且sum(SA1-1,SA1-2, SA1-3)>0)﻿﻿，該值為1﻿，﻿否則為0                                                                                                                                          |
| 自動   | 教師分類PA    | 技術導向學者﻿: 若﻿此表﻿教師分類SA==1﻿﻿則為0﻿；否則﻿﻿﻿，若PA1==1﻿且PA1a==1﻿且sum(PA1-1﻿至PA1-8)>=2，﻿﻿﻿該值為1﻿，﻿否則﻿為0                                                                                                                     |
| 自動   | 教師分類SP    | 學術導向專業技術人員﻿: 若﻿此表教師分類SA+﻿教師分類PA==1﻿，﻿﻿返回0﻿；﻿否則﻿，﻿若SP1==1﻿且sum﻿(﻿S﻿P1-1, SP1-2, SP1-3)>=2﻿，﻿﻿返回1，﻿否則﻿為﻿0                                                                                                         |
| 自動   | 教師分類IP    | 實務導向專業技術人員﻿: 若﻿教師分類SA+PA+SP==1﻿，﻿則該值為0﻿；﻿否則﻿，﻿若IP1==1﻿且﻿I﻿P1a==1﻿且sum(﻿I﻿P1-1﻿至IP1-5)>=1﻿，﻿返回1﻿，﻿否則為0                                                                                                           |
| 自動   | 教師分類Other | 其他類﻿: 若SA+PA+SP+IP>0﻿，﻿﻿該值為0﻿，﻿否則為1                                                                                                                                                                             |
| 自動   | SA0       | 取得ABD資格未超過三年，直接是SA，不論﻿前三個條件﻿﻿:﻿ ﻿﻿若此表﻿最高學位﻿為ABD﻿且取得最高學位年度>=2014﻿，﻿則該值為1﻿，﻿否則為0                                                                                                                                  |
| 自動   | SA1       | 博士或法律、稅法碩士(SA1+SA1-1、SA1-2、SA1-3一項以上資格﻿): ﻿﻿若﻿此表最高學位﻿為PhD﻿或TAX﻿或A+L﻿，﻿則該值為1﻿，﻿否則為0                                                                                                                              |
| 自動   | SA1-1     | 五年內獲得博士頭銜的新聘教師﻿: 若此表﻿最高學位﻿為PhD﻿且取得最高學位年度>=報告資料區間第一年﻿(﻿此份為2019﻿年)，﻿則該值為1﻿，﻿否則為0                                                                                                                                  |
| 自動   | SA1-2     | 五年內有三篇著作發表於A1有審閱制度期刊﻿: ﻿﻿若此表PRJ>=3﻿，該值為1，﻿否則為0                                                                                                                                                                  |
| 自動   | SA1-3     | 五年內有二篇或以上著作發表於A1有審閱制度的期刊，並有二篇或以上符合AACSB  8項IC指標(A2-A9): ﻿若此表PRJ>=2﻿且(Additional Peer- or Editorial-Review Intellectual Contributions + All Other Intellectual Contributions) >= 2﻿，﻿則該值為1﻿，﻿否則為0                |
| 自動   | PA1       | 博士學位(PA1+PA1a，且符合下列PA1-1~PA1-8兩項以上資格): ﻿若此表﻿最高學位﻿為PhD﻿則為1﻿，﻿否則為0                                                                                                                                                |
| 自動   | PA1a      | 五年內有一篇或以上著作發表於有審閱制度的期刊(A1)，或有兩篇或以上著作符合AACSB  IC指標(A2-A3): ﻿若此表PRJ>=1﻿，﻿則該值為1﻿；否則﻿，﻿若(Additional Peer- or Editorial-Review Intellectual Contributions + All Other Intellectual Contributions) >= 2﻿，﻿該值為1﻿，﻿否則為0 |

註：SA0欄位待確認，還不確定要從哪個年份往前推三年

##### e. 第五部分資料：

| 輸入方式 | 欄位名稱                                   | 欄位說明                                                                                                                                                                                                                                       |
|------|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 連結   | PA1-1 & IP1-1                          | ﻿教師履歷: ﻿近一年借調至產學界或政府機關                                                                                                                                                                                                                     |
| 連結   | PA1-2                                  | 教師履歷: ﻿近一年參與產業界的活動或與產業界主管有聯繫互動                                                                                                                                                                                                             |
| 連結   | PA1-3                                  | 教師履歷: ﻿近一年參與產業經營或擔任專業職務                                                                                                                                                                                                                    |
| 連結   | PA1-4                                  | 教師履歷: ﻿近一年於學會/協會組織擔任高階職務                                                                                                                                                                                                                   |
| 連結   | PA1-5                                  | 教師履歷: ﻿近一年參與學會/協會團體組織之活動                                                                                                                                                                                                                   |
| 連結   | PA1-6                                  | 教師履歷: ﻿近一年長期提供企業諮詢（一年以上）                                                                                                                                                                                                                   |
| 連結   | PA1-7 & IP1-3                          | 教師履歷: ﻿近一年擔任董事會（理事會）/監察人（監事）相關職務                                                                                                                                                                                                           |
| 連結   | PA1-8 & SP1-3                          | 教師履歷: ﻿近一年具商管教育經歷並持續累積中                                                                                                                                                                                                                    |
| ﻿自動  | SP1                                    | 碩士以上學位，五年內有一篇或以上著作發表，並符合AACSB  IC指標。(含A1-A9, SP1+1-1~1-3兩項以上資格)﻿:﻿ ﻿此表中﻿最高學位﻿為PhD, TAX, A+L, ABD﻿或Master﻿，﻿且(PRJ + Additional Peer- or Editorial-Review Intellectual Contributions + All Other Intellectual Contributions)>0﻿，﻿則該值為1﻿，否則為0 |
| 連結   | SP1-1                                  | 教師履歷: ﻿近一年參與學術/業界相關之活動/社群/學會/協會                                                                                                                                                                                                            |
| 連結   | SP1-2                                  | 教師履歷: ﻿近一年於業界擔任重要職務                                                                                                                                                                                                                        |
| 連結   | IP1                                    | 碩士以上學位(IP1+IP1a+1-1~1-5一項以上資格): ﻿此表中﻿最高學位﻿為PhD, TAX, A+L, ABD﻿或Master﻿﻿，﻿則該值為1﻿，﻿否則為0                                                                                                                                                      |
| 連結   | IP1a                                   | 教師履歷: ﻿近一年具有產業界全職或兼職之工作                                                                                                                                                                                                                    |
| 連結   | IP1-2                                  | 教師履歷: ﻿近一年企業主、合夥人、或專業經理人                                                                                                                                                                                                                   |
| 連結   | IP1-4                                  | 教師履歷: ﻿近一年業界活躍人士                                                                                                                                                                                                                           |
| 連結   | IP1-5                                  | 教師履歷: ﻿近一年會計師、律師或擁有其他專業證照                                                                                                                                                                                                                  |
| 連結   | 教育背景Education                          | 輸入英文                                                                                                                                                                                                                                       |
| 連結   | 經歷Teaching and Prefessional Experience | 輸入英文                                                                                                                                                                                                                                       |
| 連結   | 教學興趣Teaching Interests                 | 輸入英文                                                                                                                                                                                                                                       |
| 連結   | 研究興趣Research Interests                 | 輸入英文                                                                                                                                                                                                                                       |

##### f. 第六部分資料：

(給特定TABLE使用的資料，暫不顯示，待完成)

#### (3) 產生各系報表

(可能改貼報表的圖片)

##### TABLE 8-1A

| Part A: Five-Year Summary of the Intellectual Contributions                                                                                                                                                         |                                              |                                                             |                                                |        |                                                        |                                                                                  |                                                 |        |                                                                                 |                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------|------------------------------------------------|--------|--------------------------------------------------------|----------------------------------------------------------------------------------|-------------------------------------------------|--------|---------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Faculty*<br/>Aggregate and summarize data to reflect the organizational structure of the school's faculty (e.g., departments, research groups). Do not list by individual faculty member.<br/>依系所（或研究學群）呈現專兼任教師論著資訊 | Portfolio of Intellectual Contributions      |                                                             |                                                |        | Types of Intellectual Contributions                    |                                                                                  |                                                 |        | Percentages of Faculty Producing ICs                                            |                                                                            |
|                                                                                                                                                                                                                     | Basic or Discovery Scholarship <br/>學術相關論著篇數 | Applied or Integration/Application Scholarship<br/>實務相關論著篇數 | Teaching and Learning Scholarship<br/>教學相關論著篇數 | Total* | Peer-Reviewed Journal Articles<br/>有審閱制度期刊及論文篇數/會議論文篇數 | Additional Peer- or Editorial-Review Intellectual Contributions<br/>其他有審閱制度的學術貢獻 | All Other Intellectual Contributions<br/>其他學術貢獻 | Total* | Percent of Participating Faculty Producing ICs*<br/>專任教師論著百分比 （該系所專任篇數/該系所全部篇數） | Percentage of Total Full Time Equivalent (FTE) Faculty Producing ICs*<br/> |
| Accounting                                                                                                                                                                                                          | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| BA                                                                                                                                                                                                                  | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| DBA                                                                                                                                                                                                                 | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| EMBA                                                                                                                                                                                                                | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Finance                                                                                                                                                                                                             | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Intl Buss                                                                                                                                                                                                           | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| IMBA                                                                                                                                                                                                                | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| MBA                                                                                                                                                                                                                 | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| MIS                                                                                                                                                                                                                 | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| M & B                                                                                                                                                                                                               | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| RMI                                                                                                                                                                                                                 | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Statistics                                                                                                                                                                                                          | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| TIM & IIP                                                                                                                                                                                                           | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Grand Total                                                                                                                                                                                                         | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |

##### TABLE 8-1B

| Part A: Five-Year Summary of the Intellectual Contributions                                                                                                                                                         |                                              |                                                             |                                                |        |                                                        |                                                                                  |                                                 |        |                                                                                 |                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------|------------------------------------------------|--------|--------------------------------------------------------|----------------------------------------------------------------------------------|-------------------------------------------------|--------|---------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Faculty*<br/>Aggregate and summarize data to reflect the organizational structure of the school's faculty (e.g., departments, research groups). Do not list by individual faculty member.<br/>依系所（或研究學群）呈現專兼任教師論著資訊 | Portfolio of Intellectual Contributions      |                                                             |                                                |        | Types of Intellectual Contributions                    |                                                                                  |                                                 |        | Percentages of Faculty Producing ICs                                            |                                                                            |
|                                                                                                                                                                                                                     | Basic or Discovery Scholarship <br/>學術相關論著篇數 | Applied or Integration/Application Scholarship<br/>實務相關論著篇數 | Teaching and Learning Scholarship<br/>教學相關論著篇數 | Total* | Peer-Reviewed Journal Articles<br/>有審閱制度期刊及論文篇數/會議論文篇數 | Additional Peer- or Editorial-Review Intellectual Contributions<br/>其他有審閱制度的學術貢獻 | All Other Intellectual Contributions<br/>其他學術貢獻 | Total* | Percent of Participating Faculty Producing ICs*<br/>專任教師論著百分比 （該學群專任篇數/該學群全部篇數） | Percentage of Total Full Time Equivalent (FTE) Faculty Producing ICs*<br/> |
| Accounting                                                                                                                                                                                                          | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Actuarial Science                                                                                                                                                                                                   | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Behavioral Science / Organizational Behavior                                                                                                                                                                        | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Business Communication                                                                                                                                                                                              | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Business Education                                                                                                                                                                                                  | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Business Ethics - incl Corporate Social Responsibility                                                                                                                                                              | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Business Law / Legal Enviroment                                                                                                                                                                                     | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Computer or Management Information Systems                                                                                                                                                                          | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Consulting                                                                                                                                                                                                          | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Data Analytics                                                                                                                                                                                                      | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| E-Business - inxl Economics                                                                                                                                                                                         | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Economics / Mnagerial Economics                                                                                                                                                                                     | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Entrepreneurship / Small Business Admin                                                                                                                                                                             | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Finance - incl Banking                                                                                                                                                                                              | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| General Business                                                                                                                                                                                                    | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| HR Mgt - incl Personnel & Ind / Labor Relations                                                                                                                                                                     | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Insurance                                                                                                                                                                                                           | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Intellectual Property                                                                                                                                                                                               | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| International Business                                                                                                                                                                                              | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Management                                                                                                                                                                                                          | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Manufacturing and Technology Management                                                                                                                                                                             | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Marketing                                                                                                                                                                                                           | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Operations Research                                                                                                                                                                                                 | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Production / Operations Management                                                                                                                                                                                  | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Public Administration                                                                                                                                                                                               | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Quantitative Methods                                                                                                                                                                                                | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Real Estate                                                                                                                                                                                                         | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Statistics                                                                                                                                                                                                          | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Strategic Management                                                                                                                                                                                                | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Supply Chian / Transport / Logistics                                                                                                                                                                                | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Taxation                                                                                                                                                                                                            | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |                                                                                 |                                                                            |
| Grand Total                                                                                                                                                                                                         | 0                                            | 0                                                           | 0                                              | 0      | 0                                                      | 0                                                                                | 0                                               | 0      |

（以下TABLE待完成）

##### TABLE 3-1

##### TABLE 3-2

##### TABLE 3-2B_學士班

##### TABLE 3-2B_MBA Program

##### TABLE 3-2B_MBA

##### TABLE 3-2B_IMBA

##### TABLE 3-2B_碩士班

##### TABLE 3-2B_EMBA

##### TABLE 3-2B_DBA

##### TABLE 3-2B_博士班

#### ➤此階段資料處理需求：

1. 減輕各系助教重複複製貼上的動作
2. 有些資料在其他地方已有，不需要一直手動輸入
3. 自動化產生出上述眾多TABLE（各系報表）
4. 教師履歷研究興趣等內容，是否要限制輸入格式


### 6.認證辦公室彙整各系教師資料

各系報表產出後，會由認證辦公室回收所有報表並彙整成全院總報表（有Word檔可參考，機密資料不可外流），並提交給學院確認。

#### ➤此階段資料處理需求：

1. 同樣解決重複複製貼上的動作


### 7.學院進行最後確認

學院確認完畢後，即可彙整進國際認證報告書，準備提交給認證單位審核。


# 教師履歷管理系統設計

（待討論）