print('''              ,.  _~-.,               .
           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'

~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^''')
print("Bienvenida a la aventura.")
print("Elige tu destino") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
crossroad1=input("Te ganas un viaje para bucear en Hawai o apostar en las Vegas.\n¿A dónde vas? Escribe \"hawai\" o \"vegas\"\n").lower()
if crossroad1=="hawai":#or crossroad1=="Hawai" or crossroad1=="HAWAI"
  crossroad2=input("Llegas a Hawai y tomas un paseo en bote para ir a bucear.\nAl emerger te ofrecen un viaje en avión privado a Japón.\nEscribe \"volar\" para ir a japón o \"esperar\" para quedarte a\ndisfrutar un poco mas de la playa\n").lower()
  if crossroad2=="esperar":
    crossroad3=input("El guia de turistas te da 3 alternativas para pasar el resto de la tarde.\nIr a la selva a explorar, ir a surfear o ir al centro comercial.\nEscribe \"selva\", \"surf\" o \"centro\"\n").lower()
    if crossroad3=="selva":
      print("Has sido devorada por una tribu de canibales.\nFin del juego")
    elif crossroad3=="surf":
      print("Has sido devorada por un tiburón.\nFin del juego")
    elif crossroad3=="centro":
      print("Compras algunos souvenirs y regresas a casa sana y salva.\n¡Felicidades has ganado el juego!")
    else:
      print("Esa no es una opción válida, te cae un meteorito y mueres al instante.\nFin del juego")
  else:
    print("A 3,600m todos sufren de enfermedad por descompresión y se estrellan,\nlo que hace que el avión explote y mate a todos a bordo.\nFin del juego")
else:
  print("Apostaste todo tu dinero en el casino y ahora estas en bancarrota.\nFin del juego")
  
