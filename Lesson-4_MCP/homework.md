# 📝 Homework Assignment

## 📌 Mavzu  
MCP asosida SQL tool yaratish va uni Claude Desktop bilan integratsiya qilish

## 🎯 Maqsad  
Model Context Protocol (MCP) asosida SQL bilan ishlovchi tool yaratish, uni server sifatida ishga tushirish va Claude Desktop ga ulab, ma'lumotlar bazasi ustida savollar berish orqali test qilish.

---

## 📋 Vazifa tavsifi  

Quyidagi bosqichlar amalga oshirilishi kerak:

### 1. MCP asosida SQL tool yaratish  
- MCP protokoli asosida ishlovchi tool ishlab chiqish  
- Tool quyidagi funksiyani bajarishi kerak:
  - SQL query qabul qilish  
  - Uni ma'lumotlar bazasida bajarish  
  - Natijani qaytarish  

---

### 2. MCP server yaratish  
- Yaratilgan tool MCP server sifatida ishga tushirilishi kerak  
- Server quyidagi imkoniyatlarga ega bo‘lishi lozim:
  - Request qabul qilish  
  - Tool ni chaqirish  
  - Natijani qaytarish  

---

### 3. Ma'lumotlar bazasi bilan integratsiya  
- SQL tool real ma'lumotlar bazasiga ulangan bo‘lishi kerak  
- Quyidagi DBlardan biri ishlatilishi mumkin:
  - SQLite  
  - PostgreSQL  
- Query bajarish va natijani olish mexanizmi to‘g‘ri ishlashi kerak  

---

### 4. Claude Desktop bilan integratsiya  
- MCP server ni Claude Desktop ga ulash  
- Config fayl orqali serverni ro‘yxatdan o‘tkazish  
- Claude orqali tool ni chaqirish imkoniyati yaratilishi kerak  

---

### 5. Test qilish  
- Claude Desktop orqali DB haqida savollar berish  
- Misollar:
  - "Eng ko‘p sotuv qilgan mahsulot qaysi?"  
  - "Jadvalda nechta foydalanuvchi bor?"  
- Tool to‘g‘ri SQL query ishlab chiqishi va natija qaytarishi kerak  

---

## ⚙️ Texnik talablar  
- Dasturlash tili: Python  
- MCP SDK yoki mos implementatsiya  
- DB bilan ishlash uchun:
  - `sqlite3` yoki `SQLAlchemy` 

---

## 🚫 Cheklovlar  
- Xavfli SQL operatsiyalarni (DELETE, DROP, UPDATE) cheklash  
- Faqat SELECT querylarga ruxsat berish tavsiya etiladi  
- Xatoliklar uchun exception handling bo‘lishi kerak  

---

## ✅ Kutilayotgan natija  
- MCP asosida ishlovchi SQL tool yaratiladi  
- Server muvaffaqiyatli ishga tushadi  
- Claude Desktop bilan integratsiya qilinadi  
- Foydalanuvchi savollariga DB dan real natijalar qaytariladi