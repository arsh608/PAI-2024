import re

def extract_dates(text):

    date_pattern = r'\b(\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{1,2}-\d{1,2}|[A-Za-z]{3} \d{1,2}, \d{4})\b'
    dates = re.findall(date_pattern, text)
    unique_dates = set(dates)
    return list(unique_dates)

text_block = """
The meeting is scheduled for 12/09/2023. 
Please note that the project deadline is 2023-09-12. 
We also have a team lunch on Sep 12, 2023.
Additionally, there is an event on 11/11/2023 and a follow-up on 2023-11-01.
"""

extracted_dates = extract_dates(text_block)

print("Extracted Dates:")
for date in extracted_dates:
    print(date)
