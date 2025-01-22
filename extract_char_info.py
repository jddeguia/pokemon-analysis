import requests
import pandas as pd
import time

def get_characteristic_info(id):
    url = f"https://pokeapi.co/api/v2/characteristic/{id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        characteristic_data = response.json()
        
        # Initialize the characteristic info
        characteristic_info = {
            "characteristic_id": id,
            "gene_modulo": characteristic_data["gene_modulo"],
            "highest_stat": characteristic_data["highest_stat"]["name"],
        }
        
        # Extract the English description
        en_description = next((desc["description"] for desc in characteristic_data["descriptions"] if desc["language"]["name"] == "en"), None)
        characteristic_info["description_en"] = en_description
        
        return characteristic_info
    else:
        return None

# Function to retrieve and retry on failure
def get_characteristic_data(ids):
    characteristic_data_list = []
    
    for id in ids:
        while True:
            print(f"Fetching data for Characteristic ID: {id}")
            characteristic_info = get_characteristic_info(id)
            if characteristic_info:
                characteristic_data_list.append(characteristic_info)
                print(f"Successfully fetched data for Characteristic ID: {id}")
                break  # Exit the retry loop on success
            else:
                print(f"Failed to fetch data for Characteristic ID: {id}. Retrying...")
                time.sleep(2)  # Wait before retrying
    
    return characteristic_data_list

# Main script execution
if __name__ == "__main__":
    # List of Characteristic IDs to fetch data for (1 to 30)
    characteristic_ids = list(range(1, 31))
    
    # Get Characteristic data with retries
    characteristic_data_list = get_characteristic_data(characteristic_ids)
    
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(characteristic_data_list)
    
    # Export the DataFrame to a CSV file
    df.to_csv('characteristic_data.csv', index=False, encoding='utf-8')
    print("CSV file has been created: characteristic_data.csv")
