from __init__ import app, db, register_blueprints

with app.app_context():
    try:
        db.create_all()
        print("資料庫連接成功")
    except Exception as e:
        print("資料庫連接失敗", e)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        register_blueprints(app)
    app.run(port=5432, debug=True)
