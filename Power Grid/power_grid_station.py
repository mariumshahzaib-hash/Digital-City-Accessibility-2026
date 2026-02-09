# ========================================
# LEVEL 3: ENGINEER - Power Grid Light Sensor
# Mission: Add Error Handling to Prevent Crashes
# Security Key: CRYSTAL_CLEAR
# ========================================

print("💡 POWER GRID LIGHT SENSOR STARTING...")
print("Checking light levels with error protection...")

# This code has error handling to stop "saboteurs"
try:
    # Get the light level from the sensor
    light_level = int(input("Enter light level (0-100): "))
    
    # Check if the input is valid
    if light_level < 0 or light_level > 100:
        print("⚠️ Error: Light level must be between 0 and 100")
    elif light_level < 30:
        print("🌙 LOW LIGHT - Turning street lights ON")
        print("🔑 Security Key: CRYSTAL_CLEAR")
    elif light_level < 70:
        print("☁️ MEDIUM LIGHT - Lights at 50% brightness")
    else:
        print("☀️ BRIGHT LIGHT - Street lights OFF")
    
    print("✅ Power Grid System Complete!")

except ValueError:
    print("🛡️ ERROR BLOCKED! Invalid input detected.")
    print("The system is protected from crashes!")
    print("Please enter a NUMBER between 0 and 100")

except Exception as e:
    print("🛡️ UNKNOWN ERROR BLOCKED!")
    print("System protected. Error type: " + str(e))
