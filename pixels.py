#!/usr/bin/python
import os
def main():
    XRES = 500
    YRES = 500
    MAXCOLOR = 256
    #s= ""
    if os.path.exists("pixels.ppm"):
        os.remove("pixels.ppm")
    f = open("pixels.ppm", "w+")
    f.write("P3" + " " + str(XRES) + " " + str(YRES) + " " + str(MAXCOLOR) + "\n")
    #s ="P3" + XRES + YRES + MAXCOLOR + "\n"
    for i in range(YRES):
      #  print "1"
        for j in range(XRES):
      #      s += j%MAXCOLOR + " " + j%MAXCOLOR + " " + j%MAXCOLOR + " "
            f.write(str(pow(j, 2)%MAXCOLOR) + " " + str(pow(j, 3)%MAXCOLOR) + " " + str(pow(j, 4)%MAXCOLOR) + " ")
            j = j+1
       #     print "2"
     #   s += "\n"
        f.write("\n")
    f.close()
    #print s


main()
    
