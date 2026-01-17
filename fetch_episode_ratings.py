import requests
import pandas as pd
import time
import sys

def get_tvmaze_show_id(imdb_id):
    url = f"https://api.tvmaze.com/lookup/shows?imdb={imdb_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('id'), response.json().get('name')
    return None, None

def get_episodes(tvmaze_id):
    url = f"https://api.tvmaze.com/shows/{tvmaze_id}/episodes"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

def fetch_all_ratings(input_csv, output_csv):
    with open(input_csv, 'r') as f:
        content = f.read().strip()
        imdb_ids = [id.strip() for id in content.split(',')]
    
    print(f"Found {len(imdb_ids)} shows")
    
    all_episodes = []
    
    for imdb_id in imdb_ids:
        print(f"\n Fetching {imdb_id}")
        
        tvmaze_id, show_name = get_tvmaze_show_id(imdb_id)
        if not tvmaze_id:
            print(f"-Could not find show for {imdb_id}")
            continue
        
        print(f"-Found: {show_name} (TVMaze ID: {tvmaze_id})")
        
        episodes = get_episodes(tvmaze_id)
        print(f"-Fetched {len(episodes)} episodes")
        
        for ep in episodes:
            all_episodes.append({
                'imdb_id': imdb_id,
                'show_name': show_name,
                'season': ep.get('season'),
                'episode': ep.get('number'),
                'episode_name': ep.get('name'),
                'airdate': ep.get('airdate'),
                'rating': ep.get('rating', {}).get('average'),
                'runtime': ep.get('runtime')
            })
        
        time.sleep(0.5)
    
    df = pd.DataFrame(all_episodes)
    df.to_csv(output_csv, index=False)
    
    return df

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "imdb_ids.csv"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "episode_ratings.csv"
    
    fetch_all_ratings(input_file, output_file)
