import socket
import requests

def SendSMSTelegram(sms):

	BOTTOKEN = 'XXXXXX'
	BOTCHATID = 'xxxx'

	send_text = 'https://api.telegram.org/bot' + BOTTOKEN + '/sendMessage?chat_id=' + BOTCHATID + '&parse_mode=Markdown&text=' + sms
	response = requests.get(send_text)

	return response.json()

def GetIRCIp():

	IRCHOST = 'irc.slynetwork.es'
	IRCPORT = 6667
	BOTNICK = None

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

		# Anti Zoombie Nick
		if (BOTNICK == b'nick1'):
			BOTNICK == b'nick2'
		else:
			BOTNICK = b'nick1'

		ip_ini = 0
		ip_fin = 0

		s.connect((IRCHOST, IRCPORT))
		s.send(b'NICK %b\r\nUSER SlynetworkBot 8 *  :.\r\n' % BOTNICK)

		data = s.recv(1024)

		while (ip_fin == 0):

			op = data.split()[0]
			if (op == b'PING'):
				pingid=data.split()[1]
				s.send(b'PONG %b\r\n' % pingid)

			if (op == b'ERROR'):
				ip = data.split()[3]
				ip_fin = ip.split(b'@')[1]
				SendSMSTelegram("Disconnected - Old IP was: " + str(ip_fin[:-1]))

			if (ip_ini == 0):
				data = s.recv(1024)
				ip = data.split()[9]
				ip_ini = ip.split(b'@')[1]
				SendSMSTelegram("Connected - New IP is: " + str(ip_ini))

			data = s.recv(1024)

if __name__ == '__main__':
	while True: GetIRCIp()
