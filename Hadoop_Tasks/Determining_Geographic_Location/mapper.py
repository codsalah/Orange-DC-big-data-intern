import sys

def mapper():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            country_code, latitude, longitude = line.split(',')
            longitude = float(longitude)
            latitude = float(latitude)

            # Determine the coord
            if latitude >= 0:
                lat_class = "North"
            else:
                lat_class = "South"

            if longitude >= 0:
                lon_class = "East"
            else:
                lon_class = "West"

            # Output key-value pairs: (country_code, classification) as key and coordinates as value
            print(f"{country_code}_{lat_class}_{lon_class}\t{longitude},{latitude}")

        except ValueError:
            continue

if __name__ == "__main__":
    mapper()
