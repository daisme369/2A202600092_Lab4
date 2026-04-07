# [TEST CASE 1]
Bạn: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.

TravelBuddy đang suy nghĩ...
Response: Chào bạn! TravelBuddy rất vui được hỗ trợ bạn lên kế hoạch. Để mình dễ dàng gợi ý những điểm đến hấp dẫn và phù hợp nhất, bạn có thể cho mình biết thêm một chút về mong muốn của mình không?

*   Bạn dự định đi vào khoảng thời gian nào? (Ví dụ: cuối tuần này, tháng sau, mùa hè...)
một chút về mong muốn của mình không?

*   Bạn dự định đi vào khoảng thời gian nào? (Ví dụ: cuối tuần này, tháng sau, mùa hè...)
*   Bạn muốn đi mấy ngày?
*   Ngân sách dự kiến của bạn cho chuyến đi này là khoảng bao nhiêu? (Ví dụ: dưới 5 triệu, 5-10 triệu, trên 10 triệu...)
*   Bạn thích kiểu du lịch nào? (Ví dụ: nghỉ dưỡng biển, khám phá núi rừng, dạo phố phường, trải nghiệm văn hóa...)

# [TEST CASE 2]
Bạn: Giúp tôi tìm chuyến bay từ Hà Nội đi Đà Nẵng

TravelBuddy đang suy nghĩ...
Tool:search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
Response: Tuyệt vời! Từ Hà Nội đi Đà Nẵng có mấy lựa chọn cho bạn đây:

*   **Vietnam Airlines:**
    *   Chuyến 06:00 - 07:20, giá 1.450.000đ (hạng economy)
    *   Chuyến 14:00 - 15:20, giá 2.800.000đ (hạng business)
*   **VietJet Air:**
    *   Chuyến 08:30 - 09:50, giá 890.000đ (hạng economy)
*   **Bamboo Airways:**
    *   Chuyến 11:00 - 12:20, giá 1.200.000đ (hạng economy)

Bạn muốn đi vào ngày nào và có ngân sách khoảng bao nhiêu để mình tìm thêm khách sạn và tính toán tổng chi phí cho tiện nhé?


# [TEST CASE 3]
Bạn: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

TravelBuddy đang suy nghĩ...

[!] Đang gọi bộ công trợ: search_flights - Tham số: {'destination': 'Phú Quốc', 'origin': 'Hà Nội'}...

[!] Đang gọi bộ công trợ: search_hotels - Tham số: {'city': 'Phú Quốc'}...

[!] Đang gọi bộ công trợ: calculate_budget - Tham số: {'expenses': 'Chuyến bay: 1100000, Khách sạn: 3000000', 'total_budget': 5000000}...

TravelBuddy: Hành trình đề xuất: Hà Nội ✈️ Phú Quốc
Thời gian: 2 đêm (Ngày đi - Ngày về linh hoạt)

Chuyến bay tối ưu:
- VietJet Air | 16:00 - 18:15 | Giá: 1.100.000đ

Khách sạn phù hợp:
- Sol by Meliá | 4 sao | Giá: 1.500.000đ/đêm x 2 đêm

Tổng chi phí ước tính: 4.100.000đ (Chiếm 82% ngân sách của bạn).

Lý do lựa chọn (Gợi ý thêm): Sự kết hợp này giúp bạn có chuyến bay giá tốt nhất và trải nghiệm nghỉ dưỡng tại khách sạn 4 sao chất lượng, vẫn còn dư ngân sách để khám phá ẩm thực địa phương. Bạn có thể ghé thăm Chợ đêm Phú Quốc để thưởng thức hải sản tươi ngon và mua sắm quà lưu niệm. 

# [TEST CASE 4]
Bạn: Tôi muốn đặt khách sạn

TravelBuddy đang suy nghĩ...

TravelBuddy: Bạn muốn đặt khách sạn ở đâu và ngân sách của bạn cho mỗi đêm là bao nhiêu?

# [TEST CASE 5]
Bạn: Giải giúp tôi bài tập lập trình Python về Linked List

TravelBuddy đang suy nghĩ...

TravelBuddy: Xin lỗi, tôi là trợ lý TravelBuddy và chỉ có thể hỗ trợ bạn lên kế hoạch du lịch.

