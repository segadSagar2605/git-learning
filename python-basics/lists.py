#creating a small list of features
backlog = ["Login", "Signup", "Profile", "Settings", "Logout"]
print(f"current Backlog: {backlog}")

top_priority_feature = backlog[0]
print(f"Top priority feature: {top_priority_feature}")

# Adding a new feature to the backlog
new_feature = "Dashboard"
backlog.append(new_feature)
print(f"Updated Backlog: {backlog}")

# Removing a feature from the backlog
backlog.remove("Settings")
print(f"Updated Backlog after removing 'Settings': {backlog}")


for feature in backlog:
    print(f"Processing feature: {feature}")

print(f"Total number of features in the backlog: {len(backlog)}")