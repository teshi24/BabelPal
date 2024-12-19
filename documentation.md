# Dokumentation BablePal
## Technischer Aufbau
![diagram aufbau](img/aufbau_babelpal.jpg)

Die selber implementierte Funkionalität vom BabelPal ist aufgeteilt in zwei verschiedene Laufzeitumgebungen.
Auf einer VM ist die spezifische Python Version 2.7 installiert, die Pepper voraussetzt. Darauf sind alle Features rund um Pepper implementiert: die Bewegungen für das Nicken, das Anschauen der Personen, die animierte Sprache inklusive Gestik und die Steuerung vom Tablet.
Auf einer weiteren Umgebung ist die Funktionalität vom Speech-To-Text und die Übersetzung implementiert. Diese wird über eine API zur Verfügung gestellt. 
Dieser Aufbau wurde gewählt, um für die Sprache- und Übersetzungsfunktionalität unabhängig von der Python-Version 2.7 sein zu können. 

## Speech Translation API
This API provides endpoints to start a speech-to-text conversion via the internal microphone and receive a translated text once the stop endpoint is called. See OpenAPI specification [here](swagger.yaml)

### /start

#### GET
##### Summary:

Start the recording for speech-to-text

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| language | query | Language which is spoken | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successfully started the speech-to-text |

### /stop

#### GET
##### Summary:

Stop the speech-to-text and return the text translated into the provided language

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| language | query | Language the recorded text should be translated into | Yes | string |

##### Responses

| Code | Description                         |
| ---- |-------------------------------------|
| 200 | successful stop and translated text |



## Umsetzung Mimik und Gestik
Damit Pepper während dem Sprechen die richtige Person anschaut, wurde folgender Ablauf implementiert:
1. Beim Start von einem Satz berührt man den Kopf von Pepper
2. Beginnt man dann zu sprechen, versucht Pepper über die API **ALSoundLocalization** den Standort der Person auszumachen. 
3. Die erste erhaltene Position wird fixiert und wir lassen Pepper in diese Richtung schauen.
4. Sobald der Kopf die Position gewechselt hat, beginnt Pepper zwischenzeitlich zu Nicken, um zuhören zu signalisieren
5. Beendet die erste Person seinen Sprach-Input über eine weitere Kopfberührung, wird der Kopf in die Startposition zurückbewegt und dann lassen wir Pepper im selben Winkel in die entgegengesetzte Richtung blicken.
 ![diagram personen anschauen](img/people_percept.jpg)
6. Pepper gibt den übersetzten Text wieder. Während dem Sprechen gestikuliert Pepper im 'contextual' Modus.
7. Wenn Pepper fertig gesprochen hat, wird der Roboter in die Standardposition zurückgeführt, um unnatürliche fixierte Armhaltungen zu vermeiden.
### Abgrenzung  
Die Kopfdrehungen basieren auf der Annahme, dass sich jeweils zwei Personen unterhalten und diese zusammen mit Pepper in einem Dreieck aufgestellt haben. 
Diese Annahme ist momentan nötig, da die Person, welche noch nicht gesprochen hat von Pepper sonst nicht aufgefunden werden kann.
Wahrscheinlich könnte diese Detektion mit den APIs **ALPeoplePerception** und **ALFaceDetection** verbessert werden.
### Simultane Befehle durch Multithreading
Pepper muss bei den Steps 2.-5. gleichzeitig auf den beendenden Touch-Event hören und die Kopfbewegungen ausführen.
Damit auf den von Pepper emittete Touch-Event reagiert werden kann, dürfen die Kopfbewegungen kein blockierender Call sein.
Deshalb wurde dieser Teil der Applikation mit Multithreading eingebaut. Beim ersten Touch-Event wird der Thread gestartet, welcher die Person detektiert, den Kopf dreht und das Nicken startet. Ausserdem wird das 'is_listening'-Flag im Roboter gesetzt.
Beim zweiten Touch-Event wird das Flag zurückgesetzt. Dieses wird innerhalb des Threads regelmässig abgefragt und führt beim Zurücksetzen zur Beendigung des Threads und damit der Kopfbewegungen. Das Flag wird mit einem Lock thread-save behandelt, da es in 2 Threads verwendet wird.

Die Bewegung im Punkt 5 braucht keinen eigenen Thread, da während dem Wiedergeben der Übersetzung auf keinen Touch-Event gehört werden muss. Es wird erwartet, dass die andere Person zuerst zuhört, bevor sie selbst sprechen will.

## Umsetzung Tablet Interaktionen
Für die Umsetzung der Tabletinputs wurde eine pixelbasierete Variante gewählt. Das heisst, zu Beginn haben wir für jeden möglichen Screen ein passendes Bild erstellt.

Einmal für die Startauswahl:  
  <img src="img/language_selection.png" width="400">
   
Und jeweils für jede Sprachkombination, zum Beispiel Deutsch --> Spanisch:  
 <img src="img/german_spanish.png" width="400">

 Danach wird über die Koordinaten X / Y festgelegt, ob eine Fläche berührt worden ist oder nicht:
  <img src="img/tablet_pixel.jpg" width="400">

Die einzelnen Randpunkte für die Flächen können jeweils über eine Berührung ausgelesen werden und danach fix codiert werden. Dieser Ansatz ist sehr simple und funktioniert für solche wenigen Inputs gut. Steigt jedoch die Komplexität muss dieser Ansatz überdenkt werden.