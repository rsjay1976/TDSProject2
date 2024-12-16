import requests
import json
from google.colab import userdata
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import chardet 

def get_csv_data_as_string(file_path):
    try:
        with open(file_path, "rb") as file:
            result_encode = chardet.detect(file.read()) 
            print(result_encode)           
            encoding_csv = result_encode['encoding']
            print (encoding_csv)
        with open(file_path, mode='r', encoding='Windows-1252') as csv_file:
            reader = csv.reader(csv_file)
            
            # Read the header
            header = next(reader, None)
            
            # Read the first two rows
            first_two_rows = [next(reader, None) for _ in range(2)]
            
            # Combine header and rows into a single string
            csv_data = "\n".join([",".join(header)] + [",".join(row) for row in first_two_rows if row])
            
            return csv_data
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def generate_readme_content(csv_content,img_heat,img_outlier, proxy_url,auth_token):
    # Prepare the payload
    prompt = f"""
    for csv data:
    
    {csv_content}
    
    and  the correlation heatmap image:
    
    {img_heat}
    
    and outlier image:

    {img_outlier}
    
    
    
    1. please gnerate readme
    """
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that generates Python code."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }
    
        # Send a POST request to the proxy server
    response = requests.post(
            proxy_url,
            headers={"Content-Type": "application/json",
                     
            "Authorization": f"Bearer {auth_token}"},
            data=json.dumps(payload)
        )
    response_data = response.json()
    return response_data["choices"][0]["message"]["content"]

def generate_code_via_proxy(csv_content, proxy_url,auth_token):
    # Prepare the payload
    prompt = f"""
    Given the following CSV data:

    {csv_content}

    Generate Python code to:
    1. Read a input csv file passed as a parameter in above format 
    2. Find correlation among coloumns
    3. Find any outlier
    4. Please avoid any character in like '''
    5. The output will be run with exec to which the csv file will be passed as context input
    6. Please generate the output without any extra documentation so that it can be directly passed to exec.
    7. Please include the function call in generated code so that it can be used in exec command
    8. global variable csv_file need to be used in  function call. Please dont initialize it.
    9. Please handle invalid data to avoid "could not convert string to float" kind of  errors    
    10. Please use seaborn api to pictorially depict the correlation as heatmap. store as  heatmap.png. Please keep size of image minimum
    11. Please use the best chart to depict outlier. Store as outlier.png.Please keep size of image minimum.
    
    """
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that generates Python code."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }

    try:
        # Send a POST request to the proxy server
        response = requests.post(
            proxy_url,
            headers={"Content-Type": "application/json",
                     
            "Authorization": f"Bearer {auth_token}"},
            data=json.dumps(payload)
        )
        
        # Check the response status
        if response.status_code != 200:
            raise Exception(f"Proxy returned status code {response.status_code}: {response.text}")

        # Parse and return the generated code
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]

    except Exception as e:
        print(f"Error communicating with the proxy: {e}")
        return None

# Example usage
proxy_url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
auth_token=userdata.get('aiproxy_secret_key')
csv_file = "media.csv"  # Replace with the path to your CSV file


csv_data = get_csv_data_as_string(csv_file)

# csv_data = """Name,Age,Location
# Alice,30,New York
# Bob,25,San Francisco
# Charlie,35,Los Angeles"""
generated_code = generate_code_via_proxy(csv_data, proxy_url,auth_token)

if generated_code:
    print("Generated Code:")
    print(generated_code)
print("****************")
start_marker = "```python"
end_marker = "```"

# Extract the code block
if start_marker in generated_code and end_marker in generated_code:
    code_start = generated_code.index(start_marker) + len(start_marker)
    code_end = generated_code.index(end_marker, code_start)
    generated_code = generated_code[code_start:code_end].strip()
    print (generated_code)
    try:
     exec (generated_code)   
    except Exception as e:
      print("Error:", e)



imageheat = mpimg.imread("heatmap.png")
imageoutlier= mpimg.imread("outlier.png")

generated_readme = generate_readme_content(csv_data,imageheat,imageoutlier, proxy_url,auth_token)
print (generated_readme)
with open("readme1.md", "w") as file:
    file.write(generated_readme)