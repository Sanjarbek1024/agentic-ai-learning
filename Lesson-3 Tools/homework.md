# 📝 Homework Assignment

## 📌 Mavzu  
Function Calling orqali ma'lumotlar bazasi bilan ishlash

## 🎯 Maqsad  
Foydalanuvchi tomonidan berilgan savollarga asoslanib, sun'iy intellekt yordamida SQL query generatsiya qilish va natijani ma'lumotlar bazasidan olib foydalanuvchiga ko‘rsatish.

---

## 📋 Vazifa tavsifi  

Quyidagi funksionalliklar amalga oshirilishi kerak:

### 1. Function Calling integratsiyasi  
- AI model bilan function calling mexanizmi ishlatilishi kerak  
- Foydalanuvchi savoli analiz qilinadi va kerakli funksiya chaqiriladi  
- Funksiya parametr sifatida SQL query qabul qiladi  

---

### 2. SQL query generatsiyasi  
- Foydalanuvchi savoliga mos ravishda AI tomonidan SQL query yozilishi kerak  
- Query to‘g‘ri va xavfsiz bo‘lishi kerak  
- Faqat ruxsat etilgan (allowed) jadvallar bilan ishlashi kerak  

---

### 3. Database bilan ishlash  
- Generatsiya qilingan SQL query ma'lumotlar bazasida bajariladi  
- Natija (result) olinadi va qayta ishlanadi  
- Bo‘sh yoki xatolik holatlari uchun tekshiruv bo‘lishi kerak  

---

### 4. Natijani foydalanuvchiga chiqarish  
- DB dan olingan natija foydalanuvchiga tushunarli formatda chiqarilishi kerak  
- Misol:
  - Jadval ko‘rinishida  
  - JSON formatda  
  - Yoki oddiy matn ko‘rinishida  

---

## ⚙️ Texnik talablar  
- Dasturlash tili: Python  
- AI integratsiya: AzureOpenAI API or Gemini API (function calling)  
- DB: SQLite / PostgreSQL  
- Xavfsizlik:
  - SQL Injection oldini olish  
  - Faqat SELECT querylarga ruxsat berish tavsiya etiladi  

---

## 🚫 Cheklovlar  
- DELETE, UPDATE, INSERT kabi xavfli querylarga ruxsat berilmasligi kerak  
- Foydalanuvchi inputi to‘g‘ridan-to‘g‘ri queryga qo‘shilmasligi kerak  

---

## ✅ Kutilayotgan natija  
- Foydalanuvchi savol beradi → AI SQL query yozadi  
- Query DB da bajariladi  
- Natija foydalanuvchiga chiqariladi  
- Tizim xavfsiz va barqaror ishlaydi