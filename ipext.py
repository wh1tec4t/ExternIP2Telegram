import socket
import requests

def SendSMSTelegram(sms):

	BOTTOKEN = 'foo'
	BOTCHATID = 'bar'

	send_text = 'https://api.telegram.org/bot' + BOTTOKEN + '/sendMessage?chat_id=' + BOTCHATID + '&parse_mode=Markdown&text=' + sms
	response = requests.get(send_text)
	return response.json()

def GetIRCIp():

	IRCHOST = 'irc.chathispano.com'
	IRCPORT = 6667

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((IRCHOST, IRCPORT))
		s.send(b'NICK Calambrazos\r\nUSER Calambrazos 8 *  :.\r\n')
		data = s.recv(1024)
		print('Received', repr(data))
		ip = 0
		while (ip == 0):
			op = data.split()[0]
			if (op == b'PING'):
				pingid=data.split()[1]
				s.send(b'PONG %b\r\n' % pingid)
				data = s.recv(1024)
				print('Received', repr(data))
			elif (op == b'ERROR'):
				ip = data.split()[4]
				print('Received', repr(data))
				SendSMSTelegram(ip)
			else:
				data = s.recv(1024)
				print('Received', repr(data))

if __name__ == '__main__':
	GetIRCIp()
