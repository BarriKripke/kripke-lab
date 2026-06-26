from pathlib import Path

HTML = r'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Kripke Lab | Лаборатория автоматизации</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>

<div class="boot" id="boot">
  <div class="terminal">
    <p>> Initializing KRIPKE LAB OS...</p>
    <p>> Loading Telegram Engine...</p>
    <p>> Loading Web Automation...</p>
    <p>> Loading Android Module...</p>
    <p class="ready">> READY</p>
  </div>
</div>

<div class="bg-grid"></div>

<header class="hero">
  <nav class="nav">
    <a class="brand" href="#">
      <span class="brand-mark">KL</span>
      <span><b>KRIPKE LAB</b><small>automation studio</small></span>
    </a>
    <div class="nav-links">
      <a href="#services">Модули</a>
      <a href="#portfolio">Портфолио</a>
      <a href="#contacts">Контакты</a>
    </div>
  </nav>

  <div class="hero-inner">
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
  </div>
</header>

<section class="metrics">
  <div><b>Telegram</b><span>боты, магазины, заявки</span></div>
  <div><b>Web</b><span>сайты, формы, панели</span></div>
  <div><b>Android</b><span>приложения из сайта</span></div>
  <div><b>Data</b><span>парсеры, Excel, Sheets</span></div>
</section>

<section id="services" class="section">
  <h2>Модули Kripke Lab</h2>
  <p class="section-text">Можно заказать один модуль или собрать систему: сайт → бот → заявки → таблицы → приложение.</p>

  <div class="modules">
    <article><span>01</span><h3>Telegram Engine</h3><p>Боты заявок, каталоги, магазины, оплаты, рассылки, уведомления.</p><b>от 3 000 ₽</b></article>
    <article><span>02</span><h3>Web Interface</h3><p>Лендинги, сайты-визитки, формы, портфолио, доработка сайтов.</p><b>от 4 000 ₽</b></article>
    <article><span>03</span><h3>Android Shell</h3><p>APK из сайта, WebView-приложения, мобильная витрина бизнеса.</p><b>от 5 000 ₽</b></article>
    <article><span>04</span><h3>Parser Core</h3><p>Сбор цен, товаров, контактов, объявлений и данных в Excel / CSV.</p><b>от 4 000 ₽</b></article>
    <article><span>05</span><h3>Sheets Automation</h3><p>Excel, Google Sheets, отчёты, формулы, автоматизация рутины.</p><b>от 2 000 ₽</b></article>
    <article><span>06</span><h3>Marketplace Pack</h3><p>Карточки WB / Ozon, инфографика, описания, таблицы товаров.</p><b>от 1 500 ₽</b></article>
  </div>
</section>

<section id="portfolio" class="section">
  <h2>Портфолио</h2>
  <p class="section-text">Примеры направлений, которые показывают, какие задачи закрывает Kripke Lab.</p>

  <div class="portfolio">
    <article><img src="images/telegram-zayavki.png"><div><h3>Telegram-бот заявок</h3><p>Сбор заявок и уведомления админу.</p></div></article>
    <article><img src="images/telegram-shop.png"><div><h3>Telegram-магазин</h3><p>Каталог, товары, кнопки заказа.</p></div></article>
    <article><img src="images/telegram-payment.png"><div><h3>Бот с оплатой</h3><p>Сценарии покупки и проверка оплаты.</p></div></article>
    <article><img src="images/android-site.png"><div><h3>Android из сайта</h3><p>WebView-приложение и APK.</p></div></article>
    <article><img src="images/parser-excel.png"><div><h3>Парсер в Excel</h3><p>Сбор данных в таблицы.</p></div></article>
    <article><img src="images/admin-panel.png"><div><h3>Админ-панель / CRM</h3><p>Заявки, клиенты, статусы.</p></div></article>
  </div>
</section>

<section class="section">
  <h2>Как проходит запуск</h2>
  <div class="timeline">
    <div><b>01</b><span>Разбираем задачу</span></div>
    <div><b>02</b><span>Выбираем простой MVP</span></div>
    <div><b>03</b><span>Собираем рабочую версию</span></div>
    <div><b>04</b><span>Проверяем и дорабатываем</span></div>
    <div><b>05</b><span>Запускаем и передаём проект</span></div>
  </div>
</section>

<section id="apk" class="apk">
  <div>
    <small>Android demo</small>
    <h2>APK-приложение Kripke Lab</h2>
    <p>Скоро здесь будет доступна демонстрация приложения сайта.</p>
  </div>
  <a class="btn" href="downloads/kripke-lab.apk" download>Скачать APK</a>
</section>

<section id="contacts" class="section contacts">
  <h2>Связь с Kripke Lab</h2>
  <p>Выберите удобную площадку или оставьте заявку через Telegram-бота.</p>

  <div class="contacts-grid">
    <a href="https://t.me/kripke_lab_bot">🤖 Telegram-бот</a>
    <a href="https://t.me/kripkelab">📢 Telegram-канал</a>
    <a href="https://t.me/kripke_barry">👤 Админ Telegram</a>
    <a href="https://vk.com/kripkelab">VK профиль</a>
    <a href="https://vk.com/kripkelab_official">VK сообщество</a>
    <a class="disabled" href="#">YouTube скоро</a>
    <a class="disabled" href="#">TikTok скоро</a>
  </div>
