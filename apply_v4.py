from pathlib import Path

html = Path("index.html").read_text(encoding="utf-8")
css = Path("style.css").read_text(encoding="utf-8")

old_hero = '''  <div class="hero-inner">
    <div class="eyebrow">Telegram • Web • Android • Data • AI</div>
    <h1>Лаборатория автоматизации для бизнеса</h1>
    <p>
      Собираем сайты, Telegram-ботов, Android WebView-приложения,
      парсеры, таблицы, CRM-панели и цифровые витрины под задачу.
    </p>
    <div class="buttons">
      <a class="btn" href="https://t.me/kripke_lab_bot">Запустить проект</a>
      <a class="btn ghost" href="#portfolio">Смотреть работы</a>
    </div>
  </div>

  <div class="orbit">
    <div class="core">KRIPKE<br>LAB</div>
    <div class="node n1">🤖 Bot</div>
    <div class="node n2">🌐 Web</div>
    <div class="node n3">📱 APK</div>
    <div class="node n4">📊 Data</div>
  </div>'''

new_hero = '''  <div class="hero-product">
    <div class="hero-copy">
      <div class="eyebrow">Telegram • Web • Android • Data • AI</div>
      <h1>Лаборатория автоматизации для бизнеса</h1>
      <p>
        Собираем сайты, Telegram-ботов, Android WebView-приложения,
        парсеры, таблицы, CRM-панели и цифровые витрины под задачу.
      </p>
      <div class="buttons">
        <a class="btn" href="https://t.me/kripke_lab_bot">Запустить проект</a>
        <a class="btn ghost" href="#portfolio">Смотреть работы</a>
      </div>
    </div>

    <div class="product-panel">
      <div class="panel-top">
        <span class="dot green"></span>
        <span class="dot yellow"></span>
        <span class="dot blue"></span>
        <b>Kripke Lab Flow</b>
      </div>

      <div class="flow">
        <div class="flow-card active">
          <span>01</span>
          <b>Telegram Bot</b>
          <p>Клиент оставляет заявку</p>
        </div>

        <div class="flow-line"></div>

        <div class="flow-card">
          <span>02</span>
          <b>CRM / Admin</b>
          <p>Заявка приходит админу</p>
        </div>

        <div class="flow-line"></div>

        <div class="flow-card">
          <span>03</span>
          <b>Parser / Sheets</b>
          <p>Данные уходят в таблицы</p>
        </div>

        <div class="flow-line"></div>

        <div class="flow-card">
          <span>04</span>
          <b>Web / Android</b>
          <p>Витрина работает 24/7</p>
        </div>
      </div>

      <div class="panel-status">
        <span class="pulse"></span>
        SYSTEM ONLINE
      </div>
    </div>
  </div>'''

html = html.replace(old_hero, new_hero)

