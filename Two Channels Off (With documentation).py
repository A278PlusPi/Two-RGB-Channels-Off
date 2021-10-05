#Anthony John Regner (anthonyjohn.regner61@myhunter.cuny.edu)
#Two Channels Off - extension of Assignment 40
#Completion: 7/22/2021

#Before you start, I am letting you that my program only accepts 24-bit images (no alpha channel).
#If you want my program to accept 32-bit images with alpha channel, change the following:

#Change from: copiesmany = np.ones((length*rows, width*columns, 3))
#    To this: copiesmany = np.ones((length*rows, width*columns, 4))

#Step 1: The program imports the libraries before doing anything else
import matplotlib.pyplot as plt
import numpy as np

#Step 2: The program asks us for an image file, specifically PNG. The users doesn't have to include .png
#        since we appended .png to the end of the image name.
#Step 3: The program reads the PNG file.
#Note:   If the program didn't find the requested file, the "except" portion of the code will run.

name = input("What image did you want to open? We have appended .png at the end of each file name, so you don't have to.")
try:
    image = plt.imread(name+".png")
except FileNotFoundError:
    print("We can't find the file you are looking for.")
    print("Tip: This program only recognizes files within your working directory.")

else:
    
#Step 4: The program asks us to specify a number of rows and columns
#Note 2: If the rows and columns aren't at least one each, the program will ask them again to specify a number of rows and columns.
#Note 3: The program will warn the users if the image size is too large (>10000 pixels each)
    
#Step 5: The program will print the image size to help the user decide whether one should continue or not.

    rows = int(input("How many rows?"))
    columns = int(input("How many columns?"))

    while rows < 1 or columns < 1:
        print("Both the rows and columns must be at least one")
        rows = int(input("How many rows?"))
        columns = int(input("How many columns?"))

    length = image.shape[0]
    width = image.shape[1]

    print("The image size will be: ("+str(length*rows)+" by "+str(width*columns)+").")
    
    if length * rows > 10000 or width * columns > 10000:
        confirm1 = input("The image will be very large! Are you really sure you want to continue?!")
    else:
        confirm1 = input("Do you want to continue?")

    if confirm1 == "Yes" or confirm1 == "Y":
        
#Step 6: The program will create a new image, which is the size of the image times by the number of
#        rows and columns we specified.
#Step 7: The program stores the new image into a variable called "copiesmany"

        copiesmany = np.ones((length*rows, width*columns, 3))

#Step 8: With a nested for loop, the programs makes as many copies of the image specified by us.

        for i in range(0,rows):
            for j in range(0,columns):
                copiesmany[i*length:(i+1)*length, j*width:(j+1)*width, :] = image

#Step 9: The program tells us that there are (rows*columns) copies of our image.
#Step 10: The program shows us a collage of many copies of our image.

        print("There are " + str(rows*columns) + " copies of your image.")
        plt.imshow(copiesmany)		                 
        plt.show()

#Step 11: The program asks us what two color channels we want to erase.
#Note 4:  The program may skip one or both of the processes if the number of rows and/or columns are set to 1.
        
#Step 12: The program stores our input into variables called "erasecor1" and "erasecor2"

        if rows > 1:
            erasecor1 = input("What color do you want to erase? Red, green, or blue?")
        if columns > 1:
            erasecor2 = input("What other color do you want to erase? Red, green, or blue?")

#Step 13: To be flexible with our inputs, the program makes all inputs uppercase.
#Step 14: The program stores our uppercase inputs into new variables called "ecor1" and "ecor2".

        if rows > 1:
            ecor1 = erasecor1.upper()
        if columns > 1:  
            ecor2 = erasecor2.upper()

#Step 15: If ecor1 and ecor2 matches the specified inputs (full color or shorthand), then the program
#         assigns ecor1 and ecor2 new integer values (0 = red, 1 = green, 2 = blue)

        if rows > 1:
            if ecor1 == "RED" or ecor1 == "R":
                ecor1 = int(0)
            if ecor1 == "GREEN" or ecor1 == "G":
                ecor1 = int(1)
            if ecor1 == "BLUE" or ecor1 == "B":
                ecor1 = int(2)

        if columns > 1:
            if ecor2 == "RED" or ecor2 == "R":
                ecor2 = int(0)
            if ecor2 == "GREEN" or ecor2 == "G":
                ecor2 = int(1)
            if ecor2 == "BLUE" or ecor2 == "B":
                ecor2 = int(2)

#Step 16: The program sets cor1values and cor2values equal to one.
#Step 17: The program makes a copy of the copiesmany image, and assigns it to a new variable called color.

        cor1value = 1
        cor2value = 1
        color = copiesmany.copy()

#Step 18: The program will iterate two for loops where two color channels of their choice would gradually be erased.
#         The first for loop will gradually erase their first color in each row by decrementing the cor1value -> 1/(rows-1)
#         The last row (rows-1) will assign the cor1value to zero to prevent errors.
#         The same procedure will occur as the first for loop, but for each column instead.
    
        for i in range(1,rows):
            if i == (rows-1):
                cor1value = 0;
            else:
                cor1value -= 1/(rows-1)
            color[i*length:(i+1)*length, :, ecor1] *= cor1value

        for j in range(1,columns):
            if j == (columns-1):
                cor2value = 0;
            else:
                cor2value -= 1/(columns-1)
            color[:, j*width:(j+1)*width, ecor2] *= cor2value

#Step 19: The program will show the image with two of the three color channels being gradually removed.
        plt.imshow(color)		                 
        plt.show()

#Step 20: The program will determine the new file name, depending on the number of rows and columns, and color channels
#         that are removed. If there is only one image (itself), the file name will remain the same.

        if rows > 1 and columns > 1:
            savename = (name+" ("+str(rows)+"x"+str(columns)+") off("+str(ecor1)+","+str(ecor2)+").png")
        elif rows > 1:
            savename = (name+" ("+str(rows)+"x"+str(columns)+") off("+str(ecor1)+").png")
        elif columns > 1:
            savename = (name+" ("+str(rows)+"x"+str(columns)+") off("+str(ecor2)+").png")
        else:
            savename = name

#Step 21: The program asked the user if one wants to save the new image?
#Step 22: If the user prompted "Yes" or "Y", then the image is saved into their working directory.
        
        confirm2 = input("Do you want to save as "+savename+"?")

        if confirm2 == "Yes" or confirm2 == "Y":
            plt.imsave(savename, color)
            print("Image saved.")

        else:
            print("Image not saved.")
