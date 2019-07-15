import pandas as pd
import threading
import argparse
import socket
import numpy
import logging
import concurrent.futures
import ast
import time
import random
from threading import Thread
import threading
import pymysql.cursors
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

ap = argparse.ArgumentParser()
ap.add_argument("-m1", "--matrix1", required=True)
ap.add_argument("-m2", "--matrix2", required=True)
ap.add_argument("-p", "--productors", required=True)
ap.add_argument("-c", "--clientes", required=True)
ap.add_argument("-b", "--buffer", required=True)

args = vars(ap.parse_args())

# CATCHING ARGUMENTS
m1=str(args["matrix1"])
m2=str(args["matrix2"])
p=int(args["productors"])
c=int(args["clientes"])
b=int(args["buffer"])

mutex = threading.Semaphore(1)
fillCount = threading.Semaphore()
emptyCounter = threading.Semaphore(b)
onlyone = threading.Semaphore()



def sendtosql(fila, columna, resultado, tiempo, thread):
    # Connect to the database
    onlyone.acquire()
    #print("Ingresa a sendtosql")
    conn = pymysql.connect(host='localhost',
            user='root',
            password='______',
            db='database_name',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    try:
        cursor = conn.cursor()
         # Create a new record
        sql = """UPDATE resul SET resultado = resultado + %s, tiempo = %s + tiempo WHERE fila = %s AND columna = %s;"""
        data = (resultado, tiempo, fila, columna, )
        cursor.execute(sql, data)
        #print ("Record Updated successfully ")
        conn.commit()
    except:
        print("Failed to update records to database, thread ",name )
        conn.rollback()
    finally:
    #closing database connection.
        cursor.close()
        conn.close()
        #print("Connection was closed")
    onlyone.release()


def productores_ft(name):
    while True:
        emptyCounter.acquire()
        mutex.acquire()
        try:
            task=tasks[0]
            tasks.pop(0)
        except:
            task=""
        mutex.release()
        if task=="":
            time.sleep(2)
        else:
            index = task[2]
            for i in range(len(task[0])):
                valma = task[0][i]
                valmb = task[1][i]
                #print("INDEX.    ", index, "valma ", valma, "valmb ", valmb, "i.  ", i, "thread. ", name)
            # LOG OPERATION MADE 
                print("Thread PRODUCTOR %s: (%s, %s) INDEX %s" % (name, valma, valmb, index))
                tlist = [valma, valmb, index]
                buffer_ready.append(tlist)
                #print("This is the tlist", tlist)
                #print("Buffer list", buffer_ready, "\n")
        fillCount.release()

def consumidor_ft(name):
    listd = []
    while True:
        fillCount.acquire()
        mutex.acquire()
        start_time = time.time()
        try:
            task=buffer_ready[0]
            buffer_ready.pop(0)
            #print("This is the task", task)
        except:
            task=""
        mutex.release()
        if task=="":
            time.sleep(2)
        else:
            valma = task[0]
            valmb = task[1]
            index = task[2]
            res = valma * valmb
            # LOG OPERATION MADE 
            print("Thread CONSUMIDOR %s: (%s, %s) = %s INDEX %s" % (name, valma, valmb, res, index))
            etime = time.time() - start_time
            sendtosql(index[0], index[1], res, etime, name)
        emptyCounter.release()

if __name__ == "__main__":
    global tasks, buffer_ready
    # dataframes initialization
    df1=pd.read_csv(m1+'.csv',header=None)
    df2=pd.read_csv(m2+'.csv',header=None)
    tasks = []
    buffer_ready = []

    # TASK CREATION
    for i in range(len(df1)):
        for j in range(len(df2)):
            tasks.append([list(df1.iloc[i]),list(df2[j]),[i,j]])
    #print(tasks)
    # THREADS INITIALIZATION
    consumidores=[]
    productores=[]

    for i in range(p):
        x = threading.Thread(target=productores_ft, args=(i,))
        productores.append(x)
        x.start()

    for i in range(c):
        y = threading.Thread(target=consumidor_ft, args=(i,))
        consumidores.append(y)
        y.start()

    for i in productores:
        i.join()
    print("Ended Productores...")

    for j in consumidores:
        j.join()
    print("Ended Consumidores...")

    print("All Threads done exiting")
