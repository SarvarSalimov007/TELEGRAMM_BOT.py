# 🤖 EXA_SHUT_UP_BOT

Zamonaviy Telegram moderatsiya boti - so'kinish so'zlarini aniqlash va foydalanuvchilarni avtomatik mute qilish.

## ✨ Xususiyatlar

- 🔇 **So'kinish aniqlash**: O'zbek, rus va ingliz tillaridagi so'kinish so'zlarini aniqlaydi
- ⏱️ **Progressiv jazo**: So'kinishlar soniga qarab mute muddati oshadi
  - 1-chi ogohlantirish: 5 daqiqa
  - 2-chi ogohlantirish: 15 daqiqa
  - 3-chi ogohlantirish: 1 soat
  - 4+ ogohlantirish: 24 soat
- 🚫 **Reklama bloklash**: Reklama va spam xabarlarni avtomatik bloklaydi
- 🎨 **Zamonaviy dizayn**: Chiroyli va tushunarli xabarlar
- ✅ **Xatolarsiz ishlash**: To'liq xato boshqaruvi

## 📋 Talablar

- Python 3.8+
- Telegram bot token (@BotFather dan oling)
- Bot admin huquqlari (guruhda mute qilish uchun)

## 🚀 O'rnatish

1. **Repositoryni klonlang:**
```bash
git clone <repository_url>
cd telegram_bot
```

2. **Virtual environment yarating:**
```bash
python -m venv venv
# Windows uchun:
venv\Scripts\activate
# Linux/Mac uchun:
source venv/bin/activate
```

3. **Kutubxonalarni o'rnating:**
```bash
pip install -r requirements.txt
```

4. **.env faylini yarating:**
```bash
copy .env.example .env
```

5. **.env faylini tahrirlang va bot tokenini kiriting:**
```
BOT_TOKEN=your_bot_token_here
```

## 📖 Ishlatish

1. **Botni ishga tushiring:**
```bash
python bot.py
```

2. **Telegramda botni guruhga qo'shing va admin qiling**

3. **Bot avtomatik ishlaydi:**
   - So'kinish so'zlari aniqlanadi va foydalanuvchi mute qilinadi
   - Reklama xabarlar o'chiriladi

## 🎮 Buyruqlar

- `/start` - Botni ishga tushirish
- `/help` - Yordam olish
- `/stats` - Statistika ko'rish (admin uchun)
- `/reset_user [user_id]` - Foydalanuvchi ma'lumotlarini tozalash (admin uchun)

## ⚙️ Sozlash

Bot sozlamalarini `config.py` va `filters.py` fayllarida o'zgartirishingiz mumkin:

- **So'kinish so'zlari**: `filters.py` → `ProfanityFilter.bad_words`
- **Reklama filtrlari**: `filters.py` → `AdFilter.ad_patterns`

## 🔒 Huquqlar

Bot to'g'ri ishlashi uchun quyidagi huquqlar kerak:
- Xabarlarni o'chirish
- Foydalanuvchilarni mute qilish
- Chat a'zolarini ko'rish

## 📝 Izoh

Bu bot faqat o'quv maqsadida yaratilgan. Haqiqiy loyihada qo'shimcha xavfsizlik va optimizatsiya talab qilinadi.

## 📄 Lisensiya

MIT

## 👨‍💻 Muallif

EXA_SHUT_UP_BOT Development Team

