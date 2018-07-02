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
    ('keturiasdešimties_ke', 'keturiasdešimties'), # 1
    ('konkistadoriai_ta', 'konkistadoriai'), # 2
    ('aprašomaisiais_ra', 'aprašomaisiais'), # 1
    ('ilgaamžiškumu_ku', 'ilgaamžiškumu'), # 1
    ('kolekcijomis_mis', 'kolekcijomis'), # 1
    ('sugniuždami_gniuž', 'sugniuždami'), # 1
    ('architektūra_tū', 'architektūra'), # 2
    ('žemdirbyste_bys', 'žemdirbyste'), # 1
    ('gyvenamuose_muo', 'gyvenamuose'), # 1
    ('atskyriantį_sky', 'atskyriantį'), # 1
    ('pralaužimui_lau', 'pralaužimui'), # 2
    ('patiekalais_tie', 'patiekalais'), # 1
    ('prancūzijos_cū', 'prancūzijos'), # 1
    ('gyvenamuose_se', 'gyvenamuose'), # 1
    ('temperatūra_tū', 'temperatūra'), # 2
    ('natūralios_lios', 'natūralios'), # 1
    ('gubernijoje_ni', 'gubernijoje'), # 1
    ('paveldimos_vel', 'paveldimos'), # 4
    ('dokumentus_men', 'dokumentus'), # 2
    ('griaunama_griau', 'griaunama'), # 3
    ('paviršinio_vir', 'paviršinio'), # 1
    ('tokiooos_kiooos', 'tokiooos'), # 1
    ('ankstyvųju_ty', 'ankstyvųju'), # 1
    ('rezultatus_ta', 'rezultatus'), # 1
    ('patiekiant_pa', 'patiekiant'), # 1
    ('jauniklius_ni', 'jauniklius'), # 1
    ('tarpeklius_pe', 'tarpeklius'), # 1
    ('augmenijos_me', 'augmenijos'), # 1
    ('lytiniuose_ti', 'lytiniuose'), # 1
    ('sutartines_ti', 'sutartines'), # 2
    ('plyšiuose_ply', 'plyšiuose'), # 3
    ('kilometru_tru', 'kilometru'), # 1
    ('kiekviena_vie', 'kiekviena'), # 1
    ('vadinamaa_maa', 'vadinamaa'), # 1
    ('pastolius_pas', 'pastolius'), # 1
    ('pradžioje_pra', 'pradžioje'), # 2
    ('slenksčių_čių', 'slenksčių'), # 2
    ('nutiestos_tos', 'nutiestos'), # 1
    ('stalininė_li', 'stalininė'), # 1
    ('didžiąją_džią', 'didžiąją'), # 1
    ('sakalinių_sa', 'sakalinių'), # 1
    ('kriokliu_kliu', 'kriokliu'), # 1
    ('druskingu_gu', 'druskingu'), # 1
    ('aukštumo_aukš', 'aukštumo'), # 1
    ('sustojimu_ji', 'sustojimu'), # 2
    ('aptinkama_ma', 'aptinkama'), # 1
    ('didesnius_di', 'didesnius'), # 1
    ('uždrausta_už', 'uždrausta'), # 4
    ('užlipdomi_mi', 'užlipdomi'), # 1
    ('pelėnais_nais', 'pelėnais'), # 1
    ('įvairios_rios', 'įvairios'), # 2
    ('sugriauta_ta', 'sugriauta'), # 4
    ('dramblis_dram', 'dramblis'), # 1
    ('nukreipta_ta', 'nukreipta'), # 4
    ('atkasamos_ka', 'atkasamos'), # 1
    ('aštuonis_nis', 'aštuonis'), # 1
    ('lizdeika_dei', 'lizdeika'), # 1
    ('kankinės_kan', 'kankinės'), # 1
    ('dešimtis_tis', 'dešimtis'), # 3
    ('dvejines_dve', 'dvejines'), # 1
    ('trejinės_tre', 'trejinės'), # 1
    ('ketvyrta_vyr', 'ketvyrta'), # 1
    ('procentų_cen', 'procentų'), # 1
    ('septinta_tin', 'septinta'), # 7
    ('ritualus_tua', 'ritualus'), # 1
    ('membrana_bra', 'membrana'), # 1
    ('didesnės_nės', 'didesnės'), # 4
    ('gamtinės_gam', 'gamtinės'), # 1
    ('dzūkijos_dzū', 'dzūkijos'), # 2
    ('griežlė_griež', 'griežlė'), # 1
    ('šoklinių_nių', 'šoklinių'), # 1
    ('vilhelmo_hel', 'vilhelmo'), # 1
    ('ketvirta_vir', 'ketvirta'), # 6
    ('statinių_sta', 'statinių'), # 1
    ('dvejinės_dve', 'dvejinės'), # 2
    ('privačia_va', 'privačia'), # 1
    ('išpjauta_ta', 'išpjauta'), # 1
    ('driežai_drie', 'driežai'), # 1
    ('augalija_li', 'augalija'), # 1
    ('dešimčiu_de', 'dešimčiu'), # 1
    ('laiptinė_ti', 'laiptinė'), # 1
    ('sukurtas_su', 'sukurtas'), # 1
    ('tamsiai_siai', 'tamsiai'), # 1
    ('tirštas_tirš', 'tirštas'), # 1
    ('objektai_ob', 'objektai'), # 3
    ('virtuves_tu', 'virtuves'), # 2
    ('terminio_mi', 'terminio'), # 1
    ('biržais_žais', 'biržais'), # 1
    ('užpiltas_už', 'užpiltas'), # 1
    ('mantrai_trai', 'mantrai'), # 1
    ('nušautas_nu', 'nušautas'), # 1
    ('sausros_saus', 'sausros'), # 2
    ('pagrindu_du', 'pagrindu'), # 2
    ('pagrindų_dų', 'pagrindų'), # 1
    ('siauros_siau', 'siauros'), # 2
    ('sriubos_sriu', 'sriubos'), # 1
    ('aukštus_tus', 'aukštus'), # 1
    ('karštos_kar', 'karštos'), # 1
    ('skystos_sky', 'skystos'), # 1
    ('dešimta_šim', 'dešimta'), # 7
    ('sausuma_sau', 'sausuma'), # 1
    ('aštuoni_tuo', 'aštuoni'), # 8
    ('žiūrima_žiū', 'žiūrima'), # 3
    ('stebima_ste', 'stebima'), # 1
    ('devinta_vin', 'devinta'), # 7
    ('septyni_ty', 'septyni'), # 10
    ('trejinę_tre', 'trejinę'), # 1
    ('aukštas_tas', 'aukštas'), # 1
    ('aukštos_tos', 'aukštos'), # 3
    ('eštuoni_tuo', 'eštuoni'), # 1
    ('dauguma_dau', 'dauguma'), # 2
    ('debesys_sys', 'debesys'), # 1
    ('fundavo_fun', 'fundavo'), # 1
    ('aštunta_tun', 'aštunta'), # 7
    ('sausros_sau', 'sausros'), # 1
    ('katinių_nių', 'katinių'), # 2
    ('klūpojo_klū', 'klūpojo'), # 1
    ('gausumą_gau', 'gausumą'), # 2
    ('auštant_auš', 'auštant'), # 2
    ('dideles_les', 'dideles'), # 1
    ('ištysus_sus', 'ištysus'), # 1
    ('krosnis_nis', 'krosnis'), # 1
    ('surengė_ren', 'surengė'), # 1
    ('vandens_van', 'vandens'), # 4
    ('aukštai_tai', 'aukštai'), # 1
    ('adresai_ad', 'adresai'), # 1
    ('penkta_penk', 'penkta'), # 2
    ('kasimui_ka', 'kasimui'), # 2
    ('kastinį_ti', 'kastinį'), # 3
    ('pradėti_dė', 'pradėti'), # 5
    ('patogus_to', 'patogus'), # 1
    ('plauko_plau', 'plauko'), # 6
    ('auštant_au', 'auštant'), # 5
    ('medžius_me', 'medžius'), # 1
    ('taigoje_je', 'taigoje'), # 1
    ('gausuma_ma', 'gausuma'), # 1
    ('kankinė_ki', 'kankinė'), # 1
    ('sriuba_sriu', 'sriuba'), # 1
    ('gyvulių_gy', 'gyvulių'), # 1
    ('fregata_ga', 'fregata'), # 1
    ('mieste_mies', 'mieste'), # 1
    ('dykumos_dy', 'dykumos'), # 1
    ('apsauga_ga', 'apsauga'), # 1
    ('aplankų_ap', 'aplankų'), # 3
    ('veiklų_veik', 'veiklų'), # 4
    ('sukurtu_su', 'sukurtu'), # 1
    ('didelės_di', 'didelės'), # 6
    ('junesko_ju', 'junesko'), # 1
    ('sanams_nams', 'sanams'), # 1
    ('uodegos_uo', 'uodegos'), # 2
    ('aptikta_ta', 'aptikta'), # 1
    ('dydelės_dy', 'dydelės'), # 1
    ('senams_nams', 'senams'), # 1
    ('laikomi_mi', 'laikomi'), # 1
    ('aukštus_us', 'aukštus'), # 1
    ('išverda_iš', 'išverda'), # 1
    ('baltymų_ty', 'baltymų'), # 1
    ('kokios_kios', 'kokios'), # 1
    ('sukurta_su', 'sukurta'), # 2
    ('sukurta_ta', 'sukurta'), # 4
    ('mūrinio_mū', 'mūrinio'), # 1
    ('surengę_su', 'surengę'), # 1
    ('valdoma_ma', 'valdoma'), # 1
    ('penkta_pen', 'penkta'), # 5
    ('trečia_tre', 'trečia'), # 7
    ('įrengia_į', 'įrengia'), # 1
    ('kilpas_pas', 'kilpas'), # 1
    ('žiemos_mos', 'žiemos'), # 1
    ('ssalių_lių', 'ssalių'), # 1
    ('auštant_u', 'auštant'), # 3
    ('baltai_bal', 'baltai'), # 1
    ('kilmės_kil', 'kilmės'), # 1
    ('vienos_nos', 'vienos'), # 1
    ('rastos_ras', 'rastos'), # 3
    ('veiklų_vei', 'veiklų'), # 5
    ('dulkes_kes', 'dulkes'), # 1
    ('daugumą_a', 'daugumą'), # 1
    ('langus_gus', 'langus'), # 3
    ('šaltos_šal', 'šaltos'), # 1
    ('kmynai_nai', 'kmynai'), # 2
    ('šernus_nus', 'šernus'), # 1
    ('klanai_kla', 'klanai'), # 1
    ('tokios_to', 'tokios'), # 12
    ('įkurtas_į', 'įkurtas'), # 2
    ('darbus_bus', 'darbus'), # 1
    ('tarmių_tar', 'tarmių'), # 1
    ('auštan_auš', 'auštan'), # 1
    ('mišrus_rus', 'mišrus'), # 1
    ('dešros_ros', 'dešros'), # 1
    ('uodega_ga', 'uodega'), # 15
    ('šamanų_nų', 'šamanų'), # 1
    ('daline_da', 'daline'), # 1
    ('sekama_ma', 'sekama'), # 1
    ('rėminį_mi', 'rėminį'), # 1
    ('pelėda_da', 'pelėda'), # 1
    ('tyrimo_ty', 'tyrimo'), # 1
    ('minima_mi', 'minima'), # 1
    ('skęstu_tu', 'skęstu'), # 1
    ('sudėti_dė', 'sudėti'), # 1
    ('keterų_te', 'keterų'), # 1
    ('didumą_du', 'didumą'), # 1
    ('lokiai_lo', 'lokiai'), # 2
    ('nulėmė_lė', 'nulėmė'), # 1
    ('uodega_uo', 'uodega'), # 5
    ('devyni_vy', 'devyni'), # 8
    ('laviną_la', 'laviną'), # 1
    ('nugara_ra', 'nugara'), # 1
    ('žinia_nia', 'žinia'), # 2
    ('įvesta_į', 'įvesta'), # 1
    ('kovos_vos', 'kovos'), # 1
    ('vilku_vil', 'vilku'), # 2
    ('viena_vie', 'viena'), # 1
    ('šešta_šeš', 'šešta'), # 7
    ('pirma_pir', 'pirma'), # 7
    ('visos_sos', 'visos'), # 1
    ('mišku_miš', 'mišku'), # 2
    ('rasti_ras', 'rasti'), # 1
    ('ritme_rit', 'ritme'), # 1
    ('valgį_val', 'valgį'), # 1
    ('vienu_vie', 'vienu'), # 1
    ('rasta_ras', 'rasta'), # 3
    ('klanų_kla', 'klanų'), # 2
    ('kelių_lių', 'kelių'), # 4
    ('taksi_tak', 'taksi'), # 1
    ('galva_gal', 'galva'), # 1
    ('sanai_nai', 'sanai'), # 1
    ('kalba_ba', 'kalba'), # 1
    ('sūnūs_sū', 'sūnūs'), # 1
    ('uoloz_uo', 'uoloz'), # 1
    ('šilta_ta', 'šilta'), # 2
    ('metus_me', 'metus'), # 3
    ('lūšis_lū', 'lūšis'), # 1
    ('mėsos_mė', 'mėsos'), # 1
    ('duona_na', 'duona'), # 1
    ('poros_po', 'poros'), # 1
    ('šalta_ta', 'šalta'), # 1
    ('rasta_ta', 'rasta'), # 1
    ('įteka_te', 'įteka'), # 1
    ('kalnu_nu', 'kalnu'), # 1
    ('grybų_bų', 'grybų'), # 1
    ('diena_na', 'diena'), # 1
    ('mėsas_mė', 'mėsas'), # 1
    ('plote_te', 'plote'), # 1
    ('antra_an', 'antra'), # 7
    ('aišku_ku', 'aišku'), # 1
    ('kovos_ko', 'kovos'), # 1
    ('sieną_na', 'sieną'), # 1
    ('urvus_ur', 'urvus'), # 2
    ('lūšių_lū', 'lūšių'), # 1
    ('sėjos_sė', 'sėjos'), # 2
    ('olos_los', 'olos'), # 1
    ('imti_im', 'imti'), # 1
    ('puse_pu', 'puse'), # 4
    ('sija_si', 'sija'), # 1
    ('žymi_žy', 'žymi'), # 3
    ('upes_up', 'upes'), # 1
    ('urvu_ur', 'urvu'), # 1
    ('kaba_ba', 'kaba'), # 1
    ('metų_tų', 'metų'), # 1
    ('nėra_nė', 'nėra'), # 1
    ('rajų_jų', 'rajų'), # 1
    ('yra_y', 'yra'), # 4
    ('au_au', 'au'), # 1
]

