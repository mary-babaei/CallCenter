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
        for day in range(self.num_day):
            for call_id in range(self.num_call_per_day):
                call_date = self.faker.date_this_month().strftime('%Y-%m-%d')
                call_time = self.faker.time()
                call_datetime = f"{call_date} {call_time}"
                agent_id = f"Agent_{randint(1, self.num_agent)}"
                customer_id = self.faker.uuid4()
                call_duration = randint(1, 15)
                call_resolved = choice([True, False])
                call_type = choice(["Inbound", "Outbound", "Follow-up"])
                customer_satisfaction = randint(1, 5) if call_resolved else np.nan
                abandoned = choice([True, False])
                queue_wait_time = randint(0, 10) if not abandoned else 0

                call_data.append([
                    call_id, agent_id, customer_id, call_datetime, call_duration,
                    call_resolved, call_type, customer_satisfaction, abandoned, queue_wait_time
                ])

        df = pd.DataFrame(call_data, columns=[
            "Call_ID", "Agent_ID", "Customer_ID", "Call_DateTime", "Call_Duration",
            "Call_Resolved", "Call_Type", "Customer_Satisfaction", "Abandoned", "Queue_Wait_Time"
        ])
        return df


