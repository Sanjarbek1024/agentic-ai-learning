# 📝 Homework Assignment

## 📌 Mavzu  
n8n platformasini o‘rganish va memory asosida chat tizimi yaratish

## 🎯 Maqsad  
n8n automation platformasini o‘rganish va darslikda ko‘rsatilgan usul asosida xotiraga (memory) ega bo‘lgan chat tizimini yaratish.

---

## 📋 Vazifa tavsifi  

Quyidagi bosqichlar amalga oshirilishi kerak:

### 1. n8n bilan tanishish  
- n8n platformasining asosiy tushunchalarini o‘rganish:
  - Workflows  
  - Nodes  
  - Triggers  
- n8n interfeysi va ishlash prinsipini tushunish  

---

### 2. Chat workflow yaratish  
- n8n orqali chat tizimi uchun workflow tuzish  
- Foydalanuvchi inputini qabul qiluvchi node qo‘shish  
- AI (masalan, OpenAI) bilan integratsiya qilish  

---

### 3. Memory (xotira) qo‘shish  
- Chat history (oldingi xabarlar) saqlanishi kerak  
- Memory quyidagi usullardan biri orqali amalga oshirilishi mumkin:
  - n8n built-in memory (agar mavjud bo‘lsa)  
  - Database (SQLite / PostgreSQL)  
  - External storage (Redis va boshqalar)  

---

### 4. Chatni davom ettirish  
- Har bir yangi xabar oldingi suhbat kontekstini hisobga olgan holda ishlanishi kerak  
- AI ga oldingi xabarlar yuborilib, context saqlanishi ta’minlanadi  

---

### 5. Test qilish  
- Chat workflow ishga tushiriladi  
- Bir nechta ketma-ket xabarlar yuboriladi  
- Tizim oldingi suhbatni “eslab”, mos javob berishi tekshiriladi  

---

## ⚙️ Texnik talablar  
- Platforma: n8n  
- AI integratsiya: OpenAI API (yoki boshqa LLM)  
- Storage (memory uchun):
  - SQLite / PostgreSQL / Redis (ixtiyoriy)  
- Workflow to‘g‘ri va mantiqiy tuzilgan bo‘lishi kerak  

---

## ✅ Kutilayotgan natija  
- n8n platformasi tushuniladi va ishlatila oladi  
- Memory asosida ishlovchi chat tizimi yaratiladi  
- Chat kontekstni saqlagan holda to‘g‘ri javob beradi