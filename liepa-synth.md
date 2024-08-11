# Projektas LIEPA
Projektą LIEPA („Lietuvių šneka valdomos paslaugos“) vykdė Vilniaus universitetas kartu su
partneriais 2013–2015 metais. Vykdant projektą buvo sukurtas keturių balsų sintezatorius.
Specialiai stengtasi, kad balsai būtų kuo skirtingesni, todėl sukurtas jaunatviškas moteriškas, jaunatviškas vyriškas, vyresnio amžiaus moteriškas ir vyresnio amžiaus vyriškas balsai. Balsai vadinami atitinkamai: ``Aistė (diktorė Aistė Diržiūtė)``, ``Edvardas (Edvardas Kubilius)``,
``Regina (Regina Jokubauskaitė)`` ir ``Vladas (Vladas Bagdonas)``.
Sintezei naudojamas vienetų parinkimo algoritmas, t. y. sudarytos kiekvieno diktoriaus ištisinių įrašų bazės. Jų apimtis: nuo 483 iki 577 MB, t. y. nuo 3 val. 2 min. iki 3 val. 38 min. arba
šiek tiek daugiau nei 5000 sakinių, kuriuose – daugiau kaip 161 tūkst. garsų.
Projekto LIEPA balsų galima pasiklausyti svetainėje LIEPA – Teksto sintezatorius. Balsai Regina
ir Edvardas buvo specialiai pritaikyti akliesiems, juos galima parsisiųsti iš svetainės LIEPA –
Sintezatorius akliesiems ir įsidiegti kompiuteryje. Be to, balsas Regina „skaito“ Lietuvos žinias,
balsai Aistė ir Edvardas „vaidino“ trupės Rimini Protokoll spektaklyje Remote Vilnius, visi keturi
balsai „įdarbinti“ paslaugoje RoboBraille, kurios esmė tokia: el. paštu nusiuntus tekstinį failą
adresu regina@robobraille.org, edvardas@robobraille.org, aiste@robobraille.org arba vladas@robobraille.org gaunama nuoroda į atitinkamu balsu susintezuotą garso failą.


Kiekvienas sintezatorius kuriamas remiantis konkretaus žmogaus balso parametrais, t. y.
stengiamasi, kad sintezatoriaus balsas būtų panašus į to žmogaus balsą. Taigi visų pirma
reikia pasirinkti diktorių. Visuotinai sutariama, kad nuo diktoriaus parinkimo priklauso galutinė sintezuoto balso kokybė. Huang ir kt. (2001, p.800) teigia, kad diktoriaus parinkimas
nulemia iki 0,3 balo subjektyvioje penkiabalėje MOS (angl. mean opinion score) skalėje. Nors
diktoriaus parinkimas svarbus, tačiau literatūros apie tai yra labai nedaug (Syrdal ir kt., 1998;
Braga ir kt., 2007).

Bragos ir kt. (2007) išsamiai aprašyta diktorės atranka portugalų kalbos sintezatoriui. Pirmiausiai iš 485 kandidačių atrinktos 74 remiantis anketiniais duomenimis (gimtoji kalba,
išsilavinimas, diktoriaus darbo patirtis ir t. t.). Iš pastarųjų diktorių atsiųstų balso pavyzdžių
remiantis subjektyviais testais atrinkta 12 kandidačių. Subjektyvių testų metu klausytojai
penkiabalėje sistemoje vertino tokius parametrus kaip balso malonumas, suprantamumas,
tartis, kirčiavimas, išraiškingumas, išskirtinumas, jausmingumas, tinkamumas skaityti naujienas, instrukcijas, el. pašto laiškus ir pan. Galiausiai visos diktorės vienodomis įrašymo
sąlygomis perskaitė tą patį tekstą (219 žodžių). Galutiniam vertinimui taip pat galima panaudoti subjektyvius testus, tačiau egzistuoja ir objektyviai apskaičiuojami parametrai, kurie
koreliuoja su subjektyviais vertinimais, pavyzdžiui, žmonėms patinka moteriški balsai, kurių
pagrindinio tono vidurkis yra nuo 186 iki 206 Hz, arba, kai dusliųjų segmentų (garsų /s/, /š/)
energija yra didelė lyginat su skardžiųjų segmentų energija (Syrdal ir kt., 1998). Dar vienas
būdas – tai atlikti bandomąją sintezę ir subjektyviai įvertinti rezultatą. Tam galima tiesiog
modifikuoti signalo pagrindinį toną ir (arba) garsų trukmę (Braga ir kt., 2007) arba iškirpti
tam tikrą aibę difonų ir juos perstatant susintezuoti kelias frazes (Syrdal ir kt., 1998). Subjektyviai įvertinus paaiškėja, kad vieni balsai tokioms modifikacijoms atsparesni už kitus, o
sintezėje tai svarbu.

