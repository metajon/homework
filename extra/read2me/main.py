import curses
screen = curses.initscr()
dims = screen.getmaxyx()
msg = 'Read2Me!'
screen.addstr(dims[0]/2,dims[1]/2-len(msg),msg)
screen.refresh()
screen.getch()
curses.endwin()