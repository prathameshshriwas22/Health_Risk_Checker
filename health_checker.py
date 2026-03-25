print("🏥 Health Risk Checker")

age = int(input("Enter your age: "))
bp = int(input("Enter your blood pressure: "))
heart_rate = int(input("Enter your heart rate: "))

if age > 50 and bp > 140:
    print("⚠️ High Health Risk. Please consult a doctor.")

elif heart_rate > 100:
    print("⚠️ Heart rate is high. Monitor your health.")

else:
    print("✅ Your health parameters look normal.")