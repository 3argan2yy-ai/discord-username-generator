import random
import string

def generate_discord_username(count=1):
    """
    توليد يوزرنيمات ديسكورد رباعية عشوائية
    
    المعاملات:
        count (int): عدد اليوزرنيمات المراد توليدها (افتراضي: 1)
    
    الإرجاع:
        list: قائمة بالحروف والأرقام العشوائية
    """
    usernames = []
    
    # الأحرف المسموحة (أحرف صغيرة وأرقام)
    characters = string.ascii_lowercase + string.digits
    
    for _ in range(count):
        # توليد يوزرنيم رباعي عشوائي
        username = ''.join(random.choice(characters) for _ in range(4))
        usernames.append(username)
    
    return usernames


def generate_unique_usernames(count=1):
    """
    توليد يوزرنيمات فريدة (بدون تكرار)
    
    المعاملات:
        count (int): عدد اليوزرنيمات المراد توليدها
    
    الإرجاع:
        list: قائمة بالحروف الفريدة
    """
    characters = string.ascii_lowercase + string.digits
    all_combinations = set()
    
    # إذا كان العدد أكبر من الحد الأقصى المتاح (36^4 = 1,679,616)
    max_possible = 36 ** 4
    if count > max_possible:
        print(f"تحذير: العدد المطلوب ({count}) أكبر من الحد الأقصى المتاح ({max_possible})")
        count = max_possible
    
    while len(all_combinations) < count:
        username = ''.join(random.choice(characters) for _ in range(4))
        all_combinations.add(username)
    
    return list(all_combinations)


if __name__ == "__main__":
    # مثال على الاستخدام
    print("=" * 50)
    print("مولد يوزرنيمات ديسكورد رباعية")
    print("=" * 50)
    
    # توليد 10 يوزرنيمات عشوائية
    print("\n✓ 10 يوزرنيمات عشوائية:")
    usernames = generate_discord_username(10)
    for i, username in enumerate(usernames, 1):
        print(f"  {i}. {username}")
    
    # توليد 5 يوزرنيمات فريدة
    print("\n✓ 5 يوزرنيمات فريدة (بدون تكرار):")
    unique_usernames = generate_unique_usernames(5)
    for i, username in enumerate(unique_usernames, 1):
        print(f"  {i}. {username}")
    
    print("\n" + "=" * 50)
