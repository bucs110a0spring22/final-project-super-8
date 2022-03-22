import pygame
#import your controller
mylist = []
for i in range(4):
  item = int(input("Choose an integer: "))
  number_list.append(item)
  print(item)
mylist[0:], mylist[:3]  = mylist[:3], mylist[0:]
def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()