"""
EXA_SHUT_UP_BOT - Telegram moderatsiya boti
Zamonaviy dizayn va xatolarsiz ishlash
"""

import logging
from datetime import datetime, timedelta
from typing import Dict

from telegram import Update, ChatPermissions
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from config import Config
from filters import ProfanityFilter, AdFilter

# Logging sozlash
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Foydalanuvchi jazo ma'lumotlari
user_warnings: Dict[int, Dict] = {}


class ShutUpBot:
    """Asosiy bot sinfi"""
    
    def __init__(self):
        self.config = Config()
        self.profanity_filter = ProfanityFilter()
        self.ad_filter = AdFilter()
        
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Start buyrug'i"""
        welcome_message = (
            "╔════════════════════════════╗\n"
            "║  ✨ <b>EXA_SHUT_UP_BOT</b> ✨  ║\n"
            "╚════════════════════════════╝\n\n"
            
            "🎯 <b>NEON MODERATION SYSTEM</b> 🎯\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            
            "⚡ <b>Bot Faollashtirildi!</b> ⚡\n\n"
            
            "🎨 <b>⚡ Premium Funksiyalar ⚡</b>\n"
            "┌────────────────────────────┐\n"
            "│ 🔇 So'kinish aniqlash     │\n"
            "│ 🚫 Reklama/spam bloklash  │\n"
            "│ ⚡ Auto-mute tizimi        │\n"
            "│ 🎯 Progressiv jazo        │\n"
            "└────────────────────────────┘\n\n"
            
            "💫 Bot <b>AVTOMATIK</b> ishlaydi!\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )
        await update.message.reply_text(
            welcome_message,
            parse_mode='HTML'
        )
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Help buyrug'i"""
        help_text = (
            "╔════════════════════════════╗\n"
            "║   📖 <b>YORDAM MARKAZI</b> 📖   ║\n"
            "╚════════════════════════════╝\n\n"
            
            "🎮 <b>⚡ Buyruqlar Ro'yxati ⚡</b>\n"
            "┌─────────────────────────────┐\n"
            "│ /start  → Botni ishga tushirish\n"
            "│ /help   → Yordam olish\n"
            "│ /stats  → Statistikani ko'rish\n"
            "│ /reset_user [id] → Ma'lumotlarni tozalash\n"
            "└─────────────────────────────┘\n\n"
            
            "⚙️ <b>🔧 Qanday Ishlaydi 🔧</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "┃ 🔍 Bot so'kinish so'zlarini\n"
            "┃    avtomatik aniqlaydi\n\n"
            
            "🎯 <b>Jazo Tizimi:</b>\n"
            "┌─────────────────────────────┐\n"
            "│ ⚠️  1-chi: 5 daqiqa mute\n"
            "│ ⚠️⚠️  2-chi: 15 daqiqa mute\n"
            "│ ⚠️⚠️⚠️  3-chi: 1 soat mute\n"
            "│ ⚠️⚠️⚠️⚠️  4+ chi: 24 soat mute\n"
            "└─────────────────────────────┘\n\n"
            
            "🚫 Reklama va spam ham\n"
            "   avtomatik bloklanadi!"
        )
        await update.message.reply_text(
            help_text,
            parse_mode='HTML'
        )
    
    async def stats_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Statistika ko'rsatish"""
        if not await self._check_admin(update, context):
            return
        
        total_warnings = sum(len(data.get('warnings', [])) for data in user_warnings.values())
        active_users = len([u for u in user_warnings.values() if u.get('warnings', [])])
        
        stats_text = (
            "╔════════════════════════════╗\n"
            "║  📊 <b>STATISTIKA MARKAZI</b> 📊  ║\n"
            "╚════════════════════════════╝\n\n"
            
            "━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"⚠️ <b>Jami ogohlantirishlar:</b>\n"
            f"   <code>{total_warnings}</code>\n\n"
            
            f"👥 <b>Jazo olganlar:</b>\n"
            f"   <code>{active_users}</code>\n\n"
            
            f"📝 <b>Kuzatilgan foydalanuvchilar:</b>\n"
            f"   <code>{len(user_warnings)}</code>\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )
        await update.message.reply_text(
            stats_text,
            parse_mode='HTML'
        )
    
    async def reset_user_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Foydalanuvchi ma'lumotlarini tozalash"""
        if not await self._check_admin(update, context):
            return
        
        if not context.args:
            await update.message.reply_text(
                "╔════════════════════════════╗\n"
                "║      ❌ <b>XATO</b> ❌      ║\n"
                "╚════════════════════════════╝\n\n"
                "⚠️ Foydalanuvchi ID sini kiriting!\n\n"
                "📌 <b>Misol:</b>\n"
                "<code>/reset_user 123456789</code>"
            )
            return
        
        try:
            user_id = int(context.args[0])
            if user_id in user_warnings:
                del user_warnings[user_id]
                await update.message.reply_text(
                    "╔════════════════════════════╗\n"
                    "║   ✅ <b>MUVAFFAQIYAT</b> ✅   ║\n"
                    "╚════════════════════════════╝\n\n"
                    f"✨ Foydalanuvchi <code>{user_id}</code>\n"
                    f"   ma'lumotlari <b>TOZALANDI!</b> ✨"
                )
            else:
                await update.message.reply_text(
                    "╔════════════════════════════╗\n"
                    "║   ℹ️ <b>XABAR</b> ℹ️   ║\n"
                    "╚════════════════════════════╝\n\n"
                    f"🔍 Foydalanuvchi <code>{user_id}</code>\n"
                    f"   topilmadi."
                )
        except ValueError:
            await update.message.reply_text(
                "╔════════════════════════════╗\n"
                "║      ❌ <b>XATO</b> ❌      ║\n"
                "╚════════════════════════════╝\n\n"
                "⚠️ Noto'g'ri ID format!\n"
                "📌 ID faqat raqamlardan iborat bo'lishi kerak."
            )
    
    async def _check_admin(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
        """Admin tekshirish"""
        if not update.message or not update.message.chat:
            return False
        
        try:
            member = await context.bot.get_chat_member(
                update.message.chat.id,
                update.message.from_user.id
            )
            return member.status in ['administrator', 'creator']
        except Exception as e:
            logger.error(f"Admin tekshirishda xatolik: {e}")
            return False
    
    def _calculate_mute_duration(self, warning_count: int) -> timedelta:
        """Mute muddatini hisoblash"""
        if warning_count == 1:
            return timedelta(minutes=5)
        elif warning_count == 2:
            return timedelta(minutes=15)
        elif warning_count == 3:
            return timedelta(hours=1)
        else:
            return timedelta(hours=24)
    
    async def _mute_user(self, update: Update, context: ContextTypes.DEFAULT_TYPE, duration: timedelta):
        """Foydalanuvchini mute qilish"""
        try:
            user_id = update.message.from_user.id
            chat_id = update.message.chat.id
            
            # Mute permissions
            until_date = datetime.now() + duration
            permissions = ChatPermissions(
                can_send_messages=False,
                can_send_audios=False,
                can_send_documents=False,
                can_send_photos=False,
                can_send_videos=False,
                can_send_video_notes=False,
                can_send_voice_notes=False,
                can_send_polls=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False
            )
            
            await context.bot.restrict_chat_member(
                chat_id=chat_id,
                user_id=user_id,
                permissions=permissions,
                until_date=until_date
            )
            
            return True
        except Exception as e:
            logger.error(f"Mute qilishda xatolik: {e}")
            return False
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xabarlarni boshqarish"""
        if not update.message or not update.message.text:
            return
        
        # Grupda ishlash
        if update.message.chat.type not in ['group', 'supergroup']:
            return
        
        user_id = update.message.from_user.id
        message_text = update.message.text.lower()
        chat_id = update.message.chat.id
        
        # Adminlarni o'tkazib yuborish
        try:
            member = await context.bot.get_chat_member(chat_id, user_id)
            if member.status in ['administrator', 'creator']:
                return
        except Exception:
            pass
        
        # Reklama/spam tekshirish
        if self.ad_filter.check(message_text):
            try:
                await update.message.delete()
                warning_msg = (
                    "╔════════════════════════════╗\n"
                    "║   🚫 <b>REKLAMA BLOKLASHI</b> 🚫  ║\n"
                    "╚════════════════════════════╝\n\n"
                    f"👤 <b>Foydalanuvchi:</b> {update.message.from_user.first_name}\n\n"
                    "⚠️ Reklama/spam yuborish <b>TAQIQ</b>!\n\n"
                    "💡 Guruhda faqat mazmunli xabarlar\n"
                    "   yuborishingiz mumkin."
                )
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=warning_msg,
                    parse_mode='HTML'
                )
                return
            except Exception as e:
                logger.error(f"Reklama bloklashda xatolik: {e}")
            return
        
        # So'kinish tekshirish
        profanity_found = self.profanity_filter.check(message_text)
        
        if profanity_found:
            # Foydalanuvchi ma'lumotlarini yangilash
            if user_id not in user_warnings:
                user_warnings[user_id] = {
                    'warnings': [],
                    'total_count': 0
                }
            
            warning_count = len(user_warnings[user_id]['warnings']) + 1
            user_warnings[user_id]['warnings'].append({
                'timestamp': datetime.now(),
                'message': update.message.text
            })
            user_warnings[user_id]['total_count'] = warning_count
            
            # Mute muddatini hisoblash
            mute_duration = self._calculate_mute_duration(warning_count)
            
            # Xabarni o'chirish
            try:
                await update.message.delete()
            except Exception as e:
                logger.error(f"Xabarni o'chirishda xatolik: {e}")
            
            # Mute qilish
            mute_success = await self._mute_user(update, context, mute_duration)
            
            # Ogohlantirish xabari
            duration_text = self._format_duration(mute_duration)
            
            # Emoji va belgilar jazo darajasiga qarab
            warning_emoji = "⚠️" * min(warning_count, 4)
            level_emoji = "🔴" if warning_count >= 4 else "🟠" if warning_count >= 3 else "🟡" if warning_count >= 2 else "🟢"
            
            warning_message = (
                "╔════════════════════════════╗\n"
                "║  🔇 <b>MUTE JAROYONI</b> 🔇  ║\n"
                "╚════════════════════════════╝\n\n"
                
                f"👤 <b>Foydalanuvchi:</b> {update.message.from_user.first_name}\n\n"
                
                "━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"⚠️ <b>Sabab:</b> So'kinish so'zi ishlatilgan\n\n"
                
                f"{level_emoji} <b>Jazo Darajasi:</b> <code>{warning_count}</code> {warning_emoji}\n\n"
                
                f"⏱️ <b>Mute Muddati:</b>\n"
                f"   <code>{duration_text}</code>\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                
                "💬 <b>Guruhda adabiy gapiring!</b>\n"
                "✨ Jazo muddati tugagunga qadar kutishingiz kerak."
            )
            
            try:
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=warning_message,
                    parse_mode='HTML'
                )
            except Exception as e:
                logger.error(f"Ogohlantirish xabarini yuborishda xatolik: {e}")
    
    @staticmethod
    def _format_duration(duration: timedelta) -> str:
        """Mute muddatini formatlash"""
        total_seconds = int(duration.total_seconds())
        
        if total_seconds < 3600:
            minutes = total_seconds // 60
            return f"{minutes} daqiqa"
        elif total_seconds < 86400:
            hours = total_seconds // 3600
            return f"{hours} soat"
        else:
            days = total_seconds // 86400
            return f"{days} kun"
    
    def run(self):
        """Botni ishga tushirish"""
        application = Application.builder().token(self.config.BOT_TOKEN).build()
        
        # Handlers
        application.add_handler(CommandHandler("start", self.start_command))
        application.add_handler(CommandHandler("help", self.help_command))
        application.add_handler(CommandHandler("stats", self.stats_command))
        application.add_handler(CommandHandler("reset_user", self.reset_user_command))
        
        # Message handler (so'kinish va reklama tekshirish)
        application.add_handler(
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                self.handle_message
            )
        )
        
        # Botni ishga tushirish
        logger.info("Bot ishga tushirildi!")
        application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    bot = ShutUpBot()
    bot.run()

