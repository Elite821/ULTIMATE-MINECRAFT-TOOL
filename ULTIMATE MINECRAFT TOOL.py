from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import os, fnmatch
import os.path
import glob
#Scan 3D Stuffs
def scan3D(filename, xBanDau, yBanDau, zBanDau):

  f = open(filename, "w")

  f.write(str(SIZEX) + "," + str(SIZEY) + "," + str(SIZEZ) + "\n")
  
  for y in range(SIZEY):
      
    f.write("\n")

    for x in range(SIZEX):

      line = ""

      for z in range(SIZEZ):

        blockid = mc.getBlock(xBanDau+x, yBanDau+y, zBanDau+z)

        if line != "":
          line = line + ","

        line = line + str(blockid)

      f.write(line + "\n")

  f.close()
#Print 3D Stuffs
def print3D(filename, xBanDau, yBanDau, zBanDau):
    maze = open(filename,"r")
    thdong = maze.readlines()
    Dong1=thdong[0].split(",")
    
    x1 = int(Dong1[0])
    y1 = int(Dong1[1])
    z1 = int(Dong1[2])
    
    STTDong = 1
    
    for y in range(y1):
        STTDong += 1
    
        for x in range(x1):

            line = thdong[STTDong]
        
            DongHienThoi = line.split(",")
        
            for z in range(z1):
        
                blockid = int(DongHienThoi[z])
                mc.setBlock(xBanDau+x, yBanDau+y, zBanDau+z, blockid)
        
            STTDong += 1
    maze.close()
#The actual code
while True:
    print("")
    print("ULTIMATE MINECRAFT TOOL v1.0")
    print("Made by Quoc Viet")
    print("1. Scan3D")
    print("2. Print3D")
    print("3. Delete all data in a file")
    print("4. Search for csv files")
    print("5. Tutorials")
    print("6. Stop the program")
    option = int(input(" Select Your Option!    "))
    #Scan 3D's code
    if option == 1:
        FILENAME = str(input("Input your Filename.csv here   "))
        SIZEX = int(input("Input the x size here   "))
        SIZEY = int(input("Input the y size here   "))
        SIZEZ = int(input("Input the z size here   "))
        pos = mc.player.getTilePos()
        scan3D(FILENAME, pos.x+1, pos.y, pos.z+1)
        print("Done!")
    #Print 3D's code
    if option == 2:
        FILENAME = str(input("Input your Filename.csv here   "))
        pos = mc.player.getTilePos()
        print3D(FILENAME, pos.x+1, pos.y, pos.z+1)
        print("Done!")
    # Delete whatever that is's code
    if option == 3:
        FILENAME = str(input("Input your Filename.csv here   "))
        maze = open(FILENAME,"w")
        maze.write("")
        maze.close()
        print("Done!")
    #Search Base code
    if option == 4:
        print("1.Search all")
        print("2.Search for csv only")
        searchOption = int(input("Input your search option!   "))
        #Search All Code
        if searchOption == 1:
                filename = "*."+str(input("Input the file name here   "))
                files = glob.glob(filename)
                print("Results:")
                for i in files:
                    print(i)
        #Search CSV Code
        if searchOption == 2:
                files = glob.glob("*.csv")
                print("Results:")
                for i in files:
                    print(i)
    #Help Code
    if option == 5:
        print("What you need help with?")
        print("1. How to make a csv???")
        print("2. I want to contribute to this and help. What can i do?")
        helpOption = int(input("Input what you need help here   "))
        #When people cant seem to know how to make a csv
        if helpOption == 1:
            print("Oh.")
            print("This is pretty common in new users.")
            print("Just go to excel and make a new file,")
            print("And then click 'save as' in the menu. ")
            print("Then change the ending of the file name to .csv")
            print("Is that all you need?")
            print("1. THX")
            print("2. WAT I STILL CANT DO THIS HELP????")
            moreHelpOption = int(input("Input your answer here   "))
            #Thank god.
            if moreHelpOption == 1:
                print("No problems. Enjoy using the program!")
            #Oh. Ok
            if moreHelpOption == 2:
                print("Still cant do this? No problems. Just Copy + Paste the link below to your browser")
                print("https://lh3.googleusercontent.com/S53jVEAS6butBpnQjVEd83WvXYyz6G2RRpZqygrGIpKaie6wYXk-ylKKl9F0r1i6kYJmlg=s170")
        #When contributors want to help...
        if helpOption == 2:
            print("Well, we need people like you in the world, but if u want to contact, DM me in Discord!")
            print("EliteGame#4827")
    #Shutdown Code
    if option == 6:
        print("Thanks for using! Be sure to expect new updates soon!")
        break;
