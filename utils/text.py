silence_indicators = [
    '_tyla', # 6319
    '_pauze', # 59481
]

"""
Following words in the begining of a sentence may indicate question.
"""
question_words = [
    'ar', 'kur', 'kada', 'kodėl', 'kaip', 'kas', 'kiek'
]

"""
List of noise indicators produced by running with regex over initial word count output.
After having only words containing _ in the beginning.

PATTERN: (_([^_\n]+)) (\d+)
REPLACEMENT: ('$1', '$2'), # $3
"""
noise_indicators = [
    '_cepsejimas', # 14
    '_durys', # 8
    '_pilvas', # 21
    '_kede', # 43
    '_nurijimas', # 61
    '_garsas', # 117
    '_puslapis', # 179
    '_iskvepimas', # 6716
    '_ikvepimas', # 19932
]

"""
List of mistypes produced by running with regex over initial word count output.
After having only words containing _ in the middle.

PATTERN: (([^_\n]+)_([^_\n]+)) (\d+)
REPLACEMENT: ('$1', '$2'), # $4
"""
mistypes_1 = [
    ('dulkes_kes', 'dulkes'), # 1
    ('surengę_su', 'surengę'), # 1
    ('kalnu_nu', 'kalnu'), # 1
    ('sudėti_dė', 'sudėti'), # 1
    ('kokios_kios', 'kokios'), # 1
    ('aukštus_tus', 'aukštus'), # 1
    ('natūralios_lios', 'natūralios'), # 1
    ('ketvyrta_vyr', 'ketvyrta'), # 1
    ('rezultatus_ta', 'rezultatus'), # 1
    ('gausuma_ma', 'gausuma'), # 1
    ('taigoje_je', 'taigoje'), # 1
    ('gyvenamuose_se', 'gyvenamuose'), # 1
    ('ritme_rit', 'ritme'), # 1
    ('rajų_jų', 'rajų'), # 1
    ('lizdeika_dei', 'lizdeika'), # 1
    ('įvesta_į', 'įvesta'), # 1
    ('kovos_vos', 'kovos'), # 1
    ('lūšių_lū', 'lūšių'), # 1
    ('biržais_žais', 'biržais'), # 1
    ('aprašomaisiais_ra', 'aprašomaisiais'), # 1
    ('jauniklius_ni', 'jauniklius'), # 1
    ('viena_vie', 'viena'), # 1
    ('atkasamos_ka', 'atkasamos'), # 1
    ('sukurtu_su', 'sukurtu'), # 1
    ('keterų_te', 'keterų'), # 1
    ('atskyriantį_sky', 'atskyriantį'), # 1
    ('sieną_na', 'sieną'), # 1
    ('kilpas_pas', 'kilpas'), # 1
    ('aišku_ku', 'aišku'), # 1
    ('mėsas_mė', 'mėsas'), # 1
    ('nulėmė_lė', 'nulėmė'), # 1
    ('laiptinė_ti', 'laiptinė'), # 1
    ('nugara_ra', 'nugara'), # 1
    ('skęstu_tu', 'skęstu'), # 1
    ('įrengia_į', 'įrengia'), # 1
    ('aštuonis_nis', 'aštuonis'), # 1
    ('sakalinių_sa', 'sakalinių'), # 1
    ('junesko_ju', 'junesko'), # 1
    ('diena_na', 'diena'), # 1
    ('ssalių_lių', 'ssalių'), # 1
    ('mieste_mies', 'mieste'), # 1
    ('baltai_bal', 'baltai'), # 1
    ('kankinė_ki', 'kankinė'), # 1
    ('adresai_ad', 'adresai'), # 1
    ('grybų_bų', 'grybų'), # 1
    ('kalba_ba', 'kalba'), # 1
    ('eštuoni_tuo', 'eštuoni'), # 1
    ('aukštas_tas', 'aukštas'), # 1
    ('paviršinio_vir', 'paviršinio'), # 1
    ('įteka_te', 'įteka'), # 1
    ('išverda_iš', 'išverda'), # 1
    ('laikomi_mi', 'laikomi'), # 1
    ('tokiooos_kiooos', 'tokiooos'), # 1
    ('rasta_ta', 'rasta'), # 1
    ('gyvulių_gy', 'gyvulių'), # 1
    ('kriokliu_kliu', 'kriokliu'), # 1
    ('debesys_sys', 'debesys'), # 1
    ('šalta_ta', 'šalta'), # 1
    ('šernus_nus', 'šernus'), # 1
    ('stalininė_li', 'stalininė'), # 1
    ('didžiąją_džią', 'didžiąją'), # 1
    ('gubernijoje_ni', 'gubernijoje'), # 1
    ('stebima_ste', 'stebima'), # 1
    ('augmenijos_me', 'augmenijos'), # 1
    ('aukštumo_aukš', 'aukštumo'), # 1
    ('gyvenamuose_muo', 'gyvenamuose'), # 1
    ('dvejines_dve', 'dvejines'), # 1
    ('trejinės_tre', 'trejinės'), # 1
    ('mantrai_trai', 'mantrai'), # 1
    ('trejinę_tre', 'trejinę'), # 1
    ('poros_po', 'poros'), # 1
    ('tarmių_tar', 'tarmių'), # 1
    ('imti_im', 'imti'), # 1
    ('auštan_auš', 'auštan'), # 1
    ('dideles_les', 'dideles'), # 1
    ('pelėnais_nais', 'pelėnais'), # 1
    ('prancūzijos_cū', 'prancūzijos'), # 1
    ('šoklinių_nių', 'šoklinių'), # 1
    ('tamsiai_siai', 'tamsiai'), # 1
    ('sukurtas_su', 'sukurtas'), # 1
    ('ištysus_sus', 'ištysus'), # 1
    ('dydelės_dy', 'dydelės'), # 1
    ('druskingu_gu', 'druskingu'), # 1
    ('terminio_mi', 'terminio'), # 1
    ('sausuma_sau', 'sausuma'), # 1
    ('visos_sos', 'visos'), # 1
    ('fregata_ga', 'fregata'), # 1
    ('augalija_li', 'augalija'), # 1
    ('krosnis_nis', 'krosnis'), # 1
    ('mėsos_mė', 'mėsos'), # 1
    ('dešros_ros', 'dešros'), # 1
    ('dramblis_dram', 'dramblis'), # 1
    ('mišrus_rus', 'mišrus'), # 1
    ('urvu_ur', 'urvu'), # 1
    ('nutiestos_tos', 'nutiestos'), # 1
    ('sausros_sau', 'sausros'), # 1
    ('šamanų_nų', 'šamanų'), # 1
    ('daline_da', 'daline'), # 1
    ('minima_mi', 'minima'), # 1
    ('fundavo_fun', 'fundavo'), # 1
    ('upes_up', 'upes'), # 1
    ('aukštus_us', 'aukštus'), # 1
    ('baltymų_ty', 'baltymų'), # 1
    ('ritualus_tua', 'ritualus'), # 1
    ('vienu_vie', 'vienu'), # 1
    ('keturiasdešimties_ke', 'keturiasdešimties'), # 1
    ('tarpeklius_pe', 'tarpeklius'), # 1
    ('procentų_cen', 'procentų'), # 1
    ('vilhelmo_hel', 'vilhelmo'), # 1
    ('tyrimo_ty', 'tyrimo'), # 1
    ('užpiltas_už', 'užpiltas'), # 1
    ('au_au', 'au'), # 1
    ('aptinkama_ma', 'aptinkama'), # 1
    ('darbus_bus', 'darbus'), # 1
    ('pastolius_pas', 'pastolius'), # 1
    ('klanai_kla', 'klanai'), # 1
    ('užlipdomi_mi', 'užlipdomi'), # 1
    ('skystos_sky', 'skystos'), # 1
    ('karštos_kar', 'karštos'), # 1
    ('šaltos_šal', 'šaltos'), # 1
    ('sriubos_sriu', 'sriubos'), # 1
    ('didesnius_di', 'didesnius'), # 1
    ('taksi_tak', 'taksi'), # 1
    ('kaba_ba', 'kaba'), # 1
    ('sija_si', 'sija'), # 1
    ('žemdirbyste_bys', 'žemdirbyste'), # 1
    ('privačia_va', 'privačia'), # 1
    ('pagrindų_dų', 'pagrindų'), # 1
    ('sanai_nai', 'sanai'), # 1
    ('senams_nams', 'senams'), # 1
    ('galva_gal', 'galva'), # 1
    ('didumą_du', 'didumą'), # 1
    ('kankinės_kan', 'kankinės'), # 1
    ('sekama_ma', 'sekama'), # 1
    ('lytiniuose_ti', 'lytiniuose'), # 1
    ('nušautas_nu', 'nušautas'), # 1
    ('metų_tų', 'metų'), # 1
    ('sūnūs_sū', 'sūnūs'), # 1
    ('uoloz_uo', 'uoloz'), # 1
    ('vienos_nos', 'vienos'), # 1
    ('olos_los', 'olos'), # 1
    ('kilometru_tru', 'kilometru'), # 1
    ('patogus_to', 'patogus'), # 1
    ('patiekalais_tie', 'patiekalais'), # 1
    ('sugniuždami_gniuž', 'sugniuždami'), # 1
    ('medžius_me', 'medžius'), # 1
    ('ilgaamžiškumu_ku', 'ilgaamžiškumu'), # 1
    ('kilmės_kil', 'kilmės'), # 1
    ('griežlė_griež', 'griežlė'), # 1
    ('sriuba_sriu', 'sriuba'), # 1
    ('patiekiant_pa', 'patiekiant'), # 1
    ('valgį_val', 'valgį'), # 1
    ('gamtinės_gam', 'gamtinės'), # 1
    ('dykumos_dy', 'dykumos'), # 1
    ('apsauga_ga', 'apsauga'), # 1
    ('lūšis_lū', 'lūšis'), # 1
    ('laviną_la', 'laviną'), # 1
    ('nėra_nė', 'nėra'), # 1
    ('membrana_bra', 'membrana'), # 1
    ('rasti_ras', 'rasti'), # 1
    ('ankstyvųju_ty', 'ankstyvųju'), # 1
    ('sanams_nams', 'sanams'), # 1
    ('klūpojo_klū', 'klūpojo'), # 1
    ('aptikta_ta', 'aptikta'), # 1
    ('duona_na', 'duona'), # 1
    ('plote_te', 'plote'), # 1
    ('kovos_ko', 'kovos'), # 1
    ('statinių_sta', 'statinių'), # 1
    ('dešimčiu_de', 'dešimčiu'), # 1
    ('surengė_ren', 'surengė'), # 1
    ('kolekcijomis_mis', 'kolekcijomis'), # 1
    ('driežai_drie', 'driežai'), # 1
    ('aukštai_tai', 'aukštai'), # 1
    ('mūrinio_mū', 'mūrinio'), # 1
    ('kiekviena_vie', 'kiekviena'), # 1
    ('rėminį_mi', 'rėminį'), # 1
    ('pelėda_da', 'pelėda'), # 1
    ('valdoma_ma', 'valdoma'), # 1
    ('išpjauta_ta', 'išpjauta'), # 1
    ('daugumą_a', 'daugumą'), # 1
    ('tirštas_tirš', 'tirštas'), # 1
    ('vadinamaa_maa', 'vadinamaa'), # 1
    ('žiemos_mos', 'žiemos'), # 1
    ('urvus_ur', 'urvus'), # 2
    ('sutartines_ti', 'sutartines'), # 2
    ('katinių_nių', 'katinių'), # 2
    ('dokumentus_men', 'dokumentus'), # 2
    ('virtuves_tu', 'virtuves'), # 2
    ('vilku_vil', 'vilku'), # 2
    ('sustojimu_ji', 'sustojimu'), # 2
    ('slenksčių_čių', 'slenksčių'), # 2
    ('šilta_ta', 'šilta'), # 2
    ('įvairios_rios', 'įvairios'), # 2
    ('siauros_siau', 'siauros'), # 2
    ('penkta_penk', 'penkta'), # 2
    ('žinia_nia', 'žinia'), # 2
    ('dzūkijos_dzū', 'dzūkijos'), # 2
    ('pagrindu_du', 'pagrindu'), # 2
    ('konkistadoriai_ta', 'konkistadoriai'), # 2
    ('įkurtas_į', 'įkurtas'), # 2
    ('dvejinės_dve', 'dvejinės'), # 2
    ('sukurta_su', 'sukurta'), # 2
    ('dauguma_dau', 'dauguma'), # 2
    ('uodegos_uo', 'uodegos'), # 2
    ('pradžioje_pra', 'pradžioje'), # 2
    ('architektūra_tū', 'architektūra'), # 2
    ('kmynai_nai', 'kmynai'), # 2
    ('sėjos_sė', 'sėjos'), # 2
    ('klanų_kla', 'klanų'), # 2
    ('sausros_saus', 'sausros'), # 2
    ('kasimui_ka', 'kasimui'), # 2
    ('lokiai_lo', 'lokiai'), # 2
    ('pralaužimui_lau', 'pralaužimui'), # 2
    ('auštant_auš', 'auštant'), # 2
    ('gausumą_gau', 'gausumą'), # 2
    ('mišku_miš', 'mišku'), # 2
    ('temperatūra_tū', 'temperatūra'), # 2
    ('auštant_u', 'auštant'), # 3
    ('aplankų_ap', 'aplankų'), # 3
    ('objektai_ob', 'objektai'), # 3
    ('metus_me', 'metus'), # 3
    ('rasta_ras', 'rasta'), # 3
    ('kastinį_ti', 'kastinį'), # 3
    ('aukštos_tos', 'aukštos'), # 3
    ('plyšiuose_ply', 'plyšiuose'), # 3
    ('rastos_ras', 'rastos'), # 3
    ('dešimtis_tis', 'dešimtis'), # 3
    ('žiūrima_žiū', 'žiūrima'), # 3
    ('griaunama_griau', 'griaunama'), # 3
    ('žymi_žy', 'žymi'), # 3
    ('langus_gus', 'langus'), # 3
    ('paveldimos_vel', 'paveldimos'), # 4
    ('veiklų_veik', 'veiklų'), # 4
    ('kelių_lių', 'kelių'), # 4
    ('puse_pu', 'puse'), # 4
    ('sukurta_ta', 'sukurta'), # 4
    ('didesnės_nės', 'didesnės'), # 4
    ('sugriauta_ta', 'sugriauta'), # 4
    ('yra_y', 'yra'), # 4
    ('nukreipta_ta', 'nukreipta'), # 4
    ('vandens_van', 'vandens'), # 4
    ('uždrausta_už', 'uždrausta'), # 4
    ('pradėti_dė', 'pradėti'), # 5
    ('auštant_au', 'auštant'), # 5
    ('penkta_pen', 'penkta'), # 5
    ('veiklų_vei', 'veiklų'), # 5
    ('uodega_uo', 'uodega'), # 5
    ('plauko_plau', 'plauko'), # 6
    ('didelės_di', 'didelės'), # 6
    ('ketvirta_vir', 'ketvirta'), # 6
    ('pirma_pir', 'pirma'), # 7
    ('antra_an', 'antra'), # 7
    ('trečia_tre', 'trečia'), # 7
    ('šešta_šeš', 'šešta'), # 7
    ('septinta_tin', 'septinta'), # 7
    ('aštunta_tun', 'aštunta'), # 7
    ('devinta_vin', 'devinta'), # 7
    ('dešimta_šim', 'dešimta'), # 7
    ('aštuoni_tuo', 'aštuoni'), # 8
    ('devyni_vy', 'devyni'), # 8
    ('septyni_ty', 'septyni'), # 10
    ('tokios_to', 'tokios'), # 12
    ('uodega_ga', 'uodega'), # 15
]

