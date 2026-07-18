# 📝 Homework Assignment

## 📌 Mavzu  
LangGraph: Reflection Agent yaratish va IELTS Writing workflow ishlab chiqish

## 🎯 Maqsad  
LangGraph framework yordamida reflection agent (o‘zini tekshiruvchi agent) yaratish, unda ikki LLM o‘rtasida iterativ workflow tashkil qilish: biri matn yozadi, ikkinchisi esa uni tekshiradi va kerak bo‘lsa qayta yozdiradi.

---

## 📋 Vazifa tavsifi  

Quyidagi tizim ishlab chiqilishi kerak:

### 1. Reflection Agent konseptini o‘rganish  
- Reflection agent nima ekanligini tushunish  
- Iterative AI workflow qanday ishlashini o‘rganish  
- LangGraph ning asosiy tushunchalari:
  - Nodes  
  - Edges  
  - State management  
  - Conditional routing  

---

### 2. IELTS Writing task workflow yaratish  

Tizim quyidagi logika asosida ishlashi kerak:

#### 🔹 Input  
- User 7+ band IELTS Writing Task 2 prompt beradi  

---

#### 🔹 Step 1: Writer LLM  
- 1-LLM quyidagi vazifani bajaradi:
  - IELTS Writing (Task 2) essay yozadi  
  - 7+ band darajaga mos yozuv yaratadi  
  - Structure:
    - Introduction  
    - Body paragraph 1  
    - Body paragraph 2  
    - Conclusion  

---

#### 🔹 Step 2: Checker LLM (Reflection Agent)  
- 2-LLM yozilgan essayni tekshiradi  
- Quyidagilarni baholaydi:
  - Grammar xatolari  
  - Cohesion va coherence  
  - Vocabulary level (Band 7+)  
  - Task response to‘g‘riligi  

- Natija:
  - `PASS` → agar 7+ band talabiga mos bo‘lsa  
  - `FAIL` → agar yetarli bo‘lmasa  

---

#### 🔹 Step 3: Loop (Reflection cycle)  
- Agar natija `FAIL` bo‘lsa:
  - Checker feedback yozadi  
  - Writer LLM qayta yozadi (improvement bilan)  
  - Process yana Checker ga qaytadi  
- Agar `PASS` bo‘lsa:
  - Workflow to‘xtaydi (END)

---

### 3. LangGraph workflow dizayni  
- Quyidagi node-lar bo‘lishi kerak:
  - `input_node` (user prompt)  
  - `writer_node` (LLM 1)  
  - `checker_node` (LLM 2)  
  - `router_node` (PASS/FAIL decision)  
  - `loop_edge` (FAIL bo‘lsa qaytish)  
  - `end_node`  

---

### 4. State management  
- Quyidagi ma’lumotlar state ichida saqlanishi kerak:
  - user_prompt  
  - essay  
  - feedback  
  - attempt_count  

---

## ⚙️ Texnik talablar  
- Dasturlash tili: Python  
- Framework: LangGraph  
- LLM: OpenAI / boshqa LLM (ixtiyoriy)  
- Workflow:
  - Conditional edges  
  - Loop structure  
  - State-based execution  

---

## 🚫 Cheklovlar  
- Infinite loop bo‘lmasligi kerak (max attempt limit qo‘shish tavsiya etiladi)  
- Checker aniq kriteriyalarga asoslanishi kerak  
- Har bir iteration log qilinishi kerak  

---

## ✅ Kutilayotgan natija  
- IELTS Writing generatsiya qiluvchi agent ishlaydi  
- Checker feedback asosida essayni yaxshilaydi  
- PASS bo‘lmaguncha qayta yozadi  
- LangGraph orqali to‘liq reflection workflow amalga oshiriladi