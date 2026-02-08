servers=["server1","server2","server3 ","server4" ]
print(servers)
print(f"Total number of servers: {len(servers)}")

user_input=input("Enter the name of the server you want to add: ").lower()

servers.append(user_input)

user_input=input("Enter the name of the server you want to remove: ").lower()
if user_input in servers:
  servers.remove(user_input) 

print(servers)
print(f"Total number of servers: {len(servers)}")