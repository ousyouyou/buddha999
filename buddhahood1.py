#!/usr/bin/python 
import cgi 
import cgitb 
import random
import hashlib

cgitb.enable() 
form = cgi.FieldStorage() 
print("Content-Type: text/html") 
print() 
print('<html>')
print('<head><title>成仏度診断</title></head>')
print('<body>') 
print('<h1 style="color:#9000ff">あなたの成仏度を診断！</h1>')
print('<p>あなたはどのくらい成仏の素質があるのかを診断しましょう〜</p>')
print('<form action="./buddhahood1.py" method="POST">') 
print('氏名: <input type="text" name="fn">') 
print('<input type="submit">') 
print('</form>') 

if "fn" not in form : 
   print("<p>氏名を入力してください。</p>") 
   rate = 0
else: 
   fn=form["fn"].value 
   if fn == '釈迦':
      rate1 = 1000
   else:
      hashed = hashlib.md5(fn.encode()).hexdigest()
      digit = int(hashed[0],16)%10
      rate1 = digit+random.randint(72,99)
   print('<p>Hello, %s </P>' % (fn)) 
   print('武蔵野から見ると君の成仏度は'+str(rate1)+'%です')

print('<br><br><br>')
print('<a href="https://twitter.com/intent/tweet?related=muds.gdl&amp;text=武蔵野から見ると私の成仏度は'+str(rate1)+'%25です%0A%23あなたの成仏度診断 https://muds.gdl.jp/~s2122011/buddhahood1.py " target="_blank" class="twitter-link loginbtn lbt ga_tweet"> 診断結果をツイートする！</a>')
print('<br>')
print('<p class="header_followbtn_area" style="color:#9000ff">Web環境におけるソーシャルサービス構築開発演習をやって<br><a class="tw-follow-btn" href="https://twitter.com/" target="_blank">Xtwitter</a><a class="threads-follow-btn" href="https://www.threads.net/" target="_blank"><img src="https://d28qudu5i15bto.cloudfront.net/images/threads_logo.png" alt="Threads" width="20"> Threads</a><a class="misskey-follow-btn" href="https://misskey.io/" target="_blank"><img src="https://d28qudu5i15bto.cloudfront.net/images/misskey_logo.png" alt="misskeyロゴ" height="20"> Misskey</a><a class="taittsu-follow-btn" href="https://taittsuu.com/" target="_blank"><img src="https://d28qudu5i15bto.cloudfront.net/images/taitsu_logo.png" alt="タイッツーロゴ" height="20"> タイッツー</a></p>')
print('<br><br><br>')
print('<iframe src=“https://docs.google.com/presentation/d/e/2PACX-1vRlvJ9s9OjrECUrkOO5qjXERsrCl7Bqdam3dw05rR28eQrT6oqjTeYGSqQDvv6bwGJu7UgiGWrDtUFT/embed?start=false&loop=true&delayms=5000” frameborder=“0" width=“480” height=“299" allowfullscreen=“true” mozallowfullscreen=“true” webkitallowfullscreen=“true”></iframe>')
print('</body></html') 