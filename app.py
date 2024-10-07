from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# 各手順の番号に対応する単語リスト
step1_words = ['La', 'Il', 'The', 'Fandango', 'Ferrari']
step2_words = ['Maranello', 'Modena', 'Italia', 'Fiorano', 'Monza', 'Tifosi', 'Cavalino', 'Testa', 'Rossa', 'Ferrari']
step4_words = ['Stradale', 'Scuderia', 'Pista', 'Competizione', 'Turismo', 'XX', 'GTB', 'Aperta', 'GTO', 'Anniversario']
step5_words = ['Superfast', 'Ultraquick', 'Veloceboss', 'Grandespeed', 'Moltowhoosh']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        num3 = int(request.form['num3'])
        num4 = int(request.form['num4'])
        num5 = int(request.form['num5'])

        if not (1 <= num1 <= 5):
            raise ValueError("1～5の間で入力してください。")
        if not (1 <= num2 <= 10):
            raise ValueError("1～10の間で入力してください。")
        if not (249 <= num3 <= 999):
            raise ValueError("249～999の間で入力してください。")
        if not (1 <= num4 <= 10):
            raise ValueError("1～10の間で入力してください。")
        if not (1 <= num5 <= 5):
            raise ValueError("1～5の間で入力してください。")

        # 各ステップで選ばれた単語を取得
        word1 = step1_words[num1 - 1]
        word2 = step2_words[num2 - 1]
        word4 = step4_words[num4 - 1]
        word5 = step5_words[num5 - 1]

        result = f"{word1} {word2} {num3} {word4} {word5}です！"
        return render_template('index.html', result=result)
    except ValueError as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
