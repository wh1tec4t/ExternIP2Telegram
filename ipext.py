import socket
import requests

def SendSMSTelegram(sms):

	BOTTOKEN = 'XXXXXX'
	BOTCHATID = 'XXXX'

	send_text = 'https://api.telegram.org/bot' + BOTTOKEN + '/sendMessage?chat_id=' + BOTCHATID + '&parse_mode=Markdown&text=' + sms
	response = requests.get(send_text)

	return response.json()

def GetIRCIp():

	IRCHOST = 'xxxx'
	IRCPORT = 6667

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

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
				ip_fin = data.split()[3]

			if (ip_ini == 0):
				data = s.recv(1024)
				ip_ini = data.split()[9]

			data = s.recv(1024)

		return (str(ip_fin) + "-->" + str(ip_ini))

if __name__ == '__main__':

	while True:
		SendSMSTelegram(GetIRCIp())
