# 後端架構
```
backend
|
|– .env (儲存環境變數)
|
|– __init__.py (初始化伺服器，引入 API 和資料庫)
|
|– main.py (伺服器啟動的位置)
|
|– api
|   |
|   |– departmentView.py (系所助教所需的資料 API)
|   |
|   |– teacherView.py (教師所需的資料 API)
|
|– models.py (定義資料庫的位置)

```

# 啟動專案

1. 在要放專案的位置中用下方指令將專案複製到本機
```
git clone https://github.com/ZeoXer/dbms-final-project.git
```

2. 進入 `backend` 資料夾，並下載 python 所需的相關套件
```
cd backend
pip install -r requirements.txt
```

3. 將 `.env.default` 複製一份並改名為 `.env`，並在裡面輸入資料庫的連結
```
DATABASE_URI=資料庫連結
```

4. 啟動 server
```
python main.py
```
