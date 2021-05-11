from flask import Flask, render_template
app = Flask(__name__)

@app.route('/a')
def hello():
    return render_template()

@app.route('/b')
def hello2():
    return 'Hello, World!bbbbbbbbbb'
@app.route('/naver')
def naver():
    return '안녕 나는 네이버야~'

@app.route('/taxi')
def taxi():
    return ''' 
    <!DOCTYPE html>
    <html>
    <body>

    <h2>모범택시</h2>
    <img src="https://img2.sbs.co.kr/img/sbs_cms/WE/2021/04/05/fNJ1617581491817.jpg" alt="모범택시" width="500" height="333">

    </body>
    </html>
    '''
# 웹브라우저에 http://127.0.0.1:5000/naver 
# 위와같이 접속 하면 안녕 나는 네이버야~
# 라는 글자를 나타나게 하시오

if __name__ == '__main__':
    app.run()