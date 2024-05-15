from collections import Counter

def calculate_mode(data):
    # นับความถี่ของข้อมูลแต่ละตัว
    frequencies = Counter(data)
    
    # หาค่าที่มีความถี่สูงสุด
    max_frequency = max(frequencies.values())
    
    # สร้างลิสต์เพื่อเก็บค่าที่มีความถี่เท่ากับค่าสูงสุด
    modes = [value for value, frequency in frequencies.items() if frequency == max_frequency]
    
    return modes

# ตัวอย่างการใช้งาน
data = [12, 15, 22, 10, 16, 9, 15, 27, 8,11,20]
modes = calculate_mode(data)
print("Mode(s):", modes)
