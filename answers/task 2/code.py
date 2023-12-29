import pandas as pd
import json

def create_json_from_excel(sheet1_path, sheet2_path):
    
    candidates_df = pd.read_excel(sheet1_path)
    jobs_df = pd.read_excel(sheet2_path)

    
    candidates_data = {}

    
    for index, row in candidates_df.iterrows():
        candidate_id = row['Candidate ID']
        email = row['Email']
        phone = row['Phone']

        
        if candidate_id not in candidates_data:
            candidates_data[candidate_id] = {
                "id": candidate_id,
                "name": row['Name'],
                "email": email,
                "title": row['Job Title'],
                "org": row['Company'],
                "source": row['Source'],
                "lead_owner": row['Lead owner'],
                "added_by": row['Added by'],
                "jobs": [],
                "experience": [],
                "education": []
            }

            
            for i in range(1, 4):
                degree_key = f'Degree {i}'
                school_key = f'School {i}'
                start_key = f'Education Start {i}'
                end_key = f'Education End {i}'

                if not pd.isnull(row[degree_key]):
                    candidates_data[candidate_id]["education"].append({
                        "degree": row[degree_key],
                        "school": row[school_key],
                        "from": [row[start_key], None],
                        "to": [row[end_key], None]
                    })

            
            for i in range(1, 4):
                title_key = f'Title {i}'
                company_key = f'Company {i}'
                start_key = f'Experience Start {i}'
                end_key = f'Experience End {i}'

                if not pd.isnull(row[title_key]):
                    candidates_data[candidate_id]["experience"].append({
                        "designation": row[title_key],
                        "organization": row[company_key],
                        "from": [row[start_key], None],
                        "to": [row[end_key], None]
                    })

        
        candidate_jobs = jobs_df[(jobs_df['Email'] == email) | (jobs_df['Phone'] == phone)]
        for _, job_row in candidate_jobs.iterrows():
            candidates_data[candidate_id]["jobs"].append(job_row['Jobs'])

    
    candidates_list = list(candidates_data.values())

    
    json_data = json.dumps(candidates_list, indent=2)

    
    with open('output.json', 'w') as json_file:
        json_file.write(json_data)

    print("JSON file created successfully.")


sheet1_path = "/content/Sheet1.xlsx"
sheet2_path = "/content/Sheet2.xlsx"
create_json_from_excel(sheet1_path, sheet2_path)
