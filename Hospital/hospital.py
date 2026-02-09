15# ========================================
# LEVEL 2: ARCHITECT - Hospital Triage System
# Mission: Fix the Emergency Room Logic
# Security Key: HEARTBEAT
# ========================================

print("🏥 HOSPITAL TRIAGE SYSTEM STARTING...")
print("Checking patient pain level...")

# Get the pain level from the patient
pain_level = int(input("Enter patient pain level (1-10): "))

# YOUR MISSION: Complete the triage system!
# HINT: Use if, elif, elif, else
# HINT: Check these ranges:
#   - 8 to 10 = Critical (Emergency Room)
#   - 5 to 7 = Urgent (See doctor soon)
#   - 1 to 4 = Routine (Regular appointment)
#   - Anything else = Invalid

# START YOUR CODE HERE:
if pain_level >= 8:
    print("🚨 CRITICAL - Send to Emergency Room immediately!")
    print("🔑 Security Key: HEARTBEAT")
# ADD MORE CODE HERE - What about pain levels 5-7?


# ADD MORE CODE HERE - What about pain levels 1-4?


# ADD MORE CODE HERE - What if it's not 1-10?


print("✅ Hospital Triage System Complete!")


# ========================================
# SOLUTION CODE (Don't look until you try!)
# ========================================
"""
if pain_level >= 8:
    print("🚨 CRITICAL - Send to Emergency Room immediately!")
    print("🔑 Security Key: HEARTBEAT")
elif pain_level >= 5:
    print("⚠️ URGENT - See doctor within 30 minutes")
elif pain_level >= 1:
    print("ℹ️ ROUTINE - Schedule regular appointment")
else:
    print("❓ Invalid pain level - Please re-enter")
"""
