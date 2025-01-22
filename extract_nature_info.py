import requests
import pandas as pd
import time

def get_nature_info(id):
    url = f"https://pokeapi.co/api/v2/nature/{id}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        nature_data = response.json()

        # Flatten the nature info
        nature_info = {
            "nature_id": id,
            "name": nature_data["name"],
        }

        # Flatten move_battle_style_preferences
        for i, move_battle_style in enumerate(nature_data["move_battle_style_preferences"], 1):
            nature_info[f"move_battle_style_{i}_name"] = move_battle_style["move_battle_style"]["name"]
            nature_info[f"move_battle_style_{i}_high_hp_preference"] = move_battle_style["high_hp_preference"]
            nature_info[f"move_battle_style_{i}_low_hp_preference"] = move_battle_style["low_hp_preference"]

        # Flatten pokeathlon_stat_changes
        for i, stat_change in enumerate(nature_data["pokeathlon_stat_changes"], 1):
            nature_info[f"pokeathlon_stat_change_{i}_name"] = stat_change["pokeathlon_stat"]["name"]
            nature_info[f"pokeathlon_stat_change_{i}_max_change"] = stat_change["max_change"]

        return nature_info
    else:
        return None

# Function to retrieve and retry on failure
def get_nature_data(ids):
    nature_data_list = []
    
    for id in ids:
        while True:
            print(f"Fetching data for Nature ID: {id}")
            nature_info = get_nature_info(id)
            if nature_info:
                nature_data_list.append(nature_info)
                print(f"Successfully fetched data for Nature ID: {id}")
                break  # Exit the retry loop on success
            else:
                print(f"Failed to fetch data for Nature ID: {id}. Retrying...")
                time.sleep(2)  # Wait before retrying
    
    return nature_data_list

# Main script execution
if __name__ == "__main__":
    # List of Nature IDs to fetch data for (1 to 25)
    nature_ids = list(range(1, 26))
    
    # Get Nature data with retries
    nature_data_list = get_nature_data(nature_ids)
    
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(nature_data_list)
    
    # Export the DataFrame to a CSV file
    df.to_csv('nature_data.csv', index=False, encoding='utf-8')
    print("CSV file has been created: nature_data.csv")
