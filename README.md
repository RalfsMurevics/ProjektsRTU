# Projekts 
## Projekta uzdevums
Šis projekts tika izveidots, lai atvieglotu Nacionālās basketbola asociācijas (NBA) fantāzijas līgas konkrētu spēlētaju statistikas apskati. Projektā izvēlētie basketbola spēlētaji ir izvēlēti, balstoties uz manas fantāzijas komandas spēlētajiem. Projekta pamatuzdevums ir iegūt konkrētu statistiku par katru spēlētāju. Izveidojot šo projektu, tas palīdzēs ietaupīt laiku, jo savas komandas spēlētāju statistikas par iepriekšējo spēli varēšu apskatīties vienā failā. Iespēja ir arī redzēt pēdējo piecu spēļu statiskikas, lai varētu pāredzami pārskatīt vai nav vajadzīgas veikt korekcijas komandā, ja spēlētāja, piemēram, iegūtie punkti samazinās.
### Par fantāzijas līgu
NBA fantāzijas līga ir virtuāla sacensības, kur dalībnieki veido komandas ar reāliem NBA spēlētajiem, iegūstot punktus atkarībā no to snieguma reālājās spēlēs.
## Izmantotas Python bibliotēkas
### requests
Šī bibliotēka tiek izmantota, lai veiktu HTTP pieprasījumus uz norādītajiem URL, lai iegūtu spēlētāju statiskitikas lapas HTML saturu.
### BeautifulSoup
Šī bibliotēka tiek izmantota, lai strukturēti un ērti atrastu nepieciešamos datus. 
### pandas 
Šī bibliotēka tiek izmantota, lai saglabātu datus izveidotajā Excel failā.
### xlsxwriter
Šī bibliotēka tiek izmantota, lai iegūtos datus varētu saglabāt atsevišķās Excel lapās.
## Programmatūras izmantošanas meodes
Programma ir izveidota tā, ka tikka apkopots katra spēlētāja konkrēts URL, kurā tika atrasta konkrēta informācija un pēc tam apkopota Excel failā. 
Programma
