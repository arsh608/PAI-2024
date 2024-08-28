def convert_url():
    url = input("Enter your URL (should start with http://www.): ")
    if url.startswith("http://www."):
        new_url = url[11:] + ".com"
        print(f"Converted URL: {new_url}")
    else:
        print("Invalid URL format. It should start with 'http://www.'")

convert_url()
