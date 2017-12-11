import random
import pyperclip


# txt file dirty Lists
astroTags = open('txt files/Astro.txt', 'r')
ancientTags = open('txt files/Ancient.txt', 'r')
blacknwhiteTags = open('txt files/Black and White.txt', 'r')
barTags = open('txt files/Bar.txt', 'r')
carTags = open('txt files/Cars.txt', 'r')
catTags = open('txt files/Cats.txt', 'r')
customTags = open('txt files/Custom Tags.txt', 'r')
digitalartTags = open('txt files\Digital Art.txt', 'r')
dogTags = open('txt files/Dogs.txt', 'r')
droneTags = open('txt files/Drone.txt', 'r')
fashionTags = open('txt files/Fashion.txt', 'r')
fineartTags = open('txt files/Fine Art.txt', 'r')
foodTags = open('txt files/Food.txt', 'r')
gemTags = open('txt files/Gems.txt', 'r')
glamourTags = open('txt files/Glamour.txt', 'r')
hdrTags = open('txt files/HDR.txt', 'r')
instagramTags = open('txt files/Instagram.txt', 'r')
jewelryTags = open('txt files/Jewelry.txt', 'r')
landscapeTags = open('txt files/Landscape.txt', 'r')
macroTags = open('txt files/Macro.txt', 'r')
minimalTags = open('txt files/Minimal.txt', 'r')
musicTags = open('txt files/Music.txt', 'r')
petTags = open('txt files/Pets.txt', 'r')
photographyTags = open('txt files/Photography.txt', 'r')
portraitTags = open('txt files/Portraits.txt', 'r')
saleGiveTags = open('txt files/Sale.Giveaway.txt', 'r')
saltAqTags = open('txt files/Salt Aquarium.txt', 'r')
sportTags = open('txt files/Sports.txt', 'r')
streetTags = open('txt files/Street.txt', 'r')
travelTags = open('txt files/Travel.txt', 'r')
videogameTags = open('txt files/Video Games.txt', 'r')
weddingTags = open('txt files/Wedding.txt', 'r')
wildanimalTags = open('txt files/Wild Animals.txt', 'r')
wirewrapTags = open('txt files/Wire Wrap.txt', 'r')
vaporwaveTags = open('txt files/Vaporwave.txt', 'r')

# User Inputs
userinput1 = 123
userinput2 = 123
userinput3 = 123

# Clean Lists
a1 = []
a2 = []
b1 = []
b2 = []
c1 = []
c2 = []
c3 = []
d1 = []
d2 = []
d3 = []
f1 = []
f2 = []
f3 = []
g2 = []
g1 = []
h1 = []
i1 = []
j1 = []
l1 = []
m1 = []
m2 = []
m3 = []
p1 = []
p2 = []
p3 = []
s1 = []
s2 = []
s3 = []
s4 = []
t1 = []
v1 = []
w1 = []
w2 = []
w3 = []
v2 = []
taglist = []
finalthirty = []

def intro():
    print('''
                            iG #hashTag Generator                          
                                    v2.1b
                          http://ReallyEpicShit.com''')
    print("                                  #Tags:", len(a1 + a2 + b1 + b2 + c1 + c2 + c3 + d1 + d2 + d3 + f1 + f2 + f3 + g1 +g2 + h1 + i1 + j1 + l1 + m1 + m2 + m3 + p1 + p2 + p3 + s1 + s2 + s3 + s4 + t1 + v1 + w1 + w2 + w3 + v1))
    print('''
    1: Astro           11: Glamour       21: Portraits       31: Bar
    2: Black & White   12: HDR           22: Sale/Giveaway   32: Custom Tags
    3: Cars            13: Instagram     23: Salt Aquarium   33: Ancient
    4: Cats            14: Jewelry       24: Sports          34: Gems
    5: Digital Art     15: Landscape     25: Street          35: ＶａｐｏｒＷａｖｅ
    6: Dogs            16: Macro         26: Travel          36: --------
    7: Drone           17: Minimal       27: Video Games     37: --------
    8: Fashion         18: Music         28: Wedding         38: --Time Lapse--
    9: Fine Art        19: Pets          29: Wild Animals    39: --------
    10: Food           20: Photography   30: Wire Wrap       40: ----3d printing--
    ''')

    pickCat1()

