import sys, struct


positions = {'Size': slice(4, 8), 'Type': slice(20, 22), \
			'Channels': slice(22, 24), 'Rate': slice(24, 28), \
			'Bits': slice(34, 36), 'Data size': slice(40, 44)}

size_to_format = {2: 'H', 4: 'I'}

wav = sys.stdin.buffer.read()

header = wav[8:12].decode()
if header != 'WAVE':
	print('NO')
	sys.exit()

info = {}
for key, value in positions.items():
	size = value.stop - value.start
	try:
		info[key] = struct.unpack(size_to_format[size], wav[value])[0]
	except:
		print('NO')
		break
else:
	print(', '.join(f'{key}={value}' for key, value in info.items()))