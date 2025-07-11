# --- Storing Information Using Variables and Data Types ---

# String: for storing text
name = "Alex Taylor"

# Integer: for storing whole numbers
age = 22

# Float: for storing numbers with decimals
desired_salary = 75000.50 

# Boolean: for storing True or False values
is_seeking_job = True

# List: for storing an ordered collection of items
skills = ["Python", "Data Analysis", "Web Basics", "miauuuu"]

# Dictionary: for storing key-value pairs of related info
contact_info = {
    "email": "alex.taylor@email.com",
    "linkedin": "linkedin.com/in/alextaylor"
}

skills.append("Git")

contact_info["github"] = "github.com/your-username"

# --- Displaying the Stored Information ---

print("--- Candidate Profile ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Actively seeking a job: {is_seeking_job}")
print(f"Desired Salary: ${desired_salary}")

# We can access list items by their index (position), which starts at 0.
print(f"Primary Skill: {skills[0]}") 

# Printing the whole list of skills
print(f"All Skills: {skills}")

# We can access dictionary items by their key.
print(f"Email: {contact_info['email']}")
print(f"LinkedIn: {contact_info['linkedin']}")
print(f"GitHub: {contact_info['github']}")
print("-----------------------")