def  pickCat1():
    global userinput1
    print('Select a Number ', end='')
    try:
        userInput = int(input("~ "))
    except ValueError:
        print('Try again')
        pickCat1()

    if userInput == 1:
        userinput1 = 1
        print("Astro")
    if userInput == 2:
        userinput1 = 2
        print("Black and White")
    if userInput == 3:
        userinput1 = 3
        print("Cars")
    if userInput == 4:
        userinput1 = 4
        print("Cats")
    if userInput == 5:
        userinput1 = 5
        print("Digital Art")
    if userInput == 6:
        userinput1 = 6
        print("Dogs")
    if userInput == 7:
        userinput1 = 7
        print("Drone")
    if userInput == 8:
        userinput1 = 8
        print("Fashion")
    if userInput == 9:
        userinput1 = 9
        print("Fine Art")
    if userInput == 10:
        userinput1 = 10
        print("Food")
    if userInput == 11:
        userinput1 = 11
        print("Glamour")
    if userInput == 12:
        userinput1 = 12
        print("HDR")
    if userInput == 13:
        userinput1 = 13
        print("Instagram")
    if userInput == 14:
        userinput1 = 14
        print("Jewelry")
    if userInput == 15:
        userinput1 = 15
        print("Landscape")
    if userInput == 16:
        userinput1 = 16
        print("Macro")
    if userInput == 17:
        userinput1 = 17
        print("Minimal")
    if userInput == 18:
        userinput1 = 18
        print("Music")
    if userInput == 19:
        userinput1 = 19
        print("Pets")
    if userInput == 20:
        userinput1 = 20
        print("Photography")
    if userInput == 21:
        userinput1 = 21
        print("Portraits")
    if userInput == 22:
        userinput1 = 22
        print("Sale/Giveaway")
    if userInput == 23:
        userinput1 = 23
        print("Salt Aquarium")
    if userInput == 24:
        userinput1 = 24
        print("Sports")
    if userInput == 25:
        userinput1 = 25
        print("Street")
    if userInput == 26:
        userinput1 = 26
        print("Travel")
    if userInput == 27:
        userinput1 = 27
        print("Video Games")
    if userInput == 28:
        userinput1 = 28
        print("Wedding")
    if userInput == 29:
        userinput1 = 29
        print("Wild Animals")
    if userInput == 30:
        userinput1 = 30
        print("Wire Wrap")
    if userInput == 31:
        userinput1 = 31
        print("Bar")
    if userInput == 32:
        userinput1 = 32
        print("Custom Tags")
    if userInput == 33:
        userinput1 = 33
        print('Ancient')
    if userInput == 34:
        userinput1 = 34
        print('Gems')
    if userInput == 35:
        userinput1 = 35
        print('ＶａｐｏｒＷａｖｅ')
    elif userInput > 35:
        print('Error Nothing Here, Try Again')
        pickCat1()
    elif userInput == 0:
        print('Try Again')
        pickCat1()

    pickCat2()

