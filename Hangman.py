
'''
HANGMAN BY AMARDEEP SINGH
2018
'''

#imports
from random import *
from graphics import *
from button import*

'''
this function returns letters cliked on the graphical keyboard
'''
def getLetter(pt,win,quitButton,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,one,two,three,four,five,six,seven,eight,nine,zero):
    # loop so you can clike anywhere and it wont crash
    while not quitButton.clicked(pt):
        #variable for the letter it will returned
        letter=""
        #mouse click for buttons
        pt = win.getMouse()
        #there is a button for each letter and number when it is clicked it is deactivaited
        #so it cant be clicked again
        if a.clicked(pt):
            letter="a"
            a.deactivate()
        elif b.clicked(pt):
            letter="b"
            b.deactivate()
        elif c.clicked(pt):
            letter="c"
            c.deactivate()
        elif d.clicked(pt):
            letter="d"
            d.deactivate()
        elif e.clicked(pt):
            letter="e"
            e.deactivate()
        elif f.clicked(pt):
            letter="f"
            f.deactivate()
        elif g.clicked(pt):
            letter="g"
            g.deactivate()
        elif h.clicked(pt):
            letter="h"
            h.deactivate()
        elif i.clicked(pt):
            letter="i"
            i.deactivate()
        elif j.clicked(pt):
            letter="j"
            j.deactivate()
        elif k.clicked(pt):
            letter="k"
            k.deactivate()
        elif l.clicked(pt):
            letter="l"
            l.deactivate()
        elif m.clicked(pt):
            letter="m"
            m.deactivate()
        elif n.clicked(pt):
            letter="n"
            n.deactivate()
        elif o.clicked(pt):
            letter="o"
            o.deactivate()
        elif p.clicked(pt):
            letter="p"
            p.deactivate()
        elif q.clicked(pt):
            letter="q"
            q.deactivate()
        elif r.clicked(pt):
            letter="r"
            r.deactivate()
        elif s.clicked(pt):
            letter="s"
            s.deactivate()
        elif t.clicked(pt):
            letter="t"
            t.deactivate()
        elif u.clicked(pt):
            letter="u"
            u.deactivate()
        elif v.clicked(pt):
            letter="v"
            v.deactivate()
        elif w.clicked(pt):
            letter="w"
            w.deactivate()
        elif x.clicked(pt):
            letter="x"
            x.deactivate()
        elif y.clicked(pt):
            letter="y"
            y.deactivate()
        elif z.clicked(pt):
            letter="z"
            z.deactivate()
        elif one.clicked(pt):
            letter="1"
            one.deactivate()
        elif two.clicked(pt):
            letter="2"
            two.deactivate()
        elif three.clicked(pt):
            letter="3"
            three.deactivate()
        elif four.clicked(pt):
            letter="4"
            four.deactivate()
        elif five.clicked(pt):
            letter="5"
            five.deactivate()
        elif six.clicked(pt):
            letter="6"
            six.deactivate()
        elif seven.clicked(pt):
            letter="7"
            seven.deactivate()
        elif eight.clicked(pt):
            letter="8"
            eight.deactivate()
        elif nine.clicked(pt):
            letter="9"
            nine.deactivate()
        elif zero.clicked(pt):
            letter="0"
            zero.deactivate()
        else:
            letter=""
        #if the letter is not the same as it started ""
        #then it will return
        if letter != "":
            letter = letter.upper()
            return letter
    win.close()

'''
this function creats the dashed out word
'''
def getWordfill(word):
    wordfill = []
    for ch in word:
        if ch == " ":
            #since i used underscores with spaces already in between them a regular space must be
            #twice as big to look normal
            wordfill.append("  ")
        elif ch == "'":
            wordfill.append("'")
        elif ch == "&":
            wordfill.append("&")
        elif ch == ".":
            wordfill.append(".")
        elif ch == ",":
            wordfill.append(",")
        elif ch == "-":
            wordfill.append("-")
        else:
            #each letter is an underscore seperated by a space
            wordfill.append("_ ")
    return wordfill

