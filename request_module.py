import requests

res = requests.get('https://shakespeare.folger.edu/downloads/pdf/romeo-and-juliet_PDF_FolgerShakespeare.pdf')
#Get command will download the file in the URL.
# res.status code: This will give a HTML error/success code depending on the result

res.raise_for_status()
#This will raise an exception if the script fails.
#Program will stop working if an error occures.

playFile= open('RomeandJuliet2.txt', 'wb')

# You can save the file or webpage to your hard drive with this function.wb stands for write binary.

for chunck in res.iter_content(100000): # Chunck stands for the text in the webpage.Chunck stands for byte data type.
    playFile.write(chunck)

playFile.close()