# Append v4 CSS overrides
css += r'''

/* === Kripke Lab 4.0 hero upgrade === */

.hero {
  min-height: 860px;
}

.hero-product {
  max-width: 1200px;
  margin: 115px auto 0;
  display: grid;
  grid-template-columns: 0.95fr 1.05fr;
  gap: 54px;
  align-items: center;
}

.hero-copy {
  position: relative;
  z-index: 2;
}

.hero-copy h1 {
  font-size: 58px;
  line-height: 1.02;
  letter-spacing: -2px;
  margin-bottom: 28px;
}

.hero-copy p {
  max-width: 650px;
  font-size: 21px;
  color: #cbd5e1;
  line-height: 1.6;
  margin-bottom: 34px;
}

.product-panel {
  position: relative;
  min-height: 520px;
  padding: 24px;
  border-radius: 34px;
  background:
    radial-gradient(circle at 20% 0%, rgba(34, 211, 238, 0.18), transparent 34%),
    radial-gradient(circle at 80% 100%, rgba(34, 197, 94, 0.13), transparent 34%),
    rgba(15, 23, 42, 0.72);
  border: 1px solid rgba(125, 211, 252, 0.24);
  box-shadow:
    0 35px 100px rgba(0, 0, 0, 0.42),
    inset 0 0 0 1px rgba(255,255,255,0.03);
  backdrop-filter: blur(18px);
  overflow: hidden;
}

.product-panel::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(125, 211, 252, 0.045) 1px, transparent 1px),
    linear-gradient(90deg, rgba(125, 211, 252, 0.045) 1px, transparent 1px);
  background-size: 34px 34px;
  opacity: .65;
}

.panel-top {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  gap: 9px;
  padding: 14px 16px;
  border-radius: 18px;
  background: rgba(2, 6, 23, 0.55);
  border: 1px solid rgba(125, 211, 252, 0.16);
  margin-bottom: 24px;
}

.panel-top b {
  margin-left: 10px;
  color: #dbeafe;
}

.dot {
  width: 11px;
  height: 11px;
  border-radius: 50%;
}

.green { background: #22c55e; }
.yellow { background: #eab308; }
.blue { background: #38bdf8; }

.flow {
  position: relative;
  z-index: 2;
  display: grid;
  gap: 14px;
}

.flow-card {
  position: relative;
  padding: 20px;
  border-radius: 22px;
  background: rgba(2, 6, 23, 0.58);
  border: 1px solid rgba(125, 211, 252, 0.16);
  transition: .25s ease;
}

.flow-card.active,
.flow-card:hover {
  border-color: rgba(34, 211, 238, 0.65);
  box-shadow: 0 0 40px rgba(34, 211, 238, 0.12);
  transform: translateX(4px);
}

.flow-card span {
  display: inline-block;
  color: #22c55e;
  font-weight: 900;
  margin-bottom: 8px;
}

.flow-card b {
  display: block;
  font-size: 22px;
  margin-bottom: 8px;
}

.flow-card p {
  color: #cbd5e1;
  margin: 0;
}

.flow-line {
  width: 2px;
  height: 24px;
  margin-left: 32px;
  background: linear-gradient(to bottom, #38bdf8, #22c55e);
  box-shadow: 0 0 20px rgba(34, 211, 238, .5);
  position: relative;
}

.flow-line::after {
  content: "";
  width: 9px;
  height: 9px;
  background: #22c55e;
  border-radius: 50%;
  position: absolute;
  left: -3.5px;
  top: 0;
  animation: dataMove 1.6s linear infinite;
}

@keyframes dataMove {
  from { top: 0; opacity: 0; }
  20% { opacity: 1; }
  to { top: 24px; opacity: 0; }
}

.panel-status {
  position: relative;
  z-index: 2;
  margin-top: 22px;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 13px 16px;
  border-radius: 999px;
  background: rgba(34, 197, 94, 0.10);
  border: 1px solid rgba(34, 197, 94, 0.35);
  color: #86efac;
  font-weight: 900;
}

.pulse {
  width: 10px;
  height: 10px;
  background: #22c55e;
  border-radius: 50%;
  box-shadow: 0 0 0 rgba(34, 197, 94, 0.8);
  animation: pulse 1.4s infinite;
}

@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.8); }
  70% { box-shadow: 0 0 0 12px rgba(34, 197, 94, 0); }
  100% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
}

/* Hide old orbit styles if something remains */
.orbit {
  display: none !important;
}

@media(max-width:1000px) {
  .hero-product {
    grid-template-columns: 1fr;
    margin-top: 80px;
  }

  .hero-copy {
    text-align: center;
  }

  .hero-copy p {
    margin-left: auto;
    margin-right: auto;
  }

  .hero-copy .buttons {
    justify-content: center;
  }

  .hero-copy h1 {
    font-size: 48px;
  }
}

@media(max-width:620px) {
  .hero {
    min-height: auto;
    padding-bottom: 70px;
  }

  .hero-product {
    margin-top: 60px;
  }

  .hero-copy {
    text-align: left;
  }

  .hero-copy .buttons {
    justify-content: flex-start;
  }

  .hero-copy h1 {
    font-size: 38px;
    letter-spacing: -1px;
  }

  .product-panel {
    padding: 16px;
    border-radius: 24px;
  }

  .flow-card {
    padding: 16px;
  }
}
'''

Path("index.html").write_text(html, encoding="utf-8")
Path("style.css").write_text(css, encoding="utf-8")

print("Kripke Lab 4.0 applied")
