import pandas as pd

# Step 1: Create data using { }
perth_suburbs = {
    "suburb": ["Nedlands", "Subiaco", "Mount Lawley", "Crawley", "Shenton Park"],
    "rent_shared": [700, 650, 550, 850, 600],
    "rent_studio": [1400, 1300, 1100, 1600, 1200],
    "distance_km": [1.5, 6, 10, 0, 3],
    "safety_rating": [9, 8, 7, 9, 8]
}

# Step 2: Convert to DataFrame using ( )
df = pd.DataFrame(perth_suburbs)

print("Full DataFrame:")
print(df)

# To get just the suburb names (single column, Series), use df[ ] 
suburb_names = df["suburb"]
print("\nSuburb names:")
print(suburb_names)

# To get suburb and rent_shared (multiple columns, DataFrame), use df[ [ ] ]
budget_info = df[["suburb", "rent_shared"]]
print("\nBudget info:")
print(budget_info)

# To filter suburbs where rent_shared < 700, use df[df[] < ___]
cheap_suburbs = df[df["rent_shared"] < 700]
print("\nCheap suburbs:")
print(cheap_suburbs)

# To find suburbs that are both cheap (<700) AND safe (>7), use df[(df[] < ___) & (df[] > ___)]
cheap_safe = df[(df["rent_shared"] < 700) & (df["safety_rating"] > 7)]
print("\nCheap AND safe:")
print(cheap_safe)

# To get average rent for shared rooms, use df[].mean()
avg_rent = df["rent_shared"].mean()
print(f"\nAverage shared rent: ${avg_rent:.0f}")

# To sort by rent (cheapest first), use df.sort_values()
sorted_df = df.sort_values("rent_shared")
print("\nSorted by rent:")
print(sorted_df)

# To add a new column calculating rent difference (studio - shared), use df[] = df[] - df[]
df["rent_difference"] = df["rent_studio"] - df["rent_shared"]
print("\nAdded rent difference column:")
print(df[["suburb", "rent_shared", "rent_studio", "rent_difference"]])

print("\n Bracket Summary")
print("{ } for creating, ( ) for doing, [ ] for getting")