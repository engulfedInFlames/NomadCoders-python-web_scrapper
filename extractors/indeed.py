from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_page_count(keyword):
    base_url = f"https://kr.indeed.com/jobs?q={keyword}"
    options = Options()
    browser = webdriver.Chrome(options=options)
    browser.get(base_url) 
    soup = BeautifulSoup(browser.page_source, "lxml")
    pagination = soup.find("nav", role="navigation")
    pages = pagination.find_all("div", recursive=False)
    count = len(pages)
    if count == 0:
        return 1
    elif count >= 5:
        return 5
    else:
        return count

def indeed_extractor(keyword):
    pages = get_page_count(keyword)
    print(pages, "pages founded")
    base_url = f"https://kr.indeed.com/jobs?q={keyword}"
    results = []
    for page in range(pages):
        final_url = f"{base_url}&start={page*10}"
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Chrome(options=options)
        browser.get(final_url)
        soup = BeautifulSoup(browser.page_source, "lxml")
        jobs = soup.find_all("td", class_="resultContent") 
        for job in jobs:
            anchor = job.select_one("h2 a")
            title = anchor["aria-label"]
            link = anchor["href"]
            company = job.find("span", class_="companyName")
            region = job.find("div", class_="companyLocation")
            data = {
                "title": title.replace(","," "),
                "company": company.string.replace(",", " "),
                "region": region.string.replace(",", " "),
                "link": f"https://kr.indeed.com{link}",
            }
            results.append(data)
    return results