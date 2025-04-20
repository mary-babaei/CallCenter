import pandas as pd

class KPIAnalyzer:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def average_handle_time(self):
        return round(self.df['Call_Duration'].mean(), 2)

    def first_call_resolution_rate(self):
        resolved_calls = self.df['Call_Resolved'].sum()
        total_calls = len(self.df)
        return round((resolved_calls / total_calls) * 100, 2)

    def customer_satisfaction_score(self):
        return round(self.df['Customer_Satisfaction'].mean(), 2)

    def abandonment_rate(self):
        abandoned_calls = self.df['Abandoned'].sum()
        total_calls = len(self.df)
        return round((abandoned_calls / total_calls) * 100, 2)

    def average_wait_time(self):
        return round(self.df['Queue_Wait_Time'].mean(), 2)

    def call_volume_per_agent(self):
        return self.df['Agent_ID'].value_counts()

    def summary_report(self):
        print("🔍 گزارش KPI مرکز تماس")
        print(f"1. متوسط زمان مکالمه (AHT): {self.average_handle_time()} دقیقه")
        print(f"2. نرخ حل تماس در اولین تماس (FCR): {self.first_call_resolution_rate()}٪")
        print(f"3. امتیاز رضایت مشتری (CSAT): {self.customer_satisfaction_score()} از 5")
        print(f"4. نرخ قطع تماس (Abandonment Rate): {self.abandonment_rate()}٪")
        print(f"5. میانگین زمان انتظار: {self.average_wait_time()} دقیقه")
        print("\n6. تعداد تماس‌ها برای هر اپراتور:")
        print(self.call_volume_per_agent())