"""
List of mistypes produced by running with regex over initial word count output.
After having only words containing _ in the beginning.

PATTERN: (_([^_\n]+)) ()\d+)
REPLACEMENT: ('$1', '$2'), # $3
"""
mistypes_2 = [
    ('_užburančiaisiais', 'užburančiaisiais'), # 1
    ('_išsilydžiussioms', 'išsilydžiussioms'), # 1
    ('_grandiozdiškumas', 'grandiozdiškumas'), # 1
    ('_gran-dioziškumas', 'gran-dioziškumas'), # 1
    ('_architektūrinių', 'architektūrinių'), # 1
    ('_de-ko-ratyvinių', 'de-ko-ratyvinių'), # 1
    ('_atsiskleidžiama', 'atsiskleidžiama'), # 1
    ('_architektūrinio', 'architektūrinio'), # 1
    ('_mi-kroklimatas', 'mi-kroklimatas'), # 1
    ('_įspūdigiausias', 'įspūdigiausias'), # 1
    ('_išsilydžiusios', 'išsilydžiusios'), # 1
    ('_nacionaliniame', 'nacionaliniame'), # 1
    ('_atskleidžiama', 'atskleidžiama'), # 1
    ('_koplystulpiai', 'koplystulpiai'), # 2
    ('_kuni-gaikštis', 'kuni-gaikštis'), # 1
    ('_kryž-dirbystę', 'kryž-dirbystę'), # 1
    ('_krikščioniško', 'krikščioniško'), # 1
    ('_mauzauliejaus', 'mauzauliejaus'), # 1
    ('_koplytstulpes', 'koplytstulpes'), # 1
    ('_civelizacijos', 'civelizacijos'), # 1
    ('_nematere-laus', 'nematere-laus'), # 1
    ('_ver-čiama-ssi', 'ver-čiama-ssi'), # 1
    ('_svarbiausias', 'svarbiausias'), # 1
    ('_saundheidžas', 'saundheidžas'), # 1
    ('_kryždarbystę', 'kryždarbystę'), # 1
    ('_puo-šiančios', 'puo-šiančios'), # 1
    ('_sstounhedžas', 'sstounhedžas'), # 1
    ('_saundheidžui', 'saundheidžui'), # 1
    ('_staunhendžiu', 'staunhendžiu'), # 1
    ('_staunhendžas', 'staunhendžas'), # 1
    ('_prisitaikyta', 'prisitaikyta'), # 1
    ('_susidomėjima', 'susidomėjima'), # 1
    ('_stounhedžas', 'stounhedžas'), # 1
    ('_puosiančios', 'puosiančios'), # 1
    ('_atsiduriame', 'atsiduriame'), # 1
    ('_hiphipotezė', 'hiphipotezė'), # 1
    ('_sachralinio', 'sachralinio'), # 1
    ('_stounhedžui', 'stounhedžui'), # 2
    ('_na-tūralios', 'na-tūralios'), # 1
    ('_išskobtuoti', 'išskobtuoti'), # 1
    ('_lotyniškaja', 'lotyniškaja'), # 1
    ('_chamelionai', 'chamelionai'), # 1
    ('_natūralios', 'natūralios'), # 1
    ('_padpadėtis', 'padpadėtis'), # 1
    ('_švent-yklų', 'švent-yklų'), # 1
    ('_kompjuterį', 'kompjuterį'), # 1
    ('_ssskersinė', 'ssskersinė'), # 1
    ('_klėstinčiu', 'klėstinčiu'), # 1
    ('_gimtaienis', 'gimtaienis'), # 1
    ('_por-tugalų', 'por-tugalų'), # 1
    ('_vienuoliai', 'vienuoliai'), # 1
    ('_grikiškojo', 'grikiškojo'), # 1
    ('_susidomėjo', 'susidomėjo'), # 1
    ('_portu-galų', 'portu-galų'), # 1
    ('_unika-lių', 'unika-lių'), # 1
    ('_televizor', 'televizor'), # 1
    ('_valgomiej', 'valgomiej'), # 1
    ('_laip-tais', 'laip-tais'), # 1
    ('_vienuoliu', 'vienuoliu'), # 1
    ('_tradicjos', 'tradicjos'), # 1
    ('_medžiotai', 'medžiotai'), # 1
    ('_minaratas', 'minaratas'), # 1
    ('_smiltanio', 'smiltanio'), # 1
    ('_voliuotos', 'voliuotos'), # 1
    ('_liettuvių', 'liettuvių'), # 1
    ('_lotyniško', 'lotyniško'), # 1
    ('_šiau-rėje', 'šiau-rėje'), # 1
    ('_aplinkėse', 'aplinkėse'), # 1
    ('_aptinkama', 'aptinkama'), # 1
    ('_testinuma', 'testinuma'), # 1
    ('_klajoklio', 'klajoklio'), # 1
    ('_liaudiess', 'liaudiess'), # 1
    ('_nelygiais', 'nelygiais'), # 1
    ('_por-talus', 'por-talus'), # 1
    ('_tadicijos', 'tadicijos'), # 1
    ('_mineretas', 'mineretas'), # 2
    ('_produkto', 'produkto'), # 1
    ('_kambodža', 'kambodža'), # 1
    ('_valgomie', 'valgomie'), # 1
    ('_ssikerta', 'ssikerta'), # 1
    ('_sssienos', 'sssienos'), # 1
    ('_ča-ižant', 'ča-ižant'), # 1
    ('_patalbas', 'patalbas'), # 1
    ('_valiutos', 'valiutos'), # 1
    ('_ppasvėrė', 'ppasvėrė'), # 1
    ('_rodiniai', 'rodiniai'), # 1
    ('_iškobtos', 'iškobtos'), # 3
    ('_sloguoju', 'sloguoju'), # 1
    ('_gimtanis', 'gimtanis'), # 1
    ('_pasveria', 'pasveria'), # 1
    ('_taikliai', 'taikliai'), # 1
    ('_susidūrė', 'susidūrė'), # 1
    ('_tibrizas', 'tibrizas'), # 1
    ('_kombodže', 'kombodže'), # 1
    ('_bucharas', 'bucharas'), # 1
    ('_įtrūkimu', 'įtrūkimu'), # 1
    ('_dzūkijos', 'dzūkijos'), # 1
    ('_skersine', 'skersine'), # 1
    ('_uolienos', 'uolienos'), # 1
    ('_centrai', 'centrai'), # 1
    ('_peršalu', 'peršalu'), # 1
    ('_auštant', 'auštant'), # 2
    ('_sudėjim', 'sudėjim'), # 1
    ('_fregata', 'fregata'), # 1
    ('_ankores', 'ankores'), # 1
    ('_šššimtą', 'šššimtą'), # 1
    ('_skeldėo', 'skeldėo'), # 1
    ('_pietine', 'pietine'), # 1
    ('_viršūne', 'viršūne'), # 1
    ('_įvairov', 'įvairov'), # 1
    ('_did-elė', 'did-elė'), # 1
    ('_šedevro', 'šedevro'), # 1
    ('_ssstovi', 'ssstovi'), # 1
    ('_puoštus', 'puoštus'), # 1
    ('_šaldymo', 'šaldymo'), # 1
    ('_sssijos', 'sssijos'), # 1
    ('_įtraukų', 'įtraukų'), # 1
    ('_tur-gus', 'tur-gus'), # 1
    ('_element', 'element'), # 1
    ('_aptikta', 'aptikta'), # 1
    ('_raižyb', 'raižyb'), # 1
    ('_sienos', 'sienos'), # 1
    ('_naujap', 'naujap'), # 1
    ('_sssija', 'sssija'), # 1
    ('_šil-ko', 'šil-ko'), # 1
    ('_freksų', 'freksų'), # 1
    ('_sssalų', 'sssalų'), # 1
    ('_žmoniu', 'žmoniu'), # 1
    ('_įkutas', 'įkutas'), # 1
    ('_tvyros', 'tvyros'), # 1
    ('_saules', 'saules'), # 1
    ('_stačią', 'stačią'), # 2
    ('_vinofs', 'vinofs'), # 2
    ('_fikūrų', 'fikūrų'), # 1
    ('_žodyno', 'žodyno'), # 1
    ('_ikomų', 'ikomų'), # 1
    ('_parkų', 'parkų'), # 1
    ('_parke', 'parke'), # 1
    ('_kapsų', 'kapsų'), # 1
    ('_galvą', 'galvą'), # 1
    ('_kolek', 'kolek'), # 1
    ('_jūros', 'jūros'), # 1
    ('_u-pes', 'u-pes'), # 1
    ('_upės', 'upės'), # 1
    ('_dais', 'dais'), # 1
    ('_jjos', 'jjos'), # 1
    ('_įjun', 'įjun'), # 1
    ('_kyba', 'kyba'), # 1
    ('_šilo', 'šilo'), # 1
    ('_sija', 'sija'), # 1
    ('_gua', 'gua'), # 1
    ('_eh', 'eh'), # 1
    ('_o', 'o'), # 1

    #('_is', 'is'),
    ('_is kvepimas', '_iskvepimas'),

    # Noise indicator mistype fix
    ('_dutys', '_durys'), # 3
    ('_puslpais', '_puslapis'), # 3
]


