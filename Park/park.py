# ========================================
# LEVEL 1: SCAVENGER - Park Ramp System
# Mission: Fix the Water Level/Weight Sensor
# Security Key: RAMP2025
# ========================================

print("🏞️ PARK RAMP SYSTEM STARTING...")
print("Checking weight sensor...")

# Get the weight from the sensor
weight = int(input("Enter weight detected (in kg): "))

# YOUR MISSION: Fix the code below!
# HINT: Use if, elif, and else
# HINT: Check if weight is less than 10, or 10 or more

if weight < 10:
    print("⏸️ Standby - No action needed")
# ADD YOUR CODE HERE - What happens when weight is 10 or more?


print("✅ Park Ramp System Complete!")


# ========================================
# SOLUTION CODE (Don't look until you try!)
# ========================================
"""
if weight < 10:
    print("⏸️ Standby - No action needed")
elif weight >= 10:
    print("♿ Deploying Ramp... Access Granted!")
    print("🔑 Security Key: RAMP2025")
else:
    print("⚠️ Unknown weight - Please check sensor")
"""
