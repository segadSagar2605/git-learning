#input () always returns a string, so we need to convert it to an integer
feature_name=input("Enter the name of the feature you want to use: ")
estimated_days=input("Enter the estimated number of days to complete the feature: ")

# Convert the estimated days to an integer
estimated_days = int(estimated_days)

print(f"--------------Report for feature: {feature_name}--------------")

if estimated_days > 30:
  print(f"Too long to complete the feature in this sprint")
else:
  print(f"Added to the sprint")
