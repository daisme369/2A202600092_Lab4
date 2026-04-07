from langchain_core.tools import tool
import json


FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1450000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2800000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1200000, "class": "economy"},
    ],

    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2100000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1350000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1100000, "class": "economy"},
    ],

    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1600000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1300000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3200000, "class": "business"},
    ],

    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1300000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780000, "class": "economy"},
    ],

    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1100000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650000, "class": "economy"},
    ],
}


HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1800000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1200000, "area": "Mỹ Khê", "rating": 4.3},
        {"name": "Fivitel Danang", "stars": 3, "price_per_night": 650000, "area": "Sơn Trà", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250000, "area": "Hải Châu", "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 2, "price_per_night": 350000, "area": "An Thượng", "rating": 4.7},
    ],

    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3500000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1500000, "area": "Bãi Trường", "rating": 4.2},
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800000, "area": "Dương Đông", "rating": 4.0},
        {"name": "Station Hostel", "stars": 2, "price_per_night": 200000, "area": "Dương Đông", "rating": 4.5},
    ],

    "Hồ Chí Minh": [
        {"name": "Rex Hotel", "stars": 5, "price_per_night": 2800000, "area": "Quận 1", "rating": 4.3},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1400000, "area": "Quận 1", "rating": 4.1},
        {"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550000, "area": "Quận 3", "rating": 4.4},
        {"name": "The Common Room", "stars": 2, "price_per_night": 180000, "area": "Quận 1", "rating": 4.6},
    ],
}

def format_price(price):
    return f"{int(price):,.0f}".replace(',', '.') + "đ"

@tool
def search_flights(origin: str, destination: str) -> str:
    """
    Tìm kiếm các chuyến bay giữa hai thành phố.
    Tham số:
        - origin: thành phố khởi hành
        - destination: thành phố đến
    Trả về danh sách chuyến bay với hãng, giờ bay, giá vé.
    Nếu không tìm thấy chuyến bay, trả về thông báo không có chuyến.
    """
    flights = FLIGHTS_DB.get((origin, destination))
    if not flights:
        flights = FLIGHTS_DB.get((destination, origin))
        
    if not flights:
        return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."
        
    result = []
    for f in flights:
        price_str = format_price(f['price'])
        result.append(f"{f['airline']} | {f['departure']} - {f['arrival']} | Giá: {price_str} | Hạng: {f['class']}")
        
    return "\n".join(result)

@tool
def search_hotels(city: str, max_price_per_night: int = 99999999) -> str:
    """
    Tìm kiếm các khách sạn tại một thành phố.
    Tham số:
        - city: thành phố
        - max_price_per_night: giá tối đa mỗi đêm (VNĐ), mặc định không giới hạn
    Trả về danh sách khách sạn với tên, sao, giá phòng, khu vực, đánh giá.
    Nếu không tìm thấy khách sạn, trả về thông báo không có khách sạn.
    """
    hotels = HOTELS_DB.get(city, [])
    
    # Lọc theo giá
    filtered_hotels = [h for h in hotels if h["price_per_night"] <= max_price_per_night]
    
    if not filtered_hotels:
        price_str = format_price(max_price_per_night)
        return f"Không tìm thấy khách sạn tại {city} với giá dưới {price_str}/đêm. Hãy thử tăng ngân sách."
        
    # Sắp xếp theo rating giảm dần
    filtered_hotels.sort(key=lambda x: x["rating"], reverse=True)
    
    result = []
    for h in filtered_hotels:
        price_str = format_price(h['price_per_night'])
        result.append(f"{h['name']} | {h['stars']} sao | {h['area']} | Rating: {h['rating']} | Giá: {price_str}/đêm")
        
    return "\n".join(result)

@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Tính toán ngân sách còn lại sau khi trừ các khoản chi phí.
    Tham số:
        - total_budget: tổng ngân sách ban đầu
        - expenses: chuỗi mô tả các khoản chi, cách nhau bởi dấu ","
        
        định dạng 'tên_khoản: số_tiền'
        trả về bảng chi tiết các khoản chi và ngân sách còn lại
        nếu vượt quá ngân sách, trả về thông báo ngân sách không đủ
    """
    try:
        total_expenses = 0
        expenses_dict = {}
        if expenses.strip():
            expenses_list = expenses.split(",")
            for expense in expenses_list:
                expense = expense.strip()
                if not expense:
                    continue
                expense_name, expense_amount = expense.split(":")
                val = int(expense_amount.strip())
                expenses_dict[expense_name.strip()] = val
                total_expenses += val
                
        remaining = total_budget - total_expenses
        
        lines = ["Bảng chi phí:"]
        for name, amount in expenses_dict.items():
            lines.append(f"  - {name}: {format_price(amount)}")
            
        lines.append("  ---")
        lines.append(f"  Tổng chi: {format_price(total_expenses)}")
        lines.append(f"  Ngân sách: {format_price(total_budget)}")
        lines.append(f"  Còn lại: {format_price(remaining)}")
        
        if remaining < 0:
            lines.append(f"Vượt ngân sách {format_price(abs(remaining))}! Cần điều chỉnh.")
            
        return "\n".join(lines)
        
    except Exception as e:
        return f"Lỗi định dạng expenses: {e}. Vui lòng nhập đúng định dạng 'tên_khoản:số_tiền, ...' (VD: 'Vé máy bay:2000000, Khách sạn:1500000')"

