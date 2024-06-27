from flask import Flask, request, render_template

app = Flask(__name__)


# シーザー暗号のエンコード処理
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result


# シーザー暗号のデコード処理
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form.get('text')
        shift = int(request.form.get('shift'))
        operation = request.form.get('operation')

        if operation == 'encrypt':
            result = caesar_encrypt(text, shift)
        else:
            result = caesar_decrypt(text, shift)

        return render_template('index.html', result=result)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000)
