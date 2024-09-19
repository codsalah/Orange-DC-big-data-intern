# Task Statement

Determining Geographic Location (North, South, East, West) using Hadoop and MapReduce

## Overview

This guide provides instructions for testing Hadoop mapper and reducer scripts locally using sample data.

### Mapper

**`mapper.py`**: Reads geographic coordinates, classifies them into regions (North/South, East/West), and outputs key-value pairs with the classification as the key and coordinates as the value.

### Reducer

**`reducer.py`**: Aggregates coordinates by their classification keys and outputs the collected data for each key.

### Input Data
```
country_code,latitude,longitude,country,usa_state_code,usa_state_latitude,usa_state_longitude,usa_state
AD,42.546245,1.601554,Andorra,AK,63.588753,-154.493062,Alaska
AE,23.424076,53.847818,United Arab Emirates,AL,32.318231,-86.902298,Alabama
AF,33.93911,67.709953,Afghanistan,AR,34.969704,-92.373123,Arkansas
```

### Preprocessed Data
```
country_code,latitude,longitude
AD,42.546245,1.601554
AE,23.424076,53.847818
AF,33.93911,67.709953
```

### Output Data
```
AD_North_East	1.601554,42.546245
AE_North_East	53.847818,23.424076
AF_North_East	67.709953,33.93911
```


# Directory Structure

## Overview

This guide provides instructions for testing Hadoop mapper and reducer scripts locally using sample data.

## Directory Structure

- **Input Data**: `preprocessed_data/processed_data.csv`
- **Mapper Script**: `mapper.py`
- **Reducer Script**: `reducer.py`
- **Output Directory**:
  - **Intermediate File**: `Output/intermediate.txt`
  - **Final Output File**: `Output/output.txt`

