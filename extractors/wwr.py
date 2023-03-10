from requests import get
from bs4 import BeautifulSoup

def wwr_extractor(keyword):
    baseUrl="https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
    response = get(f"{baseUrl}{keyword}")
    results = []
    
    soup = BeautifulSoup(response.text, "lxml")
    jobs_sections = soup.find_all("section", class_="jobs")
    for jobs_section in jobs_sections:
        job_posts = jobs_section.find_all("li")
        job_posts.pop(-1)
        for job_post in job_posts:
            anchors = job_post.find_all("a")
            job_info = anchors[1]
            href = job_info["href"]
            position = job_info("span", class_="title")[0]
            company, region = job_info.find_all("span", class_="company")
            data = {
                "title": position.string,
                "company": company.string.replace(",", " "),
                "region": region.string.replace(",", " "),
                "link": f"https://weworkremotely.com/{href}"
            }
            results.append(data)
        return results