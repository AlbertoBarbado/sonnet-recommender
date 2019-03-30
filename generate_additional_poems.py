# -*- coding: utf-8 -*-
"""
@author: Alberto Barbado González
@mail: alberto.barbado.gonzalez@gmail.com

"""

# Sonetos extraídos principalmente de http://amediavoz.com/ para autores del S.XX

import json
from config import OTHER_SONNETS
dct_sonnets = {}

################
# New Author
################

data = {}
author = "Federico García Lorca"
#data['author'] = author
i = 0

### Sonnet
texto = """Este pichón del Turia que te mando, 
de dulces ojos y de blanca pluma, 
sobre laurel de Grecia vierte y suma 
llama lenta de amor do estoy parando.
        
Su cándida virtud, su cuello blando, 
en limo doble de caliente espuma, 
con un temblor de escarcha, perla y bruma
la ausencia de tu boca está marcando.

Pasa la mano sobre su blancura 
y verás qué nevada melodía 
esparce en copos sobre tu hermosura. 

Así mi corazón de noche y día, 
preso en la cárcel del amor oscura, 
llora sin verte su melancolía.
        
"""
        
title = 'SONETO GONGORINO EN QUE EL POETA MANDA A SU AMOR UNA PALOMA'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Esta luz, este fuego que devora. 
Este paisaje gris que me rodea.
Este dolor por una sola idea. 
Esta angustia de cielo, mundo y hora.

Este llanto de sangre que decora 
lira sin pulso ya, lúbrica tea.
Este peso del mar que me golpea.
Este alacrán que por mi pecho mora.

Son guirnalda de amor, cama de herido, 
donde sin sueño, sueño tu presencia
entre las ruinas de mi pecho hundido.

Y aunque busco la cumbre de prudencia 
me da tu corazón valle tendido
con cicuta y pasión de amarga ciencia.
        
"""
        
title = 'LLAGAS DE AMOR'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """¡Esa guirnalda! ¡Pronto! ¡Que me muero! 
¡Teje deprisa! ¡Cantal ¡Gime! ¡Canta!
Que la sombra me enturbia la garganta 
y otra vez viene y mil la luz de enero.

Entre lo que me quieres y te quiero, 
aire de estrellas y temblor de planta 
espesura de anémonas levanta 
con oscuro gemir un año entero. 

Goza el fresco paisaje de mi herida, 
quiebra juncos y arroyos delicados, 
bebe en muslo de miel sangre vertida. 

Pronto ¡prontol! Que unidos, enlazados,
boca rota de amor y alma mordida, 
el tiempo nos encuentre destrozados.
        
"""
        
title = 'SONETO DE LA GUIRNALDA DE LAS ROSAS'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Quiero llorar mi pena y te lo digo
para que tú me quieras y me llores 
en un anochecer de ruiseñores 
con un puñal, con besos y contigo.

Quiero matar al único testigo 
para el asesinato de mis flores 
y convertir mi llanto y mis sudores 
en eterno montón de duro trigo.

Que no se acabe nunca la madeja 
del te quiero me quieres, siempre ardida
con decrépito sol y luna vieja.

Que lo que no me des y no te pida 
será para la muerte, que no deja 
ni sombra por la carne estremecida.
        
"""
        
title = 'EL POETA DICE LA VERDAD'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Amor de mis entrañas, viva muerte, 
en vano espero tu palabra escrita
y pienso, con la flor que se marchita, 
que si vivo sin mí quiero perderte. 

El aire es inmortal, la piedra inerte 
ni conoce la sombra ni la evita. 
Corazón interior no necesita 
la miel helada que la luna vierte. 

Pero yo te sufrí, rasgué mis venas, 
tigre y paloma, sobre tu cintura 
en duelo de mordiscos y azucenas. 

Llena, pues, de palabras mi locura 
o déjame vivir en mi serena noche 
del alma para siempre oscura.
        
"""
        
title = 'EL POETA PIDE A SU AMOR QUE LE ESCRIBA'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """¡Ay voz secreta del amor oscuro!
¡ay balido sin lanas! ¡ay herida!
¡ay aguja de hiel, camelia hundida! 
¡ay corriente sin mar, ciudad sin muro!

¡Ay noche inmensa de perfil seguro, 
montaña celestial de angustia erguida! 
¡ay perro en corazón, voz perseguida! 
¡silencio sin confín, lirio maduro!

Huye de mí, caliente voz de hielo,
no me quieras perder en la maleza 
donde sin fruto gimen carne y cielo.

Deja el duro marfil de mi cabeza,
apiádate de mí, ¡rompe mi duelo!
¡que soy amor, que soy naturaleza!
        
"""
        
title = 'AY VOZ SECRETA DEL AMOR OSCURO'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Tengo miedo a perder la maravilla
de tus ojos de estatua y el acento 
que me pone de noche en la mejilla 
la solitaria rosa de tu aliento.

Tengo pena de ser en esta orilla 
tronco sin ramas, y lo que más siento 
es no tener la flor, pulpa o arcilla, 
para el gusano de mi sufrimiento.

Si tú eres el tesoro oculto mío,
si eres mi cruz y mi dolor mojado, 
si soy el perro de tu señorío.

No me dejes perder lo que he ganado
y decora las aguas de tu río
con hojas de mi Otoño enajenado.
        
"""
        
title = 'SONETO DE LA DULCE QUEJA'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Noche arriba los dos con luna llena,
yo me puse a llorar y tú reías.
Tu desdén era un dios, las quejas mías
momentos y palomas en cadena

Noche abajo los dos. Cristal de pena,
llorabas tú por hondas lejanías.
Mi dolor era un grupo de agonías
sobre tu débil corazón de arena.

La aurora nos unió sobre la cama,
las bocas puestas sobre el chorro helado 
de una sangre sin fin que se derrama. 

Y el sol entró por el balcón cerrado 
y el coral de la vida abrió su rama 
sobre mi corazón amortajado.
        
"""
        
title = 'NOCHE DEL AMOR INSOMNE'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """¿Te gustó la ciudad que gota a gota 
labró el agua en el centro de los pinos? 
¿Viste sueños y rostros y caminos 
y muros de dolor que el aire azota?

¿Viste la grieta azul de luna rota
que el Júcar moja de cristal y trinos? 
¿Han besado tus dedos los espinos 
que coronan de amor piedra remota?

Te acordaste de mí cuando subías 
al silencio que sufre la serpiente, 
prisionera de grillos y de umbrías?

¿No viste por el aire transparente 
una dalia de penas y alegrías 
que te mandó mi corazón caliente?
        
"""
        
title = 'EL POETA PREGUNTA A SU AMOR POR LA CIUDAD ENCANTADA DE CUENCA'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """¿Te gustó la ciudad que gota a gota 
labró el agua en el centro de los pinos? 
¿Viste sueños y rostros y caminos 
y muros de dolor que el aire azota?

¿Viste la grieta azul de luna rota
que el Júcar moja de cristal y trinos? 
¿Han besado tus dedos los espinos 
que coronan de amor piedra remota?

Te acordaste de mí cuando subías 
al silencio que sufre la serpiente, 
prisionera de grillos y de umbrías?

¿No viste por el aire transparente 
una dalia de penas y alegrías 
que te mandó mi corazón caliente?
        
"""
        
title = 'EL POETA HABLA POR TELÉFONO CON EL AMOR'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Tú nunca entenderás lo que te quiero 
porque duermes en mí y estás dormido. 
Yo te oculto llorando, perseguido
por una voz de penetrante acero.

Norma que agita igual carne y lucero 
traspasa ya mi pecho dolorido
y las turbias palabras han mordido 
las alas de tu espíritu severo.

Grupo de gente salta en los jardines
esperando tu cuerpo y mi agonía
en caballos de luz y verdes crines.

Pero sigue durmiendo, vida mía.
Oye mi sangre rota en los violines.
¡Mira que nos acechan todavía!
        
"""
        
title = 'EL AMOR DUERME EN EL PECHO DEL POETA'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """¡Una viola de luz yerta y helada
eres ya por las rocas de la altura.
Una voz sin garganta, voz oscura 
que suena en todo sin sonar en nada.

Tu pensamiento es nieve resbalada
en la gloria sin fin de la blancura.
Tu perfil es perenne quemadura,
tu corazón paloma desatada.

Canta ya por el aire sin cadena
la matinal fragante melodía,
monte de luz y llaga de azucena.

Que nosotros aquí de noche y día
haremos en la esquina de la pena
una guirnalda de melancolía.
        
"""
        
title = 'A Mercedes en su vuelo'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1



### Sonnet
texto = """¡Quién dirá que te vio, y en qué momento!
¡Qué dolor de penumbra iluminada!
Dos voces suenan: el reloj y el viento,
mientras flota sin ti la madrugada.

Un delirio de nardo ceniciento
invade tu cabeza delicada.
¡Hombre! ¡Pasión! ¡Dolor de luz! Memento.
Vuelve hecho luna y corazón de nada.

Vuelve hecho luna: con mi propia mano
lanzaré tu manzana sobre el río
turbio de rojos peces de verano.

Y tú, arriba, en lo alto, verde y frío,
¡olvídate! y olvida al mundo vano,
delicado Giocondo, amigo mío.
        
"""
        
title = 'En la muerte de José de Ciria y Escalante'
date = '1926'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Yo sé que mi perfil será tranquilo
en el norte de un cielo sin reflejo:
Mercurio de vigilia, casto espejo
donde se quiebre el pulso de mi estilo.

Que si la yedra y el frescor del hilo
fue la norma del cuerpo que yo dejo,
mi perfil en la arena será un viejo
silencio sin rubor de cocodrilo.

Y aunque nunca tendrá sabor de llama
mi lengua de palomas ateridas
sino desierto gusto de retama,

libre signo de normas oprimidas
seré, en el cuello de la yerta rama
y en el sinfín de dalias doloridas.
        
"""
        
title = 'Yo sé que mi perfil será tranquilo'
date = '1930'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Esta piedra que vemos levantada
sobre hierbas de muerte y barro oscuro
guarda lira de sombra, sol maduro,
urna de canto sola y derramada.

Desde la sal de Cádiz a Granada,
que erige en agua su perpetuo muro,
en caballo andaluz de acento duro
tu sombra gime por la luz dorada.

¡Oh dulce muerto de pequeña mano!
¡Oh música y bondad entretejida!
¡Oh pupila de azor, corazón sano!

Duerme cielo sin fin, nieve tendida.
Sueña invierno de lumbre, gris verano.
¡Duerme en olvido de tu vieja vida!
        
"""
        
title = 'Epitafio a Isaac Albéniz'
date = '1935'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Tengo miedo a perder la maravilla
de tus ojos de estatua y el acento
que de noche me pone en la mejilla
la solitaria rosa de tu aliento.

Tengo pena de ser en esta orilla
tronco sin ramas; y lo que más siento
es no tener la flor, pulpa o arcilla,
para el gusano de mi sufrimiento.

Si tú eres el tesoro oculto mío,
si eres mi cruz y mi dolor mojado,
si soy el perro de tu señorío,

no me dejes perder lo que he ganado
y decora las aguas de tu río
con hojas de mi otoño enajenado.
        
"""
        
title = 'Tengo miedo a perder la maravilla'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Una luz de jacinto me ilumina la mano
al escribir tu nombre de tinta y cabellera
y en la neutra ceniza de mi verso quisiera
silbo de luz y arcilla de caliente verano.

Un Apolo de hueso borra el cauce inhumano
donde mi sangre teje juncos de primavera,
aire débil de alumbre y aguja de quimera
pone loco de espigas el silencio del grano.

En este duelo a muerte por la virgen poesía,
duelo de rosa y verso, de número y locura,
tu regalo semeja sol y vieja alegría.

¡Oh pequeña morena de delgada cintura!
¡Oh Perú de metal y de melancolía!
¡Oh España, o luna muerta sobre la piedra dura!
        
"""
        
title = 'A Carmela, la peruana'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


################
# New Author
################

#data = {}
author = "Rafael Alberti"
#data['author'] = author
#i = 0


### Sonnet
texto = """Lloraba recio, golpeando, oscuro,
las humanas paredes sin salida.
Para marcarlo de una sacudida,
lo esperaba la luz fuera del muro.

Grito en la entraña que lo hincó, futuro,
desventuradamente y resistida
por la misma cerdada, abierta herida
que ha de exponerlo al primer golpe duro.

¡Qué desconsolación y qué ventura!
Monstruo batido en sangre, descuajado
de la cueva carnal del sufrimiento.

Mama la luz y agótala, criatura,
tabícala en tu ser iluminado,
que mamas con la leche el pensamiento.
        
"""
        
title = 'Sonetos Corporales (I)'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Asombro de la estrella ante el destello
de su cardada lumbre en alborozo.
Sueña el melocotón en que su bozo
al aire pueda amanecer cabello.

Atónito el limón y agriado el cuello,
sufre en la greña del membrillo mozo,
y no hay para la rosa mayor gozo
que ver sus piernas de espinado vello.

Ensombrecida entre las lajas, triste
de sufrirlas tan duras y tan solas,
lisas para el desnudo de sus manos,

