import os

#pfad =r'C:\Users\Max\Desktop\cashshow\bilder'
pfad =r'C:\Users\Max\Documents\Apowersoft\Windows ApowerMirror'

def get_path():
    while len(os.listdir(pfad)) <= 0:
        pass
    return pfad + '\\' + os.listdir(pfad)[0]

def hist_file(pic_path, nr_str, flag):
    dest_path = r'C:\Users\Max\Desktop\cashshow\hist\\' + str(nr_str) + r'.png'  
    if flag == True:
        os.rename(pic_path, dest_path)
    else:
        os.remove(pic_path)

if __name__ == "__main__":
    pass