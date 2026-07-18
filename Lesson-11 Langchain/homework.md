# 📝 Homework Assignment

## 📌 Mavzu  
LangChain PromptTemplate, Structured Output va Streaming bilan ishlash

## 🎯 Maqsad  
LangChain framework yordamida PromptTemplate yaratish, structured output (JSON format) olish, hamda streaming jarayonini sinab ko‘rish.

---

## 📋 Vazifa tavsifi  

Quyidagi amallar bajarilishi kerak:

---

### 1. PromptTemplate bilan ishlash  
- `ChatPromptTemplate` yordamida prompt yaratish  
- System va Human message formatidan foydalanish  
- Prompt ichida quyidagilar bo‘lishi kerak:
  - message input  
  - categories ro‘yxati  
- Prompt classification (tasniflash) vazifasini bajarishi kerak  

---

### 2. LLM integratsiya qilish  
- Azure OpenAI (`AzureChatOpenAI`) ulanishi sozlanishi kerak  
- Environment variables (`.env`) orqali API konfiguratsiya qilinadi:
  - API key  
  - endpoint  
  - version  
  - deployment name  

---

### 3. Structured Output (JSON format)  
- Modeldan faqat JSON formatda natija qaytarish talab qilinadi  
- Format quyidagicha bo‘lishi kerak:

```json
{
  "category_name": "Math | Music | Programming",
  "score": 0.0 - 1.0
}
```

- JSON parse qilish (`json.loads`) amalga oshiriladi  
- Xatolik holatlari uchun validation qo‘shish tavsiya etiladi  

---

### 4. LangChain Chain pipeline  
- Quyidagi pipeline ishlatiladi:

```
prompt → llm → output_parser
```

- `StrOutputParser` orqali raw output olinadi  
- Keyin JSON ga aylantiriladi  

---

### 5. Classification logikasi  
- Foydalanuvchi inputi asosida AI kategoriya aniqlaydi  
- Quyidagi kategoriyalar ishlatiladi:
  - Math  
  - Music  
  - Programming  

---

### 6. Natijani chiqarish  
- Console ga quyidagilar chiqariladi:
  - category_name  
  - score  

---

## ⚡ Bonus Task (Optional)  

### Streaming qo‘shish  
- `stream()` yoki `astream()` metodini ishlatish  
- Model javobini real-time (chunk-by-chunk) chiqarish  
- Streaming jarayonida JSON formatni buzmaslikka e'tibor berish  

---

## ⚙️ Texnik talablar  
- Python 3.10+  
- LangChain:
  - `langchain-core`  
  - `langchain-openai`  
- Azure OpenAI API  
- dotenv (`python-dotenv`)  
- JSON parsing (`json`)  

---

## 🚫 Cheklovlar  
- Output faqat JSON formatda bo‘lishi kerak  
- Prompt ichida category listdan tashqariga chiqmaslik kerak  
- API key kod ichida yozilmasligi kerak (faqat `.env`)  

---

## ✅ Kutilayotgan natija  
- LangChain PromptTemplate to‘g‘ri ishlaydi  
- AI message ni category ga ajratadi  
- Structured JSON output muvaffaqiyatli parse qilinadi  
- (Bonus) Streaming orqali real-time output ko‘rinadi