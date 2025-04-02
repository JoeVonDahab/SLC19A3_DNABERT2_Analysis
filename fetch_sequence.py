import requests
import json

def fetch_sequence():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    data = {
        "region": "2:227683763-227718028",
        "coord_system_version": "GRCh38"
    }
    
    response = requests.post(
        "https://rest.ensembl.org/sequence/region/homo_sapiens",
        headers=headers,
        data=json.dumps(data)
    )
    
    if response.status_code == 200:
        result = response.json()
        return result.get('seq', '')
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

if __name__ == "__main__":
    sequence = fetch_sequence()
    if sequence:
        print("Wild type gene sequence:")
        print(sequence)
        # Save to file
        with open('wild_type_sequence.txt', 'w') as f:
            f.write(sequence)
        print("\nSequence saved to wild_type_sequence.txt") 