ante el crinado mar que las embiste,
mira la adolescente por las olas
poblársele las ingles de vilanos
"""
        
title = 'Sonetos Corporales (II)'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Huele a sangre mezclada con espliego,
venida entre un olor de resplandores.
A sangre huelen las quemadas flores
y a súbito ciprés de sangre el fuego.

Del aire baja un repentino riego
de astro y sangre resueltos en olores,
y un tornado de aromas y colores
al mundo deja por la sangre ciego.

Fría y enferma y sin dormir y aullando,
desatada la fiebre va saltando,
como un temblor, por las terrazas solas.

Coagulada la luna en la cornisa,
mira la adolescente sin camisa
poblársele las ingles de amapolas.
"""
        
title = 'Sonetos Corporales (III)'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Un papel desvelado en su blancura.
La hoja blanca de un álamo intachable.
El revés de un jazmín insobornable.
Una azucena virgen de escritura.

El albo viso de una córnea pura.
La piel del agua impúber e impecable.
El dorso de una estrella invulnerable
sobre lo opuesto a una paloma oscura.

Lo blanco a lo más blanco desafía.
Se asesinan de cal los carmesíes
y el pelo rubio de la luz es cano.

Nada se atreve a desdecir al día.
Mas todo se me mancha de alhelíes
por la movida nieve de una mano.
"""
        
title = 'Sonetos Corporales (IV)'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Nace en las ingles un calor callado,
como un rumor de espuma silencioso.
Su dura mimbre el tulipán precioso
dobla sin agua, vivo y agotado.

Crece en la sangre un desasosegado,
urgente pensamiento belicoso.
La exhausta flor perdida en su reposo
rompe su sueño en la raíz mojado.

Salta la tierra y de su entraña pierde
savia, venero y alameda verde.
Palpita, cruje, azota, empuja, estalla.

La vida hiende vida en plena vida.
Y aunque la muerte gane la partida,
todo es un campo alegre de batalla.
"""
        
title = 'Sonetos Corporales (V)'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Sal tú, bebiendo campos y ciudades,
En largo ciervo de agua convertido,
Hacia el mar de las albas claridades,
Del martín-pescador mecido nido;

Que yo saldré a esperarte, amortecido,
Hecho junco, a las altas soledades,
Herido por el aire y requerido
Por tu voz, sola entre las tempestades.

Deja que escriba, débil junco frío,
Mi nombre en esas aguas corredoras,
Que el viento llama, solitario, río.

Disuelto ya en tu nieve el nombre mío,
Vuélvete a tus montañas trepadoras,
Ciervo de espuma, rey del monterío.
        
"""
        
title = 'A Federico García Lorca (Invierno)'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """En esta noche en que el puñal del viento
acuchilla el cadáver del verano,
yo he visto dibujarse en mi aposento
tu rostro oscuro de perfil gitano.

Vega florida. Alfanjes de los ríos,
tintos en sangre pura de las flores.
Adelfares. Cabañas. Praderíos.
Por la sierra, cuarenta salteadores.

Despertaste a la sombra de una oliva,
junto a la pitiflor de los cantares.
Tu alma de tierra y aire fue cautiva...

Abandonando, dulce, sus altares,
quemó ante ti una anémona votiva
la musa de los cantos populares.
        
"""
        
title = 'A Federico García Lorca (Otoño)'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Todas mis novias, las de mar y tierra
—Amaranta, Coral y Serpentina,
Trébol del agua, Rosa y Leontina—,
verdes del sol, del aire, de la sierra;

contigo, abiertas por la ventolina,
coronándote están sobre las dunas,
de amarantos, corales y de lunas
de tréboles del agua matutina.

¡Vientos del mar, salid, y, coronado
por mis novias, mirad al dulce amigo
sobre las altas dunas reclinado!

¡Peces del mar, salid, cantad conmigo:
—Pez azul yo te nombro, al desabrigo
del aire, pez del monte, colorado!
        
"""
        
title = 'A Federico García Lorca (Primavera)'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Clava tu espada en mí, tú pez-espada,
en mí -- corzo del mar de agua caliente --
que hundida por el plato de mi frente,
parta el cristal del fondo, ensangrentada.

Clavado yo, clavada sea mi amada
segadora de vidrio en la corriente...
Libre del alma. Y de su cuerpo ausente,
emerja de la mar alborotada.

Y emerja yo también, cuerp sin vida,
mi alma de corzo a su cabello asida,
verde eslabón, no de la mar cadena...

Que nos traiga el vendaval playero,
y nos recoja un viejo marinero,
cadáveres los dos sobre la arena.
"""
        
title = 'A Federico García Lorca (Verano)'
date = '1936'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Te digo adiós, amor, y no estoy triste.	
Gracias, mi amor, por lo que ya me has dado,	
un solo beso lento y prolongado	
que se truncó en dolor cuando partiste.	

No supiste entender, no comprendiste	
que era un amor final, desesperado,	
ni intentaste arrancarme de tu lado	
cuando con duro corazón me heriste.	

Lloré tanto aquel día que no quiero	
pensar que el mismo sufrimiento espero	
cada vez que en tu vida reaparece	

ese amor que al negarlo te ilumina.	
Tu luz es él cuando mi luz decrece,	
tu solo amor cuando mi amor declina.	
"""
        
title = 'Te digo adiós, amor, y no estoy triste...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """A ti, contorno de la gracia humana,
recta, curva, bailable geometría,
delirante en la luz, caligrafía
que diluye la niebla más liviana.

A ti, sumisa cuanto más tirana
misteriosa de flor y astronomía
imprescindible al sueño y la poesía
urgente al curso que tu ley dimana.

A ti, bella expresión de lo distinto
complejidad, araña, laberinto
donde se mueve presa la figura.

El infinito azul es tu palacio.
Te canta el punto ardiendo en el espacio.
A ti, andamio y sostén de la pintura.	
"""
        
title = 'A la línea'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Rubios, pulidos senos de Amaranta,
por una lengua de lebrel limados
pórticos de limones desviados
por el canal que asciende a tu garganta.

Rojo, un puente de rizos se adelanta
e incendia tus marfiles ondulados.
Muerde, heridor, tus dientes desangrados,
y corvo, en vilo, al viento te levanta.

La soledad, dormida en la espesura
calza su pie de céfiro y desciende
del olmo alto al mar de la llanura.

Su cuerpo en sombra, oscuro, se le enciende,
y gladiadora, como un ascua impura
entre Amaranta y su amador se tiende.	
"""
        
title = 'Amaranta'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Nace en las ingles un calor callado,
como un rumor de espuma silencioso.
Su dura mimbre el tulipán precioso
dobla sin agua, vivo y agotado.

Crece en la sangre un desasosegado,
urgente pensamiento belicoso.
La exhausta flor perdida en su reposo
rompe su sueño en la raíz mojado.

Salta la tierra y de su entraña pierde
savia, veneno y alameda verde.
Palpita, cruje, azota, empuja, estalla.

La vida hiende vida en plena vida.
Y aunque la muerte gane la partida,
todo es un campo alegre de batalla.
"""
        
title = 'Campo de batalla'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Cúbreme, amor, el cielo de la boca 
con esa arrebatada espuma extrema, 
que es jazmín del que sabe y del que quema, 
brotado en punta de coral de roca. 

Alóquemelo, amor, su sal, aloca 
Tu lancinante aguda flor suprema, 
Doblando su furor en la diadema 
del mordiente clavel que la desboca. 

¡Oh ceñido fluir, amor, oh bello 
borbotar temperado de la nieve 
por tan estrecha gruta en carne viva, 

para mirar cómo tu fino cuello 
se te resbala, amor, y se te llueve 
de jazmines y estrellas de saliva!
"""
        
title = 'Cúbreme, amor, el cielo de la boca...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Huele a sangre mezclada con espliego, 
Venida entre un olor de resplandores. 
A sangre huelen las quemadas flores 
Y a súbito ciprés de sangre el fuego. 

Del aire baja un repentino riego 
De astro y sangre resueltos en olores, 
Y un tornado de aromas y colores 
Al mundo deja por la sangre ciego. 

Fría y enferma y sin dormir y aullando, 
Desatada la fiebre va saltando, 
Como un temblor, por las terrazas solas. 

Coagulada la luna en la cornisa, 
Mira la adolescente sin camisa 
Poblársele las ingles de amapolas.
"""
        
title = 'Huele a sangre mezclada con espliego...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Luna mía de ayer, hoy de mi olvido, 
Ven esta noche a mí, baja a la tierra, 
Y en vez de ser hoy luna de la guerra, 
Sélo tan sólo de mi amor dormido. 

Dale en tu luz el reno perseguido 
Que por los yelos de tus ojos yerra, 
Y dile, si tu lumbre lo destierra, 
Que será lana su destierro y nido. 

Tiempos de horror en que la sangre habita 
Obligatoriamente separada 
De la linde natal de su terreno. 

¡Ay luna de mi olvido, tu visita 
no me despierte el labio de la espada, 
sí el de mi amor, guardado por tu reno!
"""
        
title = 'Luna mía de ayer, hoy de mi olvido...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Las floridas espaldas ya en la nieve,
y los cabellos de marfil al viento. 
Agua muerta en la sien, el pensamiento
color halo de luna cuando llueve.

¡Oh, qué clamor bajo del seno breve,
qué palma al aire el solitario aliento!
¡Qué témpano, cogido al firmamento,
el pie descalzo que a morir se atreve!

Brazos de mar, en cruz, sobre la helada
bandeja de la noche; senos fríos,
de donde surge, yerta, la alborada;

¡oh piernas como dos celestes ríos,
Malva-luna-de-yelo, amortajada
bajo los mares de los ojos míos!
"""
        
title = 'Malva-luna de yelo'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Por allí, hondo, una humedad ardiente; 
blando, un calor oscuro el que allí hervía; 
sofocado anhelar el que se hundía, 
doblándose y muriendo largamente. 

Labios en labios que no ataca diente; 
Lengua en garganta que se corta, umbría; 
Áspero alrededor, fiera porfía 
Por morder lo imposible de la fuente. 

Fiera porfía, ya que ni a la hembra 
Más hembra ni al varón más varón dieron 
Otra cumbre que ser sembrado y siembra. 

Pues lo demás, ¡oh cuerpos desvelados!, 
Son fulgores que al alba se perdieron 
En un súbito arder, desesperados.
"""
        
title = 'Por allí, hondo, una humedad ardiente...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Sabes tanto de mí, que yo mismo quisiera
repetir con tus labios mi propia poesía,
elegir un pasaje de mi vida primera:
un cometa en la playa, peinado por Sofía.

No tengo que esperar ni que decirte espera
a ver en la memoria de la melancolía,
los pinares de Ibiza, la escondida trinchera,
el lento amanecer sin que llegara el día.

Y luego amor, y luego, ver que la vida avanza
plena de abiertos años y plena de colores,
sin final, no cerrada al sol por ningún muro.

Tú sabes bien que en mí no muere la esperanza,
que los años en mí no son hojas, son flores,
que nunca soy pasado, sino siempre futuro.
"""
        
title = 'Sabes tanto de mí, que yo mismo quisiera...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Oh tú mi amor, la de subidos senos
en punta de rubíes levantados
los más firmes, pulidos, deseados,
llenos de luz y de penumbra llenos.

Hermosos, dulces, mágicos, serenos
o en la batalla erguidos, agitados,
o ya en juegos de puro amor besados,
gráciles corzas de dormir morenos.

Oh tú mi amor, el esmerado estilo
de tu gran hermosura que en sigilo
casi muriendo alabo a toda hora.

Oh tú mi amor, yo canto la armonía
de tus perfectos senos la alegría
al ver que se me abren cada aurora.
"""
        
title = 'Sabes tanto de mí, que yo mismo quisiera...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Subes del mar, entras del mar ahora.
Mis labios sueñan ya con tus sabores.
Me beberé tus algas, los licores
de tu más escondida, ardiente flora.

Conmigo no podrá la lenta aurora,
pues me hallará prendido a tus alcores,
resbalando por dulces corredores
a ese abismo sin fin que me devora.

Ya estás del mar aquí, flor sacudida,
estrella revolcada, descendida
espuma seminal de mis desvelos.

Vuélcate, estírate, tiéndete, levanta,
éntrate toda entera en mi garganta,
y para siempre vuélame a tus cielos.
"""
        
title = 'Subes del mar, entras del mar ahora...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Un papel desvelado en su blancura. 
La hoja blanca de un álamo intachable. 
El revés de un jazmín insobornable. 
Una azucena virgen de escritura. 

El albo viso de una córnea pura. 
La piel del agua impúber e impecable. 
El dorso de una estrella invulnerable 
Sobre lo opuesto a una paloma oscura. 

Lo blanco a lo más blanco desafía. 
Se asesinan de cal los carmesíes 
Y el pelo rubio de la luz es cano. 

Nada se atreve a desdecir el día. 
Mas todo se me mancha de alhelíes 
Por la movida nieve de una mano.
"""
        
title = 'Un papel desvelado en su blancura...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Ven, mi amor, en la tarde de Aniene
y siéntate conmigo a ver el viento.
Aunque no estés, mi solo pensamiento
es ver contigo el viento que va y viene.

Tú no te vas, porque mi amor te tiene.
Yo no me iré, pues junto a ti me siento
más vida de mi sangre, más tu aliento,
más luz del corazón que me sostiene.

Tú no te irás, mi amor, aunque lo quieras.
Tú no te irás, mi amor, y si te fueras,
aún yéndote, mi amor, jamás te irías.

