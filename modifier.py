import os


file = open('./requirements.txt')
lines = file.readlines()
modified_lines = []

for line in lines:
    line = line.split('==')[0]
    modified_lines.append(line+'\n')

file.close()
os.remove('./requirements.txt')

modified_file = open('./requirements.txt', 'w')
modified_file.writelines(modified_lines)
modified_file.close()