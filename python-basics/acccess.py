#Sample Learning assignment using if and else
user_name=input("Enter your name: ").lower()

if user_name == "tanuja":
    print(f"Welcome {user_name}! You have full access to the system.")
else:
  user_role=input("Enter your role (admin/editor/viewer): ").lower()
  security_level=input("Enter your security level (high/medium/low): ").lower()

  print(f"Welcome {user_name}! Checking your access level... ")

  if user_role == "admin":
      print(f"Welcome {user_name}! You have admin access to the system.")
  elif user_role == "editor" and security_level in ["low", "medium"]:
      print(f"Welcome {user_name}! You have editor access to the system")
  elif user_role == "editor" and security_level == "high":
      print(f"Welcome {user_name}! You don't have access to the system.")
  elif user_role == "viewer" and security_level == "low":
      print(f"Welcome {user_name}! You have viewer access to the system.")
  else:
      print(f"Welcome {user_name}! You don't have access to the system.") 