Tiek kuriant SINT.AS, tiek projekte LIEPA į atranką buvo kviečiami tik profesionalūs diktoriai
ir aktoriai, taigi galima teigti, kad buvo atliekamas tik paskutinis atrankos etapas. Sintezatoriui SINT.AS moteriškas balsas atsirinktas iš 6-ių kandidatų, o vyriškas balsas – iš 3-jų. Į
atranką buvo kviečiama visa diktorių grupė ir iš jų išsirenkamas geriausias. Projekte LIEPA
diktoriai į atranką buvo kviečiami po vieną. Atranka buvo nutraukiama radus bent minimalius
reikalavimus tenkinantį diktorių. Taip buvo siekiama sumažinti į atranką kviečiamų diktorių skaičių. Kaip vyresnis moteriškas balsas pakviesta SINT.AS atrankoje dalyvavusi diktorė,
kaip vyresnis vyriškas balsas pasirinktas atrankoje ketvirtuoju dalyvavęs kandidatas, likusių
dviejų balsų atrankose dalyvavo po 3-is kandidatus.
SINT.AS atrankoje diktoriai turėjo perskaityti specialų 13 sakinių tekstą (309 garsai), kuriame
visi 92 fonemų sistemos garsai panaudoti bent po vieną kartą. Projekto LIEPA atrankoje šis
tekstas dar papildytas 7 sakiniais (339 garsais) su balsių junginiais, taip pat 14 sakinių (491
garsu) su sprogstamųjų priebalsių junginiais. Diktoriai atrinkti pagal tokius kriterijus:
_ Pagrindinio tono monotoniškumas;
_ Sklandus balsių jungimas;
_ Aiškus garsų artikuliavimas, ypač sakinių pabaigoje;
_ Signalo formos paprastumas: ar lengva vizualiai įžiūrėti pagrindinio tono periodus, garsų
ribas;
_ Ar balsai pakankamai skirtingi (projekte LIEPA).

Vienetų parinkimo metodas pirmą kartą pasiūlytas Hunt ir Black (1996). Jis naudoja anotuotus ištisinius diktoriaus balso įrašus. Sintezuojant idealiu atveju galima rasti ir visą įrašytą sakinį, o nepavykus imami mažesni segmentai, blogiausiu atveju sintezuotas įrašas
suklijuojamas iš atskirų fonemų. Tinkamiausi įrašo segmentai parenkami remiantis garsų
keitimo ir garsų jungimo kainomis, kainų prasmę iliustruoja toliau pateiktas pavyzdys. Kainos gali būti apskaičiuojamos remiantis įvairiais akustiniais arba fonologiniais požymiais,
arba įvairiais jų deriniais (Taylor, 2009, p.512). Kuriant lietuviškus vienetų parinkimu grįstus
sintezatorius buvo pasinaudota Yi ir Glass (2002) pasiūlytais fonologiniais požymiais. Vienetų
parinkimo algoritmas išsamiau aprašytas Kasparaičio ir Anbinderio (2014).
Panagrinėkime pavyzdį. Tarkime, norime susintezuoti sakinį Vãsara Palangojè. Projekto LIEPA garsų bazėse yra toliau pateikti penki sakiniai, iš kurių ir paimami reikiami segmentai:

Vãsara Palangojè
 Vãsaros jūra nuplóvė spalvàs
 Ẽglė Sarapáitė ir Giẽdrė Paugáitė
kad visi kiti jaũčia tikrą paláimą
 herefòrdų, aberdinų, angùsų
 ar prisimeni nãgą žaliojè lankojè
 
Galima pastebėti, kad žodis Palangojè yra paskutinis sakinyje, todėl ir segmentai jam
imami iš paskutinių sakinių žodžių. Žodis Vãsara yra pirmas sakinyje, todėl pirmasis segmentas taip pat paimtas iš pirmo sakinio žodžio, o štai antrasis segmentas paimtas iš
sakinio vidurio, nes nepavyko rasti reikiamo segmento sakinio pradžioje. Tai, kad šiame pavyzdyje paimti trijų fonemų dydžio segmentai, yra visiškas atsitiktinumas, segmentų dydis
gali būti bet koks.
Jungimo kainų veikimą paaiškinsime žemiau pateiktu pavyzdžiu. Klausimas, kodėl imama
po tris fonemas, o ne keturios ir dvi, t. y.

 Vãsaros jūra nuplóvė spalvàs
 Ẽglė Sarapáitė ir Giẽdrė Paugáitė
 
o ne

 Vãsaros jūra nuplóvė spalvàs
 Ẽglė Sarapáitė ir Giẽdrė Paugáitė

 
Atsakymas: sa jungimo kaina mažesnė nei ar, nes kuo garsai skirtingesni, tuo labiau tikėtina, kad žmogus garsų jungimo nepajus.
Keitimo kainų prasmę iliustruosim kitu pavyzdžiu. Klausimas, kodėl imama


 herefòrdų, aberdinų, angùsų
 ar prisimeni nãgą žaliojè lankojè

 
o ne
 
 
 herefòrdų, aberdinų, angùsų
 galimýbes táikyti juõs Lietuvojè

Atsakymas: ko keitimo į go kaina mažesnė nei vo keitimo į go, nes panašesnis kontekstas.
Dar vienas svarbus klausimas, kokio dydžio turėtų būti vienetų parinkimui naudojama garsų bazė. Taylor (2009, p.529) teigia, kad turėtų būti bent viena valanda įrašo. Priešingu
atveju reikiami segmentai bus labai išbarstyti, todėl nebus išnaudojamas tas metodo privalumas, kai bazėje randami dideli ištisai įrašytos kalbos fragmentai. Daugelyje sistemų
naudojamos bazės, apimančios 5 valandas ir daugiau. Taigi SINT.AS garsų bazių apimtis
tik truputį viršija rekomenduojamą minimumą, o projekto LIEPA garsų bazių apimtis yra
artima vidutinei.
