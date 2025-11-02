"""
Bot funksiyalarini test qilish (Telegram kerak emas)
"""

from filters import ProfanityFilter, AdFilter


def test_profanity_filter():
    """So'kinish filtrlarni test qilish"""
    print("=" * 50)
    print("🔍 SO'KINISH FILTR TESTLARI")
    print("=" * 50)
    
    filter_obj = ProfanityFilter()
    
    # Test so'zlari
    test_cases = [
        ("Salom qanday", False, "Oddiy so'z"),
        ("fuck bu", True, "Ingliz so'kinish"),
        ("ahmoq", True, "O'zbek so'kinish"),
        ("блять", True, "Rus so'kinish"),
        ("sikama", True, "O'zbek so'kinish"),
        ("qo'toq", True, "O'zbek so'kinish"),
        ("Juda yaxshi bot", False, "Oddiy matn"),
        ("suka", True, "Rus so'kinish"),
    ]
    
    passed = 0
    failed = 0
    
    for text, expected, description in test_cases:
        result = filter_obj.check(text)
        status = "✅" if result == expected else "❌"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
            print(f"\n{status} {description}")
            print(f"   Matn: '{text}'")
            print(f"   Kutilgan: {expected}, Topildi: {result}")
    
    print(f"\n📊 Natija: {passed}/{len(test_cases)} testlar o'tdi")
    if failed > 0:
        print(f"⚠️ {failed} ta xatolik topildi")
    else:
        print("🎉 Barcha testlar muvaffaqiyatli!")


def test_ad_filter():
    """Reklama filtrlarni test qilish"""
    print("\n" + "=" * 50)
    print("🔍 REKLAMA FILTR TESTLARI")
    print("=" * 50)
    
    filter_obj = AdFilter()
    
    # Test holatlar
    test_cases = [
        ("Salom qanday yuribsiz?", False, "Oddiy xabar"),
        ("t.me/channel sotib olaman pul", True, "Telegram link + reklama"),
        ("http://example.com", True, "URL"),
        ("Bu juda yaxshi guruh", False, "Oddiy xabar"),
        ("Sotaman mashina kredit", True, "Reklama so'zlari"),
        ("t.me/test", True, "Telegram link"),
        ("Oddiy gap va hikoya", False, "Oddiy matn"),
    ]
    
    passed = 0
    failed = 0
    
    for text, expected, description in test_cases:
        result = filter_obj.check(text)
        status = "✅" if result == expected else "❌"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
            print(f"\n{status} {description}")
            print(f"   Matn: '{text}'")
            print(f"   Kutilgan: {expected}, Topildi: {result}")
    
    print(f"\n📊 Natija: {passed}/{len(test_cases)} testlar o'tdi")
    if failed > 0:
        print(f"⚠️ {failed} ta xatolik topildi")
    else:
        print("🎉 Barcha testlar muvaffaqiyatli!")


def test_bad_words_count():
    """So'kinish so'zlari sonini ko'rsatish"""
    print("\n" + "=" * 50)
    print("📊 SO'KINISH SO'ZLARI STATISTIKASI")
    print("=" * 50)
    
    filter_obj = ProfanityFilter()
    total_words = len(filter_obj.bad_words)
    
    # Tildan tili bo'yicha sanash
    uzbek = sum(1 for w in filter_obj.bad_words if any(c.isascii() and not any(ord(c) > 127 for c in w) for c in w) and not any(ord(c) > 1000 for c in w))
    russian = sum(1 for w in filter_obj.bad_words if any(ord(c) > 1000 and ord(c) < 2000 for c in w))
    english = sum(1 for w in filter_obj.bad_words if all(c.isascii() for c in w) and not any(ord(c) > 127 for c in w))
    other = total_words - uzbek - russian - english
    
    print(f"🌍 Jami so'zlar: {total_words}")
    print(f"🇺🇿 O'zbek: ~{uzbek // 3} (taxminan)")
    print(f"🇷🇺 Rus: ~{russian} (taxminan)")
    print(f"🇬🇧 Ingliz: ~{english} (taxminan)")
    print(f"🔤 Boshqa variantlar: ~{other}")


if __name__ == "__main__":
    import sys
    import io
    
    # Windows uchun encoding sozlash
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    print("\n" + "=" * 50)
    print("    BOT TEST SISTEMASI")
    print("=" * 50 + "\n")
    
    try:
        test_profanity_filter()
        test_ad_filter()
        test_bad_words_count()
        
        print("\n" + "=" * 50)
        print("✅ BARCHA TESTLAR TUGADI")
        print("=" * 50)
        print("\n💡 Eslatma: Botni to'liq sinab ko'rish uchun:")
        print("   1. Telegram Web (web.telegram.org) orqali kirish")
        print("   2. Do'stingizdan botni test qilishni so'rash")
        print("   3. Botni guruhga qo'shib sinab ko'rish\n")
        
    except Exception as e:
        print(f"\n❌ Xatolik yuz berdi: {e}")
        import traceback
        traceback.print_exc()

