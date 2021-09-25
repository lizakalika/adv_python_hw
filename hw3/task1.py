with open('textfile.txt','r') as file:
    data = file.readlines()

for i in range(len(data)):
    line = data[i].split('')
    data[i] = ' '.join(line)
    
print(''.join(data))
