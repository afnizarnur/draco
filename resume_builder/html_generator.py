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
    
def generate_header(basics):
    f_name = basics['name'].split(' ')[0]
    return f'''<head>
    <title>{f_name}\'s Resume</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{basics.get('name')}\'s Digital Resume">
    <meta name="author" content="{basics.get('name')}">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="css/kube.min.css" />
    <link rel="stylesheet" href="css/font-awesome.min.css" />
    <link rel="stylesheet" href="css/custom.min.css" />
    <link rel="shortcut icon" href="img/favicon.ico" />
	<link href='https://fonts.googleapis.com/css?family=Playfair+Display+SC:700' rel='stylesheet' type='text/css'>
	<link href='https://fonts.googleapis.com/css?family=Lato:400,700' rel='stylesheet' type='text/css'>
	<style>
		.intro h1:before {{
			content: "{f_name}";
		}}
	</style>
</head>'''

def generate_navigation(json_data):
	def generate_header_list(json_keys):
		header_list = '''<li class="active"><a href="#about">About</a></li><li><a href="#experiences">Experiences</a></li><li><a href="#education">Education</a></li>'''
		for key in json_keys:
			if key in ['publications','projects']:
				key = key.replace('_', ' ')
				header_list += f'<li><a href=\"#{key}\">{key.title()}</a></li>'
		return header_list

	f_name = json_data.get('basics').get('name').split(' ')[0]
	return f'''<!-- Navigation -->
	<div class="main-nav">
		<div class="container">
			<header class="group top-nav">
				<div class="navigation-toggle" data-tools="navigation-toggle" data-target="#navbar-1">
				    <span class="logo">{f_name.upper()}</span>
				</div>
			    <nav id="navbar-1" class="navbar item-nav">
				    <ul>
				        {generate_header_list(json_data.keys())}
				    </ul>
				</nav>
			</header>
		</div>
	</div>'''

def generate_introduction(basics):
	markup = f'''<!-- Introduction -->
	<div class="intro section" id="about">
		<div class="container">
			<p>Hi, I’m {basics['name'].split(' ')[0]}</p>
			<div class="units-row units-split wrap">
				<div class="unit-20">
					<img src="{basics.get('image')}" alt="Avatar">
				</div>
			  <div class="unit-80">
					<h1>My passions are<br><span id="typed"></span></h1>
				</div>
			  <p>{basics['summary']}</p>
			</div>
		</div>
	</div>'''
	return markup

def generate_work_experience(work_experience):
	markup = '''<!-- Work Experience / Volunteer --><div class="work section second" id="experiences">
 	<div class="container">
		<h1>Work<br>Experiences</h1>'''
	for company, experiences in work_experience.items():
		markup += f'''<ul class="work-list">
			<li><a href="#">{company}</a></li>'''
		for experience in experiences:
			markup += f"<li>{experience.get('job_title')}</li>"
		markup += "</ul>"
	markup += "</div></div>"  
	return markup

def generate_education_and_certs(education=None, certifications=None, awards=None):
	if not certifications and education:
		return None
	if certifications:
		markup = '''<!-- Certifications --><div class="certifications section second" id="certifications">
		<div class="container">
			<h1>CERTIFICATIONS &amp;<br>Education<br></h1>
				<ul class="award-list list-flat"><li>Certifications</li>'''
		for certification in certifications:
			if certification.get('url', None):
				title = f'''<a href="{certification.get('url')}" target="_blank">{certification.get('title')}</a>'''
			else:
				title = f"{certification.get('title')}"
			markup += f"<li>{title} | {certification.get('date')}</li>"
		markup += '''</ul>'''
	elif education:
		markup = '''<!-- Education --><div class="education section second" id="education">
		<div class="container">
			<h1>Education<br></h1>'''
	markup += '''<ul class="award-list list-flat">
<li>Education</li>'''
	for school in education:
		url = school.get('url', None)
		honors = school.get('honors', None)
		gpa = school.get('score', None)
		markup += f"<li><b>{school.get('studyType')} in {school.get('area')}</b></li>"
		if url:    
			markup += f'''<li><a href={url} target="_blank">{school.get('institution').title()}</a></li>'''
		else: 
			markup += f"<li><b>{school.get('institution')}</b></li>"
		if honors:
			markup += f"<li>{honors.title()}</li>"
		elif gpa:
			markup += f"<li>GPA: {gpa}</li>"
		markup += f"<li><i>{school.get('startDate')} - {school.get('endDate')}</i></li>"
		if school != education[-1]:
			markup += "<br>"
	markup += "</ul>"
	if awards:
		markup += '''<ul class="award-list list-flat"><li>Awards</li>'''
		for award in awards:
			markup += f"<li><b>{award.get('title')}</b> | {award.get('awarder').title()} | <i>{award.get('date')}</i></li>"
	markup += "</ul></div></div>"
	return markup


if __name__ == "__main__":
    # Reading the JSON file
    json_data = read_json_file('draco-resume/resume_builder/resume.json')
    
    # Generating the markup
    markup = f'''<!DOCTYPE html>
<html>
{generate_header(json_data.get('basics'))}
<body>
	{generate_navigation(json_data)}
	{generate_introduction(json_data.get('basics'))}
	{generate_work_experience(json_data.get('work_experience'))}
	{generate_education_and_certs(json_data.get('education', None), json_data.get('certifications', None),json_data.get('awards', None))}
	<!-- Technical Skills -->
	<div class="skills section second" id="skills">
		<div class="container">
			<h1>Technical<br>Skills</h1>
			<ul class="skill-list list-flat">
				<li>Personal</li>
				<li>Problem-Solving / Eagerness to Learn / Effective Communication</li>
			</ul>
			<ul class="skill-list list-flat">
				<li>Development</li>
				<li>Python (OOP) / Git / AWS / Sigma Rules </li>
			</ul>
			<ul class="skill-list list-flat">
				<li>Security</li>
				<li>Network Forensics / SIEM & SOAR / Incident Handling </li>
			</ul>
		</div>
	</div>

	<!-- Quote -->
	<div class="quote">
		<div class="container text-centered">
			<h1>Automate / Educate / Secure</h1>
		</div>
	</div>

	<footer>
		<div class="container">
			<div class="units-row">
			    <div class="unit-50">
			    	<p>Colin McAllister</p>
			    </div>
			    <div class="unit-50">
					<ul class="social list-flat right">
						<li><a href="https://www.linkedin.com/in/offsetcolin/" target="_blank"><i class="fa fa-linkedin-square"></i></a></li>
						<li><a href="https://github.com/offsetkeyz" target="_blank"><i class="fa fa-github-square"></i></a></li>
					</ul>
			    </div>
			</div>
		</div>
	</footer>

	<!-- Javascript -->
	<script src="js/jquery.min.js"></script>
	<script src="js/typed.min.js"></script>
    <script src="js/kube.min.js"></script>
    <script src="js/site.js"></script>
    <script>
		function newTyped(){{}}$(function(){{$("#typed").typed({{
		// Change to edit type effect
		strings: ["Automation", "Security", "Python", "Music", "Photography"],

		typeSpeed:89,backDelay:700,contentType:"html",loop:!0,resetCallback:function(){{newTyped()}}}}),$(".reset").click(function(){{$("#typed").typed("reset")}})}});
    </script>
    
</body>
</html>
'''

    # Write the content to a markup file
    with open("./draco-resume/resume_draco.html", "w") as file:
        file.write(markup)
