import json
#Sample learning script for dictionaries
products = {
    "name": "Core Coontent Management System",
    "version": 26.1,
    "active": True,
    "modules": ["login", "dashboard", "analytics"],
}

print(products["name"])  # Output: Core Coontent Management System
print(products["version"])  # Output: 26.1

#modify a value
products["version"] = 26.2
print(f"Updated version: {products['version']}")  # Output: Updated version: 26.2

#add a new key-value pair
products["release_date"] = "2024-07-01"
print(f"Release Date: {products['release_date']}")  # Output: Release Date: 2024-07-01


#check if a key exists
#safe access using get method
print(products.get("modules"))  # Output: ['login', 'dashboard', 'analytics']
price = products.get("price", "Price not available")
print(price)  # Output: Price not available

#user updated logic to check if it already exists
new_modules = input("Enter new modules to add (comma separated): ")
new_modules_list = [module.strip() for module in new_modules.split(",")]
#check if new modules already exist in the products dictionary
if "modules" in products:
    existing_modules = set(products["modules"])
    for module in new_modules_list:
        if module not in existing_modules:
            products["modules"].append(module)
            print(f"Added module: {module}")
        else:
            print(f"Module '{module}' already exists.")


#now access the updated modules list
print(f"Updated modules: {products['modules']}")


#now simulating an API response with a dictionary
print("\n------- JSON output (API Payload):---") 
json_string=json.dumps(products, indent=4)

print(json_string)