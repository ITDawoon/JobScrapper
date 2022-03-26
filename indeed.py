import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?as_and=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class": "pagination"})
  links = pagination.find_all('a')
  pages = []
  
  for link in links[:-1]:
    pages.append(int(link.string))

  max_page = (pages[-1])
  return max_page


def extract_indeed_jobs(last_page):
  jobs = []
  #for page in range(last _page):
  result = requests.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")

  # Find all jobs
  results = soup.find_all("a", {"class": "fs-unmask"})
  print("")
  
  for result in results:
    # Jobs' title
    jobTitle = result.find("h2", {"class": "jobTitle"})
    title = jobTitle.find("span", title = True).string
    if title == "new":
      title = jobTitle.find_all("span")[1].string
    #print(title)

    # Jobs' company
    company = result.find("span", {"class": "companyName"})
    company_anchor = company.find("a")
    if company_anchor is not None:
      company = str(company_anchor.string)
    else:
      company = str(company.string)
      company = company.strip()
    #print(company)
    print(title, company)
  return jobs