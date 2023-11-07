_name = "Colin McAllister"
_bio = '''I'm a motivated security practitioner and developer, specializing in SIEM/SOAR operations, Python, cybersecurity fundamentals, incident handling, and Sigma rules. I'm dedicated to solving complex security challenges and proactively strengthening systems against emerging threats. I thrive on continuous learning and adaptability in the ever-evolving cybersecurity landscape. Let's connect to collaborate and bolster digital defenses for a safer digital world.'''

contact_info = [
    {
        "title" : "Email",
        "value" : "colin.mcallister0723@gmail.com"
    },
    {
        "title" : "website",
        "value" : "colinmca.com"
    }#,
    # {
    #     "title" : "phone",
    #     "value" : "555-123-4567"
    # }
]

work_experience = {
    "Arctic Wolf Networks": [
        {
            "job_title" : "Security Developer",
            "location" : "San Antonio, TX",
            "start_date" : "July 2020",
            "end_date" : "Present",
            "responsibilities" : [
                "coding and stuff"
                ],
            "skills" : [],
            "projects" : []
        },
        {
            "job_title" : "Business Analyst",
            "location" : "San Antonio, TX",            
            "start_date" : "July 2019",
            "end_date" : "July 2020",
            "responsibilities" : [],
            "skills" : [],
            "projects" : []
        }
    ]

}

skills = {
    "Personal" : [
        "Problem-Solving",
        "Eagerness to Learn",
        "Effective Communication"
    ],
    "Development" : [
        "Python (OOP)",
        "Git",
        "AWS",
        "Sigma Rules"
    ],
    "Security" : [
        "SIEM/SOAR",
        "Incident Handling",
        "Cybersecurity Fundamentals",
        "Threat Hunting"
    ] 
}

certifications = [
    {
        "title" : "GIAC Advisory Board",
        "date" : "2023",
        "link" : "https://www.credly.com/badges/144c9ca4-ff0e-479e-aef6-7fd2c4d344f0/public_url"
    },
    {
        "title" : "AWS Certified Cloud Practitioner (CCP)",
        "date" : "2023",
        "link" : "https://www.credly.com/badges/febe16fe-eece-4852-be1d-c57db1e1087b/public_url"        
    },
    {
        "title" : "GIAC Network Forensic Analyst (GNFA)",
        "date" : "2022",
        "link" : "https://www.credly.com/badges/d5ca28ac-7c6e-4baa-beb8-56d4ed5bd3c4/public_url"
    },
    {
        "title" : "GIAC Security Essentials (GSEC)",
        "date" : "2023",
        "link" : "https://www.credly.com/badges/d283e815-124b-4cb1-ba60-149a1a73bf05/public_url"
    }
]

education = [
    {
        "title" : "Master's in Cyber Security",
        "school" : "SANS Technical Institute",
        "url" : "https://www.sans.edu/cyber-security-programs/masters-degree/",
        "start_date" : "2023",
        "end_date" : "Present",
        "honors": [],
        "gpa" : "4.0"
    },
    {
        "title" : "Master's in Cyber Security",
        "school" : "SANS Technical Institute",
        "url" : "https://www.sans.edu/cyber-security-programs/masters-degree/",
        "start_date" : "2023",
        "end_date" : "Present",
        "honors": [],
        "gpa" : "4.0"
    }
]

projects = [
    {}
]

social_media = [
    {
        "title" : "LinkedIn",
        "url" : "https://www.linkedin.com/in/offsetcolin/"
    },
    {
        "title" : "GitHub",
        "url" : "https://github.com/offsetkeyz",
    }
]

def generate_work_experience(work_experience):
    markdown_string = "## Work Experience\n"
    for company, jobs in work_experience.items():
        markdown_string += f"### {company}\n"
        for job in jobs:
            markdown_string += f"#### {job['job_title']}\n"
            markdown_string += f"*{job['start_date']} to {job['end_date']}*\n"
            markdown_string += f"_{job['location']}_\n"
            for responsibility in job['responsibilities']:
                markdown_string += f"* {responsibility}\n"   
            markdown_string += "\n"             
    return markdown_string

def generate_skills(skills):
    markdown_string = "## Skills\n\n"
    for category, skill_list in skills.items():
        markdown_string += f"**{category}**\n"
        for skill in skill_list:
            markdown_string += f"- {skill}\n"
    return markdown_string

def generate_certifications(certifications):
    markdown_string = "## Certifications\n\n"
    for certification in certifications:
        markdown_string += f"**{certification['title']}**\n"
        markdown_string += f"->_{certification['date']}_\n"
        markdown_string += f"**[View Certificate]({certification['link']})**\n\n"
    return markdown_string

def generate_education(education):
    markdown_string = "## Education\n\n"
    for degree in education:
        markdown_string += f"**{degree['title']}**\n"
        markdown_string += f"->_{degree['school']}_\n"
        markdown_string += f"**{degree['start_date']} to {degree['end_date']}**\n\n"
        if degree['gpa']:
            markdown_string += f"**GPA: {degree['gpa']}**\n"
        if degree['url']:
            markdown_string += f"**[View Program]({degree['url']})**\n"
        if len(degree['honors']) > 0:
            markdown_string += "**Honors:**\n"
            for honor in degree['honors']:
                markdown_string += f"- {honor}\n"
    return markdown_string

def generate_contact_info(contact_info):
    markdown_string = "||: "
    for contact in contact_info:
        markdown_string += f"{contact['title']}: **<{contact['value']}>**"
        if contact != contact_info[-1]:
            markdown_string += " || "
    markdown_string += " :||"
    return markdown_string

markdown = f'''
# **{_name}**
{_bio}

{generate_work_experience(work_experience)}
{generate_skills(skills)}
{generate_certifications(certifications)}
{generate_education(education)}
---

{generate_contact_info(contact_info)}
'''

# Write the content to a Markdown file
with open("resume.md", "w") as file:
    file.write(markdown)
    file.write("\n\n")  # Separate the sections with a newline
    # file.write(kate_content)

print("Markdown file 'resume.md' has been generated.")