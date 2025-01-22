# Pokemon Analysis

## Setup
The process involved in the project is shown in the image below
![image](https://github.com/user-attachments/assets/9605ec48-c909-486b-b2c5-6c6305212a31)

- The API was tested on Postman to see how the API will respond
- Load the API using Python
- For Pokemon Info, the ID was loaded from 1-100
- For Character Info, the ID was loaded from 1-30
- For Nature Info, the ID was loaded from 1-25
- We flatten the JSON data and export it as CSV
- We use the CSV as a datasource for the dashboard

## Dashboard
The output of the assessment is a dashboard. 

It can be accessed on this dashboard link

[Dashboard](https://lookerstudio.google.com/reporting/1b2f0f97-e715-4ffe-8898-e7d2fe8cf4bc)

This is a screenshot of the dashboard for order analysis
![image](https://github.com/user-attachments/assets/a5d8db6f-df43-426e-9832-22342e255d52)
![image](https://github.com/user-attachments/assets/8413fc4a-7b57-4bac-a6d1-b4c10864904c)

The dashboard contains the following charts
- Pie Graphs for least and favorite flavor
- Table about Pokemon Nature and Pokemon Characteristic
- Table for Average Stats per Pokemon Primary Type

## Scrips
The Python scripts used in this project are
- `extract_pokemon_info.py` to extract pokemon general info
- `extract_nature_info.py` to extract pokemon nature info
- `extract_character_info.py` to extract pokemon character info
