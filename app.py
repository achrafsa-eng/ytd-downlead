from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        video_url = request.form['text']
        try:
            yt = YouTube(video_url)
            video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            video.download(output_path='/your/actual/file/path')  
            return 'تم تنزيل الفيديو بنجاح!'
        except Exception as e:
            return f'حدث خطأ: {str(e)}'

if __name__ == '_main_':
    app.run(debug=True)