import curses,serial
import Bot
import Sparser as sp
import plot as pt
import numpy as np
import iqd
import corner 
import pfilter as pf
import line
import math

ser = serial.Serial('/dev/ttyACM1',9600)
a = Bot.Bot() #creates bot object
particles = pf.particle()
xycor = np.empty(shape = (0,2),dtype = np.float32)
# get the curses screen window
screen = curses.initscr()
# turn off input echoing
curses.noecho()
   
# respond to keys immediately (don't wait for enter)
curses.cbreak()
    
# map arrow keys to special values
screen.keypad(True)
     
try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break

	
        elif char == ord('o'):
            a.observe()
            a.append()

        elif char == ord('i'):
		for i in range(0, len(a.m)-1):
			[flag, corner3] = corner.corner(a.m[i],a.c[i],a.m[i+1],a.c[i+1])
                        if flag == True:
				xycor = np.append(xycor,np.array(corner3),axis=0)
                [flag1, corner4] = corner.corner(a.m[0],a.c[0],a.m[len(a.m)-1],a.c[len(a.m)-1])
                if flag1 == True:
                    xycor = np.append(xycor,np.array(corner4),axis=0)
                #xycor = np.append(xycor,np.array(corner4),axis=0)
		xycor = np.append(xycor,[xycor[0]],axis=0)

        elif char == ord('r'):
            a.reset()

        elif char == ord('p'):
            a.plot()
            
        elif char == ord('k'):
            pt.plotArray(xycor)

        elif char == ord('s'):
            np.savetxt('test.txt', a.Map, delimiter=',') 

        elif char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            screen.addstr(0, 0, 'right')
            a.right()

        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left')
            a.left()
            m,c = line.inter(a.Batch)
            d = line.perp(m, c, a.Pos[0][0], a.Pos[0][1])
            pf.duichoti()
	    #pf.particlefilterupdate(particles,0, 90, 10, 5, np.pi/2)

        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up')
            a.fwd()

        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down')
            a.back()
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
