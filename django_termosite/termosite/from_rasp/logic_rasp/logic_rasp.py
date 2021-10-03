import serial



ser = serial.Serial('/dev/ttyACM0',9600)
d = []


pattern = r"(\d{1,3}\.\d{1,2})"

float_lst = []

data = ser.readline()  #read data from serial
print(data)
    #print(type(data))
if data is not None:
        
        
        
    strdata = str(data) #его будем извлекать по 1 значению
    print("strdata - ", strdata)
                
        
        
        #print("rez - (извлеченные цифры)", rez)
        #print("rez type - ", type(rez))  #class 'list' of str
        
        
        
def main_run():  
    limit = 8 # 8 значения получаем
    n = 0
    while n < limit:
        n += 1
        
        #data2 = int(strdata)
        
        #d.append(data2)  #добавили строки в d
        #print("strdata2 - ", strdata2)

    
for go in range(2):
    #print("float_lst - перед следующей итерацией", float_lst)
    main_run()
    
    #print("float_lst - МЕжДУ ЦИКЛАМИ ФУНКЦИИ", float_lst)
 


print("ГОТОВО!")    
#with open("result_file.log", 'w') as output_file:
#    writer = csv.writer(output_file)
#    writer.writerows(d)
#    output_file.close()
#with open("result_log.log", 'w') as log:
#    print("Результат - " + str(d[0]), file=log)

    