Es tuya mi canción, en ella estoy.
Y en ese viento que va y viene voy,
y en ese viento siempre me verías.
"""
        
title = 'Ven'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Vuela la noche antigua de erecciones, 
Muertas, como las manos, a la aurora. 
Un clavel prolongado desmejora, 
Hasta empalidecerlos, los limones. 

Contra lo oscuro cimbran esquilones, 
Y émbolos de una azul desnatadora 
Mueven entre la sangre batidora 
Un vertido rodar de cangilones. 

Cuando el cielo se arranca su armadura 
Y en un errante nido de basura 
Le grita un ojo al sol recién abierto. 

Futuro en las entrañas sueña el trigo, 
Llamando al hombre para ser testigo... 
Mas ya el hombre a su lado duerme muerto.
"""
        
title = 'Vuela la noche antigua de erecciones...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

################
# New Author
################
#data = {}
author = "Dámaso Alonso"
#data['author'] = author
#i = 0

### Sonnet
texto = """¡Primavera feroz! Va mi ternura 
por las más hondas venas derramada, 
fresco hontanar, y furia desvelada, 
que a extenuante pasmo se apresura.

¡Oh qué acezar, qué hervir, oh, qué premura 
de hallar, en la colina clausurada, 
la llaga roja de la cueva helada, 
y su cura más dulce, en la locura!

¡Monstruo fugaz, espanto de mi vida, 
rayo sin luz, oh tú, mi primavera, 
mi alimaña feroz, mi arcángel fuerte!

¿Hacia qué hondón sombrío me convida, 
desplegada y astral, tu cabellera? 
¡Amor. amor, principio de la muerte!
"""

title = 'Amor'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """No sé. Sólo me llega, en el venero
de tus ojos, la lóbrega noticia
de dios; sólo en tus labios, la caricia
de un mundo en mies, de un celestial granero.

¿Eres limpio cristal, o ventisquero
destructor? No, no sé... De esta delicia,
yo sólo sé su cósmica avaricia,
el sideral latir con que te quiero.

yo no sé si eres muerte o eres vida,
si toco rosa en ti, si toco estrella,
si llamo a Dios o a ti cuando te llamo.

Junco en el agua o sorda piedra herida,
sólo sé que la tarde es ancha y bella,
sólo sé que soy hombre y que te amo.
"""

title = 'Ciencia de amor'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """La puerta franca.
                        Vino queda y suave. 
Ni materia ni espíritu. Traía 
una ligera inclinación de nave 
y una luz matinal de claro día.

No era de ritmo, no era de armonía 
ni de color. El corazón la sabe, 
pero decir cómo era no podría 
porque no es forma, ni en la forma cabe.

Lengua, barro mortal, cincel inepto 
deja la flor intacta del concepto 
en esta clara noche de mi boda,

y canta mansamente, humildemente, 
la sensación, la sombra, el accidente, 
mientras Ella me llena el alma toda.
"""

title = '¿Cómo era?'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """¿Te quebraré, varita de avellano, 
te quebraré quizás? ¡Oh tierna vida, 
ciega pasión en verde hervor nacida, 
tú, frágil ser que oprimo con mi mano!

Un chispazo fugaz, sólo un liviano 
crujir en dulce pulpa estremecida, 
y aprenderás, oh rama desvalida, 
cuánto pudo la muerte en un verano.

Mas, no; te dejaré... Juega en el viento, 
hasta que pierdas, al otoño agudo, 
tu verde frenesí, hoja tras hoja.

Dame otoño también, Señor, que siento 
no sé qué hondo crujir, qué espanto mudo.
Detén, oh Dios, tu llamarada roja.
"""

title = 'Destrucción inminente'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Oh, blancura. ¿Quién puso en nuestras vidas 
de frenéticas bestias abismales 
este claror de luces siderales, 
estas nieves, con sueño enardecidas?

Oh dulces bestezuelas perseguidas. 
Oh terso roce. Oh signos cenitales. 
Oh músicas. Oh llamas. Oh cristales. 
Oh velas altas, de la mar surgidas.

Ay, tímidos fulgores, orto puro, 
quién os trajo a este pecho de hombre duro, 
a este negro fragor de odio y olvido?

Dulces espectros, nubes, flores vanas... 
¡Oh tiernas sombras, vagamente humanas,
tristes mujeres, de aire o de gemido!
"""

title = 'Mujeres'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Tú le diste esa ardiente simetría 
de los labios, con brasa de tu hondura, 
y en dos enormes cauces de negrura, 
simas de infinitud, luz de tu día;

esos bultos de nieve, que bullía 
al soliviar del lino la tersura, 
y, prodigios de exacta arquitectura, 
dos columnas que cantan tu armonía.

Ay, tú, Señor, le diste esa ladera 
que en un álabe dulce se derrama, 
miel secreta en el humo entredorado.

¿A qué tu poderosa mano espera? 
Mortal belleza eternidad reclama. 
¡Dale la eternidad que le has negado!
"""

title = 'Oración por la belleza de una muchacha'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


################
# New Author
################
#data = {}
author = "Julia Prilutzky"
#data['author'] = author
#i = 0

### Sonnet
texto = """Cómo decir, amor, en qué momento
te rompes dulcemente entre las manos,
sin quejas, sin recuerdos, sin arcanos
y tal vez sin temor ni sufrimiento.

Cómo volver a amar, qué sentimiento
de elementos divinos o profanos
puede reverdecer entre desganos,
en la etapa final del desaliento.

Pregunta al corazón por qué no cree,
pregúntale al mirar qué cosas lee,
pregunta al labio cruel por qué no besa,

y te dirán, sin duda, su fatiga
del amor fiel o la pasión mendiga,
su falta de esperanza o de sorpresa.
"""

title = 'Cómo decir, amor, en qué momento...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Dame tu brazo, amor, y caminemos,
dame tu mano y sírveme de guía.
Ya no quiero saber si es noche o día:
mis ojos están ciegos. Avancemos.

Dame tu estar, amor, en los extremos,
tu presencia y tu infiel sabiduría:
por los caminos de la sangre mía
ya no sé si es que vamos o volvemos.

Y no me digas nada. No es preciso.
Deja que vuelva al pórtico indeciso 
desde donde no escucho ni presencio:

Todo fue dicho ya, tan a menudo,
que ahora tengo miedo, amor, y dudo
de aquello que está al borde del silencio.
"""

title = 'Dame tu brazo, amor, y caminemos...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Está bien. Seré dulce y obediente
o lo pareceré. Te da lo mismo:
Necesita, de pronto, tu egoísmo
que yo me quede así, sumisamente,

Sin sufrir, sin dolor, sin aliciente,
sin pasiones al borde del abismo,
sin mucha fe ni un gran escepticismo,
sin recordar la esclusa ni el torrente.

Necesitas las llamas sin el fuego,
que el fuego del amor no sea un juego
y que esté el rayo aquí, sin la tormenta.

Quieres que espere así, sin esperarte, 
que te adore también sin adorarte
y estar clavado en mi, sin que te sienta.
"""

title = 'Está bien. Seré dulce y obediente...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Este amor que se va, que se me pierde,
esta oscura certeza de vacío:
mi corazón, mi corazón ya es mío
sin nada que le implore ni recuerde.

De pronto, vuelve a ser un fruto verde
sin madurez, ni aroma en el rocío:
ay del que quiere apresurar su estío,
ay de aquél que lo besa o que lo muerde.

Yo sé que algo persiste, todavía.
Pero no existen ya ni la alegría
ni la embriaguez radiante ni la lumbre

ardiendo en la mirada y en los labios.
Ni exaltación ni búsqueda ni agravios:
apenas una cálida costumbre.
"""

title = 'Este amor que se va, que se me pierde...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Este miedo de ti, de mí... de todo, 
miedo de lo sabido y lo entrevisto, 
temor a lo esperado y lo imprevisto, 
congoja ante la nube y ante el lodo.

Déjame estar. Así. ¿No te incomodo?... 
Abajo ya es la noche, y hoy has visto 
cómo acerca el temor: aún me resisto 
pero me lleva a ti de extraño modo.

Déjate estar. No luches: está escrito. 
Desde lejos nos llega, como un grito 
o como un lerdo vértigo rugiente.

Me darás lo más dulce y más amargo: 
una breve alegría, un llanto largo... 
sé que voy al dolor. Inútilmente.
"""

title = 'Este miedo de ti, de mí... de todo...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Gris y más gris. No estás, y yo estoy triste
de una tristeza apenas explicable
con palabras, y de una imperturbable 
soledad, que por ti nace y existe. 

Siempre de gris, mi corazón se viste: 
polvo y humo, ceniza abominable, 
y la envolvente bruma irrenunciable 
que estaba ayer. Y hoy. Y que persiste. 

Gris a mí alrededor. Contra mi mano 
la nube espesa se va abriendo en vano 
porque el fuego que soy, no está encendido 

y hay niebla en lo que miro y lo que toco. 
Ah, yo no sé... Tal vez te odio un poco 
porque está gris, y llueve, y no has venido.
"""

title = 'Este sabor de lágrimas'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Llueve otra vez. Llueve de nuevo. Llueve:
siempre el amor me llega con la lluvia.
Sobre la calle una llovizna breve
y aquí en mi corazón, cómo diluvia...

Llueve. Y el agua cae sin relieve
sobre las piedras, ávidas de lluvia.
Aquí en mi corazón, cómo remueve;
aquí en mi corazón, cómo diluvia.

Siempre el amor me llega así. Sin ruido,
con silencioso paso estremecido:
niebla menuda que después diluvia.

Siempre el amor me llega así, callado,
con silencioso andar desesperado...
Y no sé dónde estás. Y está la lluvia.
"""

title = 'Frente al misterio estoy, de nuevo alerta...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Ni una palabra quedará, siquiera, 
amor que eras mi amor, que eras mi vida. 
Ya no te digo adiós, ni hay despedida 
ni volveré a llorar por lo que fuera. 

Dónde quedó el terror frente a la espera, 
dónde el pretexto fácil de la huida: 
estoy de pronto, como adormecida, 
brazos ausentes, párpados de cera. 

Amor que eras mi amor, estas tan lejos 
que tu imagen se vela en los espejos 
y está la niebla donde había llamas. 

Oigo que rondas pero no te veo, 
vuelvo a escuchar tu voz, pero no creo. 
Ya no importa si estás ni si me llamas.
"""

title = 'Ni una palabra quedará, siquiera...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """No amarse ahora, pero haber amado.
Y encontrarse otra vez... Recuerdo grave
como el de alguna flor de aroma suave
que se mustia en un libro ya olvidado.

Va surgiendo el recuerdo desvelado:
una palabra, un gesto... Es una clave
que nadie descifró, que nadie sabe;
recinto nuestro, cántico inviolado.

Estamos en silencio, frente a frente.
Y sin verte, yo sé que me has mirado
con no sé qué recuerdo transparente

en los ojos lejanos... No has cambiado.
Y es dulce estarse así, indolentemente,
pero no amarse ya. Haberse amado.
"""

title = 'No amarse ahora, pero haber amado...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1



### Sonnet
texto = """No quiero esto de andar enamorado,
estar triste y alegre sin motivo,
saberse generoso y vengativo,
dormirse sin dormir. Y estar cansado.

Y sin embargo, es el acostumbrado
milagro de estar trémulo y altivo,
tanto más libre cuando más cautivo,
tanto más rico cuanto más se ha dado.

Esto de respirar bebiendo el aire,
sentirse rey, temblar frente al desaire,
con el gesto indeciso y la mirada

más cerca o más allá del horizonte,
sufrir el sol, tratar que no tramonte,
mirar sin ver. Y ver, sin mirar nada. 
"""

title = 'No quiero esto de andar enamorado...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """No sé si es el amor el que regresa
brotando entre la sombra temerosa,
si es un viejo cansancio que reposa
o una pasión impune que no cesa.

Mi corazón a solas se confiesa
mientras calla la boca perezosa:
nunca fue su verdad tan nebulosa,
nunca fue la penumbra más aviesa.

Yo sé que no es antorcha ni ceniza,
ni tierra fiel, ni duna movediza
ni el asombro total ni la experiencia.

Pero igual que un torrente trascendido
retomo el cauce del amor perdido:
no perturba el estar sino la ausencia.
"""

title = 'No sé si es el amor el que regresa...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """No sé si espero, amor, ni si te espero
pero de pronto estás, inesperado,
con tu visaje cruel y desolado
en este abrazo cálido de enero.

Reconozco tus ojos de viajero,
tu inseguro silencio, tu llamado,
tus labios sin mañana y sin pasado:
eres el rostro del dolor primero.

Vuelvo a mirarte aún. Y eres el mismo
milagro de ternura y egoísmo,
triste y feliz, eterno y pasajero,

burlón, desesperado, inquieto, firme.
Cómo quedarme, amor, y cómo irme,
cómo estar sin estar. Ya no te quiero.
"""

title = 'No sé si espero, amor, ni si te espero...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Porque la tarde es gris y todos hablan
yo escucho dilatarse un gran silencio.
Las gentes van juntando más palabras:
yo no sé de sus voces ni sus ecos.

Los árboles se alejan lentamente
entre la tibia niebla del paseo
mientras las frases caen como gotas
y apenas van cambiando los acentos.

Porque la tarde se va haciendo noche
los murmullos son más, los ruidos menos
y los pájaros se hunden en la sombra:

aún los oigo cantar; ya no los veo.
Tanto sonido inútil, derramado,
si dos palabras bastan hoy: te quiero.
"""

title = 'Porque la tarde es gris y todos hablan...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1



