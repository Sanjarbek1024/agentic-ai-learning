# 📝 Homework Assignment

## 📌 Mavzu  
Chat tizimini kengaytirish va production darajaga olib chiqish

## 🎯 Maqsad  
Mavjud chat tizimini takomillashtirish, ma'lumotlar bazasini optimallashtirish va qo‘shimcha funksiyalar qo‘shish orqali uni production-ready holatga keltirish.

---

## 📋 Vazifa tavsifi  

Quyidagi funksionalliklar amalga oshirilishi kerak:

### 1. Production-ready Database va SQLAlchemy  
- Ma'lumotlar bazasi production darajada ishlashga tayyor bo‘lishi kerak
- Model (jadval) strukturasi to‘g‘ri va optimallashtirilgan bo‘lishi kerak  
- Migration (masalan, Alembic) qo‘llash tavsiya etiladi  

---

### 2. Oxirgi N ta xabarni olish (Optional)  
- Foydalanuvchi uchun oxirgi **N ta xabarni olish** imkoniyati qo‘shilishi kerak  
- Bu parametr configurable (o‘zgaruvchan) bo‘lishi lozim  
- Misol:
  - Oxirgi 10 ta xabar  
  - Oxirgi 50 ta xabar  

---

### 3. Chat xonalar (Chat Rooms) qo‘shish (Optional)  
- Har bir foydalanuvchi uchun alohida chat xonalar yaratish imkoniyati  
- Yoki bir nechta foydalanuvchi bitta chat room ichida bo‘lishi mumkin  
- Har bir chat room quyidagi ma'lumotlarni o‘z ichiga olishi kerak:
  - Room ID  
  - Foydalanuvchilar ro‘yxati  
  - Xabarlar tarixi  

---

## ⚙️ Texnik talablar  
- Dasturlash tili: Python  
- `SQLAlchemy`  
- Qo‘shimcha:
  - `Alembic` (migration uchun, ixtiyoriy lekin tavsiya etiladi)  
- Kod toza va modul tarzda yozilishi kerak  

---

## ✅ Kutilayotgan natija  
- Tizim production darajada ishlashga tayyor bo‘ladi  
- Xabarlar bilan ishlash samaradorligi oshadi  
- Qo‘shimcha funksiyalar (history, chat rooms) muvaffaqiyatli ishlaydi