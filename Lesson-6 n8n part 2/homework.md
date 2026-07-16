# 📝 Homework Assignment

## 📌 Mavzu  
n8n orqali PostgreSQL bilan integratsiya va AI chat orqali DB savollariga javob berish

## 🎯 Maqsad  
n8n platformasi yordamida PostgreSQL ma'lumotlar bazasiga ulanish, va AI chat orqali foydalanuvchi savollariga asoslanib DB dan ma'lumot olib, javob qaytaruvchi tizim yaratish.

---

## 📋 Vazifa tavsifi  

Quyidagi bosqichlar amalga oshirilishi kerak:

### 1. PostgreSQL bilan integratsiya  
- n8n da PostgreSQL node orqali DB ga ulanish  
- Kerakli credentials (host, port, user, password, database) sozlanishi kerak  
- Test query orqali ulanish muvaffaqiyatli ekanligi tekshiriladi  

---

### 2. Chat workflow yaratish  
- Foydalanuvchi inputini qabul qiluvchi trigger (Webhook / Chat node) qo‘shish  
- Input AI modelga yuboriladi  

---

### 3. AI orqali SQL query generatsiyasi  
- Foydalanuvchi savoliga mos SQL query AI tomonidan yaratiladi  
- Query faqat ruxsat etilgan jadvallar bilan ishlashi kerak  
- SELECT query bilan cheklash tavsiya etiladi  

---

### 4. PostgreSQL da query bajarish  
- AI tomonidan yaratilgan SQL query PostgreSQL node orqali bajariladi  
- Natija olinadi va keyingi bosqichga uzatiladi  

---

### 5. Natijani AI orqali formatlash  
- DB dan olingan natija AI ga yuboriladi  
- AI natijani foydalanuvchi uchun tushunarli ko‘rinishda qayta ishlaydi  

---

### 6. Foydalanuvchiga javob qaytarish  
- Yakuniy natija chat orqali foydalanuvchiga chiqariladi  
- Natija quyidagi formatlarda bo‘lishi mumkin:
  - Oddiy matn  
  - Jadval ko‘rinishida  
  - JSON formatda  

---

## ⚙️ Texnik talablar  
- Platforma: n8n  
- Ma'lumotlar bazasi: PostgreSQL  
- AI integratsiya: OpenAI API yoki boshqa LLM  
- Workflow quyidagi node-lardan tashkil topishi mumkin:
  - Webhook / Chat Trigger  
  - OpenAI (yoki AI node)  
  - PostgreSQL node  
  - Set / Function node  

---

## 🚫 Cheklovlar  
- DELETE, UPDATE, INSERT kabi querylarga ruxsat berilmasligi kerak  
- SQL Injection oldini olish choralarini ko‘rish kerak  
- Faqat SELECT querylarga ruxsat berish tavsiya etiladi  

---

## ✅ Kutilayotgan natija  
- n8n orqali PostgreSQL bilan to‘liq integratsiya ishlaydi  
- AI foydalanuvchi savolidan SQL query hosil qiladi  
- Query DB da bajariladi va natija olinadi  
- Foydalanuvchiga aniq va tushunarli javob qaytariladi