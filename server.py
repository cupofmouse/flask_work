from flask import Flask, request, render_template
from Converting_img import convert_img

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    result_path=None
    if request.method == 'POST':
        file = request.files['image']
        #request는 사용자에게 받는 http요청의 모든 정보를 다양한 방식으로
        #접근할 수 있게 해준다, request.files: 사용자가 파일 업로드시 전송된 파일 데이터에 접근한다
        n_colors=int(request.form.get('n_colors', 5))
        #request.form: POST방식의 html폼 데이터에 접근한다.
        input_path=f"static/uploads/{file.filename}"
        output_path=f"static/processed/{file.filename}"
        file.save(input_path)
        convert_img(input_path, output_path, n_colors)

        result_path='/'+output_path
    return render_template('index.html', result_path=result_path)
    #render_template는 html등 템플릿 파일을 서버에 렌더링하여 결과생성, 반환한다.
    #templates폴더에 있는 html파일을 가져온다.
    #두번째인자부턴 html에 넘겨줄 변수(데이터)를 전달한다.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
