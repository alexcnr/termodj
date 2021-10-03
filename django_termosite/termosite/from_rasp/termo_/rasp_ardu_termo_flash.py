#import RPi.GPIO as GPIO
#import time, datetime
import serial
import re
import csv
import sqlite3, datetime


#GPIO.setmode(GPIO.BCM)
#GPIO.setup(12, GPIO.OUT)

import RPi.GPIO as GPIO

#import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
#GPIO.setup(12, GPIO.OUT)           # set GPIO 12 as an output



conn = sqlite3.connect('tempdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Results')

        

cur.execute('''CREATE TABLE Results
        (temp_C REAL, temp_K REAL, temp_F REAL, humidity REAL, data_timer TEXT) ''')



ser = serial.Serial('/dev/ttyACM0',9600)
d = []


pattern = r"(\d{1,3}\.\d{1,2})"

float_lst = []

def convert_data(text):
    """ИЗВЛЕКАЕМ ТОЛЬКО ЦИФРЫ ИЗ ПОТОКА"""
        
    result = re.findall(pattern, text) #list
    #print(type(result))

    return result


def listconnect(lstlst):
    """ОБЪЕДИНЯЕМ СПИСОК СПИСКОВ В 1 СПИСОК ЗНАЧЕНИй"""
    all=[]
    for lst in lstlst:
        all.extend(lst)
    return all


def receive_data():
 
    data = ser.readline()  #read data from serial
    #print(data)
    #print(type(data))
    if data is not None:
        
        strdata = str(data) #его будем извлекать по 1 значению
        #print("strdata - ", strdata)
                
        rez = convert_data(strdata)
        
        #print("rez - (извлеченные цифры)", rez)
        #print("rez type - ", type(rez))  #class 'list' of str
        
        
        return rez
 
def main_run():  
    limit = 4 # 4 значения получаем
    n = 0
    while n < limit:
        n += 1
    
        strdata2 = receive_data()
        d.append(strdata2)  #добавили строки в d
        #print("strdata2 - ", strdata2)
        #print("d   -   ", d)
        v = listconnect(d) #получили 1 список строк
        #print("v   -   ", v)
        
    for x in v:
    
        float_lst.append(float(x))
        
    #print ("float_lst СРАЗУ ПОСЛЕ ДОБАВЛЕНИЯ", float_lst)
    
    row = cur.fetchone()
    
    dtimer = datetime.datetime.now()
    #date_time = datetime.datetime.today()
    #date_time = date_time.strftime("%Y-%m-%d; %H.%M.%S")
    #print(dtimer)
    

    if row is None:
        cur.execute('''INSERT INTO Results (temp_C, temp_K, temp_F, humidity, data_timer)
             VALUES (?, ?, ?, ?, ?)''', (float_lst[0], float_lst[1], float_lst[2], float_lst[3], dtimer) )
        
        
        #####  сюда еСли боЛьшЕ тЕмпЕрАТуРА, чЕМ..., ТО зАжЕЧЬ ДИОД нА РАСПР
        #if float_lst[0] > 30.0:
         #   print("Высокая температура!")
        GPIO.setwarnings(False)
            #GPIO.setmode(GPIO.BOARD)
          #  GPIO.setup(12, GPIO.OUT)

           # for hot in range(1): 
            #    GPIO.output(12, True)
             #   time.sleep(0.5)
              #  GPIO.output(12, False)
            #    time.sleep(0.5)
        #GPIO.cleanup()
#import RPi.GPIO as GPIO            # import RPi.GPIO module  
#from time import sleep             # lets us have a delay  
#GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
#GPIO.setup(24, GPIO.OUT)           # set GPIO24 as an output
#try:  
#    while True:  
#        GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
#        sleep(0.5)                 # wait half a second  
#        GPIO.output(24, 0)         # set GPIO24 to 0/GPIO.LOW/False  
#        sleep(0.5)                 # wait half a second  
  
#except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
#    GPIO.cleanup()                 # resets all GPIO ports used by this program              
         
    conn.commit()
    
    
    #SELECT temp_C FROM Results WHERE Value == 36.2 
    
    #SELECT temp_C FROM Results where > 36.6
    
    
    float_lst.clear()
    d.clear()
    v.clear()

    #SELECT * FROM Results WHERE humidity ='50';
    

    
for go in range(720):
    #измеряем 12 часов 1 раз в 60 секунд
    #print("float_lst - перед следующей итерацией", float_lst)
    main_run()
    
    #print("float_lst - МЕжДУ ЦИКЛАМИ ФУНКЦИИ", float_lst)
 

conn.commit()
cur.close()

print("ГОТОВО!")    
#with open("result_file.log", 'w') as output_file:
#    writer = csv.writer(output_file)
#    writer.writerows(d)
#    output_file.close()
#with open("result_log.log", 'w') as log:
#    print("Результат - " + str(d[0]), file=log)

    

