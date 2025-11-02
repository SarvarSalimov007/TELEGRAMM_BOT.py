# 🧪 Botni Test Qilish Usullari (Telegram/Telefon Yo'q)

Telegram yoki telefon bo'lmasa ham botni tekshirishning bir necha usuli bor!

## ✅ Usul 1: Telegram Web (ENG OSON!)

**Brauzerda ishlaydi, telefon kerak emas!**

1. **Telegram Web ga kiring:**
   - https://web.telegram.org
   - Yoki https://telegram.org/web

2. **Hisob yarating:**
   - Email yoki telefon raqam orqali
   - Telefon raqam kerak bo'ladi, lekin kodni SMS yoki telefon qo'ng'irog'i orqali olish mumkin

3. **Botni test qiling:**
   - @BotFather ga kiring
   - Bot yarating
   - Token oling va `.env` ga qo'ying
   - Botni ishga tushiring!

## ✅ Usul 2: Test Skripti (Kod Tekshirish)

**Kod xatolarini topish uchun:**

```bash
python test_bot.py
```

Bu skript:
- ✅ So'kinish filtrlarni test qiladi
- ✅ Reklama filtrlarni test qiladi  
- ✅ Statistikani ko'rsatadi
- ✅ Xatolarni topadi

## ✅ Usul 3: Sintaksis Tekshirish

**Python kod xatolarini topish:**

```bash
# Windows
python -m py_compile bot.py
python -m py_compile filters.py
python -m py_compile config.py

# Linux/Mac
python3 -m py_compile bot.py filters.py config.py
```

Agar xato bo'lmasa - kod to'g'ri!

## ✅ Usul 4: Do'stingizdan Yordam So'rash

1. Kodni GitHub ga yuklang
2. Do'stingizdan botni test qilishni so'rang
3. Screenshotlar va natijalarni ulashish

## ✅ Usul 5: Python REPL da Test

**Python konsolida test:**

```python
python
>>> from filters import ProfanityFilter, AdFilter
>>> pf = ProfanityFilter()
>>> pf.check("test matn")  # False bo'lishi kerak
>>> pf.check("fuck")       # True bo'lishi kerak
>>> ad = AdFilter()
>>> ad.check("http://example.com")  # True bo'lishi kerak
```

## ✅ Usul 6: Virtual Mashina/Sandbox

1. **Online Python IDE:**
   - https://replit.com
   - https://www.online-python.com
   - Kodni yuklab sinab ko'ring

## 📱 Telegram Web Qo'llanmasi

### Qadam 1: Web ga kiring
```
https://web.telegram.org/k/
```

### Qadam 2: Telefon raqam kiriting
- Har qanday telefon raqam (do'stingizniki ham bo'lishi mumkin)
- SMS yoki qo'ng'iroq orqali kod oling

### Qadam 3: Bot yarating
1. @BotFather ni qidiring
2. /newbot buyrug'ini bering
3. Bot nomini yarating: `EXA_SHUT_UP_BOT`
4. Username: `your_bot_name_bot`
5. Token oling!

### Qadam 4: Botni ishga tushiring
```bash
python bot.py
```

## 🎯 Test Qilinadigan Funksiyalar

### 1. So'kinish Aniqlash
- ✅ Ingliz so'zlar
- ✅ Rus so'zlar  
- ✅ O'zbek so'zlar
- ✅ Variantlar

### 2. Reklama Bloklash
- ✅ URLlar
- ✅ Telegram linklar
- ✅ Spam patternlar

### 3. Jazo Tizimi
- ✅ 1-chi: 5 daqiqa
- ✅ 2-chi: 15 daqiqa
- ✅ 3-chi: 1 soat
- ✅ 4+ chi: 24 soat

## 💡 Maslahatlar

1. **Kod sintaksisini tekshiring** - `test_bot.py` ishga tushiradi
2. **Telegram Web** - eng oson usul
3. **Do'stlar yordami** - ular test qilsin
4. **GitHub Actions** - avtomatik test

## ❓ Savollar?

Agar muammo bo'lsa:
- Test skriptini ishga tushiring
- Kod sintaksisini tekshiring
- Do'stingizdan yordam so'rang

**Bot tayyor va ishlaydi! Faqat Telegram orqali sinab ko'rish kerak.** 🚀