def  pickCat2():
    global userinput2
    print('Select a Number(0 - Skip) ', end='')
    try:
        userInput = int(input("~ "))
    except ValueError:
        print('Try again')
        pickCat2()

    if userInput == 1:
        userinput2 = 1
        print("Astro")
    if userInput == 2:
        userinput2 = 2
        print("Black and White")
    if userInput == 3:
        userinput2 = 3
        print("Cars")
    if userInput == 4:
        userinput2 = 4
        print("Cats")
    if userInput == 5:
        userinput2 = 5
        print("Digital Art")
    if userInput == 6:
        userinput2 = 6
        print("Dogs")
    if userInput == 7:
        userinput2 = 7
        print( "Drone")
    if userInput == 8:
        userinput2 = 8
        print("Fashion")
    if userInput == 9:
        userinput2 = 9
        print("Fine Art")
    if userInput == 10:
        userinput2 = 10
        print("Food")
    if userInput == 11:
        userinput2 = 11
        print("Glamour")
    if userInput == 12:
        userinput2 = 12
        print("HDR")
    if userInput == 13:
        userinput2 = 13
        print("Instagram")
    if userInput == 14:
        userinput2 = 14
        print("Jewelry")
    if userInput == 15:
        userinput2 = 15
        print("Landscape")
    if userInput == 16:
        userinput2 = 16
        print("Macro")
    if userInput == 17:
        userinput2 = 17
        print("Minimal")
    if userInput == 18:
        userinput2 = 18
        print("Music")
    if userInput == 19:
        userinput2 = 19
        print("Pets")
    if userInput == 20:
        userinput2 = 20
        print("Photography")
    if userInput == 21:
        userinput2 = 21
        print("Portraits")
    if userInput == 22:
        userinput2 = 22
        print("Sale/Giveaway")
    if userInput == 23:
        userinput2 = 23
        print("Salt Aquarium")
    if userInput == 24:
        userinput2 = 24
        print("Sports")
    if userInput == 25:
        userinput2 = 25
        print("Street")
    if userInput == 26:
        userinput2 = 26
        print("Travel")
    if userInput == 27:
        userinput2 = 27
        print("Video Games")
    if userInput == 28:
        userinput2 = 28
        print("Wedding")
    if userInput == 29:
        userinput2 = 29
        print("Wild Animals")
    if userInput == 30:
        userinput2 = 30
        print("Wire Wrap")
    if userInput == 31:
        userinput2 = 31
        print("Bar")
    if userInput == 32:
        userinput2 = 32
        print("Custom Tags")
    if userInput == 33:
        userinput2 = 33
        print('Ancient')
    if userInput == 34:
        userinput2 = 34
        print('Gems')
    if userInput == 35:
        userinput2 = 35
        print('ＶａｐｏｒＷａｖｅ')
    if userInput == 0:
        userinput2 = 0
        print("Skip")
        pickCat3()
    elif userInput > 35:
        print('Error Nothing Here, Try Again')
        pickCat2()

    pickCat3()

def  pickCat3():
    global userinput3
    print('Select a Number(0 - Skip) ', end='')
    try:
        userInput = int(input("~ "))
    except ValueError:
        print('Try again')
        pickCat3()
    if userInput == 1:
        userinput3 = 1
        print("Astro")
    if userInput == 2:
        userinput3 = 2
        print("Black and White")
    if userInput == 3:
        userinput3 = 3
        print("Cars")
    if userInput == 4:
        userinput3 = 4
        print("Cats")
    if userInput == 5:
        userinput3 = 5
        print("Digital Art")
    if userInput == 6:
        userinput3 = 6
        print("Dogs")
    if userInput == 7:
        userinput3 = 7
        print("Drone")
    if userInput == 8:
        userinput3 = 8
        print("Fashion")
    if userInput == 9:
        userinput3 = 9
        print("Fine Art")
    if userInput == 10:
        userinput3 = 10
        print("Food")
    if userInput == 11:
        userinput3 = 11
        print("Glamour")
    if userInput == 12:
        userinput3 = 12
        print("HDR")
    if userInput == 13:
        userinput3 = 13
        print("Instagram")
    if userInput == 14:
        userinput3 = 14
        print("Jewelry")
    if userInput == 15:
        userinput3 = 15
        print("Landscape")
    if userInput == 16:
        userinput3 = 16
        print("Macro")
    if userInput == 17:
        userinput3 = 17
        print("Minimal")
    if userInput == 18:
        userinput3 = 18
        print("Music")
    if userInput == 19:
        userinput3 = 19
        print("Pets")
    if userInput == 20:
        userinput3 = 20
        print("Photography")
    if userInput == 21:
        userinput3 = 21
        print("Portraits")
    if userInput == 22:
        userinput3 = 22
        print("Sale/Giveaway")
    if userInput == 23:
        userinput3 = 23
        print("Salt Aquarium")
    if userInput == 24:
        userinput3 = 24
        print("Sports")
    if userInput == 25:
        userinput3 = 25
        print("Street")
    if userInput == 26:
        userinput3 = 26
        print("Travel")
    if userInput == 27:
        userinput3 = 27
        print("Video Games")
    if userInput == 28:
        userinput3 = 28
        print("Wedding")
    if userInput == 29:
        userinput3 = 29
        print("Wild Animals")
    if userInput == 30:
        userinput3 = 30
        print("Wire Wrap")
    if userInput == 31:
        userinput3 = 31
        print("Bar")
    if userInput == 32:
        userinput3 = 32
        print("Custom Tags")
    if userInput == 33:
        userinput3 = 33
        print('Ancient')
    if userInput == 34:
        userinput3 = 34
        print('Gems')
    if userInput == 35:
        userinput3 = 35
        print('ＶａｐｏｒＷａｖｅ')
    if userInput == 0:
        userinput3 = 0
        print("Skip")
        loadlists()
    elif userInput > 35:
        print('Error Nothing Here, Try Again')
        pickCat3()


    loadlists()