### Sonnet
texto = """Quiero estar en tu sueño. Ser tu sueño.
Penetrar más allá de lo que advierte
la mirada sutil. Como beleño
recorrer, galopar tu sangre inerte.

Quiero quebrar con definido empeño
toda defensa en ti: muralla, fuerte:
y adentrarme, crisálida de ensueño
más allá de tu vida y de tu muerte.

Más allá de tu piel, y más adentro
de toda sombra, y más allá del centro
desconocido, virgen, tembloroso...

Y estar dentro de ti -seguro puerto-
como un paradojal milagro cierto,
presentido a la vez que pavoroso.
"""

title = 'Quiero estar en tu sueño. Ser tu sueño...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Quiero hablar de tu amor, porque es el mío:
decirme tu impaciencia y tu sorpresa,
tu soledad de mí que en mí no cesa,
tu sed que ignora el borde del hastío.

Quiero decir tu dulce desafío,
tu inseguro temblor y tu certeza,
tu júbilo que es casi una tristeza,
tu miedo indetenible como un río.

Quiero hablar de mi amor, porque es el tuyo:
porque estoy en el grito y el arrullo
-desesperado actor, mudo testigo-

porque soy quien se va pero regresa
para morder tu mano, mientras besa,
porque soy el que otorga. Y el mendigo.
"""

title = 'Quiero hablar de tu amor, porque es el mío...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Quiero un amor de todos los instantes,
aunque no sea un amor para la vida;
quiero un amor con la ansiedad del antes
para después del ansia desmedida.

Quiero la fe de todos los amantes
en este solo amor, ver contenida:
tumulto de horizontes trashumantes
y luego, claridad de agua dormida.

Quiero un amor transfigurado en fuente
de todo florecer: fruto y simiente;
a tal único amor, mi amor sentencio:

aquél de la impaciencia y el latido
y la fiebre y el grito y el gemido
y el difícil momento del silencio.
"""

title = 'Quiero un amor de todos los instantes...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Un día te querré... Un día: ¿cuándo?
No lo sé, ni me importa, todavía.
Tan segura de amarte estoy, un día,
que ni anhelo ni busco, voy andando.

Mi mano que la espera va ahuecando
hoy reposa indolente, blanda y fría.
Un día te querrá... Hoy sólo ansía
encerrarse en la tuya, descansando.

Mi amor sabe aguardar. No es impaciente:
su deseo es arroyo, y no torrente
que hacia ti, con certeza, sigue andando.

Y una tarde cualquiera y diferente
me ha de dar a tu amor, serenamente.
Un día te amaré: ¿qué importa cuándo?
"""

title = 'Un día te querré... Un día: ¿cuándo?...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """No amarse ahora, pero haber amado.
Y encontrarse otra vez, recuerdo grave
como el de alguna flor de aroma suave
que se mustia en un libro ya olvidado,

Va surgiendo el recuerdo desvelado:
una palabra, un gesto... Es una clave
que nadie descifró, que nadie sabe;
recinto nuestro, cántico inviolado.

Estamos en silencio, frente a frente.
Y sin verte, yo sé que me has mirado
con no sé qué recuerdo transparente

en los ojos lejanos... No has cambiado.
Y es dulce estarse así, indolentemente,
pero no amarse ya. Haberse amado.
"""

title = 'Viaje sin partida'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Voy hacia ti como una rosa viva
deshojada en distancias y en esperas...
No lo sabes aún. Y no aceleras
el encuentro en la hora decisiva. 

Voy hacia ti con precisión altiva 
y antes que yo  -oscuras mensajeras 
del porvenir-  las grises hilanderas 
van tejiendo la trama fugitiva. 

Estás en mí. Y no eres el culpable: 
algo de tu presencia indescifrable 
me dilata en las venas el latido 

y se estira en mi piel con grave alarde. 
Mis pájaros se alargan en la tarde 
y todo es tan perfecto, que ya ha sido.
"""

title = 'Voy hacia ti como una rosa viva...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Yo no sé todavía cómo existe,
cómo ha venido a mí y está creciendo
la indócil llamarada que no enciendo
y esta emoción que tiembla y que persiste.

No sé si estar alegre o estar triste,
ya no entiendo la voz sino el acento,
ya no busco ni espero ni presiento:
apenas sé que estoy. Que está. Qué existe.

Pero cómo saber si es sólo un juego:
neblina, soledad, engaño, fuego.
¿Es un juego? Pues bien, hay que jugarlo

con una dulce complacencia esquiva
o una total entrega fugitiva.
¿Y si fuera el amor? Hay que aceptarlo.
"""

title = 'Yo no sé todavía cómo existe...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


################
# New Author
################

#data = {}
author = "Pilar Paz Pasamar"
#data['author'] = author
#i = 0

### Sonnet
texto = """De tierra adentro a mar, de trecho a trecho
desde el invierno hasta el feliz verano,
de la estepa encendida de la mano
a la región volcánica del pecho

va posándose amor, y va en acecho
amor de cima a sima, y sobre el llano,
y va implantando en todos, soberano,
su ley, su ejecución y su derecho.

Rey de la geografía del semblante,
encendedor de lumbres abisales
toda región desconsolada anima.

Cruza desde el poniente hasta el levante
implantando sus órdenes reales:
su agua, su luz, su voluntad, su clima...
        
"""
        
title = 'De tierra adentro a mar, de trecho a trecho...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Intermediario ser, anfibio alado.
Amor hecho de raptos y de ausencia,
a otros alimentaste con tu ciencia
desposeyéndome del esperado.

Bien sé cómo eres, aunque disfrazado
cruzaras tantas veces mi dolencia,
haciéndome creer que era experiencia
de ti lo que ni apenas tu recado.

Ahora, burlada, llega el importuno
labio de quien te sabe a repetirme
tu nombre con informes y resabios.

Condenada a la espera y al ayuno
no te alzaré la voz ni habrás de oírme
porque la soledad no tiene labios.
        
"""
        
title = 'Intermediario ser, anfibio alado...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """No le consientas tanto, que acostumbras
mal a mi corazón. Exige, hiere.
Niégale a mi pregunta lo que inquiere,
si pide luz, mantenla en las penumbras

del amor. Cuanto más lo alzas y encumbras
más insaciable está. Mi amor prefiere
luchar por la respuesta, y que él espere
impaciente la luz con que me alumbras.

No le perdones nada a mi descuido
que me duele ser siempre la deudora
de tanto amor, y tal renunciamiento.

Dame que perdonar. Yo te lo pido.
Hiere mi corazón, hiérele ahora
para que perdonando esté contento.
        
"""
        
title = 'No le consientas tanto, que acostumbras...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Por ellos no pasaste. Bien se advierte
que están secos, con sólo la sonrisa.
Van de una cosa a otra tan deprisa
que el agua de la vida se les vierte.

Van de acá para allá sin conocerte,
gastados por el soplo de otra brisa,
pero nunca sabrán de la precisa
hora en que el mundo en fuego se convierte.

Míralos: desatentos, desalados,
desparramados, secos, sin saberte,
más solos que la luna y ateridos.

No supieron ganar y están ganados,
no supieron mirar y están sin verte...
¡Qué pocos son, amor, los elegidos!
        
"""
        
title = 'Por ellos no pasaste. Bien se advierte...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Si un verso olvido nunca me devuelve su cita.
Volver es tan difícil como morir de veras,
por eso son distintas todas las primaveras
y esperamos en vano que un sueño se repita.

¡Y tú quieres llegar! En mi mano vacía
tu presencia se vierte reducida y oscura;
se pudren las raíces y el brote no me dura
lo que dura el deseo bajo el golpe del día.

Si hay para cada instante una voz diferente,
ni hay silencio que envuelva por dos veces mi frente,
ni ola que desdoble repetida en la orilla,

¿cómo vas a llegar sobre tu propio paso
si el camino es distinto, y hasta Dios tiemble acaso
al besarnos dos veces en la misma mejilla?
        
"""
        
title = 'Retorno'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Ya me tiene mi Dios. Me ha señalado 
el pecho y la razón con su caricia, 
y ya siento el empuje que se inicia 
en forma inmaterial. Me he levantado 

sedienta de confines y, logrado 
mi afán, he de buscarme la sonrisa 
y al despertar, entre la nueva brisa,
veré mi corazón enajenado. 

Porque ya voy a Ti, con esta entrega, 
déjame despedirme de la rosa 
y saludar la luz en su carrera. 

Antes de comenzar mi dulce vuelo, 
el árbol prestará toda su sombra 
a la fiebre encendida de mi anhelo.
        
"""
        
title = 'Ya me tiene mi Dios. Me ha señalado...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


################
# New Author
################

#data = {}
author = "Juan Ramón Jiménez"
#data['author'] = author
#i = 0

### Sonnet
texto = """Siempre tienes la rama preparada
para la rosa justa; andas alerta
siempre, el oído cálido en la puerta
de tu cuerpo, a la flecha inesperada.

Una onda no pasa de la nada,
que no se lleve de tu sombra abierta
la luz mejor. De noche, estás despierta
en tu estrella, a la vida desvelada.

Signo indeleble pones en las cosas.
luego, tornada gloria de las cumbres,
revivirás en todo lo que sellas.

Tu rosa será norma de las rosas;
tu oír, de la armonía; de las lumbres
tu pensar; tu velar, de las estrellas.
        
"""
        
title = 'A mi alma'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """¿Cómo era, Dios mío, cómo era? 
-¡Oh corazón falaz, mente indecisa!- 
¿Era como el pasaje de la brisa? 
¿Como la huida de la primavera? 

Tan leve, tan voluble, tan ligera 
cual estival vilano... ¡Sí! Imprecisa 
como sonrisa que se pierde en risa... 
¡Vana en el aire, igual que una bandera! 

¡Bandera, sonreír, vilano, alada 
primavera de junio, brisa pura...! 
¡Qué loco fue tu carnaval, qué triste! 

Todo tu cambiar trocóse en nada 
-¡memoria, ciega abeja de amargura!- 
¡No sé cómo eras, yo que sé qué fuiste!
        
"""
        
title = '¿Cómo era, Dios mío, cómo era?'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """¡Esperar! ¡Esperar! Mientras, el cielo
cuelga nubes de oro a las lluviosas;
las espigas suceden a las rosas;
las hojas secas a la espiga; el yelo

sepulta la hoja seca; en largo duelo,
despide el ruiseñor las amorosas
noches; y las volubles mariposas
doblan en el caliente sol su vuelo.

Ahora, a la candela campesina,
la lenta cuna de mis sueños mecen
los vientos del octubre colorado...

La carne se me torna más divina,
viejas, las ilusiones, encanecen,
y lo que espero ¡ay! es mi pasado.
        
"""
        
title = 'Esperanza'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Nevada de los cielos, pareciste
la luna trastornada en primavera.
Vi una vez, no sé dónde, una pradera
así, blanca cual tú te apareciste.

En un sueño más sueño aún, volviste
de nuevo a mí como la mensajera
del último blancor que el alma espera...
Me desperté dos veces, triste y triste.

No sé si desvelada va o dormida
mi esperanza contigo. Sobrepasa
unas veces, con luz, tu mismo albor,

cuando estoy más despierto que en la vida...
Ya veces es como que me traspasa
la negra sombra de un almendro en flor...
        
"""
        
title = 'Nubes'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """A través de la paz del agua pura,
el sol le dora al río sus verdines;
las hojas secas van, y los jazmines
últimos, sobre el oro a la ventura.

El cielo, verde, en la más libre altura
de su ancha plenitud, deja los fines
del mundo en un extremo de jardines
de ilusión. ¡Tarde en toda tu hermosura!

¡Qué paz! Al chopo claro viene y canta
un pájaro. Una nube se desvae
sin color, y una sota mariposa,

luz, se sume en la luz... y se levanta
de todo no sé qué hálito, que trae,
triste de no morir aún más, la rosa.  
"""
        
title = 'Octubre II'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Esparce octubre, al blando movimiento
del sur, las hojas áureas y las rojas,
y, en la caída clara de sus hojas,
se lleva al infinito el pensamiento.

Qué noble paz en este alejamiento
de todo; oh prado bello que deshojas
tus flores; oh agua fría ya, que mojas
con tu cristal estremecido el viento!

¡Encantamiento de oro! Cárcel pura,
en que el cuerpo, hecho alma, se enternece,
echado en el verdor de una colina!

En una decadencia de hermosura,
la vida se desnuda, y resplandece
la excelsitud de su verdad divina.
"""
        
title = 'Otoño'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Abril, sin tu asistencia clara, fuera
invierno de caídos esplendores;
mas aunque abril no te abra a ti sus flores,
tú siempre exaltarás la primavera.

Eres la primavera verdadera:
rosa de los caminos interiores
brisa de los secretos corredores,
lumbre de la recóndita ladera.

¡Qué paz, cuando en la tarde misteriosa,
abrazados los dos, sea tu risa
el surtidor de nuestra sola fuente!

Mi corazón recogerá tu rosa,
sobre mis ojos se echará tu brisa
tu luz se dormirá sobre mi frente...
"""
        
title = 'Primavera'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Se entró mi corazón en esta nada,
como aquel pajarillo, que, volando
de los niños, se entró, ciego y temblando,
en la sombría sala abandonada. 

De cuando en cuando intenta una escapada
a lo infinito, que lo está engañando
por su ilusión; duda, y se va, piando,
del vidrio a la mentira iluminada.

Pero tropieza contra el bajo cielo,
una vez y otra vez, y por la sala
deja, pegada y rota, la cabeza...

En un rincón se cae, al fin, sin vuelo
ahogándose de sangre, fría el ala, 
palpitando de anhelo y de torpeza. 
"""
        
