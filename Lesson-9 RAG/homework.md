# 📝 Homework Assignment

## 📌 Mavzu  
RAG (Retrieval-Augmented Generation) ni o‘rganish va Azure OpenAI bilan integratsiya qilish

## 🎯 Maqsad  
RAG arxitekturasini tushunish, darslikda berilgan kodlarni tahlil qilish va ularni Azure OpenAI xizmatlari bilan integratsiya qilish orqali amaliy tizim yaratish.

---

## 📋 Vazifa tavsifi  

Quyidagi bosqichlar amalga oshirilishi kerak:

### 1. RAG tushunchasini o‘rganish  
- RAG (Retrieval-Augmented Generation) nima ekanligini tushunish  
- Asosiy komponentlarini o‘rganish:
  - Retriever (ma'lumot qidirish)  
  - Generator (javob yaratish)  
- RAG qayerlarda ishlatilishini o‘rganish:
  - Chatbotlar  
  - Knowledge base tizimlari  
  - Dokument qidiruv tizimlari  

---

### 2. Darslikdagi kodni tahlil qilish  
- Berilgan RAG kodini tushunish  
- Quyidagi jarayonni aniqlash:
  - Ma'lumotlarni yuklash (documents)  
  - Embedding yaratish  
  - Vector database ga joylash  
  - Query qilish va javob olish  

---

### 3. Azure OpenAI bilan integratsiya  
- Azure OpenAI xizmatini sozlash:
  - API key  
  - Endpoint  
  - Deployment nomi  
- Darslikdagi kodni Azure OpenAI ga moslashtirish:
  - Embedding modelni Azure orqali ishlatish  
  - Chat/Completion modelni Azure orqali ishlatish  

---

### 4. Embedding va Retrieval jarayonini sozlash  
- Hujjatlar uchun embedding yaratish  
- Vector storage (masalan: FAISS, Chroma) bilan integratsiya  
- Foydalanuvchi query asosida eng mos hujjatlarni topish  

---

### 5. Javob generatsiyasi  
- Topilgan kontekstni Azure OpenAI modeliga uzatish  
- To‘liq va aniq javob generatsiya qilish  
- Prompt engineering qo‘llash  

---

### 6. Test qilish  
- Turli savollar bilan tizimni sinab ko‘rish  
- Natijalarni tekshirish:
  - Javobning aniqligi  
  - Kontekstga mosligi  

---

## ⚙️ Texnik talablar  
- Dasturlash tili: Python  
- AI: Azure OpenAI  
- Vector DB:
  - FAISS yoki Chroma  
- Kutubxonalar:
  - `langchain` yoki `llama-index` (ixtiyoriy)  

---

## 🚫 Cheklovlar  
- Noto‘g‘ri yoki irrelevant kontekstdan foydalanmaslik  
- Token limit va xarajatlarni hisobga olish  
- API xatoliklari uchun exception handling yozish  

---

## ✅ Kutilayotgan natija  
- RAG arxitekturasi tushuniladi  
- Darslik kodi muvaffaqiyatli ishlaydi  
- Azure OpenAI bilan to‘liq integratsiya qilinadi  
- Tizim real savollarga kontekst asosida javob bera oladi