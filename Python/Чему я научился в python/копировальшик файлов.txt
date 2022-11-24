filename1 = input('Какой фаил забекапить?:')
filename2 = 'backup_' + filename1

file1 = open(filename1, 'r')
file2 = open(filename2, 'w')

file2.write( file1.read())

file1.close()
file2.close() 

print('Копирование успешно завершено!') 