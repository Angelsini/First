import requests
import pandas as pd
import statistics

# CONFIG

ADZUNA_APP_ID = "YOUR_ADZUNA_APP_ID"
ADZUNA_APP_KEY = "YOUR_ADZUNA_APP_KEY"

skills = [
    "Python", "Java", "Machine Learning", "Deep Learning", "Data Science",
    "AWS", "React", "Node.js", "DevOps", "Cybersecurity",
    "Kubernetes", "Docker", "AI"
]

COUNTRY = "in"   # in = India, us = USA


# GLASSDOOR SALARY API

def get_salary_from_glassdoor(skill, location="India"):
    """Fetch salaries from Glassdoor public salary endpoint."""
    url = "https://www.glassdoor.com/api/salaries/find"
    params = {"jobTitle": skill, "location": location}

    response = requests.get(url, params=params)

    try:
        data = response.json()
    except:
        return 0  # no data

    salaries = []

    for item in data.get("salaries", []):
        if item.get("meanBasePay"):
            salaries.append(item["meanBasePay"])

    if len(salaries) == 0:
        return 0

    return round(statistics.mean(salaries))


# ADZUNA JOB OPENINGS API

def get_job_openings(skill):
    url = f"https://api.adzuna.com/v1/api/jobs/{COUNTRY}/search/1"

    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "what": skill,
        "results_per_page": 50
    }

    response = requests.get(url, params=params).json()

    return response.get("count", 0)   # total available jobs


# MAIN ANALYSIS

final_data = []

for skill in skills:
    print(f"Fetching data for: {skill} ...")

    avg_salary = get_salary_from_glassdoor(skill)
    openings = get_job_openings(skill)

    final_data.append({
        "skill": skill,
        "salary": avg_salary,
        "job_openings": openings
    })


# Sort by salary (highest first)
final_data.sort(key=lambda x: x["salary"], reverse=True)

df = pd.DataFrame(final_data)

print("\n===============================")
print("TOP PAYING TECH SKILLS")
print("===============================\n")
print(df)


# Display nicely formatted
print("\n========== FINAL OUTPUT ==========\n")
for row in final_data:
    print(
        f"Skill: {row['skill']}\n"
        f"Average Salary: ₹{row['salary']}\n"
        f"Job Openings: {row['job_openings']}\n"
        f"----------------------------------"
    )
