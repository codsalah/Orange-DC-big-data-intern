import sys
from collections import defaultdict

def reducer():
    locations = defaultdict(list)

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            country_class, coords = line.split('\t')
            longitude, latitude = coords.split(',')

            # Collect coordinates for each (country_code, classification)
            locations[country_class].append((longitude, latitude))
        except ValueError:
            continue

    # Output aggregated results
    for country_class, coords_list in locations.items():
        for longitude, latitude in coords_list:
            print(f"{country_class}\t{longitude},{latitude}")

if __name__ == "__main__":
    reducer()
