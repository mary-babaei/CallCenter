import pandas as pd
import sqlite3

class DataStorage:
    def __init__(self, csv_path, db_name="call_center.db"):
        self.csv_path = csv_path
        self.db_name = db_name

    def store_in_sqlite(self):
        # خواندن فایل CSV
        df = pd.read_csv(self.csv_path)

        # اتصال به دیتابیس SQLite
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # ذخیره دیتا در جدول
        df.to_sql("calls", conn, if_exists="replace", index=False)

        # چک کردن تعداد رکورد ذخیره‌شده
        cursor.execute("SELECT COUNT(*) FROM calls")
        total = cursor.fetchone()[0]
        print(f"✅ {total} رکورد با موفقیت در دیتابیس ذخیره شد.")

        # بستن اتصال
        conn.close()