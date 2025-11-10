import requests

# API endpoint
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    users = response.json()

    print("===== All Users =====")
    for index, user in enumerate(users, start=1):
        print(f"User {index}:")
        print(f"  Name: {user['name']}")
        print(f"  Username: {user['username']}")
        print(f"  Email: {user['email']}")
        print(f"  City: {user['address']['city']}")
        print("------------------------")

    print("\n===== Users Whose City Starts With 'S' =====")
    for index, user in enumerate(users, start=1):
        city = user['address']['city']
        if city.startswith("S"):
            print(f"User {index}:")
            print(f"  Name: {user['name']}")
            print(f"  Username: {user['username']}")
            print(f"  Email: {user['email']}")
            print(f"  City: {city}")
            print("------------------------")

else:
    print("Failed to fetch data. Status Code:", response.status_code)
