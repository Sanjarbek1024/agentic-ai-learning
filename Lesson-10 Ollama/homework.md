# 📝 Homework Assignment

## 📌 Mavzu  
Ollama platformasini o‘rganish va quantized modellarda tajriba o‘tkazish

## 🎯 Maqsad  
Ollama toolini o‘rganish, darslikdagi kodlarni amaliy tarzda sinab ko‘rish hamda quantized (siqilgan) modellar bilan ishlash bo‘yicha tajriba orttirish.

---

## 📋 Vazifa tavsifi  

Quyidagi bosqichlar bajarilishi kerak:

### 1. Ollama bilan tanishish  
- Ollama nima ekanligini o‘rganish  
- Local LLM ishlash prinsipi bilan tanishish  
- Model yuklash va ishga tushirish jarayonini tushunish  

---

### 2. Darslikdagi kodlarni sinab ko‘rish  
- Berilgan Ollama kodlarini amaliy bajarish  
- Quyidagi funksiyalarni tekshirish:
  - Model chaqirish (generate)  
  - Chat completion  
  - Prompt berish va javob olish  

---

### 3. Model management  
- Mavjud modellar ro‘yxatini ko‘rish (`list`)  
- Yangi model yuklab olish (`pull`)  
- Modelni o‘chirish va boshqarish (`rm`)  

---

### 4. Quantized model bilan ishlash  
- Quantized model nima ekanligini o‘rganish  
- GGUF yoki shunga o‘xshash siqilgan modellardan foydalanish  
- Quyidagilarni sinab ko‘rish:
  - Tezlik farqi  
  - RAM/CPU ishlatilishi  
  - Javob sifati  

---

### 5. Amaliy test  
- Kamida 2 ta turli model sinab ko‘riladi:
  - Oddiy (full precision) model  
  - Quantized model (masalan: Q4, Q5, Q8 variantlari)  
- Har biriga bir xil prompt berilib natijalar taqqoslanadi  

---

## ⚙️ Texnik talablar  
- Platforma: Ollama (local runtime)  
- Dasturlash tili: Python yoki terminal (CLI)  
- Model formatlari:
  - GGUF (quantized)  
- Ixtiyoriy:
  - `ollama Python client` yoki HTTP API  

---

## 🚫 Cheklovlar  
- Faqat lokal ishlash (internetga bog‘liq bo‘lmagan testlar ham qilinishi mumkin)  
- Har bir model natijasi hujjatlashtirilishi kerak  

---

## 📊 Kutilayotgan natija  
- Ollama platformasi to‘liq o‘rganiladi  
- Model boshqarish amaliy ko‘nikmaga aylanadi  
- Quantized va full model farqlari aniq tushuniladi  
- Tezlik va resurs ishlatilishi bo‘yicha tahlil qilinadi