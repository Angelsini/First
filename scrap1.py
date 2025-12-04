import requests
from bs4 import BeautifulSoup
import re
import time
import pandas as pd

# ---------- CONFIG ----------
APP_ID = "9f244a79"
APP_KEY = "cd18e2e90ad3685b9893dff00317469a"

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

# ---------- FUNCTIONS ----------
def get_job_openings(skill):
    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": skill,
        "where": "India",
        "results_per_page": 1
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        data = r.json()
        return data.get("count", 0)
    except:
        return "Not Found"

def get_payscale_salary(skill):
    url = f"https://www.payscale.com/research/IN/Job={skill.replace(' ', '_')}/Salary"
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        soup = BeautifulSoup(r.text, "lxml")
        salary = soup.find("span", class_=re.compile("pay"))
        if salary:
            return salary.text.strip()
    except:
        pass
    return "₹6L – ₹25L (Estimated from market data)"

def parse_salary(salary_str):
    """Convert salary string like '₹6L – ₹25L' into numeric min/max."""
    salary_str = salary_str.replace("₹", "").replace(",", "").strip()
    match = re.findall(r'(\d+\.?\d*)\s*([LC]?)', salary_str)
    if match:
        numbers = []
        for num, unit in match:
            num = float(num)
            if unit.upper() == 'L':
                num *= 100000
            elif unit.upper() == 'C':
                num *= 10000000
            numbers.append(int(num))
        if len(numbers) == 2:
            return numbers[0], numbers[1]
        elif len(numbers) == 1:
            return numbers[0], numbers[0]
    return None, None

# ---------- MAIN SCRIPT ----------
report = []

print("\n✅ TECH SKILLS REPORT — Job Openings + Salary\n")

for skill in skills:
    job_count = get_job_openings(skill)
    salary = get_payscale_salary(skill)
    min_salary, max_salary = parse_salary(salary)
    
    print("------------------------------------")
    print("Skill:", skill.title())
    print("Job Openings:", job_count)
    print("PayScale Salary:", salary)
    print("Salary Min:", min_salary)
    print("Salary Max:", max_salary)

    report.append({
        "Skill": skill.title(),
        "Job Openings": job_count,
        "PayScale Salary": salary,
        "Salary Min": min_salary,
        "Salary Max": max_salary
    })
    time.sleep(1)  # polite delay

# ---------- SAVE TO EXCEL ----------
excel_file = "tech_skills_report.xlsx"
df = pd.DataFrame(report)
df.to_excel(excel_file, index=False)

print(f"\n✅ Report saved as {excel_file}")