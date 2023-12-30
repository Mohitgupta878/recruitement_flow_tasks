
import json
import re

content = """
Contact
www.linkedin.com/in/martin-boyle-59031711 (LinkedIn)
Top Skills
Stakeholder Management
Business Transformation
Project Delivery
Martin Boyle
COO & Executive Director | CTO | Transformation
Bristol, England, United Kingdom
Experience
The West Brom
COO & Executive Director West Brom
April 2023 - Present (8 months)
West Bromwich, England, United Kingdom
Metro Bank (UK)
Chief Transformation Officer Metro Bank
June 2020 - April 2023 (2 years 11 months)
London
Nationwide Building Society
8 years 8 months
Chief Transformation Officer
November 2016 - June 2020 (3 years 8 months)
Swindon, United Kingdom
Director Business Transformation
November 2011 - November 2016 (5 years 1 month)
Responsible for all Group Change Programmes including investment budget.
Nationwide Building Society
Head of Group Programmes
August 2007 - 2010 (3 years)
Accenture
Manager
1994 - 2003 (9 years)
Education
Cambridge University
Master of Philosophy (MPhil), Management Studies · (1993 - 1994)
Queens University Belfast
Bachelor of Science (BSc), Computer Science · (1989 - 1992)
"""
contents="/content/Profile - 2023-11-08T204134.129.pdf"

# Extract LinkedIn profile link
linkedin_profile = re.search(r'(www.linkedin.com/in/[^\s?]+)', content)
linkedin_profile = linkedin_profile.group(0) if linkedin_profile else None


# Extract experience details
experience_details = []
experience_data = re.findall(r'Experience(.*?)Education', content, re.DOTALL)
for exp in experience_data:
    exp_matches = re.findall(r'(.+?)\n(.+?)\n(.+?) - (.+?) \((.+?)\)', exp)
    for match in exp_matches:
        exp_detail = {
            "organization": match[0],
            "designation": match[1],
            "from": match[2],
            "to": match[3],
            "duration": match[4]
        }
        experience_details.append(exp_detail)

# Extract education details
education_details = []
education_data = re.findall(r'Education(.*?)$', content, re.DOTALL)
for edu in education_data:
    edu_matches = re.findall(r'(.+?)\n(.+?) \((\d+) - (\d+)\)', edu)
    for match in edu_matches:
        edu_detail = {
            "institution": match[0],
            "degree": match[1],
            "from": match[2],
            "to": match[3]
        }
        education_details.append(edu_detail)

# Output
output = {
    "linkedin_profile": linkedin_profile,
    "experience": experience_details,
    "education": education_details
}


#print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in output.items()) + "}")
#print (*[(x,y)for x,y in output.items()],sep="\n")

'''def print_nested_dict(dictionary, indent=0):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print("  " * indent + f"{key}:")
            print_nested_dict(value, indent + 1)
        else:
            print("  " * indent + f"{key}: {value}")
'''


# Print the nested dictionary in sequential order
#print_nested_dict(output)
print(json.dumps(output, indent=4))