title = 'Se entró mi corazón en esta nada...'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Imagen alta y tierna del consuelo,
aurora de mis mares de tristeza,
lis de paz con olores de pureza,
¡premio divino de mi largo duelo!

Igual que el tallo de la flor del cielo,
tu alteza se perdía en su belleza...
Cuando hacia mí volviste la cabeza,
creí que me elevaban de este suelo.

Ahora, en el alba casta de tus brazos,
acogido a tu pecho transparente,
¡cuán claras a mí toman mis prisiones!

¡Cómo mi corazón hecho pedazos
agradece el dolor, al beso ardiente
con que tú, sonriendo, lo compones!
"""
        
title = 'Sueño'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

################
# New Author
################

#data = {}
author = "Carmen González Huguet"
#data['author'] = author
#i = 0

### Sonnet
texto = """Aire sólo, fervor que callo y digo,
palabra que te nombra y te delata,
que te eleva en su vuelo o te maniata:
en mi boca te encierro o te prodigo.

Te dejo a la intemperie o al abrigo,
te guardo en ventisquero o en fogata.
Pródiga, codiciosa catarata,
vas en mi labio como fiel testigo

de todo lo que en él pones y eres,
de todo lo que en él tu sed convoca
y de lo que en su amor beber quisieres.

Silencia esta ebriedad que el labio aloca
y con el agua en que dichoso mueres
cúbreme, amor, el cielo de la boca.  
"""
        
title = 'Ausencia (I)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Hay esta piel por tanto beso herida,
esta música en tanta luz cegada,
esta ternura a solas escanciada,
esta verdad por tu fervor vertida,

esta palabra en sombras encendida,
esta caricia ardiendo derramada,
tu mirada bebida y escuchada,
tu silencio envolviéndome la vida,

todas las cosas que forman mi cielo:
el canto, la presencia de tu beso,
la voz que tiene cada anhelo preso,

los aleros del ave ahíta en vuelo,
tu sed lo enciende todo y me lo quema
con esa arrebatada espuma extrema.
"""
        
title = 'Ausencia (II)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """¿Qué va a saber el sol del día triste?
¿Qué va a saber el agua de sequía?
¿Qué va a saber la luz de lluvia fría
y el viento de la rama que resiste?

¿Qué va a saber la llama que subsiste
de cenizas que apaguen su porfía?
¿Qué va a saber, por fin, de la alegría
esa nostalgia que su ser contriste?

Ven que te explique ese fulgor oscuro,
ese dolor amigo, ese ojo ciego,
ese frío quemándome en el fuego.

En la piel que me siembras de futuro
coróname de espuma, oculta yema,
que es jazmín del que sabe y del que quema.
"""
        
title = 'Ausencia (III)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Es aire, sólo el aire, quien te besa,
el aire que lamiendo está la llama,
el aire que te envuelve y te reclama,
que libera tu vuelo y que lo apresa.

Es aire, sólo el aire, en que la espesa
sangre del corazón de aquel que ama
vence al silencio donde se derrama
la palabra trocada en fiel pavesa.

Es aire la verdad que desafía
al frío, la distancia y esa boca
ciega a la sed ajena y su agonía

que siembra su existir en otra boca.
Máteme el beso de tu alevosía
brotado en punta de coral de roca.
"""
        
title = 'Ausencia (IV)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Siembre tu corazón en labio ajeno,
aire que hiera el surco de mi oído;
y en él siembre su pecho estremecido
la palabra dolida y su veneno.

Siembre la luz ardiente el labio pleno
en quieta frente, en pensamiento herido.
Derrota ausencia, desamor, olvido,
la voz donde a vivir yo te condeno.

Desordena mi cielo, mi mañana,
mi vida entera mueve y equivoca
con la corriente que en tu labio mana.

Que me asesina el vino de tu boca
esta escasa cordura, cruel tirana.
Alóquemela, amor, su sal, aloca.
"""
        
title = 'Ausencia (V)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """En ti afirma la carne su porfía,
el carmín de la rosa, la azucena,
el canto del cenzontle, la serena
superficie del agua, la armonía.

En ti enciende sus luces cada día
la voz que incendia el aire cuando suena
su canto repetido en lengua ajena,
hecho fecunda y sola compañía.

Comparte en la distancia esta locura
que tengo por el fuego de tu boca
que ya toda cordura se hace poca.

No me cures jamás la quemadura
donde el alma se muere y se me quema
por tu secreta aguda flor suprema.
"""
        
title = 'Ausencia (VI)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Explora mis panales, mi recinto
secreto donde oculta miel destila.
El tiempo su madeja fiel deshila
confiado a los fervores del instinto.

Bebe el beso que el dulce labio afila,
devora la epidermis del jacinto:
el deseo saciado, nunca extinto,
desde tu tersa torre me vigila.

Tus manos, tu mirada, tu dulzura
desbordan en el vértigo del fuego
donde en olvido la razón se quema.

Coróneme el rocío y su luz pura
en el instante eterno en que me entrego
doblando su fervor en su diadema.
"""
        
title = 'Ausencia (VII)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Me devora la boca que me besa,
me erosiona la voz que me acaricia
y me da vida la tenaz sevicia
de tu labio trocado en fiel pavesa.

Me asesina la mano que confiesa
lo que la voz no eleva a la caricia
me edifica tu labio y su codicia
que dilapida su lujuria aviesa.

Me reta y me sostiene tu locura,
me desalienta tu vivir sensato,
me desarma y cautiva tu ternura,

y en este canto preso que desato
se me enamoran alma, mente y boca
del mordiente clavel que las desboca.
"""
        
title = 'Ausencia (VIII)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """El espejismo me llamaba en vano,
en vano la quimera y su luz pura,
en vano la sirena y su dulzura,
el misterio y la voz de cada arcano.

Inútilmente el fuego del verano
me daba el beso de su quemadura;
su amor, el fuego; el agua, su frescura:
paraíso en la palma de tu mano.

Labio sediento por tu voz, oído;
párpado ciego que la luz evoca;
agua que quema todo lo que toca:

Déjame ser silencio puro, olvido;
de tu fuego el más íntimo destello
¡oh ceñido fluir, amor, tan bello!
"""
        
title = 'Ausencia (IX)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Amor, eres lo único que tengo,
agua que entre mis dedos se diluye,
que cuanto más persigo, más me huye,
por más que mi penar sin fin prevengo.

Tenaz tormento que al latir sostengo,
casa en la arena que el azar destruye.
Lunar marea, medra y disminuye
la herida de vivir que en ella vengo.

Rota de sed, desnuda y calcinada,
mi boca tu veneno dulce bebe
y bebe tu palabra alucinada

mi oído fiel. Cautiva en tu mirada
se me queda la piel enamorada
del borbotar templado de tu nieve.
"""
        
title = 'Ausencia (X)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Humo toqué: ceniza, viva llama,
Y me quemé las manos y el aliento.
Nadie condene el daño que consiento:
Soy víctima y verdugo de mi drama.

Soy quien muere de sed y quien derrama
El agua que le sirve de sustento,
Quien construye su gozo y su tormento,
Quien dispone los hilos y la trama.

Que no encuentre consuelo quien remiso
A la cordura fue, huésped esquiva
De la ilusión que en polvo se deshizo,

Quien por su mal se quiso ver cautiva
De ese breve, engañoso paraíso
En tan estrecha gruta en carne viva.
"""
        
title = 'Ausencia (XI)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Herida fui en el gozo, en el olvido
Libre me vi, desnuda y desolada.
¿Para qué libertad abandonada
Y palabras de amor en ciego oído?

¿Para quién hambre y sed en el sentido
Si me abraza la sombra demudada?
¿Para quién alma y boca enamorada
Si tengo el corazón de ausencia herido?

No hay cicatriz en esta piel serena
Que manifieste con su oscuro sello
La fiera luz que arde en cada vena.

Íntimo fuego del que soy destello:
A brasa fiel mi boca se condena
Para mirar arder tu fino cuello.
"""
        
title = 'Ausencia (XII)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """No me mueve, mi amor, para quererte
la dicha dulce con que me has mentido,
ni la fecunda gracia que has vertido
en mi piel, sin llegar a merecerte.

El ojo no ha logrado conocerte,
ni el beso alcanza a asir todo el sentido,
ni la voz dice todo lo vivido,
ni consigo explicarte ni entenderte.

La luz que brilla al fondo en tu mirada
es la estrella que arde y que me mueve
a cruzar esta ausencia desolada.

Y es la fe que sostiene el lazo leve
adonde la pasión inconfesada
se te resbala, amor, y se te llueve.
"""
        
title = 'Ausencia (XIII)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Construyo esta apretada geometría,
esta sonora cárcel, este abrigo
donde congelo el tiempo y su castigo
y salvo este espejismo que me guía.

Libre y tenaz como una red vacía,
abarca lo que callo y lo que digo,
lo poco que ahora sé, lo que persigo,
lo que viví contigo cada día.

Aire sólo me queda. En este viaje
escribí mis palabras en la arena,
aré en el mar, creí en cada sirena,

viví confiada al viento y al oleaje
con mi voz en tu boca hecha cautiva
por jazmines y estrellas de saliva.
"""
        
title = 'Ausencia (XIV)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Brasa en la llaga, sal en cada herida,
sombra en el sol, carámbano en el fuego,
río de luz que fluye en ojo ciego,
brújula encandilada y confundida.

Vas en mis venas como va la vida
en el ardor oculto que trasiego
y afirmas en mi pecho lo que niego
con la voz traicionada y malherida.

Vas en esta palabra renacido
con una decisión de ser tan fuerte
capaz de hacer arder hasta el olvido.

Y yo, que renunciara a retenerte,
me abandono en el cauce de tu oído,
lengua del mal, guijarro de la muerte.
"""
        
title = 'Presencia (I)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Su navaja de pluma corta el viento,
pero sus ojos glaucos, amorosos,
besan los tuyos mudos y gozosos
de arder sin fin en tan feliz tormento.

No se escapan del labio voz ni aliento
de no dar cuenta del amor medrosos,
mas pueden piel y tacto codiciosos
aprisionar la magia del momento.

En el dulce minuto sin ceniza
vibra con cuerda oculta el tiempo quieto
olvidando en la carne cauce y prisa.

Y logra el beso conquistar el reto
que en la piel fugitiva se eterniza
con la finura de un puñal escueto.
"""
        
title = 'Presencia (II)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Abierta herida, abierta en el costado,
más denostada cuanto más querida
por unir gozo, muerte, llanto y vida
en manantial sin pausa derramado.

Fuego fecundo, instante congelado,
vas navegante en permanente herida:
la voz renace cuanto más transida
y el canto vibra del dolor alzado.

Busco tu corazón, fiel enemigo,
con la palabra en que al olvido reto,
con la ilusión con que al amor bendigo

y en vano intento mantener sujeto
el don con que en tan dulce y cruel castigo
me rozó la cintura tu secreto.*
"""
        
title = 'Presencia (III)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """¿Quién arde en ti, chiltota, quién te hiere?
¿Quién tuerce el derrotero de tu vuelo?
¿Quién te regala el llanto y el consuelo?
¿Quién hay que de tu canto se apodere?

¿Quién abandona el trino, quién lo quiere?
¿Quién alimenta su tenaz desvelo?
¿Quién eleva sus alas hasta el cielo
y salva a la ilusión que desespere?

Encuentras el desdén, gesto vencido,
rota la fe, sin fuerza el ala inerte,
en el páramo frío del olvido,

Y vas, confiada al rumbo de la suerte,
sin mí, que doy tu cielo por perdido,
y consumí la luz por comprenderte.
"""
        
title = 'Presencia (IV)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Gracias te doy porque enjugaste el llanto,
gracias por el abrigo de tu alero,
por ser recodo grato en el sendero,
y miel en la amargura del quebranto.

Tu caricia escondida va en el canto
y tu luz me ilumina en el lucero.
Aunque te vayas, queda prisionero
en esta línea un trozo del encanto.

Gracias, amor, porque por fin viniste,
por la breve ilusión que me trajiste,
por el gozo en el vértigo secreto.

Gracias te doy aun porque pusiste
en mi sonrisa con tu beso quieto
color de sangre anclada y viejo abeto.
"""
        
title = 'Presencia (V)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Si me engañé, bendito sea el engaño,
benditos sean el beso y cada herida,
bendita sea la carne conmovida
y la fe naufragando en gesto huraño.

Benditos sean el día, el mes, el año
cuando la fiel promesa fue cumplida;
bendito sea el sueño y sea la vida,
el dolor, la caricia, el gozo, el daño.

Bendito lo que aprendo, lo vivido,
lo que recuerdo, lo que al fin despierte
en mí, lo que salvé del río hundido.

Me enfrenté cara a cara con la muerte
y aunque luché y viví a brazo partido,
mi garganta no pudo contenerte.
"""
        
title = 'Presencia (VI)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """En la distancia estás, pero presente
sigues en mí. Tus ojos no se han ido.
Fijos, me dicen: “Calla. No hay olvido.
Te engaña el viento, el horizonte miente”.

Estás aquí, debajo de mi frente,
cerca del corazón y su latido.
Tu aliento va en mis venas escondido
como un secreto, generoso afluente.

