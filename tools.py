import re
from langchain_core.tools import tool

# ============================================================
# MOCK DATA — Dữ liệu giả lập hệ thống du lịch
# ============================================================

FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1_450_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2_800_000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1_200_000, "class": "economy"},
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1_350_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1_100_000, "class": "economy"},
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1_600_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1_300_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3_200_000, "class": "business"},
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1_300_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780_000, "class": "economy"},
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650_000, "class": "economy"},
    ],
}

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Sea Breeze Hotel", "price": 700000, "rating": 4.5, "stars": 4, "distance": "0.4 km"},
        {"name": "Sunset Boutique", "price": 550000, "rating": 4.2, "stars": 3, "distance": "1.1 km"},
        {"name": "Dragon Beach Resort", "price": 900000, "rating": 4.8, "stars": 5, "distance": "0.8 km"},
    ],
    "Phú Quốc": [
        {"name": "Ocean Pearl", "price": 850000, "rating": 4.6, "stars": 4, "distance": "2.0 km"},
        {"name": "Island Garden Hotel", "price": 620000, "rating": 4.1, "stars": 3, "distance": "1.5 km"},
        {"name": "Sunny Beach Resort", "price": 1100000, "rating": 4.9, "stars": 5, "distance": "0.7 km"},
    ],
    "Hồ Chí Minh": [
        {"name": "Central Saigon Hotel", "price": 760000, "rating": 4.3, "stars": 4, "distance": "0.5 km"},
        {"name": "Riverside Inn", "price": 540000, "rating": 4.0, "stars": 3, "distance": "1.8 km"},
        {"name": "Skyline Luxury", "price": 1250000, "rating": 4.7, "stars": 5, "distance": "0.9 km"},
    ],
}


def format_vnd(value: int) -> str:
    return f"{value:,}".replace(",", ".") + "đ"


@tool
def search_flights(origin: str, destination: str) -> str:
    """
    Tìm kiếm các chuyến bay giữa hai thành phố.
    """
    key = (origin, destination)
    reverse_key = (destination, origin)

    if key in FLIGHTS_DB:
        flights = FLIGHTS_DB[key]
    elif reverse_key in FLIGHTS_DB:
        flights = FLIGHTS_DB[reverse_key]
    else:
        return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."

    lines = [
        f"{idx+1}. {flight['airline']} - {flight['departure']} đến {flight['arrival']} - {flight['class'].capitalize()} - {format_vnd(flight['price'])}"
        for idx, flight in enumerate(flights)
    ]
    return "Kết quả tìm kiếm chuyến bay:\n" + "\n".join(lines)


@tool
def search_hotels(city: str, max_price_per_night: int = 99999999) -> str:
    """
    Tìm kiếm khách sạn theo thành phố và giá tối đa mỗi đêm.
    """
    if city not in HOTELS_DB:
        return f"Không tìm thấy khách sạn tại {city} với giá dưới {format_vnd(max_price_per_night)}/đêm."

    hotels = [hotel for hotel in HOTELS_DB[city] if hotel["price"] <= max_price_per_night]
    if not hotels:
        return f"Không tìm thấy khách sạn tại {city} với giá dưới {format_vnd(max_price_per_night)}/đêm."

    hotels.sort(key=lambda item: item["rating"], reverse=True)
    lines = [
        f"{idx+1}. {hotel['name']} - {hotel['stars']} sao - {format_vnd(hotel['price'])}/đêm - Rating {hotel['rating']} - Cách trung tâm {hotel['distance']}"
        for idx, hotel in enumerate(hotels)
    ]
    return "Kết quả tìm kiếm khách sạn:\n" + "\n".join(lines)


@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Tính toán ngân sách còn lại dựa trên chuỗi chi phí.
    """
    parsed = {}

    for part in expenses.split(","):
        if ":" not in part:
            continue
        key, value = part.split(":", 1)
        key = key.strip()
        raw_number = re.sub(r"[^0-9]", "", value)
        if not raw_number:
            continue
        parsed[key] = int(raw_number)

    if not parsed:
        return "Không có chi phí hợp lệ để tính toán. Vui lòng kiểm tra định dạng input."

    total_cost = sum(parsed.values())
    lines = [f"- {name}: {format_vnd(amount)}" for name, amount in parsed.items()]
    result = ["Bảng chi phí:", *lines, "", f"Tổng chi: {format_vnd(total_cost)}", f"Ngân sách: {format_vnd(total_budget)}"]

    if total_cost > total_budget:
        over = total_cost - total_budget
        result.append(f"Vượt ngân sách {format_vnd(over)}!")
    else:
        remaining = total_budget - total_cost
        result.append(f"Còn lại: {format_vnd(remaining)}")

    return "\n".join(result)
