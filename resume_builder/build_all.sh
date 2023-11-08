python3 md_generator.py
python3 html_generator.py
pandoc colins_resume.md -f markdown -t html -c resume-stylesheet.css -s -o resume.html
wkhtmltopdf --enable-local-file-access resume.html resume.pdf 