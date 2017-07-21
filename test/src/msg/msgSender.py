from twilio.rest import Client
import os,time
k=1
while k <2:
    now_time=time.strftime('%Y-%m-%d %H-%M-%S')
    print("开始运行脚本:")

    # Your Account SID from twilio.com/console
    account_sid = "ACb043a1986fe80818a7af8aff50c1955f"
    # Your Auth Token from twilio.com/console
    auth_token = "0dfa7d3951701e4516b421502609b0bb"

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+8613594632344",
        from_="+14156108429",
        body="xiaojiejie")

    print(message.sid)

    print("运行完成退出")
    time.sleep(1)