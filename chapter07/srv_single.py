#!/home/aaron/geo_env python3
#Foundations of Python Network Programming, Third Edition
#https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/srv_single.py
#Single_threaded server that servers one client at a time; others must wait.


import zen_utils


if __name__ == '__main__':
	address = zen_utils.parse_command_line('simple single_threaded server')
	listener = zen_utils.create_srv_socket(address)
	zen_utils.accept_connections_forever(listener)

