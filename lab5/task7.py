import re

def extract_email_addresses(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_addresses = re.findall(email_pattern, text)

    return email_addresses

text_block = """
Hello, you can reach me at john.doe@example.com for any inquiries.
You can also contact my colleague at jane_doe123@company.org.
Another email you might need is support@my-site.net.
However, invalid emails like user@com or user@.com should not be included.
"""

emails = extract_email_addresses(text_block)

print("Extracted Email Addresses:")
for email in emails:
    print(email)