def loadtxts():
    global a1
    global a2
    global b1
    global b2
    global c1
    global c2
    global c3
    global d1
    global d2
    global d3
    global f1
    global f2
    global f3
    global g2
    global g1
    global h1
    global i1
    global j1
    global l1
    global m1
    global m2
    global m3
    global p1
    global p2
    global p3
    global s1
    global s2
    global s3
    global s4
    global t1
    global v1
    global w1
    global w2
    global w3
    global v2
    global totalTags
    for eachLine in astroTags:
        tag = eachLine.strip()
        a1.append(tag)
    for eachLine in blacknwhiteTags:
        tag = eachLine.strip()
        b1.append(tag)
    for eachLine in carTags:
        tag = eachLine.strip()
        c1.append(tag)
    for eachLine in catTags:
        tag = eachLine.strip()
        c2.append(tag)
    for eachLine in digitalartTags:
        tag = eachLine.strip()
        d1.append(tag)
    for eachLine in dogTags:
        tag = eachLine.strip()
        d2.append(tag)
    for eachLine in droneTags:
        tag = eachLine.strip()
        d3.append(tag)
    for eachLine in fashionTags:
        tag = eachLine.strip()
        f1.append(tag)
    for eachLine in fineartTags:
        tag = eachLine.strip()
        f2.append(tag)
    for eachLine in foodTags:
        tag = eachLine.strip()
        f3.append(tag)
    for eachLine in glamourTags:
        tag = eachLine.strip()
        g1.append(tag)
    for eachLine in hdrTags:
        tag = eachLine.strip()
        h1.append(tag)
    for eachLine in instagramTags:
        tag = eachLine.strip()
        i1.append(tag)
    for eachLine in jewelryTags:
        tag = eachLine.strip()
        j1.append(tag)
    for eachLine in landscapeTags:
        tag = eachLine.strip()
        l1.append(tag)
    for eachLine in macroTags:
        tag = eachLine.strip()
        m1.append(tag)
    for eachLine in minimalTags:
        tag = eachLine.strip()
        m2.append(tag)
    for eachLine in musicTags:
        tag = eachLine.strip()
        m3.append(tag)
    for eachLine in petTags:
        tag = eachLine.strip()
        p1.append(tag)
    for eachLine in photographyTags:
        tag = eachLine.strip()
        p2.append(tag)
    for eachLine in portraitTags:
        tag = eachLine.strip()
        p3.append(tag)
    for eachLine in saleGiveTags:
        tag = eachLine.strip()
        s1.append(tag)
    for eachLine in saltAqTags:
        tag = eachLine.strip()
        s2.append(tag)
    for eachLine in sportTags:
        tag = eachLine.strip()
        s3.append(tag)
    for eachLine in streetTags:
        tag = eachLine.strip()
        s4.append(tag)
    for eachLine in travelTags:
        tag = eachLine.strip()
        t1.append(tag)
    for eachLine in videogameTags:
        tag = eachLine.strip()
        v1.append(tag)
    for eachLine in weddingTags:
        tag = eachLine.strip()
        w1.append(tag)
    for eachLine in wildanimalTags:
        tag = eachLine.strip()
        w2.append(tag)
    for eachLine in wirewrapTags:
        tag = eachLine.strip()
        w3.append(tag)
    for eachLine in barTags:
        tag = eachLine.strip()
        b2.append(tag)
    for eachLine in customTags:
        tag = eachLine.strip()
        c3.append(tag)
    for eachLine in ancientTags:
        tag = eachLine.strip()
        a2.append(tag)
    for eachLine in gemTags:
        tag = eachLine.strip()
        g2.append(tag)
    for eachLine in vaporwaveTags:
        tag = eachLine.strip()
        v2.append(tag)

    intro()

