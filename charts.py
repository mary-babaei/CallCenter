import matplotlib.pyplot as plt

class ChartAnalysis:
    def __init__(self, df):
        self.df = df

    def plot_call_volume_per_agent(self):
        call_counts = self.df['Agent_ID'].value_counts()

        plt.figure(figsize=(10, 6))
        call_counts.plot(kind='bar', color='lightcoral')
        plt.title('Call Volume per Agent')
        plt.xlabel('Agent ID')
        plt.ylabel('Number of Calls')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
