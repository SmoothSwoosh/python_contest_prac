import base64, struct


#read packet and decode it from base85
packet = str.encode(input())
decoded_bytes = base64.b85decode(packet)

#split decoded bytes by bytes. For example: b'\x04\x05\x06' = [b'\x04', b'\x05', b'\x06']
splitted_by_bytes = [decoded_bytes[i:i+1] for i in range(len(decoded_bytes))] 

#iterate over splitted bytes extracting field sizes
#until 0 is occured (the end of header)
field_sizes = []
for byte in splitted_by_bytes:
    size = int.from_bytes(byte, byteorder='big', signed=True)
    
    if size == 0:
        break
    
    field_sizes.append(size)

#extract the body from packet
fields = decoded_bytes[len(field_sizes)+1:]

#calculate number of fields in packet
num_of_fields = len(fields) // sum(abs(size) for size in field_sizes)

#build format to unpack fields values
int_to_format = {1: 'B', -1: 'b', 2: 'H', -2: 'h', \
                 4: 'I', -4: 'i', 8: 'Q', -8: 'q'}
fmt = '>' + ''.join(int_to_format[size] for size in field_sizes) * num_of_fields

#calculate sum of fields values
sum_of_fields = sum(struct.unpack(fmt, fields))

print(sum_of_fields)
