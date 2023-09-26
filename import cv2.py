import cv2
import os

# Tên tệp video và thư mục đầu ra
video_file = 'animals.mp4' 
output_folder = 'frames'

# Tạo thư mục đầu ra nếu nó chưa tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Mở tệp video
cap = cv2.VideoCapture(video_file)

# Đếm số lượng khung hình
frame_count = 0
while True:
    # Đọc khung hình từ video
    ret, frame = cap.read()
    
    # Kiểm tra xem đã đọc hết video chưa
    if not ret:
        break
    
    # Kiểm tra xem khung hình có rỗng không trước khi lưu
    if not frame.empty():
        # Lưu khung hình vào thư mục đầu ra
        frame_filename = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg') 
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

# Đóng tập video và thông báo khi hoàn thành
cap.release()
cv2.destroyAllWindows()
print(f'Phân rã thành {frame_count} khung hình và lưu vào thư mục {output_folder}.')