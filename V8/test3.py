import json
import ffmpeg
import cv2
# RTSP 스트림 URL
rtsp_url = 'rtsp://admin:satech1234@192.168.0.151:554/udp/av0_0'
# OpenCV VideoCapture를 사용하여 RTSP 스트림 열기
cap = cv2.VideoCapture(rtsp_url)

# VideoCapture가 열렸는지 확인
if not cap.isOpened():
    print("RTSP 스트림을 열 수 없습니다.")
    exit()

# 윈도우 생성
cv2.namedWindow('RTSP Stream', cv2.WINDOW_NORMAL)

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # 프레임 표시
    cv2.imshow('RTSP Stream', frame)

    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료 시 리소스 해제
cap.release()
cv2.destroyAllWindows()