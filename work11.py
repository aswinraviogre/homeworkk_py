import json
from datetime import datetime

def get_record(city, comment, date):
    return {"city": city, "comment": comment, "date": date}

records = [
    get_record("Paris", "Loved the Eiffel Tower!", "15-05-2023"),
    get_record("Tokyo", "Enjoyed sushi and temples.", "10-09-2024"),
    get_record("New York", "Times Square was amazing!", "05-11-2025")
]

for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")

records_json = json.dumps(records, indent=4)
print(records_json)

parsed
