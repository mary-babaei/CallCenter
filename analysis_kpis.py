import pandas as pd


class KPIAnalyzer:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        # اطمینان از اینکه ستون Call_Time به فرمت datetime تبدیل بشه
        self.df['Call_Time'] = pd.to_datetime(self.df['Call_Time'], format='%H:%M:%S').dt.strftime('%H:%M')

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

    def answered_rate(self):
        answered_calls = self.df['answered'].sum()
        total_calls = len(self.df)
        return round((answered_calls / total_calls) * 100, 2)

    def average_wait_time(self):
        return round(self.df['Queue_Wait_Time'].mean(), 2)

    def call_volume_per_agent(self):
        return self.df['Agent_ID'].value_counts()

    def std_satisfaction(self):
        return self.df['Customer_Satisfaction'].std()

    def mean_satisfaction(self):
        return self.df['Customer_Satisfaction'].mean()

    def mean_satisfaction_by_date(self):
        return self.df.groupby('Call_Date')['Customer_Satisfaction'].mean().round(2)

    def mean_satisfaction_by_time(self):
        return self.df.groupby('Call_Time')['Customer_Satisfaction'].mean().round(2)

    def summary_report(self):
        print("🔍 گزارش KPI مرکز تماس")
        print(f"1. متوسط زمان مکالمه (AHT): {self.average_handle_time()} دقیقه")
        print(f"2. نرخ حل تماس در اولین تماس (FCR): {self.first_call_resolution_rate()}٪")
        print(f"3. امتیاز رضایت مشتری (CSAT): {self.customer_satisfaction_score()} از 5")
        print(f"4. نرخ قطع تماس (Abandonment Rate): {self.abandonment_rate()}٪")
        print(f"5. نرخ برقراری تماس (Answered Rate): {self.answered_rate()}٪")
        print(f"6. میانگین زمان انتظار: {self.average_wait_time()} دقیقه")
        print(f"📏 انحراف معیار رضایت: {self.std_satisfaction():.2f}")
        print(f"📏 میانگین رضایت : {self.mean_satisfaction():.2f}")
        print("📏 میانگین رضایت بر اساس زمان:")
        print(self.mean_satisfaction_by_time())
        print("📏 میانگین رضایت بر اساس تاریخ:")
        print(self.mean_satisfaction_by_date())

        print("\n7. تعداد تماس‌ها برای هر اپراتور:")
        print(self.call_volume_per_agent())
