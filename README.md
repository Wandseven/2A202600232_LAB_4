# TravelBuddy Agent 🚀✈️

Một trợ lý du lịch thông minh được xây dựng với **LangChain** + **LangGraph** + **OpenAI GPT-4**, chuyên tư vấn về chuyến bay, khách sạn, và lập kế hoạch ngân sách du lịch tại Việt Nam.

## 📋 Tính Năng

- **🛫 Tìm kiếm chuyến bay** — Tra cứu giá vé máy bay giữa các thành phố
- **🏨 Tìm kiếm khách sạn** — Tìm khách sạn theo ngân sách và địa điểm
- **💰 Tính toán ngân sách** — Quản lý chi phí chuyến đi và lên kế hoạch tài chính
- **🤖 AI thông minh** — Tư vấn du lịch tự động bằng tiếng Việt

## 📦 Cấu Trúc Dự Án

```
lab4_agent/
├── agent.py              # Core agent logic sử dụng LangGraph
├── tools.py              # 3 công cụ chính: search_flights, search_hotels, calculate_budget
├── system_prompt.txt     # Hướng dẫn hành vi của agent (persona + rules)
├── test_results.md       # Tài liệu kết quả test
└── README.md             # File này
```

## 🛠️ Cài Đặt

### Yêu Cầu
- Python 3.8+
- pip

### Bước 1: Tạo Virtual Environment

```bash
python -m venv venv
./venv/Scripts/Activate.ps1    # Trên Windows PowerShell
# hoặc
source venv/bin/activate        # Trên Linux/Mac
```

### Bước 2: Cài Đặt Dependencies

```bash
pip install -r requirements.txt
```

Danh sách package cần thiết:
```
langchain==0.1.x
langchain-openai
langgraph
python-dotenv
```

### Bước 3: Cấu Hình API Key

Tạo file `.env` trong thư mục gốc:

```env
OPENAI_API_KEY=your_api_key_here
```

## 🚀 Sử Dụng

### Chạy Agent

```bash
python agent.py
```

Agent sẽ sẵn sàng đáp ứng các yêu cầu du lịch của bạn.

### Ví Dụ Câu Hỏi

```
"Tôi muốn bay từ Hà Nội đến Đà Nẵng với ngân sách 5 triệu đồng, có khách sạn tốt không?"

"Giá vé máy bay từ Hà Nội đến Phú Quốc là bao nhiêu?"

"Tôi ở Hồ Chí Minh, muốn sang Đà Nẵng chơi 2 ngày. Tính toán chi phí vé và khách sạn với ngân sách 10 triệu?"
```

---

## 🛠️ Chi Tiết Công Cụ

### 1. `search_flights(origin: str, destination: str) -> str`

Tìm kiếm chuyến bay giữa hai điểm.

**Tham số:**
- `origin` — Thành phố xuất phát (ví dụ: "Hà Nội")
- `destination` — Thành phố đích (ví dụ: "Đà Nẵng")

**Kết quả:**
- Danh sách chuyến bay bao gồm: hãng hàng không, giờ cất/hạ cánh, loại vé, giá

**Ví dụ:**
```python
search_flights("Hà Nội", "Đà Nẵng")
```

---

### 2. `search_hotels(city: str, max_price_per_night: int = 99999999) -> str`

Tìm kiếm khách sạn theo thành phố và giá tối đa.

**Tham số:**
- `city` — Tên thành phố (ví dụ: "Đà Nẵng")
- `max_price_per_night` — Giá tối đa mỗi đêm (tùy chọn, mặc định không giới hạn)

**Kết quả:**
- Danh sách khách sạn: tên, số sao, giá/đêm, rating, khoảng cách từ trung tâm

**Ví dụ:**
```python
search_hotels("Đà Nẵng", max_price_per_night=800000)
```

---

### 3. `calculate_budget(total_budget: int, expenses: str = "", destination: str = "", hotel_price: int = 0, nights: int = 1) -> str`

Tính toán ngân sách còn lại và đề xuất chi phí dựa trên điểm đến.

**Tham số:**
- `total_budget` — Ngân sách tổng (bắt buộc)
- `expenses` — Chuỗi chi phí (ví dụ: "vé máy bay: 1.450.000đ, khách sạn: 700.000đ")
- `destination` — Điểm đến (dùng để đề xuất giá khách sạn)
- `hotel_price` — Giá khách sạn mỗi đêm
- `nights` — Số đêm lưu trú

**Kết quả:**
- Bảng chi phí chi tiết
- Tổng chi phí
- Ngân sách còn lại hoặc cảnh báo vượt ngân sách
- Đề xuất giá khách sạn theo điểm đến

**Ví dụ:**
```python
calculate_budget(
    total_budget=5000000,
    expenses="vé máy bay: 1.450.000đ",
    destination="Đà Nẵng",
    hotel_price=700000,
    nights=2
)
```

---

## 📊 Dữ Liệu Giả Lập

### Các Thành Phố/Tuyến Bay Có Sẵn
- **Hà Nội** ↔ Đà Nẵng / Phú Quốc / Hồ Chí Minh
- **Hồ Chí Minh** ↔ Đà Nẵng / Phú Quốc
- **Đà Nẵng**, **Phú Quốc**, **Hồ Chí Minh** (có khách sạn)

### Hãng Hàng Không
- Vietnam Airlines
- VietJet Air
- Bamboo Airways

---

## 🔧 Cấu Hình Agent

**File:** `system_prompt.txt`

Mô tả các yếu tố:
- **Persona**: Trợ lý thân thiện, am hiểu du lịch Việt Nam
- **Rules**: Ưu tiên tiết kiệm, tư vấn dựa vào ngân sách thực tế
- **Tools Instruction**: Hướng dẫn sử dụng 3 công cụ
- **Response Format**: Cấu trúc trả lời chuẩn

---

## 📝 Ví Dụ Sử Dụng

### Script Test

```bash
python test_api.py
```

Kiểm tra kết nối OpenAI API và các công cụ cơ bản.

### Chạy Agent Interactively

Chỉnh sửa `agent.py` để thêm vòng lặp tương tác:

```python
if __name__ == "__main__":
    from langgraph.graph import StateGraph, START
    
    app = builder.compile()
    
    while True:
        user_input = input("Bạn: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break
        
        result = app.invoke({"messages": [("user", user_input)]})
        print("Agent:", result["messages"][-1].content)
```

---

## 🐛 Troubleshooting

### Lỗi: `No module named 'langchain'`
```bash
pip install langchain langchain-openai langgraph
```

### Lỗi: `OPENAI_API_KEY not found`
- Kiểm tra file `.env` tồn tại
- Kiểm tra API key đúng

### Lỗi: `City not found in HOTELS_DB`
- Chỉ có dữ liệu khách sạn cho: Đà Nẵng, Phú Quốc, Hồ Chí Minh

---

## 📌 Ghi Chú

- Tất cả giá cả đều tính bằng **VND (Đồng Việt Nam)**
- Định dạng tiền tệ: `1.450.000đ`
- Agent được thiết kế để tư vấn du lịch Việt Nam
- Sử dụng mô hình **GPT-4o-mini** (tiết kiệm chi phí API)

---

## 📚 Tài Liệu Tham Khảo

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [OpenAI API](https://platform.openai.com/docs/)

---

## 👨‍💻 Tác Giả

VinAI Training Program - 2A202600232 Nguyen Tuan Kiet

---

## 📄 License

MIT License
