import socket
import sys

def main():
	stand_page_number = 132
	command_sent = 0
	#posture_file = open("../cat_robot_posture.txt", "r")
	robot_info = {}
	command_list = {}
	# Open jimmy info file and create dictionary
	# Currently this project only uses one robot
	with open("robot_info.txt","r") as fin:
		for line in fin:
			line = line.strip('\n')
			parts = line.split(',')
			temp = {}
			temp['host'] = parts[1]
			temp['port'] = int(parts[2])
			robot_info[parts[0]] = temp
	
	print robot_info
	previous_data = 99
	
	response = "a"

	# result.txt is the output file of the OpenCV C++ program, it will
	# contain the command number to be sent over to the robot
	while response != "q":
		command_file = open("result.txt", "r")
		data = command_file.readline()
		command_file.close()

		try:
			if int(data) != previous_data:
				command_sent = 0
				previous_data = data
		except:
			pass
		
		host = temp['host']
		HOST = '{}'.format(host)
		PORT = temp['port'] 
		
		try:
			# Try to open a UDP connection, and send the command to the robot
			if int(command_sent) == 0:
				sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				# 3 is the command used by Motion script to play a page number from RME,
				# this could be extended to send other kinds of commands as well, such as walk
				# or turn. Assign stand_page_number above for what page number you want to send over
				command = "%d" % (data)
				sock.sendto(command, (HOST, PORT))
				print HOST
				print PORT
				print "Sent:     %s" % (command)
				command_sent = 1
		except:
			pass


if __name__ == "__main__":
	main()
