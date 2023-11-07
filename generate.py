_name = "Colin McAllister"
_bio = '''
I'm a motivated security practitioner and developer, specializing in SIEM/SOAR operations, Python, cybersecurity fundamentals, incident handling, and Sigma rules. I'm dedicated to solving complex security challenges and proactively strengthening systems against emerging threats. I thrive on continuous learning and adaptability in the ever-evolving cybersecurity landscape. Let's connect to collaborate and bolster digital defenses for a safer digital world.'''

work_experience = {
    "Arctic Wolf Networks": [
        {
            "job_title" : "Security Developer",
            "location" : "San Antonio, TX",
            "start_date" : "July 2020",
            "end_date" : "Present",
            "responsibilities" : []
        },
        {
            "job_title" : "Business Analyst",
            "location" : "San Antonio, TX",
            "start_date" : "July 2019",
            "end_date" : "July 2020",
            "responsibilities" : []
        }
    ]

}

def generate_work_experience(work_experience):
    markdown_string = "## Work Experience\n\n"
    for company, jobs in work_experience.items():
        markdown_string += f"### {company}\n"
        for job in jobs:
            markdown_string += f"**{job['job_title']}**\n"
            markdown_string += f"->_{job['location']}_\n\n"
            markdown_string += f"**{job['start_date']} to {job['end_date']}**\n\n"
            for responsibility in job['responsibilities']:
                markdown_string += f"- {responsibility}\n"
                
    return markdown_string

markdown = f'''
# **{_name}**
{_bio}

{generate_work_experience(work_experience)}
## Skills

Technical: `Python` `Go` `Microservices Architecture`

Management: `Kanban Methodology` `Scrum`

## Education

### Carnegie Mellon University
->_2014-2016_
**Masters of Computer Science**, _Pittsburgh, Pennsylvania_

### The State University of NY
->_2010 - 2014_
**Bachelor of Engineering**,  _Oswego, New York_

---

||: Email: **<katemiller@gmail.com>** || Phone: **+123 456 789** || Website: **[katemiller.com](katemiller.com)** :||
- Increased engineering staff's operating efficiency by providing structure, operating procedures, engineering tools, guidelines, and handbooks.
- Contributed to company-wide engineering initiatives
- Supported the engineering and product teams to achieve a high level of technical quality, reliability, and ease-of-use.

**Backend Engineer, Financial Data**
->_April 2018 to December 2018_

- Built large-scale (petabyte-size) financial data platform/solution/pipelines using Big Data technologies
- Worked cross-functionally with many teams: Engineering, Treasury, Finance, Accounting, etc.
- Worked on systems critical to future operation, with impact over billions of dollars of payments volume.
- Developed a deep understanding of modern payments and financial technology across many countries.

### Stripe
->_San Francisco, CA_

**Full Stack Engineer**
-> _September 2016 to March 2018_

- Responsible for developing, maintaining internal web applications
- Collaborated with technical and business staff in design, development, testing and implementation
- Set up, managed and monitored systems to ensure business continuity

### Bloomberg
->_New York, NY_

**Software Engineer Intern**
->_June 2016 to August 2016_

- Worked on Bloomberg's platform to enhance the user experience
- Proactively participated in the team's weekly meetings and conducted reports on the project's progress

## Skills

Technical: `Python` `Go` `Microservices Architecture`

Management: `Kanban Methodology` `Scrum`

## Education

### Carnegie Mellon University
->_2014-2016_
**Masters of Computer Science**, _Pittsburgh, Pennsylvania_

### The State University of NY
->_2010 - 2014_
**Bachelor of Engineering**,  _Oswego, New York_

---

||: Email: **<katemiller@gmail.com>** || Phone: **+123 456 789** || Website: **[katemiller.com](katemiller.com)** :||
'''

# Write the content to a Markdown file
with open("resume.md", "w") as file:
    file.write(markdown)
    file.write("\n\n")  # Separate the sections with a newline
    # file.write(kate_content)

print("Markdown file 'resume.md' has been generated.")