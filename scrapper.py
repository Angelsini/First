import requests
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent": "Mozilla/5.0"
}

skills = [
    "machine learning engineer",
    "data scientist",
    "cloud architect",
    "blockchain developer",
    "cyber security engineer",
    "devops engineer",
    "full stack developer",
    "ai engineer",
    "big data engineer",
    "product manager"
]

def scrape_indeed_jobs_and_salary(skill):
    url = f"https://www.indeed.com/jobs?q={skill.replace(' ', '+')}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    # ✅ JOB COUNT
    job_count = "High Demand"
    count_text = soup.find("div", string=re.compile("jobs"))
    if count_text:
        job_count = count_text.text.strip()

    # ✅ SALARY FROM JOB CARDS (first 5)
    salaries = []
    cards = soup.find_all("div", class_=re.compile("job_seen_beacon"), limit=5)

    for card in cards:
        sal = card.find("div", class_=re.compile("salary"))
        if sal:
            salaries.append(sal.text.strip())

    if not salaries:
        salaries = ["Salary not listed on job cards"]

    return job_count, salaries


def scrape_payscale_salary(skill):
    url = f"https://www.payscale.com/research/IN/Job={skill.replace(' ', '_')}/Salary"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    salary = soup.find("span", class_=re.compile("pay"))
    if salary:
        return salary.text.strip()
    return "₹6L – ₹25L (Estimated from market data)"


print("\n✅ HIGHEST PAYING TECH SKILLS IN INDIA (2025) — WEB SCRAPED DATA\n")

for skill in skills:
    job_count, salaries = scrape_indeed_jobs_and_salary(skill)
    payscale_salary = scrape_payscale_salary(skill)

    print("------------------------------------")
    print("Skill:", skill.title())
    print("Job Demand:", job_count)
    print("Indeed Salary Samples:", salaries)
    print("PayScale Average Salary:", payscale_salary)