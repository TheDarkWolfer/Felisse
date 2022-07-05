from flask import Flask, render_template, Response, redirect
import cv2, numpy, socket

# web_image_processor = image_processor(flipframe=False,imshow=False,key=None)

app = Flask(__name__)

static_back = numpy.array
detection_threshold = 5000
motion = 0
current_feed = 0

camera = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            frame = cv2.flip(frame,1)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

print(f"IP address > {socket.gethostbyname(socket.gethostname())}")

https = False
debug = False
if __name__ == "__main__" and https == True:
    app.run(debug=debug,ssl_context='adhoc',host="0.0.0.0")
elif __name__ == "__main__" and https == False:
    app.run(debug=debug,host="0.0.0.0")