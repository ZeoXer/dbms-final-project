# Data Preprocessing

<a id='toc0_'></a>    
- [Department 系所](#toc1_)    
- [PartTime 校外兼職](#toc2_)    
- [Teacher & FacultyType & Class](#toc3_)    
  - [Teacher 教師](#toc3_1_)    
  - [FacultyType 專兼別](#toc3_2_)    
  - [Class 開課時數](#toc3_3_)    
- [List 學術、實務與教學貢獻清單](#toc4_)    
  - [論著資料](#toc4_1_)    
  - [研究計畫](#toc4_2_)    
  - [獎項](#toc4_3_)    
- [Resume 教師履歷](#toc5_)    

<!-- vscode-jupyter-toc-config
	numbering=true
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[Department 系所](#toc0_)


```python
import pandas as pd
import numpy as np
```


```python
dep = pd.read_csv('dataset/Department.csv')
dep['department_Cname_simple'] = ['商學院','國貿系','金融系','會計系','統計系','企管系','資管系','財管系','風管系','企研所(MBA學位學程)','科管智財所','營管碩','國營碩','產業博','外院'] # 後續資料整理用
dep
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>department_id</th>
      <th>department_Ename</th>
      <th>department_Cname</th>
      <th>department_Cname_simple</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>300</td>
      <td>College of Commerce</td>
      <td>商學院</td>
      <td>商學院</td>
    </tr>
    <tr>
      <th>1</th>
      <td>301</td>
      <td>Intl Buss</td>
      <td>國際經營與貿易學系</td>
      <td>國貿系</td>
    </tr>
    <tr>
      <th>2</th>
      <td>302</td>
      <td>Finance</td>
      <td>金融學系</td>
      <td>金融系</td>
    </tr>
    <tr>
      <th>3</th>
      <td>303</td>
      <td>Accounting</td>
      <td>會計學系</td>
      <td>會計系</td>
    </tr>
    <tr>
      <th>4</th>
      <td>304</td>
      <td>Statistics</td>
      <td>統計學系</td>
      <td>統計系</td>
    </tr>
    <tr>
      <th>5</th>
      <td>305</td>
      <td>BA</td>
      <td>企業管理學系</td>
      <td>企管系</td>
    </tr>
    <tr>
      <th>6</th>
      <td>306</td>
      <td>MIS</td>
      <td>資訊管理學系</td>
      <td>資管系</td>
    </tr>
    <tr>
      <th>7</th>
      <td>307</td>
      <td>M &amp; B</td>
      <td>財務管理學系</td>
      <td>財管系</td>
    </tr>
    <tr>
      <th>8</th>
      <td>308</td>
      <td>RMI</td>
      <td>風險管理與保險學系</td>
      <td>風管系</td>
    </tr>
    <tr>
      <th>9</th>
      <td>363</td>
      <td>MBA</td>
      <td>企業管理研究所(MBA)</td>
      <td>企研所(MBA學位學程)</td>
    </tr>
    <tr>
      <th>10</th>
      <td>364</td>
      <td>TIM &amp; IIP</td>
      <td>科技管理與智慧財產研究所</td>
      <td>科管智財所</td>
    </tr>
    <tr>
      <th>11</th>
      <td>932</td>
      <td>EMBA</td>
      <td>經營管理碩士學程(EMBA)</td>
      <td>營管碩</td>
    </tr>
    <tr>
      <th>12</th>
      <td>933</td>
      <td>IMBA</td>
      <td>國際經營管理英語碩士學位學程(IMBA)</td>
      <td>國營碩</td>
    </tr>
    <tr>
      <th>13</th>
      <td>998</td>
      <td>DBA</td>
      <td>產業組博士學位學程(DBA)</td>
      <td>產業博</td>
    </tr>
    <tr>
      <th>14</th>
      <td>999</td>
      <td>Others</td>
      <td>外院</td>
      <td>外院</td>
    </tr>
  </tbody>
</table>
</div>



# <a id='toc2_'></a>[PartTime 校外兼職](#toc0_)


```python
parttime = pd.read_excel('raw_data/電算中心原始資料.xlsx', sheet_name='112學年度商學院教師至校外兼職名冊') # 要刪除原始excel檔的第一列
parttime.rename(columns={'員工代號':'teacher_id', '兼職機關':'pt_company', '兼職單位':'pt_department', '兼職職稱':'pt_position','兼職起日':'pt_start','兼職迄日':'pt_end'}, inplace=True)
parttime.drop(columns=['序號','姓名','單位','職稱'], inplace=True)
parttime.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>pt_company</th>
      <th>pt_department</th>
      <th>pt_position</th>
      <th>pt_start</th>
      <th>pt_end</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>301018</td>
      <td>美喆國際股份有限公司</td>
      <td>NaN</td>
      <td>獨立董事</td>
      <td>110/08/12</td>
      <td>113/08/11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>301018</td>
      <td>新盛力科技股份有限公司</td>
      <td>NaN</td>
      <td>獨立董事、薪資報酬委員暨審計委員</td>
      <td>111/09/07</td>
      <td>114/09/06</td>
    </tr>
    <tr>
      <th>2</th>
      <td>103902</td>
      <td>行政院環境保護署</td>
      <td>第4屆溫室氣體管理基金管理會</td>
      <td>委員</td>
      <td>111/06/01</td>
      <td>113/05/31</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 民國年轉換為西元年
def pt_year(pt_original):
    temp = pt_original.split('/')
    temp[0] = str(int(temp[0])+1911)
    return '/'.join(temp)

parttime['pt_start'] = parttime['pt_start'].apply(lambda x: pt_year(x))
parttime['pt_end'] = parttime['pt_end'].apply(lambda x: pt_year(x))

print(parttime.shape)
parttime.head(3)
```

    (196, 6)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>pt_company</th>
      <th>pt_department</th>
      <th>pt_position</th>
      <th>pt_start</th>
      <th>pt_end</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>301018</td>
      <td>美喆國際股份有限公司</td>
      <td>NaN</td>
      <td>獨立董事</td>
      <td>2021/08/12</td>
      <td>2024/08/11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>301018</td>
      <td>新盛力科技股份有限公司</td>
      <td>NaN</td>
      <td>獨立董事、薪資報酬委員暨審計委員</td>
      <td>2022/09/07</td>
      <td>2025/09/06</td>
    </tr>
    <tr>
      <th>2</th>
      <td>103902</td>
      <td>行政院環境保護署</td>
      <td>第4屆溫室氣體管理基金管理會</td>
      <td>委員</td>
      <td>2022/06/01</td>
      <td>2024/05/31</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 確認是否unique(是否有重複的row)
parttime.duplicated().sum()
```




    0




```python
# 匯出
parttime.to_csv('dataset/PartTime.csv', index=False)
```

# <a id='toc3_'></a>[Teacher & FacultyType & Class](#toc0_)


```python
# 合併112學年度第一二學期開課資料
fullyear = pd.DataFrame()

# 112-1
temp = pd.read_excel('raw_data/電算中心原始資料.xlsx', sheet_name='112-1商學院專兼任教師開課時數表')
temp.drop(columns=['序號','性別'], inplace=True)
temp.rename(columns={'姓名':'Cname', '員工編號':'teacher_id', '單位名稱':'department_Cname_simple', '教師任職':'teacher_type'}, inplace=True)
temp_colname = temp.columns.tolist()
temp_colname[5:] = ['學士班', 'MBA', 'IMBA', '一般碩士班', '博士班', 'EMBA', 'DBA']
temp.columns = temp_colname # 更改欄位名稱
temp['year'] = 112 # 紀錄資料所屬學年度
temp['semester'] = 1 # 紀錄資料所屬學期
fullyear = pd.concat([fullyear, temp], axis=0)

# 112-2
temp = pd.read_excel('raw_data/電算中心原始資料.xlsx', sheet_name='112-2商學院專兼任教師開課時數表')
temp.drop(columns=['序號','性別'], inplace=True)
temp.rename(columns={'姓名':'Cname', '員工編號':'teacher_id', '單位名稱':'department_Cname_simple', '教師任職':'teacher_type'}, inplace=True)
temp_colname = temp.columns.tolist()
temp_colname[5:] = ['學士班', 'MBA', 'IMBA', '一般碩士班', '博士班', 'EMBA', 'DBA']
temp.columns = temp_colname # 更改欄位名稱
temp['year'] = 112 # 紀錄資料所屬學年度
temp['semester'] = 2 # 紀錄資料所屬學期
fullyear = pd.concat([fullyear, temp], axis=0)

print(fullyear.shape)
fullyear.head(3)
```

    (533, 14)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cname</th>
      <th>teacher_id</th>
      <th>department_Cname_simple</th>
      <th>teacher_type</th>
      <th>職稱</th>
      <th>學士班</th>
      <th>MBA</th>
      <th>IMBA</th>
      <th>一般碩士班</th>
      <th>博士班</th>
      <th>EMBA</th>
      <th>DBA</th>
      <th>year</th>
      <th>semester</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>于紀隆</td>
      <td>114576</td>
      <td>會計系</td>
      <td>兼任</td>
      <td>教授級約聘教學人員</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>112</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>王文英</td>
      <td>101476</td>
      <td>會計系</td>
      <td>專任</td>
      <td>教授</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>112</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王正偉</td>
      <td>308001</td>
      <td>風管系</td>
      <td>專任</td>
      <td>講師</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>112</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## <a id='toc3_1_'></a>[Teacher 教師](#toc0_)


```python
teacher = fullyear[['teacher_id','Cname','職稱','department_Cname_simple']].copy() # 補：Ename, job_title, year, dep_id
teacher
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>Cname</th>
      <th>職稱</th>
      <th>department_Cname_simple</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>114576</td>
      <td>于紀隆</td>
      <td>教授級約聘教學人員</td>
      <td>會計系</td>
    </tr>
    <tr>
      <th>1</th>
      <td>101476</td>
      <td>王文英</td>
      <td>教授</td>
      <td>會計系</td>
    </tr>
    <tr>
      <th>2</th>
      <td>308001</td>
      <td>王正偉</td>
      <td>講師</td>
      <td>風管系</td>
    </tr>
    <tr>
      <th>3</th>
      <td>104280</td>
      <td>王采彤</td>
      <td>助教</td>
      <td>財管系</td>
    </tr>
    <tr>
      <th>4</th>
      <td>101881</td>
      <td>王淑珍</td>
      <td>助教</td>
      <td>會計系</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>250</th>
      <td>107991</td>
      <td>羅明琇</td>
      <td>教授</td>
      <td>企管系</td>
    </tr>
    <tr>
      <th>251</th>
      <td>128808</td>
      <td>羅秉政</td>
      <td>助理教授</td>
      <td>金融系</td>
    </tr>
    <tr>
      <th>252</th>
      <td>102104</td>
      <td>譚丹琪</td>
      <td>教授</td>
      <td>國貿系</td>
    </tr>
    <tr>
      <th>253</th>
      <td>122580</td>
      <td>蘇瓜藤</td>
      <td>教授</td>
      <td>會計系</td>
    </tr>
    <tr>
      <th>254</th>
      <td>117118</td>
      <td>蘇威傑</td>
      <td>教授</td>
      <td>國貿系</td>
    </tr>
  </tbody>
</table>
<p>533 rows × 4 columns</p>
</div>




```python
# job_title: 取代職稱並轉換成英文
eng_jt = {
    '教授': 'Professor',
    '副教授': 'Associate Professor',
    '助理教授': 'Assistant Professor',
    '講師': 'Instructor'
}
teacher['job_title'] = teacher['職稱'].str.replace('級約聘教學人員|級專業技術人員', '', regex=True).replace(eng_jt)

teacher
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>Cname</th>
      <th>職稱</th>
      <th>department_Cname_simple</th>
      <th>job_title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>114576</td>
      <td>于紀隆</td>
      <td>教授級約聘教學人員</td>
      <td>會計系</td>
      <td>Professor</td>
    </tr>
    <tr>
      <th>1</th>
      <td>101476</td>
      <td>王文英</td>
      <td>教授</td>
      <td>會計系</td>
      <td>Professor</td>
    </tr>
    <tr>
      <th>2</th>
      <td>308001</td>
      <td>王正偉</td>
      <td>講師</td>
      <td>風管系</td>
      <td>Instructor</td>
    </tr>
    <tr>
      <th>3</th>
      <td>104280</td>
      <td>王采彤</td>
      <td>助教</td>
      <td>財管系</td>
      <td>助教</td>
    </tr>
    <tr>
      <th>4</th>
      <td>101881</td>
      <td>王淑珍</td>
      <td>助教</td>
      <td>會計系</td>
      <td>助教</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>250</th>
      <td>107991</td>
      <td>羅明琇</td>
      <td>教授</td>
      <td>企管系</td>
      <td>Professor</td>
    </tr>
    <tr>
      <th>251</th>
      <td>128808</td>
      <td>羅秉政</td>
      <td>助理教授</td>
      <td>金融系</td>
      <td>Assistant Professor</td>
    </tr>
    <tr>
      <th>252</th>
      <td>102104</td>
      <td>譚丹琪</td>
      <td>教授</td>
      <td>國貿系</td>
      <td>Professor</td>
    </tr>
    <tr>
      <th>253</th>
      <td>122580</td>
      <td>蘇瓜藤</td>
      <td>教授</td>
      <td>會計系</td>
      <td>Professor</td>
    </tr>
    <tr>
      <th>254</th>
      <td>117118</td>
      <td>蘇威傑</td>
      <td>教授</td>
      <td>國貿系</td>
      <td>Professor</td>
    </tr>
  </tbody>
</table>
<p>533 rows × 5 columns</p>
</div>




```python
# dep_id: 從dep帶入
teacher = teacher.merge(dep[['department_id','department_Cname_simple']].rename(columns={'department_id':'dep_id'}), on='department_Cname_simple', how='left')
teacher.drop(columns=['職稱','department_Cname_simple'], inplace=True)

teacher
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>Cname</th>
      <th>job_title</th>
      <th>dep_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>114576</td>
      <td>于紀隆</td>
      <td>Professor</td>
      <td>303</td>
    </tr>
    <tr>
      <th>1</th>
      <td>101476</td>
      <td>王文英</td>
      <td>Professor</td>
      <td>303</td>
    </tr>
    <tr>
      <th>2</th>
      <td>308001</td>
      <td>王正偉</td>
      <td>Instructor</td>
      <td>308</td>
    </tr>
    <tr>
      <th>3</th>
      <td>104280</td>
      <td>王采彤</td>
      <td>助教</td>
      <td>307</td>
    </tr>
    <tr>
      <th>4</th>
      <td>101881</td>
      <td>王淑珍</td>
      <td>助教</td>
      <td>303</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>528</th>
      <td>107991</td>
      <td>羅明琇</td>
      <td>Professor</td>
      <td>305</td>
    </tr>
    <tr>
      <th>529</th>
      <td>128808</td>
      <td>羅秉政</td>
      <td>Assistant Professor</td>
      <td>302</td>
    </tr>
    <tr>
      <th>530</th>
      <td>102104</td>
      <td>譚丹琪</td>
      <td>Professor</td>
      <td>301</td>
    </tr>
    <tr>
      <th>531</th>
      <td>122580</td>
      <td>蘇瓜藤</td>
      <td>Professor</td>
      <td>303</td>
    </tr>
    <tr>
      <th>532</th>
      <td>117118</td>
      <td>蘇威傑</td>
      <td>Professor</td>
      <td>301</td>
    </tr>
  </tbody>
</table>
<p>533 rows × 4 columns</p>
</div>




```python
# Ename, year: 參考2021教師履歷資料(因目前商學院沒有同名同姓的老師，所以直接用姓名merge)
temp = pd.read_csv('raw_data/Teacher_temp.csv')
temp.rename(columns={'姓名(中文)':'Cname','姓名(英文)':'Ename','到職日':'year'}, inplace=True)
temp.drop_duplicates(['Cname'], inplace=True)
teacher = teacher.merge(temp[['Cname','Ename','year']], how='left', on='Cname')
teacher.drop_duplicates(subset=['teacher_id'], keep='last', inplace=True) # 因資料為112第一與第二學期名單，故上下學期可能會有重複值，重複值選擇保留第二學期的 job_title & dep_id
teacher = teacher[['teacher_id','Cname','Ename','job_title','year','dep_id']]
teacher
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>Cname</th>
      <th>Ename</th>
      <th>job_title</th>
      <th>year</th>
      <th>dep_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>125929</td>
      <td>王智弘</td>
      <td>Wang, Jason Chih-Hung</td>
      <td>Associate Professor</td>
      <td>2019.0</td>
      <td>300</td>
    </tr>
    <tr>
      <th>19</th>
      <td>111283</td>
      <td>何小台</td>
      <td>Ho, Chester S.</td>
      <td>Professor</td>
      <td>2010.0</td>
      <td>933</td>
    </tr>
    <tr>
      <th>47</th>
      <td>129823</td>
      <td>李鐘培</td>
      <td>NaN</td>
      <td>Professor</td>
      <td>NaN</td>
      <td>933</td>
    </tr>
    <tr>
      <th>50</th>
      <td>127335</td>
      <td>汪志謙</td>
      <td>Wang, Chih-Chien</td>
      <td>Associate Professor</td>
      <td>2019.0</td>
      <td>300</td>
    </tr>
    <tr>
      <th>52</th>
      <td>131347</td>
      <td>車麗梅</td>
      <td>NaN</td>
      <td>Professor</td>
      <td>NaN</td>
      <td>303</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>528</th>
      <td>107991</td>
      <td>羅明琇</td>
      <td>Lo, Ming-Shiow</td>
      <td>Professor</td>
      <td>2008.0</td>
      <td>305</td>
    </tr>
    <tr>
      <th>529</th>
      <td>128808</td>
      <td>羅秉政</td>
      <td>NaN</td>
      <td>Assistant Professor</td>
      <td>NaN</td>
      <td>302</td>
    </tr>
    <tr>
      <th>530</th>
      <td>102104</td>
      <td>譚丹琪</td>
      <td>Tan, Dan-Chi</td>
      <td>Professor</td>
      <td>2001.0</td>
      <td>301</td>
    </tr>
    <tr>
      <th>531</th>
      <td>122580</td>
      <td>蘇瓜藤</td>
      <td>Su, Robert K.</td>
      <td>Professor</td>
      <td>1992.0</td>
      <td>303</td>
    </tr>
    <tr>
      <th>532</th>
      <td>117118</td>
      <td>蘇威傑</td>
      <td>Su, Wei-Chieh</td>
      <td>Professor</td>
      <td>2013.0</td>
      <td>301</td>
    </tr>
  </tbody>
</table>
<p>294 rows × 6 columns</p>
</div>




```python
# 若上述改成
# teacher.drop_duplicates(subset=['teacher_id','dep_id'], keep='last', inplace=True)
# 此時執行以下
# teacher[teacher['teacher_id'].isin(teacher['teacher_id'][teacher['teacher_id'].duplicated()].tolist())].sort_values(by='teacher_id')
# 會發現有老師轉換系所
```


```python
# 將原始資料教師清單+2021教師履歷所取得的資料，合併到teacher中
temp2 = pd.read_csv('raw_data/Teacher_temp2.csv')
temp2.dropna(inplace=True)
add_id = set(temp2['teacher_id'])-set(teacher['teacher_id'])
teacher = pd.concat([teacher, temp2[temp2['teacher_id'].isin(add_id)]], axis=0)
teacher
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>Cname</th>
      <th>Ename</th>
      <th>job_title</th>
      <th>year</th>
      <th>dep_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>125929</td>
      <td>王智弘</td>
      <td>Wang, Jason Chih-Hung</td>
      <td>Associate Professor</td>
      <td>2019.0</td>
      <td>300</td>
    </tr>
    <tr>
      <th>19</th>
      <td>111283</td>
      <td>何小台</td>
      <td>Ho, Chester S.</td>
      <td>Professor</td>
      <td>2010.0</td>
      <td>933</td>
    </tr>
    <tr>
      <th>47</th>
      <td>129823</td>
      <td>李鐘培</td>
      <td>NaN</td>
      <td>Professor</td>
      <td>NaN</td>
      <td>933</td>
    </tr>
    <tr>
      <th>50</th>
      <td>127335</td>
      <td>汪志謙</td>
      <td>Wang, Chih-Chien</td>
      <td>Associate Professor</td>
      <td>2019.0</td>
      <td>300</td>
    </tr>
    <tr>
      <th>52</th>
      <td>131347</td>
      <td>車麗梅</td>
      <td>NaN</td>
      <td>Professor</td>
      <td>NaN</td>
      <td>303</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>388</th>
      <td>126856</td>
      <td>黃冠華</td>
      <td>Huang, Sunny</td>
      <td>Assistant Professor</td>
      <td>2020.0</td>
      <td>300</td>
    </tr>
    <tr>
      <th>390</th>
      <td>104856</td>
      <td>黃台心</td>
      <td>Huang, Tai-Hsin</td>
      <td>Professor</td>
      <td>2005.0</td>
      <td>302</td>
    </tr>
    <tr>
      <th>404</th>
      <td>305011</td>
      <td>黃秉德</td>
      <td>Huang, Ping-Der</td>
      <td>Associate Professor</td>
      <td>1991.0</td>
      <td>305</td>
    </tr>
    <tr>
      <th>406</th>
      <td>303507</td>
      <td>黃金發</td>
      <td>Hwang, Jin-Fa</td>
      <td>Associate Professor</td>
      <td>1980.0</td>
      <td>303</td>
    </tr>
    <tr>
      <th>407</th>
      <td>123155</td>
      <td>黃韋仁</td>
      <td>Huang, Wei-Jen</td>
      <td>Instructor</td>
      <td>2017.0</td>
      <td>305</td>
    </tr>
  </tbody>
</table>
<p>368 rows × 6 columns</p>
</div>




```python
# 確認是否unique(是否有重複的row)
teacher['teacher_id'].duplicated().sum()
```




    0




```python
# 匯出
teacher.to_csv('dataset/Teacher.csv', index=False)
```


```python
# 補充：2021教師履歷有但商學院教師名單沒有的教師（應為外院教師）
print(set(temp['Cname'])-set(teacher['Cname']))
```

    {'周振鋒', '王文杰', '洪德欽', '冷則剛', '丁克華', '周德宇', '沈宗倫', '朱德芳', '沈錳坤', '林祖嘉', '朱芳妮', '吳文傑', '林日璇'}


## <a id='toc3_2_'></a>[FacultyType 專兼別](#toc0_)


```python
fullyear['sum_class'] = fullyear[['學士班', 'MBA', 'IMBA', '一般碩士班', '博士班', 'EMBA', 'DBA']].sum(axis=1) # 有開課才有專兼別

facultytype = fullyear.loc[fullyear['sum_class']>0, ['teacher_id','year','semester','teacher_type']]
facultytype
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>year</th>
      <th>semester</th>
      <th>teacher_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>101476</td>
      <td>112</td>
      <td>1</td>
      <td>專任</td>
    </tr>
    <tr>
      <th>2</th>
      <td>308001</td>
      <td>112</td>
      <td>1</td>
      <td>專任</td>
    </tr>
    <tr>
      <th>6</th>
      <td>101388</td>
      <td>112</td>
      <td>1</td>
      <td>專任</td>
    </tr>
    <tr>
      <th>7</th>
      <td>111389</td>
      <td>112</td>
      <td>1</td>
      <td>兼任</td>
    </tr>
    <tr>
      <th>8</th>
      <td>124500</td>
      <td>112</td>
      <td>1</td>
      <td>名譽</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>250</th>
      <td>107991</td>
      <td>112</td>
      <td>2</td>
      <td>專任</td>
    </tr>
    <tr>
      <th>251</th>
      <td>128808</td>
      <td>112</td>
      <td>2</td>
      <td>專任</td>
    </tr>
    <tr>
      <th>252</th>
      <td>102104</td>
      <td>112</td>
      <td>2</td>
      <td>專任</td>
    </tr>
    <tr>
      <th>253</th>
      <td>122580</td>
      <td>112</td>
      <td>2</td>
      <td>兼任</td>
    </tr>
    <tr>
      <th>254</th>
      <td>117118</td>
      <td>112</td>
      <td>2</td>
      <td>專任</td>
    </tr>
  </tbody>
</table>
<p>425 rows × 4 columns</p>
</div>




```python
# 除了專任教師外，其餘專兼別皆改為兼任
print(facultytype['teacher_type'].drop_duplicates().tolist()) # 查看原本除了專任兼任外，還有哪些類別
facultytype['teacher_type'] = facultytype['teacher_type'].apply(lambda x: x if x=='專任' else '兼任')
facultytype
```

    ['專任', '兼任', '名譽', '函聘博', '講座', '合聘', '輔系', '函聘', '博士生兼任講師']





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>year</th>
      <th>semester</th>
      <th>teacher_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>101476</td>
      <td>112</td>
      <td>1</td>
      <td>專任</td>
    </tr>
    <tr>
      <th>2</th>
      <td>308001</td>
      <td>112</td>
      <td>1</td>
      <td>專任</td>
    </tr>
    <tr>
      <th>6</th>
      <td>101388</td>
      <td>112</td>
      <td>1</td>
      <td>專任</td>
    </tr>
    <tr>
      <th>7</th>
      <td>111389</td>
      <td>112</td>
      <td>1</td>
      <td>兼任</td>
    </tr>
    <tr>
      <th>8</th>
      <td>124500</td>
      <td>112</td>
      <td>1</td>
      <td>兼任</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>250</th>
      <td>107991</td>
      <td>112</td>
      <td>2</td>
      <td>專任</td>
    </tr>
    <tr>
      <th>251</th>
      <td>128808</td>
      <td>112</td>
      <td>2</td>
      <td>專任</td>
    </tr>
    <tr>
      <th>252</th>
      <td>102104</td>
      <td>112</td>
      <td>2</td>
      <td>專任</td>
    </tr>
    <tr>
      <th>253</th>
      <td>122580</td>
      <td>112</td>
      <td>2</td>
      <td>兼任</td>
    </tr>
    <tr>
      <th>254</th>
      <td>117118</td>
      <td>112</td>
      <td>2</td>
      <td>專任</td>
    </tr>
  </tbody>
</table>
<p>425 rows × 4 columns</p>
</div>




```python
# 確認是否unique(是否有重複的row)
facultytype[['teacher_id','year','semester']].duplicated().sum()
```




    0




```python
# 匯出
facultytype.to_csv('dataset/FacultyType.csv', index=False)
```

## <a id='toc3_3_'></a>[Class 開課時數](#toc0_)


```python
# 根據不同學制轉換成長表格
classdf = fullyear.melt(id_vars=['teacher_id','year','semester'], value_vars=['學士班', '一般碩士班', '博士班', 'MBA', 'IMBA', 'EMBA', 'DBA'], var_name='degree', value_name='num_class')
classdf = classdf[classdf['num_class']>0] # 只儲存有開課的資料
classdf
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>year</th>
      <th>semester</th>
      <th>degree</th>
      <th>num_class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>101476</td>
      <td>112</td>
      <td>1</td>
      <td>學士班</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>308001</td>
      <td>112</td>
      <td>1</td>
      <td>學士班</td>
      <td>6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>101388</td>
      <td>112</td>
      <td>1</td>
      <td>學士班</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>111389</td>
      <td>112</td>
      <td>1</td>
      <td>學士班</td>
      <td>3</td>
    </tr>
    <tr>
      <th>11</th>
      <td>131349</td>
      <td>112</td>
      <td>1</td>
      <td>學士班</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3294</th>
      <td>107924</td>
      <td>112</td>
      <td>1</td>
      <td>DBA</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3318</th>
      <td>102700</td>
      <td>112</td>
      <td>1</td>
      <td>DBA</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3379</th>
      <td>111578</td>
      <td>112</td>
      <td>1</td>
      <td>DBA</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3443</th>
      <td>118330</td>
      <td>112</td>
      <td>1</td>
      <td>DBA</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3472</th>
      <td>117118</td>
      <td>112</td>
      <td>1</td>
      <td>DBA</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
<p>792 rows × 5 columns</p>
</div>




```python
# 確認是否unique(是否有重複的row)
classdf[['teacher_id','year','semester','degree']].duplicated().sum()
```




    0




```python
# 匯出
classdf.to_csv('dataset/Class.csv', index=False)
```

# <a id='toc4_'></a>[List 學術、實務與教學貢獻清單](#toc0_)


```python
# 合併2021教師履歷資料與新資料
listdf = pd.DataFrame()
```


```python
# 2021教師履歷資料
dep = pd.read_csv('dataset/Department.csv')
temp = pd.read_csv('raw_data/List_temp.csv')
temp = temp.merge(dep[['department_id','department_Ename']], how='left', on='department_Ename').sort_values(by='department_id', ascending=True) # 加入 department_id
temp['item_name'] = temp['item_name'].apply(lambda x: x.rstrip())
print(temp.shape)
temp.drop_duplicates(subset=['Cname','item_name','item_year','scholarship_type','equis'], keep='first', inplace=True, ignore_index=True) # 剔除重複資料
temp = temp.merge(teacher[['teacher_id','Cname']], how='left', on='Cname') # 加入老師id
temp.drop_duplicates(subset=['Cname','item_name','item_year','scholarship_type','equis'], keep='last', inplace=True, ignore_index=True) # 讓有兩個id的老師只留下最後的一個id
temp.drop(columns=['Cname','department_id','department_Ename'], inplace=True)
print(temp.shape)
temp.head(3)
```

    (2729, 12)
    (2707, 10)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>item_name</th>
      <th>item_year</th>
      <th>item_type</th>
      <th>journal</th>
      <th>journal_type</th>
      <th>co_worker_in</th>
      <th>co_worker_out</th>
      <th>scholarship_type</th>
      <th>equis</th>
      <th>teacher_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>柯冠成;蘇湘茹;林信助;朱香蕙*, 2016.06, '技術分析對台灣波動度及規模效果之影響...</td>
      <td>2016.0</td>
      <td>NaN</td>
      <td>Journal of Management and Business Research (管...</td>
      <td>O</td>
      <td>NaN</td>
      <td>柯冠成;蘇湘茹;朱香蕙</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E1:Academic Research Articles</td>
      <td>102349.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Yen;Yu-Min Yen*, 2017.09, 'Risk Evaluations wi...</td>
      <td>2017.0</td>
      <td>NaN</td>
      <td>Journal of Banking and Finance</td>
      <td>O</td>
      <td>NaN</td>
      <td>Ray Yeutien Chou;Tso-Jung</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E1:Academic Research Articles</td>
      <td>118586.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>公司理財整合型研究-子計畫三: 股東權益成本之探討:以指數成分股變動為例(2/3)</td>
      <td>2020.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E3:Studies and Reports commissioned by compani...</td>
      <td>101607.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 2021教師履歷資料: 補部分 journal_type
temp['journal_type'].fillna('X')
temp.dropna(subset=['teacher_id','item_name','item_year'], inplace=True, ignore_index=True) # 這幾個欄位有na者移除

# 確認是否unique(是否有重複的row)
print(temp.duplicated(subset=['teacher_id','item_name','item_year','equis']).sum())
# temp.drop_duplicates(subset=['teacher_id','item_name','item_year','equis'], keep='last', inplace=True, ignore_index=True)
print(temp.shape)
```

    0
    (2575, 10)



```python
listdf = pd.concat([listdf, temp[['teacher_id','item_name', 'item_year', 'journal', 'journal_type','co_worker_in', 'co_worker_out', 'scholarship_type', 'equis']]], ignore_index=True)
listdf['teacher_id'] = listdf['teacher_id'].astype(int)
listdf['item_year'] = listdf['item_year'].astype(int)
print(listdf.shape)
listdf.head(3)
```

    (2575, 9)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>item_name</th>
      <th>item_year</th>
      <th>journal</th>
      <th>journal_type</th>
      <th>co_worker_in</th>
      <th>co_worker_out</th>
      <th>scholarship_type</th>
      <th>equis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>102349</td>
      <td>柯冠成;蘇湘茹;林信助;朱香蕙*, 2016.06, '技術分析對台灣波動度及規模效果之影響...</td>
      <td>2016</td>
      <td>Journal of Management and Business Research (管...</td>
      <td>O</td>
      <td>NaN</td>
      <td>柯冠成;蘇湘茹;朱香蕙</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E1:Academic Research Articles</td>
    </tr>
    <tr>
      <th>1</th>
      <td>118586</td>
      <td>Yen;Yu-Min Yen*, 2017.09, 'Risk Evaluations wi...</td>
      <td>2017</td>
      <td>Journal of Banking and Finance</td>
      <td>O</td>
      <td>NaN</td>
      <td>Ray Yeutien Chou;Tso-Jung</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E1:Academic Research Articles</td>
    </tr>
    <tr>
      <th>2</th>
      <td>101607</td>
      <td>公司理財整合型研究-子計畫三: 股東權益成本之探討:以指數成分股變動為例(2/3)</td>
      <td>2020</td>
      <td>NaN</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E3:Studies and Reports commissioned by compani...</td>
    </tr>
  </tbody>
</table>
</div>



## <a id='toc4_1_'></a>[論著資料](#toc0_)


```python
# 新資料：論著資料
temp = pd.read_excel('raw_data/電算中心原始資料.xlsx', sheet_name='論著資料(2019~2023)')
temp.rename(columns={'教師編號':'teacher_id','論著名稱':'item_name','論著日期':'item_year','論著類別':'item_type','期刊名':'journal'}, inplace=True)
temp.drop(columns=['系所代碼','系所名稱','教師姓名','論著名稱二','審查制度','專書性質','著作人數'], inplace=True)
temp['teacher_id'] = temp['teacher_id'].astype(int)
temp['item_name'] = temp['item_name'].apply(lambda x: x.rstrip())
print(temp.shape)
temp.head(3)
```

    (1270, 19)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>論著編號</th>
      <th>item_name</th>
      <th>item_year</th>
      <th>item_type</th>
      <th>journal</th>
      <th>期刊資料庫所屬</th>
      <th>合著者1</th>
      <th>合著者2</th>
      <th>合著者3</th>
      <th>合著者4</th>
      <th>合著者5</th>
      <th>合著者6</th>
      <th>合著者7</th>
      <th>合著者8</th>
      <th>合著者9</th>
      <th>合著者10</th>
      <th>合著者11</th>
      <th>合著者12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>102703</td>
      <td>412899</td>
      <td>Do local leads deliver contracting benefits? E...</td>
      <td>2019</td>
      <td>期刊論文</td>
      <td>Asia-Pacific Journal of Accounting &amp; Economics</td>
      <td>SSCI</td>
      <td>Chow, Y. E.</td>
      <td>Yoa, W. R.</td>
      <td>Chen Lung Chin.</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>111520</td>
      <td>416269</td>
      <td>Team goal orientation composition, team effica...</td>
      <td>201911</td>
      <td>期刊論文</td>
      <td>Journal of Management &amp; Organization</td>
      <td>SSCI</td>
      <td>Huang, C. Y.</td>
      <td>Huang, J. C.</td>
      <td>Chang, Y. E.</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>119794</td>
      <td>416411</td>
      <td>由比較法觀點論會計師之責任限制</td>
      <td>201906</td>
      <td>期刊論文</td>
      <td>證券市場發展季刊</td>
      <td>TSSCI</td>
      <td>陳俊元</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 新資料：論著資料-前處理

# item_year 只取年份
temp['item_year'] = temp['item_year'].apply(lambda x: int(str(x)[:4]))

# item_type 取代空格，不看學術交流，其他變成None
temp['item_type'] = temp['item_type'].str.replace(' ','')
temp = temp[temp['item_type']!='學術交流']
temp['item_type'] = temp['item_type'].apply(lambda x: None if x=='其他' else x)

# journal_type 先判斷三種
temp['journal_type'] = temp['期刊資料庫所屬'].apply(lambda x: 'O' if any(item in str(x).split() for item in ['SSCI','SCI','TSSCI']) else 'X')

# co_worker_in, co_worker_out 暫時先把所有合著者放在co_worker_out，之後由老師修改
temp['co_worker_in'] = None
temp['co_worker_out'] = temp.apply(lambda row: ';'.join([str(row[f'合著者{x}']) for x in range(1, 13) if pd.notna(row[f'合著者{x}'])]), axis=1)

# scholarship_type
temp['scholarship_type'] = np.where(temp['item_type']=='個案', 'Applied_or_Integration_Application_Scholarship', 'Basic_or_Discovery_Scholarship')

# equis
temp['equis'] = np.where(temp['item_type']=='個案', 'E6:Published Case Studies', 
                         np.where(temp['item_type']=='期刊論文', 'E1:Academic Research Articles',
                                  np.where(temp['item_type']=='會議論文','E4:Papers in Academic conferences',
                                           np.where(temp['item_type']=='專書','E7:Books (e.g. research monographs)',
                                                    np.where(temp['item_type']=='專書篇章','E8:Chapters in books',
                                                             np.where(temp['item_type']=='研究報告',"E12:Studies and Reports produced as part of an int'l network", None))))))

# 論著編號 刪除重複的值，不同年份視為不重複
temp.drop_duplicates(subset=['論著編號','item_year'], keep='last', inplace=True, ignore_index=True)

print(temp.shape)
temp.head(3)
```

    (1220, 24)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>論著編號</th>
      <th>item_name</th>
      <th>item_year</th>
      <th>item_type</th>
      <th>journal</th>
      <th>期刊資料庫所屬</th>
      <th>合著者1</th>
      <th>合著者2</th>
      <th>合著者3</th>
      <th>...</th>
      <th>合著者8</th>
      <th>合著者9</th>
      <th>合著者10</th>
      <th>合著者11</th>
      <th>合著者12</th>
      <th>journal_type</th>
      <th>co_worker_in</th>
      <th>co_worker_out</th>
      <th>scholarship_type</th>
      <th>equis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>102703</td>
      <td>412899</td>
      <td>Do local leads deliver contracting benefits? E...</td>
      <td>2019</td>
      <td>期刊論文</td>
      <td>Asia-Pacific Journal of Accounting &amp; Economics</td>
      <td>SSCI</td>
      <td>Chow, Y. E.</td>
      <td>Yoa, W. R.</td>
      <td>Chen Lung Chin.</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>O</td>
      <td>None</td>
      <td>Chow, Y. E.;Yoa, W. R.;Chen Lung Chin.</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E1:Academic Research Articles</td>
    </tr>
    <tr>
      <th>1</th>
      <td>111520</td>
      <td>416269</td>
      <td>Team goal orientation composition, team effica...</td>
      <td>2019</td>
      <td>期刊論文</td>
      <td>Journal of Management &amp; Organization</td>
      <td>SSCI</td>
      <td>Huang, C. Y.</td>
      <td>Huang, J. C.</td>
      <td>Chang, Y. E.</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>O</td>
      <td>None</td>
      <td>Huang, C. Y.;Huang, J. C.;Chang, Y. E.</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E1:Academic Research Articles</td>
    </tr>
    <tr>
      <th>2</th>
      <td>119794</td>
      <td>416411</td>
      <td>由比較法觀點論會計師之責任限制</td>
      <td>2019</td>
      <td>期刊論文</td>
      <td>證券市場發展季刊</td>
      <td>TSSCI</td>
      <td>陳俊元</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>O</td>
      <td>None</td>
      <td>陳俊元</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E1:Academic Research Articles</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 24 columns</p>
</div>




```python
# 新資料：論著資料-已有的item_name不再加入
mask = ~temp.set_index(['teacher_id','item_name','item_year']).index.isin(listdf.set_index(['teacher_id','item_name','item_year']).index)
temp = temp[mask].reset_index(drop=True)
print(temp.shape)
```

    (928, 24)



```python
# 確認是否unique(是否有重複的row)
# temp[temp.duplicated(subset=['teacher_id','item_name','item_year','equis'], keep=False)]
print(temp.duplicated(subset=['teacher_id','item_name','item_year','equis']).sum())
temp.drop_duplicates(subset=['teacher_id','item_name','item_year','equis'], keep='last', inplace=True, ignore_index=True)
print(temp.shape)
```

    18
    (910, 24)



```python
listdf = pd.concat([listdf, temp[['teacher_id','item_name', 'item_year', 'journal', 'journal_type','co_worker_in', 'co_worker_out', 'scholarship_type', 'equis']]], ignore_index=True)
print(listdf.shape)
listdf.head(3)
```

    (3485, 9)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>item_name</th>
      <th>item_year</th>
      <th>journal</th>
      <th>journal_type</th>
      <th>co_worker_in</th>
      <th>co_worker_out</th>
      <th>scholarship_type</th>
      <th>equis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>102349</td>
      <td>柯冠成;蘇湘茹;林信助;朱香蕙*, 2016.06, '技術分析對台灣波動度及規模效果之影響...</td>
      <td>2016</td>
      <td>Journal of Management and Business Research (管...</td>
      <td>O</td>
      <td>NaN</td>
      <td>柯冠成;蘇湘茹;朱香蕙</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E1:Academic Research Articles</td>
    </tr>
    <tr>
      <th>1</th>
      <td>118586</td>
      <td>Yen;Yu-Min Yen*, 2017.09, 'Risk Evaluations wi...</td>
      <td>2017</td>
      <td>Journal of Banking and Finance</td>
      <td>O</td>
      <td>NaN</td>
      <td>Ray Yeutien Chou;Tso-Jung</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E1:Academic Research Articles</td>
    </tr>
    <tr>
      <th>2</th>
      <td>101607</td>
      <td>公司理財整合型研究-子計畫三: 股東權益成本之探討:以指數成分股變動為例(2/3)</td>
      <td>2020</td>
      <td>NaN</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E3:Studies and Reports commissioned by compani...</td>
    </tr>
  </tbody>
</table>
</div>



## <a id='toc4_2_'></a>[研究計畫](#toc0_)


```python
# 新資料：研究計畫
temp = pd.read_excel('raw_data/電算中心原始資料.xlsx', sheet_name='研究計畫(20190101~)')
temp.rename(columns={'教師代號':'teacher_id','計畫名稱':'item_name','起始年度':'item_year'}, inplace=True)
temp['teacher_id'] = temp['teacher_id'].astype(int)
temp['item_name'] = temp['item_name'].apply(lambda x: x.rstrip())
temp['journal'] = None
temp['journal_type'] = 'X'
temp['co_worker_out'] = None
temp.drop(columns=['系所代碼','系所名稱','計畫職稱','核定年度','主持人代碼','主持人','委託單位'], inplace=True) # '起迄日期'
print(temp.shape)
temp.head(3)
```

    (925, 10)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>教師姓名</th>
      <th>item_year</th>
      <th>校內編號</th>
      <th>item_name</th>
      <th>計畫類別</th>
      <th>起迄日期</th>
      <th>journal</th>
      <th>journal_type</th>
      <th>co_worker_out</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>115045</td>
      <td>湛可南</td>
      <td>109</td>
      <td>107B109001</td>
      <td>資訊交易，共同基金，與公司財務(3/3)</td>
      <td>科技部</td>
      <td>2020/08/01-2021/07/31</td>
      <td>None</td>
      <td>X</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>113615</td>
      <td>周冠男</td>
      <td>109</td>
      <td>107B109002</td>
      <td>定錨偏誤，報酬可預測性及公司決策(3/3)</td>
      <td>科技部</td>
      <td>2020/08/01-2021/07/31</td>
      <td>None</td>
      <td>X</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>102106</td>
      <td>戚務君</td>
      <td>109</td>
      <td>107B109003</td>
      <td>審計對盈餘可比性的影響：法律責任、會計師特性與關鍵查核事項(3/3)</td>
      <td>科技部</td>
      <td>2020/08/01-2021/07/31</td>
      <td>None</td>
      <td>X</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 新資料：研究計畫-前處理

# item_year 西元年
temp['item_year'] = temp['item_year'].apply(lambda x: int(x+1911))

# co_worker_in 同個計畫的內教師都先放在校內合著者
temp['co_worker_in'] = temp.groupby(['校內編號', 'item_name'])['教師姓名'].transform(lambda x: ';'.join(x))
temp['co_worker_in'] = temp.apply(lambda row: ';'.join([name for name in row['co_worker_in'].split(';') if name != row['教師姓名']]), axis=1) # 移除自己的姓名

# scholarship_type 科技部為basic，非科技部為applied
temp['scholarship_type'] = np.where(temp['計畫類別']=='科技部','Basic_or_Discovery_Scholarship','Applied_or_Integration_Application_Scholarship')

# equis 科技部為E15，非科技部為E3
temp['equis'] = np.where(temp['計畫類別']=='科技部','E15:Other(Please describe)其他(科技部學術型計畫 MOST Research Project)',"E3:Studies and Reports commissioned by companies and gov't agencies(企業、政府、科技部產學合作計畫)")

# item_name 處理相同 'teacher_id', 'item_year', 'item_name' 的 item_name -1, -2, -3...
def update_item_names(group):
    group = group.sort_values(by='起迄日期').reset_index(drop=True)
    if len(group)>1:
        group['item_name'] = [group['item_name'][0]+'-'+str(i + 1) for i in range(len(group))]
    return group
temp = temp.groupby(['teacher_id', 'item_year', 'item_name'], group_keys=False).apply(update_item_names)

print(temp.shape)
temp.head(3)
```

    (925, 13)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>教師姓名</th>
      <th>item_year</th>
      <th>校內編號</th>
      <th>item_name</th>
      <th>計畫類別</th>
      <th>起迄日期</th>
      <th>journal</th>
      <th>journal_type</th>
      <th>co_worker_out</th>
      <th>co_worker_in</th>
      <th>scholarship_type</th>
      <th>equis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101388</td>
      <td>王儷玲</td>
      <td>2019</td>
      <td>108F108069</td>
      <td>期貨公會活動補助案</td>
      <td>非科技部</td>
      <td>2019/10/01-2019/12/31</td>
      <td>None</td>
      <td>X</td>
      <td>None</td>
      <td></td>
      <td>Applied_or_Integration_Application_Scholarship</td>
      <td>E3:Studies and Reports commissioned by compani...</td>
    </tr>
    <tr>
      <th>0</th>
      <td>101388</td>
      <td>王儷玲</td>
      <td>2019</td>
      <td>108A108131</td>
      <td>開放銀行在電信業之研究與應用</td>
      <td>非科技部</td>
      <td>2019/12/15-2020/12/31</td>
      <td>None</td>
      <td>X</td>
      <td>None</td>
      <td>陳恭;謝明華;彭金隆;宋皇志</td>
      <td>Applied_or_Integration_Application_Scholarship</td>
      <td>E3:Studies and Reports commissioned by compani...</td>
    </tr>
    <tr>
      <th>0</th>
      <td>101388</td>
      <td>王儷玲</td>
      <td>2020</td>
      <td>109A109129</td>
      <td>2020金融服務產業未來展望：數位科技創新</td>
      <td>非科技部</td>
      <td>2020/09/15-2021/03/31</td>
      <td>None</td>
      <td>X</td>
      <td>None</td>
      <td>謝明華;彭金隆</td>
      <td>Applied_or_Integration_Application_Scholarship</td>
      <td>E3:Studies and Reports commissioned by compani...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 新資料：研究計畫-已有的item_name不再加入
mask = ~temp.set_index(['teacher_id','item_name','item_year']).index.isin(listdf.set_index(['teacher_id','item_name','item_year']).index)
temp = temp[mask].reset_index(drop=True)
print(temp.shape)
```

    (787, 13)



```python
# 確認是否unique(是否有重複的row)
# temp[temp.duplicated(subset=['teacher_id','item_name','item_year','equis'], keep=False)]
print(temp.duplicated(subset=['teacher_id','item_name','item_year','equis']).sum())
# temp.drop_duplicates(subset=['teacher_id','item_name','item_year','equis'], keep='last', inplace=True, ignore_index=True)
# print(temp.shape)
```

    0



```python
listdf = pd.concat([listdf, temp[['teacher_id','item_name', 'item_year', 'journal', 'journal_type','co_worker_in', 'co_worker_out', 'scholarship_type', 'equis']]], ignore_index=True)
print(listdf.shape)
listdf.head(3)
```

    (4272, 9)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>item_name</th>
      <th>item_year</th>
      <th>journal</th>
      <th>journal_type</th>
      <th>co_worker_in</th>
      <th>co_worker_out</th>
      <th>scholarship_type</th>
      <th>equis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>102349</td>
      <td>柯冠成;蘇湘茹;林信助;朱香蕙*, 2016.06, '技術分析對台灣波動度及規模效果之影響...</td>
      <td>2016</td>
      <td>Journal of Management and Business Research (管...</td>
      <td>O</td>
      <td>NaN</td>
      <td>柯冠成;蘇湘茹;朱香蕙</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E1:Academic Research Articles</td>
    </tr>
    <tr>
      <th>1</th>
      <td>118586</td>
      <td>Yen;Yu-Min Yen*, 2017.09, 'Risk Evaluations wi...</td>
      <td>2017</td>
      <td>Journal of Banking and Finance</td>
      <td>O</td>
      <td>NaN</td>
      <td>Ray Yeutien Chou;Tso-Jung</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E1:Academic Research Articles</td>
    </tr>
    <tr>
      <th>2</th>
      <td>101607</td>
      <td>公司理財整合型研究-子計畫三: 股東權益成本之探討:以指數成分股變動為例(2/3)</td>
      <td>2020</td>
      <td>NaN</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E3:Studies and Reports commissioned by compani...</td>
    </tr>
  </tbody>
</table>
</div>



## <a id='toc4_3_'></a>[獎項](#toc0_)


```python
# 新資料：獎項
temp = pd.read_excel('raw_data/電算中心原始資料.xlsx', sheet_name='獎項(108學年~)')
temp.rename(columns={'教師代號':'teacher_id','年度':'item_year'}, inplace=True)
temp['teacher_id'] = temp['teacher_id'].astype(int)
temp['journal'] = None
temp['journal_type'] = 'X'
temp['co_worker_in'] = None
temp['co_worker_out'] = None
temp.drop(columns=['單位代碼','單位名稱','序號','教師姓名','頒獎單位'], inplace=True) # '起迄日期'
print(temp.shape)
temp.head(3)
```

    (285, 8)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>item_year</th>
      <th>獎項</th>
      <th>備註</th>
      <th>journal</th>
      <th>journal_type</th>
      <th>co_worker_in</th>
      <th>co_worker_out</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>102104</td>
      <td>108</td>
      <td>科技部研究獎勵                                       ...</td>
      <td>NaN</td>
      <td>None</td>
      <td>X</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>102104</td>
      <td>108</td>
      <td>科技部研究獎勵                                       ...</td>
      <td>NaN</td>
      <td>None</td>
      <td>X</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>111580</td>
      <td>108</td>
      <td>科技部研究獎勵                                       ...</td>
      <td>NaN</td>
      <td>None</td>
      <td>X</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 新資料：獎項-前處理  scholarship_type	equis

# item_year 西元年
temp['item_year'] = temp['item_year'].apply(lambda x: int(x+1911))

# item_name 加入備註
temp['備註'].fillna(0, inplace=True)
temp['item_name'] = temp.apply(lambda row: str(int(row['備註']))+row['獎項'] if row['備註']!=0 else row['獎項'], axis=1)
temp['item_name'] = temp['item_name'].apply(lambda x: x.rstrip())

# scholarship_type basic or applied，先算在basic，之後給老師調整
temp['scholarship_type'] = 'Basic_or_Discovery_Scholarship'

# equis E15
temp['equis'] = 'E15:Other(Competitive Research Awards Received)獲重要研究獎項次數'

# 移除重複值
temp.drop_duplicates(subset=['teacher_id','item_year','item_name'], inplace=True, ignore_index=True)

print(temp.shape)
temp.head(3)
```

    (235, 11)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>item_year</th>
      <th>獎項</th>
      <th>備註</th>
      <th>journal</th>
      <th>journal_type</th>
      <th>co_worker_in</th>
      <th>co_worker_out</th>
      <th>item_name</th>
      <th>scholarship_type</th>
      <th>equis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>102104</td>
      <td>2019</td>
      <td>科技部研究獎勵                                       ...</td>
      <td>0.0</td>
      <td>None</td>
      <td>X</td>
      <td>None</td>
      <td>None</td>
      <td>科技部研究獎勵</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E15:Other(Competitive Research Awards Received...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>111580</td>
      <td>2019</td>
      <td>科技部研究獎勵                                       ...</td>
      <td>0.0</td>
      <td>None</td>
      <td>X</td>
      <td>None</td>
      <td>None</td>
      <td>科技部研究獎勵</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E15:Other(Competitive Research Awards Received...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>111580</td>
      <td>2019</td>
      <td>學術研究優良獎                                       ...</td>
      <td>0.0</td>
      <td>None</td>
      <td>X</td>
      <td>None</td>
      <td>None</td>
      <td>學術研究優良獎</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E15:Other(Competitive Research Awards Received...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 新資料：獎項-已有的item_name不再加入
mask = ~temp.set_index(['teacher_id','item_name','item_year']).index.isin(listdf.set_index(['teacher_id','item_name','item_year']).index)
temp = temp[mask].reset_index(drop=True)
print(temp.shape)
```

    (221, 11)



```python
# 確認是否unique(是否有重複的row)
# temp[temp.duplicated(subset=['teacher_id','item_name','item_year','equis'], keep=False)]
print(temp.duplicated(subset=['teacher_id','item_name','item_year','equis']).sum())
# temp.drop_duplicates(subset=['teacher_id','item_name','item_year','equis'], keep='last', inplace=True, ignore_index=True)
# print(temp.shape)
```

    0



```python
listdf = pd.concat([listdf, temp[['teacher_id','item_name', 'item_year', 'journal', 'journal_type','co_worker_in', 'co_worker_out', 'scholarship_type', 'equis']]], ignore_index=True)
print(listdf.shape)
listdf.head(3)
```

    (4493, 9)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>item_name</th>
      <th>item_year</th>
      <th>journal</th>
      <th>journal_type</th>
      <th>co_worker_in</th>
      <th>co_worker_out</th>
      <th>scholarship_type</th>
      <th>equis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>102349</td>
      <td>柯冠成;蘇湘茹;林信助;朱香蕙*, 2016.06, '技術分析對台灣波動度及規模效果之影響...</td>
      <td>2016</td>
      <td>Journal of Management and Business Research (管...</td>
      <td>O</td>
      <td>NaN</td>
      <td>柯冠成;蘇湘茹;朱香蕙</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E1:Academic Research Articles</td>
    </tr>
    <tr>
      <th>1</th>
      <td>118586</td>
      <td>Yen;Yu-Min Yen*, 2017.09, 'Risk Evaluations wi...</td>
      <td>2017</td>
      <td>Journal of Banking and Finance</td>
      <td>O</td>
      <td>NaN</td>
      <td>Ray Yeutien Chou;Tso-Jung</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E1:Academic Research Articles</td>
    </tr>
    <tr>
      <th>2</th>
      <td>101607</td>
      <td>公司理財整合型研究-子計畫三: 股東權益成本之探討:以指數成分股變動為例(2/3)</td>
      <td>2020</td>
      <td>NaN</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Basic_or_Discovery_Scholarship</td>
      <td>E3:Studies and Reports commissioned by compani...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 確認是否unique(是否有重複的row)
print(listdf.duplicated(subset=['teacher_id','item_name','item_year','equis']).sum())
```

    0



```python
# 匯出
listdf.dropna(subset=['teacher_id','item_name','item_year','scholarship_type','equis'], inplace=True, ignore_index=True)
print(listdf.shape)
listdf.to_csv('dataset/List1.csv', index=False)
```

    (4471, 9)


# <a id='toc5_'></a>[Resume 教師履歷](#toc0_)
匯入歷年資料用，未來不用執行


```python
dep = pd.read_csv('dataset/Department.csv')

temp = pd.read_csv('raw_data/Resume_temp.csv')
temp = temp.merge(dep[['department_id','department_Ename']], how='left', on='department_Ename') # 加入 department_id，稍後用來對照teacher有否該組(teacher_id,dep_id)資料
temp = temp[temp['teacher_id'].isin(teacher['teacher_id'].tolist())]
temp.sort_values(by=['teacher_id','department_id'], ascending=True, inplace=True, ignore_index=True)
print(temp.shape)
temp.head(3)
```

    (374, 29)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>resume_year</th>
      <th>department_Ename</th>
      <th>highest_edu_degree</th>
      <th>highest_edu_department</th>
      <th>highest_edu_school</th>
      <th>highest_edu_graduation_year</th>
      <th>experience</th>
      <th>teaching_interests</th>
      <th>research_interests</th>
      <th>...</th>
      <th>PA1-6</th>
      <th>PA1-7&amp;IP1-3</th>
      <th>PA1-8&amp;SP1-3</th>
      <th>SP1-1</th>
      <th>SP1-2</th>
      <th>IP1a</th>
      <th>IP1-2</th>
      <th>IP1-4</th>
      <th>IP1-5</th>
      <th>department_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101388</td>
      <td>2021</td>
      <td>RMI</td>
      <td>PhD</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1998</td>
      <td>1. Chairperson,Pension Fund Association, 2011-...</td>
      <td>Risk Management and Insurance, Pension Plan an...</td>
      <td>Pension Plan, Insurance Finance and Accounting</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>308</td>
    </tr>
    <tr>
      <th>1</th>
      <td>101388</td>
      <td>2021</td>
      <td>EMBA</td>
      <td>PhD</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1998</td>
      <td>1. Chairperson,Pension Fund Association, 2011-...</td>
      <td>Risk Management and Insurance, Pension Plan an...</td>
      <td>Pension Plan, Insurance Finance and Accounting</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>932</td>
    </tr>
    <tr>
      <th>2</th>
      <td>101476</td>
      <td>2021</td>
      <td>Accounting</td>
      <td>PhD</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1998</td>
      <td>1. Associate Professor, Department of Accounti...</td>
      <td>Cost and Managerial Accounting,  Advanced Mana...</td>
      <td>Cost and Managerial Accounting, Financial Acco...</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>303</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 29 columns</p>
</div>




```python
# 原始教師履歷資料存在重複值，即一位教師會有不同系所（有至他系上課會納入計算），這邊選擇先刪除，只留主系所的資料
resume = pd.DataFrame()
# for id in temp['teacher_id'].drop_duplicates():
#     dep_num = teacher.loc[teacher['teacher_id']==id, 'dep_id'].values[0]
#     resume = pd.concat([resume, temp.loc[(temp['teacher_id']==id)&(temp['department_id']==dep_num),]], axis=0)
resume = temp.drop_duplicates(subset='teacher_id', keep='first', ignore_index=True).copy()
resume.drop(columns=['department_Ename','department_id'], inplace=True)
print(resume.shape)
resume.head(3)
```

    (252, 27)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>teacher_id</th>
      <th>resume_year</th>
      <th>highest_edu_degree</th>
      <th>highest_edu_department</th>
      <th>highest_edu_school</th>
      <th>highest_edu_graduation_year</th>
      <th>experience</th>
      <th>teaching_interests</th>
      <th>research_interests</th>
      <th>discipline</th>
      <th>...</th>
      <th>PA1-5</th>
      <th>PA1-6</th>
      <th>PA1-7&amp;IP1-3</th>
      <th>PA1-8&amp;SP1-3</th>
      <th>SP1-1</th>
      <th>SP1-2</th>
      <th>IP1a</th>
      <th>IP1-2</th>
      <th>IP1-4</th>
      <th>IP1-5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101388</td>
      <td>2021</td>
      <td>PhD</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1998</td>
      <td>1. Chairperson,Pension Fund Association, 2011-...</td>
      <td>Risk Management and Insurance, Pension Plan an...</td>
      <td>Pension Plan, Insurance Finance and Accounting</td>
      <td>NaN</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>101476</td>
      <td>2021</td>
      <td>PhD</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1998</td>
      <td>1. Associate Professor, Department of Accounti...</td>
      <td>Cost and Managerial Accounting,  Advanced Mana...</td>
      <td>Cost and Managerial Accounting, Financial Acco...</td>
      <td>NaN</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>101477</td>
      <td>2021</td>
      <td>PhD</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1991</td>
      <td>1.Dean of International Cooperation, National ...</td>
      <td>Human Resource Management, Social Innovation, ...</td>
      <td>Human Resource Management, Intellectual Capita...</td>
      <td>NaN</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 27 columns</p>
</div>




```python
# 確認是否unique(是否有重複的row)
resume[['teacher_id','resume_year']].duplicated().sum()
```




    0




```python
# 匯出
resume.to_csv('dataset/Resume.csv', index=False)
```
