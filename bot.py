import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ── MESSAGES ─────────────────────────────────────────────────

WELCOME = """👋 Welcome! I'm Lincoln Adura's WhatsApp Business Bot.

I'm an Automation Developer, Web Developer & Bot Developer.

Reply with a number to explore:
1️⃣ Services
2️⃣ Pricing
3️⃣ Portfolio
4️⃣ About Me
5️⃣ Contact"""

SERVICES = """🛠 *Services*

🤖 *Automation Development*
End-to-end workflow automation using Python, n8n, Zapier & Make.

🌐 *Web Development*
Professional websites with full automation integration and live deployment.

💬 *Bot Development*
Telegram & WhatsApp bots built for always-on business communication.

📊 *Automated Reporting*
Data-driven reporting systems delivered automatically on schedule.

🧾 *Document & Invoice Automation*
Auto-generate and distribute professional PDF documents with zero manual effort.

🔗 *API & Systems Integration*
Connect platforms and tools so your entire operation runs seamlessly.

Reply with a number:
1️⃣ Services  2️⃣ Pricing  3️⃣ Portfolio  4️⃣ About  5️⃣ Contact"""

PRICING = """💰 *Pricing Guide*

🌐 Web Development — from $200
🤖 Automation System — from $300
💬 Telegram/WhatsApp Bot — from $250
📊 Automated Report System — from $300
🧾 Document & Invoice Automation — from $150
📦 Full Systems Package — from $600

Every project includes full setup, testing, and professional handover.
Custom quotes available for enterprise and complex projects.

Reply with a number:
1️⃣ Services  2️⃣ Pricing  3️⃣ Portfolio  4️⃣ About  5️⃣ Contact"""

PORTFOLIO = """📂 *Portfolio*

✅ Project 1 — Automated Business Report Sender
Connects to Google Sheets, processes data, and delivers branded reports via Gmail automatically.
🔗 github.com/Fiercexontan/auto-business-reporter

✅ Project 2 — Professional Web System with Contact Automation
Fully deployed website with automated lead capture and notification system.
🔗 lincolnadura.netlify.app

✅ Project 3 — Automated PDF Invoice Generator
Generates and delivers professional PDF invoices automatically with one command.
🔗 github.com/Fiercexontan/auto-invoice-generator

✅ Project 4 — Telegram Business Bot
Intelligent bot handling services, pricing, and portfolio 24/7.
🔗 github.com/Fiercexontan/telegram-business-bot

🌐 Full Portfolio: lincolnadura-portfolio.netlify.app

Reply with a number:
1️⃣ Services  2️⃣ Pricing  3️⃣ Portfolio  4️⃣ About  5️⃣ Contact"""

ABOUT = """👨‍💻 *About Lincoln Adura*

I'm a professional Automation Developer, Web Developer & Bot Developer based in Africa 🌍

I design and build systems that eliminate manual work, connect platforms intelligently, and run automatically around the clock.

🛠 Core Stack:
Python · JavaScript · n8n · Zapier · Make · Telegram API · WhatsApp API · Google Sheets API · Gmail SMTP · GitHub · Netlify · REST APIs

💡 Mission: To engineer systems that work harder than any manual process ever could.

📌 Note: I specialize in Automation, Web Development & Bot Development — and I take on any project that falls within or connects to these disciplines. If you have something in mind, let's talk.
 
Reply with a number:
1️⃣ Services  2️⃣ Pricing  3️⃣ Portfolio  4️⃣ About  5️⃣ Contact"""

CONTACT = """📩 *Get In Touch*

Have a project or system you want to build? Let's talk.

🌐 Portfolio: lincolnadura-portfolio.netlify.app
💼 LinkedIn: linkedin.com/in/lincoln-adura
📧 Email: lincolnadura97@gmail.com

I respond within 24 hours. Let's build something powerful together. 🚀

Reply with a number:
1️⃣ Services  2️⃣ Pricing  3️⃣ Portfolio  4️⃣ About  5️⃣ Contact"""

# ── WEBHOOK ──────────────────────────────────────────────────

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming = request.form.get("Body", "").strip().lower()
    response = MessagingResponse()
    msg = response.message()

    replies = {
        "1": SERVICES,
        "2": PRICING,
        "3": PORTFOLIO,
        "4": ABOUT,
        "5": CONTACT,
        "hi": WELCOME,
        "hello": WELCOME,
        "start": WELCOME,
        "menu": WELCOME,
    }

    msg.body(replies.get(incoming, WELCOME))
    return str(response)

# ── MAIN ─────────────────────────────────────────────────────

if __name__ == "__main__":
    print("🚀 Starting Lincoln Adura WhatsApp Bot...")
    print("✅ Bot is running on http://localhost:5000")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)