name = input("What's your name? ").strip().title()

# Split the name into first name and last name
# I can assign multiple variables at a time.
first, last = name.split(" ")

print (f"Hello, {first}.") #format string = f-string
