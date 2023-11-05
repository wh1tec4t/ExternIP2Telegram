import socket
import requests
import time


def SendSMSTelegram(sms):

	BOTTOKEN = 'XXXXXX'
	BOTCHATID = 'xxxx'

	send_text = 'https://api.telegram.org/bot' + BOTTOKEN + '/sendMessage?chat_id=' + BOTCHATID + '&parse_mode=Markdown&text=' + sms
	response = requests.get(send_text)

	return response.json()


def GetIRCIp():

	IRCHOST = 'xxxx'
	IRCPORT = 6667

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

		# Espera 3' a que el nick zoombie anterior salga por ping timeout en caso de reconexion abrupta.
		time.sleep(180)

		ip_ini = 0
		ip_fin = 0

		s.connect((IRCHOST, IRCPORT))
		s.send(b'NICK SlynetworkBot\r\nUSER SlynetworkBot 8 *  :.\r\n')

		data = s.recv(1024)

		while (ip_fin == 0):

			op = data.split()[0]
			if (op == b'PING'):
				pingid=data.split()[1]
				s.send(b'PONG %b\r\n' % pingid)

			if (op == b'ERROR'):
				ip = data.split()[3]
				ip_fin = ip.split("@")[1]
				SendSMSTelegram("Disconnected - Old IP was: " + str(ip_fin))

			if (ip_ini == 0):
				data = s.recv(1024)
				ip = data.split()[9]
				ip_ini = ip.split("@")[1]
				SendSMSTelegram("Connected - New IP is: " + str(ip_ini))

			data = s.recv(1024)


if __name__ == '__main__':
	GetIRCIp()
