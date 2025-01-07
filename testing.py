import json
filename = "order_details.json"
def append_dict_to_json(data, filename):
    with open(filename, 'r') as file:
        existing_data = list(json.load(file))

    # Assuming the existing data is a list, you can append the new dictionary to it
    existing_data.extend(data)

    with open(filename, 'w') as file:
        json.dump(existing_data, file)
append_dict_to_json([1,2,3,4],filename)