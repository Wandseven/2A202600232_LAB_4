## Test 1: Direct Answer (Không cần tool)

User: "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu."

Kỳ vọng: Agent chào hỏi, hỏi thêm về sở thích/ngân sách/thời gian. Không gọi tool nào.

### Result:

Bạn: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.

Trả lời trực tiếp

Chào bạn! Rất vui khi được giúp đỡ bạn lên kế hoạch cho chuyến đi. Bạn có ý định đi đâu chưa? Hay bạn muốn tôi gợi ý một số địa điểm thú vị để sống ảo, khám phá văn hóa hay thư giãn? Ngoài ra, cho tôi biết bạn dự định đi trong thời gian nào và ngân sách khoảng bao nhiêu nhé!

## Test 2: Single Tool Call

User: "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng"

Kỳ vọng: Gọi search_flights("Hà Nội", "Đà Nẵng"), liệt kê 4 chuyến bay.

### Result:

Bạn: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng         

Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})

Trả lời trực tiếp

Chuyến bay từ Hà Nội đi Đà Nẵng có các lựa chọn sau:

1. **Vietnam Airlines**: Khởi hành lúc 06:00, đến 07:20 - Economy - Giá 1.450.000đ
2. **Vietnam Airlines**: Khởi hành lúc 14:00, đến 15:20 - Business - Giá 2.800.000đ
3. **VietJet Air**: Khởi hành lúc 08:30, đến 09:50 - Economy - Giá 890.000đ
4. **Bamboo Airways**: Khởi hành lúc 11:00, đến 12:20 - Economy - Giá 1.200.000đ

Nếu bạn có nhu cầu cụ thể về thời gian bay hoặc loại ghế, cho mình biết để mình có thể tư vấn thêm nhé!

## Test 3: Multi-Step Tool Chaining

User: "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!"

Kỳ vọng: Agent phải tự chuỗi nhiều bước:

search_flights("Hà Nội", "Phú Quốc") → tìm vé rẻ nhất (1.100.000đ)

Google Hotels("Phú Quốc", max_price phù hợp) → gợi ý trong tầm giá

calculate_budget(5000000, "vé_bay: 1100000, khách_sạn: ...") → tính còn lại

Kết quả: Rồi tổng hợp thành gợi ý hoàn chỉnh với bảng chi phí.

### Result:

Bạn: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})

Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 2500000})

Gọi tool: calculate_budget({'total_budget': 5000000, 'expenses': '2100000, 1100000, 850000, 620000'})

Gọi tool: calculate_budget({'total_budget': 5000000, 'expenses': '2100000, 8500000'})

Gọi tool: calculate_budget({'total_budget': 5000000, 'expenses': '2100000, 2200000'})

Trả lời trực tiếp

Dựa trên yêu cầu của bạn, dưới đây là những thông tin chi tiết cho chuyến đi từ Hà Nội đến Phú Quốc trong 2 đêm:

**Chuyến bay:**
1. **VietJet Air** - Khởi hành lúc 10:00 và đến Phú Quốc lúc 12:15 - Giá vé: 1.350.000đ
2. **VietJet Air** - Khởi hành lúc 16:00 và đến Phú Quốc lúc 18:15 - Giá vé: 1.100.000đ

**Khách sạn:**
1. **Ocean Pearl - 4 sao** - Giá: 850.000đ/đêm
2. **Sunny Beach Resort - 5 sao** - Giá: 1.100.000đ/đêm
3. **Island Garden Hotel - 3 sao** - Giá: 620.000đ/đêm

**Tổng chi phí ước tính:**
- Chọn chuyến bay **VietJet Air** (giá vé 1.350.000đ)
- Chọn khách sạn **Ocean Pearl** (850.000đ/đêm x 2 đêm = 1.700.000đ)

**Tổng chi phí:**
- Vé máy bay: 1.350.000đ
- Khách sạn: 1.700.000đ
- **Tổng cộng: 3.050.000đ**

Với ngân sách 5 triệu, bạn còn dư 1.950.000đ cho chi phí ăn uống, di chuyển và tham quan tại Phú Quốc. 

**Gợi ý thêm:**
- Hãy đặt vé máy bay và lưu trú sớm để có giá tốt nhất. 
- Tham khảo các điểm tham quan nổi tiếng như Vinpearl, bãi biển Long Beach và khu phố cổ Dương Đông khi đến Phú Quốc nhé!

Nếu bạn cần thêm thông tin chi tiết hoặc hỗ trợ gì khác, cứ cho mình biết nhé!

## Test 4: Missing Info / Clarification

User: "Tôi muốn đặt khách sạn"

Kỳ vọng: Agent hỏi lại: thành phố nào? bao nhiêu đêm? ngân sách bao nhiêu? Không gọi tool vội.

### Result:

Bạn: Tôi muốn đặt khách sạn

Trả lời trực tiếp

Bạn vui lòng cung cấp thông tin chi tiết hơn về yêu cầu của bạn nhé! Bạn đang tìm khách sạn tại thành phố nào? Ngân sách mỗi đêm của bạn là bao nhiêu? Thời gian lưu trú là khi nào?

## Test 5: Guardrail / Refusal

User: "Giải giúp tôi bài tập lập trình Python về linked list"

Kỳ vọng: Từ chối lịch sự, nói rằng chỉ hỗ trợ về du lịch.

### Result:

Bạn: Giải giúp tôi bài tập lập trình Python về linked list

Trả lời trực tiếp

Xin lỗi, nhưng tôi không thể giúp bạn với bài tập lập trình. Tuy nhiên, nếu bạn cần lên kế hoạch cho chuyến đi, tìm vé máy bay, khách sạn hoặc quản lý ngân sách cho chuyến đi của mình, tôi rất sẵn lòng hỗ trợ! Hãy cho tôi biết thông tin bạn cần nhé.