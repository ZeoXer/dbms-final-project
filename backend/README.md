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
|– api.py (API function 的位置，可以視情況另開資料夾拆檔整理)
|
|– models.py (定義資料庫的位置，可以視情況另開資料夾拆檔整理)

```

# 啟動專案

1. 在要放專案的位置中用下方指令將專案複製到本機
```
git clone https://github.com/ZeoXer/dbms-final-project.git
```

2. 進入 `backend` 資料夾，並下載 python 所需的相關套件
```
cd backend
pip install requirement.txt
```

3. 將 `.env.default` 複製一份並改名為 `.env`，並在裡面輸入資料庫的連結
```
DATABASE_URI=資料庫連結
```

4. 啟動 server
```
python main.py
```

5. 若有新的修改，完成後提交紀錄並上傳 (協作方式待決定)
```
git add <檔案>
git commit -m "紀錄訊息"
git push origin main
```

* 目前測試起來其他 contributors 還不能從本機端 push 更新上去，目前還沒找到問題來源，可能可以先確認本機設定的使用者資訊是否和 GitHub 上的帳號資訊相同
```
git config --global user.name
git config --global user.email
```
