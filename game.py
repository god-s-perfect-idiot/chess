import pygame


cboard=[]

w,h = (1400,950)

bg_color = (255,255,255)

def makein(a,x,y):
    
    im = pygame.image.load(a)
    im = pygame.transform.scale(im,(x,y))
    return im    
    
bim = makein('res/board.jpeg',800,800)
sel = makein('res/selected.png',100,100)

wpawn = makein('res/wpawn.png',100,100)
wknight = makein('res/wknight.png',100,100)
wbishop = makein('res/wbishop.png',100,100)
wrook = makein('res/wrook.png',100,100)
wqueen = makein('res/wqueen.png',100,100)
wking = makein('res/wking.png',100,100)
bpawn = makein('res/bpawn.png',100,100)
bknight = makein('res/bknight.png',100,100)
bbishop = makein('res/bbishop.png',100,100)
brook = makein('res/brook.png',100,100)
bqueen = makein('res/bqueen.png',100,100)
bking = makein('res/bking.png',100,100)

piece=""


def init():

    global cboard

    for i in range(8):

        cb=[]
    
        for j in range(8):

            if(i==1):
                cb.append("wpawn")

            elif(i==6):
                cb.append("bpawn")

            elif(i==0):
                cb = ["wrook","wknight","wbishop","wqueen","wking","wbishop","wknight","wrook"]

            elif(i==7):
                cb = ["brook","bknight","bbishop","bqueen","bking","bbishop","bknight","brook"]

            else:
                
                cb=["1","1","1","1","1","1","1","1",]

        cboard.append(cb)



def setpeice():

    defx=300
    defy=100

    for i in range(8):
        for j in range(8):

            if(cboard[i][j]=="bpawn"):
                screen.blit(bpawn,(defx+j*100,defy+i*100))
            elif(cboard[i][j]=="wpawn"):
                screen.blit(wpawn,(defx+j*100,defy+i*100))
            elif(cboard[i][j]=="wknight"):
                screen.blit(wknight,(defx+j*100,defy+i*100))
            elif(cboard[i][j]=="wbishop"):
                screen.blit(wbishop,(defx+j*100,defy+i*100))    
            elif(cboard[i][j]=="bbishop"):
                screen.blit(bbishop,(defx+j*100,defy+i*100))
            elif(cboard[i][j]=="wqueen"):
                screen.blit(wqueen,(defx+j*100,defy+i*100))
            elif(cboard[i][j]=="wking"):
                screen.blit(wking,(defx+j*100,defy+i*100))
            elif(cboard[i][j]=="bking"):
                screen.blit(bking,(defx+j*100,defy+i*100))
            elif(cboard[i][j]=="bqueen"):
                screen.blit(bqueen,(defx+j*100,defy+i*100))
            elif(cboard[i][j]=="bknight"):
                screen.blit(bknight,(defx+j*100,defy+i*100))
            elif(cboard[i][j]=="wrook"):
                screen.blit(wrook,(defx+j*100,defy+i*100))
            elif(cboard[i][j]=="brook"):
                screen.blit(brook,(defx+j*100,defy+i*100))            



def board(a):
    
    screen.fill(bg_color)
    screen.blit(bim,(300,100))

    if(a==1):
        init()

    setpeice()


        
def set_text(string,_font,_size,x,y,color,textRect,fill):

    global w,h,bg_color
	
    font = pygame.font.Font(_font, _size)
    text = font.render(string, True, color, (256,256,256))
    textRect = text.get_rect()
    textRect.center = (x,y)
    if(fill==1):
        screen.fill(bg_color)
    screen.blit(text,textRect)


def clicked(x,y):

    global piece,cboard

    board(0)      
    screen.blit(sel,(x*100+300,y*100+100))
    pygame.display.update()

    piece = cboard[y][x]
    if(piece != "1"):
        cboard[y][x]="1"



def moved(x,y):

    global cboard

    if(piece != "1"):
        cboard[y][x] = piece

    board(0)      
    pygame.display.update()


screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('CHESS')

board(1)
pygame.display.update()

alive=1

hover = 1



while(alive):

    for event in pygame.event.get():
    

        if event.type == pygame.KEYDOWN:
            pass

                    

        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
    
            (x,y) = pygame.mouse.get_pos()
            x=x//100 - 3
            y=y//100 - 1

            if(hover == 1):
                
                clicked(x,y)
                hover=0    
                print(cboard[x][y])

    
            else:
            
                moved(x,y)
                hover=1     

     





