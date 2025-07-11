# --- Our Data ---

# Here is our list of skills.
skills = ["Python", "Data Analysis", "Java", "SQL", "Web Basics", "C++", "Git"]

# Let's say these are the skills you want to highlight.
confident_skills = ["Python", "SQL", "Git"]


# --- The Logic: Loop and Conditionals ---

print("--- Analyzing Skills ---")

# This is a 'for' loop. It will go through each item in the 'skills' list,
# one by one, and temporarily call that item 'skill'.
for skill in skills:
    
    # This is our conditional check.
    # 'if' the current 'skill' is also in our 'confident_skills' list...
    if skill in confident_skills:
        # ...then print this special message.
        print(f"- {skill}  (⭐ Confident)")
    else:
        # ...'else' (otherwise), just print the skill name normally.
        print(f"- {skill}")

print("------------------------")