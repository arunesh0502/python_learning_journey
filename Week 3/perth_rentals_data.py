import pandas as pd
import numpy as np

# Creating a Realistic Dataset for Perth Rentals (Simulating Real Listings)
np.random.seed(42)  # For reproducible random numbers

suburbs = ["Nedlands", "Subiaco", "Mount Lawley", "Crawley", "Shenton Park", "Fremantle", "Victoria Park", "Leederville", "Claremont", "Cottesloe"]*15
n_listings = len(suburbs)

# Generating Realistic Data
data = {
    'listing_id': range(1001, 1001 + n_listings),
    'suburb': suburbs,
    'property_type': np.random.choice(['Shared Room', 'Studio Room', '1 BR', '2 BR'], n_listings),
    'rent_weekly': np.random.randint(200, 1000, n_listings),   
    'bonds': np.random.randint(800, 4000, n_listings),
    'bedrooms': np.random.choice([1, 2, 3, 4], n_listings),
    'bathrooms': np.random.choice([1, 2], n_listings),
    'furnished': np.random.choice(['Yes', 'No', 'Semi'], n_listings),
    'parking': np.random.choice(['Yes', 'No'], n_listings),
    'pets_allowed': np.random.choice(['Yes', 'No'], n_listings),
    'available_from': pd.date_range('2026-07-01', periods=n_listings, freq='W'),
    'distance_to_uwa_km': np.random.uniform(0.5, 15, n_listings).round(1),
    'safety_rating': np.random.randint(1, 10, n_listings),
    'description_length': np.random.randint(50, 300, n_listings) 
}
df = pd.DataFrame(data)

# Making some realistic price adjustments based on property type
for idx, row in df.iterrows():
    if row['property_type'] == 'Shared Room':
        df.loc[idx, 'rent_weekly'] = np.random.randint(200, 400)
    elif row['property_type'] == 'Studio Room':
        df.loc[idx, 'rent_weekly'] = np.random.randint(400, 700)
    elif row['property_type'] == '1 BR':
        df.loc[idx, 'rent_weekly'] = np.random.randint(500, 800)
    else:  # 2 BR
        df.loc[idx, 'rent_weekly'] = np.random.randint(750, 1000)
    # Bond is typically 4 weeks rent
    df.loc[idx, 'bonds'] = df.loc[idx, 'rent_weekly'] * 4

# Adjusting the bedrooms and bathrooms based on property type
for idx, row in df.iterrows():
    if row['property_type'] == 'Shared Room':
        df.loc[idx, 'bedrooms'] = np.random.choice([2, 3, 4])
        df.loc[idx, 'bathrooms'] = np.random.choice([1, 2])
    elif row['property_type'] == 'Studio Room':
        df.loc[idx, 'bedrooms'] = 1
        df.loc[idx, 'bathrooms'] = 1
    elif row['property_type'] == '1 BR':
        df.loc[idx, 'bedrooms'] = 1
        df.loc[idx, 'bathrooms'] = 1
    else:  # 2 BR
        df.loc[idx, 'bedrooms'] = 2
        df.loc[idx, 'bathrooms'] = np.random.choice([1, 2])

# Adding some missing values to simulate real-world data imperfections
missing_indices = np.random.choice(df.index, 15, replace=False)
df.loc[missing_indices, 'pets_allowed'] = np.nan

missing_indices1 = np.random.choice(df.index, 10, replace=False)
df.loc[missing_indices1, 'parking'] = np.nan

# Save to Dataset
df.to_csv('perth_rentals.csv', index=False)

print("Perth rental dataset created")
print(f"{len(df)} listings generated")
print(f"Saved as: perth_rentals.csv")
print("\nFirst few rows:")
print(df.head(10))
print("\nDataset info:")
print(df.info())