import requests
import pandas as pd
import time

def get_pokemon_info(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        
        # Flatten the Pokémon info
        pokemon_info = {
            "pokemon_id": id,
            "name": pokemon_data["name"],
            "base_experience": pokemon_data["base_experience"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
        }

        # Flatten the stats into separate fields
        for stat_data in pokemon_data["stats"]:
            stat_name = stat_data["stat"]["name"]
            base_stat = stat_data["base_stat"]
            pokemon_info[f"stats_{stat_name}"] = base_stat

        # Flatten abilities into separate columns (ability_1, ability_2, etc.)
        for i, ability in enumerate(pokemon_data["abilities"], 1):
            pokemon_info[f"ability_{i}"] = ability["ability"]["name"]
        
        # Flatten types into separate columns (type_1, type_2, etc.)
        for i, type_data in enumerate(pokemon_data["types"], 1):
            pokemon_info[f"type_{i}"] = type_data["type"]["name"]
        
        return pokemon_info
    else:
        return None

# Function to retrieve and retry on failure
def get_pokemon_data(ids):
    pokemon_data_list = []
    
    for id in ids:
        while True:
            print(f"Fetching data for Pokémon ID: {id}")
            pokemon_info = get_pokemon_info(id)
            if pokemon_info:
                pokemon_data_list.append(pokemon_info)
                print(f"Successfully fetched data for Pokémon ID: {id}")
                break  # Exit the retry loop on success
            else:
                print(f"Failed to fetch data for Pokémon ID: {id}. Retrying...")
                time.sleep(2)  # Wait before retrying
    
    return pokemon_data_list

# Main script execution
if __name__ == "__main__":
    # List of Pokémon IDs to fetch data for (1 to 100)
    pokemon_ids = list(range(1, 101))
    
    # Get Pokémon data with retries
    pokemon_data_list = get_pokemon_data(pokemon_ids)
    
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(pokemon_data_list)
    
    # Export the DataFrame to a CSV file
    df.to_csv('pokemon_data.csv', index=False, encoding='utf-8')
    print("CSV file has been created: pokemon_data.csv")
