
## Directory / file structure decoding

### Synthesis dataset
MII_LIEPA_SYN_V*

* **Aiste** voice id Aiste
  * data
    * 0.wav
      * 0 - utterance id

### Recognition dataset
MII_LIEPA_REC_V*

* **D10** voice id 10 (LT **D**iktorius)
  * **S001** sentence group 001
    * S010Mi_001_01.wav
      * S - sentece (LT **S**akinys)
      * 010 - voice id
      * M - female (LT **M**oteris)
      * i – Age group
      * 001 - sentence group
      * 01 - recording numerber within group
  * **Z010** word or command group 010
    * Z010Mi_001_00.wav
      * Z - word or command (LT **Ž**odis)
      * 010 - voice id
      * M - female
      * i – Age group
      * 001 - word or command group
      * 00 - recording numerber within group
* **D150** voice id 150
  * **S039** sentence group 039
    * S150Vm_039_01.wav
      * S - sentece
      * 150 - voice id
      * V - male (LT **V**yras)
      * m – Age group
      * 039 - sentence group
      * 01 - recording numerber within group

### Age groups
* **c** - 12
* **d** - 13
* **e** - 14
* **f** - 15
* **g** - 16
* **h** - 17
* **i** - 18
* **j** - 19
* **k** - 20
* **l** - 21 to 25
* **m** - 26 to 30
* **n** - 31 to  40
* **o** - 41 to 50
* **p** - 51 to 60
* **r** - Above 61
