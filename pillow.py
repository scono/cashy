from PIL import Image

def get_sub_pics(path):
    while True:
        try:
            im = Image.open(path)
            break
        except PermissionError:
            pass
        except OSError:
            pass

    if 'IMG' in path:
        box_frage = (42, 245, 550, 370) #Frage
        box_1 = (88, 482, 485, 529) #erste Antwort
        box_2 = (88, 600, 485, 650) #zweite Antwort
        box_3 = (88, 722, 485, 780) #dritte Antwort
        box_nummer = (40, 133, 160, 168) #Nummer
    else:
        box_frage = (25, 130, 390, 260) #Frage
        box_1 = (50, 310, 310, 350) #erste Antwort
        box_2 = (50, 390, 310, 430) #zweite Antwort
        box_3 = (50, 470, 310, 510) #dritte Antwort
        box_nummer = (25, 90, 110, 108) #Nummer

    frage       = im.crop(box_frage)
    antwort1    = im.crop(box_1)
    antwort2    = im.crop(box_2)
    antwort3    = im.crop(box_3)
    nummer      = im.crop(box_nummer)

    path_frage = r'C:\Users\Max\Desktop\cashshow\temp\frage.png'
    path_a1 = r'C:\Users\Max\Desktop\cashshow\temp\antwort1.png'
    path_a2 = r'C:\Users\Max\Desktop\cashshow\temp\antwort2.png'
    path_a3 = r'C:\Users\Max\Desktop\cashshow\temp\antwort3.png'
    path_nr = r'C:\Users\Max\Desktop\cashshow\temp\nummer.png'
    
    frage.save(path_frage)
    antwort1.save(path_a1)
    antwort2.save(path_a2)
    antwort3.save(path_a3)
    nummer.save(path_nr)

    return path_frage, path_a1, path_a2, path_a3, path_nr

if __name__ == "__main__":
    pass