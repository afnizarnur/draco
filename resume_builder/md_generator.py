import json
from datetime import datetime

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON. Please ensure the file is a valid JSON format.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to generate skills section
def generate_skills(skills=None, specialty_skills=None):
    markdown = "## Skills\n\n"
    if not skills and not specialty_skills:
        return None
    if skills:
        for skill in skills:
            markdown += f"```{skill}```\n"
        markdown += "\n"
    if specialty_skills:
        for spskill in specialty_skills:
            markdown += f"**{spskill['name']}**: "
            for keyword in spskill['keywords']:
                markdown += f"{keyword}"
                if keyword != spskill['keywords'][-1]:
                    markdown += ", "
            markdown += "  \n"
    return markdown

# Function to generate experience section
def generate_experience(work_experience):
    markdown = "## Experience\n\n"
    for company, positions in work_experience.items():
        markdown += f"### {company}  \n"
        for position in positions:
            responsibilities = position.get('responsibilities', None)
            skills = position.get('skills', None)
            markdown += f"#### {position['job_title']}  \n{position['start_date']} - {position['end_date']}, {position['location']}  \n"
            if responsibilities:                
                for responsibility in position['responsibilities']:
                    markdown += f"- {responsibility}  \n"
            if skills:
                markdown += f"*Technologies Used*: "
                for skill in skills:
                    markdown += f"```{skill}```"
                    if skill != skills[-1]:
                        markdown += ", "
                markdown += "  \n"
            
            markdown += "\n"
    return markdown

def generate_certifications(certifications):
    if not certifications:
        return None
    markdown = "## Certifications\n\n"
    for certification in certifications:
        url = certification.get('url', None)
        if url:
            markdown += f"- **[{certification['title']}]({url})** | {certification['date']}\n"
        else: 
            markdown += f"- **{certification['title']}** | {certification['date']}\n"
    return markdown

# Function to generate education section
def generate_education(education):
    if not education:
        return None
    markdown = "## Education\n\n"
    for edu in education:
        courses = edu.get('courses', None)
        honors = edu.get('honors', None)
        gpa = edu.get('score', None)
        start_year = datetime.strptime(edu['startDate'], '%Y-%m-%d').year
        try:
            end_year = datetime.strptime(str(edu['endDate']), '%Y-%m-%d').year
        except ValueError:
            # endDate is not a valid date, use it as a string
            end_year = edu['endDate']
        
        markdown += f"### {str(edu['studyType'])} in {edu['area']} @ {edu['institution']}\n"
        markdown += f"{start_year} - {end_year}  \n"
        if honors:
            markdown += f"- Honors: *{honors}*  \n"
        if gpa:
            markdown += f"- GPA: *{gpa}*  \n"
        if courses:
            markdown += f"- Courses: {', '.join(edu['courses'])}  \n"
        markdown += "  \n"
    return markdown

# Function to generate awards section
def generate_awards(awards):
    if not awards:      
        return None
    markdown = "## Awards & Recognition\n\n"
    for award in awards:
        markdown += f"- **{award['title']}** | {award['awarder']} ({get_month_and_year(award['date'])})  \n"
    return markdown

def get_month_and_year(date):
    if date == 'Present':
        return date
    return datetime.strptime(date, '%Y-%m-%d').strftime('%b %Y')

# Function to generate projects section
def generate_projects(projects):
    if not projects:
        return None
    markdown = "## Projects\n\n"
    for project in projects:
        project_url = (project.get('url',None))
        markdown += f"**{project['name']}**" + (f"[{project_url}]({project_url})" if project_url else "") + f" ({get_month_and_year(project['startDate'])} - {get_month_and_year(project['endDate'])})  \n"
        markdown += f"*{project['description']}*  \n"
        for highlight in project['highlights']:
            markdown += f"- {highlight}  \n"
        markdown += "\n"
    return markdown

def generate_keywords(skills):
    keywords = ""
    for skill in skills:
        keywords += f"- {skill}\n"
    return keywords

def generate_contact_info(contact_info):
    markdown = "###### "
    for contact in contact_info:
        markdown += f"{contact['title']}: **{contact['value']}**"
        if contact != contact_info[-1]:
            markdown += " | "
    return markdown

if __name__ == "__main__":
    # Reading the JSON file
    json_data = read_json_file('resume.json')
    # Generating the markdown
    markdown = f'''---
margin-left: 2cm
margin-right: 2cm
margin-top: 1cm
margin-bottom: 2cm
title: {json_data['basics']['name']}
description-meta: 'Resume of {json_data['basics']['name']} - {json_data['basics']['label']}'
keywords:
{generate_keywords(json_data['skills'])}
author:
- {json_data['basics']['name']}
subject: 'Resume'
---
{generate_contact_info(json_data['basics']['contact_info'])}

#### {json_data['basics']['summary']}

{generate_skills(json_data['skills'], json_data.get('specialty_skills', None))}
{generate_certifications(json_data.get('certifications', None))}
{generate_education(json_data.get('education', None))}
{generate_experience(json_data['work_experience'])}
{generate_awards(json_data.get('awards', None))}
{generate_projects(json_data.get('projects', None))}

<!-- pandoc colins_resume.md -f markdown -t html -c resume-stylesheet.css -s -o resume.html -->
<!-- wkhtmltopdf --enable-local-file-access resume.html resume.pdf -->'''

    # Write the content to a Markdown file
    with open("colins_resume.md", "w") as file:
        file.write(markdown)
