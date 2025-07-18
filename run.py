from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = 'bottoken'



# 💬 Custom title for the admin
ADMIN_TITLE = "Group Overlord"

# 🛠 /give_admin <user_id>
async def give_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat

    # Only for supergroups
    if chat.type != "supergroup":
        await update.message.reply_text("❌ This command only works in a *supergroup*.")
        return

    # Check if user ID is given
    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text("❗ Usage: /give_admin <user_id>")
        return

    user_id = int(context.args[0])

    try:
        # Promote the user with full rights and anonymity
        await context.bot.promote_chat_member(
            chat_id=chat.id,
            user_id=user_id,
            can_change_info=True,
            can_post_messages=True,
            can_edit_messages=True,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=True,
            can_manage_video_chats=True,
            is_anonymous=True
        )

        # Set the admin's custom title
        await context.bot.set_chat_administrator_custom_title(
            chat_id=chat.id,
            user_id=user_id,
            custom_title=ADMIN_TITLE
        )

        await update.message.reply_text(
            f"✅ User `{user_id}` promoted as *anonymous admin* titled: `{ADMIN_TITLE}`",
            parse_mode="Markdown"
        )

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# Optional: Show your user ID
async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Your Telegram ID is: `{update.effective_user.id}`",
        parse_mode="Markdown"
    )

# Optional: Debug group info
async def debug(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    await update.message.reply_text(
        f"Chat ID: `{chat.id}`\nChat Type: `{chat.type}`",
        parse_mode="Markdown"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("give_admin", give_admin))
    app.add_handler(CommandHandler("myid", myid))
    app.add_handler(CommandHandler("debug", debug))
    app.run_polling()

if __name__ == '__main__':
    main()
