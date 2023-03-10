# from requests import get
# websites = [
#     "https://google.com",
#     "airbnb.com",
#     "https://naver.com",
#     "youtube.com"
# ]

### For case 1
# _websites= []

# for website in websites:
#     if (website.startswith("https://")):
#         _websites.append(website)
#     else:
#         websites.append(f"https://{website}")
# print(_websites)

### For case 2
# _websites = {}

# for website in websites:
#     if not website.startswith("https://"):
#         website = f"https://{website}"
#     response = get(website) # get()의 argument로 오는 url은 http:// 또는 https://로 시작해야 한다.
#     if response.status_code == 200:
#         _websites[website] = "Good"
#     else:
#         _websites[website] = "Bad"
# print(_websites)
        