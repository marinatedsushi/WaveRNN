import pvleopard
import os

leopard = pvleopard.create(access_key="hBUpLSwiUywGvw96UeM5zRNQgk7nDjIJ9ClDQ2XtppVZXMFIMqXL7g==")

directory = 'C:/Users/16782/Desktop/Tate Dataset/wavs'
entries = {}
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    #print(filename)
   
    formattedFileNumber = filename[0:-4]
    f = os.path.join(directory, filename)

    if os.path.isfile(f):
        #print(f)
        transcript, words = leopard.process_file(f)
        print(formattedFileNumber + "|" + transcript + ",")





#for x in range(62):
 #   e = str(x)
 #   print(e + "|")

    