import socket
import requests

def SendSMSTelegram(sms):

	BOTTOKEN = 'xxxx'
	BOTCHATID = 'xxxx'

	send_text = 'https://api.telegram.org/bot' + BOTTOKEN + '/sendMessage?chat_id=' + BOTCHATID + '&parse_mode=Markdown&text=' + sms
	response = requests.get(send_text)

	return response.json()

def GetIRCIp():

	IRCHOST = 'irc.chathispano.com'
	IRCPORT = 6667

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((IRCHOST, IRCPORT))
		s.send(b'NICK SlynetworkBot\r\nUSER SlynetworkBot 8 *  :.\r\n')
		data = s.recv(1024)
		#print('Received', repr(data))
		ip = 0
		while (ip == 0):
			op = data.split()[0]
			if (op == b'PING'):
				pingid=data.split()[1]
				s.send(b'PONG %b\r\n' % pingid)
				data = s.recv(1024)
				#print('Received', repr(data))
			elif (op == b'ERROR'):
				ip = data.split()[3]
				#print('Received', repr(data))
			else:
				data = s.recv(1024)
				#print('Received', repr(data))
		return ip

if __name__ == '__main__':

	while True:
		SendSMSTelegram(str(GetIRCIp()))
