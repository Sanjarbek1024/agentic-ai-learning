# 📝 Homework Assignment

## 📌 Mavzu  
Suhbatni ma'lumotlar bazasida saqlash va qayta davom ettirish

## 🎯 Maqsad  
Foydalanuvchi bilan tashkil qilingan suhbatni ma'lumotlar bazasiga yozish va dastur qayta ishga tushirilganda suhbatni oxirgi holatidan davom ettirish mexanizmini ishlab chiqish.

---

## 📋 Vazifa tavsifi  

Quyidagi funksionalliklar amalga oshirilishi kerak:

### 1. Suhbatni saqlash  
- Foydalanuvchi va tizim o‘rtasidagi barcha xabarlar ma'lumotlar bazasiga yozilishi kerak  
- Har bir xabar quyidagi ma'lumotlarni o‘z ichiga olishi lozim:
  - sessiya ID  
  - Xabar matni  
  - Xabar turi (user / system)  
  - Yuborilgan vaqt (timestamp)

---

### 2. Ma'lumotlar bazasi bilan ishlash  
- Istalgan DB dan foydalanish mumkin:
  - SQLite (tavsiya etiladi, oddiyligi sababli)
  - PostgreSQL
  - MySQL  
- Jadval (table) strukturasi aniq ishlab chiqilishi kerak

---

### 3. Suhbatni tiklash (resume qilish)  
- Dastur qayta ishga tushirilganda:
  - Oxirgi sessiya aniqlanishi kerak  
  - Saqlangan xabarlar DB dan o‘qilishi kerak  
  - Suhbat oxirgi joyidan davom ettirilishi kerak  

---

### 4. Terminal orqali ishlash  
- Dastur terminal (CLI) orqali ishlashi kerak  
- Foydalanuvchi xabar yozadi → tizim javob beradi → DB ga saqlanadi  
- Dastur to‘xtatilganda (stop), qayta ishga tushirilganda eski suhbat davom etadi  

---

## ⚙️ Texnik talablar  
- Dasturlash tili: Python  
- DB bilan ishlash uchun kutubxona:
  - `sqlite3` yoki `SQLAlchemy`  
- Kod modul tarzida yozilishi kerak  
- Exception handling (xatoliklarni ushlash) qo‘shilishi kerak  

---

## ✅ Kutilayotgan natija  
- Suhbatlar to‘liq DB da saqlanadi  
- Dastur qayta ishga tushirilganda suhbat yo‘qolmaydi  
- Foydalanuvchi suhbatni uzluksiz davom ettira oladi