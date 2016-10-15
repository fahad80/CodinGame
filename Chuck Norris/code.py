
msg_str = input("Enter your msg: ")
print (' '.join(format(ord(x), 'b') for x in msg_str))
encoded_msg = []
count = 0
zero_flag = False
one_flag  = False

for msg_byte in msg_str:
    msg_byte_bin =  bin(int.from_bytes(msg_byte.encode(), 'big'))
    msg_byte_bin = msg_byte_bin[2:]

    if(len(msg_byte_bin)<7):
        msg_byte_bin = '0' + msg_byte_bin
    
    for msg_byte_bit in msg_byte_bin:
        if msg_byte_bit == '0':
            if one_flag == True:
                for i in range(count):
                    encoded_msg.append("0")
                encoded_msg.append(" ")
                count = 0
                one_flag  = False
                    
            count += 1
            if zero_flag == False:
                encoded_msg.append("00 ")
                zero_flag = True
            
        else:
            if zero_flag == True:
                for i in range(count):
                    encoded_msg.append("0")
                encoded_msg.append(" ")
                count = 0
                zero_flag  = False
                    
            count += 1
            if one_flag == False:
                encoded_msg.append("0 ")
                one_flag = True
                
for i in range(count):
    encoded_msg.append("0")


print(''.join(encoded_msg))

