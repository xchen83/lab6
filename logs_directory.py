import os

# Define the directory name
directory_name = "logs"

# Check if the directory already exists
if not os.path.exists(directory_name):
    # Create the "logs" directory
    os.mkdir(directory_name)
    print(f"The '{directory_name}' directory has been created.")
else:
    print(f"The '{directory_name}' directory already exists.")