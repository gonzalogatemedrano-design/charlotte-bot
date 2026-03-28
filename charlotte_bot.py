import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# ─── CONFIGURACIÓN ────────────────────────────────────────────────────────────
TOKEN = "8562554776:AAEHmLXMM_M-PxRagft6bDYpmfVRbVdW7H0"
FILE_ID = "BAACAgEAAxkDAAMNacdAaFrRvESjFbNvXv2azkQ222IAAvwFAAKrP0BGs0EL-ydfVY86BA"
LANDING_URL = "https://starfayglobal.com/go/ru"
# ──────────────────────────────────────────────────────────────────────────────

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

usuarios_atendidos = set()

async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    nombre = update.effective_user.first_name
    print(f"📩 Mensaje recibido de {nombre} (ID: {user_id})")

    if user_id in usuarios_atendidos:
        print(f"⚠️ Usuario {nombre} ya fue atendido, saltando...")
        return

    usuarios_atendidos.add(user_id)

    try:
        print(f"⚡ Mandando video a {nombre}...")
        await update.message.reply_video(
            video=FILE_ID,
            caption=f"🎁 Regalo desbloqueado, te explico cómo aprovecharlo ya mismo👇\n\nAquí está tu link exclusivo, regístrate ahora antes de que el código promocional se agote 👇🏼\n\n{LANDING_URL}"
        )
        print(f"✅ Mensaje enviado a {nombre}")
    except Exception as e:
        print(f"❌ Error: {e}")
        usuarios_atendidos.discard(user_id)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, manejar_mensaje))
    print("✅ Bot de Charlotte iniciado y esperando mensajes...")
    app.run_polling()

if __name__ == "__main__":
    main()

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, manejar_mensaje))
    print("✅ Bot de Charlotte iniciado y esperando mensajes...")
    app.run_polling()

if __name__ == "__main__":
    main()


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, manejar_mensaje))
    print("✅ Bot de Charlotte iniciado y esperando mensajes...")
    app.run_polling()

if __name__ == "__main__":
    main()