def loadlists():
    global userinput1
    global userinput2
    global userinput3
    global taglist
    if userinput1 == 1:
        taglist = taglist + a1
    if userinput1 == 2:
        taglist = taglist + b1
    if userinput1 == 3:
        taglist = taglist + c1
    if userinput1 == 4:
        taglist = taglist + c2
    if userinput1 == 5:
        taglist = taglist + d1
    if userinput1 == 6:
        taglist = taglist + d2
    if userinput1 == 7:
        taglist = taglist + d3
    if userinput1 == 8:
        taglist = taglist + f1
    if userinput1 == 9:
        taglist = taglist + f2
    if userinput1 == 10:
        taglist = taglist + f3
    if userinput1 == 11:
        taglist = taglist + g1
    if userinput1 == 12:
        taglist = taglist + h1
    if userinput1 == 13:
        taglist = taglist + i1
    if userinput1 == 14:
        taglist = taglist + j1
    if userinput1 == 15:
        taglist = taglist + l1
    if userinput1 == 16:
        taglist = taglist + m1
    if userinput1 == 17:
        taglist = taglist + m2
    if userinput1 == 18:
        taglist = taglist + m3
    if userinput1 == 19:
        taglist = taglist + p1
    if userinput1 == 20:
        taglist = taglist + p2
    if userinput1 == 21:
        taglist = taglist + p3
    if userinput1 == 22:
        taglist = taglist + s1
    if userinput1 == 23:
        taglist = taglist + s2
    if userinput1 == 24:
        taglist = taglist + s3
    if userinput1 == 25:
        taglist = taglist + s4
    if userinput1 == 26:
        taglist = taglist + t1
    if userinput1 == 27:
        taglist = taglist + v1
    if userinput1 == 28:
        taglist = taglist + w1
    if userinput1 == 29:
        taglist = taglist + w2
    if userinput1 == 30:
        taglist = taglist + w3
    if userinput1 == 31:
        taglist = taglist + b2
    if userinput1 == 32:
        taglist = taglist + c3
    if userinput1 == 33:
        taglist = taglist + a2
    if userinput1 == 34:
        taglist = taglist + g2
    if userinput1 == 35:
        taglist = taglist + v2
        #### 2 ####
    if userinput2 == 0:
        taglist = taglist
    if userinput2 == 1:
        taglist = taglist + a1
    if userinput2 == 2:
        taglist = taglist + b1
    if userinput2 == 3:
        taglist = taglist + c1
    if userinput2 == 4:
        taglist = taglist + c2
    if userinput2 == 5:
        taglist = taglist + d1
    if userinput2 == 6:
        taglist = taglist + d2
    if userinput2 == 7:
        taglist = taglist + d3
    if userinput2 == 8:
        taglist = taglist + f1
    if userinput2 == 9:
        taglist = taglist + f2
    if userinput2 == 10:
        taglist = taglist + f3
    if userinput2 == 11:
        taglist = taglist + g1
    if userinput2 == 12:
        taglist = taglist + h1
    if userinput2 == 13:
        taglist = taglist + i1
    if userinput2 == 14:
        taglist = taglist + j1
    if userinput2 == 15:
        taglist = taglist + l1
    if userinput2 == 16:
        taglist = taglist + m1
    if userinput2 == 17:
        taglist = taglist + m2
    if userinput2 == 18:
        taglist = taglist + m3
    if userinput2 == 19:
        taglist = taglist + p1
    if userinput2 == 20:
        taglist = taglist + p2
    if userinput2 == 21:
        taglist = taglist + p3
    if userinput2 == 22:
        taglist = taglist + s1
    if userinput2 == 23:
        taglist = taglist + s2
    if userinput2 == 24:
        taglist = taglist + s3
    if userinput2 == 25:
        taglist = taglist + s4
    if userinput2 == 26:
        taglist = taglist + t1
    if userinput2 == 27:
        taglist = taglist + v1
    if userinput2 == 28:
        taglist = taglist + w1
    if userinput2 == 29:
        taglist = taglist + w2
    if userinput2 == 30:
        taglist = taglist + w3
    if userinput2 == 31:
        taglist = taglist + b2
    if userinput2 == 32:
        taglist = taglist + c3
    if userinput2 == 33:
        taglist = taglist + a2
    if userinput2 == 34:
        taglist = taglist + g2
    if userinput1 == 35:
        taglist = taglist + v2

        #### 3 ####
    if userinput3 == 0:
        taglist = taglist
    if userinput3 == 1:
        taglist = taglist + a1
    if userinput3 == 2:
        taglist = taglist + b1
    if userinput3 == 3:
        taglist = taglist + c1
    if userinput3 == 4:
        taglist = taglist + c2
    if userinput3 == 5:
        taglist = taglist + d1
    if userinput3 == 6:
        taglist = taglist + d2
    if userinput3 == 7:
        taglist = taglist + d3
    if userinput3 == 8:
        taglist = taglist + f1
    if userinput3 == 9:
        taglist = taglist + f2
    if userinput3 == 10:
        taglist = taglist + f3
    if userinput3 == 11:
        taglist = taglist + g1
    if userinput3 == 12:
        taglist = taglist + h1
    if userinput3 == 13:
        taglist = taglist + i1
    if userinput3 == 14:
        taglist = taglist + j1
    if userinput3 == 15:
        taglist = taglist + l1
    if userinput3 == 16:
        taglist = taglist + m1
    if userinput3 == 17:
        taglist = taglist + m2
    if userinput3 == 18:
        taglist = taglist + m3
    if userinput3 == 19:
        taglist = taglist + p1
    if userinput3 == 20:
        taglist = taglist + p2
    if userinput3 == 21:
        taglist = taglist + p3
    if userinput3 == 22:
        taglist = taglist + s1
    if userinput3 == 23:
        taglist = taglist + s2
    if userinput3 == 24:
        taglist = taglist + s3
    if userinput3 == 25:
        taglist = taglist + s4
    if userinput3 == 26:
        taglist = taglist + t1
    if userinput3 == 27:
        taglist = taglist + v1
    if userinput3 == 28:
        taglist = taglist + w1
    if userinput3 == 29:
        taglist = taglist + w2
    if userinput3 == 30:
        taglist = taglist + w3
    if userinput3 == 31:
        taglist = taglist + b2
    if userinput3 == 32:
        taglist = taglist + c3
    if userinput3 == 33:
        taglist = taglist + a2
    if userinput3 == 34:
        taglist = taglist + g2
    if userinput1 == 35:
        taglist = taglist + v2

    choosetags()

def choosetags():
    global finalthirty
    num_to_select = 30  # set the number to select here.
    list_of_random_items = random.sample(taglist, num_to_select)
    finalthirty = list_of_random_items[0:30]

    displaytags()

def displaytags():
    global finalthirty
    str1 = ' '.join(finalthirty)
    pyperclip.copy(str1)
    print('')
    print(finalthirty)
    print('\n#hashTags Copied To Clipboard!')

    rerun()

def rerun():
    global taglist
    print('\nRestart? y/n', end='')
    userInput = (input("~ "))
    if userInput == 'y':
        taglist = []
        intro()
    if userInput == 'n':
        exit()
    else:
        print('Try again')
        rerun()


loadtxts()
input()