En la ceniza está oculta la brasa
y el fuego en cada pecho que suspira,
que el gozo besa y que el dolor traspasa.

Déjame, amor, al menos la mentira
de este espejismo dulce que no pasa
como un leopardo de humo que se estira.
"""
        
title = 'Presencia (VII)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Quemé la luz, fui miel en la dulzura,
gota en la lluvia y llama con el fuego,
aroma en cada rosa, instante ciego,
y nardo que dio envidia a la blancura.

Fui sombra en la profunda noche oscura,
silencio en la raíz, raudo despego,
y al fin a tu distante orilla llego:
roto el timón, la brújula insegura.

Al borde de tu barba se me queda
detenida la voz, mudo el acento
como el viajero exhausto en la vereda.

La caricia que tejo y que alimento
se apaga en una suavidad de seda
hasta morir hilada por el viento.
"""
        
title = 'Presencia (VIII)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Mi ciega luz, mi vértigo secreto,
mi larga y venturosa travesía,
mi explorada, bendita geografía,
mi ruta circular, mi viaje quieto.

Eclipse de la voz, fuego indiscreto
que cumple prodigiosa profecía,
da lumbre al sol y claridad al día,
sombra a la noche, a la ilusión objeto.

Da sed al agua, filo al malherido,
paz a la angustia, a la inquietud urgente
reposo dulce, albergue bendecido.

Y derrama en tu beso ese torrente
que llevas en el pecho contenido
y en la sonrisa encubres, de repente.
"""
        
title = 'Presencia (IX)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Un hombre es lo que hace, lo que ama,
lo que pinta su voz con el aliento,
lo que construye su palabra al viento,
lo que desde sus manos se derrama.

Lo que florece en tierra o en escama,
lo que da al mundo desde el pensamiento:
trigo y harina, masa y alimento,
la letra impresa, el fruto en cada rama.

Un hombre, sobre todo, es el reflejo
del instante fugaz en que respira
el aire que lo va poniendo viejo.

Un hombre es esa imagen que suspira
cuando por fin descubre en el espejo
un ángel sosegado que se mira.
"""
        
title = 'Presencia (X)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Una mujer armando el paraíso
sembrando esa verdad en cada herida,
rescatando la brasa consumida
y el incendio en el vientre del granizo.

Viviendo libre, sola y sin permiso,
indiferente al miedo, convencida
de ser cauce fecundo de la vida
y fiel depositaria de su hechizo.

Una mujer que sabe y reconoce
por igual lo que piensa y lo que siente,
que abraza cada pena y cada goce.

Una mujer que reta a aquel que intente
colocarla en el centro de la ira
a arder los pies sobre incendiado puente.
"""
        
title = 'Presencia (XI)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Del rumor de tus manos me alimento
y mi hoguera renuevo en lluvia fría.
Surge de ti fluyente geometría:
venero de la luz, cálido acento.

El seno de la vela que hincha el viento
para partir a la aventura un día,
y tu tierra en su quieta geografía,
trazada en gozo exacto y fiel tormento.

Se abre el ojo a la flor de la belleza
que se desata con fervor de río
y se instala a soñar en tu cabeza.

Por tu perpetuo, floreciente estío
cruza la tarde donde, libre y presa,
la luz corre desnuda por el río.
"""
        
title = 'Tierra (I)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Raíz y rama, flor, nube y colina
Hundidas en el mar de aire que mueve
El invisible cuerpo donde bebe
La vida transitoria y cristalina.

Espejismo tenaz que la alucina,
Fuego escondido al fondo de la nieve,
Sed que escancia la boca donde llueve
La palabra triunfando de la ruina.

Vano intento: aferrar la llamarada
De ayer, hecha pavesa hoy inasible
Para incendiar su esencia ya gastada.

Victoria que tu esfuerzo hace posible:
Congelar la belleza alucinada
huyendo sin cesar en lo movible.
"""
        
title = 'Tierra (II)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """La belleza te anida en la cintura,
en la bondad azul en que navego:
cosecha permanente donde siego
los frutos de la voz y su ventura.

Derramas con largueza tu hermosura
y en la pupila tanta luz trasiego,
que siento arder en mí tu puro fuego
y en la noche brillar tu quemadura.

Estás en mí, como agua de la fuente,
como la sed al fondo del estío
que calme su anhelar en la corriente;

y estás en cada estrella con que guío
el viaje que me lleve hasta tu frente
y a la profundidad del hondo frío.
"""
        
title = 'Tierra (III)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Alimenta la sed, dale a mi trigo
Más hambre para así seguir viviendo.
Echa más fuego al sol, que siga ardiendo,
Y más dolor a este fatal castigo.

Da tu aliento vital a lo que digo,
Pon sangre y alma a lo que voy haciendo,
Entrega esta verdad que nace hiriendo
Y acompaña su luz a herir contigo.

No te dejes vencer, no te acobardes,
apuesta sin cesar a lo imposible,
y construye primero lo que aguardes.

Pero emprende la ruta ineludible
En este mismo instante. No te tardes,
Porque empiezan la sombra y lo invisible.
"""
        
title = 'Tierra (IV)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """La lluvia te bendice y la mañana
Se alza de ti con sucesivo aliento.
Bebo la antigua magia y el acento,
Patria de la sonrisa y la manzana.

De tu verdor provengo y me alimento,
Del alba y de su risa de campana.
Es más dulce la música lejana
Que acerca a mi heredad la voz del viento.

En el recuerdo palpa la cadena
De la nostalgia el hijo verdadero
Y vuelve a tu remoto y fiel estío

Sigue cautiva y quieta tu sirena
En fuente donde el corazón viajero
La conoció al nacer: era el rocío.
"""
        
title = 'Tierra (V)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Yo no olvido tu sangre, ni tu herida,
Ni todo lo que en odio te sofoca.
Mi voz te busca y la mirada toca
La tristeza patente y la escondida.

Tu cicatriz en la memoria ardida
Aún sangra triste y mi piedad invoca,
Y tu dolor fatal no desemboca:
Llanto en el pecho, piedra contenida.

Espina en cada flor, sangriento rito,
Colibrí degollado, inaccesible
Tumba sin cruz, ni nombre en ella escrito,

¿quién te dictó destino tan terrible:
abandonarte a la heredad del grito
y a este vano correr tras lo imposible?
"""
        
title = 'Tierra (VI)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Me cae tu palabra hasta la boca
como una tempestad de hierro ardiendo,
como un golpe de mar, un sol muriendo
entre las fauces de un jaguar de roca.

Desciende a mí la carga con que invoca
todo el sentido de tu nombre abriendo
el cauce del recuerdo que va huyendo
hasta el origen que tu sangre evoca.

Me traes con el aire y el sonido
el rumor de tu risa y tus enojos,
y el dolor sin alivio en suelo herido;

Pero me das también en el oído
más palabras de rosas que de abrojos
que endulzan los saleros de los ojos.
"""
        
title = 'Tierra (VII)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """¿Y si vino y se fue? ¿Si ya ha venido
y en vano espera mi ansiedad despierta?
¿Y si acaso ha llegado hasta mi puerta
y la encontró cerrada y ha partido?

¿Si ha deshecho el camino ya vencido
-la fuerza desmayada, la fe muerta-
y a retomar la ruta el pie no acierta,
ni el ojo al horizonte recorrido?

Yo sigo aquí, por la esperanza atada,
y en vano espero ver la carabela
bajar el ancla en la tranquila rada.

E inquieto, el corazón se me rebela
porque no alcanza la ilusión amada
a volver con los remos y la vela.
"""
        
title = 'Tierra (VIII)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Abre tu corazón al aire, al cielo,
a la luz que tu dulce cáliz moja,
a la mejilla que el rubor sonroja,
a la brisa de audaz y abierto vuelo;

Al paso de la vida con su celo;
a la dicha, al dolor, a la congoja;
al devenir que entrega y que despoja;
a la brasa, a la pena, al gozo, al hielo.

Abre tu corazón, flor apacible,
corone tu violeta cada trino
y engalane la altura perecible.

En el dibujo de tu labio fino
hay un mensaje anónimo y legible
escrito con un beso cristalino.
"""
        
title = 'Flor de San Sebastián (Catleya skinneri)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Gota a gota en tu sangre, gota a gota
el sol desciende en silenciosa herida,
como si en el costado, abierta, ardida,
la luz vertieras por la vena rota.

Dolor que no se extingue, flor que brota
en la frente del cielo, espina hundida,
cauterio que deja detenida
la brasa de la flor que no se agota.

Te veo arder en tu tenaz hoguera,
encendiendo la tarde silencioso,
indiferente a la tormenta fiera.

Restañas con tus ramas, amoroso,
la moribunda fe de la quimera
que halló, en tu rama fiel, dicha y reposo.
"""
        
title = 'Árbol de fuego (Delonix regia)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Amor, y tú lo sabes, es venero
de profundas y dulces quemaduras,
y también tiene espinas tan seguras
que matan con el roce más ligero.

Amor hace lo eterno pasajero
y nos convierte en lámparas oscuras.
Nos hace contemplar dichas futuras
y nos regresa al polvo volandero.

amor fue tu canción y tu batalla
por vencer a la muerte y su letargo
y al labio que su red rendida calla.

Se endulzó tu canción, amor tan largo,
que ahora brota tu dulce amor amargo
como una inmensa flor que me avasalla.
"""
        
title = 'Locura Amor (I)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Cuando supere esta distancia ardida,
esta larga y doliente quemadura,
este golpe de hiel, esta tortura
de tu rosa en espina convertida;

cuando logre vencer la acometida
de la distancia que el dolor procura;
cuando imponga la luz a la locura
y logre revivir mi fe perdida;

entonces volveré a habitar el cielo
de tu abrazo deseado y presentido
en las espinas crueles del anhelo.

Volveré a la tibieza de ese nido
y en mi canto de renovado vuelo,
voy a gritarte amor hasta el olvido.
"""
        
title = 'Locura Amor (II)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """De repente la rosa se hizo llanto,
y el abrazo se convirtió en ausencia,
y el celo se cambió en indiferencia,
y el gozo más deseado fue quebranto.

Como una nube, se borró el encanto
que fascinó la luz de la conciencia
y obnubiló la flor de la experiencia
con su perfume que apreciara tanto.

¿Por qué no fue el engaño duradero?
¿Por qué sólo en la llama del sentido
se dibujó la llama porque muero?

No quiero que la arena del olvido
me haga pensar de todo lo que quiero:
-¿Y si sólo fue un sueño lo vivido?
"""
        
title = 'Locura Amor (III)'
date = 'S. XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

################
# New Author
################

author = "Ernestina de Chamourcín"
#data['author'] = author

### Sonnet
texto = """Inercia de la muerte. ¡Qué distancia
me aleja ya, segura, de lo humano!
Aquella rosa que murió en mi mano
será pronto recuerdo de fragancia.

Silencio de silencios. En mi estancia
diluye su perfil lo cotidiano
y retorna sin hieles a su arcano
esa amargura que la vida escancia.

Nada será de todo lo que ha sido.
Voy a ofrecer al sello del olvido
mis párpados febriles y mis labios

que inmoviliza el rictus de lo eterno.
¡Quiero escapar indemne del infierno
que arde en la trama de tus besos sabios!
"""
        
title = 'Huida'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Búscame en ti. La flecha de mi vida  
ha clavado sus rumbos en tu pecho  
y esquivo entre tus brazos el acecho  
de las cien rutas que mi paso olvida. 

Despójame del ansia desmedida  
que abrasaba mi espíritu en barbecho.  
El roce de tus manos ha deshecho  
la audacia de mi frente envanecida. 

Navegaré en tus pulsos. Dicha inerte  
del silencio total. Ávida muerte  
donde renacen, tuyos, mis sentidos. 

Ahoga entre tus labios mi tristeza,  
y esta inquietud punzante que ya empieza  
a taladrar mi sien con sus latidos. 
"""
        
title = 'La voz del viento'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


################
# New Author
################

author = "Carolina Coronado"
#data['author'] = author

### Sonnet
texto = """¿Cuál de las hijas del verano ardiente, 
cándida rosa, iguala a tu hermosura, 
la suavísima tez y la frescura 
que brotan de tu faz resplandeciente? 

La sonrosada luz de alba naciente 
no muestra al desplegarse más dulzura, 
ni el ala de los cisnes la blancura 
que el peregrino cerco de tu frente. 

Así, gloria del huerto, en el pomposo 
ramo descuellas desde verde asiento; 
cuando llevado sobre el manso viento 

a tu argentino cáliz oloroso 
roba su aroma insecto licencioso, 
y el puro esmalte empaña con su aliento. 
"""
        
title = 'La rosa blanca'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """¡Oh, cuál te adoro! Con la luz del día
tu nombre invoco, apasionada y triste,
y cuando el cielo en sombras se reviste
aun te llama exaltada el alma mía.

Tú eres el tiempo que mis horas guía,
tú eres la idea que a mi mente asiste,
porque en ti se encuentra cuanto existe,
mi pasión, mi esperanza, mi poesía.

No hay canto que igualar pueda a tu acento
cuando mi amor me cuentas y deliras
revelando la fe de tu contento;

tiemblo a tu voz y tiemblo si me miras,
y quisiera exhalar mi último aliento
abrasada en el aire que respiras.
"""
        
title = '¡Oh, cuál te adoro!'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

################
# New Author
################

author = "Victoriano Cremer"
#data['author'] = author

