filelist = ["myfile.txt", "myprogram.exe", "yourfile.txt"]
for filename in filelist: 
    if ".txt" in filename:
        print(filename)
    else:
        print("Alert! Alert! We are under attack!")
    
        