from generate_data import GenerateData
from analysis_kpis import KPIAnalyzer
from store_data import DataStorage
from charts import ChartAnalysis

if __name__ == "__main__":
    # ساخت دیتاست و ذخیره آن در فایل CSV
    generator = GenerateData()
    df = generator.generate_data()  # افزودن پرانتز برای فراخوانی متد
    df.to_csv("C:/Users/Maryam/PycharmProjects/pythonProject1/Call_Data_Analysis/call_center_data_new.csv", index=False)
    print("✅ دیتاست با موفقیت ساخته شد.")

    # تحلیل KPIها
    analyzer = KPIAnalyzer("C:/Users/Maryam/PycharmProjects/pythonProject1/Call_Data_Analysis/call_center_data_new.csv")

    # ذخیره در دیتابیس SQLite
    storage = DataStorage("C:/Users/Maryam/PycharmProjects/pythonProject1/Call_Data_Analysis/call_center_data_new.csv")
    storage.store_in_sqlite()

    # چارت
    visualizer = ChartAnalysis(df)
    visualizer.plot_call_volume_per_agent()