### Sonnet
texto = """Extenso mar, o renovado velo;
cuna del sueño, en la que el ser madura;
alondra vertical ganando altura
en la flotante música del vuelo.

Si látigo, te ciñes con anhelo.
Si beso, resplandece tu blancura
y la tierra redime su clausura
en la pradera extática del cielo.

De la raíz del hombre te alimentas,
de sus juegos más nobles, y le dejas
como una negra tierra fecundada.

¡Mírame ciego, Amor, buscando a tientas,
en un mundo de adioses y de rejas,
la salvadora luz de tu mirada!
"""
        
title = 'Amor'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1



################
# New Author
################

author = "Laura Victoria"
#data['author'] = author

### Sonnet
texto = """Ya ni versos escribo, sólo queda
este soñar de lágrimas teñido,
y una queja distante en el olvido
azul lejano de tu voz de seda.

Amor no es, es algo que remeda
la desmembranza del rosal caído,
donde ya ni las sombras hacen nido,
ni el viento en rondas de cristal enreda.

Algo que ayer fue lirio de mi fuente,
frescura de mi noche, y suavemente
luminar en mi senda florecida.

Algo que en mi agonía aún retengo,
porque es la única verdad que tengo
y no puedo arrancarla de mi vida.
"""
        
title = 'Amor no es...'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Te busco aún imagen ya perdida,
cegada luz, desorbitado viento,
esperanza tan sólo sostenida
por la ternura de mi pensamiento.

Algo tuyo quedose entre mi vida
como afilada flor de sufrimiento;
sangra mi llanto por tu propia herida
y sube tu canción por mi lamento.

Esa es la causa de mi mal cercano,
la certidumbre del inmenso hastío
que dobla las espigas de tu mano.

Porque tú eres la espuma de ese río
que nace en tus llanuras de verano
y muere en mis crepúsculos de frío.
"""
        
title = 'Cegada luz'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Yo misma no lo sé, pero vencida,
rendí a su orgullo mi virtud pagana,
y fui por un momento cortesana,
en el sarcasmo de mi propia vida.

Con beso ausente refresqué su herida,
absorta en él me le fingí lejana,
su voluntad despedacé liviana
y su pasión hallome arrepentida.

Fue un instante no más. Placer no hubo.
Pero su boca entre mi boca tuvo
amor y angustia, languidez y olvido.

Sobre el cansancio me tendí cobarde
y fui para su anhelo aquella tarde
tan grande y cruel como jamás lo he sido.
"""
        
title = 'Dualidad'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Amé constante a los que no me amaron
y les di la verdad cuando mintieron.
Mientras unos temblando me besaron
rogó mi beso a los que no quisieron.

Siempre busqué los que jamás me hallaron.
Mi voz llamó los que jamás me oyeron.
Y los que resignados me esperaron
nunca en mi copa de placer bebieron.

Hoy una voz abscóndita reclama
mi voluptuoso corazón de llama,
que limpio ardió como la brasa al viento.

Allá me voy. Torciendo mi camino
avanzo al horizonte de platino,
desnuda hasta del propio pensamiento.
"""
        
title = 'Otro rumbo'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Yo soy la plenitud, soy el estío.
Mi piel trigueña por el sol tostada,
tiene una leve amarillez de hastío
y un perfume de fruta sazonada.

Mi amor ondula como turbio río
por un valle de yerba calcinada,
y es mi beso perenne escalofrío
que aviva una celeste llamarada.

Amo el dolor porque el dolor es cumbre,
amo la vida que la vida es lumbre
si se perfila en páginas de fuego.

No me importan la vida ni el sarcasmo,
porque templo la fe de mi entusiasmo,
sobre la fragua del cupido ciego.
"""
        
title = 'Plenitud'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Pulpa de fruta que destila un vino
tinto de sombra en el lagar rosado,
dátil maduro, mora del camino,
granado en flor bajo el azul tostado.

Dientes más blancos que la flor de espino
y más menudos que el arroz cuajado.
Nievan en la sonrisa como el lino,
y son puñales de marfil tallado.

Boca, en sazón, perfecta, deleitosa,
que tiene a veces languidez de rosa
y ansia insaciable de recién nacido.

Ya que fuiste la copa de mi canto,
sella hoy mi beso desteñido en llanto
y ayúdame a partir hacia el olvido.
"""
        
title = 'Tu boca'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Quieres borrar con el sopor del vino
la hiel de olvido que dejé en tu boca,
y eres la polvareda en mi camino
y yo soy en tus vértigos la roca.

Es inútil que sigas mi destino
con el sarcasmo que tu pie provoca.
Yo fui para tu orgullo el torbellino,
y tú la inundación que se desboca.

Por eso para ahogar tus ambiciones,
te azotaré con risa en mis canciones,
y como esclavo te unciré a mis huellas.

Mientras que cien pupilas de mujeres,
te ofrecerán en lúbricos placeres
mi propia imagen deformada en ellas.
"""
        
title = 'Venganza'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

################
# New Author
################

author = "Concha Lagos"
#data['author'] = author

### Sonnet
texto = """Otra vez a soñar desde el oscuro
imposible por qué, mano tendida,
intentando apresar amor y vida,
fijarle a lo inseguro lo seguro.

Otras veces cabalgando hacia tu muro,
soledad que me tiras de la brida,
seguidora incansable de mi huida,
vencedora en la lucha en que perduro.

Otra vez a mirar arena y cielo
en tu playa sin fin siempre desnuda,
bebiéndome el silencio que te nombra.

Otra vez como ayer perdido el vuelo
por el salto hacia atrás de miedo y duda,
seguida y seguidora de tu sombra.
"""
        
title = 'Otra vez a soñar desde el oscuro...'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Urgente la presencia te reclamo,
eje te quiero de mi todavía,
la espuma de tu orilla por la mía
ascendiendo sedienta tramo a tramo.

Prolongado oleaje del te amo
que de mi playa aleje la agonía.
Por volverlo a escuchar deshojaría
hasta el último sueño de mi ramo.

Vuelve y vuelve otra vez, vuelve a cantarme,
repíteme el compás a cada hora,
quédate detenido en mi presente.

Hoy sé que una campana va a sonarme
anunciando la vuelta de otra aurora
la razón de esta lucha por mi frente.
"""
        
title = 'Por volverlo a escuchar'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


################
# New Author
################

author = "Concha Urquiza"
#data['author'] = author

### Sonnet
texto = """Aunque tu nombre es tierno como un beso
y trasciende como óleo derramado,
y tu recuerdo es dulce y deseado,
rica fiesta al sentido y embeleso;

y es gloria y luz, Amor, llevarlo impreso
como un sello en el alma dibujado,
no basta al corazón enamorado
para alcanzar la vida todo eso.

Ya sólo, Amor, perdido en tus abrazos,
cabe tu pecho detendrá su empeño:
no aflojará las redes y los lazos,

verá la paz ni gozará del sueño,
hasta que tenga paz entre tus brazos
y duerma en el regazo de su Dueño.
"""
        
title = 'Aunque tu nombre es tierno como un beso...'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """¡Oh Betsabé, simbólica y vehemente!
Con doble sed mi corazón heriste
Cuando la llama de tu cuerpo hiciste
Duplicarse en la onda transparente.

Cerca el terrado y el marido ausente,
¿quién a la dicha de tu amor resiste?
No en vano fue la imagen que me diste
Acicate a los flancos y a la mente.

¡Ay de mí, Betsabé, tu brazo tierno,
traspasado de luz como las ondas,
lió mis carnes a dolor eterno! 

¡Qué horrenda sangre salpicó mis frondas!
¡En qué negrura y qué pavor de invierno
se ahogó la luz de tus pupilas blondas!
"""
        
title = 'David'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Del ser que alienta y del color que brilla
me separa tu cálida presencia,
clausurando el sentido en la vehemencia.
de una noche sin fondo y sin orilla.

En ella mi tortuosa pesadilla
te confiere su trágica opulencia,
y tórnase inmortal como una esencia,
siendo que eres trivial como una arcilla.

Te he engendrado en mi lumbre y mi universo,
en tu forma plural he proyectado
la queja vaga y el afán disperso.

Dudando está el espíritu sitiado
si eres mi sangre disculpada en verso
o mi dolor en carne figurado.
"""
        
title = 'Del ser que alienta y del color que brilla...'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Palidez consumada en el deseo,
suma de carne transparente y fina,
ya sellada, en profética rutina,
para el soldado y para el can hebreo.

¡Oh desahuciada fiebre, oh devaneo
que oscila como péndulo en rüina,
de un viñedo que el sol mimba y fulmina
a cruenta gloria y militar trofeo!

Horror de pausa y de silencio, acaso
para no conocer turbias carreras
del corazón, hacia el fatal ocaso,

ni sentir que en sus válvulas arteras
se endulza ya la sangre paso a paso
para halagar las fauces de las fieras.
"""
        
title = 'Jezabel'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Hazme saber, Amor, dónde apacientas,
dó guías tus rebaños, dónde vagas,
no huelle tras las ínsulas aciagas
las rutas de la tarde cenicientas.

Tu grey, oh tierno Amor, dó la sustentas
y con pastos riquísimos halagas,
mientras mi torpe corazón amagas
con sendas largas, y con horas lentas.

No principie a seguir de los pastores
los dispersos rebaños. Vida mía;
muestra, lejos, el sol de tus amores;

¡dime dónde apacientas todavía!,
y seguiré tu rastro entre las flores,*
por los fuegos del áureo mediodía.
"""
        
title = 'La canción de Sulamita'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Mi cumbre solitaria y opulenta
declinó hacia tu valle tenebroso,
que oro de espiga ni frescor de pozo
ni pajarera gárrula sustenta.

En tu luz gravitante y macilenta,
quebrado el equilibrio del reposo,
vago sobre tu espíritu medroso
como un jirón de bruma cenicienta.

Libre soy de tornar a mis alcores
do Eros impúber la zampoña toca
ceñido de corderos y pastores;

mas a exilio perpetuo me provoca
la chispa de tus ojos turbadores,
la roja encrespadura de tu boca.
"""
        
title = 'Mi cumbre solitaria y opulenta...'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Miente mi corazón cuando te ama,
hecho intérprete fiel de mi sentido,
como el eco en abismo percibido
que el viento, no la voz, forma y derrama.

Este imperioso afán que te reclama
no en el centro del alma fue nutrido:
me ha turbado sin mí, como el sonido,
es ajeno a mi ser, como la llama.

Cuando la sangre el corazón satura
de sólo tu sabor -término medio
en loco silogismo de amargura-,

inaccesible al implacable asedio,
como trozo de plomo en agua obscura
húndese el alma en silencioso tedio.
"""
        
title = 'Miente mi corazón cuando te ama...'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Hoja a hoja la tierna primavera
el verdor de los campos restituye
y, desatado de los hielos, huye
el arroyo burlando la pradera.

Despierto ayer a la canción primera,
el salvaje gorrión el ala intuye
y por la luz que se derrama y fluye
sube y baja la escala pajarera.

Ya la amapola su fulgor deshoja
y el dientecillo su dorada pluma;
todo a la fiesta del color se arroja;

sólo en el claro azul, que nada bruma,
flota una nube desgarrada y floja
cual recinto brevísimo de espuma.
"""
        
title = 'Primavera'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Quiero decir que te amo y no lo digo
aunque bien siento el corazón llagado,
porque para mi mal tengo probado
que soy tibio amador y flaco amigo.

No amarte más es culpa y es castigo,
que de ansias de tu amor me has abrasado,
y con sólo dejarme en mi pecado
extremas tu rigor para conmigo.

Sólo quiero vivir para buscarte,
sólo temo morir antes de hallarte,
sólo siento vivir cuando te llamo;

y, aunque vivo ardiendo en vivo fuego,
como la entera voluntad te niego
no me atrevo a decirte que te amo.
"""
        
title = 'Quiero decir que te amo y no lo digo...'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """La quieta soledad, el lecho oscuro
De inmortales tinieblas coronado,
El silencio en la noche derramado,
Y el cerco de la paz, ardiente y puro.

Ruth detiene el aliento mal seguro, 
Descubre el rostro de dolor turbado,
Y por largos anhelos agitado
Con dura mano oprime el seno duro. 

Duerme Booz en tanto; su sentido,
En misterioso sueño sumergido, 
La presencia tenaz de Ruth ignora. 

Mas su despierto coraz ó n medita..
Y la noche fugaz se precipita 
Hacia los claros lechos de la aurora.
"""
        
title = 'Ruth'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Atraída al olor de tus aromas
y embriagada del vino de tus pechos,
olvidé mi ganado en los barbechos
y perdí mi canción entre, las pomas.

Como buscan volando las palomas
las corrientes mecidas en sus lechos,
por el monte de cíngulos estrechos
buscaré los parajes donde asomas.

Ya por toda la tierra iré perdida,
dejando la canción abandonada,
sin guarda la manada desvalida,

desque olvidé mi amor y mi morada,
al olor de tus huertos atraída,
del vino de tus pechos embriagada.
"""
        
title = 'Sulamita'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Hay en tus ojeras luna diluida
y olor de jazmines, y triste cantar,
la nostalgia en ellas quedóse dormida,
disuelta en las perlas de un dulce llorar...

Cuando lloras cantan tus lágrimas puras
los himnos sagrados que Eros formó,
y hay en tus arcanas pupilas oscuras
los hondos misterios que Apolo cantó.

Desmayan los sueños en sus tristes rasos
que mudos semejan pálidos ocasos...
pálidos ocasos de riente ilusión...

Mientras sus hogueras tus labios encienden
y tus dos ojeras en tu rostro prenden
el lirio azul pálido de su corazón...
"""
        