'''
this function prompts the user to try again when they finish a game
'''
def tryagain(win):
    win.setCoords(0, 0, 100, 100)
    cover=Rectangle(Point(0,0), Point(100,45))
    cover.setFill('white')
    cover.draw(win)
    trytxt=Text(Point(50,30),"Do you want to play again?")
    trytxt.setSize(15)
    trytxt.setStyle('bold')
    trytxt.draw(win)
    yes = Button(win, Point(35,15), 10,10, "YES")
    yes.activate()

    no = Button(win, Point(65,15), 10,10, "NO")
    no.activate()


    trya=True
    while trya:
        pt=win.getMouse()
        if yes.clicked(pt):
            win.close()
            main()
            trya=False
        elif no.clicked(pt):
            win.close()
            trya=False
        else:
            trya=True

'''
This function runs the main while loop which checks if the game is ove or not
'''
def getWin(wordfill,word,lives):
    wordfill = "".join(wordfill)
    word=word.replace(" ","  ")
    if word == wordfill:
        return False
    elif lives == 0:
        return False
    else:
        return True

'''
this fuction displays if the player wins or looses on the end screen
'''
def checkWin(wordfill,word,lives,win,):
    win.setCoords(0, 0, 100, 100)
    wordfill = "".join(wordfill)
    if word == wordfill:
        wordtxt=Text(Point(50,95),"YOU WIN\n You gussed the word:{0}".format(word))
        wordtxt.setStyle('bold')
        wordtxt.draw(win)
    elif lives == 0:
        wordtxt=Text(Point(50,90),"YOU LOOSE\n The word is:{0}".format(word))
        wordtxt.setStyle('bold')
        wordtxt.draw(win)

'''
this function subtracts from the lives
'''
def getLives(spot,lives,win):
    if spot==[]:
        lives=lives-1
    return lives

'''
this function finds the spot of the letter to replace
'''
def findLetter(word,letr):
    count=-1
    spot=""

    for c in word:
        count+= 1
        if c == letr:
            spot=spot+str(count)+" "
    spot=spot.split()

    for i in range(len(spot)):
        spot[i]=int(spot[i])

    return spot

'''
this function draws the hangman with gif images
'''
def drawMan(lives,lvl,win):
    if lvl == "easy":
        if lives==10:
            hangimg = Image(Point(5.5,7),"manstart.gif")
        elif lives==9:
            hangimg = Image(Point(5.5,7),"man9.gif")
        elif lives==8:
            hangimg = Image(Point(5.5,7),"man8.gif")
        elif lives==7:
            hangimg = Image(Point(5.5,7),"man7.gif")
        elif lives==6:
            hangimg = Image(Point(5.5,7),"man6.gif")
        elif lives==5:
            hangimg = Image(Point(5.5,7),"man5.gif")
        elif lives==4:
            hangimg = Image(Point(5.5,7),"man4.gif")
        elif lives==3:
            hangimg = Image(Point(5.5,7),"man3.gif")
        elif lives==2:
            hangimg = Image(Point(5.5,7),"man2.gif")
        else:
            hangimg = Image(Point(5.5,7),"man1.gif")
    elif lvl == "mid":
        if lives==7:
            hangimg = Image(Point(5.5,7),"manstart.gif")
        elif lives==6:
            hangimg = Image(Point(5.5,7),"man6.gif")
        elif lives==5:
            hangimg = Image(Point(5.5,7),"man5.gif")
        elif lives==4:
            hangimg = Image(Point(5.5,7),"man4.gif")
        elif lives==3:
            hangimg = Image(Point(5.5,7),"man3.gif")
        elif lives==2:
            hangimg = Image(Point(5.5,7),"man2.gif")
        else:
            hangimg = Image(Point(5.5,7),"man1.gif")
    else:
        if lives==5:
            hangimg = Image(Point(5.5,7),"manstart.gif")
        elif lives==4:
            hangimg = Image(Point(5.5,7),"man6.gif")
        elif lives==3:
            hangimg = Image(Point(5.5,7),"man5.gif")
        elif lives==2:
            hangimg = Image(Point(5.5,7),"man3.gif")
        else:
            hangimg = Image(Point(5.5,7),"man1.gif")

    hangimg.draw(win)

'''
this function updates the word when its letters are guessed
'''
def updatewordfill(spot,wordfill,letr):
    for i in range(len(spot)):
        wordfill[spot[i]]=letr
    return wordfill

