# 📝 Homework Assignment

## 📌 Mavzu  
Embedding va uning strategiyalarini o‘rganish hamda turli modellarda sinab ko‘rish

## 🎯 Maqsad  
Embedding tushunchasini chuqur o‘rganish, uning asosiy strategiyalarini tushunish va darslikdagi kodni turli embedding modellarda (masalan, HuggingFace, Gemini) sinab ko‘rish.

---

## 📋 Vazifa tavsifi  

Quyidagi bosqichlar amalga oshirilishi kerak:

### 1. Embedding tushunchasini o‘rganish  
- Embedding nima ekanligini tushunish  
- Matnni vektor ko‘rinishiga o‘tkazish prinsiplari  
- Embedding qayerlarda ishlatilishini o‘rganish:
  - Semantic search  
  - Recommendation systems  
  - Chatbotlar  
  - RAG (Retrieval-Augmented Generation) tizimlari  

---

### 2. Embedding strategiyalarini o‘rganish  
Quyidagi strategiyalarni tushunish va taqqoslash:

- Chunking (matnni bo‘laklarga ajratish)  
- Sliding window  
- Overlap qo‘llash  
- Context size bilan ishlash  
- Vector similarity (cosine similarity va boshqalar)  

---

### 3. Darslikdagi kodni tahlil qilish  
- Berilgan kodni tushunish  
- Qanday embedding modeli ishlatilayotganini aniqlash  
- Input → embedding → natija pipeline ni tahlil qilish  

---

### 4. Turli embedding modellarda sinab ko‘rish  
Darslikdagi kodni quyidagi modellarda ishlatib ko‘rish:

- HuggingFace (masalan: `sentence-transformers`)  
- Gemini Embeddings (Google)  
- (Ixtiyoriy) OpenAI embeddings  

Har bir model uchun:
- Embedding generatsiya qilish  
- Natijalarni taqqoslash  
- Tezlik va aniqlikni baholash  

---

### 5. Natijalarni tahlil qilish  
- Qaysi model yaxshiroq ishlayotganini aniqlash  
- Farqlarni yozib chiqish:
  - Aniqlik (relevance)  
  - Tezlik  
  - Resurs sarfi  

---

## ⚙️ Texnik talablar  
- Dasturlash tili: Python  
- Kutubxonalar:
  - `transformers` / `sentence-transformers` (HuggingFace)  
  - Google Gemini API  
- (Ixtiyoriy) `faiss` yoki `chroma` vector DB  

---

## ✅ Kutilayotgan natija  
- Embedding tushunchasi to‘liq o‘zlashtiriladi  
- Turli embedding modellari bilan ishlash tajribasi hosil qilinadi  
- Modellar orasida taqqoslash va tahlil amalga oshiriladi  
- Amaliy tajriba orqali eng optimal yechim aniqlanadi