'''
This module scraps the web to extract job specific information from the given url.
'''


import requests
from bs4 import BeautifulSoup


def get_job_info(url):
    
    # Send a GET request to the URL
    response = requests.get(url).text

    # Create a BeautifulSoup object for parsing the HTML content
    soup = BeautifulSoup(response, 'html.parser')

    # Extract specific information from the page using BeautifulSoup methods
    role_name = soup.find('h1', class_='top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title').get_text().strip()
    company_name = soup.find('a', class_='topcard__org-name-link topcard__flavor--black-link').get_text().strip()
    
    '''
    When extracting the contents of the div with the job description we dont want the 'Show More' and 'Show Less' button contents.
    Hence, we extract those out. And while joining the content of different elements inside the div, we add space between them.
    The space was not alrerady there and it looked like a single word, when it was not.
    '''
    parent_div_desc = soup.find('div', class_='description__text description__text--rich')
    buttons = parent_div_desc.find_all('button')
    for button in buttons:
        button.extract()

    # Extract the text from the div
    text_elements = [element.text.strip() for element in parent_div_desc.find_all(text=True) if element != '\n']
    description = ' '.join(text_elements)

    return role_name, company_name, description
