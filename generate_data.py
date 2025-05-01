from faker import Faker
import pandas as pd
import numpy as np
from random import randint, choice


class GenerateData:
    def __init__(self):
        self.faker = Faker()
        self.num_day = 30
        self.num_agent = 10
        self.num_call_per_day = 200

    def generate_data(self):
        call_data = []
        total_calls = 0
        answered_calls = 0
        abandoned_calls = 0
        resolved_calls = 0

        for day in range(self.num_day):
            for call_id in range(self.num_call_per_day):
                total_calls += 1

                call_date = self.faker.date_this_year().strftime('%Y-%m-%d')
                call_time = self.faker.time()
                call_datetime = f"{call_date} {call_time}"
                agent_id = f"Agent_{randint(1, self.num_agent)}"
                customer_id = self.faker.uuid4()
                call_duration = randint(1, 15)
                call_resolved = choice([True, False])
                call_type = choice(["Inbound", "Outbound", "Follow-up"])
                customer_satisfaction = randint(1, 5) if call_resolved else np.nan
                abandoned = choice([True, False])
                answered = not abandoned  # تماس‌های جواب‌داده شده نمی‌توانند قطع‌شده باشند
                queue_wait_time = randint(0, 10) if not abandoned else 0

                # ✅ محاسبه وضعیت تماس
                is_answered = answered
                is_abandoned = abandoned
                is_resolved = call_resolved and is_answered

                if is_answered:
                    answered_calls += 1
                if is_abandoned:
                    abandoned_calls += 1
                if is_resolved:
                    resolved_calls += 1

                call_data.append([
                    call_id, agent_id, customer_id, call_date, call_time, call_datetime, call_duration,
                    call_resolved, call_type, customer_satisfaction,
                    abandoned, answered, queue_wait_time,
                    is_answered, is_abandoned, is_resolved
                ])

        df = pd.DataFrame(call_data, columns=[
            "Call_ID", "Agent_ID", "Customer_ID", "Call_Date", "Call_Time", "Call_DateTime", "Call_Duration",
            "Call_Resolved", "Call_Type", "Customer_Satisfaction",
            "Abandoned", 'answered', "Queue_Wait_Time",
            "Is_Answered", "Is_Abandoned", "Is_Resolved"
        ])

        print(f'📞 Calls Date: {call_date}')
        print(f'📞 Calls Time: {call_time}')
        print(f"📞 Total Calls: {total_calls}")
        print(f"✅ Answered Calls: {answered_calls}")
        print(f"❌ Abandoned Calls: {abandoned_calls}")
        print(f"📍 Resolved Calls: {resolved_calls}")
        print(f"📊 Answer Rate: {answered_calls / total_calls:.2%}")
        print(f'📊 Abandoned Rate: {abandoned_calls / total_calls:.2%}')
        print(f'Call Type: {call_type}')

        return df