"""
List of mistypes produced by running with regex over word count output after first cleanup.
After having only words containing - in the middle.

PATTERN: (([^-\n]+)-([^-\n]+)(-([^-\n]+))?) (\d+)
REPLACEMENT: ('$1', '$2$3$5'), # $6
"""
mistypes_3 = [
    ('gran-dioziškumas', 'grandioziškumas'), # 1
    ('de-ko-ratyvinių', 'dekoratyvinių'), # 1
    ('mi-kroklimatas', 'mikroklimatas'), # 1
    ('per-tinkavimas', 'pertinkavimas'), # 1
    ('kuni-gaikštis', 'kunigaikštis'), # 1
    ('kryž-dirbystę', 'kryždirbystę'), # 1
    ('nematere-laus', 'nematerelaus'), # 1
    ('ver-čiama-ssi', 'verčiamassi'), # 1
    ('puo-šiančios', 'puošiančios'), # 1
    ('na-tūralios', 'natūralios'), # 1
    ('švent-yklų', 'šventyklų'), # 1
    ('portu-galų', 'portugalų'), # 1
    ('por-tugalų', 'portugalų'), # 1
    ('unika-lių', 'unikalių'), # 1
    ('laip-tais', 'laiptais'), # 1
    ('šiau-rėje', 'šiaurėje'), # 1
    ('por-talus', 'portalus'), # 1
    ('sa-helio', 'sahelio'), # 1
    ('ča-ižant', 'čaižant'), # 1
    ('did-elė', 'didelė'), # 1
    ('tur-gus', 'turgus'), # 1
    ('šil-ko', 'šilko'), # 1
    ('u-pes', 'upes'), # 1

    # Exception
    # ('simono-petro', 'simonopetro'), # 2
]

