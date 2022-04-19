import numpy as np
from PIL import Image, ImageDraw


def IMG0(filename1,filename2,outputfile):
    try:
        img1=Image.open(filename1)
        img2=Image.open(filename2)
    except OSError:
        print(" cannot open img")
        return 1

    imarr1=np.array(img1)
    imarr2=np.array(img2)

    ishape1=imarr1.shape
    ishape2=imarr2.shape

    if ishape1!= ishape2:
        print("Different sizes")
        return 2
    for i in range (ishape1[0]):
        for j in range (ishape1[1]):
            if  (int(imarr1[i][j][0])+int(imarr1[i][j][1])+int(imarr1[i][j][2]))!= (int(imarr2[i][j][0])+int(imarr2[i][j][1])+int(imarr2[i][j][2]) and (int(imarr1[i][j][0])+int(imarr1[i][j][1])+int(imarr1[i][j][2]))!=0 ):
                brdiff=(int(imarr2[i][j][0])+int(imarr2[i][j][1])+int(imarr2[i][j][2]))/(int(imarr1[i][j][0])+int(imarr1[i][j][1])+int(imarr1[i][j][2]))
                imarr1[i][j][0]=int(imarr1[i][j][0]*brdiff)
                imarr1[i][j][1]=int(imarr1[i][j][1]*brdiff)
                imarr1[i][j][2]=int(imarr1[i][j][2]*brdiff)
            else:
                imarr1[i][j][0]=0
                imarr1[i][j][1]=0
                imarr1[i][j][2]=0

    outimage=Image.fromarray(imarr1)
    outimage.save(outputfile)

#filename1=input("Введите имя первого файла\n")
#filename2=input("Введите имя второго файла\n")
#outputfile=input("Введите файла для записи\n")

IMG0("55.jpg","34.jpg","1.jpg")