title = 'Tus ojeras'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Un soñar con el pálido ramaje
y las llanuras donde cuaja el trigo,
un aspirar a soledad contigo
por los húmedos valles y el boscaje:

un buscar la región honda y salvaje,
un desear poseerte sin testigo,
un abrazado afán de estar conmigo
viendo tu faz en interior paisaje:

tal fue mi juventud más verdadera;
en el clima ideal de tu dulzura
maduró mi divina primavera:

y tuve mi esperanza tan segura,
como que en la hermosura pasajera
se me entregaba, intacta, Tu hermosura.
"""
        
title = 'Un soñar con el pálido ramaje...'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Ya corre el corazón por este suelo
Como antes del remanso el agua impura:
Aún lleva tierras en la entraña obscura
Y pretende copiar la faz del cielo. 

Van creciendo el dolor y el anhelo,
La corriente se turba y se apresura, 
Y es fuente el sedimento de amargura 
Más que las alas con que intenta el vuelo.

Si tendieras la mano solamente 
Y el agua temblorosa se aquietara,
Ya, contemplando el cielo largamente,

¡Oh Deseado!, el corazón dejara
flotar sobre su sueño transparente
la divina belleza de tu cara.
"""
        
title = 'Ya corre el corazón por este suelo...'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


################
# New Author
################

author = "Gerardo Diego"
#data['author'] = author

### Sonnet
texto = """Dentro, en tus ojos, donde calla y duerme
un palpitar de acuario submarino,
quisiera - licor tenue al difumino -
hundirme, decantarme, adormecerme.

Y a través de tu espalda, pura, inerme,
que me trasluce el ritmo de andantino
de tu anhelar, si en ella me reclino,
quisiera trasvasarme y extenderme.

Multiplicar mi nido en tus regazos
innumerables, que al cerrar los brazos
no encontrases mi carne, en ti disuelta.

Y que mi alma, en bulto y tacto vuelta,
te resbalase en torno, transparente
como tu frente, amor, como tu frente.
"""
        
title = 'Amor'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Tú y tu desnudo sueño. No lo sabes. 
Duermes.  No. No lo sabes. Yo en desvelo, 
y tú, inocente, duermes bajo el cielo. 
Tú por tu sueño, y por el mar las naves.

En cárceles de espacio, aéreas llaves 
te me encierran, recluyen, roban. Hielo, 
cristal de aire en mil hojas. No. No hay vuelo 
que alce hasta ti las alas de mis aves.

Saber que duermes tú, cierta, segura 
- cauce fiel de abandono, línea pura -, 
tan cerca de mis brazos maniatados.

Qué pavorosa esclavitud de isleño, 
yo, insomne, loco, en los acantilados, 
las naves por el mar, tú por tu sueño.
"""
        
title = 'Insomnio'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Déjame acariciarte lentamente,
déjame lentamente comprobarte,
ver que eres de verdad, un continuarte
de ti misma a ti misma extensamente.

Onda tras onda irradian de tu frente
y mansamente, apenas sin rizarte,
rompen sus diez espumas al besarte
de tus pies en la playa adolescente.

Así te quiero, fluida y sucesiva,
manantial tú de ti, agua furtiva,
música para el tacto perezosa.

Así te quiero, en límites pequeños,
aquí y allá, fragmentos, lirio, rosa,
y tu unidad después, luz de mis sueños.
"""
        
title = 'Sucesiva'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Tú me miras, amor, al fin me miras
de frente, tú me miras y te entregas
y de tus ojos líricos trasiegas
tu inocencia a los míos. No retiras

tu onda y onda dulcísima, mentiras
que yo soñaba y son verdad, no juegas.
Me miras ya sin ver, mirando a ciegas
tu propio amor que en mi mirar respiras.

No ves mis ojos, no mi amor de fuente,
miras para no ver, miras cantando
cantas mirando, oh música del cielo.

Oh mi ciega del alma, incandescente,
mi melodía en que mi ser revelo.
Tú me miras, amor, me estás mirando.
"""
        
title = 'Tú me miras, amor, al fin me miras...'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

################
# New Author
################

author = "José Hierro"
#data['author'] = author

### Sonnet
texto = """Llegué por el dolor a la alegría.
Supe por el dolor que el alma existe.
Por el dolor, allá en mi reino triste,
un misterioso sol amanecía.

Era alegría la mañana fría
y el viento loco y cálido que embiste.
( Alma que verdes primaveras viste
maravillosamente se rompía. )

Así la siento más. Al cielo apunto
y me responde cuando le pregunto
con dolor tras dolor para mi herida.

Y mientras se ilumina mi cabeza
ruego por el que he sido en la tristeza
a las divinidades de la vida.
"""
        
title = 'Alegría'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """En mí la siento aunque se esconde. Moja
mis oscuros caminos interiores.
Quién sabe cuántos mágicos rumores
sobre el sombrío corazón deshoja.

A veces alza en mí su luna roja
o me reclina sobre extrañas flores.
Dicen que ha muerto, que de sus verdores
el árbol de mi vida se despoja.

Sé que no ha muerto, porque vivo. Tomo,
en el oculto reino en que se esconde,
la espiga de su mano verdadera.

Dirán que he muerto, y yo no muero.¿Cómo
podría ser así, decidme, dónde
podría ella reinar si yo muriera?
"""
        
title = 'Alegría Interior'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Una esfinge pigmea. Se diría
que no está aquí: no ve, ni oye, ni huele.
Esta no es una Marta que currele,
sino María de la fantasía.

Susurra. Hormiga china, todavía
no distingue la erre de la ele.
Posiblemente un día se rebele
su Marta agazapada en su María.

Entonces, cara y cruz por siempre unidas,
sin eses de costuras descocidas,
Martamaría cantará su dúo.

Pero mientras no ocurra tal encuentro
es un búho que mira desde dentro
de un búho que está dentro de otro búho.
"""
        
title = 'La impasible María con erres, eles y eses'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """No vives ya de ainrazones.
¿Tan sola estabas, alma mía?
El alba nueva no traía,
para acunarte, sus canciones.

Llega la luz de otras regiones
sin la hermosura que solía.
Mala alegría es la alegría
que nos abrasa los corazones.

¿Dentro de ti la buscas? ¿Llevas
dentro de ti su llama? ¿Elevas
de tu noche su mediodía?

¿Has de matar todas las cosas?
¿Cortar, para olerlas, las rosas?
¿Tan sola estabas, alma mía?
"""
        
title = 'Razones'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Es una rubia furia desatada,
gatea, sube y baja, embiste, grita.
Cléndula que araña, uñas de pita,
torito bravo, más: una manada.

Comedora de flores desmadrada,
Vesubio en miniatura. Es la rayita
que no cesa, pimienta y dinamita,
torbellinita desencadenada.

¿La imagináis durmiendo una muñeca?
La Bubu es domadora, es carateca,
pulgón y filoxera de la vida.

¡Ay madre mía, cuando tenga dientes!
Prepárense sus deudos y parientes.
(Y aún creen sus padres que esto es una niña!)
"""
        
title = 'Soneto'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Por qué te olvidas y por qué te alejas
del instante que hiere con su lanza.
Por qué te ciñes de desesperanza
si eres muy joven, y las cosas viejas.

Las orillas que cruzas las reflejas;
pero tu soledad de río avanza.
Bendita forma que en tus aguas danza
y que en olvido para siempre dejas.

Por qué vas ciego, rompes, quemas, pisas,
ignoras cielos, manos, piedras, risas.
Por qué imaginas que tu luz se apaga.

Por qué no apresas el dolor errante.
Por qué no perpetúas el instante
antes de que en tus manos se deshaga.
"""
        
title = 'Variaciones sobre el instante eterno'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Después de todo, todo ha sido nada,
a pesar de que un día lo fue todo.
Después de nada, o después de todo
supe que todo no era más que nada.

Grito «¡Todo!», y el eco dice «¡Nada!»
Grito «¡Nada!», y el eco dice «¡Todo!»
Ahora sé que la nada lo era todo.
y todo era ceniza de la nada.

No queda nada de lo que fue nada.
(Era ilusión lo que creía todo
y que, en definitiva, era la nada.)

Qué más da que la nada fuera nada
si más nada será, después de todo,
después de tanto todo para nada.
"""
        
title = 'Vida'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


################
# New Author
################

author = "José Hierro"
#data['author'] = author

### Sonnet
texto = """Llegué por el dolor a la alegría.
Supe por el dolor que el alma existe.
Por el dolor, allá en mi reino triste,
un misterioso sol amanecía.

Era alegría la mañana fría
y el viento loco y cálido que embiste.
( Alma que verdes primaveras viste
maravillosamente se rompía. )

Así la siento más. Al cielo apunto
y me responde cuando le pregunto
con dolor tras dolor para mi herida.

Y mientras se ilumina mi cabeza
ruego por el que he sido en la tristeza
a las divinidades de la vida.
"""
        
title = 'Alegría'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


################
# New Author
################

author = "Vicente Aleixandre"
#data['author'] = author

### Sonnet
texto = """Pensamiento apagado, alma sombría,
¿quién aquí tú, que largamente beso?
Alma o bulto sin luz, o letal hueso
que inmóvil consumió la fiebre mía.

Aquí ciega pasión se estrelló fría,
aquí mi corazón golpeó obseso,
tercamente insistió, palpitó opreso.
Aquí perdió mi boca su alegría.

Entre mis brazos ciega te he tenido,
bajo mi pecho respiraste amada
y en ti vivió mi sangre tu latido.

Oh noche oscura. Ya no espero nada.
La soledad no miente a tu sentido.
Reina la pura sombra sosegada.
"""
        
title = 'Sombra final'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


################
# New Author
################

author = "Jorge Guillén"
#data['author'] = author

### Sonnet
texto = """Este soñar a solas... ¡Si tu vida
de pronto amaneciese ante mi espera!
¿Por dónde voy cayendo? Primavera,
mientras, en tomo mío dilapida

su olor y se me escapa en la caída.
¡Tan solitariamente se acelera
-y está la noche ahí, variando fuera-
la gravedad de un ansia desvalida!

Pero tanto sofoco en el vacío
cesará. Gozaré de apariciones
que atajarán el vergonzante empeño

de henchir tu ausencia con mi desvarío.
¡Realidad, realidad, no me abandones
para soñar mejor el hondo sueño!
"""
        
title = 'El hondo sueño'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Ya se alargan las tardes, ya se deja
despacio acompañar el sol postrero
mientras él, desde el cielo de febrero,
retira al río la ciudad refleja

de la corriente, sin cesar pareja
-más todavía tras algún remero-
a mí, que errante junto al agua quiero
sentirme así fugaz sin una queja,

viendo la lentitud con que se pierde
serenando su fin tanta hermosura,
dichosa de valer cuando más arde

-bajo los arreboles- hasta el verde
tenaz de los abetos y se apura
la retirada lenta de la tarde.
"""
        
title = 'Ya se alargan las tardes, ya se deja...'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1

### Sonnet
texto = """Miro hacia atrás, hacia los años, lejos, 
Y se me ahonda tanta perspectiva 
Que del confín apenas sigue viva 
La vaga imagen sobre mis espejos. 

Aun vuelan, sin embargo, los vencejos 
En torno de unas torres, y allá arriba 
Persiste mi niñez contemplativa. 
Ya son buen vino mis viñedos viejos. 

Fortuna adversa o próspera no auguro. 
Por ahora me ahínco en mi presente, 
Y aunque sé lo que sé, mi afán no taso. 

Ante los ojos, mientras, el futuro 
Se me adelgaza delicadamente, 
Más difícil, más frágil, más escaso.
"""
        
title = 'Del transcurso'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Alguna vez me angustia una certeza,
y ante mí se estremece mi futuro.
Acechándolo está de pronto un muro
del arrabal final en que tropieza

La luz del campo. ¿Mas habrá tristeza
si la desnuda el sol?. No, no hay apuro
todavía. Lo urgente es el maduro 
fruto. La mano ya lo descorteza.

... Y un día entre los días el más triste
será. Tenderse deberá la mano
sin afán. Y acatando el inminente

poder diré sin lágrimas: embiste,
justa fatalidad. El muro cano 
va a imponerme su ley, no su accidente.
"""
        
title = 'Muerte a lo lejos'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


### Sonnet
texto = """Pasa el tiempo y suspiro porque paso,
aunque yo quede en mí, que sabe y cuenta,
y no con el reloj, su marcha lenta
nunca es la mía bajo el cielo raso.

Calculo, sé, suspiro, no soy caso
de excepción y a esta altura, los setenta,
mi afán del día no se desalienta,
a pesar de ser frágil lo que amaso.

Ay, Dios mío, me sé mortal de veras.
Pero mortalidad no es el instante
que al fin me privará de mi corriente.

Estas horas no son las postrimeras,
y mientras haya vida por delante,
serás mis sucesiones de viviente.
"""
        
title = 'Pasa el tiempo y suspiro porque paso...'
date = 'S.XX'
poem = {'text':texto, 'title':title, 'date':date, 'author':author}
data[i] = poem
i += 1


########
# Save info
########

with open('{0}.json'.format(OTHER_SONNETS + "/dct_sonnets_sxx"), 'w') as fp:
    json.dump(data, fp)