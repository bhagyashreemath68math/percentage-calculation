import sys

# Check for command-line arguments
if len(sys.argv) == 3:
    script_name = sys.argv[0]
    classes_held = int(sys.argv[1])
    classes_attended = int(sys.argv[2])
else:
    print("Usage: python attendance.py <classes_held> <classes_attended>")
    sys.exit(1)

# Calculate percentage
percentage = (classes_attended / classes_held) * 100

# Display details
print("Script Name          :", script_name)
print("Classes Held         :", classes_held)
print("Classes Attended     :", classes_attended)
print("Attendance Percentage:", percentage)

# Eligibility check
if percentage >= 75:
    print("Status               : Eligible")
else:
    print("Status               : Not Eligible")
    print("Note                 : Minimum 75% attendance required")
