import cv2
import ffmpeg

# RTSP 스트림 URL
rtsp_url = 'rtsp://admin:satech1234@192.168.0.151:554/udp/av0_0'

# FFmpeg로 RTSP 스트림 열기
input_stream = ffmpeg.input(rtsp_url, rtsp_transport='udp')  # rtsp_transport 인수 추가

# FFmpeg로 영상 디코딩
output_stream = ffmpeg.output(input_stream, 'pipe:', format='rawvideo', pix_fmt='bgr24')

# FFmpeg 실행
#ffmpeg_process = ffmpeg.run(output_stream, pipe_stdout=True, input=input_stream, vcodec='copy')  # input 및 vcodec 인수 추가
ffmpeg_process = ffmpeg.run(output_stream, pipe_stdout=True, quiet=True, overwrite_output=True, input=input_stream)

# OpenCV를 사용하여 영상 디스플레이
while True:
    # FFmpeg에서 프레임 읽기
    in_bytes = ffmpeg_process.stdout.read(1920 * 1080 * 3)  # 적절한 프레임 크기로 수정

    if not in_bytes:
        break

    # 바이트 데이터를 NumPy 배열로 변환
    frame = cv2.imdecode(np.frombuffer(in_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)

    # 영상 디스플레이
    cv2.imshow('RTSP Stream', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# OpenCV 창 닫기 및 FFmpeg 프로세스 종료
cv2.destroyAllWindows()
ffmpeg_process.stdout.close()
ffmpeg_process.wait()