"""
List of mistypes produced by running with regex over initial word count output.
After having only words containing _ in the beginning.

PATTERN: (_([^_\n]+)) ()\d+)
REPLACEMENT: ('$1', '$2'), # $3
"""
mistypes_2 = [
    ('_centrai', 'centrai'), # 1
    ('_įjun', 'įjun'), # 1
    ('_staunhendžas', 'staunhendžas'), # 1
    ('_žmoniu', 'žmoniu'), # 1
    ('_koplytstulpes', 'koplytstulpes'), # 1
    ('_vienuoliai', 'vienuoliai'), # 1
    ('_ikomų', 'ikomų'), # 1
    ('_kolek', 'kolek'), # 1
    ('_galvą', 'galvą'), # 1
    ('_lotyniškaja', 'lotyniškaja'), # 1
    ('_skersine', 'skersine'), # 1
    ('_kyba', 'kyba'), # 1
    ('_ankores', 'ankores'), # 1
    ('_išskobtuoti', 'išskobtuoti'), # 1
    ('_saules', 'saules'), # 1
    ('_šilo', 'šilo'), # 1
    ('_susidomėjima', 'susidomėjima'), # 1
    ('_staunhendžiu', 'staunhendžiu'), # 1
    ('_vienuoliu', 'vienuoliu'), # 1
    ('_voliuotos', 'voliuotos'), # 1
    ('_dzūkijos', 'dzūkijos'), # 1
    ('_įtrūkimu', 'įtrūkimu'), # 1
    ('_bucharas', 'bucharas'), # 1
    ('_smiltanio', 'smiltanio'), # 1
    ('_atsiskleidžiama', 'atsiskleidžiama'), # 1
    ('_grandiozdiškumas', 'grandiozdiškumas'), # 1
    ('_dais', 'dais'), # 1
    ('_architektūrinio', 'architektūrinio'), # 1
    ('_kryždarbystę', 'kryždarbystę'), # 1
    ('_saundheidžas', 'saundheidžas'), # 1
    ('_susidomėjo', 'susidomėjo'), # 1
    ('_saundheidžui', 'saundheidžui'), # 1
    ('_sija', 'sija'), # 1
    ('_peršalu', 'peršalu'), # 1
    ('_liaudiess', 'liaudiess'), # 1
    ('_raižyb', 'raižyb'), # 1
    ('_gua', 'gua'), # 1
    ('_kombodže', 'kombodže'), # 1
    ('_įvairov', 'įvairov'), # 1
    ('_šedevro', 'šedevro'), # 1
    ('_televizor', 'televizor'), # 1
    ('_valgomiej', 'valgomiej'), # 1
    ('_element', 'element'), # 1
    ('_tibrizas', 'tibrizas'), # 1
    ('_svarbiausias', 'svarbiausias'), # 1
    ('_sudėjim', 'sudėjim'), # 1
    ('_upės', 'upės'), # 1
    ('_jūros', 'jūros'), # 1
    ('_šššimtą', 'šššimtą'), # 1
    ('_skeldėo', 'skeldėo'), # 1
    ('_civelizacijos', 'civelizacijos'), # 1
    ('_aptinkama', 'aptinkama'), # 1
    ('_fikūrų', 'fikūrų'), # 1
    ('_susidūrė', 'susidūrė'), # 1
    ('_įtraukų', 'įtraukų'), # 1
    ('_tadicijos', 'tadicijos'), # 1
    ('_taikliai', 'taikliai'), # 1
    ('_atskleidžiama', 'atskleidžiama'), # 1
    ('_mauzauliejaus', 'mauzauliejaus'), # 1
    ('_gran-dioziškumas', 'gran-dioziškumas'), # 1
    ('_medžiotai', 'medžiotai'), # 1
    ('_minaratas', 'minaratas'), # 1
    ('_kapsų', 'kapsų'), # 1
    ('_pietine', 'pietine'), # 1
    ('_kompjuterį', 'kompjuterį'), # 1
    ('_tvyros', 'tvyros'), # 1
    ('_nacionaliniame', 'nacionaliniame'), # 1
    ('_natūralios', 'natūralios'), # 1
    ('_testinuma', 'testinuma'), # 1
    ('_švent-yklų', 'švent-yklų'), # 1
    ('_puo-šiančios', 'puo-šiančios'), # 1
    ('_sstounhedžas', 'sstounhedžas'), # 1
    ('_įkutas', 'įkutas'), # 1
    ('_unika-lių', 'unika-lių'), # 1
    ('_gimtaienis', 'gimtaienis'), # 1
    ('_por-tugalų', 'por-tugalų'), # 1
    ('_laip-tais', 'laip-tais'), # 1
    ('_eh', 'eh'), # 1
    ('_mi-kroklimatas', 'mi-kroklimatas'), # 1
    ('_viršūne', 'viršūne'), # 1
    ('_u-pes', 'u-pes'), # 1
    ('_did-elė', 'did-elė'), # 1
    ('_šaldymo', 'šaldymo'), # 1
    ('_ppasvėrė', 'ppasvėrė'), # 1
    ('_sssalų', 'sssalų'), # 1
    ('_išsilydžiussioms', 'išsilydžiussioms'), # 1
    ('_ča-ižant', 'ča-ižant'), # 1
    ('_sssienos', 'sssienos'), # 1
    ('_šiau-rėje', 'šiau-rėje'), # 1
    ('_na-tūralios', 'na-tūralios'), # 1
    ('_kuni-gaikštis', 'kuni-gaikštis'), # 1
    ('_architektūrinių', 'architektūrinių'), # 1
    ('_de-ko-ratyvinių', 'de-ko-ratyvinių'), # 1
    ('_valgomie', 'valgomie'), # 1
    ('_o', 'o'), # 1
    ('_nelygiais', 'nelygiais'), # 1
    ('_por-talus', 'por-talus'), # 1
    ('_sachralinio', 'sachralinio'), # 1
    ('_krikščioniško', 'krikščioniško'), # 1
    ('_kambodža', 'kambodža'), # 1
    ('_freksų', 'freksų'), # 1
    ('_šil-ko', 'šil-ko'), # 1
    ('_grikiškojo', 'grikiškojo'), # 1
    ('_sssijos', 'sssijos'), # 1
    ('_ssikerta', 'ssikerta'), # 1
    ('_tur-gus', 'tur-gus'), # 1
    ('_lotyniško', 'lotyniško'), # 1
    ('_ssskersinė', 'ssskersinė'), # 1
    ('_sssija', 'sssija'), # 1
    ('_įspūdigiausias', 'įspūdigiausias'), # 1
    ('_prisitaikyta', 'prisitaikyta'), # 1
    ('_portu-galų', 'portu-galų'), # 1
    ('_kryž-dirbystę', 'kryž-dirbystę'), # 1
    ('_sloguoju', 'sloguoju'), # 1
    ('_ver-čiama-ssi', 'ver-čiama-ssi'), # 1
    ('_naujap', 'naujap'), # 1
    ('_hiphipotezė', 'hiphipotezė'), # 1
    ('_stounhedžas', 'stounhedžas'), # 1
    ('_užburančiaisiais', 'užburančiaisiais'), # 1
    ('_nematere-laus', 'nematere-laus'), # 1
    ('_žodyno', 'žodyno'), # 1
    ('_atsiduriame', 'atsiduriame'), # 1
    ('_sienos', 'sienos'), # 1
    ('_išsilydžiusios', 'išsilydžiusios'), # 1
    ('_uolienos', 'uolienos'), # 1
    ('_aplinkėse', 'aplinkėse'), # 1
    ('_aptikta', 'aptikta'), # 1
    ('_padpadėtis', 'padpadėtis'), # 1
    ('_klėstinčiu', 'klėstinčiu'), # 1
    ('_puosiančios', 'puosiančios'), # 1
    ('_patalbas', 'patalbas'), # 1
    ('_puoštus', 'puoštus'), # 1
    ('_gimtanis', 'gimtanis'), # 1
    ('_valiutos', 'valiutos'), # 1
    ('_tradicjos', 'tradicjos'), # 1
    ('_rodiniai', 'rodiniai'), # 1
    ('_produkto', 'produkto'), # 1
    ('_pasveria', 'pasveria'), # 1
    ('_parke', 'parke'), # 1
    ('_jjos', 'jjos'), # 1
    ('_klajoklio', 'klajoklio'), # 1
    ('_liettuvių', 'liettuvių'), # 1
    ('_chamelionai', 'chamelionai'), # 1
    ('_fregata', 'fregata'), # 1
    ('_parkų', 'parkų'), # 1
    ('_ssstovi', 'ssstovi'), # 1
    ('_vinofs', 'vinofs'), # 2
    ('_is', 'is'), # 2
    ('_stačią', 'stačią'), # 2
    ('_stounhedžui', 'stounhedžui'), # 2
    ('_auštant', 'auštant'), # 2
    ('_mineretas', 'mineretas'), # 2
    ('_koplystulpiai', 'koplystulpiai'), # 2
    ('_iškobtos', 'iškobtos'), # 3

    # Noise indicator mistype fix
    ('_dutys', '_durys'), # 3
    ('_puslpais', '_puslapis'), # 3
]

regex_replacements = [
    ('(\s?[\t\r\n]\s?|\s{2,})+', ' '),
    ('\s+$', ''),
    ('^\s+', ''),
]

mistypes = [] + mistypes_1 + mistypes_2