</section>

<footer>© Kripke Lab | Лаборатория автоматизации</footer>

<div class="chat-widget">
  <div class="chat-window">
    <button class="chat-close">×</button>
    <b>🤖 Kripke Lab Bot</b>
    <p>Здравствуйте! Чем помочь?</p>
    <a href="https://t.me/kripke_lab_bot">Оставить заявку</a>
    <a href="#services">Посмотреть услуги</a>
    <a href="https://t.me/kripke_barry">Написать админу</a>
  </div>
  <button class="chat-button">🤖</button>
</div>

<script src="script.js"></script>
</body>
</html>
'''

CSS = r'''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Arial,sans-serif;background:#020617;color:#fff;overflow-x:hidden}a{color:inherit}.bg-grid{position:fixed;inset:0;z-index:-2;background:radial-gradient(circle at 20% 5%,rgba(34,211,238,.22),transparent 28%),radial-gradient(circle at 80% 15%,rgba(168,85,247,.16),transparent 28%),radial-gradient(circle at 50% 70%,rgba(34,197,94,.12),transparent 30%),linear-gradient(180deg,#020617,#07111f 45%,#020617)}.bg-grid:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(148,163,184,.055) 1px,transparent 1px),linear-gradient(90deg,rgba(148,163,184,.055) 1px,transparent 1px);background-size:42px 42px}.boot{position:fixed;inset:0;background:#020617;z-index:9999;display:grid;place-items:center;animation:bootHide .6s ease 2.3s forwards}.terminal{width:min(560px,90vw);padding:30px;border:1px solid rgba(34,211,238,.35);border-radius:22px;background:rgba(15,23,42,.86);box-shadow:0 0 80px rgba(34,211,238,.18)}.terminal p{font-family:monospace;color:#7dd3fc;margin:10px 0}.terminal .ready{color:#22c55e}@keyframes bootHide{to{opacity:0;visibility:hidden}}.hero{min-height:100vh;padding:24px;position:relative}.nav{max-width:1200px;margin:auto;display:flex;align-items:center;justify-content:space-between;padding:18px 0}.brand{display:flex;gap:14px;align-items:center;text-decoration:none}.brand-mark{width:52px;height:52px;border-radius:16px;display:grid;place-items:center;font-weight:900;background:linear-gradient(135deg,#06b6d4,#22c55e);box-shadow:0 20px 60px rgba(6,182,212,.35)}.brand b{display:block;letter-spacing:3px;color:#7dd3fc}.brand small{color:#94a3b8}.nav-links{display:flex;gap:24px}.nav-links a{text-decoration:none;color:#cbd5e1;font-weight:800}.nav-links a:hover{color:#7dd3fc}.hero-inner{max-width:980px;margin:145px auto 0;text-align:center;position:relative;z-index:2}.eyebrow{display:inline-block;padding:10px 18px;border:1px solid rgba(125,211,252,.45);border-radius:999px;color:#7dd3fc;background:rgba(15,23,42,.6);margin-bottom:26px}h1{font-size:76px;line-height:.98;margin:0 0 28px;letter-spacing:-3px;background:linear-gradient(180deg,#fff,#9bdcff);-webkit-background-clip:text;color:transparent}.hero p,.section-text{color:#cbd5e1;line-height:1.6}.hero p{font-size:22px;max-width:780px;margin:0 auto 36px}.buttons{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}.btn{display:inline-block;padding:16px 30px;border-radius:14px;text-decoration:none;font-weight:900;background:linear-gradient(135deg,#06b6d4,#22c55e);box-shadow:0 18px 55px rgba(6,182,212,.28)}.btn.ghost{background:rgba(15,23,42,.6);border:1px solid rgba(125,211,252,.45);box-shadow:none}.orbit{position:absolute;left:50%;bottom:60px;transform:translateX(-50%);width:520px;height:230px;opacity:.9}.core{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:160px;height:160px;border-radius:50%;display:grid;place-items:center;text-align:center;font-weight:900;background:rgba(15,23,42,.75);border:1px solid rgba(125,211,252,.45);box-shadow:0 0 80px rgba(34,211,238,.22)}.orbit:before{content:"";position:absolute;inset:15px;border:1px solid rgba(125,211,252,.18);border-radius:50%;animation:spin 18s linear infinite}.node{position:absolute;padding:13px 18px;border-radius:999px;background:rgba(15,23,42,.85);border:1px solid rgba(125,211,252,.3);font-weight:900}.n1{left:5%;top:18%}.n2{right:2%;top:25%}.n3{left:16%;bottom:10%}.n4{right:16%;bottom:4%}@keyframes spin{to{transform:rotate(360deg)}}.metrics,.section,.apk{max-width:1200px;margin:auto;padding:80px 24px}.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:-60px}.metrics div,.modules article,.portfolio article,.timeline div,.contacts-grid a{background:rgba(15,23,42,.68);border:1px solid rgba(125,211,252,.16);border-radius:24px;backdrop-filter:blur(16px)}.metrics div{padding:24px}.metrics b{display:block;color:#7dd3fc;font-size:24px;margin-bottom:8px}.metrics span{color:#cbd5e1}h2{text-align:center;font-size:48px;margin:0 0 18px;letter-spacing:-1px}.section-text{text-align:center;max-width:780px;margin:0 auto 44px;font-size:19px}.modules{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}.modules article{padding:30px;min-height:245px;transition:.25s}.modules article:hover,.portfolio article:hover,.contacts-grid a:hover{transform:translateY(-5px);border-color:rgba(125,211,252,.55)}.modules span{color:#22c55e;font-weight:900}.modules h3{font-size:26px;margin:16px 0}.modules p,.portfolio p,.timeline span{color:#dbeafe;line-height:1.5}.modules b{display:block;color:#22c55e;margin-top:20px}.portfolio{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}.portfolio article{overflow:hidden;transition:.25s}.portfolio img{width:100%;height:230px;object-fit:cover;display:block}.portfolio div{padding:22px}.portfolio h3{margin:0 0 10px;font-size:22px}.timeline{display:grid;grid-template-columns:repeat(5,1fr);gap:18px}.timeline div{padding:24px}.timeline b{display:block;color:#7dd3fc;font-size:24px;margin-bottom:12px}.apk{display:flex;justify-content:space-between;align-items:center;gap:28px;background:linear-gradient(135deg,rgba(14,165,233,.16),rgba(34,197,94,.10));border:1px solid rgba(125,211,252,.25);border-radius:34px;margin-top:40px;margin-bottom:60px}.apk small{color:#7dd3fc;font-weight:900}.apk h2{text-align:left}.apk p{color:#cbd5e1}.contacts{text-align:center}.contacts p{color:#cbd5e1;font-size:19px}.contacts-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:34px}.contacts-grid a{padding:18px;text-decoration:none;font-weight:900}.disabled{opacity:.55;cursor:not-allowed}footer{text-align:center;color:#94a3b8;padding:34px;border-top:1px solid rgba(148,163,184,.12)}.chat-widget{position:fixed;right:24px;bottom:24px;z-index:999}.chat-button{width:68px;height:68px;border-radius:50%;border:0;background:linear-gradient(135deg,#06b6d4,#22c55e);font-size:31px;cursor:pointer;box-shadow:0 18px 55px rgba(6,182,212,.45)}.chat-window{display:none;position:absolute;right:0;bottom:84px;width:300px;padding:22px;background:rgba(15,23,42,.96);border:1px solid rgba(125,211,252,.45);border-radius:22px;box-shadow:0 24px 70px rgba(0,0,0,.45);backdrop-filter:blur(16px)}.chat-window.active{display:block}.chat-close{position:absolute;right:14px;top:10px;background:none;border:0;color:#94a3b8;font-size:24px;cursor:pointer}.chat-window b{color:#7dd3fc}.chat-window p{color:#cbd5e1}.chat-window a{display:block;text-decoration:none;padding:12px 14px;margin-top:10px;background:#101c2f;border:1px solid #26364f;border-radius:12px;font-weight:800}@media(max-width:1000px){h1{font-size:52px}.orbit{position:relative;left:auto;bottom:auto;transform:none;margin:60px auto 0}.metrics,.modules,.portfolio,.timeline,.contacts-grid{grid-template-columns:repeat(2,1fr)}.apk{flex-direction:column;align-items:flex-start}}@media(max-width:620px){.nav{align-items:flex-start;gap:18px;flex-direction:column}.nav-links{flex-wrap:wrap}.hero-inner{margin-top:80px;text-align:left}.buttons{justify-content:flex-start}h1{font-size:42px;letter-spacing:-1px}.hero p{font-size:18px}.orbit{width:100%;height:250px}.metrics,.modules,.portfolio,.timeline,.contacts-grid{grid-template-columns:1fr}.portfolio img{height:210px}.chat-widget{right:16px;bottom:16px}.chat-window{width:280px}}
'''

JS = r'''const chatButton = document.querySelector(".chat-button");
const chatWindow = document.querySelector(".chat-window");
const chatClose = document.querySelector(".chat-close");

if (chatButton && chatWindow && chatClose) {
  chatButton.addEventListener("click", () => chatWindow.classList.toggle("active"));
  chatClose.addEventListener("click", () => chatWindow.classList.remove("active"));
  setTimeout(() => chatWindow.classList.add("active"), 2500);
}
'''

Path("index.html").write_text(HTML, encoding="utf-8")
Path("style.css").write_text(CSS, encoding="utf-8")
Path("script.js").write_text(JS, encoding="utf-8")

print("Kripke Lab 3.0 applied: index.html, style.css, script.js")