'''
thisfunction prompts users to choose a catagory for their words
'''
def catagories(win):
    cattxt=Text(Point(50,50),"Select Category")
    cattxt.setSize(25)
    cattxt.setStyle('bold')
    cattxt.draw(win)
    Movie = Button(win, Point(25,25), 15,15, "MOVIES")
    Movie.activate()
    Car = Button(win, Point(75,75), 15,15, "CARS")
    Car.activate()
    Countries = Button(win, Point(25,75), 15,15, "COUNTRIES")
    Countries.activate()
    Colour = Button(win, Point(75,25), 15,15, "COLOURS")
    Colour.activate()
    quitButton = Button(win, Point(10,1), 5, 5, "Quit")
    quitButton.activate()
    listname=""
    while listname=="":
        pt = win.getMouse()
        listname=""
        if Movie.clicked(pt):
            listname="movies.txt"
            Movie.deactivate()
        elif Car.clicked(pt):
            listname="cars.txt"
            Car.deactivate()
        elif Countries.clicked(pt):
            listname="countries.txt"
            Countries.deactivate()
        elif Colour.clicked(pt):
            listname="colours.txt"
            Colour.deactivate()
        elif quitButton.clicked(pt):
            win.close()
        else:
            listname=""
    cover=Rectangle(Point(-5,1000), Point(1000,-5))
    cover.setFill('white')
    cover.draw(win)
    return listname

'''
this function gets a random word from the lists
'''
def getWord(win):
    listname=catagories(win)
    infile = open(listname,'r')
    #makes a list of all the words in a file
    #we talked about using readline but decided this is more efficient
    t = infile.read()
    #split on each line because each line is a new word
    WORDLIST = t.split("\n")
    #random pick
    realword = WORDLIST[randrange(0,len(WORDLIST))]
    word = realword.upper()
    return word
    infile.close()


'''
this funtion alowes user to choose the difficulty by changing the amount of lives they get
'''
def level(win):
    lvltxt=Text(Point(50,90),"Select Difficulty")
    lvltxt.setSize(25)
    lvltxt.setStyle('bold')
    lvltxt.draw(win)

    Easy = Button(win, Point(50,60),20,10,"EASY")
    Easy.activate()
    Medium = Button(win, Point(50,40),20,10,"MEDIUM")
    Medium.activate()
    Hard = Button(win, Point(50,20),20,10,"HARD")
    Hard.activate()
    quitButton = Button(win, Point(10,1), 5, 5, "Quit")
    quitButton.activate()
    lives=0
    while lives==0:
        pt = win.getMouse()
        if Easy.clicked(pt):
            lives=10    #all of the face
            lvl="easy"
            Easy.deactivate()
        elif Medium.clicked(pt):
            lives=7    #just body seperatly
            lvl="mid"
            Medium.deactivate()
        elif Hard.clicked(pt):
            lives=5    #body parts come together like both arms at once
            lvl="hard"
            Hard.deactivate()
        elif quitButton.clicked(pt):
            win.close()
        else:
            lives=0
    cover=Rectangle(Point(-5,1000), Point(1000,-5))
    cover.setFill('white')
    cover.draw(win)
    return lives,lvl

'''
this fuction makes the intro screen
'''
def intro(win):
    txt=Text(Point(50,80),"WELCOME TO THE GAME OF\nHANGMAN")
    txt.setSize(35)
    txt.setStyle('bold')
    txt.draw(win)

    ropeimg = Image(Point(50,150),"rope.gif")
    ropeimg.draw(win)
    for i in range(35):
        ropeimg.undraw()
        ropeimg.move(0,-3)
        ropeimg.draw(win)
        time.sleep(0.1)

    continuetxt=Text(Point(50,10),"Click to Play")
    continuetxt.draw(win)

    win.getMouse()
    ropeimg.undraw()
    txt.undraw()
    continuetxt.undraw()


def main():
    try:
        #setup main window
        win=GraphWin("HANGMAN",1000,700)
        win.setCoords(0, 0, 100, 100)
        win.setBackground('white')
        intro(win)
        #gets the word
        word=getWord(win)
        lives,lvl=level(win)
        wordfill=getWordfill(word)
        startwordfill="".join(wordfill)
        wordtxt=Text(Point(50,50),"{0}".format(startwordfill))
        wordtxt.setSize(35)
        wordtxt.draw(win)
        livestxt=Text(Point(50,90),"Lives:{0}".format(lives))
        livestxt.draw(win)
