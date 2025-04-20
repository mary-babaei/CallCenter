from generate_data import GenerateData
from analysis_kpis import KPIAnalyzer
from store_data import DataStorage
from charts import ChartAnalysis

if __name__ == "__main__":
    # ساخت دیتاست و ذخیره آن در فایل CSV
    generator = GenerateData()
    df = generator.generate_data()
    df.to_csv("C:/Users/Maryam/PycharmProjects/pythonProject1/Call_Data_Analysis/call_center_data.csv", index=False)
    print("✅ دیتاست با موفقیت ساخته شد.")

    # تحلیل KPIها
    analyzer = KPIAnalyzer("call_center_data.csv")
    analyzer.summary_report()

    # ذخیره در دیتابیس SQLite
    storage = DataStorage("call_center_data.csv")
    storage.store_in_sqlite()

    # چارت
    visualizer = ChartAnalysis(df)
    visualizer.plot_call_volume_per_agent()