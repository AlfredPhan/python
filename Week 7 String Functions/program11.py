#Program No.11 Response String Chaining functions
response = input("Are you generally happy with Python class? ")

#with chaining
if response.strip().lower().startswith("yes"):
    print(f"Good! Your response is '{response}'")

#without chaining
response = response.strip()
response = response.lower()
if response.startswith("yes"):
    print(f"Good! Your response is '{response}'")
else:
    print(f"Bad! Your response is '{response}'")

print()
