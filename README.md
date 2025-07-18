

# 👑 Telegram Anonymous Admin Bot

A lightweight Telegram bot to **promote users to anonymous administrators** in supergroups with a custom title.

> 🔒 Perfect for groups that want to elevate users without revealing their identity.

---

## 🚀 Features

* 🛠️ `/give_admin <user_id>`
  Promote a user to **anonymous admin** with full permissions and a custom title.

* 🧾 `/myid`
  Returns your Telegram user ID for easy use with `/give_admin`.

* 🐞 `/debug`
  Displays the current chat’s ID and type — handy for debugging.

---

## 📸 Example

```bash
/give_admin 123456789
```

➡️ Promotes user `123456789` to anonymous admin titled: **Group Overlord**

---

## 🧠 Admin Title

You can easily customize the admin title by changing this line in the code:

```python
ADMIN_TITLE = "Group Overlord"
```

---

## ⚙️ Setup

1. Clone the repo:

```bash
git clone https://github.com/yourusername/anon-admin-bot.git
cd anon-admin-bot
```

2. Install dependencies:

```bash
pip install python-telegram-bot --upgrade
```

3. Add your bot token:

Replace the `BOT_TOKEN` in the script:

```python
BOT_TOKEN = 'your_bot_token_here'
```

4. Run the bot:

```bash
python bot.py
```

---

## 🔐 Permissions Required

Make sure your bot has the **"Add Admins"** and **"Promote Members"** rights in the group.

---

## 🧪 Notes

* Only works in **supergroups**.
* The bot must be an **admin** to promote others.
* Anonymous admin feature is unique to Telegram supergroups.

---

## 🛠 Built With

* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) — A modern Python Telegram Bot API wrapper

---

## 🤝 Contributing

Pull requests welcome! Feel free to fork and submit improvements.

---

## 📜 License

MIT License — free for personal and commercial use.
