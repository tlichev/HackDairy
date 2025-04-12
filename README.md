# 🐄 HackDairy – Hacker Blog & Web Security Playground

**HackDairy** е Django уеб приложение тип блог, фокусирано върху демонстрация на уязвимости в уеб сигурността и тяхното предотвратяване. Проектът е подходящ както за обучение, така и за тестване на защити като **XSS** и **CSP**.

---

## 🚀 Основни функции

- 📝 Създаване и четене на блог постове на хакерски теми
- 💀 Симулиране на Cross-Site Scripting (**XSS**) атаки
- 🛡️ Тестове на Content Security Policy (**CSP**) защита
- 🔄 Два клона:
  - `insecure` – без защити, идеален за демонстрация на уязвимости
  - `secure` – с приложени мерки за сигурност

---

## 🛠️ Технологии

- Python 3.x
- Django 4.x
- SQLite (локално)
- Bootstrap (по избор за UI)

---

## ⚙️ Инсталация

```bash
# 1. Клонирай проекта
git clone https://github.com/твоя-потребител/HackDairy.git
cd HackDairy

# 2. Създай виртуална среда
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Инсталирай зависимостите
pip install -r requirements.txt

# 4. Стартирай сървъра
python manage.py runserver
