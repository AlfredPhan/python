#Program No.1 Number formatting using strings concept
print("Unformatted")
print(f"{123.456789}")
print()
print("Formatted as decimals")
print(f"{123.456789:8.2f}") # Làm tròn số thập phân
print(f"{123:8.2f}")
print(f"{123456.789:8.2f}")
print()
print("Formatted in scientific natation")
print(f"{123.456789:8.2e}")
print(f"{123:8.2e}")
print(f"{123456.789:8.2e}")
print(f"{0.00123456789:8.2e}")
print()
print("Formatted as currency")
print(f"£{0.123456789}")