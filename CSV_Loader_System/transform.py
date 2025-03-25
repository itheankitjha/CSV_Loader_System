def transform_data(data):
    transformed_data = []
    for row in data:
        # Example transformation: capitalize the name and remove records for people under 25
        if int(row['age']) >= 25:
            row['name'] = row['name'].capitalize()
            transformed_data.append(row)
    return transformed_data