# Replace silence indicators with appropriate punctuation
silence_replacements = [
    (' _tyla kur ', ', kur '), (' _tyla kuriuo ', ', kuriuo '), (' _pauze karių ', ', karių '),
    ('_pauze ir ', 'ir '), ('_pauze yra ', 'yra '), (' _pauze kur', ', kur'), (' _tyla yra ', ', yra '),
    ('_tyla tačiau ', 'tačiau '), (' _tyla kad ', ', kad '), (' darymas _pauze lietuvių ',' darymas - lietuvių '),
    (' kryžiai _pauze liaudies ', ' kryžiai - liaudies '), (' amato _pauze meno ', ' amato, meno '),
    (' skulptūros kalvystės ', ' skulptūros, kalvystės '),
    ('koplytstulpiai _pauze koplytėlės ', 'koplytstulpiai, koplytėlės '),
    ('geležinėmis viršūnėmis _tyla ornamentuoti kryžiai saulutės', 'geležinėmis viršūnėmis, ornamentuoti kryžiai, saulutės'),
    ('ankoras didžiulis šventyklų rūmų _pauze vandens telkinių', 'ankoras - didžiulis šventyklų, rūmų, vandens telkinių'),
    (' hipotezė _tyla stounhedžas ', ' hipotezė - stounhedžas '), (' goa _pauze įsikūrė ', ' goa įsikūrė '),
    (' akcentas _pauze frontoną ', ' akcentas - frontoną '), (' lubos sunkūs ', ' lubos, sunkūs '),
    (' išskobtos _tyla laidojimo ', ' išskobtos laidojimo '),
    (' žemdirbyste žvejyba medžio raižyba', ' žemdirbyste, žvejyba, medžio raižyba'),
    (' celių bendri valgomieji', ' celių, bendri valgomieji'),
    (' yra pavasarį esu ', ' yra pavasarį, esu '), (' akys pilkos gyvenu ', ' akys pilkos, gyvenu '),
    (' žaisti sportuoti piešti žiūrėti ', ' žaisti, sportuoti, piešti, žiūrėti '),
    ('skauda galvą gerklę sloguoju kosėju turiu ', 'skauda galvą, gerklę, sloguoju, kosėju, turiu '),
    (' vaistus nuo temperatūros nuo kosulio vaistus ', ' vaistus nuo temperatūros, nuo kosulio, vaistus '),
    (' amatininkai _pauze juvelyras ', ' amatininkai - juvelyras '),
    (' prieskonis _pauze druska', ' prieskonis - druska'),
    (' produktai jų apdaurojimo principai  svarbiausi patiekalai kulinarijos filosofija stalo etiketas',
    ' produktai jų apdaurojimo principai, svarbiausi patiekalai, kulinarijos filosofija, stalo etiketas'),
    ('priežasties _tyla iki mūsų dienų _pauze pilies architektūra _pauze išliko _pauze ',
    'priežasties iki mūsų dienų pilies architektūra išliko '),
    (' tapti _pauze klestinčiu ', ' tapti klestinčiu '),
    (' suklestint _pauze vietovė ', ' suklestint, vietovė '), ('prieskoniai _pauze gausi', 'prieskoniai - gausi'),
    ('mėsa _pauze jautiena kiauliena paukštiena aviena ožkiena', 'mėsa: jautiena, kiauliena, paukštiena, aviena, ožkiena '),
    (' priežastis _pauze skirtingos ', ' priežastis - skirtingos '),
    ('salų gyventojai _pauze audrų nublokšti paukščiai _pauze fregata flamingas',
    'salų gyventojai - audrų nublokšti paukščiai: fregata, flamingas'),
    (' šaltiniai _pauze antroji ', ' šaltiniai - antroji '),
    (' pastovus _tyla tvyro ', ' pastovus, tvyro '),
    (' būdinga viduramžių _pauze arabiška ', ' būdinga viduramžių arabiška '),
    (' tautų _pauze tokių kaip ', ' tautų, tokių kaip '),
    (' pajėgumai _tyla bokštas', ' pajėgumai - bokštas'),
    (' yra gyvuliniai _pauze daugiausia ', ' yra gyvuliniai, daugiausia '),
    ('koldūnai virtiniai _pauze šaltanosiai skryliai', 'koldūnai, virtiniai, šaltanosiai, skryliai'),
    ('išvystė _pauze rūkymo tradicijas', 'išvystė rūkymo tradicijas'),
    ('rūšis atrado lėtojo', 'rūšis, atrado lėtojo'),
    ('virtuvėse _pauze gausiai naudojami kmynai mairūnas  petražolė krapas', 'virtuvėse, gausiai naudojami kmynai, mairūnas, petražolė, krapas'),
    ('šakotis žagarėliai _pauze  bajoriškosios virtuvės palikimas', 'šakotis, žagarėliai - bajoriškosios virtuvės palikimas'),
    ('lietuviška virtuvė _pauze lietuvoje', 'lietuviška virtuvė - lietuvoje'),
    ('karaimai _pauze turi', 'karaimai turi'),
    (' piktogramomis _pauze ant ', ' piktogramomis ant '),
    (' indais _pauze ant ', ' indais ant '),
    (' vienuolis _pauze tūkstantis ', ' vienuolis tūkstantis '),
    (' metais _pauze nuo ', ' metais nuo '),
    (' atono kalno _pauze atsikraustė į kalambaką', ' atono kalno _pauze atsikraustė į kalambaką'),
    (' vienuolynai _pauze įkurti ', ' vienuolynai įkurti '),
    (' metrų _pauze aukštyje', ' metrų aukštyje'),
    (' devynioliktame _pauze amžiuje ', ' devynioliktame amžiuje '),
    (' mokinys josifas _tyla po ', ' mokinys josifas po '),
    (' pilis _pauze viena ', ' pilis - viena '),
    (' pilių _pauze pastatytų ', ' pilių, pastatytų '),
    (' septynioliktame _pauze amžiuje', ' septynioliktame amžiuje'),
    (' ketvirto _pauze amžiaus ', ' ketvirto amžiaus '),
    (' kodeksas _tyla graikų ', ' kodeksas - graikų '),
    (' virtuvėse _pauze gausiai naudojami kmynai mairūnas petražolė krapas', ' virtuvėse gausiai naudojami kmynai, mairūnas, petražolė, krapas'),
    (' desertų kaip šakotis žagarėliai _pauze bajoriškosios', ' desertų kaip šakotis, žagarėliai - bajoriškosios'),
    ('bulviniai blynai žemaitiški blynai virtos bulvės su krapais su rūgusiu pienu _tyla varške ', 'bulviniai blynai, žemaitiški blynai, virtos bulvės su krapais, su rūgusiu pienu, varške '),
    ('vienuolynas _pauze didžiausias', 'vienuolynas - didžiausias'),
    ('pastatytas _pauze šešių šimtų _pauze dvidešimt ', 'pastatytas šešių šimtų dvidešimt '),
    ('pirmiausia _pauze įspūdį ', 'pirmiausia įspūdį '),
    ('lubų _pauze išdabinta', 'lubų išdabinta'),
    (' pastatyti _pauze ant ', ' pastatyti ant '),
    ('smiltainio _pauze uolų', 'smiltainio uolų'),
    (' akcentas _pauze kupolinės lubos _pauze mediniai balkonai ir viršutiniai _pauze aukštai', ' akcentas - kupolinės lubos, mediniai balkonai ir viršutiniai aukštai'),
    ('undinės mitinės vandens būtybės randamos ', 'undinės - mitinės vandens būtybės, randamos '),
    (' į vienuolyną _pauze buvo ', ' į vienuolyną buvo '),
    (' uolienoms auštant čaižant vėjams jos kietėjo ', ' uolienoms auštant, čaižant vėjams, jos kietėjo '),
    (' įsodintą žmogų _pauze tam skirto _pauze įrenginio pagalba pakeldavo', ' įsodintą žmogų, tam skirto įrenginio pagalba, pakeldavo'),
    (' raštai _tyla religiniai straipsniai _pauze karių uniformos bei ginklai', 'raštai, religiniai straipsniai, karių uniformos bei ginklai'),
    (' raštai _tyla religiniai straipsniai', 'raštai, religiniai straipsniai'),
    (' megalo _pauze galima ', ' megalo galima '),
    (' nesunku _pauze lyginant ', ' nesunku, lyginant '),
    (' legenda _pauze jo buveinė buvo ', ' legenda, jo buveinė buvo '),
    (' užnešti tik _pauze angelas ar _pauze erelis', ' užnešti tik angelas ar erelis'),
    (' angelas ar _pauze erelis', ' angelas ar erelis'),
    (' vyno rūsys _tyla požeminis kalėjimas _pauze ilgas koridorius ir _pauze kėlimo gervė', ' vyno rūsys, požeminis kalėjimas, ilgas koridorius ir kėlimo gervė'),
    (' patekti _pauze į ', ' patekti į '),
    (' _tyla kaip ir į daugelį kitų _tyla reikia įveikti statų šlaitą', ', kaip ir į daugelį kitų, reikia įveikti statų šlaitą'),
    ('didžiausias _pauze seniausias ir ', 'didžiausias, seniausias ir '),
    ('graikų arabų armėnų _pauze hebrajų _pauze gruzinų _pauze asirų _pauze udų ', 'graikų, arabų, armėnų, hebrajų, gruzinų, asirų, udų '),
    (' konstrukcija _tyla buvo numatytas', ' konstrukcija buvo numatyta'),
    (' meteoros _pauze išvertus ', ' meteoros išvertus '),
    (' kalbos _pauze jis reiškia ', ' kalbos jis reiškia '),
    (' uolas _pauze kybančias ore.', ' uolas, kybančias ore.'),
    (' meteorą _pauze geriausia pradėti sustojimu _pauze megalo vienuolyne', ' meteorą geriausia pradėti sustojimu megalo vienuolyne'),
    (' vienuolynų _pauze įkūrėju _pauze laikomas šventasis _pauze afanasijus', ' vienuolynų įkūrėju laikomas šventasis afanasijus'),
    (' nuo atono kalno _pauze atsikraustė ', ' nuo atono kalno atsikraustė '),
    (' relikvijų _pauze vienuolynas žymus ', ' relikvijų, vienuolynas žymus '),
    (' vienuolynas _pauze kartu su šventojo _pauze antano vienuolynu ', ' vienuolynas kartu su šventojo antano vienuolynu '),
    (' seniausiais pasaulyje _pauze tebeveikiančiais ', ' seniausiais pasaulyje tebeveikiančiais '),
    (' istoriją _pauze pilis ', ' istoriją, pilis '),
    (' visą _pauze ilgą', ' visą ilgą'),
    (' istoriją _tyla nė karto ', ' istoriją nė karto '),
    (' nebuvo _pauze užgrobtas _pauze sugriautas _pauze ar _pauze apgadintas', ' nebuvo užgrobtas, sugriautas ar apgadintas'),
    (' kalno _pauze užnešę _pauze angelai', ' kalno užnešę angelai'),
    (' saugoma _pauze antra ', ' saugoma antra '),
    (' kolekcija _tyla nusileidžianti ', ' kolekcija nusileidžianti '),
    (' tradicijos _tyla šiame', ' tradicijos šiame'),
    (' palaidota kankinė _pauze šventoji kotryna _pauze aleksandrietė', ' palaidota kankinė - šventoji kotryna aleksandrietė'),
    (' bokšto _pauze išreiškiančio', ' bokšto, išreiškiančio'),
    (' stilių _pauze stogai ir ddvikraigiai stogai _pauze pakopa po pakopos _pauze iškyla _pauze aukštai _pauze virš pilies', ' stilių, stogai ir dvikraigiai stogai, pakopa po pakopos iškyla aukštai virš pilies'),
    (' žingsnis _pauze leido ', ' žingsnis leido '),
    (' septynioliktojo _pauze amžiaus _pauze antrojoje ', ' septynioliktojo amžiaus antrojoje '),
    ('kotryna _tyla kilusi', 'kotryna kilusi'),
    (' šeimos _pauze išsilavinusi _pauze mokėjo daug kalbų _pauze studijavo matematiką ', ' šeimos, išsilavinusi, mokėjo daug kalbų, studijavo matematiką '),
    (' krikščionišką tikėjimą romos imperatorių _tyla ji buvo', ' krikščionišką tikėjimą romos imperatorių, ji buvo'),
    (' mochamedas _pauze arabų kalifai _pauze turkų sultonai ir prancūzijos imperatorius napoleonas bonapartas', ' mochamedas, arabų kalifai, turkų sultonai ir prancūzijos imperatorius napoleonas bonapartas'),
    (' islamo šalimi _tyla vienuolyno ', ' islamo šalimi, vienuolyno '),
    (' pilis _tyla tarp jų ir baltojo garnio _tyla turėjo daugiaaukštį pagrindinį bokštą _tyla ir medinę rėminę konstrukciją.', ' pilis, tarp jų ir baltojo garnio, turėjo daugiaaukštį pagrindinį bokštą ir medinę rėminę konstrukciją.'),
    (' kotrynos vienuolynas _pauze rytų stačiatikių vienuolynas egipte _pauze sinajaus ', ' kotrynos vienuolynas - rytų stačiatikių vienuolynas egipte, sinajaus '),
    (' teritorijoje _pauze auga erškėtis _pauze krūmas kurio ', ' teritorijoje auga erškėtis - krūmas, kurio '),
    (' dokumentas _pauze rastas vienuolyne, yra', ' dokumentas, rastas vienuolyne, yra'),
    (' asocijuojasi _pauze aukštos baltai tinkuotos pilies sienos', ' asocijuojasi aukštos, baltai tinkuotos, pilies sienos'),
    (' mozaikų _pauze ikonų iš penkto šešto amžiaus _tyla nepaliestų bizantinio meno', ' mozaikų, ikonų iš penkto šešto amžiaus, nepaliestų bizantinio meno'),
    (' pagrindo _tyla su įgaubtais šonais _tyla ir ', ' pagrindo su įgaubtais šonais ir '),
    (' įtvirtinta tačiau ', ' įtvirtinta, tačiau '),
    (' nebuvo _pauze išmėginti', ' nebuvo išmėginti'),
    ('jies yra sudaryti _pauze iš', 'jie yra sudaryti iš'),
    (' driežai _pauze prisitaikę', ' driežai, prisitaikę'),
    (' keliautojai nuotykių ieškotojai _pauze banginių medžiotojai', ' keliautojai, nuotykių ieškotojai, banginių medžiotojai'),
    ('ankštiniai _pauze svarbiausias ', 'ankštiniai - svarbiausias '),
    ('pagrindo _tyla su įgaubtais nuožulniais šonais _tyla ir', 'pagrindo su įgaubtais nuožulniais šonais ir'),
    (' pasakyti kur yra', ' pasakyti, kur yra'),
    ('ėda ir varles _pauze žiogus sliekus smulkius paukščius jų jauniklius kiaušinius', 'ėda ir varles, žiogus, sliekus, smulkius paukščius, jų jauniklius, kiaušinius'),
    ('sporto šakos _pauze žvejyba', 'sporto šakos, žvejyba'),
    ('biotopuose _tyla vandens telkinių krantuose _pauze pelkėtuose miškuose _pauze kirtavietėse durpynuose karjeruose _pauze kelmų', 'biotopuose: vandens telkinių krantuose, pelkėtuose miškuose, kirtavietėse, durpynuose, karjeruose, kelmų'),
    (' labai lygus _pauze išdžiūvęs tampa panašus į dyglius _tyla tai padeda', ' labai lygus, išdžiūvęs tampa panašus į dyglius, tai padeda'),
    ('aktyviausia sutemus _pauze baikšti', 'aktyviausia sutemus, baikšti'),
    ('pelėmis _pauze pelėnais vandeniniais pelėnais', 'pelėmis, pelėnais, vandeniniais pelėnais'),
    ('krabus _pauze įvairias žuvis', 'krabus, įvairias žuvis'),
    ('šermuonėlis _tyla kiauninių šeimos plėšrus žinduolis', 'šermuonėlis - kiauninių šeimos'),
    ('valdoma teritorija _tyla ne mažiau ', 'valdoma teritorija, ne mažiau '),
    ('ūdra _tyla kiauninių šeimos ', 'ūdra - kiauninių šeimos ')
]

regex_replacements = [
    ('(\s?[\t\r\n]\s?|\s{2,})+', ' '),
    ('\s+$', ''),
    ('^\s+', ''),
]

mistypes = [] + mistypes_1 + mistypes_2 + mistypes_3
