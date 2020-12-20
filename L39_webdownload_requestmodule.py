import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code) # 200 means succeeded
print(len(res.text))
# print first 500 characters to validate download
print(res.text[:500])
#raise excpetion if issue downloading the file
res.raise_for_status()
#for example - uncomment  next 2 lines to see throw exception
#adRes = requests.get('http://automatetheboringstuff.com/asdfksadjf;laskjfsl;j')
#badRes.raise_for_status()
# to save locally must open in write-binary mode open(filename, 'wb')
playFile = open('RomeoAndJuliet.txt', 'wb')
# to write the download to the file need a for loop
for chunk in res.iter_content(100000): #each chunk is of the bytes data type here 100,000 as we get to define the size
    playFile.write(chunk)
playFile.close


