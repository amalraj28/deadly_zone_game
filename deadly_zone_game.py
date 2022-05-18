# Deadly Zone Game

# ************************ Function defintions begin here *******************************

def success():
    print('Yeeee!!!! You safely escaped from the \"Deadly Zone\"!!!!!!')


def fail():
    print('Game over!')


def lake():
    choice = input('You have reached a lake. Type \"swim\" to swim across or type \"boat\" to go via boat: ').lower()
    if choice == 'swim':
        print('You were attacked by an alligator.')
        fail()
    else:
        success()


def crossroad():
    print('You have managed to reach a crossroad.')
    choice = input('Do you want to turn left, right or straight?: ').lower()
    if choice == 'left':
        print('You reached a lion\'s den.')
        fail()
    elif choice == 'right':
        print('You are surrounded by snakes.')
        fail()
    elif choice == 'straight':
        print('You came out of the jungle sucessfully!')
        lake()


def jungle(choice):
    if choice == 'jump':
        crossroad()
    elif choice == 'walk':
        print('The path was a thorny path')
        fail()
    else:
        print('You entered an invalid option.')
        fail()

# ************************** Function defintions end here ****************************

# main code
print('''
.. ........... .............  ........... . ..... ........ .......
 ......  ....................%.... .... ..... .........%............
 .@@@ ........ @@.... @@@@  . ............................  *  .....
 ....@@ ..... @ .... @ .............   ....... .....; .... *** .....
 .....\@\....@ .... @ ............................. #  .. *****  ...
  @@@.. @@@@@  @@@@@@___.. ....... ...%..... ...  {###}  *******
 ....@-@..@ ..@......@@@\...... %...... ....... <## ####>********
   @@@@\...@ @ ........\@@@@ ..... ...... ....... {###}***********
 ....%..@  @@ /@@@@@ . ....... ...............<###########> *******
 ...... .@-@@@@ ...V......     .... %.......... {#######}******* ***
 ...... .  @@ .. ..v.. .. . { } ............<###############>*******
 ......... @@ .... ........ {^^,     .......   {## ######}***** ****
 ..%..... @@ .. .%.... . .. (   `-;   ... <###################> ****
 . .... . @@ . .... .. _  .. `;;~~ ......... {#############}********
 .... ... @@ ... ..   /(______); .. ....<################  #####>***
 . .... ..@@@ ...... (         (  .........{##################}*****
 ......... @@@  ....  |:------( )  .. <##########################>**
  @@@@ ....@@@  ... _// ...... \\ ...... {###   ##############}*****
 @@@@@@@  @@@@@ .. / /@@@@@@@@@ vv  <##############################>
 @@@@@@@ @@@@@@@ @@@@@@@@@@@@@@@@@@@ ..... @@@@@@  @@@@@@@  @@@@
 @@@@@@###@@@@@### @@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@###@##@@ @@@@@@@@@@@@@@@@@@@@@ @@@@@   @@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@### @@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@
 -@@@@@@@@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
''')
print('Welcome to the game \"Escape from the Deadly Zone\"')
print('Your aim is to safely escape from the \"Deadly Zone\". You have to cross a jungle and then a lake to win the game.')

choice1 = input('You are about to enter the jungle. Type \"jump\" to jump from branch to branch or type \'walk\' to walk: ').lower()

jungle(choice1)