#draws the keyboard
        win.setCoords(0, 0, 11, 10)
        q = Button(win, Point(1,3), 1, .8, "Q")
        q.activate()
        a = Button(win, Point(1,2), 1, .8, "A")
        a.activate()
        z = Button(win, Point(1,1), 1, .8, "Z")
        z.activate()
        w = Button(win, Point(2,3), 1, .8, "W")
        w.activate()
        s = Button(win, Point(2,2), 1, .8, "S")
        s.activate()
        x = Button(win, Point(2,1), 1, .8, "X")
        x.activate()
        e = Button(win, Point(3,3), 1, .8, "E")
        e.activate()
        d = Button(win, Point(3,2), 1, .8, "D")
        d.activate()
        c = Button(win, Point(3,1), 1, .8, "C")
        c.activate()
        r = Button(win, Point(4,3), 1, .8, "R")
        r.activate()
        f = Button(win, Point(4,2), 1, .8, "F")
        f.activate()
        v = Button(win, Point(4,1), 1, .8, "V")
        v.activate()
        t = Button(win, Point(5,3), 1, .8, "T")
        t.activate()
        g = Button(win, Point(5,2), 1, .8, "G")
        g.activate()
        b = Button(win, Point(5,1), 1, .8, "B")
        b.activate()
        y = Button(win, Point(6,3), 1, .8, "Y")
        y.activate()
        h = Button(win, Point(6,2), 1, .8, "H")
        h.activate()
        n = Button(win, Point(6,1), 1, .8, "N")
        n.activate()
        u = Button(win, Point(7,3), 1, .8, "U")
        u.activate()
        j = Button(win, Point(7,2), 1, .8, "J")
        j.activate()
        m = Button(win, Point(7,1), 1, .8, "M")
        m.activate()
        i = Button(win, Point(8,3), 1, .8, "I")
        i.activate()
        k = Button(win, Point(8,2), 1, .8, "K")
        k.activate()
        o = Button(win, Point(9,3), 1, .8, "O")
        o.activate()
        l = Button(win, Point(9,2), 1, .8, "L")
        l.activate()
        p = Button(win, Point(10,3), 1, .8, "P")
        p.activate()
        one = Button(win, Point(1,4), 1, .8, "1")
        one.activate()
        two = Button(win, Point(2,4), 1, .8, "2")
        two.activate()
        three = Button(win, Point(3,4), 1, .8, "3")
        three.activate()
        four = Button(win, Point(4,4), 1, .8, "4")
        four.activate()
        five = Button(win, Point(5,4), 1, .8, "5")
        five.activate()
        six = Button(win, Point(6,4), 1, .8, "6")
        six.activate()
        seven = Button(win, Point(7,4), 1, .8, "7")
        seven.activate()
        eight = Button(win, Point(8,4), 1, .8, "8")
        eight.activate()
        nine = Button(win, Point(9,4), 1, .8, "9")
        nine.activate()
        zero = Button(win, Point(10,4), 1, .8, "0")
        zero.activate()
        quitButton = Button(win, Point(10,1), .5, .5, "Quit")
        quitButton.activate()
        hangimg=Image(Point(5.5,7),"manstart.gif")
        hangimg.draw(win)


        covers=Rectangle(Point(0,0), Point(100,45))
        covers.setFill('white')
        covers.draw(win)

        readytxt=Text(Point(5.5,5.5),"The Word is {0} Characters Long\nClick to Play".format(len(word)))
        readytxt.setSize(25)
        readytxt.draw(win)

        pt=win.getMouse()
        covers.undraw()
        readytxt.undraw()

        while getWin(wordfill,word,lives):
            letr=getLetter(pt,win,quitButton,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,one,two,three,four,five,six,seven,eight,nine,zero)
            spot=findLetter(word,letr)
            lives=getLives(spot,lives,win)
            drawMan(lives,lvl,win)
#updates lives
            livestxt.setText("Lives:{0}".format(lives))
            wordfill=updatewordfill(spot,wordfill,letr)
            newword="".join(wordfill)
            wordtxt.setText("{0}".format(newword))
        livestxt.undraw()
        word=word.replace(" ","  ")
        checkWin(wordfill,word,lives,win)
        tryagain(win)
#handles all errors so window closes nicely
    except:
        win.close()
        print()

main() #########################################################################



