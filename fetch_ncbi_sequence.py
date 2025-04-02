import requests
import time

def fetch_sequence():
    # NCBI E-utilities API endpoint
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    
    # Parameters for the request
    params = {
        'db': 'nuccore',
        'id': 'NC_000002.12',  # Human chromosome 2 reference sequence
        'seq_start': '227683763',
        'seq_stop': '227718028',
        'strand': '1',
        'rettype': 'fasta',
        'retmode': 'text'
    }
    
    # Add delay to respect NCBI's rate limits
    time.sleep(1)
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        # Extract sequence from FASTA format
        lines = response.text.split('\n')
        sequence = ''.join(line for line in lines if not line.startswith('>'))
        
        # Save to file
        with open('wild_type_sequence.txt', 'w') as f:
            f.write(sequence)
        
        print("Wild type gene sequence:")
        print(sequence)
        print("\nSequence saved to wild_type_sequence.txt")
        return sequence
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sequence: {e}")
        return None

if __name__ == "__main__":
    sequence = fetch_sequence() 