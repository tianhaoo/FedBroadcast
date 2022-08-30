import matplotlib.pyplot as plt

fedavg_s ="""test_semi_fb acc_test_lst [tensor(26.6904), tensor(27.5676), tensor(36.2816), tensor(30.4965), tensor(25.), tensor(22.0803), tensor(25.1812), tensor(26.0323), tensor(20.5128), tensor(19.5255)]
fedavg, day 0 acc_test tensor(25.9368) train_loss 1.9550167866511492
test_semi_fb acc_test_lst [tensor(29.3594), tensor(30.9910), tensor(39.7112), tensor(34.3972), tensor(28.8043), tensor(28.8321), tensor(27.3551), tensor(30.8797), tensor(25.6410), tensor(25.9124)]
fedavg, day 1 acc_test tensor(30.1883) train_loss 1.8673907011206423
test_semi_fb acc_test_lst [tensor(29.3594), tensor(33.1532), tensor(42.2383), tensor(35.2837), tensor(32.4275), tensor(30.8394), tensor(30.2536), tensor(35.1885), tensor(28.7546), tensor(27.5547)]
fedavg, day 2 acc_test tensor(32.5053) train_loss 1.811032896501418
test_semi_fb acc_test_lst [tensor(32.0285), tensor(34.9550), tensor(44.2238), tensor(36.5248), tensor(32.4275), tensor(32.8467), tensor(32.6087), tensor(36.8043), tensor(30.2198), tensor(28.8321)]
fedavg, day 3 acc_test tensor(34.1471) train_loss 1.7726796752873684
test_semi_fb acc_test_lst [tensor(32.2064), tensor(35.3153), tensor(46.5704), tensor(37.0567), tensor(32.2464), tensor(34.6715), tensor(33.6957), tensor(38.2406), tensor(30.9524), tensor(30.2920)]
fedavg, day 4 acc_test tensor(35.1247) train_loss 1.7443929427539908
test_semi_fb acc_test_lst [tensor(32.3843), tensor(36.5766), tensor(47.2924), tensor(38.6525), tensor(32.6087), tensor(34.8540), tensor(35.1449), tensor(38.7792), tensor(31.5018), tensor(30.6569)]
fedavg, day 5 acc_test tensor(35.8451) train_loss 1.721991908255481
test_semi_fb acc_test_lst [tensor(33.8078), tensor(36.2162), tensor(47.8339), tensor(39.3617), tensor(34.0580), tensor(35.0365), tensor(37.1377), tensor(39.3178), tensor(32.6007), tensor(32.2993)]
fedavg, day 6 acc_test tensor(36.7670) train_loss 1.7032469431907211
test_semi_fb acc_test_lst [tensor(33.9858), tensor(36.2162), tensor(49.2780), tensor(39.3617), tensor(34.7826), tensor(36.3139), tensor(37.3188), tensor(39.6768), tensor(33.5165), tensor(32.8467)]
fedavg, day 7 acc_test tensor(37.3297) train_loss 1.687752274205585
test_semi_fb acc_test_lst [tensor(33.9858), tensor(36.2162), tensor(49.4585), tensor(39.7163), tensor(35.5072), tensor(36.8613), tensor(38.4058), tensor(40.0359), tensor(33.8828), tensor(32.8467)]
fedavg, day 8 acc_test tensor(37.6917) train_loss 1.6738593395804602
test_semi_fb acc_test_lst [tensor(34.5196), tensor(36.7568), tensor(49.2780), tensor(39.7163), tensor(35.8696), tensor(37.2263), tensor(38.4058), tensor(40.3950), tensor(34.4322), tensor(33.0292)]
fedavg, day 9 acc_test tensor(37.9629) train_loss 1.6618953334224693
test_semi_fb acc_test_lst [tensor(34.1637), tensor(37.1171), tensor(49.2780), tensor(40.6028), tensor(36.0507), tensor(37.5912), tensor(38.9493), tensor(40.9336), tensor(34.6154), tensor(34.1241)]
fedavg, day 10 acc_test tensor(38.3426) train_loss 1.6504273748783647
test_semi_fb acc_test_lst [tensor(34.5196), tensor(36.3964), tensor(49.6390), tensor(40.4255), tensor(35.8696), tensor(38.6861), tensor(39.6739), tensor(41.8312), tensor(35.5311), tensor(34.4891)]
fedavg, day 11 acc_test tensor(38.7062) train_loss 1.6401643719415937
test_semi_fb acc_test_lst [tensor(35.2313), tensor(36.7568), tensor(50.1805), tensor(40.7801), tensor(37.1377), tensor(38.5037), tensor(40.0362), tensor(42.5494), tensor(35.5311), tensor(34.6715)]
fedavg, day 12 acc_test tensor(39.1378) train_loss 1.6320563455618653
test_semi_fb acc_test_lst [tensor(35.9431), tensor(36.2162), tensor(50.3610), tensor(41.8440), tensor(36.7754), tensor(39.7810), tensor(40.0362), tensor(42.1903), tensor(35.7143), tensor(34.4891)]
fedavg, day 13 acc_test tensor(39.3351) train_loss 1.6242873731258323
test_semi_fb acc_test_lst [tensor(35.7651), tensor(36.5766), tensor(51.0830), tensor(41.8440), tensor(36.4130), tensor(39.4161), tensor(40.2174), tensor(42.0108), tensor(36.0806), tensor(35.5839)]
fedavg, day 14 acc_test tensor(39.4991) train_loss 1.617845392787177
test_semi_fb acc_test_lst [tensor(36.2989), tensor(36.5766), tensor(51.0830), tensor(41.8440), tensor(36.7754), tensor(39.0511), tensor(40.3986), tensor(42.0108), tensor(35.3480), tensor(35.4015)]
fedavg, day 15 acc_test tensor(39.4788) train_loss 1.6116570744583214
test_semi_fb acc_test_lst [tensor(36.8327), tensor(36.7568), tensor(51.0830), tensor(42.7305), tensor(36.4130), tensor(38.8686), tensor(40.9420), tensor(42.1903), tensor(35.5311), tensor(34.6715)]
fedavg, day 16 acc_test tensor(39.6020) train_loss 1.6064521000762095
test_semi_fb acc_test_lst [tensor(37.0107), tensor(36.0360), tensor(51.0830), tensor(42.5532), tensor(36.4130), tensor(38.8686), tensor(40.9420), tensor(42.3698), tensor(36.4469), tensor(35.2190)]
fedavg, day 17 acc_test tensor(39.6942) train_loss 1.6023382872056007
test_semi_fb acc_test_lst [tensor(37.5445), tensor(36.7568), tensor(51.4440), tensor(42.7305), tensor(37.1377), tensor(39.2336), tensor(40.9420), tensor(42.3698), tensor(36.6300), tensor(35.4015)]
fedavg, day 18 acc_test tensor(40.0190) train_loss 1.599311174882017
test_semi_fb acc_test_lst [tensor(37.5445), tensor(36.5766), tensor(51.4440), tensor(42.5532), tensor(36.9565), tensor(39.0511), tensor(41.1232), tensor(42.5494), tensor(37.1795), tensor(36.1314)]
fedavg, day 19 acc_test tensor(40.1109) train_loss 1.5960153835344395
test_semi_fb acc_test_lst [tensor(37.7224), tensor(36.7568), tensor(51.4440), tensor(42.7305), tensor(36.9565), tensor(39.5985), tensor(41.4855), tensor(42.9084), tensor(37.3626), tensor(36.1314)]
fedavg, day 20 acc_test tensor(40.3097) train_loss 1.59425389052133
test_semi_fb acc_test_lst [tensor(37.5445), tensor(36.7568), tensor(51.6245), tensor(42.7305), tensor(37.3188), tensor(39.7810), tensor(41.8478), tensor(42.9084), tensor(37.7289), tensor(36.8613)]
fedavg, day 21 acc_test tensor(40.5103) train_loss 1.592757543008226
test_semi_fb acc_test_lst [tensor(37.3665), tensor(37.4775), tensor(52.7076), tensor(43.2624), tensor(36.9565), tensor(40.5109), tensor(41.6667), tensor(43.0880), tensor(38.0952), tensor(37.0438)]
fedavg, day 22 acc_test tensor(40.8175) train_loss 1.5922529346219614
test_semi_fb acc_test_lst [tensor(37.7224), tensor(37.2973), tensor(51.9856), tensor(43.4397), tensor(36.2319), tensor(40.3285), tensor(41.3043), tensor(43.0880), tensor(38.0952), tensor(37.0438)]
fedavg, day 23 acc_test tensor(40.6537) train_loss 1.5922287534210298
test_semi_fb acc_test_lst [tensor(37.5445), tensor(37.2973), tensor(52.1661), tensor(43.4397), tensor(36.4130), tensor(39.5985), tensor(41.6667), tensor(43.2675), tensor(38.2784), tensor(36.6788)]
fedavg, day 24 acc_test tensor(40.6351) train_loss 1.592270066299491
test_semi_fb acc_test_lst [tensor(37.7224), tensor(37.2973), tensor(52.3466), tensor(43.4397), tensor(36.2319), tensor(40.3285), tensor(41.8478), tensor(43.4470), tensor(38.0952), tensor(37.0438)]
fedavg, day 25 acc_test tensor(40.7800) train_loss 1.5930388827464228
test_semi_fb acc_test_lst [tensor(37.5445), tensor(37.4775), tensor(52.5271), tensor(43.7943), tensor(36.7754), tensor(39.9635), tensor(41.4855), tensor(44.1652), tensor(38.2784), tensor(36.6788)]
fedavg, day 26 acc_test tensor(40.8690) train_loss 1.594065015949397
test_semi_fb acc_test_lst [tensor(37.5445), tensor(37.2973), tensor(52.3466), tensor(43.6170), tensor(36.9565), tensor(39.5985), tensor(41.6667), tensor(44.3447), tensor(38.4615), tensor(36.6788)]
fedavg, day 27 acc_test tensor(40.8512) train_loss 1.5965168204099758
test_semi_fb acc_test_lst [tensor(37.9004), tensor(37.6577), tensor(52.3466), tensor(43.7943), tensor(36.5942), tensor(39.7810), tensor(41.6667), tensor(43.9856), tensor(38.6447), tensor(37.0438)]
fedavg, day 28 acc_test tensor(40.9415) train_loss 1.5984456182943405
test_semi_fb acc_test_lst [tensor(38.0783), tensor(37.2973), tensor(52.1661), tensor(44.1489), tensor(37.1377), tensor(38.8686), tensor(42.0290), tensor(44.1652), tensor(38.6447), tensor(37.2263)]
fedavg, day 29 acc_test tensor(40.9762) train_loss 1.6023588668173323
test_semi_fb acc_test_lst [tensor(38.0783), tensor(36.9369), tensor(51.9856), tensor(43.9716), tensor(37.1377), tensor(39.2336), tensor(42.3913), tensor(43.9856), tensor(39.0110), tensor(37.2263)]
fedavg, day 30 acc_test tensor(40.9958) train_loss 1.6068016179099986
test_semi_fb acc_test_lst [tensor(37.9004), tensor(36.5766), tensor(51.2635), tensor(44.5035), tensor(38.2246), tensor(39.0511), tensor(41.4855), tensor(43.9856), tensor(39.0110), tensor(37.5912)]
fedavg, day 31 acc_test tensor(40.9593) train_loss 1.6110535309978735
test_semi_fb acc_test_lst [tensor(38.2562), tensor(37.1171), tensor(51.4440), tensor(44.1489), tensor(38.7681), tensor(39.0511), tensor(42.0290), tensor(43.9856), tensor(39.1941), tensor(37.0438)]
fedavg, day 32 acc_test tensor(41.1038) train_loss 1.6167155866926473
test_semi_fb acc_test_lst [tensor(38.2562), tensor(37.2973), tensor(51.8051), tensor(44.5035), tensor(38.7681), tensor(39.7810), tensor(42.5725), tensor(43.6266), tensor(39.0110), tensor(37.9562)]
fedavg, day 33 acc_test tensor(41.3577) train_loss 1.6216232495693115
test_semi_fb acc_test_lst [tensor(37.7224), tensor(37.2973), tensor(52.3466), tensor(45.0355), tensor(38.2246), tensor(39.7810), tensor(42.3913), tensor(43.2675), tensor(38.4615), tensor(37.4088)]
fedavg, day 34 acc_test tensor(41.1937) train_loss 1.6275189930065614
test_semi_fb acc_test_lst [tensor(37.9004), tensor(37.6577), tensor(51.2635), tensor(44.6809), tensor(39.3116), tensor(40.1460), tensor(42.0290), tensor(43.9856), tensor(37.9121), tensor(38.8686)]
fedavg, day 35 acc_test tensor(41.3755) train_loss 1.6326732278080758
test_semi_fb acc_test_lst [tensor(38.0783), tensor(37.6577), tensor(51.4440), tensor(44.8582), tensor(38.9493), tensor(39.7810), tensor(42.3913), tensor(44.3447), tensor(38.2784), tensor(38.3212)]
fedavg, day 36 acc_test tensor(41.4104) train_loss 1.6412857015518387
test_semi_fb acc_test_lst [tensor(37.5445), tensor(37.8378), tensor(51.2635), tensor(45.0355), tensor(39.3116), tensor(39.5985), tensor(42.5725), tensor(44.1652), tensor(38.6447), tensor(38.6861)]
fedavg, day 37 acc_test tensor(41.4660) train_loss 1.6471967167755472
test_semi_fb acc_test_lst [tensor(37.9004), tensor(38.0180), tensor(51.0830), tensor(44.8582), tensor(39.8551), tensor(39.9635), tensor(41.8478), tensor(43.9856), tensor(38.8278), tensor(39.0511)]
fedavg, day 38 acc_test tensor(41.5391) train_loss 1.6534480792197335
test_semi_fb acc_test_lst [tensor(37.9004), tensor(38.3784), tensor(50.5415), tensor(44.8582), tensor(39.6739), tensor(39.9635), tensor(42.2101), tensor(44.7038), tensor(39.3773), tensor(39.2336)]
fedavg, day 39 acc_test tensor(41.6841) train_loss 1.6652811974482795
test_semi_fb acc_test_lst [tensor(38.2562), tensor(38.1982), tensor(51.2635), tensor(45.0355), tensor(39.8551), tensor(39.5985), tensor(42.2101), tensor(45.4219), tensor(39.0110), tensor(39.5985)]
fedavg, day 40 acc_test tensor(41.8449) train_loss 1.6730336655177132
test_semi_fb acc_test_lst [tensor(38.7900), tensor(37.4775), tensor(51.6245), tensor(44.8582), tensor(39.6739), tensor(39.9635), tensor(41.8478), tensor(44.8833), tensor(39.5604), tensor(39.7810)]
fedavg, day 41 acc_test tensor(41.8460) train_loss 1.6805690780379319
test_semi_fb acc_test_lst [tensor(38.6121), tensor(36.9369), tensor(50.9025), tensor(45.2128), tensor(40.3986), tensor(39.7810), tensor(42.0290), tensor(45.0628), tensor(39.5604), tensor(39.7810)]
fedavg, day 42 acc_test tensor(41.8277) train_loss 1.690095208919801
test_semi_fb acc_test_lst [tensor(38.9680), tensor(36.7568), tensor(50.3610), tensor(45.2128), tensor(40.7609), tensor(39.2336), tensor(42.2101), tensor(45.4219), tensor(39.5604), tensor(40.3285)]
fedavg, day 43 acc_test tensor(41.8814) train_loss 1.7001189087123927
test_semi_fb acc_test_lst [tensor(39.1459), tensor(36.3964), tensor(50.9025), tensor(45.9220), tensor(40.7609), tensor(38.5037), tensor(42.0290), tensor(45.4219), tensor(39.5604), tensor(40.3285)]
fedavg, day 44 acc_test tensor(41.8971) train_loss 1.7092510942783183
test_semi_fb acc_test_lst [tensor(38.9680), tensor(36.0360), tensor(50.7220), tensor(45.0355), tensor(40.2174), tensor(38.8686), tensor(42.2101), tensor(45.4219), tensor(39.5604), tensor(40.5109)]
fedavg, day 45 acc_test tensor(41.7551) train_loss 1.7199904387902982
test_semi_fb acc_test_lst [tensor(39.1459), tensor(36.3964), tensor(51.0830), tensor(45.2128), tensor(40.2174), tensor(38.8686), tensor(42.0290), tensor(45.2424), tensor(39.1941), tensor(40.5109)]
fedavg, day 46 acc_test tensor(41.7901) train_loss 1.7301903347680982
test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.8559), tensor(50.7220), tensor(44.6809), tensor(40.5797), tensor(39.4161), tensor(41.6667), tensor(45.0628), tensor(39.0110), tensor(41.4234)]
fedavg, day 47 acc_test tensor(41.7742) train_loss 1.7444034899631005
test_semi_fb acc_test_lst [tensor(38.6121), tensor(36.0360), tensor(50.3610), tensor(44.8582), tensor(40.5797), tensor(39.5985), tensor(41.1232), tensor(44.7038), tensor(39.0110), tensor(41.7883)]
fedavg, day 48 acc_test tensor(41.6672) train_loss 1.7557379408898035
test_semi_fb acc_test_lst [tensor(38.4342), tensor(35.6757), tensor(50.9025), tensor(45.2128), tensor(40.2174), tensor(39.2336), tensor(41.3043), tensor(45.0628), tensor(39.0110), tensor(41.0584)]
fedavg, day 49 acc_test tensor(41.6113) train_loss 1.7691207102187585
test_semi_fb acc_test_lst [tensor(38.4342), tensor(35.4955), tensor(50.9025), tensor(45.7447), tensor(40.5797), tensor(38.8686), tensor(41.4855), tensor(45.0628), tensor(38.8278), tensor(41.6058)]
fedavg, day 50 acc_test tensor(41.7007) train_loss 1.7803334264026573
test_semi_fb acc_test_lst [tensor(38.9680), tensor(34.9550), tensor(50.9025), tensor(45.7447), tensor(40.2174), tensor(39.4161), tensor(41.3043), tensor(44.8833), tensor(39.0110), tensor(41.7883)]
fedavg, day 51 acc_test tensor(41.7191) train_loss 1.7925755438140873
test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.8559), tensor(50.3610), tensor(45.3901), tensor(40.5797), tensor(39.0511), tensor(40.9420), tensor(44.5242), tensor(39.3773), tensor(41.4234)]
fedavg, day 52 acc_test tensor(41.6828) train_loss 1.8077002983359103
test_semi_fb acc_test_lst [tensor(39.1459), tensor(35.8559), tensor(50.9025), tensor(45.7447), tensor(40.2174), tensor(38.6861), tensor(40.7609), tensor(45.0628), tensor(38.6447), tensor(42.3358)]
fedavg, day 53 acc_test tensor(41.7357) train_loss 1.8198601689905194
test_semi_fb acc_test_lst [tensor(39.1459), tensor(35.3153), tensor(50.9025), tensor(45.7447), tensor(40.3986), tensor(38.8686), tensor(40.9420), tensor(44.8833), tensor(38.8278), tensor(42.5182)]
fedavg, day 54 acc_test tensor(41.7547) train_loss 1.8362484666842858
test_semi_fb acc_test_lst [tensor(38.4342), tensor(35.6757), tensor(50.9025), tensor(45.9220), tensor(40.3986), tensor(39.0511), tensor(40.7609), tensor(45.0628), tensor(38.8278), tensor(42.1533)]
fedavg, day 55 acc_test tensor(41.7189) train_loss 1.851322822775168
test_semi_fb acc_test_lst [tensor(39.6797), tensor(35.6757), tensor(50.5415), tensor(45.3901), tensor(40.2174), tensor(39.5985), tensor(40.5797), tensor(44.5242), tensor(39.1941), tensor(41.4234)]
fedavg, day 56 acc_test tensor(41.6824) train_loss 1.8628927543638196
test_semi_fb acc_test_lst [tensor(39.1459), tensor(35.1351), tensor(50.5415), tensor(45.2128), tensor(40.2174), tensor(39.0511), tensor(40.7609), tensor(44.8833), tensor(37.9121), tensor(42.5182)]
fedavg, day 57 acc_test tensor(41.5378) train_loss 1.8756993936056634
test_semi_fb acc_test_lst [tensor(38.4342), tensor(35.6757), tensor(50.1805), tensor(45.7447), tensor(40.3986), tensor(39.5985), tensor(40.5797), tensor(45.2424), tensor(38.4615), tensor(41.7883)]
fedavg, day 58 acc_test tensor(41.6104) train_loss 1.8892664207196916
test_semi_fb acc_test_lst [tensor(38.9680), tensor(35.1351), tensor(50.7220), tensor(45.2128), tensor(40.2174), tensor(39.5985), tensor(40.9420), tensor(45.0628), tensor(38.4615), tensor(42.1533)]
fedavg, day 59 acc_test tensor(41.6474) train_loss 1.9074470572134614
test_semi_fb acc_test_lst [tensor(39.5018), tensor(36.0360), tensor(50.5415), tensor(45.5674), tensor(40.2174), tensor(39.2336), tensor(39.6739), tensor(44.8833), tensor(38.2784), tensor(41.9708)]
fedavg, day 60 acc_test tensor(41.5904) train_loss 1.9207968901438648
test_semi_fb acc_test_lst [tensor(39.8577), tensor(35.4955), tensor(50.3610), tensor(45.7447), tensor(40.2174), tensor(40.1460), tensor(41.3043), tensor(45.2424), tensor(38.2784), tensor(42.3358)]
fedavg, day 61 acc_test tensor(41.8983) train_loss 1.93718712740316
test_semi_fb acc_test_lst [tensor(39.1459), tensor(34.2342), tensor(50.1805), tensor(44.8582), tensor(40.2174), tensor(39.2336), tensor(40.2174), tensor(44.5242), tensor(39.0110), tensor(42.5182)]
fedavg, day 62 acc_test tensor(41.4141) train_loss 1.9542036663457596
test_semi_fb acc_test_lst [tensor(39.1459), tensor(34.9550), tensor(49.8195), tensor(45.3901), tensor(39.6739), tensor(39.4161), tensor(40.0362), tensor(45.0628), tensor(39.1941), tensor(41.7883)]
fedavg, day 63 acc_test tensor(41.4482) train_loss 1.9632136236792732
test_semi_fb acc_test_lst [tensor(38.9680), tensor(34.9550), tensor(50.), tensor(45.7447), tensor(39.8551), tensor(39.4161), tensor(40.3986), tensor(44.7038), tensor(39.0110), tensor(41.7883)]
fedavg, day 64 acc_test tensor(41.4840) train_loss 1.9798288484598967
test_semi_fb acc_test_lst [tensor(38.6121), tensor(34.9550), tensor(50.), tensor(45.5674), tensor(39.4928), tensor(39.5985), tensor(39.8551), tensor(45.4219), tensor(39.1941), tensor(42.1533)]
fedavg, day 65 acc_test tensor(41.4850) train_loss 2.0002046653987122
test_semi_fb acc_test_lst [tensor(39.1459), tensor(34.7748), tensor(49.4585), tensor(45.5674), tensor(39.4928), tensor(39.4161), tensor(40.2174), tensor(43.9856), tensor(39.1941), tensor(42.3358)]
fedavg, day 66 acc_test tensor(41.3588) train_loss 2.0161259605118222
test_semi_fb acc_test_lst [tensor(38.6121), tensor(35.1351), tensor(50.3610), tensor(45.5674), tensor(40.0362), tensor(39.2336), tensor(40.0362), tensor(45.0628), tensor(39.3773), tensor(42.7007)]
fedavg, day 67 acc_test tensor(41.6123) train_loss 2.025157132501402
test_semi_fb acc_test_lst [tensor(38.9680), tensor(35.6757), tensor(49.8195), tensor(44.8582), tensor(39.8551), tensor(39.5985), tensor(40.5797), tensor(44.1652), tensor(39.7436), tensor(41.6058)]
fedavg, day 68 acc_test tensor(41.4869) train_loss 2.041602192629436
test_semi_fb acc_test_lst [tensor(38.7900), tensor(35.3153), tensor(50.1805), tensor(44.8582), tensor(39.4928), tensor(39.2336), tensor(40.2174), tensor(44.1652), tensor(39.3773), tensor(42.3358)]
fedavg, day 69 acc_test tensor(41.3966) train_loss 2.0637362233490006
test_semi_fb acc_test_lst [tensor(39.3238), tensor(34.7748), tensor(49.8195), tensor(44.6809), tensor(39.4928), tensor(39.0511), tensor(39.8551), tensor(44.1652), tensor(39.3773), tensor(42.5182)]
fedavg, day 70 acc_test tensor(41.3059) train_loss 2.073375594521229
test_semi_fb acc_test_lst [tensor(39.1459), tensor(35.3153), tensor(50.1805), tensor(44.8582), tensor(40.2174), tensor(39.2336), tensor(40.2174), tensor(43.9856), tensor(40.2930), tensor(41.6058)]
fedavg, day 71 acc_test tensor(41.5053) train_loss 2.0915496653199313
test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.1351), tensor(49.6390), tensor(44.8582), tensor(39.8551), tensor(39.5985), tensor(40.2174), tensor(43.8061), tensor(39.7436), tensor(41.9708)]
fedavg, day 72 acc_test tensor(41.4148) train_loss 2.107992938430415
test_semi_fb acc_test_lst [tensor(39.5018), tensor(35.8559), tensor(50.1805), tensor(44.6809), tensor(39.3116), tensor(39.0511), tensor(40.0362), tensor(44.5242), tensor(39.9267), tensor(42.5182)]
fedavg, day 73 acc_test tensor(41.5587) train_loss 2.125999427615116
test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.3153), tensor(49.8195), tensor(44.3262), tensor(39.3116), tensor(39.2336), tensor(40.2174), tensor(44.7038), tensor(39.3773), tensor(42.1533)]
fedavg, day 74 acc_test tensor(41.3782) train_loss 2.1378308974562565
test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.4955), tensor(50.), tensor(44.5035), tensor(39.8551), tensor(39.5985), tensor(40.3986), tensor(44.3447), tensor(40.1099), tensor(41.7883)]
fedavg, day 75 acc_test tensor(41.5418) train_loss 2.149369612076948
test_semi_fb acc_test_lst [tensor(39.5018), tensor(34.7748), tensor(49.8195), tensor(44.5035), tensor(39.6739), tensor(38.6861), tensor(40.3986), tensor(44.7038), tensor(39.9267), tensor(41.9708)]
fedavg, day 76 acc_test tensor(41.3959) train_loss 2.161574499335291
test_semi_fb acc_test_lst [tensor(39.8577), tensor(35.1351), tensor(50.3610), tensor(44.3262), tensor(39.6739), tensor(39.2336), tensor(40.2174), tensor(45.0628), tensor(39.9267), tensor(42.1533)]
fedavg, day 77 acc_test tensor(41.5948) train_loss 2.1824048596564576
test_semi_fb acc_test_lst [tensor(39.8577), tensor(35.4955), tensor(50.3610), tensor(44.3262), tensor(39.3116), tensor(39.0511), tensor(40.3986), tensor(45.0628), tensor(39.5604), tensor(42.1533)]
fedavg, day 78 acc_test tensor(41.5578) train_loss 2.1981835731943162
test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.3153), tensor(49.8195), tensor(43.9716), tensor(39.1304), tensor(39.2336), tensor(40.2174), tensor(44.5242), tensor(39.7436), tensor(42.1533)]
fedavg, day 79 acc_test tensor(41.3433) train_loss 2.2122162847603746
test_semi_fb acc_test_lst [tensor(39.5018), tensor(35.6757), tensor(50.3610), tensor(43.9716), tensor(38.5870), tensor(39.0511), tensor(40.2174), tensor(44.7038), tensor(40.1099), tensor(42.3358)]
fedavg, day 80 acc_test tensor(41.4515) train_loss 2.2304987136863073
test_semi_fb acc_test_lst [tensor(39.6797), tensor(34.9550), tensor(51.2635), tensor(44.1489), tensor(39.4928), tensor(39.4161), tensor(39.8551), tensor(44.1652), tensor(39.7436), tensor(41.9708)]
fedavg, day 81 acc_test tensor(41.4691) train_loss 2.2355876002412622
test_semi_fb acc_test_lst [tensor(39.5018), tensor(35.1351), tensor(50.1805), tensor(44.1489), tensor(39.4928), tensor(39.7810), tensor(40.0362), tensor(45.0628), tensor(40.1099), tensor(41.9708)]
fedavg, day 82 acc_test tensor(41.5420) train_loss 2.264374027439024
test_semi_fb acc_test_lst [tensor(39.3238), tensor(34.4144), tensor(51.0830), tensor(43.2624), tensor(39.3116), tensor(38.8686), tensor(40.2174), tensor(44.7038), tensor(40.1099), tensor(41.9708)]
fedavg, day 83 acc_test tensor(41.3266) train_loss 2.2716484364783454
test_semi_fb acc_test_lst [tensor(39.1459), tensor(34.5946), tensor(50.3610), tensor(43.9716), tensor(39.1304), tensor(39.4161), tensor(40.0362), tensor(44.5242), tensor(40.1099), tensor(41.9708)]
fedavg, day 84 acc_test tensor(41.3261) train_loss 2.2811419238562745
test_semi_fb acc_test_lst [tensor(39.6797), tensor(34.7748), tensor(50.5415), tensor(43.2624), tensor(39.3116), tensor(39.9635), tensor(39.8551), tensor(44.3447), tensor(40.1099), tensor(41.9708)]
fedavg, day 85 acc_test tensor(41.3814) train_loss 2.2959414780182597
test_semi_fb acc_test_lst [tensor(39.5018), tensor(34.5946), tensor(50.9025), tensor(43.0851), tensor(38.9493), tensor(39.4161), tensor(39.8551), tensor(44.5242), tensor(40.2930), tensor(42.5182)]
fedavg, day 86 acc_test tensor(41.3640) train_loss 2.3119129681190866
test_semi_fb acc_test_lst [tensor(39.8577), tensor(35.3153), tensor(50.5415), tensor(43.2624), tensor(38.7681), tensor(39.2336), tensor(39.6739), tensor(44.7038), tensor(40.8425), tensor(42.3358)]
fedavg, day 87 acc_test tensor(41.4535) train_loss 2.316265101810792
test_semi_fb acc_test_lst [tensor(40.0356), tensor(34.4144), tensor(50.7220), tensor(43.2624), tensor(39.1304), tensor(39.4161), tensor(40.0362), tensor(44.5242), tensor(40.8425), tensor(41.6058)]
fedavg, day 88 acc_test tensor(41.3990) train_loss 2.3375712083748965
test_semi_fb acc_test_lst [tensor(39.6797), tensor(34.7748), tensor(50.7220), tensor(43.6170), tensor(39.3116), tensor(39.4161), tensor(39.6739), tensor(44.8833), tensor(41.2088), tensor(41.6058)]
fedavg, day 89 acc_test tensor(41.4893) train_loss 2.362649836570738
test_semi_fb acc_test_lst [tensor(39.6797), tensor(34.9550), tensor(50.9025), tensor(43.0851), tensor(38.7681), tensor(39.5985), tensor(39.8551), tensor(44.5242), tensor(41.5751), tensor(41.6058)]
fedavg, day 90 acc_test tensor(41.4549) train_loss 2.3664987033986797
test_semi_fb acc_test_lst [tensor(39.8577), tensor(34.5946), tensor(50.7220), tensor(43.0851), tensor(38.7681), tensor(39.5985), tensor(40.0362), tensor(44.8833), tensor(41.0256), tensor(41.7883)]
fedavg, day 91 acc_test tensor(41.4360) train_loss 2.3790433059525786
test_semi_fb acc_test_lst [tensor(40.0356), tensor(34.9550), tensor(50.9025), tensor(43.0851), tensor(38.7681), tensor(39.9635), tensor(40.0362), tensor(44.3447), tensor(41.3919), tensor(42.1533)]
fedavg, day 92 acc_test tensor(41.5636) train_loss 2.3979932592725923
test_semi_fb acc_test_lst [tensor(39.8577), tensor(35.3153), tensor(50.5415), tensor(42.9078), tensor(38.7681), tensor(39.7810), tensor(40.3986), tensor(44.1652), tensor(41.2088), tensor(42.1533)]
fedavg, day 93 acc_test tensor(41.5097) train_loss 2.408656664746099
test_semi_fb acc_test_lst [tensor(39.5018), tensor(35.3153), tensor(50.1805), tensor(43.2624), tensor(38.5870), tensor(40.1460), tensor(40.3986), tensor(44.1652), tensor(41.5751), tensor(41.7883)]
fedavg, day 94 acc_test tensor(41.4920) train_loss 2.4248413187004405
test_semi_fb acc_test_lst [tensor(39.5018), tensor(35.3153), tensor(50.1805), tensor(43.0851), tensor(38.7681), tensor(40.1460), tensor(40.2174), tensor(43.9856), tensor(41.3919), tensor(41.9708)]
fedavg, day 95 acc_test tensor(41.4563) train_loss 2.430579334388783
test_semi_fb acc_test_lst [tensor(39.8577), tensor(35.1351), tensor(50.5415), tensor(43.0851), tensor(38.7681), tensor(39.9635), tensor(40.0362), tensor(43.8061), tensor(41.5751), tensor(41.9708)]
fedavg, day 96 acc_test tensor(41.4739) train_loss 2.4409673563770697
test_semi_fb acc_test_lst [tensor(40.2135), tensor(34.7748), tensor(50.1805), tensor(42.7305), tensor(38.7681), tensor(39.7810), tensor(39.8551), tensor(44.1652), tensor(41.5751), tensor(41.9708)]
fedavg, day 97 acc_test tensor(41.4015) train_loss 2.4587629021513524
test_semi_fb acc_test_lst [tensor(40.2135), tensor(33.8739), tensor(50.7220), tensor(42.7305), tensor(38.9493), tensor(40.3285), tensor(40.0362), tensor(43.6266), tensor(41.7582), tensor(41.9708)]
fedavg, day 98 acc_test tensor(41.4210) train_loss 2.4709103417058325
test_semi_fb acc_test_lst [tensor(40.2135), tensor(34.4144), tensor(50.), tensor(42.5532), tensor(38.9493), tensor(40.1460), tensor(39.6739), tensor(44.3447), tensor(41.5751), tensor(41.9708)]
fedavg, day 99 acc_test tensor(41.3841) train_loss 2.492079746297487
test_semi_fb acc_test_lst [tensor(40.5694), tensor(34.0541), tensor(50.3610), tensor(42.7305), tensor(38.5870), tensor(40.6934), tensor(40.0362), tensor(44.1652), tensor(41.5751), tensor(42.1533)]
fedavg, day 100 acc_test tensor(41.4925) train_loss 2.4982029454125456
test_semi_fb acc_test_lst [tensor(40.5694), tensor(34.0541), tensor(50.), tensor(42.7305), tensor(39.1304), tensor(40.3285), tensor(40.0362), tensor(43.9856), tensor(41.5751), tensor(42.1533)]
fedavg, day 101 acc_test tensor(41.4563) train_loss 2.4972430376113133
test_semi_fb acc_test_lst [tensor(40.9253), tensor(34.2342), tensor(49.6390), tensor(42.9078), tensor(38.9493), tensor(40.5109), tensor(39.8551), tensor(43.9856), tensor(41.5751), tensor(41.9708)]
fedavg, day 102 acc_test tensor(41.4553) train_loss 2.5240058431378816
test_semi_fb acc_test_lst [tensor(40.9253), tensor(34.5946), tensor(49.6390), tensor(42.5532), tensor(38.9493), tensor(40.5109), tensor(39.8551), tensor(44.1652), tensor(41.2088), tensor(42.1533)]
fedavg, day 103 acc_test tensor(41.4555) train_loss 2.533978229578995
test_semi_fb acc_test_lst [tensor(41.2811), tensor(34.4144), tensor(49.2780), tensor(42.3759), tensor(38.9493), tensor(40.5109), tensor(40.0362), tensor(44.1652), tensor(41.0256), tensor(41.9708)]
fedavg, day 104 acc_test tensor(41.4007) train_loss 2.549091481758576
test_semi_fb acc_test_lst [tensor(41.2811), tensor(34.2342), tensor(49.2780), tensor(42.7305), tensor(38.9493), tensor(40.3285), tensor(39.8551), tensor(43.8061), tensor(41.0256), tensor(41.9708)]
fedavg, day 105 acc_test tensor(41.3459) train_loss 2.556909463955184
test_semi_fb acc_test_lst [tensor(41.2811), tensor(34.0541), tensor(49.2780), tensor(42.5532), tensor(38.5870), tensor(40.1460), tensor(39.6739), tensor(43.9856), tensor(41.3919), tensor(42.1533)]
fedavg, day 106 acc_test tensor(41.3104) train_loss 2.562337158508176
test_semi_fb acc_test_lst [tensor(41.4591), tensor(34.0541), tensor(49.0975), tensor(42.9078), tensor(38.7681), tensor(40.3285), tensor(40.0362), tensor(44.1652), tensor(41.3919), tensor(42.1533)]
fedavg, day 107 acc_test tensor(41.4362) train_loss 2.5680890910652128
test_semi_fb acc_test_lst [tensor(41.4591), tensor(34.0541), tensor(48.9170), tensor(42.9078), tensor(38.9493), tensor(40.3285), tensor(39.6739), tensor(43.4470), tensor(41.2088), tensor(42.1533)]
fedavg, day 108 acc_test tensor(41.3099) train_loss 2.5863755571809164
test_semi_fb acc_test_lst [tensor(41.8149), tensor(33.8739), tensor(48.5560), tensor(42.9078), tensor(38.9493), tensor(39.9635), tensor(39.6739), tensor(43.6266), tensor(41.0256), tensor(42.1533)]
fedavg, day 109 acc_test tensor(41.2545) train_loss 2.6031256395439346
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.9170), tensor(42.9078), tensor(38.9493), tensor(40.3285), tensor(39.8551), tensor(43.4470), tensor(41.2088), tensor(42.3358)]
fedavg, day 110 acc_test tensor(41.3640) train_loss 2.618097334146337
test_semi_fb acc_test_lst [tensor(41.6370), tensor(33.6937), tensor(48.7365), tensor(42.7305), tensor(39.1304), tensor(40.5109), tensor(39.8551), tensor(43.2675), tensor(41.0256), tensor(41.9708)]
fedavg, day 111 acc_test tensor(41.2558) train_loss 2.6299966204283844
test_semi_fb acc_test_lst [tensor(41.8149), tensor(33.8739), tensor(48.7365), tensor(42.9078), tensor(38.4058), tensor(40.6934), tensor(39.8551), tensor(43.2675), tensor(41.0256), tensor(42.1533)]
fedavg, day 112 acc_test tensor(41.2734) train_loss 2.6354045854589994
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.0541), tensor(48.7365), tensor(42.7305), tensor(38.4058), tensor(40.6934), tensor(39.8551), tensor(43.2675), tensor(40.8425), tensor(42.5182)]
fedavg, day 113 acc_test tensor(41.2919) train_loss 2.6485852660372986
test_semi_fb acc_test_lst [tensor(41.6370), tensor(33.8739), tensor(48.7365), tensor(42.7305), tensor(38.7681), tensor(41.0584), tensor(39.8551), tensor(43.2675), tensor(40.6593), tensor(42.7007)]
fedavg, day 114 acc_test tensor(41.3287) train_loss 2.657270867979502
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.2342), tensor(48.7365), tensor(42.9078), tensor(38.5870), tensor(41.0584), tensor(39.6739), tensor(43.4470), tensor(40.8425), tensor(42.5182)]
fedavg, day 115 acc_test tensor(41.3643) train_loss 2.6675965117715212
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.7365), tensor(42.5532), tensor(38.4058), tensor(40.8759), tensor(39.8551), tensor(43.4470), tensor(40.8425), tensor(42.5182)]
fedavg, day 116 acc_test tensor(41.2925) train_loss 2.672585230703473
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.7365), tensor(42.5532), tensor(38.2246), tensor(40.8759), tensor(39.6739), tensor(43.2675), tensor(40.6593), tensor(42.5182)]
fedavg, day 117 acc_test tensor(41.2200) train_loss 2.695919712880896
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.7365), tensor(42.5532), tensor(38.7681), tensor(41.0584), tensor(39.8551), tensor(43.2675), tensor(40.8425), tensor(42.5182)]
fedavg, day 118 acc_test tensor(41.3291) train_loss 2.696499484532863
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.9170), tensor(42.5532), tensor(38.9493), tensor(40.8759), tensor(39.8551), tensor(43.2675), tensor(40.6593), tensor(42.3358)]
fedavg, day 119 acc_test tensor(41.3104) train_loss 2.7132509712992667
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.9170), tensor(42.5532), tensor(38.7681), tensor(41.2409), tensor(39.8551), tensor(43.4470), tensor(40.6593), tensor(42.5182)]
fedavg, day 120 acc_test tensor(41.3650) train_loss 2.7047264286238435
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.5560), tensor(42.3759), tensor(38.4058), tensor(41.0584), tensor(39.8551), tensor(43.0880), tensor(40.8425), tensor(42.7007)]
fedavg, day 121 acc_test tensor(41.2573) train_loss 2.7330956785878016
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.0541), tensor(48.5560), tensor(42.3759), tensor(38.5870), tensor(41.0584), tensor(39.8551), tensor(43.2675), tensor(40.6593), tensor(42.3358)]
fedavg, day 122 acc_test tensor(41.2742) train_loss 2.7288959346026256
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.0541), tensor(48.5560), tensor(42.5532), tensor(38.5870), tensor(41.4234), tensor(39.8551), tensor(43.4470), tensor(40.6593), tensor(42.7007)]
fedavg, day 123 acc_test tensor(41.3651) train_loss 2.740529048973723
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.0541), tensor(48.5560), tensor(42.3759), tensor(38.4058), tensor(41.0584), tensor(39.8551), tensor(43.0880), tensor(40.6593), tensor(42.7007)]
fedavg, day 124 acc_test tensor(41.2568) train_loss 2.753109864805869
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.0541), tensor(48.3755), tensor(42.9078), tensor(38.4058), tensor(41.2409), tensor(39.8551), tensor(43.8061), tensor(40.6593), tensor(42.7007)]
fedavg, day 125 acc_test tensor(41.3998) train_loss 2.7757811328767183
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.0541), tensor(48.5560), tensor(42.5532), tensor(38.4058), tensor(41.4234), tensor(39.8551), tensor(43.6266), tensor(40.4762), tensor(42.7007)]
fedavg, day 126 acc_test tensor(41.3644) train_loss 2.772017200761774
test_semi_fb acc_test_lst [tensor(41.8149), tensor(33.8739), tensor(48.5560), tensor(42.7305), tensor(38.4058), tensor(41.4234), tensor(39.6739), tensor(43.6266), tensor(40.8425), tensor(42.8832)]
fedavg, day 127 acc_test tensor(41.3831) train_loss 2.783076486172102
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.0541), tensor(48.5560), tensor(42.7305), tensor(38.2246), tensor(41.4234), tensor(39.8551), tensor(43.6266), tensor(41.0256), tensor(43.0657)]
fedavg, day 128 acc_test tensor(41.4554) train_loss 2.7972592189811594
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.0541), tensor(48.5560), tensor(42.5532), tensor(38.0435), tensor(41.7883), tensor(39.8551), tensor(43.6266), tensor(40.8425), tensor(43.0657)]
fedavg, day 129 acc_test tensor(41.4378) train_loss 2.797889067590691
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.0541), tensor(48.3755), tensor(42.9078), tensor(38.2246), tensor(41.7883), tensor(40.0362), tensor(43.8061), tensor(40.8425), tensor(42.8832)]
fedavg, day 130 acc_test tensor(41.4911) train_loss 2.804065128636331
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.2342), tensor(48.3755), tensor(43.2624), tensor(38.2246), tensor(41.7883), tensor(40.0362), tensor(43.6266), tensor(40.6593), tensor(42.8832)]
fedavg, day 131 acc_test tensor(41.5083) train_loss 2.8215635669728227
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.0541), tensor(48.5560), tensor(43.0851), tensor(38.0435), tensor(41.7883), tensor(40.0362), tensor(43.6266), tensor(41.0256), tensor(43.4307)]
fedavg, day 132 acc_test tensor(41.5461) train_loss 2.8342387491939314
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.0541), tensor(48.3755), tensor(43.0851), tensor(38.0435), tensor(41.7883), tensor(40.0362), tensor(43.6266), tensor(40.8425), tensor(43.0657)]
fedavg, day 133 acc_test tensor(41.4732) train_loss 2.8300846402560706
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.1949), tensor(43.4397), tensor(37.8623), tensor(41.7883), tensor(40.0362), tensor(43.6266), tensor(40.8425), tensor(43.2482)]
fedavg, day 134 acc_test tensor(41.4730) train_loss 2.857657075257974
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.0541), tensor(48.3755), tensor(42.9078), tensor(38.0435), tensor(41.7883), tensor(40.0362), tensor(43.6266), tensor(40.6593), tensor(43.2482)]
fedavg, day 135 acc_test tensor(41.4732) train_loss 2.8565957285021284
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.0541), tensor(48.5560), tensor(42.9078), tensor(38.0435), tensor(41.9708), tensor(40.0362), tensor(43.4470), tensor(40.6593), tensor(43.4307)]
fedavg, day 136 acc_test tensor(41.4920) train_loss 2.8602624140284907
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.2342), tensor(48.7365), tensor(42.9078), tensor(38.0435), tensor(41.9708), tensor(40.0362), tensor(43.4470), tensor(40.6593), tensor(43.4307)]
fedavg, day 137 acc_test tensor(41.5281) train_loss 2.8791196008483433
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.2342), tensor(48.5560), tensor(42.9078), tensor(38.0435), tensor(41.6058), tensor(39.8551), tensor(43.6266), tensor(40.2930), tensor(43.0657)]
fedavg, day 138 acc_test tensor(41.4003) train_loss 2.879267690642976
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.4144), tensor(48.5560), tensor(42.9078), tensor(38.0435), tensor(41.9708), tensor(40.0362), tensor(43.4470), tensor(40.2930), tensor(43.2482)]
fedavg, day 139 acc_test tensor(41.4554) train_loss 2.8935495933365125
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.4144), tensor(48.7365), tensor(42.9078), tensor(37.8623), tensor(41.7883), tensor(40.0362), tensor(43.4470), tensor(40.2930), tensor(43.2482)]
fedavg, day 140 acc_test tensor(41.4371) train_loss 2.89946391695394
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.2342), tensor(48.5560), tensor(43.0851), tensor(38.0435), tensor(41.7883), tensor(40.0362), tensor(43.4470), tensor(40.2930), tensor(43.2482)]
fedavg, day 141 acc_test tensor(41.4369) train_loss 2.917222529145217
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.2342), tensor(48.7365), tensor(42.9078), tensor(37.8623), tensor(41.7883), tensor(39.6739), tensor(43.4470), tensor(40.2930), tensor(43.2482)]
fedavg, day 142 acc_test tensor(41.3828) train_loss 2.903529359607647
test_semi_fb acc_test_lst [tensor(41.4591), tensor(34.4144), tensor(48.3755), tensor(42.9078), tensor(38.0435), tensor(41.6058), tensor(39.8551), tensor(43.4470), tensor(40.4762), tensor(43.6131)]
fedavg, day 143 acc_test tensor(41.4197) train_loss 2.91197556022031
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.7365), tensor(42.7305), tensor(37.8623), tensor(41.7883), tensor(39.6739), tensor(43.4470), tensor(40.1099), tensor(43.4307)]
fedavg, day 144 acc_test tensor(41.3470) train_loss 2.9414796725037426
test_semi_fb acc_test_lst [tensor(41.4591), tensor(34.0541), tensor(48.7365), tensor(42.9078), tensor(37.8623), tensor(41.9708), tensor(39.6739), tensor(43.4470), tensor(40.2930), tensor(43.6131)]
fedavg, day 145 acc_test tensor(41.4018) train_loss 2.9432244918166215
test_semi_fb acc_test_lst [tensor(41.6370), tensor(33.8739), tensor(48.7365), tensor(42.7305), tensor(37.8623), tensor(42.1533), tensor(39.8551), tensor(42.9084), tensor(40.2930), tensor(43.6131)]
fedavg, day 146 acc_test tensor(41.3663) train_loss 2.947572243430473
test_semi_fb acc_test_lst [tensor(41.8149), tensor(33.8739), tensor(48.5560), tensor(42.9078), tensor(37.8623), tensor(41.9708), tensor(39.6739), tensor(43.0880), tensor(40.4762), tensor(43.4307)]
fedavg, day 147 acc_test tensor(41.3654) train_loss 2.9518164275440797
test_semi_fb acc_test_lst [tensor(41.8149), tensor(33.6937), tensor(48.5560), tensor(42.7305), tensor(37.8623), tensor(42.1533), tensor(39.6739), tensor(43.0880), tensor(40.2930), tensor(43.6131)]
fedavg, day 148 acc_test tensor(41.3479) train_loss 2.956805831016462
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.0541), tensor(48.3755), tensor(42.5532), tensor(37.8623), tensor(42.1533), tensor(39.8551), tensor(43.0880), tensor(40.4762), tensor(43.6131)]
fedavg, day 149 acc_test tensor(41.3846) train_loss 2.955620016615278
test_semi_fb acc_test_lst [tensor(41.8149), tensor(33.8739), tensor(48.5560), tensor(42.5532), tensor(37.8623), tensor(42.1533), tensor(39.6739), tensor(42.9084), tensor(40.2930), tensor(43.7956)]
fedavg, day 150 acc_test tensor(41.3485) train_loss 2.9740117871996863
test_semi_fb acc_test_lst [tensor(41.9929), tensor(33.8739), tensor(48.5560), tensor(42.5532), tensor(38.0435), tensor(42.1533), tensor(39.8551), tensor(42.9084), tensor(40.4762), tensor(43.6131)]
fedavg, day 151 acc_test tensor(41.4025) train_loss 2.9703223259396885
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.5560), tensor(42.5532), tensor(38.0435), tensor(41.9708), tensor(39.6739), tensor(43.0880), tensor(40.6593), tensor(43.7956)]
fedavg, day 152 acc_test tensor(41.4031) train_loss 2.9823736485056047
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.0541), tensor(48.5560), tensor(42.5532), tensor(38.0435), tensor(41.9708), tensor(39.8551), tensor(42.7289), tensor(40.6593), tensor(43.6131)]
fedavg, day 153 acc_test tensor(41.4205) train_loss 2.9967074461067487
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.2342), tensor(48.3755), tensor(42.5532), tensor(38.0435), tensor(41.7883), tensor(39.8551), tensor(42.9084), tensor(40.4762), tensor(43.7956)]
fedavg, day 154 acc_test tensor(41.3845) train_loss 2.993359178717865
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.4144), tensor(48.5560), tensor(42.5532), tensor(38.2246), tensor(41.9708), tensor(39.6739), tensor(42.9084), tensor(40.6593), tensor(43.7956)]
fedavg, day 155 acc_test tensor(41.4393) train_loss 3.0105972354042168
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.4144), tensor(48.3755), tensor(42.7305), tensor(38.0435), tensor(41.9708), tensor(40.0362), tensor(42.9084), tensor(40.4762), tensor(43.7956)]
fedavg, day 156 acc_test tensor(41.4566) train_loss 3.0127379753766768
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.2342), tensor(48.3755), tensor(42.5532), tensor(38.0435), tensor(41.9708), tensor(40.2174), tensor(42.9084), tensor(40.6593), tensor(43.6131)]
fedavg, day 157 acc_test tensor(41.4746) train_loss 3.0318009788454496
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.4144), tensor(48.1949), tensor(42.7305), tensor(38.0435), tensor(42.1533), tensor(39.8551), tensor(42.7289), tensor(40.4762), tensor(43.7956)]
fedavg, day 158 acc_test tensor(41.4563) train_loss 3.040541272141384
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.5946), tensor(48.0144), tensor(42.7305), tensor(37.8623), tensor(41.9708), tensor(39.6739), tensor(42.9084), tensor(40.6593), tensor(43.7956)]
fedavg, day 159 acc_test tensor(41.4381) train_loss 3.0435663805442217
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.4144), tensor(48.0144), tensor(42.7305), tensor(37.8623), tensor(41.7883), tensor(39.8551), tensor(42.7289), tensor(40.4762), tensor(43.7956)]
fedavg, day 160 acc_test tensor(41.3659) train_loss 3.0293942004569847
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.4144), tensor(48.0144), tensor(42.7305), tensor(37.8623), tensor(41.9708), tensor(39.6739), tensor(42.7289), tensor(40.6593), tensor(43.7956)]
fedavg, day 161 acc_test tensor(41.3843) train_loss 3.0454816422985624
test_semi_fb acc_test_lst [tensor(42.3488), tensor(34.7748), tensor(47.8339), tensor(42.7305), tensor(38.0435), tensor(41.7883), tensor(39.4928), tensor(42.7289), tensor(40.6593), tensor(43.7956)]
fedavg, day 162 acc_test tensor(41.4196) train_loss 3.063966765329803
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.7748), tensor(47.8339), tensor(42.7305), tensor(37.8623), tensor(41.6058), tensor(39.6739), tensor(42.7289), tensor(40.6593), tensor(43.6131)]
fedavg, day 163 acc_test tensor(41.3653) train_loss 3.064741566155186
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.7748), tensor(47.8339), tensor(42.7305), tensor(37.8623), tensor(41.6058), tensor(39.6739), tensor(42.1903), tensor(40.4762), tensor(43.7956)]
fedavg, day 164 acc_test tensor(41.2936) train_loss 3.069897507787189
test_semi_fb acc_test_lst [tensor(42.3488), tensor(34.7748), tensor(47.8339), tensor(42.7305), tensor(38.0435), tensor(41.6058), tensor(39.4928), tensor(42.1903), tensor(40.8425), tensor(43.6131)]
fedavg, day 165 acc_test tensor(41.3476) train_loss 3.0762263203353153
test_semi_fb acc_test_lst [tensor(42.3488), tensor(34.9550), tensor(47.6534), tensor(42.9078), tensor(38.0435), tensor(41.6058), tensor(39.6739), tensor(42.0108), tensor(40.6593), tensor(43.6131)]
fedavg, day 166 acc_test tensor(41.3471) train_loss 3.072190247986587
test_semi_fb acc_test_lst [tensor(42.3488), tensor(34.7748), tensor(47.8339), tensor(42.9078), tensor(38.0435), tensor(41.2409), tensor(39.6739), tensor(42.1903), tensor(40.8425), tensor(43.6131)]
fedavg, day 167 acc_test tensor(41.3469) train_loss 3.095328949606938
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.7748), tensor(47.8339), tensor(42.7305), tensor(38.2246), tensor(41.4234), tensor(39.6739), tensor(42.1903), tensor(40.6593), tensor(43.6131)]
fedavg, day 168 acc_test tensor(41.3295) train_loss 3.090475745766615
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.5946), tensor(47.6534), tensor(42.7305), tensor(38.0435), tensor(41.0584), tensor(39.6739), tensor(42.0108), tensor(40.6593), tensor(43.6131)]
fedavg, day 169 acc_test tensor(41.2208) train_loss 3.1095240983056702
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.7748), tensor(47.8339), tensor(42.7305), tensor(38.2246), tensor(41.4234), tensor(39.6739), tensor(42.0108), tensor(40.6593), tensor(43.7956)]
fedavg, day 170 acc_test tensor(41.3298) train_loss 3.0995554646085886
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.9550), tensor(47.8339), tensor(42.7305), tensor(38.2246), tensor(41.0584), tensor(39.6739), tensor(41.8312), tensor(40.6593), tensor(43.7956)]
fedavg, day 171 acc_test tensor(41.2933) train_loss 3.117663414178545
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.7748), tensor(47.6534), tensor(42.7305), tensor(38.2246), tensor(41.0584), tensor(39.6739), tensor(41.8312), tensor(40.6593), tensor(43.7956)]
fedavg, day 172 acc_test tensor(41.2573) train_loss 3.1216863302371496
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.7748), tensor(47.6534), tensor(42.7305), tensor(38.2246), tensor(41.0584), tensor(39.6739), tensor(41.8312), tensor(40.6593), tensor(43.9781)]
fedavg, day 173 acc_test tensor(41.2755) train_loss 3.1213104268014846
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.7748), tensor(47.8339), tensor(42.9078), tensor(38.2246), tensor(41.0584), tensor(39.6739), tensor(41.6517), tensor(40.8425), tensor(43.9781)]
fedavg, day 174 acc_test tensor(41.3117) train_loss 3.1325553518769027
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.7748), tensor(47.4729), tensor(42.9078), tensor(38.2246), tensor(41.0584), tensor(39.6739), tensor(41.8312), tensor(40.4762), tensor(43.7956)]
fedavg, day 175 acc_test tensor(41.2386) train_loss 3.1357403507822106
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.7748), tensor(47.6534), tensor(42.9078), tensor(38.0435), tensor(41.2409), tensor(39.6739), tensor(41.6517), tensor(40.6593), tensor(43.9781)]
fedavg, day 176 acc_test tensor(41.2576) train_loss 3.1458713897775032
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.7748), tensor(47.4729), tensor(42.9078), tensor(38.0435), tensor(41.0584), tensor(39.8551), tensor(41.6517), tensor(40.6593), tensor(43.9781)]
fedavg, day 177 acc_test tensor(41.2394) train_loss 3.1402348410075276
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.7748), tensor(47.4729), tensor(42.9078), tensor(38.0435), tensor(41.2409), tensor(39.8551), tensor(41.6517), tensor(40.6593), tensor(43.9781)]
fedavg, day 178 acc_test tensor(41.2577) train_loss 3.1430759091717255
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.7748), tensor(47.2924), tensor(42.9078), tensor(38.0435), tensor(41.0584), tensor(39.6739), tensor(41.8312), tensor(40.6593), tensor(43.9781)]
fedavg, day 179 acc_test tensor(41.2212) train_loss 3.16389961210713
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.2924), tensor(42.9078), tensor(38.0435), tensor(41.0584), tensor(39.8551), tensor(41.4722), tensor(40.6593), tensor(43.9781)]
fedavg, day 180 acc_test tensor(41.1856) train_loss 3.164289448989288
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.4729), tensor(42.9078), tensor(38.0435), tensor(41.2409), tensor(39.8551), tensor(41.6517), tensor(40.6593), tensor(43.9781)]
fedavg, day 181 acc_test tensor(41.2399) train_loss 3.167939700100661
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.2924), tensor(42.9078), tensor(38.0435), tensor(41.0584), tensor(39.8551), tensor(41.4722), tensor(40.4762), tensor(43.9781)]
fedavg, day 182 acc_test tensor(41.1673) train_loss 3.1682773897019327
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.1119), tensor(42.9078), tensor(38.0435), tensor(41.2409), tensor(39.8551), tensor(41.4722), tensor(40.2930), tensor(43.9781)]
fedavg, day 183 acc_test tensor(41.1492) train_loss 3.17544113039603
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.2924), tensor(42.9078), tensor(38.0435), tensor(41.2409), tensor(39.8551), tensor(41.4722), tensor(40.1099), tensor(43.9781)]
fedavg, day 184 acc_test tensor(41.1490) train_loss 3.193355772463605
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.2924), tensor(42.9078), tensor(38.4058), tensor(41.2409), tensor(39.8551), tensor(41.4722), tensor(39.9267), tensor(44.1606)]
fedavg, day 185 acc_test tensor(41.1851) train_loss 3.1949684172164456
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.1119), tensor(42.9078), tensor(38.2246), tensor(41.0584), tensor(39.8551), tensor(41.4722), tensor(39.9267), tensor(44.1606)]
fedavg, day 186 acc_test tensor(41.1307) train_loss 3.184796346902522
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.1119), tensor(42.9078), tensor(38.4058), tensor(41.2409), tensor(39.8551), tensor(41.4722), tensor(40.1099), tensor(44.1606)]
fedavg, day 187 acc_test tensor(41.1854) train_loss 3.2088093873548895
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.1119), tensor(42.7305), tensor(38.4058), tensor(41.2409), tensor(39.8551), tensor(41.4722), tensor(39.9267), tensor(44.1606)]
fedavg, day 188 acc_test tensor(41.1493) train_loss 3.2090884430497444
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.7748), tensor(47.1119), tensor(42.7305), tensor(38.4058), tensor(41.2409), tensor(39.8551), tensor(41.4722), tensor(40.1099), tensor(44.3431)]
fedavg, day 189 acc_test tensor(41.1681) train_loss 3.2138355035612163
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.7748), tensor(46.9314), tensor(42.7305), tensor(38.5870), tensor(41.2409), tensor(40.0362), tensor(41.4722), tensor(40.1099), tensor(44.3431)]
fedavg, day 190 acc_test tensor(41.1863) train_loss 3.2196944465764035
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(46.9314), tensor(42.7305), tensor(38.4058), tensor(41.2409), tensor(39.8551), tensor(41.4722), tensor(40.4762), tensor(44.1606)]
fedavg, day 191 acc_test tensor(41.1862) train_loss 3.2307127177490917
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.7748), tensor(47.1119), tensor(42.7305), tensor(38.4058), tensor(40.8759), tensor(39.8551), tensor(41.4722), tensor(40.2930), tensor(44.1606)]
fedavg, day 192 acc_test tensor(41.1317) train_loss 3.2261530548952453
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.9314), tensor(42.7305), tensor(38.4058), tensor(41.2409), tensor(40.0362), tensor(41.4722), tensor(40.2930), tensor(44.1606)]
fedavg, day 193 acc_test tensor(41.1863) train_loss 3.2359612346087108
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.9314), tensor(42.7305), tensor(38.4058), tensor(41.2409), tensor(40.0362), tensor(41.4722), tensor(40.2930), tensor(44.1606)]
fedavg, day 194 acc_test tensor(41.1863) train_loss 3.2500888717884653
test_semi_fb acc_test_lst [tensor(41.6370), tensor(35.1351), tensor(46.7509), tensor(42.9078), tensor(38.4058), tensor(41.2409), tensor(40.2174), tensor(41.4722), tensor(40.4762), tensor(44.1606)]
fedavg, day 195 acc_test tensor(41.2404) train_loss 3.2509963927632723
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(47.1119), tensor(42.9078), tensor(38.5870), tensor(41.2409), tensor(40.2174), tensor(41.4722), tensor(40.4762), tensor(44.1606)]
fedavg, day 196 acc_test tensor(41.2766) train_loss 3.237988176479115
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.9314), tensor(42.9078), tensor(38.5870), tensor(41.2409), tensor(40.3986), tensor(41.4722), tensor(40.4762), tensor(44.1606)]
fedavg, day 197 acc_test tensor(41.3125) train_loss 3.237329424581525
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.7509), tensor(42.9078), tensor(38.5870), tensor(41.0584), tensor(40.3986), tensor(41.4722), tensor(40.4762), tensor(44.1606)]
fedavg, day 198 acc_test tensor(41.2404) train_loss 3.2570174827585907
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.9314), tensor(42.9078), tensor(38.5870), tensor(41.4234), tensor(40.3986), tensor(41.4722), tensor(40.2930), tensor(44.1606)]
fedavg, day 199 acc_test tensor(41.3124) train_loss 3.2650083572744744
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(42.9078), tensor(38.7681), tensor(41.4234), tensor(40.3986), tensor(41.4722), tensor(40.1099), tensor(44.1606)]
fedavg, day 200 acc_test tensor(41.3302) train_loss 3.259876850465713
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(42.7305), tensor(38.5870), tensor(41.4234), tensor(40.3986), tensor(41.4722), tensor(40.2930), tensor(44.3431)]
fedavg, day 201 acc_test tensor(41.3310) train_loss 3.2760998150455696
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.9314), tensor(42.7305), tensor(38.7681), tensor(41.4234), tensor(40.3986), tensor(41.4722), tensor(40.2930), tensor(44.1606)]
fedavg, day 202 acc_test tensor(41.3128) train_loss 3.2771111574572824
test_semi_fb acc_test_lst [tensor(41.6370), tensor(35.1351), tensor(46.9314), tensor(42.7305), tensor(38.5870), tensor(41.2409), tensor(40.3986), tensor(41.4722), tensor(40.2930), tensor(44.1606)]
fedavg, day 203 acc_test tensor(41.2586) train_loss 3.2695766143070615
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.9314), tensor(42.5532), tensor(38.7681), tensor(41.4234), tensor(40.3986), tensor(41.4722), tensor(40.2930), tensor(44.3431)]
fedavg, day 204 acc_test tensor(41.3133) train_loss 3.282432380764905
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.9314), tensor(42.9078), tensor(38.7681), tensor(41.2409), tensor(40.3986), tensor(41.4722), tensor(40.2930), tensor(44.3431)]
fedavg, day 205 acc_test tensor(41.3305) train_loss 3.266207029754054
test_semi_fb acc_test_lst [tensor(41.6370), tensor(35.1351), tensor(47.2924), tensor(42.9078), tensor(38.5870), tensor(41.6058), tensor(40.2174), tensor(41.4722), tensor(40.4762), tensor(44.3431)]
fedavg, day 206 acc_test tensor(41.3674) train_loss 3.2876681669724572
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(42.9078), tensor(38.7681), tensor(41.4234), tensor(40.3986), tensor(41.2926), tensor(40.4762), tensor(44.3431)]
fedavg, day 207 acc_test tensor(41.3672) train_loss 3.3021885143082756
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(42.7305), tensor(38.7681), tensor(41.2409), tensor(40.2174), tensor(41.4722), tensor(40.4762), tensor(44.3431)]
fedavg, day 208 acc_test tensor(41.3310) train_loss 3.288098813033933
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.3153), tensor(47.1119), tensor(43.2624), tensor(38.5870), tensor(41.6058), tensor(40.2174), tensor(41.2926), tensor(40.2930), tensor(44.3431)]
fedavg, day 209 acc_test tensor(41.3843) train_loss 3.294955175766099
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(47.1119), tensor(42.9078), tensor(38.7681), tensor(41.4234), tensor(40.2174), tensor(41.4722), tensor(40.4762), tensor(44.3431)]
fedavg, day 210 acc_test tensor(41.3848) train_loss 3.30481885678914
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(43.0851), tensor(38.7681), tensor(41.2409), tensor(40.0362), tensor(41.2926), tensor(40.4762), tensor(44.5255)]
fedavg, day 211 acc_test tensor(41.3487) train_loss 3.3231409323065133
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(42.9078), tensor(38.7681), tensor(41.4234), tensor(39.8551), tensor(41.4722), tensor(40.4762), tensor(44.3431)]
fedavg, day 212 acc_test tensor(41.3308) train_loss 3.3398293235652723
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(43.0851), tensor(38.7681), tensor(41.4234), tensor(39.8551), tensor(41.2926), tensor(40.4762), tensor(44.3431)]
fedavg, day 213 acc_test tensor(41.3306) train_loss 3.325795981446697
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.9314), tensor(43.0851), tensor(38.7681), tensor(41.4234), tensor(39.8551), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fedavg, day 214 acc_test tensor(41.3487) train_loss 3.3251410290323595
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(42.7305), tensor(38.9493), tensor(41.6058), tensor(39.8551), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fedavg, day 215 acc_test tensor(41.3677) train_loss 3.3320290216738417
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(47.1119), tensor(42.9078), tensor(38.5870), tensor(41.6058), tensor(39.6739), tensor(41.2926), tensor(40.6593), tensor(44.5255)]
fedavg, day 216 acc_test tensor(41.3492) train_loss 3.3396810468384257
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.7509), tensor(43.0851), tensor(38.7681), tensor(41.4234), tensor(39.6739), tensor(41.4722), tensor(40.6593), tensor(44.5255)]
fedavg, day 217 acc_test tensor(41.3486) train_loss 3.339100108948875
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.7509), tensor(43.0851), tensor(38.9493), tensor(41.4234), tensor(39.6739), tensor(41.4722), tensor(40.6593), tensor(44.5255)]
fedavg, day 218 acc_test tensor(41.3490) train_loss 3.361026560704025
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.9078), tensor(38.9493), tensor(41.4234), tensor(39.6739), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fedavg, day 219 acc_test tensor(41.3127) train_loss 3.3426545961516756
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.9314), tensor(43.2624), tensor(38.9493), tensor(41.4234), tensor(39.6739), tensor(41.4722), tensor(40.6593), tensor(44.5255)]
fedavg, day 220 acc_test tensor(41.4025) train_loss 3.3494403658229674
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.9314), tensor(42.9078), tensor(38.9493), tensor(41.2409), tensor(39.6739), tensor(41.4722), tensor(40.6593), tensor(44.5255)]
fedavg, day 221 acc_test tensor(41.3488) train_loss 3.3747341532778465
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.9314), tensor(42.9078), tensor(38.9493), tensor(41.4234), tensor(39.6739), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fedavg, day 222 acc_test tensor(41.3488) train_loss 3.369682796239794
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.7509), tensor(43.0851), tensor(38.9493), tensor(41.4234), tensor(39.6739), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fedavg, day 223 acc_test tensor(41.3484) train_loss 3.366746549595829
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.7305), tensor(38.9493), tensor(41.6058), tensor(39.6739), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fedavg, day 224 acc_test tensor(41.3132) train_loss 3.3790069757141454
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.7509), tensor(42.9078), tensor(38.9493), tensor(41.6058), tensor(39.6739), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fedavg, day 225 acc_test tensor(41.3490) train_loss 3.369689538354471
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.7305), tensor(38.9493), tensor(41.2409), tensor(39.6739), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fedavg, day 226 acc_test tensor(41.2767) train_loss 3.371739869378067
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.7305), tensor(39.1304), tensor(41.2409), tensor(39.6739), tensor(41.6517), tensor(40.2930), tensor(44.5255)]
fedavg, day 227 acc_test tensor(41.2944) train_loss 3.3733784230396306
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.3899), tensor(42.3759), tensor(39.1304), tensor(41.2409), tensor(39.6739), tensor(41.8312), tensor(40.2930), tensor(44.5255)]
fedavg, day 228 acc_test tensor(41.2589) train_loss 3.3854609998977283
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.5704), tensor(42.5532), tensor(39.1304), tensor(41.2409), tensor(39.6739), tensor(41.6517), tensor(40.2930), tensor(44.5255)]
fedavg, day 229 acc_test tensor(41.2589) train_loss 3.3998658264930737
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.3759), tensor(39.1304), tensor(41.4234), tensor(39.8551), tensor(41.8312), tensor(40.4762), tensor(44.5255)]
fedavg, day 230 acc_test tensor(41.3316) train_loss 3.386267046800185
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.3899), tensor(42.3759), tensor(39.1304), tensor(41.4234), tensor(39.6739), tensor(41.4722), tensor(40.2930), tensor(44.5255)]
fedavg, day 231 acc_test tensor(41.2234) train_loss 3.3956596294394426
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.4928), tensor(41.2409), tensor(39.8551), tensor(42.0108), tensor(40.2930), tensor(44.5255)]
fedavg, day 232 acc_test tensor(41.3489) train_loss 3.3818219578602338
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.3899), tensor(42.5532), tensor(39.4928), tensor(41.4234), tensor(39.8551), tensor(41.8312), tensor(40.2930), tensor(44.5255)]
fedavg, day 233 acc_test tensor(41.3134) train_loss 3.389322084349813
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.3759), tensor(39.3116), tensor(41.2409), tensor(39.8551), tensor(41.8312), tensor(40.2930), tensor(44.5255)]
fedavg, day 234 acc_test tensor(41.2596) train_loss 3.4153943720259416
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.3899), tensor(42.5532), tensor(39.4928), tensor(41.4234), tensor(39.8551), tensor(41.8312), tensor(40.4762), tensor(44.5255)]
fedavg, day 235 acc_test tensor(41.3139) train_loss 3.4011044435117737
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.7305), tensor(39.3116), tensor(41.2409), tensor(39.6739), tensor(42.0108), tensor(40.4762), tensor(44.5255)]
fedavg, day 236 acc_test tensor(41.3132) train_loss 3.40233748693033
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.4928), tensor(41.4234), tensor(39.6739), tensor(41.8312), tensor(40.4762), tensor(44.5255)]
fedavg, day 237 acc_test tensor(41.3139) train_loss 3.431978004886369
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.7305), tensor(39.1304), tensor(41.2409), tensor(39.8551), tensor(42.0108), tensor(40.2930), tensor(44.5255)]
fedavg, day 238 acc_test tensor(41.2949) train_loss 3.445452323019569
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.3899), tensor(42.7305), tensor(39.8551), tensor(41.2409), tensor(39.6739), tensor(42.0108), tensor(40.4762), tensor(44.5255)]
fedavg, day 239 acc_test tensor(41.3495) train_loss 3.4218648470295006
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.4928), tensor(41.2409), tensor(39.6739), tensor(41.6517), tensor(40.4762), tensor(44.5255)]
fedavg, day 240 acc_test tensor(41.2777) train_loss 3.431604220284367
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.3899), tensor(42.5532), tensor(39.6739), tensor(41.2409), tensor(39.6739), tensor(41.8312), tensor(40.4762), tensor(44.5255)]
fedavg, day 241 acc_test tensor(41.2957) train_loss 3.4326054467551774
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.3899), tensor(42.5532), tensor(39.4928), tensor(41.4234), tensor(39.6739), tensor(42.0108), tensor(40.4762), tensor(44.5255)]
fedavg, day 242 acc_test tensor(41.3138) train_loss 3.4469524806380156
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.3899), tensor(42.5532), tensor(39.4928), tensor(41.4234), tensor(39.8551), tensor(42.0108), tensor(40.2930), tensor(44.5255)]
fedavg, day 243 acc_test tensor(41.3136) train_loss 3.4610852999095187
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.3899), tensor(42.5532), tensor(39.6739), tensor(41.2409), tensor(39.6739), tensor(41.8312), tensor(40.2930), tensor(44.5255)]
fedavg, day 244 acc_test tensor(41.2774) train_loss 3.4488652616178515
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.4234), tensor(39.8551), tensor(41.8312), tensor(40.2930), tensor(44.5255)]
fedavg, day 245 acc_test tensor(41.3318) train_loss 3.4463056646577233
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.4234), tensor(39.8551), tensor(41.8312), tensor(40.2930), tensor(44.5255)]
fedavg, day 246 acc_test tensor(41.3318) train_loss 3.4707291549631565
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.2409), tensor(39.8551), tensor(41.8312), tensor(40.2930), tensor(44.5255)]
fedavg, day 247 acc_test tensor(41.3135) train_loss 3.4380885199257616
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.4234), tensor(39.8551), tensor(41.8312), tensor(40.1099), tensor(44.3431)]
fedavg, day 248 acc_test tensor(41.2952) train_loss 3.471070833773964
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.8551), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(40.2930), tensor(44.3431)]
fedavg, day 249 acc_test tensor(41.4043) train_loss 3.4579453633813313
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(40.1099), tensor(44.3431)]
fedavg, day 250 acc_test tensor(41.3317) train_loss 3.4559057081281184
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.2409), tensor(39.8551), tensor(41.6517), tensor(40.1099), tensor(44.3431)]
fedavg, day 251 acc_test tensor(41.2768) train_loss 3.4856424409885496
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.6739), tensor(41.6058), tensor(39.8551), tensor(41.6517), tensor(40.1099), tensor(44.3431)]
fedavg, day 252 acc_test tensor(41.3313) train_loss 3.4715379956006966
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fedavg, day 253 acc_test tensor(41.3496) train_loss 3.4709235586576246
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(40.1099), tensor(44.3431)]
fedavg, day 254 acc_test tensor(41.3675) train_loss 3.4895750776496395
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.6739), tensor(41.6058), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fedavg, day 255 acc_test tensor(41.3491) train_loss 3.5028692948504867
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fedavg, day 256 acc_test tensor(41.3673) train_loss 3.4914112688563406
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.8551), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.3431)]
fedavg, day 257 acc_test tensor(41.4038) train_loss 3.485359187406159
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fedavg, day 258 acc_test tensor(41.3492) train_loss 3.4993627212489833
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.9314), tensor(42.3759), tensor(39.6739), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fedavg, day 259 acc_test tensor(41.3677) train_loss 3.5032088440410267
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(46.5704), tensor(42.3759), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(39.9267), tensor(44.1606)]
fedavg, day 260 acc_test tensor(41.2772) train_loss 3.4999863318295628
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(46.5704), tensor(42.1986), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(39.9267), tensor(44.1606)]
fedavg, day 261 acc_test tensor(41.2595) train_loss 3.5016313219165944
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(46.7509), tensor(42.1986), tensor(39.8551), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(43.9781)]
fedavg, day 262 acc_test tensor(41.2955) train_loss 3.521152112741076
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.5704), tensor(42.1986), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(39.9267), tensor(43.9781)]
fedavg, day 263 acc_test tensor(41.2592) train_loss 3.516510125932742
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(39.9267), tensor(43.9781)]
fedavg, day 264 acc_test tensor(41.2767) train_loss 3.530462866335043
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.8551), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(43.9781)]
fedavg, day 265 acc_test tensor(41.3490) train_loss 3.5310730518458318
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(39.9267), tensor(44.1606)]
fedavg, day 266 acc_test tensor(41.3488) train_loss 3.5296364731092007
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.4928), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(39.9267), tensor(44.1606)]
fedavg, day 267 acc_test tensor(41.3129) train_loss 3.537706170409702
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.9550), tensor(46.7509), tensor(42.3759), tensor(39.6739), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.1606)]
fedavg, day 268 acc_test tensor(41.3492) train_loss 3.541404968881358
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.1606)]
fedavg, day 269 acc_test tensor(41.4028) train_loss 3.5236599727096514
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.1606)]
fedavg, day 270 acc_test tensor(41.3133) train_loss 3.5367567286740984
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.1606)]
fedavg, day 271 acc_test tensor(41.3312) train_loss 3.5552637545265533
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.3153), tensor(46.5704), tensor(42.5532), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.1606)]
fedavg, day 272 acc_test tensor(41.3669) train_loss 3.5697436703000447
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.3153), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(40.1099), tensor(44.1606)]
fedavg, day 273 acc_test tensor(41.3675) train_loss 3.5572515951411
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.1606)]
fedavg, day 274 acc_test tensor(41.3490) train_loss 3.559343205907736
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.1606)]
fedavg, day 275 acc_test tensor(41.3670) train_loss 3.552048355336444
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.1606)]
fedavg, day 276 acc_test tensor(41.3670) train_loss 3.571650852519335
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.3431)]
fedavg, day 277 acc_test tensor(41.3494) train_loss 3.5642789935428674
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.3153), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(40.1099), tensor(44.1606)]
fedavg, day 278 acc_test tensor(41.4031) train_loss 3.552879116753299
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.3431)]
fedavg, day 279 acc_test tensor(41.3495) train_loss 3.581292882532897
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.5704), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.3431)]
fedavg, day 280 acc_test tensor(41.3136) train_loss 3.575095735635116
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.5704), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.7436), tensor(44.3431)]
fedavg, day 281 acc_test tensor(41.3311) train_loss 3.579299311508054
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.1351), tensor(46.5704), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.7436), tensor(44.3431)]
fedavg, day 282 acc_test tensor(41.3129) train_loss 3.589756799674318
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.1986), tensor(39.1304), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.7436), tensor(44.3431)]
fedavg, day 283 acc_test tensor(41.2770) train_loss 3.5840306799395436
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.3431)]
fedavg, day 284 acc_test tensor(41.3856) train_loss 3.572667312003375
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.7509), tensor(42.1986), tensor(39.1304), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.7436), tensor(44.3431)]
fedavg, day 285 acc_test tensor(41.2950) train_loss 3.5828436689787817
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.3431)]
fedavg, day 286 acc_test tensor(41.3498) train_loss 3.5961568046788672
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.4955), tensor(46.7509), tensor(42.1986), tensor(39.1304), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fedavg, day 287 acc_test tensor(41.3494) train_loss 3.61177430647777
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fedavg, day 288 acc_test tensor(41.3495) train_loss 3.598660544570919
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.4955), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.7080)]
fedavg, day 289 acc_test tensor(41.4040) train_loss 3.5929076191178
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.1304), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fedavg, day 290 acc_test tensor(41.3314) train_loss 3.6071285414935788
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.1304), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.7436), tensor(44.3431)]
fedavg, day 291 acc_test tensor(41.3131) train_loss 3.6054310124322315
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fedavg, day 292 acc_test tensor(41.3860) train_loss 3.6131616892199827
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.1304), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(39.7436), tensor(44.3431)]
fedavg, day 293 acc_test tensor(41.3313) train_loss 3.6060491497096696
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fedavg, day 294 acc_test tensor(41.3860) train_loss 3.617465470396787
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fedavg, day 295 acc_test tensor(41.3860) train_loss 3.617696922798155
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.1304), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fedavg, day 296 acc_test tensor(41.4039) train_loss 3.617881320715498
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.4955), tensor(46.7509), tensor(42.3759), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fedavg, day 297 acc_test tensor(41.4223) train_loss 3.6300427640457906
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.1304), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fedavg, day 298 acc_test tensor(41.3862) train_loss 3.613776443810961
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fedavg, day 299 acc_test tensor(41.3865) train_loss 3.64151509606535
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.1304), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.3431)]
fedavg, day 300 acc_test tensor(41.3857) train_loss 3.649513512410075
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fedavg, day 301 acc_test tensor(41.3865) train_loss 3.630162591534058
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fedavg, day 302 acc_test tensor(41.3865) train_loss 3.626906773435018
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.4955), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fedavg, day 303 acc_test tensor(41.4223) train_loss 3.6358327421785117
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fedavg, day 304 acc_test tensor(41.4042) train_loss 3.6391282523204835
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fedavg, day 305 acc_test tensor(41.3855) train_loss 3.6481222880131976
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fedavg, day 306 acc_test tensor(41.4038) train_loss 3.634795212208502
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fedavg, day 307 acc_test tensor(41.4220) train_loss 3.6567595851595796
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(40.1099), tensor(44.5255)]
fedavg, day 308 acc_test tensor(41.4217) train_loss 3.6545351863835753
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.1304), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fedavg, day 309 acc_test tensor(41.3673) train_loss 3.647330716751895
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fedavg, day 310 acc_test tensor(41.4036) train_loss 3.6599858779979426
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.1304), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.7436), tensor(44.5255)]
fedavg, day 311 acc_test tensor(41.3490) train_loss 3.647639489139057
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fedavg, day 312 acc_test tensor(41.4036) train_loss 3.642015733586468
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 313 acc_test tensor(41.4215) train_loss 3.655589742679224
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fedavg, day 314 acc_test tensor(41.4036) train_loss 3.6665925837431654
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 315 acc_test tensor(41.4215) train_loss 3.6716487726728038
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fedavg, day 316 acc_test tensor(41.4036) train_loss 3.666038193804497
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 317 acc_test tensor(41.4393) train_loss 3.670938719532349
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 318 acc_test tensor(41.4035) train_loss 3.681864821624622
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 319 acc_test tensor(41.4035) train_loss 3.6710102004370744
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.3153), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.9708), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 320 acc_test tensor(41.4218) train_loss 3.6854187107603242
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.3153), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 321 acc_test tensor(41.4035) train_loss 3.694470085981986
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.3153), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 322 acc_test tensor(41.4213) train_loss 3.6987486235535427
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.3153), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.9708), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 323 acc_test tensor(41.4218) train_loss 3.7001845801571256
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.6757), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 324 acc_test tensor(41.4396) train_loss 3.6848860440707916
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 325 acc_test tensor(41.4216) train_loss 3.683461148489548
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 326 acc_test tensor(41.4216) train_loss 3.712545497226803
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 327 acc_test tensor(41.4216) train_loss 3.6911671113312714
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 328 acc_test tensor(41.4216) train_loss 3.714706752988602
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 329 acc_test tensor(41.4216) train_loss 3.701797548522297
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 330 acc_test tensor(41.4216) train_loss 3.721824549685181
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 331 acc_test tensor(41.4216) train_loss 3.724614805237376
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fedavg, day 332 acc_test tensor(41.4398) train_loss 3.730721190221825
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 333 acc_test tensor(41.4216) train_loss 3.718385823075475
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.6757), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fedavg, day 334 acc_test tensor(41.4578) train_loss 3.7398313002570855
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.8559), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fedavg, day 335 acc_test tensor(41.4576) train_loss 3.7219872478597456
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fedavg, day 336 acc_test tensor(41.4217) train_loss 3.7402038659184917"""

rr_s="""test_semi_fb acc_test_lst [tensor(27.7580), tensor(27.0270), tensor(33.5740), tensor(29.9645), tensor(33.3333), tensor(35.2190), tensor(31.7029), tensor(36.9838), tensor(29.6703), tensor(33.3942)]
rr, day 0 acc_test tensor(31.8627) train_loss 1.9459608006943083
test_semi_fb acc_test_lst [tensor(32.0285), tensor(29.3694), tensor(35.9206), tensor(34.0426), tensor(36.5942), tensor(37.0438), tensor(35.3261), tensor(39.3178), tensor(31.3187), tensor(38.6861)]
rr, day 1 acc_test tensor(34.9648) train_loss 1.852153680387947
test_semi_fb acc_test_lst [tensor(34.5196), tensor(30.8108), tensor(36.6426), tensor(34.5745), tensor(38.0435), tensor(36.8613), tensor(36.9565), tensor(40.7540), tensor(33.1502), tensor(41.0584)]
rr, day 2 acc_test tensor(36.3371) train_loss 1.7957132326987122
test_semi_fb acc_test_lst [tensor(36.8327), tensor(31.1712), tensor(38.0866), tensor(34.9291), tensor(37.6812), tensor(37.7737), tensor(38.2246), tensor(42.0108), tensor(36.6300), tensor(42.1533)]
rr, day 3 acc_test tensor(37.5493) train_loss 1.7577044587425195
test_semi_fb acc_test_lst [tensor(38.7900), tensor(31.8919), tensor(37.9061), tensor(36.5248), tensor(37.3188), tensor(38.3212), tensor(40.5797), tensor(42.7289), tensor(37.5458), tensor(43.0657)]
rr, day 4 acc_test tensor(38.4673) train_loss 1.7297235260541042
test_semi_fb acc_test_lst [tensor(39.8577), tensor(31.5315), tensor(38.9892), tensor(37.9433), tensor(37.3188), tensor(38.6861), tensor(40.3986), tensor(43.2675), tensor(37.7289), tensor(43.4307)]
rr, day 5 acc_test tensor(38.9152) train_loss 1.7071714452171856
test_semi_fb acc_test_lst [tensor(40.5694), tensor(31.7117), tensor(40.2527), tensor(38.1206), tensor(37.6812), tensor(40.1460), tensor(42.0290), tensor(43.2675), tensor(36.8132), tensor(44.3431)]
rr, day 6 acc_test tensor(39.4934) train_loss 1.6884213914449377
test_semi_fb acc_test_lst [tensor(40.5694), tensor(32.0721), tensor(39.8917), tensor(38.6525), tensor(38.5870), tensor(41.0584), tensor(43.1159), tensor(42.9084), tensor(38.4615), tensor(44.8905)]
rr, day 7 acc_test tensor(40.0207) train_loss 1.672599190099995
test_semi_fb acc_test_lst [tensor(40.7473), tensor(32.7928), tensor(40.0722), tensor(38.6525), tensor(38.7681), tensor(41.6058), tensor(43.4783), tensor(43.8061), tensor(39.1941), tensor(45.0730)]
rr, day 8 acc_test tensor(40.4190) train_loss 1.658829794112837
test_semi_fb acc_test_lst [tensor(41.9929), tensor(32.9730), tensor(41.1552), tensor(38.4752), tensor(39.6739), tensor(42.3358), tensor(43.8406), tensor(44.3447), tensor(38.8278), tensor(46.1679)]
rr, day 9 acc_test tensor(40.9787) train_loss 1.6469527059921156
test_semi_fb acc_test_lst [tensor(42.1708), tensor(33.1532), tensor(41.5162), tensor(39.3617), tensor(41.1232), tensor(43.0657), tensor(43.8406), tensor(45.7810), tensor(38.8278), tensor(47.0803)]
rr, day 10 acc_test tensor(41.5920) train_loss 1.636468104609385
test_semi_fb acc_test_lst [tensor(42.1708), tensor(32.7928), tensor(42.4188), tensor(40.0709), tensor(40.9420), tensor(43.7956), tensor(44.5652), tensor(46.4991), tensor(39.3773), tensor(47.0803)]
rr, day 11 acc_test tensor(41.9713) train_loss 1.6272953520925457
test_semi_fb acc_test_lst [tensor(41.9929), tensor(33.5135), tensor(43.1408), tensor(40.4255), tensor(40.9420), tensor(44.8905), tensor(44.7464), tensor(46.4991), tensor(39.5604), tensor(47.9927)]
rr, day 12 acc_test tensor(42.3704) train_loss 1.6188834540850343
test_semi_fb acc_test_lst [tensor(42.1708), tensor(32.6126), tensor(42.7798), tensor(40.6028), tensor(42.3913), tensor(45.6204), tensor(45.6522), tensor(46.8582), tensor(40.1099), tensor(47.8102)]
rr, day 13 acc_test tensor(42.6608) train_loss 1.611684953134167
test_semi_fb acc_test_lst [tensor(42.3488), tensor(32.7928), tensor(43.3213), tensor(40.0709), tensor(42.9348), tensor(46.3504), tensor(46.1957), tensor(47.0377), tensor(40.8425), tensor(47.8102)]
rr, day 14 acc_test tensor(42.9705) train_loss 1.605215721863976
test_semi_fb acc_test_lst [tensor(42.7046), tensor(32.6126), tensor(44.2238), tensor(40.7801), tensor(42.9348), tensor(46.7153), tensor(46.3768), tensor(46.6786), tensor(40.6593), tensor(47.9927)]
rr, day 15 acc_test tensor(43.1679) train_loss 1.5998492977268484
test_semi_fb acc_test_lst [tensor(42.7046), tensor(32.4324), tensor(43.8628), tensor(40.7801), tensor(42.9348), tensor(47.6277), tensor(45.8333), tensor(47.3968), tensor(41.0256), tensor(47.9927)]
rr, day 16 acc_test tensor(43.2591) train_loss 1.595788851165131
test_semi_fb acc_test_lst [tensor(43.0605), tensor(31.8919), tensor(44.4043), tensor(42.0213), tensor(42.9348), tensor(47.4453), tensor(46.3768), tensor(47.5763), tensor(41.2088), tensor(48.1752)]
rr, day 17 acc_test tensor(43.5095) train_loss 1.5913255486931492
test_semi_fb acc_test_lst [tensor(43.2384), tensor(31.8919), tensor(44.7653), tensor(42.1986), tensor(42.7536), tensor(47.6277), tensor(46.7391), tensor(47.7558), tensor(41.9414), tensor(48.7226)]
rr, day 18 acc_test tensor(43.7635) train_loss 1.5888027291121054
test_semi_fb acc_test_lst [tensor(43.4164), tensor(32.6126), tensor(44.4043), tensor(42.3759), tensor(42.2101), tensor(47.4453), tensor(46.1957), tensor(47.7558), tensor(42.8571), tensor(48.9051)]
rr, day 19 acc_test tensor(43.8178) train_loss 1.5867560087212298
test_semi_fb acc_test_lst [tensor(43.5943), tensor(32.2523), tensor(44.2238), tensor(42.3759), tensor(41.8478), tensor(48.3577), tensor(45.8333), tensor(48.4740), tensor(42.6740), tensor(48.9051)]
rr, day 20 acc_test tensor(43.8538) train_loss 1.5842032411291904
test_semi_fb acc_test_lst [tensor(43.5943), tensor(32.9730), tensor(44.4043), tensor(42.1986), tensor(41.6667), tensor(47.6277), tensor(45.8333), tensor(48.2944), tensor(43.0403), tensor(49.0876)]
rr, day 21 acc_test tensor(43.8720) train_loss 1.5835660201404824
test_semi_fb acc_test_lst [tensor(43.4164), tensor(32.9730), tensor(44.4043), tensor(42.7305), tensor(42.7536), tensor(47.9927), tensor(46.1957), tensor(48.6535), tensor(43.0403), tensor(49.0876)]
rr, day 22 acc_test tensor(44.1248) train_loss 1.5837793746747402
test_semi_fb acc_test_lst [tensor(43.2384), tensor(32.9730), tensor(44.0433), tensor(42.9078), tensor(42.5725), tensor(47.2628), tensor(46.9203), tensor(48.4740), tensor(43.0403), tensor(48.5401)]
rr, day 23 acc_test tensor(43.9972) train_loss 1.5842937436722209
test_semi_fb acc_test_lst [tensor(43.2384), tensor(33.1532), tensor(44.7653), tensor(43.4397), tensor(42.7536), tensor(47.4453), tensor(46.0145), tensor(49.0126), tensor(43.4066), tensor(47.8102)]
rr, day 24 acc_test tensor(44.1039) train_loss 1.5859814455670005
test_semi_fb acc_test_lst [tensor(42.8826), tensor(33.1532), tensor(44.9458), tensor(43.0851), tensor(42.7536), tensor(47.4453), tensor(46.0145), tensor(48.1149), tensor(43.7729), tensor(48.5401)]
rr, day 25 acc_test tensor(44.0708) train_loss 1.588321484321261
test_semi_fb acc_test_lst [tensor(42.7046), tensor(33.3333), tensor(44.9458), tensor(42.7305), tensor(41.8478), tensor(47.2628), tensor(47.2826), tensor(49.0126), tensor(43.5897), tensor(47.9927)]
rr, day 26 acc_test tensor(44.0703) train_loss 1.5894718334964077
test_semi_fb acc_test_lst [tensor(42.7046), tensor(32.9730), tensor(45.3069), tensor(42.1986), tensor(41.6667), tensor(47.4453), tensor(47.4638), tensor(48.1149), tensor(43.5897), tensor(47.6277)]
rr, day 27 acc_test tensor(43.9091) train_loss 1.5921962951250341
test_semi_fb acc_test_lst [tensor(42.7046), tensor(33.6937), tensor(45.3069), tensor(42.0213), tensor(41.8478), tensor(47.4453), tensor(47.6449), tensor(47.9354), tensor(43.4066), tensor(47.8102)]
rr, day 28 acc_test tensor(43.9817) train_loss 1.5956036309097856
test_semi_fb acc_test_lst [tensor(42.1708), tensor(33.5135), tensor(45.3069), tensor(42.0213), tensor(41.8478), tensor(47.2628), tensor(47.6449), tensor(48.2944), tensor(43.7729), tensor(47.2628)]
rr, day 29 acc_test tensor(43.9098) train_loss 1.6000886862309014
test_semi_fb acc_test_lst [tensor(42.8826), tensor(33.5135), tensor(44.7653), tensor(42.0213), tensor(41.8478), tensor(47.4453), tensor(48.1884), tensor(48.2944), tensor(43.5897), tensor(47.2628)]
rr, day 30 acc_test tensor(43.9811) train_loss 1.604991417772129
test_semi_fb acc_test_lst [tensor(43.4164), tensor(33.5135), tensor(44.2238), tensor(42.3759), tensor(41.6667), tensor(48.1752), tensor(47.1014), tensor(48.2944), tensor(42.8571), tensor(46.8978)]
rr, day 31 acc_test tensor(43.8522) train_loss 1.608922660630439
test_semi_fb acc_test_lst [tensor(43.2384), tensor(33.1532), tensor(44.2238), tensor(42.7305), tensor(41.4855), tensor(47.8102), tensor(47.8261), tensor(48.1149), tensor(43.0403), tensor(46.8978)]
rr, day 32 acc_test tensor(43.8521) train_loss 1.6143709778659934
test_semi_fb acc_test_lst [tensor(43.4164), tensor(33.5135), tensor(44.9458), tensor(42.1986), tensor(42.3913), tensor(47.6277), tensor(48.0072), tensor(47.9354), tensor(42.8571), tensor(47.6277)]
rr, day 33 acc_test tensor(44.0521) train_loss 1.6230203206793847
test_semi_fb acc_test_lst [tensor(43.5943), tensor(33.5135), tensor(43.5018), tensor(42.7305), tensor(41.8478), tensor(48.1752), tensor(47.4638), tensor(48.1149), tensor(42.6740), tensor(47.2628)]
rr, day 34 acc_test tensor(43.8879) train_loss 1.628839637238287
test_semi_fb acc_test_lst [tensor(44.1281), tensor(33.6937), tensor(43.8628), tensor(42.7305), tensor(41.6667), tensor(48.3577), tensor(47.8261), tensor(47.5763), tensor(42.8571), tensor(47.4453)]
rr, day 35 acc_test tensor(44.0144) train_loss 1.635380873367144
test_semi_fb acc_test_lst [tensor(44.3060), tensor(33.3333), tensor(43.1408), tensor(43.7943), tensor(42.0290), tensor(48.3577), tensor(47.4638), tensor(47.5763), tensor(42.6740), tensor(47.6277)]
rr, day 36 acc_test tensor(44.0303) train_loss 1.6463059485995726
test_semi_fb acc_test_lst [tensor(44.4840), tensor(34.4144), tensor(43.3213), tensor(43.4397), tensor(42.3913), tensor(47.6277), tensor(47.2826), tensor(47.5763), tensor(42.6740), tensor(47.6277)]
rr, day 37 acc_test tensor(44.0839) train_loss 1.6542869885264884
test_semi_fb acc_test_lst [tensor(44.4840), tensor(34.0541), tensor(43.1408), tensor(43.4397), tensor(42.9348), tensor(48.1752), tensor(47.4638), tensor(47.3968), tensor(42.3077), tensor(47.8102)]
rr, day 38 acc_test tensor(44.1207) train_loss 1.662510543670247
test_semi_fb acc_test_lst [tensor(44.3060), tensor(33.1532), tensor(42.9603), tensor(43.4397), tensor(42.7536), tensor(47.9927), tensor(47.6449), tensor(47.0377), tensor(42.1245), tensor(47.4453)]
rr, day 39 acc_test tensor(43.8858) train_loss 1.672932287293322
test_semi_fb acc_test_lst [tensor(44.3060), tensor(33.3333), tensor(43.3213), tensor(43.7943), tensor(43.4783), tensor(47.9927), tensor(47.1014), tensor(47.5763), tensor(42.4908), tensor(47.2628)]
rr, day 40 acc_test tensor(44.0657) train_loss 1.6832199530396212
test_semi_fb acc_test_lst [tensor(44.8399), tensor(33.5135), tensor(42.9603), tensor(43.9716), tensor(43.4783), tensor(47.9927), tensor(47.2826), tensor(47.2172), tensor(42.6740), tensor(47.6277)]
rr, day 41 acc_test tensor(44.1558) train_loss 1.6928415799356995
test_semi_fb acc_test_lst [tensor(45.0178), tensor(34.2342), tensor(42.9603), tensor(43.6170), tensor(43.2971), tensor(48.3577), tensor(47.6449), tensor(47.7558), tensor(43.2234), tensor(47.4453)]
rr, day 42 acc_test tensor(44.3554) train_loss 1.7023516310392994
test_semi_fb acc_test_lst [tensor(45.0178), tensor(34.0541), tensor(42.0578), tensor(43.6170), tensor(44.2029), tensor(48.3577), tensor(47.1014), tensor(47.5763), tensor(42.4908), tensor(47.6277)]
rr, day 43 acc_test tensor(44.2104) train_loss 1.7164820283578135
test_semi_fb acc_test_lst [tensor(44.1281), tensor(34.7748), tensor(42.7798), tensor(43.0851), tensor(43.2971), tensor(47.8102), tensor(46.9203), tensor(47.5763), tensor(42.6740), tensor(47.4453)]
rr, day 44 acc_test tensor(44.0491) train_loss 1.7279418483420332
test_semi_fb acc_test_lst [tensor(45.0178), tensor(34.7748), tensor(42.0578), tensor(42.7305), tensor(43.4783), tensor(47.6277), tensor(47.2826), tensor(47.9354), tensor(42.4908), tensor(47.6277)]
rr, day 45 acc_test tensor(44.1023) train_loss 1.7393177883213076
test_semi_fb acc_test_lst [tensor(44.6619), tensor(35.4955), tensor(42.4188), tensor(43.2624), tensor(43.6594), tensor(47.8102), tensor(47.2826), tensor(47.3968), tensor(42.4908), tensor(47.6277)]
rr, day 46 acc_test tensor(44.2106) train_loss 1.7523238114394346
test_semi_fb acc_test_lst [tensor(45.0178), tensor(35.8559), tensor(42.2383), tensor(43.4397), tensor(43.6594), tensor(46.8978), tensor(47.4638), tensor(47.7558), tensor(42.4908), tensor(47.6277)]
rr, day 47 acc_test tensor(44.2447) train_loss 1.7641989147739137
test_semi_fb acc_test_lst [tensor(44.1281), tensor(35.4955), tensor(42.4188), tensor(43.6170), tensor(43.6594), tensor(46.8978), tensor(47.2826), tensor(47.9354), tensor(42.3077), tensor(48.1752)]
rr, day 48 acc_test tensor(44.1917) train_loss 1.7767948125670374
test_semi_fb acc_test_lst [tensor(44.8399), tensor(36.0360), tensor(42.0578), tensor(43.4397), tensor(43.4783), tensor(46.7153), tensor(47.4638), tensor(47.7558), tensor(42.6740), tensor(47.2628)]
rr, day 49 acc_test tensor(44.1723) train_loss 1.7887232258932426
test_semi_fb acc_test_lst [tensor(44.6619), tensor(35.6757), tensor(42.4188), tensor(43.9716), tensor(43.6594), tensor(47.0803), tensor(47.4638), tensor(47.5763), tensor(42.6740), tensor(47.6277)]
rr, day 50 acc_test tensor(44.2810) train_loss 1.804560618283744
test_semi_fb acc_test_lst [tensor(45.5516), tensor(34.9550), tensor(42.4188), tensor(43.9716), tensor(43.1159), tensor(46.5328), tensor(47.2826), tensor(47.0377), tensor(42.4908), tensor(47.4453)]
rr, day 51 acc_test tensor(44.0802) train_loss 1.8183922280365183
test_semi_fb acc_test_lst [tensor(45.1957), tensor(35.6757), tensor(42.2383), tensor(43.9716), tensor(42.9348), tensor(46.7153), tensor(46.7391), tensor(47.5763), tensor(42.6740), tensor(47.4453)]
rr, day 52 acc_test tensor(44.1166) train_loss 1.833137614278769
test_semi_fb acc_test_lst [tensor(44.8399), tensor(35.3153), tensor(42.4188), tensor(44.1489), tensor(42.9348), tensor(46.1679), tensor(46.5580), tensor(46.6786), tensor(42.6740), tensor(46.7153)]
rr, day 53 acc_test tensor(43.8451) train_loss 1.848103561702757
test_semi_fb acc_test_lst [tensor(44.6619), tensor(35.4955), tensor(42.4188), tensor(44.3262), tensor(42.7536), tensor(46.7153), tensor(46.5580), tensor(46.6786), tensor(42.4908), tensor(46.8978)]
rr, day 54 acc_test tensor(43.8997) train_loss 1.862483425196331
test_semi_fb acc_test_lst [tensor(45.1957), tensor(34.9550), tensor(41.6968), tensor(44.1489), tensor(42.5725), tensor(46.3504), tensor(46.7391), tensor(47.2172), tensor(43.0403), tensor(46.5328)]
rr, day 55 acc_test tensor(43.8449) train_loss 1.8742413896777794
test_semi_fb acc_test_lst [tensor(44.4840), tensor(35.1351), tensor(41.6968), tensor(43.7943), tensor(42.5725), tensor(45.8029), tensor(46.9203), tensor(46.6786), tensor(42.4908), tensor(46.7153)]
rr, day 56 acc_test tensor(43.6291) train_loss 1.8927537049579142
test_semi_fb acc_test_lst [tensor(44.4840), tensor(34.7748), tensor(42.2383), tensor(43.9716), tensor(42.5725), tensor(47.4453), tensor(47.8261), tensor(46.8582), tensor(42.4908), tensor(46.5328)]
rr, day 57 acc_test tensor(43.9194) train_loss 1.9095385252611348
test_semi_fb acc_test_lst [tensor(44.8399), tensor(34.7748), tensor(41.8773), tensor(43.7943), tensor(42.2101), tensor(46.5328), tensor(47.1014), tensor(47.0377), tensor(42.6740), tensor(47.0803)]
rr, day 58 acc_test tensor(43.7923) train_loss 1.9246449262095586
test_semi_fb acc_test_lst [tensor(44.8399), tensor(35.1351), tensor(41.8773), tensor(43.7943), tensor(42.2101), tensor(46.1679), tensor(47.1014), tensor(47.0377), tensor(43.0403), tensor(47.6277)]
rr, day 59 acc_test tensor(43.8832) train_loss 1.9413600252402525
test_semi_fb acc_test_lst [tensor(44.4840), tensor(34.0541), tensor(41.8773), tensor(43.4397), tensor(41.4855), tensor(46.3504), tensor(46.7391), tensor(46.8582), tensor(42.6740), tensor(47.2628)]
rr, day 60 acc_test tensor(43.5225) train_loss 1.9583348034648924
test_semi_fb acc_test_lst [tensor(44.4840), tensor(34.4144), tensor(42.4188), tensor(44.3262), tensor(41.8478), tensor(46.1679), tensor(47.2826), tensor(46.6786), tensor(43.0403), tensor(47.4453)]
rr, day 61 acc_test tensor(43.8106) train_loss 1.9735981863973249
test_semi_fb acc_test_lst [tensor(45.1957), tensor(34.5946), tensor(42.4188), tensor(44.3262), tensor(41.8478), tensor(46.5328), tensor(47.6449), tensor(47.5763), tensor(43.2234), tensor(47.4453)]
rr, day 62 acc_test tensor(44.0806) train_loss 1.9877991079512498
test_semi_fb acc_test_lst [tensor(44.3060), tensor(34.5946), tensor(42.5993), tensor(44.3262), tensor(41.8478), tensor(45.9854), tensor(46.5580), tensor(46.8582), tensor(43.5897), tensor(47.0803)]
rr, day 63 acc_test tensor(43.7746) train_loss 2.008100261759809
test_semi_fb acc_test_lst [tensor(44.1281), tensor(34.5946), tensor(43.3213), tensor(44.5035), tensor(42.2101), tensor(45.6204), tensor(46.9203), tensor(47.7558), tensor(43.5897), tensor(47.6277)]
rr, day 64 acc_test tensor(44.0272) train_loss 2.018326810399714
test_semi_fb acc_test_lst [tensor(44.6619), tensor(35.4955), tensor(43.5018), tensor(44.5035), tensor(42.0290), tensor(45.6204), tensor(47.2826), tensor(47.3968), tensor(43.4066), tensor(47.8102)]
rr, day 65 acc_test tensor(44.1708) train_loss 2.0394788456983908
test_semi_fb acc_test_lst [tensor(44.3060), tensor(35.8559), tensor(43.1408), tensor(44.1489), tensor(42.2101), tensor(45.8029), tensor(47.4638), tensor(47.2172), tensor(43.5897), tensor(47.6277)]
rr, day 66 acc_test tensor(44.1363) train_loss 2.0514316477555687
test_semi_fb acc_test_lst [tensor(44.3060), tensor(35.3153), tensor(43.5018), tensor(43.9716), tensor(42.2101), tensor(45.8029), tensor(47.2826), tensor(47.3968), tensor(43.9560), tensor(47.4453)]
rr, day 67 acc_test tensor(44.1189) train_loss 2.067846105812939
test_semi_fb acc_test_lst [tensor(44.8399), tensor(35.4955), tensor(43.1408), tensor(43.9716), tensor(42.3913), tensor(45.4380), tensor(47.6449), tensor(47.5763), tensor(43.7729), tensor(47.4453)]
rr, day 68 acc_test tensor(44.1716) train_loss 2.081040233751104
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.4955), tensor(43.8628), tensor(44.1489), tensor(42.2101), tensor(45.0730), tensor(47.4638), tensor(47.5763), tensor(43.9560), tensor(47.8102)]
rr, day 69 acc_test tensor(44.1191) train_loss 2.0949366711852253
test_semi_fb acc_test_lst [tensor(44.3060), tensor(35.1351), tensor(43.1408), tensor(43.9716), tensor(42.2101), tensor(45.2555), tensor(46.3768), tensor(47.5763), tensor(43.5897), tensor(47.2628)]
rr, day 70 acc_test tensor(43.8825) train_loss 2.108880780009189
test_semi_fb acc_test_lst [tensor(44.1281), tensor(34.9550), tensor(43.3213), tensor(44.1489), tensor(42.3913), tensor(45.2555), tensor(46.7391), tensor(47.5763), tensor(43.7729), tensor(47.6277)]
rr, day 71 acc_test tensor(43.9916) train_loss 2.1295492595061374
test_semi_fb acc_test_lst [tensor(43.7722), tensor(34.7748), tensor(43.8628), tensor(43.7943), tensor(42.2101), tensor(44.8905), tensor(46.7391), tensor(47.7558), tensor(43.5897), tensor(47.8102)]
rr, day 72 acc_test tensor(43.9200) train_loss 2.148076713997357
test_semi_fb acc_test_lst [tensor(43.4164), tensor(34.9550), tensor(43.3213), tensor(43.6170), tensor(42.5725), tensor(45.6204), tensor(47.1014), tensor(47.3968), tensor(43.5897), tensor(47.4453)]
rr, day 73 acc_test tensor(43.9036) train_loss 2.159862273959234
test_semi_fb acc_test_lst [tensor(43.7722), tensor(34.9550), tensor(43.5018), tensor(43.2624), tensor(42.5725), tensor(44.8905), tensor(46.3768), tensor(47.7558), tensor(43.5897), tensor(47.0803)]
rr, day 74 acc_test tensor(43.7757) train_loss 2.1790410964074747
test_semi_fb acc_test_lst [tensor(43.2384), tensor(34.7748), tensor(44.0433), tensor(43.2624), tensor(42.5725), tensor(45.4380), tensor(46.9203), tensor(47.5763), tensor(43.7729), tensor(47.0803)]
rr, day 75 acc_test tensor(43.8679) train_loss 2.19529769031177
test_semi_fb acc_test_lst [tensor(43.5943), tensor(34.7748), tensor(44.4043), tensor(43.4397), tensor(42.5725), tensor(45.8029), tensor(46.3768), tensor(47.3968), tensor(43.9560), tensor(46.8978)]
rr, day 76 acc_test tensor(43.9216) train_loss 2.2060464796060355
test_semi_fb acc_test_lst [tensor(43.5943), tensor(34.9550), tensor(42.9603), tensor(43.0851), tensor(42.2101), tensor(45.0730), tensor(46.0145), tensor(47.7558), tensor(43.5897), tensor(46.5328)]
rr, day 77 acc_test tensor(43.5771) train_loss 2.2270544757045143
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.6823), tensor(43.0851), tensor(42.2101), tensor(44.8905), tensor(46.5580), tensor(47.5763), tensor(43.7729), tensor(47.0803)]
rr, day 78 acc_test tensor(43.7948) train_loss 2.236618466194712
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.3153), tensor(43.8628), tensor(43.0851), tensor(42.0290), tensor(45.9854), tensor(46.3768), tensor(47.7558), tensor(43.7729), tensor(46.8978)]
rr, day 79 acc_test tensor(43.8319) train_loss 2.245867530556564
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.4955), tensor(43.6823), tensor(43.4397), tensor(42.3913), tensor(45.2555), tensor(46.3768), tensor(47.2172), tensor(43.4066), tensor(47.2628)]
rr, day 80 acc_test tensor(43.7944) train_loss 2.2658718842524115
test_semi_fb acc_test_lst [tensor(43.0605), tensor(34.9550), tensor(43.6823), tensor(42.5532), tensor(41.6667), tensor(45.9854), tensor(46.3768), tensor(47.3968), tensor(43.4066), tensor(47.0803)]
rr, day 81 acc_test tensor(43.6163) train_loss 2.2758537190853323
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.3153), tensor(43.6823), tensor(43.0851), tensor(41.4855), tensor(45.6204), tensor(46.5580), tensor(46.8582), tensor(43.5897), tensor(47.4453)]
rr, day 82 acc_test tensor(43.6878) train_loss 2.289365382568597
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.3153), tensor(43.8628), tensor(43.2624), tensor(41.4855), tensor(45.6204), tensor(46.5580), tensor(47.2172), tensor(43.7729), tensor(47.6277)]
rr, day 83 acc_test tensor(43.8139) train_loss 2.3122273121353705
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.3153), tensor(43.1408), tensor(42.7305), tensor(41.8478), tensor(45.2555), tensor(46.3768), tensor(47.2172), tensor(43.7729), tensor(47.2628)]
rr, day 84 acc_test tensor(43.6158) train_loss 2.3215422303211826
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.3153), tensor(43.8628), tensor(42.7305), tensor(41.6667), tensor(45.4380), tensor(46.1957), tensor(47.2172), tensor(43.5897), tensor(47.4453)]
rr, day 85 acc_test tensor(43.6700) train_loss 2.340420018723332
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.1351), tensor(44.2238), tensor(42.7305), tensor(41.4855), tensor(45.4380), tensor(46.5580), tensor(47.2172), tensor(43.9560), tensor(47.6277)]
rr, day 86 acc_test tensor(43.7788) train_loss 2.355815443405438
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.3153), tensor(43.8628), tensor(42.9078), tensor(41.4855), tensor(45.2555), tensor(46.9203), tensor(47.0377), tensor(44.1392), tensor(46.8978)]
rr, day 87 acc_test tensor(43.7060) train_loss 2.3655235691215633
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.4955), tensor(43.6823), tensor(42.9078), tensor(41.4855), tensor(45.4380), tensor(46.7391), tensor(47.2172), tensor(43.4066), tensor(47.4453)]
rr, day 88 acc_test tensor(43.7412) train_loss 2.3790433464275016
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.3153), tensor(43.6823), tensor(42.7305), tensor(41.3043), tensor(45.4380), tensor(46.5580), tensor(47.0377), tensor(43.7729), tensor(47.2628)]
rr, day 89 acc_test tensor(43.6340) train_loss 2.3948470932247075
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.6823), tensor(42.9078), tensor(41.1232), tensor(46.1679), tensor(46.9203), tensor(47.3968), tensor(43.4066), tensor(47.2628)]
rr, day 90 acc_test tensor(43.8138) train_loss 2.4048493444598544
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.8628), tensor(42.9078), tensor(41.3043), tensor(45.6204), tensor(46.3768), tensor(47.5763), tensor(43.5897), tensor(46.7153)]
rr, day 91 acc_test tensor(43.7224) train_loss 2.429567666050287
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.1351), tensor(43.8628), tensor(42.7305), tensor(41.3043), tensor(45.9854), tensor(46.9203), tensor(46.8582), tensor(43.7729), tensor(46.5328)]
rr, day 92 acc_test tensor(43.6875) train_loss 2.4380259707020837
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.1351), tensor(44.0433), tensor(42.7305), tensor(41.1232), tensor(45.6204), tensor(46.5580), tensor(47.0377), tensor(43.5897), tensor(47.4453)]
rr, day 93 acc_test tensor(43.6522) train_loss 2.4565413118231247
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.1351), tensor(44.2238), tensor(42.5532), tensor(41.3043), tensor(45.8029), tensor(46.9203), tensor(46.8582), tensor(43.4066), tensor(47.2628)]
rr, day 94 acc_test tensor(43.6706) train_loss 2.4629655237123114
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.3153), tensor(43.6823), tensor(42.3759), tensor(40.9420), tensor(45.4380), tensor(46.9203), tensor(46.6786), tensor(43.5897), tensor(47.0803)]
rr, day 95 acc_test tensor(43.5795) train_loss 2.469029997179258
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.4955), tensor(44.2238), tensor(42.1986), tensor(41.3043), tensor(45.4380), tensor(47.1014), tensor(46.8582), tensor(43.5897), tensor(46.8978)]
rr, day 96 acc_test tensor(43.6880) train_loss 2.48548195551417
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.4955), tensor(44.2238), tensor(42.0213), tensor(40.9420), tensor(45.4380), tensor(46.7391), tensor(46.4991), tensor(43.5897), tensor(46.5328)]
rr, day 97 acc_test tensor(43.4898) train_loss 2.506750126417885
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.1351), tensor(44.2238), tensor(42.1986), tensor(40.9420), tensor(45.6204), tensor(47.1014), tensor(46.4991), tensor(43.2234), tensor(46.8978)]
rr, day 98 acc_test tensor(43.5436) train_loss 2.511369806587013
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.6757), tensor(43.6823), tensor(42.3759), tensor(41.1232), tensor(45.4380), tensor(47.2826), tensor(46.4991), tensor(43.4066), tensor(47.0803)]
rr, day 99 acc_test tensor(43.6514) train_loss 2.5233873366353685
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.6757), tensor(44.0433), tensor(42.1986), tensor(41.1232), tensor(46.1679), tensor(47.2826), tensor(46.4991), tensor(43.7729), tensor(46.7153)]
rr, day 100 acc_test tensor(43.7429) train_loss 2.532536932612294
test_semi_fb acc_test_lst [tensor(44.3060), tensor(35.4955), tensor(44.0433), tensor(42.3759), tensor(41.3043), tensor(45.2555), tensor(47.2826), tensor(46.4991), tensor(43.7729), tensor(46.8978)]
rr, day 101 acc_test tensor(43.7233) train_loss 2.5516916549306634
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.6757), tensor(44.0433), tensor(42.3759), tensor(40.9420), tensor(45.4380), tensor(47.4638), tensor(46.4991), tensor(43.9560), tensor(46.3504)]
rr, day 102 acc_test tensor(43.6694) train_loss 2.5680746787475766
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.3153), tensor(44.0433), tensor(42.3759), tensor(40.9420), tensor(45.4380), tensor(47.1014), tensor(46.3196), tensor(43.5897), tensor(46.5328)]
rr, day 103 acc_test tensor(43.5430) train_loss 2.581301555783908
test_semi_fb acc_test_lst [tensor(44.3060), tensor(35.4955), tensor(43.6823), tensor(42.7305), tensor(41.3043), tensor(45.6204), tensor(47.1014), tensor(46.3196), tensor(43.5897), tensor(46.1679)]
rr, day 104 acc_test tensor(43.6318) train_loss 2.5942412090098803
test_semi_fb acc_test_lst [tensor(44.1281), tensor(35.4955), tensor(43.8628), tensor(42.5532), tensor(41.3043), tensor(45.4380), tensor(47.2826), tensor(45.9605), tensor(43.0403), tensor(46.5328)]
rr, day 105 acc_test tensor(43.5598) train_loss 2.60195643227791
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.3153), tensor(44.0433), tensor(42.5532), tensor(41.1232), tensor(45.2555), tensor(47.2826), tensor(45.9605), tensor(43.9560), tensor(46.3504)]
rr, day 106 acc_test tensor(43.5612) train_loss 2.6128423504716296
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.1351), tensor(43.5018), tensor(42.7305), tensor(40.9420), tensor(45.2555), tensor(47.2826), tensor(46.1400), tensor(43.4066), tensor(46.1679)]
rr, day 107 acc_test tensor(43.4512) train_loss 2.622966891401812
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.1351), tensor(43.6823), tensor(42.9078), tensor(41.3043), tensor(44.8905), tensor(47.1014), tensor(45.9605), tensor(43.4066), tensor(46.3504)]
rr, day 108 acc_test tensor(43.4511) train_loss 2.6323017151127215
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.4955), tensor(43.5018), tensor(42.9078), tensor(40.7609), tensor(45.0730), tensor(47.6449), tensor(45.7810), tensor(43.0403), tensor(46.1679)]
rr, day 109 acc_test tensor(43.4323) train_loss 2.649154079767218
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.4955), tensor(43.5018), tensor(43.2624), tensor(40.9420), tensor(45.0730), tensor(47.2826), tensor(45.6014), tensor(43.2234), tensor(46.3504)]
rr, day 110 acc_test tensor(43.4683) train_loss 2.6611706863229743
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.6757), tensor(43.8628), tensor(42.9078), tensor(40.9420), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(43.2234), tensor(45.9854)]
rr, day 111 acc_test tensor(43.4321) train_loss 2.666273868084599
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.6757), tensor(43.3213), tensor(43.2624), tensor(40.9420), tensor(45.2555), tensor(47.4638), tensor(45.6014), tensor(43.4066), tensor(45.8029)]
rr, day 112 acc_test tensor(43.4504) train_loss 2.681448194038045
test_semi_fb acc_test_lst [tensor(44.1281), tensor(35.6757), tensor(43.6823), tensor(43.2624), tensor(40.7609), tensor(44.8905), tensor(46.9203), tensor(45.6014), tensor(43.0403), tensor(46.3504)]
rr, day 113 acc_test tensor(43.4312) train_loss 2.694862989810216
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.4955), tensor(43.6823), tensor(43.2624), tensor(40.9420), tensor(44.8905), tensor(47.1014), tensor(45.6014), tensor(43.2234), tensor(45.8029)]
rr, day 114 acc_test tensor(43.3952) train_loss 2.703227015649286
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.3153), tensor(43.8628), tensor(43.0851), tensor(40.9420), tensor(44.8905), tensor(47.1014), tensor(45.6014), tensor(43.2234), tensor(46.3504)]
rr, day 115 acc_test tensor(43.4323) train_loss 2.714301542664288
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.6757), tensor(44.2238), tensor(43.2624), tensor(40.9420), tensor(45.0730), tensor(47.1014), tensor(45.6014), tensor(43.4066), tensor(46.1679)]
rr, day 116 acc_test tensor(43.5404) train_loss 2.7235453722351814
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.6757), tensor(44.4043), tensor(43.0851), tensor(40.9420), tensor(45.0730), tensor(47.1014), tensor(45.6014), tensor(43.2234), tensor(46.1679)]
rr, day 117 acc_test tensor(43.5225) train_loss 2.7254162959021953
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.6757), tensor(44.4043), tensor(43.2624), tensor(40.9420), tensor(45.0730), tensor(47.2826), tensor(45.4219), tensor(43.4066), tensor(45.9854)]
rr, day 118 acc_test tensor(43.5226) train_loss 2.7442070904265274
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.8559), tensor(44.9458), tensor(43.2624), tensor(40.9420), tensor(45.0730), tensor(47.4638), tensor(45.6014), tensor(43.2234), tensor(46.1679)]
rr, day 119 acc_test tensor(43.6486) train_loss 2.7545193334377194
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.1351), tensor(44.4043), tensor(43.4397), tensor(40.9420), tensor(45.0730), tensor(47.4638), tensor(45.6014), tensor(43.4066), tensor(46.3504)]
rr, day 120 acc_test tensor(43.5589) train_loss 2.7647537915679736
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.8559), tensor(44.4043), tensor(43.4397), tensor(41.1232), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(43.2234), tensor(45.9854)]
rr, day 121 acc_test tensor(43.5760) train_loss 2.78195053661218
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.4955), tensor(44.2238), tensor(43.4397), tensor(40.7609), tensor(44.8905), tensor(47.2826), tensor(45.6014), tensor(43.2234), tensor(45.9854)]
rr, day 122 acc_test tensor(43.4854) train_loss 2.7807013086882737
test_semi_fb acc_test_lst [tensor(43.9502), tensor(36.0360), tensor(44.2238), tensor(43.4397), tensor(40.9420), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(43.2234), tensor(46.3504)]
rr, day 123 acc_test tensor(43.6121) train_loss 2.7932302404556744
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.6757), tensor(44.2238), tensor(43.4397), tensor(40.7609), tensor(44.8905), tensor(47.6449), tensor(45.4219), tensor(43.2234), tensor(46.1679)]
rr, day 124 acc_test tensor(43.5221) train_loss 2.8159502431789734
test_semi_fb acc_test_lst [tensor(43.9502), tensor(36.0360), tensor(44.2238), tensor(43.2624), tensor(40.9420), tensor(45.0730), tensor(47.6449), tensor(45.6014), tensor(42.8571), tensor(45.9854)]
rr, day 125 acc_test tensor(43.5576) train_loss 2.822463824939561
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.4955), tensor(44.0433), tensor(43.2624), tensor(41.1232), tensor(44.8905), tensor(47.6449), tensor(45.4219), tensor(43.0403), tensor(46.1679)]
rr, day 126 acc_test tensor(43.5040) train_loss 2.8165438806328633
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.4955), tensor(44.2238), tensor(43.2624), tensor(40.9420), tensor(44.8905), tensor(47.6449), tensor(45.6014), tensor(42.8571), tensor(46.1679)]
rr, day 127 acc_test tensor(43.4858) train_loss 2.8393239707466167
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.8559), tensor(44.4043), tensor(42.9078), tensor(40.9420), tensor(45.0730), tensor(47.8261), tensor(45.4219), tensor(43.2234), tensor(46.1679)]
rr, day 128 acc_test tensor(43.5773) train_loss 2.8398518898605998
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.6757), tensor(44.4043), tensor(43.0851), tensor(41.1232), tensor(45.2555), tensor(47.6449), tensor(45.7810), tensor(42.6740), tensor(45.9854)]
rr, day 129 acc_test tensor(43.5401) train_loss 2.854290992240964
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.4955), tensor(44.2238), tensor(43.0851), tensor(40.9420), tensor(44.8905), tensor(47.6449), tensor(45.6014), tensor(42.6740), tensor(45.9854)]
rr, day 130 acc_test tensor(43.4493) train_loss 2.864090924749688
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.8559), tensor(44.0433), tensor(42.9078), tensor(40.9420), tensor(45.2555), tensor(47.6449), tensor(45.6014), tensor(42.4908), tensor(46.1679)]
rr, day 131 acc_test tensor(43.4682) train_loss 2.872442431586005
test_semi_fb acc_test_lst [tensor(44.1281), tensor(35.4955), tensor(44.4043), tensor(43.0851), tensor(40.9420), tensor(44.8905), tensor(47.6449), tensor(45.6014), tensor(42.4908), tensor(45.8029)]
rr, day 132 acc_test tensor(43.4486) train_loss 2.874575500138107
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.6757), tensor(43.8628), tensor(43.0851), tensor(40.9420), tensor(45.0730), tensor(47.6449), tensor(45.6014), tensor(42.4908), tensor(46.1679)]
rr, day 133 acc_test tensor(43.4316) train_loss 2.8941389390389207
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.4955), tensor(44.2238), tensor(42.7305), tensor(40.9420), tensor(44.8905), tensor(47.6449), tensor(45.6014), tensor(42.3077), tensor(46.1679)]
rr, day 134 acc_test tensor(43.3599) train_loss 2.8951132455140005
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.8559), tensor(43.8628), tensor(42.7305), tensor(40.9420), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(42.4908), tensor(46.1679)]
rr, day 135 acc_test tensor(43.3600) train_loss 2.9094360827026002
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.6757), tensor(43.8628), tensor(42.3759), tensor(40.9420), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(42.4908), tensor(46.1679)]
rr, day 136 acc_test tensor(43.3243) train_loss 2.9244577762246076
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.8559), tensor(43.6823), tensor(42.5532), tensor(40.9420), tensor(44.8905), tensor(47.6449), tensor(45.6014), tensor(42.4908), tensor(46.3504)]
rr, day 137 acc_test tensor(43.3606) train_loss 2.931126181232965
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.8559), tensor(44.0433), tensor(42.7305), tensor(40.9420), tensor(44.8905), tensor(47.6449), tensor(45.6014), tensor(42.4908), tensor(46.3504)]
rr, day 138 acc_test tensor(43.4322) train_loss 2.9405882725482773
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.8559), tensor(43.6823), tensor(42.7305), tensor(41.1232), tensor(44.8905), tensor(47.2826), tensor(45.7810), tensor(42.4908), tensor(46.7153)]
rr, day 139 acc_test tensor(43.4502) train_loss 2.9474119330708857
test_semi_fb acc_test_lst [tensor(44.1281), tensor(35.8559), tensor(43.5018), tensor(42.1986), tensor(41.1232), tensor(44.8905), tensor(47.4638), tensor(45.7810), tensor(42.4908), tensor(46.7153)]
rr, day 140 acc_test tensor(43.4149) train_loss 2.9536359163308252
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.8559), tensor(43.6823), tensor(42.5532), tensor(41.1232), tensor(44.8905), tensor(47.2826), tensor(45.7810), tensor(42.3077), tensor(46.8978)]
rr, day 141 acc_test tensor(43.4324) train_loss 2.9547421984875717
test_semi_fb acc_test_lst [tensor(43.9502), tensor(35.8559), tensor(43.6823), tensor(42.3759), tensor(41.1232), tensor(44.8905), tensor(47.4638), tensor(45.7810), tensor(42.1245), tensor(46.8978)]
rr, day 142 acc_test tensor(43.4145) train_loss 2.9647768411127395
test_semi_fb acc_test_lst [tensor(43.9502), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(40.9420), tensor(44.8905), tensor(47.2826), tensor(45.7810), tensor(42.3077), tensor(46.8978)]
rr, day 143 acc_test tensor(43.3962) train_loss 2.98136966445984
test_semi_fb acc_test_lst [tensor(43.7722), tensor(36.0360), tensor(43.6823), tensor(42.5532), tensor(41.1232), tensor(44.8905), tensor(47.2826), tensor(45.9605), tensor(42.1245), tensor(46.7153)]
rr, day 144 acc_test tensor(43.4140) train_loss 2.9860355230842726
test_semi_fb acc_test_lst [tensor(43.7722), tensor(36.2162), tensor(43.6823), tensor(42.3759), tensor(40.9420), tensor(44.8905), tensor(47.2826), tensor(45.9605), tensor(42.3077), tensor(46.8978)]
rr, day 145 acc_test tensor(43.4328) train_loss 2.992532026049158
test_semi_fb acc_test_lst [tensor(43.9502), tensor(36.2162), tensor(43.6823), tensor(42.3759), tensor(40.9420), tensor(44.8905), tensor(47.2826), tensor(45.9605), tensor(42.3077), tensor(46.8978)]
rr, day 146 acc_test tensor(43.4506) train_loss 3.008276891095982
test_semi_fb acc_test_lst [tensor(43.9502), tensor(36.2162), tensor(43.6823), tensor(42.3759), tensor(41.1232), tensor(44.8905), tensor(47.2826), tensor(45.9605), tensor(42.3077), tensor(46.8978)]
rr, day 147 acc_test tensor(43.4687) train_loss 3.00570372479187
test_semi_fb acc_test_lst [tensor(43.9502), tensor(36.0360), tensor(43.5018), tensor(42.5532), tensor(41.3043), tensor(44.8905), tensor(47.2826), tensor(45.9605), tensor(42.3077), tensor(47.0803)]
rr, day 148 acc_test tensor(43.4867) train_loss 3.013023518580953
test_semi_fb acc_test_lst [tensor(43.7722), tensor(36.2162), tensor(43.5018), tensor(42.9078), tensor(41.3043), tensor(44.8905), tensor(47.2826), tensor(45.9605), tensor(42.4908), tensor(46.8978)]
rr, day 149 acc_test tensor(43.5225) train_loss 3.036729332982456
test_semi_fb acc_test_lst [tensor(43.7722), tensor(36.2162), tensor(43.6823), tensor(42.9078), tensor(41.4855), tensor(44.8905), tensor(47.2826), tensor(45.9605), tensor(42.3077), tensor(47.0803)]
rr, day 150 acc_test tensor(43.5586) train_loss 3.0438282959202434
test_semi_fb acc_test_lst [tensor(43.7722), tensor(36.0360), tensor(43.5018), tensor(42.9078), tensor(41.3043), tensor(44.5255), tensor(47.1014), tensor(45.9605), tensor(42.4908), tensor(47.0803)]
rr, day 151 acc_test tensor(43.4681) train_loss 3.040584685631337
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.8559), tensor(43.3213), tensor(42.9078), tensor(41.3043), tensor(44.7080), tensor(47.2826), tensor(46.1400), tensor(42.6740), tensor(47.0803)]
rr, day 152 acc_test tensor(43.4869) train_loss 3.048673028659229
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.8559), tensor(43.8628), tensor(42.9078), tensor(41.3043), tensor(44.7080), tensor(47.1014), tensor(46.1400), tensor(42.6740), tensor(47.0803)]
rr, day 153 acc_test tensor(43.5051) train_loss 3.0422650766081873
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.5018), tensor(42.7305), tensor(41.3043), tensor(44.8905), tensor(47.2826), tensor(46.1400), tensor(42.4908), tensor(47.0803)]
rr, day 154 acc_test tensor(43.4695) train_loss 3.0609945788950608
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.8559), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.1014), tensor(46.1400), tensor(42.6740), tensor(47.0803)]
rr, day 155 acc_test tensor(43.4155) train_loss 3.0762482940386713
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.6823), tensor(42.7305), tensor(41.3043), tensor(44.5255), tensor(47.4638), tensor(45.9605), tensor(42.8571), tensor(47.0803)]
rr, day 156 acc_test tensor(43.5057) train_loss 3.0639711290785563
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.6823), tensor(42.5532), tensor(41.3043), tensor(44.5255), tensor(47.1014), tensor(45.9605), tensor(42.6740), tensor(46.8978)]
rr, day 157 acc_test tensor(43.4152) train_loss 3.0681263802495624
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.6823), tensor(42.5532), tensor(41.3043), tensor(44.5255), tensor(47.2826), tensor(46.1400), tensor(42.8571), tensor(47.0803)]
rr, day 158 acc_test tensor(43.4695) train_loss 3.09105586388575
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.8559), tensor(43.6823), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.2826), tensor(45.9605), tensor(42.8571), tensor(47.0803)]
rr, day 159 acc_test tensor(43.4879) train_loss 3.1074156048922648
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.5018), tensor(42.3759), tensor(41.3043), tensor(44.5255), tensor(47.4638), tensor(46.1400), tensor(42.6740), tensor(46.8978)]
rr, day 160 acc_test tensor(43.4153) train_loss 3.101158330761332
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.8559), tensor(43.5018), tensor(42.5532), tensor(41.3043), tensor(44.5255), tensor(47.4638), tensor(45.9605), tensor(42.6740), tensor(47.0803)]
rr, day 161 acc_test tensor(43.4692) train_loss 3.113456944056886
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.6757), tensor(43.6823), tensor(42.3759), tensor(41.3043), tensor(44.5255), tensor(47.2826), tensor(46.1400), tensor(42.6740), tensor(47.0803)]
rr, day 162 acc_test tensor(43.4513) train_loss 3.1122999915847265
test_semi_fb acc_test_lst [tensor(43.7722), tensor(36.0360), tensor(43.8628), tensor(42.3759), tensor(41.3043), tensor(44.5255), tensor(47.4638), tensor(46.1400), tensor(42.6740), tensor(46.7153)]
rr, day 163 acc_test tensor(43.4870) train_loss 3.1388360677747067
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.8559), tensor(43.8628), tensor(42.3759), tensor(41.3043), tensor(44.5255), tensor(47.4638), tensor(46.1400), tensor(42.6740), tensor(46.7153)]
rr, day 164 acc_test tensor(43.4690) train_loss 3.1333428606670886
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.8559), tensor(43.6823), tensor(42.3759), tensor(41.3043), tensor(44.5255), tensor(47.2826), tensor(46.1400), tensor(42.6740), tensor(46.5328)]
rr, day 165 acc_test tensor(43.3968) train_loss 3.1336456380282023
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.8559), tensor(43.8628), tensor(42.3759), tensor(41.3043), tensor(44.5255), tensor(47.2826), tensor(46.1400), tensor(42.6740), tensor(46.7153)]
rr, day 166 acc_test tensor(43.4331) train_loss 3.143887543976041
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.8559), tensor(43.8628), tensor(42.7305), tensor(41.1232), tensor(44.7080), tensor(47.2826), tensor(46.1400), tensor(42.6740), tensor(46.5328)]
rr, day 167 acc_test tensor(43.4504) train_loss 3.1491604388774608
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.8559), tensor(43.8628), tensor(42.7305), tensor(41.1232), tensor(44.5255), tensor(47.2826), tensor(46.1400), tensor(42.6740), tensor(46.7153)]
rr, day 168 acc_test tensor(43.4504) train_loss 3.180777573403625
test_semi_fb acc_test_lst [tensor(43.5943), tensor(36.0360), tensor(43.8628), tensor(42.7305), tensor(41.1232), tensor(44.7080), tensor(47.1014), tensor(46.1400), tensor(42.6740), tensor(46.7153)]
rr, day 169 acc_test tensor(43.4686) train_loss 3.157794588820486
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.8559), tensor(43.6823), tensor(42.9078), tensor(41.1232), tensor(44.7080), tensor(47.2826), tensor(46.1400), tensor(42.4908), tensor(46.7153)]
rr, day 170 acc_test tensor(43.4500) train_loss 3.1819534438520707
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.8559), tensor(43.6823), tensor(42.7305), tensor(41.1232), tensor(44.7080), tensor(47.1014), tensor(46.1400), tensor(42.4908), tensor(46.7153)]
rr, day 171 acc_test tensor(43.3964) train_loss 3.185547416244244
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.6823), tensor(42.7305), tensor(41.1232), tensor(44.5255), tensor(47.1014), tensor(46.1400), tensor(42.4908), tensor(46.5328)]
rr, day 172 acc_test tensor(43.3419) train_loss 3.1893258692356365
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.6823), tensor(42.9078), tensor(41.1232), tensor(44.7080), tensor(47.1014), tensor(46.1400), tensor(42.4908), tensor(46.3504)]
rr, day 173 acc_test tensor(43.3956) train_loss 3.199870666149273
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.6823), tensor(42.9078), tensor(41.1232), tensor(44.7080), tensor(47.1014), tensor(46.1400), tensor(42.6740), tensor(46.5328)]
rr, day 174 acc_test tensor(43.3962) train_loss 3.195982736854569
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.8559), tensor(43.6823), tensor(42.7305), tensor(41.1232), tensor(44.7080), tensor(47.1014), tensor(46.1400), tensor(42.4908), tensor(46.5328)]
rr, day 175 acc_test tensor(43.3781) train_loss 3.2091137825145957
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.6823), tensor(42.7305), tensor(41.1232), tensor(44.8905), tensor(47.1014), tensor(46.1400), tensor(42.6740), tensor(46.3504)]
rr, day 176 acc_test tensor(43.4145) train_loss 3.220847265702109
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.8559), tensor(43.6823), tensor(42.9078), tensor(41.1232), tensor(44.7080), tensor(47.1014), tensor(45.9605), tensor(42.6740), tensor(46.3504)]
rr, day 177 acc_test tensor(43.3780) train_loss 3.21917014402142
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.6823), tensor(42.9078), tensor(41.1232), tensor(44.7080), tensor(46.9203), tensor(45.9605), tensor(42.6740), tensor(46.3504)]
rr, day 178 acc_test tensor(43.3419) train_loss 3.2320735586886906
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.4955), tensor(43.6823), tensor(42.9078), tensor(41.1232), tensor(44.7080), tensor(47.1014), tensor(45.9605), tensor(42.4908), tensor(46.1679)]
rr, day 179 acc_test tensor(43.3054) train_loss 3.240535949416026
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.4955), tensor(43.6823), tensor(42.9078), tensor(41.1232), tensor(44.7080), tensor(46.9203), tensor(45.9605), tensor(42.4908), tensor(46.1679)]
rr, day 180 acc_test tensor(43.2873) train_loss 3.2400138702599923
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.6823), tensor(42.9078), tensor(41.3043), tensor(44.7080), tensor(46.9203), tensor(45.9605), tensor(42.4908), tensor(46.1679)]
rr, day 181 acc_test tensor(43.3412) train_loss 3.236971178071289
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.6823), tensor(43.0851), tensor(41.3043), tensor(44.8905), tensor(47.2826), tensor(45.9605), tensor(42.4908), tensor(46.1679)]
rr, day 182 acc_test tensor(43.3956) train_loss 3.2412801354550878
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.6823), tensor(42.9078), tensor(41.1232), tensor(44.8905), tensor(47.2826), tensor(45.9605), tensor(42.4908), tensor(46.1679)]
rr, day 183 acc_test tensor(43.3598) train_loss 3.2603312083285623
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(43.0851), tensor(41.4855), tensor(44.7080), tensor(47.2826), tensor(45.9605), tensor(42.4908), tensor(46.1679)]
rr, day 184 acc_test tensor(43.3772) train_loss 3.249538635069356
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.6823), tensor(43.0851), tensor(41.4855), tensor(44.7080), tensor(47.4638), tensor(45.9605), tensor(42.4908), tensor(46.3504)]
rr, day 185 acc_test tensor(43.4496) train_loss 3.2712560711066656
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.5018), tensor(43.2624), tensor(41.4855), tensor(44.7080), tensor(47.4638), tensor(45.9605), tensor(42.4908), tensor(46.1679)]
rr, day 186 acc_test tensor(43.4133) train_loss 3.258234870636315
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.5018), tensor(43.2624), tensor(41.4855), tensor(45.0730), tensor(47.4638), tensor(45.9605), tensor(42.4908), tensor(46.3504)]
rr, day 187 acc_test tensor(43.4680) train_loss 3.2602681956721025
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.9078), tensor(41.4855), tensor(44.7080), tensor(47.2826), tensor(46.1400), tensor(42.4908), tensor(46.5328)]
rr, day 188 acc_test tensor(43.3961) train_loss 3.2762220793744006
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.9078), tensor(41.4855), tensor(44.8905), tensor(47.4638), tensor(45.9605), tensor(42.4908), tensor(46.3504)]
rr, day 189 acc_test tensor(43.3963) train_loss 3.288620403213788
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(43.2624), tensor(41.3043), tensor(44.5255), tensor(47.2826), tensor(45.9605), tensor(42.4908), tensor(46.1679)]
rr, day 190 acc_test tensor(43.3408) train_loss 3.291920820943429
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(43.0851), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.9605), tensor(42.4908), tensor(46.5328)]
rr, day 191 acc_test tensor(43.3959) train_loss 3.3120403616237013
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.9078), tensor(41.3043), tensor(44.5255), tensor(47.2826), tensor(45.9605), tensor(42.4908), tensor(46.3504)]
rr, day 192 acc_test tensor(43.3235) train_loss 3.2950973811365087
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.9078), tensor(41.3043), tensor(44.5255), tensor(47.4638), tensor(45.9605), tensor(42.4908), tensor(46.5328)]
rr, day 193 acc_test tensor(43.3599) train_loss 3.31837490236733
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(43.0851), tensor(41.3043), tensor(44.3431), tensor(47.2826), tensor(45.9605), tensor(42.4908), tensor(46.5328)]
rr, day 194 acc_test tensor(43.3591) train_loss 3.3029490398520176
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.9078), tensor(41.3043), tensor(44.7080), tensor(47.2826), tensor(46.1400), tensor(42.4908), tensor(46.5328)]
rr, day 195 acc_test tensor(43.3958) train_loss 3.3300211881962314
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.9078), tensor(41.3043), tensor(44.3431), tensor(47.2826), tensor(46.1400), tensor(42.4908), tensor(46.5328)]
rr, day 196 acc_test tensor(43.3593) train_loss 3.308862004870464
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(43.0851), tensor(41.3043), tensor(44.5255), tensor(47.2826), tensor(45.9605), tensor(42.4908), tensor(46.5328)]
rr, day 197 acc_test tensor(43.3773) train_loss 3.3313575750064808
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(43.0851), tensor(41.3043), tensor(44.5255), tensor(47.2826), tensor(46.1400), tensor(42.4908), tensor(46.5328)]
rr, day 198 acc_test tensor(43.3953) train_loss 3.3365487251810992
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.9078), tensor(41.1232), tensor(44.5255), tensor(47.2826), tensor(45.9605), tensor(42.4908), tensor(46.5328)]
rr, day 199 acc_test tensor(43.3415) train_loss 3.326346493396069
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.1408), tensor(43.0851), tensor(41.3043), tensor(44.3431), tensor(47.2826), tensor(46.1400), tensor(42.4908), tensor(46.5328)]
rr, day 200 acc_test tensor(43.3590) train_loss 3.350358548041125
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.1408), tensor(43.0851), tensor(41.3043), tensor(44.5255), tensor(47.2826), tensor(45.9605), tensor(42.4908), tensor(46.5328)]
rr, day 201 acc_test tensor(43.3593) train_loss 3.3629561393588676
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.1408), tensor(42.9078), tensor(41.3043), tensor(44.5255), tensor(47.2826), tensor(46.1400), tensor(42.6740), tensor(46.5328)]
rr, day 202 acc_test tensor(43.3778) train_loss 3.344836257835186
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.1408), tensor(43.0851), tensor(41.1232), tensor(44.5255), tensor(47.2826), tensor(45.9605), tensor(42.4908), tensor(46.5328)]
rr, day 203 acc_test tensor(43.3233) train_loss 3.3429809627542926
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(43.0851), tensor(40.9420), tensor(44.5255), tensor(47.4638), tensor(46.1400), tensor(42.6740), tensor(46.7153)]
rr, day 204 acc_test tensor(43.4137) train_loss 3.356065143645523
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.1408), tensor(42.9078), tensor(41.1232), tensor(44.5255), tensor(47.2826), tensor(46.1400), tensor(42.4908), tensor(46.7153)]
rr, day 205 acc_test tensor(43.3596) train_loss 3.3551371235896528
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.7305), tensor(41.1232), tensor(44.5255), tensor(47.2826), tensor(45.9605), tensor(42.6740), tensor(46.7153)]
rr, day 206 acc_test tensor(43.3425) train_loss 3.3907073091359132
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.7305), tensor(40.9420), tensor(44.5255), tensor(47.2826), tensor(45.9605), tensor(42.6740), tensor(46.7153)]
rr, day 207 acc_test tensor(43.3422) train_loss 3.3782493140399947
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.7305), tensor(41.1232), tensor(44.5255), tensor(47.2826), tensor(45.9605), tensor(42.6740), tensor(46.7153)]
rr, day 208 acc_test tensor(43.3425) train_loss 3.378866936800749
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(43.0851), tensor(41.1232), tensor(44.5255), tensor(47.2826), tensor(45.9605), tensor(42.6740), tensor(46.7153)]
rr, day 209 acc_test tensor(43.3780) train_loss 3.3922120751186524
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.7305), tensor(41.1232), tensor(44.5255), tensor(47.4638), tensor(45.9605), tensor(42.4908), tensor(46.7153)]
rr, day 210 acc_test tensor(43.3423) train_loss 3.38983108434953
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.9078), tensor(41.1232), tensor(44.5255), tensor(47.4638), tensor(45.9605), tensor(42.4908), tensor(46.7153)]
rr, day 211 acc_test tensor(43.3600) train_loss 3.3893099375021905
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.7305), tensor(41.1232), tensor(44.5255), tensor(47.4638), tensor(45.9605), tensor(42.4908), tensor(46.7153)]
rr, day 212 acc_test tensor(43.3423) train_loss 3.3929845570304953
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.9078), tensor(41.1232), tensor(44.5255), tensor(47.2826), tensor(45.9605), tensor(42.4908), tensor(46.5328)]
rr, day 213 acc_test tensor(43.3237) train_loss 3.401165790225991
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.7305), tensor(41.1232), tensor(44.5255), tensor(47.4638), tensor(45.9605), tensor(42.4908), tensor(46.5328)]
rr, day 214 acc_test tensor(43.3241) train_loss 3.4009446463464768
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.9078), tensor(40.9420), tensor(44.5255), tensor(47.4638), tensor(45.9605), tensor(42.3077), tensor(46.5328)]
rr, day 215 acc_test tensor(43.3054) train_loss 3.432627168007215
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.7305), tensor(40.9420), tensor(44.7080), tensor(47.2826), tensor(45.7810), tensor(42.4908), tensor(46.5328)]
rr, day 216 acc_test tensor(43.2881) train_loss 3.4205436621422813
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.7305), tensor(40.9420), tensor(44.5255), tensor(47.4638), tensor(45.9605), tensor(42.3077), tensor(46.5328)]
rr, day 217 acc_test tensor(43.2876) train_loss 3.4245530670356867
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.7305), tensor(40.9420), tensor(44.5255), tensor(47.4638), tensor(45.9605), tensor(42.4908), tensor(46.5328)]
rr, day 218 acc_test tensor(43.3059) train_loss 3.4188187978299687
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.6757), tensor(43.3213), tensor(42.9078), tensor(40.9420), tensor(44.5255), tensor(47.2826), tensor(45.9605), tensor(42.3077), tensor(46.5328)]
rr, day 219 acc_test tensor(43.2872) train_loss 3.428796021643826
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.3213), tensor(42.7305), tensor(40.9420), tensor(44.5255), tensor(47.2826), tensor(45.7810), tensor(42.3077), tensor(46.5328)]
rr, day 220 acc_test tensor(43.2338) train_loss 3.426903553344693
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.3213), tensor(42.7305), tensor(40.9420), tensor(44.7080), tensor(47.2826), tensor(45.9605), tensor(42.3077), tensor(46.5328)]
rr, day 221 acc_test tensor(43.2700) train_loss 3.445245207489992
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.3213), tensor(42.7305), tensor(40.9420), tensor(44.7080), tensor(47.2826), tensor(45.9605), tensor(42.3077), tensor(46.5328)]
rr, day 222 acc_test tensor(43.2700) train_loss 3.433168243066747
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.7305), tensor(40.9420), tensor(44.8905), tensor(47.2826), tensor(45.9605), tensor(42.3077), tensor(46.5328)]
rr, day 223 acc_test tensor(43.2702) train_loss 3.4457991226019207
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.9078), tensor(40.9420), tensor(44.7080), tensor(47.2826), tensor(45.9605), tensor(42.3077), tensor(46.5328)]
rr, day 224 acc_test tensor(43.2696) train_loss 3.4510680802158045
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.7305), tensor(40.9420), tensor(44.8905), tensor(47.2826), tensor(45.9605), tensor(42.3077), tensor(46.5328)]
rr, day 225 acc_test tensor(43.2702) train_loss 3.461287031599204
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.9078), tensor(40.9420), tensor(44.8905), tensor(47.2826), tensor(46.1400), tensor(42.3077), tensor(46.5328)]
rr, day 226 acc_test tensor(43.3058) train_loss 3.4866781205370647
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.3213), tensor(42.7305), tensor(40.9420), tensor(44.8905), tensor(47.2826), tensor(45.6014), tensor(42.3077), tensor(46.5328)]
rr, day 227 acc_test tensor(43.2523) train_loss 3.476401716625154
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.9078), tensor(40.9420), tensor(44.7080), tensor(47.2826), tensor(46.1400), tensor(42.3077), tensor(46.5328)]
rr, day 228 acc_test tensor(43.2876) train_loss 3.4664558397433107
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.7305), tensor(40.9420), tensor(45.0730), tensor(47.2826), tensor(45.9605), tensor(42.3077), tensor(46.5328)]
rr, day 229 acc_test tensor(43.2884) train_loss 3.4781742106785054
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.7305), tensor(40.9420), tensor(44.8905), tensor(47.2826), tensor(45.7810), tensor(42.3077), tensor(46.5328)]
rr, day 230 acc_test tensor(43.2522) train_loss 3.486506326676032
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.7305), tensor(40.9420), tensor(44.7080), tensor(47.2826), tensor(45.7810), tensor(42.3077), tensor(46.5328)]
rr, day 231 acc_test tensor(43.2340) train_loss 3.4666698522918393
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.7305), tensor(40.9420), tensor(44.8905), tensor(47.2826), tensor(45.9605), tensor(42.3077), tensor(46.5328)]
rr, day 232 acc_test tensor(43.2702) train_loss 3.4812548578606353
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.7305), tensor(40.9420), tensor(44.8905), tensor(47.4638), tensor(45.9605), tensor(42.3077), tensor(46.5328)]
rr, day 233 acc_test tensor(43.2883) train_loss 3.4825227698505903
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.5532), tensor(41.1232), tensor(44.8905), tensor(47.4638), tensor(45.9605), tensor(42.3077), tensor(46.5328)]
rr, day 234 acc_test tensor(43.2887) train_loss 3.4714682813085482
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.7305), tensor(41.1232), tensor(45.0730), tensor(47.4638), tensor(45.9605), tensor(42.3077), tensor(46.5328)]
rr, day 235 acc_test tensor(43.3246) train_loss 3.490427639440013
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.7305), tensor(41.1232), tensor(44.8905), tensor(47.4638), tensor(45.9605), tensor(42.3077), tensor(46.5328)]
rr, day 236 acc_test tensor(43.3064) train_loss 3.4945215159698755
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.7305), tensor(41.1232), tensor(44.8905), tensor(47.6449), tensor(45.7810), tensor(42.3077), tensor(46.3504)]
rr, day 237 acc_test tensor(43.2883) train_loss 3.5058721253147547
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.8559), tensor(43.1408), tensor(42.7305), tensor(41.1232), tensor(44.7080), tensor(47.6449), tensor(45.7810), tensor(42.3077), tensor(46.3504)]
rr, day 238 acc_test tensor(43.2881) train_loss 3.500591212709491
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.7305), tensor(41.1232), tensor(44.8905), tensor(47.6449), tensor(45.7810), tensor(42.3077), tensor(46.3504)]
rr, day 239 acc_test tensor(43.2883) train_loss 3.497688486408092
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.6757), tensor(43.1408), tensor(42.7305), tensor(41.1232), tensor(44.8905), tensor(47.6449), tensor(45.7810), tensor(42.3077), tensor(46.3504)]
rr, day 240 acc_test tensor(43.2883) train_loss 3.5103965703580644
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.8559), tensor(43.1408), tensor(42.5532), tensor(41.1232), tensor(44.8905), tensor(47.6449), tensor(45.9605), tensor(42.3077), tensor(46.3504)]
rr, day 241 acc_test tensor(43.3065) train_loss 3.532369595757039
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.8559), tensor(43.1408), tensor(42.7305), tensor(41.1232), tensor(44.8905), tensor(47.6449), tensor(45.9605), tensor(42.3077), tensor(46.3504)]
rr, day 242 acc_test tensor(43.3243) train_loss 3.5359618936681083
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.8559), tensor(43.1408), tensor(42.7305), tensor(41.1232), tensor(44.8905), tensor(47.6449), tensor(45.9605), tensor(42.3077), tensor(46.3504)]
rr, day 243 acc_test tensor(43.3243) train_loss 3.5499960315938637
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.8559), tensor(43.1408), tensor(42.5532), tensor(41.1232), tensor(44.8905), tensor(47.6449), tensor(45.9605), tensor(42.3077), tensor(46.3504)]
rr, day 244 acc_test tensor(43.3065) train_loss 3.548216544582481
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.8559), tensor(43.1408), tensor(42.7305), tensor(41.1232), tensor(44.8905), tensor(47.6449), tensor(45.7810), tensor(42.3077), tensor(46.3504)]
rr, day 245 acc_test tensor(43.3063) train_loss 3.5465957586180124
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.8559), tensor(43.1408), tensor(42.5532), tensor(41.3043), tensor(44.8905), tensor(47.6449), tensor(45.6014), tensor(42.3077), tensor(46.3504)]
rr, day 246 acc_test tensor(43.2888) train_loss 3.5376167853363993
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.1408), tensor(42.7305), tensor(41.1232), tensor(44.8905), tensor(47.6449), tensor(45.7810), tensor(42.3077), tensor(46.3504)]
rr, day 247 acc_test tensor(43.3243) train_loss 3.5472963540184814
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.1408), tensor(42.5532), tensor(41.1232), tensor(44.8905), tensor(47.6449), tensor(45.7810), tensor(42.3077), tensor(46.3504)]
rr, day 248 acc_test tensor(43.3066) train_loss 3.544865870397506
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.1408), tensor(42.5532), tensor(41.3043), tensor(44.8905), tensor(47.6449), tensor(45.7810), tensor(42.3077), tensor(46.3504)]
rr, day 249 acc_test tensor(43.3247) train_loss 3.5506384025063027
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.1408), tensor(42.5532), tensor(41.1232), tensor(44.8905), tensor(47.6449), tensor(45.6014), tensor(42.3077), tensor(46.3504)]
rr, day 250 acc_test tensor(43.2887) train_loss 3.5674675995296408
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.1408), tensor(42.5532), tensor(41.3043), tensor(44.8905), tensor(47.6449), tensor(45.6014), tensor(42.3077), tensor(46.3504)]
rr, day 251 acc_test tensor(43.3068) train_loss 3.577098378435193
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.1408), tensor(42.5532), tensor(41.3043), tensor(45.0730), tensor(47.6449), tensor(45.9605), tensor(42.3077), tensor(46.3504)]
rr, day 252 acc_test tensor(43.3609) train_loss 3.566144607045997
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.1408), tensor(42.3759), tensor(41.1232), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(42.3077), tensor(46.3504)]
rr, day 253 acc_test tensor(43.2528) train_loss 3.5614007128114777
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.1408), tensor(42.5532), tensor(41.1232), tensor(44.8905), tensor(47.4638), tensor(45.7810), tensor(42.3077), tensor(46.3504)]
rr, day 254 acc_test tensor(43.2885) train_loss 3.5738112420126082
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.1408), tensor(42.1986), tensor(41.3043), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(42.1245), tensor(46.3504)]
rr, day 255 acc_test tensor(43.2349) train_loss 3.570567629834579
test_semi_fb acc_test_lst [tensor(43.2384), tensor(35.8559), tensor(43.1408), tensor(42.5532), tensor(41.1232), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(42.3077), tensor(46.3504)]
rr, day 256 acc_test tensor(43.2525) train_loss 3.5643378347655186
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.1408), tensor(42.5532), tensor(41.3043), tensor(44.8905), tensor(47.4638), tensor(45.7810), tensor(42.3077), tensor(46.3504)]
rr, day 257 acc_test tensor(43.3066) train_loss 3.5726516171837033
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.1408), tensor(42.3759), tensor(41.3043), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(42.1245), tensor(46.3504)]
rr, day 258 acc_test tensor(43.2526) train_loss 3.5895671309788035
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.1408), tensor(42.3759), tensor(41.3043), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(42.3077), tensor(46.3504)]
rr, day 259 acc_test tensor(43.2887) train_loss 3.587222560928032
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.1408), tensor(42.5532), tensor(41.1232), tensor(45.0730), tensor(47.4638), tensor(45.7810), tensor(42.3077), tensor(46.3504)]
rr, day 260 acc_test tensor(43.3067) train_loss 3.583918989628939
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.1408), tensor(42.1986), tensor(41.3043), tensor(44.8905), tensor(47.4638), tensor(45.4219), tensor(41.9414), tensor(46.5328)]
rr, day 261 acc_test tensor(43.2347) train_loss 3.600901831081168
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.3759), tensor(41.3043), tensor(44.8905), tensor(47.4638), tensor(45.4219), tensor(42.1245), tensor(46.5328)]
rr, day 262 acc_test tensor(43.2887) train_loss 3.599377444816455
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.3759), tensor(41.3043), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(42.1245), tensor(46.5328)]
rr, day 263 acc_test tensor(43.3067) train_loss 3.6013741790788756
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.1986), tensor(41.3043), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(42.1245), tensor(46.5328)]
rr, day 264 acc_test tensor(43.2890) train_loss 3.5950949684253377
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.7305), tensor(41.3043), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(42.1245), tensor(46.5328)]
rr, day 265 acc_test tensor(43.3422) train_loss 3.6208303098499517
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.3759), tensor(41.3043), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(41.9414), tensor(46.5328)]
rr, day 266 acc_test tensor(43.2884) train_loss 3.6173064601347718
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(41.9414), tensor(46.5328)]
rr, day 267 acc_test tensor(43.3061) train_loss 3.6234720394874014
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(42.1245), tensor(46.5328)]
rr, day 268 acc_test tensor(43.2885) train_loss 3.6069387676523172
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.8905), tensor(47.4638), tensor(45.6014), tensor(41.9414), tensor(46.5328)]
rr, day 269 acc_test tensor(43.3061) train_loss 3.6266938215172355
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.9414), tensor(46.5328)]
rr, day 270 acc_test tensor(43.2879) train_loss 3.6219749805465273
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(42.1245), tensor(46.5328)]
rr, day 271 acc_test tensor(43.3062) train_loss 3.6214028352436882
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.9414), tensor(46.3504)]
rr, day 272 acc_test tensor(43.2696) train_loss 3.630829592647882
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(42.1245), tensor(46.5328)]
rr, day 273 acc_test tensor(43.3062) train_loss 3.6434238167235837
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.9414), tensor(46.3504)]
rr, day 274 acc_test tensor(43.2696) train_loss 3.655012465999775
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.9414), tensor(46.5328)]
rr, day 275 acc_test tensor(43.2879) train_loss 3.632766460576375
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.9414), tensor(46.3504)]
rr, day 276 acc_test tensor(43.2696) train_loss 3.64431193871552
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.9414), tensor(46.3504)]
rr, day 277 acc_test tensor(43.2519) train_loss 3.6462671430483016
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.9414), tensor(46.3504)]
rr, day 278 acc_test tensor(43.2696) train_loss 3.6640654921276172
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 279 acc_test tensor(43.2513) train_loss 3.6565175354853983
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 280 acc_test tensor(43.2513) train_loss 3.6340222420641406
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 281 acc_test tensor(43.2513) train_loss 3.6679364370494523
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 282 acc_test tensor(43.2513) train_loss 3.683752413197545
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 283 acc_test tensor(43.2513) train_loss 3.6767953043055814
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 284 acc_test tensor(43.2513) train_loss 3.680746497781619
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 285 acc_test tensor(43.2336) train_loss 3.685555138634939
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.3213), tensor(42.7305), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 286 acc_test tensor(43.2512) train_loss 3.6873772969773766
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 287 acc_test tensor(43.2335) train_loss 3.6815874671993187
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 288 acc_test tensor(43.2513) train_loss 3.6770390307145533
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 289 acc_test tensor(43.2335) train_loss 3.7066593415424642
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.3213), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 290 acc_test tensor(43.2335) train_loss 3.677678795306516
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.3213), tensor(42.7305), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 291 acc_test tensor(43.2512) train_loss 3.6978470247415522
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.5018), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 292 acc_test tensor(43.2694) train_loss 3.686032384930056
test_semi_fb acc_test_lst [tensor(43.2384), tensor(36.0360), tensor(43.5018), tensor(42.5532), tensor(41.1232), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 293 acc_test tensor(43.2335) train_loss 3.7128499909286705
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.3213), tensor(42.7305), tensor(41.1232), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 294 acc_test tensor(43.2509) train_loss 3.696522024783623
test_semi_fb acc_test_lst [tensor(43.4164), tensor(36.0360), tensor(43.5018), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 295 acc_test tensor(43.2694) train_loss 3.6988595617929807
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.8559), tensor(43.5018), tensor(42.5532), tensor(41.1232), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 296 acc_test tensor(43.2332) train_loss 3.7025217049573973
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.8559), tensor(43.5018), tensor(42.7305), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.5328)]
rr, day 297 acc_test tensor(43.2873) train_loss 3.7327708342101262
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.8559), tensor(43.3213), tensor(42.7305), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.5328)]
rr, day 298 acc_test tensor(43.2693) train_loss 3.730313306270409
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.8559), tensor(43.5018), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 299 acc_test tensor(43.2336) train_loss 3.7227819333791
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.8559), tensor(43.5018), tensor(42.7305), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.5328)]
rr, day 300 acc_test tensor(43.3051) train_loss 3.7256225180442666
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.8559), tensor(43.5018), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.5328)]
rr, day 301 acc_test tensor(43.2519) train_loss 3.7456771929843597
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.8559), tensor(43.5018), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.3504)]
rr, day 302 acc_test tensor(43.2514) train_loss 3.74370556041348
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.8559), tensor(43.6823), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 303 acc_test tensor(43.3059) train_loss 3.7420482425899513
test_semi_fb acc_test_lst [tensor(43.4164), tensor(35.8559), tensor(43.6823), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.5328)]
rr, day 304 acc_test tensor(43.2699) train_loss 3.738703292407268
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.8559), tensor(43.5018), tensor(42.5532), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 305 acc_test tensor(43.3056) train_loss 3.7252796015537437
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.8559), tensor(43.5018), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.5328)]
rr, day 306 acc_test tensor(43.2874) train_loss 3.7479807344150635
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.8559), tensor(43.6823), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.5328)]
rr, day 307 acc_test tensor(43.2877) train_loss 3.7559312511987537
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.5018), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 308 acc_test tensor(43.2699) train_loss 3.742176838127554
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.5018), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 309 acc_test tensor(43.2699) train_loss 3.7488451190934198
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.8559), tensor(43.3213), tensor(42.3759), tensor(41.3043), tensor(44.5255), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 310 acc_test tensor(43.2516) train_loss 3.7719192579143344
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.5018), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 311 acc_test tensor(43.2699) train_loss 3.760072027488245
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.6823), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 312 acc_test tensor(43.2879) train_loss 3.7657871758464223
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.5018), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 313 acc_test tensor(43.2699) train_loss 3.7719583511787302
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 314 acc_test tensor(43.2518) train_loss 3.776100809931712
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.1408), tensor(42.3759), tensor(41.3043), tensor(44.5255), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 315 acc_test tensor(43.2155) train_loss 3.775532604321533
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.5018), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 316 acc_test tensor(43.2699) train_loss 3.7742060371575157
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.5018), tensor(42.3759), tensor(41.3043), tensor(44.5255), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 317 acc_test tensor(43.2516) train_loss 3.790856470501966
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.3759), tensor(41.3043), tensor(44.5255), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 318 acc_test tensor(43.2336) train_loss 3.7739925781475945
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.1408), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 319 acc_test tensor(43.2338) train_loss 3.7755134618332664
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.6757), tensor(43.3213), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.6449), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 320 acc_test tensor(43.2877) train_loss 3.7864529529739444
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.5018), tensor(42.3759), tensor(41.3043), tensor(44.7080), tensor(47.4638), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 321 acc_test tensor(43.2699) train_loss 3.795391766396765
test_semi_fb acc_test_lst [tensor(43.7722), tensor(35.6757), tensor(43.3213), tensor(42.3759), tensor(41.3043), tensor(44.5255), tensor(47.6449), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 322 acc_test tensor(43.2695) train_loss 3.7954121472782787
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.3759), tensor(41.1232), tensor(44.5255), tensor(47.6449), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 323 acc_test tensor(43.2336) train_loss 3.788698014010517
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.3759), tensor(41.3043), tensor(44.5255), tensor(47.6449), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 324 acc_test tensor(43.2517) train_loss 3.801764814104513
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.1408), tensor(42.1986), tensor(40.9420), tensor(44.5255), tensor(47.6449), tensor(45.4219), tensor(41.7582), tensor(46.7153)]
rr, day 325 acc_test tensor(43.1617) train_loss 3.789163232403345
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.1408), tensor(42.1986), tensor(41.3043), tensor(44.5255), tensor(47.6449), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 326 acc_test tensor(43.2159) train_loss 3.8183084594142196
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.1986), tensor(41.3043), tensor(44.5255), tensor(47.6449), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 327 acc_test tensor(43.2340) train_loss 3.8047196349827703
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.1408), tensor(42.1986), tensor(40.9420), tensor(44.5255), tensor(47.6449), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 328 acc_test tensor(43.1797) train_loss 3.7950943187419908
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.1408), tensor(42.1986), tensor(40.9420), tensor(44.5255), tensor(47.6449), tensor(45.6014), tensor(41.7582), tensor(46.5328)]
rr, day 329 acc_test tensor(43.1614) train_loss 3.811748632348494
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.1986), tensor(40.9420), tensor(44.5255), tensor(47.6449), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 330 acc_test tensor(43.1977) train_loss 3.815924603938166
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.1986), tensor(40.9420), tensor(44.7080), tensor(47.6449), tensor(45.6014), tensor(41.7582), tensor(46.8978)]
rr, day 331 acc_test tensor(43.2342) train_loss 3.812338255134979
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.1986), tensor(40.9420), tensor(44.5255), tensor(47.6449), tensor(45.6014), tensor(41.7582), tensor(46.7153)]
rr, day 332 acc_test tensor(43.1977) train_loss 3.8031176283929606
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.1986), tensor(41.1232), tensor(44.5255), tensor(47.6449), tensor(45.6014), tensor(41.7582), tensor(46.5328)]
rr, day 333 acc_test tensor(43.1976) train_loss 3.8228682373599323
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.1986), tensor(40.9420), tensor(44.5255), tensor(47.6449), tensor(45.4219), tensor(41.7582), tensor(46.8978)]
rr, day 334 acc_test tensor(43.1980) train_loss 3.825220111256144
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.1986), tensor(40.9420), tensor(44.5255), tensor(47.6449), tensor(45.6014), tensor(41.7582), tensor(46.8978)]
rr, day 335 acc_test tensor(43.2160) train_loss 3.8212334187426125
test_semi_fb acc_test_lst [tensor(43.5943), tensor(35.6757), tensor(43.3213), tensor(42.1986), tensor(40.9420), tensor(44.5255), tensor(47.6449), tensor(45.4219), tensor(41.7582), tensor(46.7153)]
rr, day 336 acc_test tensor(43.1798) train_loss 3.805040315973329"""

fb_s = """test_semi_fb acc_test_lst [tensor(26.6904), tensor(27.5676), tensor(36.2816), tensor(30.4965), tensor(25.), tensor(22.0803), tensor(25.1812), tensor(26.0323), tensor(20.5128), tensor(19.5255)]
fb, day 0 acc_test tensor(25.9368) train_loss 1.9550167866511492
test_semi_fb acc_test_lst [tensor(29.3594), tensor(30.9910), tensor(39.7112), tensor(34.3972), tensor(28.8043), tensor(28.8321), tensor(27.3551), tensor(30.8797), tensor(25.6410), tensor(25.9124)]
fb, day 1 acc_test tensor(30.1883) train_loss 1.8673907011206423
test_semi_fb acc_test_lst [tensor(29.3594), tensor(33.1532), tensor(42.2383), tensor(35.2837), tensor(32.4275), tensor(30.8394), tensor(30.2536), tensor(35.1885), tensor(28.7546), tensor(27.5547)]
fb, day 2 acc_test tensor(32.5053) train_loss 1.811032896501418
test_semi_fb acc_test_lst [tensor(32.0285), tensor(34.9550), tensor(44.2238), tensor(36.5248), tensor(32.4275), tensor(32.8467), tensor(32.6087), tensor(36.8043), tensor(30.2198), tensor(28.8321)]
fb, day 3 acc_test tensor(34.1471) train_loss 1.7726796752873684
test_semi_fb acc_test_lst [tensor(32.2064), tensor(35.3153), tensor(46.5704), tensor(37.0567), tensor(32.2464), tensor(34.6715), tensor(33.6957), tensor(38.2406), tensor(30.9524), tensor(30.2920)]
fb, day 4 acc_test tensor(35.1247) train_loss 1.7443929427539908
test_semi_fb acc_test_lst [tensor(32.3843), tensor(36.5766), tensor(47.2924), tensor(38.6525), tensor(32.6087), tensor(34.8540), tensor(35.1449), tensor(38.7792), tensor(31.5018), tensor(30.6569)]
fb, day 5 acc_test tensor(35.8451) train_loss 1.721991908255481
test_semi_fb acc_test_lst [tensor(33.8078), tensor(36.2162), tensor(47.8339), tensor(39.3617), tensor(34.0580), tensor(35.0365), tensor(37.1377), tensor(39.3178), tensor(32.6007), tensor(32.2993)]
fb, day 6 acc_test tensor(36.7670) train_loss 1.7032469431907211
test_semi_fb acc_test_lst [tensor(33.9858), tensor(36.2162), tensor(49.2780), tensor(39.3617), tensor(34.7826), tensor(36.3139), tensor(37.3188), tensor(39.6768), tensor(33.5165), tensor(32.8467)]
fb, day 7 acc_test tensor(37.3297) train_loss 1.687752274205585
test_semi_fb acc_test_lst [tensor(33.9858), tensor(36.2162), tensor(49.4585), tensor(39.7163), tensor(35.5072), tensor(36.8613), tensor(38.4058), tensor(40.0359), tensor(33.8828), tensor(32.8467)]
fb, day 8 acc_test tensor(37.6917) train_loss 1.6738593395804602
test_semi_fb acc_test_lst [tensor(34.5196), tensor(36.7568), tensor(49.2780), tensor(39.7163), tensor(35.8696), tensor(37.2263), tensor(38.4058), tensor(40.3950), tensor(34.4322), tensor(33.0292)]
fb, day 9 acc_test tensor(37.9629) train_loss 1.6618953334224693
test_semi_fb acc_test_lst [tensor(34.1637), tensor(37.1171), tensor(49.2780), tensor(40.6028), tensor(36.0507), tensor(37.5912), tensor(38.9493), tensor(40.9336), tensor(34.6154), tensor(34.1241)]
fb, day 10 acc_test tensor(38.3426) train_loss 1.6504273748783647
test_semi_fb acc_test_lst [tensor(34.5196), tensor(36.3964), tensor(49.6390), tensor(40.4255), tensor(35.8696), tensor(38.6861), tensor(39.6739), tensor(41.8312), tensor(35.5311), tensor(34.4891)]
fb, day 11 acc_test tensor(38.7062) train_loss 1.6401643719415937
test_semi_fb acc_test_lst [tensor(35.2313), tensor(36.7568), tensor(50.1805), tensor(40.7801), tensor(37.1377), tensor(38.5037), tensor(40.0362), tensor(42.5494), tensor(35.5311), tensor(34.6715)]
fb, day 12 acc_test tensor(39.1378) train_loss 1.6320563455618653
test_semi_fb acc_test_lst [tensor(35.9431), tensor(36.2162), tensor(50.3610), tensor(41.8440), tensor(36.7754), tensor(39.7810), tensor(40.0362), tensor(42.1903), tensor(35.7143), tensor(34.4891)]
fb, day 13 acc_test tensor(39.3351) train_loss 1.6242873731258323
test_semi_fb acc_test_lst [tensor(35.7651), tensor(36.5766), tensor(51.0830), tensor(41.8440), tensor(36.4130), tensor(39.4161), tensor(40.2174), tensor(42.0108), tensor(36.0806), tensor(35.5839)]
fb, day 14 acc_test tensor(39.4991) train_loss 1.617845392787177
test_semi_fb acc_test_lst [tensor(36.2989), tensor(36.5766), tensor(51.0830), tensor(41.8440), tensor(36.7754), tensor(39.0511), tensor(40.3986), tensor(42.0108), tensor(35.3480), tensor(35.4015)]
fb, day 15 acc_test tensor(39.4788) train_loss 1.6116570744583214
test_semi_fb acc_test_lst [tensor(36.8327), tensor(36.7568), tensor(51.0830), tensor(42.7305), tensor(36.4130), tensor(38.8686), tensor(40.9420), tensor(42.1903), tensor(35.5311), tensor(34.6715)]
fb, day 16 acc_test tensor(39.6020) train_loss 1.6064521000762095
test_semi_fb acc_test_lst [tensor(37.0107), tensor(36.0360), tensor(51.0830), tensor(42.5532), tensor(36.4130), tensor(38.8686), tensor(40.9420), tensor(42.3698), tensor(36.4469), tensor(35.2190)]
fb, day 17 acc_test tensor(39.6942) train_loss 1.6023382872056007
test_semi_fb acc_test_lst [tensor(37.5445), tensor(36.7568), tensor(51.4440), tensor(42.7305), tensor(37.1377), tensor(39.2336), tensor(40.9420), tensor(42.3698), tensor(36.6300), tensor(35.4015)]
fb, day 18 acc_test tensor(40.0190) train_loss 1.599311174882017
test_semi_fb acc_test_lst [tensor(37.5445), tensor(36.5766), tensor(51.4440), tensor(42.5532), tensor(36.9565), tensor(39.0511), tensor(41.1232), tensor(42.5494), tensor(37.1795), tensor(36.1314)]
fb, day 19 acc_test tensor(40.1109) train_loss 1.5960153835344395
test_semi_fb acc_test_lst [tensor(37.7224), tensor(36.7568), tensor(51.4440), tensor(42.7305), tensor(36.9565), tensor(39.5985), tensor(41.4855), tensor(42.9084), tensor(37.3626), tensor(36.1314)]
fb, day 20 acc_test tensor(40.3097) train_loss 1.59425389052133
test_semi_fb acc_test_lst [tensor(37.5445), tensor(36.7568), tensor(51.6245), tensor(42.7305), tensor(37.3188), tensor(39.7810), tensor(41.8478), tensor(42.9084), tensor(37.7289), tensor(36.8613)]
fb, day 21 acc_test tensor(40.5103) train_loss 1.592757543008226
test_semi_fb acc_test_lst [tensor(37.3665), tensor(37.4775), tensor(52.7076), tensor(43.2624), tensor(36.9565), tensor(40.5109), tensor(41.6667), tensor(43.0880), tensor(38.0952), tensor(37.0438)]
fb, day 22 acc_test tensor(40.8175) train_loss 1.5922529346219614
test_semi_fb acc_test_lst [tensor(37.7224), tensor(37.2973), tensor(51.9856), tensor(43.4397), tensor(36.2319), tensor(40.3285), tensor(41.3043), tensor(43.0880), tensor(38.0952), tensor(37.0438)]
fb, day 23 acc_test tensor(40.6537) train_loss 1.5922287534210298
test_semi_fb acc_test_lst [tensor(37.5445), tensor(37.2973), tensor(52.1661), tensor(43.4397), tensor(36.4130), tensor(39.5985), tensor(41.6667), tensor(43.2675), tensor(38.2784), tensor(36.6788)]
fb, day 24 acc_test tensor(40.6351) train_loss 1.592270066299491
test_semi_fb acc_test_lst [tensor(37.7224), tensor(37.2973), tensor(52.3466), tensor(43.4397), tensor(36.2319), tensor(40.3285), tensor(41.8478), tensor(43.4470), tensor(38.0952), tensor(37.0438)]
fb, day 25 acc_test tensor(40.7800) train_loss 1.5930388827464228
test_semi_fb acc_test_lst [tensor(37.5445), tensor(37.4775), tensor(52.5271), tensor(43.7943), tensor(36.7754), tensor(39.9635), tensor(41.4855), tensor(44.1652), tensor(38.2784), tensor(36.6788)]
fb, day 26 acc_test tensor(40.8690) train_loss 1.594065015949397
test_semi_fb acc_test_lst [tensor(37.5445), tensor(37.2973), tensor(52.3466), tensor(43.6170), tensor(36.9565), tensor(39.5985), tensor(41.6667), tensor(44.3447), tensor(38.4615), tensor(36.6788)]
fb, day 27 acc_test tensor(40.8512) train_loss 1.5965168204099758
test_semi_fb acc_test_lst [tensor(37.9004), tensor(37.6577), tensor(52.3466), tensor(43.7943), tensor(36.5942), tensor(39.7810), tensor(41.6667), tensor(43.9856), tensor(38.6447), tensor(37.0438)]
fb, day 28 acc_test tensor(40.9415) train_loss 1.5984456182943405
test_semi_fb acc_test_lst [tensor(38.0783), tensor(37.2973), tensor(52.1661), tensor(44.1489), tensor(37.1377), tensor(38.8686), tensor(42.0290), tensor(44.1652), tensor(38.6447), tensor(37.2263)]
fb, day 29 acc_test tensor(40.9762) train_loss 1.6023588668173323
test_semi_fb acc_test_lst [tensor(38.0783), tensor(36.9369), tensor(51.9856), tensor(43.9716), tensor(37.1377), tensor(39.2336), tensor(42.3913), tensor(43.9856), tensor(39.0110), tensor(37.2263)]
fb, day 30 acc_test tensor(40.9958) train_loss 1.6068016179099986
test_semi_fb acc_test_lst [tensor(37.9004), tensor(36.5766), tensor(51.2635), tensor(44.5035), tensor(38.2246), tensor(39.0511), tensor(41.4855), tensor(43.9856), tensor(39.0110), tensor(37.5912)]
fb, day 31 acc_test tensor(40.9593) train_loss 1.6110535309978735
test_semi_fb acc_test_lst [tensor(38.2562), tensor(37.1171), tensor(51.4440), tensor(44.1489), tensor(38.7681), tensor(39.0511), tensor(42.0290), tensor(43.9856), tensor(39.1941), tensor(37.0438)]
fb, day 32 acc_test tensor(41.1038) train_loss 1.6167155866926473
test_semi_fb acc_test_lst [tensor(38.2562), tensor(37.2973), tensor(51.8051), tensor(44.5035), tensor(38.7681), tensor(39.7810), tensor(42.5725), tensor(43.6266), tensor(39.0110), tensor(37.9562)]
fb, day 33 acc_test tensor(41.3577) train_loss 1.6216232495693115
test_semi_fb acc_test_lst [tensor(37.7224), tensor(37.2973), tensor(52.3466), tensor(45.0355), tensor(38.2246), tensor(39.7810), tensor(42.3913), tensor(43.2675), tensor(38.4615), tensor(37.4088)]
fb, day 34 acc_test tensor(41.1937) train_loss 1.6275189930065614
test_semi_fb acc_test_lst [tensor(37.9004), tensor(37.6577), tensor(51.2635), tensor(44.6809), tensor(39.3116), tensor(40.1460), tensor(42.0290), tensor(43.9856), tensor(37.9121), tensor(38.8686)]
fb, day 35 acc_test tensor(41.3755) train_loss 1.6326732278080758
test_semi_fb acc_test_lst [tensor(38.0783), tensor(37.6577), tensor(51.4440), tensor(44.8582), tensor(38.9493), tensor(39.7810), tensor(42.3913), tensor(44.3447), tensor(38.2784), tensor(38.3212)]
fb, day 36 acc_test tensor(41.4104) train_loss 1.6412857015518387
test_semi_fb acc_test_lst [tensor(37.5445), tensor(37.8378), tensor(51.2635), tensor(45.0355), tensor(39.3116), tensor(39.5985), tensor(42.5725), tensor(44.1652), tensor(38.6447), tensor(38.6861)]
fb, day 37 acc_test tensor(41.4660) train_loss 1.6471967167755472
test_semi_fb acc_test_lst [tensor(37.9004), tensor(38.0180), tensor(51.0830), tensor(44.8582), tensor(39.8551), tensor(39.9635), tensor(41.8478), tensor(43.9856), tensor(38.8278), tensor(39.0511)]
fb, day 38 acc_test tensor(41.5391) train_loss 1.6534480792197335
test_semi_fb acc_test_lst [tensor(37.9004), tensor(38.3784), tensor(50.5415), tensor(44.8582), tensor(39.6739), tensor(39.9635), tensor(42.2101), tensor(44.7038), tensor(39.3773), tensor(39.2336)]
fb, day 39 acc_test tensor(41.6841) train_loss 1.6652811974482795
test_semi_fb acc_test_lst [tensor(38.2562), tensor(38.1982), tensor(51.2635), tensor(45.0355), tensor(39.8551), tensor(39.5985), tensor(42.2101), tensor(45.4219), tensor(39.0110), tensor(39.5985)]
fb, day 40 acc_test tensor(41.8449) train_loss 1.6730336655177132
test_semi_fb acc_test_lst [tensor(38.7900), tensor(37.4775), tensor(51.6245), tensor(44.8582), tensor(39.6739), tensor(39.9635), tensor(41.8478), tensor(44.8833), tensor(39.5604), tensor(39.7810)]
fb, day 41 acc_test tensor(41.8460) train_loss 1.6805690780379319
test_semi_fb acc_test_lst [tensor(38.6121), tensor(36.9369), tensor(50.9025), tensor(45.2128), tensor(40.3986), tensor(39.7810), tensor(42.0290), tensor(45.0628), tensor(39.5604), tensor(39.7810)]
fb, day 42 acc_test tensor(41.8277) train_loss 1.690095208919801
test_semi_fb acc_test_lst [tensor(38.9680), tensor(36.7568), tensor(50.3610), tensor(45.2128), tensor(40.7609), tensor(39.2336), tensor(42.2101), tensor(45.4219), tensor(39.5604), tensor(40.3285)]
fb, day 43 acc_test tensor(41.8814) train_loss 1.7001189087123927
test_semi_fb acc_test_lst [tensor(39.1459), tensor(36.3964), tensor(50.9025), tensor(45.9220), tensor(40.7609), tensor(38.5037), tensor(42.0290), tensor(45.4219), tensor(39.5604), tensor(40.3285)]
fb, day 44 acc_test tensor(41.8971) train_loss 1.7092510942783183
test_semi_fb acc_test_lst [tensor(38.9680), tensor(36.0360), tensor(50.7220), tensor(45.0355), tensor(40.2174), tensor(38.8686), tensor(42.2101), tensor(45.4219), tensor(39.5604), tensor(40.5109)]
fb, day 45 acc_test tensor(41.7551) train_loss 1.7199904387902982
test_semi_fb acc_test_lst [tensor(39.1459), tensor(36.3964), tensor(51.0830), tensor(45.2128), tensor(40.2174), tensor(38.8686), tensor(42.0290), tensor(45.2424), tensor(39.1941), tensor(40.5109)]
fb, day 46 acc_test tensor(41.7901) train_loss 1.7301903347680982
test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.8559), tensor(50.7220), tensor(44.6809), tensor(40.5797), tensor(39.4161), tensor(41.6667), tensor(45.0628), tensor(39.0110), tensor(41.4234)]
fb, day 47 acc_test tensor(41.7742) train_loss 1.7444034899631005
test_semi_fb acc_test_lst [tensor(38.6121), tensor(36.0360), tensor(50.3610), tensor(44.8582), tensor(40.5797), tensor(39.5985), tensor(41.1232), tensor(44.7038), tensor(39.0110), tensor(41.7883)]
fb, day 48 acc_test tensor(41.6672) train_loss 1.7557379408898035
test_semi_fb acc_test_lst [tensor(38.4342), tensor(35.6757), tensor(50.9025), tensor(45.2128), tensor(40.2174), tensor(39.2336), tensor(41.3043), tensor(45.0628), tensor(39.0110), tensor(41.0584)]
fb, day 49 acc_test tensor(41.6113) train_loss 1.7691207102187585
test_semi_fb acc_test_lst [tensor(38.4342), tensor(35.4955), tensor(50.9025), tensor(45.7447), tensor(40.5797), tensor(38.8686), tensor(41.4855), tensor(45.0628), tensor(38.8278), tensor(41.6058)]
fb, day 50 acc_test tensor(41.7007) train_loss 1.7803334264026573
test_semi_fb acc_test_lst [tensor(38.9680), tensor(34.9550), tensor(50.9025), tensor(45.7447), tensor(40.2174), tensor(39.4161), tensor(41.3043), tensor(44.8833), tensor(39.0110), tensor(41.7883)]
fb, day 51 acc_test tensor(41.7191) train_loss 1.7925755438140873
test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.8559), tensor(50.3610), tensor(45.3901), tensor(40.5797), tensor(39.0511), tensor(40.9420), tensor(44.5242), tensor(39.3773), tensor(41.4234)]
fb, day 52 acc_test tensor(41.6828) train_loss 1.8077002983359103
test_semi_fb acc_test_lst [tensor(39.1459), tensor(35.8559), tensor(50.9025), tensor(45.7447), tensor(40.2174), tensor(38.6861), tensor(40.7609), tensor(45.0628), tensor(38.6447), tensor(42.3358)]
fb, day 53 acc_test tensor(41.7357) train_loss 1.8198601689905194
test_semi_fb acc_test_lst [tensor(39.1459), tensor(35.3153), tensor(50.9025), tensor(45.7447), tensor(40.3986), tensor(38.8686), tensor(40.9420), tensor(44.8833), tensor(38.8278), tensor(42.5182)]
fb, day 54 acc_test tensor(41.7547) train_loss 1.8362484666842858
test_semi_fb acc_test_lst [tensor(38.4342), tensor(35.6757), tensor(50.9025), tensor(45.9220), tensor(40.3986), tensor(39.0511), tensor(40.7609), tensor(45.0628), tensor(38.8278), tensor(42.1533)]
fb, day 55 acc_test tensor(41.7189) train_loss 1.851322822775168
test_semi_fb acc_test_lst [tensor(39.6797), tensor(35.6757), tensor(50.5415), tensor(45.3901), tensor(40.2174), tensor(39.5985), tensor(40.5797), tensor(44.5242), tensor(39.1941), tensor(41.4234)]
fb, day 56 acc_test tensor(41.6824) train_loss 1.8628927543638196
test_semi_fb acc_test_lst [tensor(39.1459), tensor(35.1351), tensor(50.5415), tensor(45.2128), tensor(40.2174), tensor(39.0511), tensor(40.7609), tensor(44.8833), tensor(37.9121), tensor(42.5182)]
fb, day 57 acc_test tensor(41.5378) train_loss 1.8756993936056634
test_semi_fb acc_test_lst [tensor(38.4342), tensor(35.6757), tensor(50.1805), tensor(45.7447), tensor(40.3986), tensor(39.5985), tensor(40.5797), tensor(45.2424), tensor(38.4615), tensor(41.7883)]
fb, day 58 acc_test tensor(41.6104) train_loss 1.8892664207196916
test_semi_fb acc_test_lst [tensor(38.9680), tensor(35.1351), tensor(50.7220), tensor(45.2128), tensor(40.2174), tensor(39.5985), tensor(40.9420), tensor(45.0628), tensor(38.4615), tensor(42.1533)]
fb, day 59 acc_test tensor(41.6474) train_loss 1.9074470572134614
test_semi_fb acc_test_lst [tensor(39.5018), tensor(36.0360), tensor(50.5415), tensor(45.5674), tensor(40.2174), tensor(39.2336), tensor(39.6739), tensor(44.8833), tensor(38.2784), tensor(41.9708)]
fb, day 60 acc_test tensor(41.5904) train_loss 1.9207968901438648
test_semi_fb acc_test_lst [tensor(39.8577), tensor(35.4955), tensor(50.3610), tensor(45.7447), tensor(40.2174), tensor(40.1460), tensor(41.3043), tensor(45.2424), tensor(38.2784), tensor(42.3358)]
fb, day 61 acc_test tensor(41.8983) train_loss 1.93718712740316
test_semi_fb acc_test_lst [tensor(39.1459), tensor(34.2342), tensor(50.1805), tensor(44.8582), tensor(40.2174), tensor(39.2336), tensor(40.2174), tensor(44.5242), tensor(39.0110), tensor(42.5182)]
fb, day 62 acc_test tensor(41.4141) train_loss 1.9542036663457596
test_semi_fb acc_test_lst [tensor(39.1459), tensor(34.9550), tensor(49.8195), tensor(45.3901), tensor(39.6739), tensor(39.4161), tensor(40.0362), tensor(45.0628), tensor(39.1941), tensor(41.7883)]
fb, day 63 acc_test tensor(41.4482) train_loss 1.9632136236792732
test_semi_fb acc_test_lst [tensor(38.9680), tensor(34.9550), tensor(50.), tensor(45.7447), tensor(39.8551), tensor(39.4161), tensor(40.3986), tensor(44.7038), tensor(39.0110), tensor(41.7883)]
fb, day 64 acc_test tensor(41.4840) train_loss 1.9798288484598967
test_semi_fb acc_test_lst [tensor(38.6121), tensor(34.9550), tensor(50.), tensor(45.5674), tensor(39.4928), tensor(39.5985), tensor(39.8551), tensor(45.4219), tensor(39.1941), tensor(42.1533)]
fb, day 65 acc_test tensor(41.4850) train_loss 2.0002046653987122
test_semi_fb acc_test_lst [tensor(39.1459), tensor(34.7748), tensor(49.4585), tensor(45.5674), tensor(39.4928), tensor(39.4161), tensor(40.2174), tensor(43.9856), tensor(39.1941), tensor(42.3358)]
fb, day 66 acc_test tensor(41.3588) train_loss 2.0161259605118222
test_semi_fb acc_test_lst [tensor(38.6121), tensor(35.1351), tensor(50.3610), tensor(45.5674), tensor(40.0362), tensor(39.2336), tensor(40.0362), tensor(45.0628), tensor(39.3773), tensor(42.7007)]
fb, day 67 acc_test tensor(41.6123) train_loss 2.025157132501402
test_semi_fb acc_test_lst [tensor(38.9680), tensor(35.6757), tensor(49.8195), tensor(44.8582), tensor(39.8551), tensor(39.5985), tensor(40.5797), tensor(44.1652), tensor(39.7436), tensor(41.6058)]
fb, day 68 acc_test tensor(41.4869) train_loss 2.041602192629436
test_semi_fb acc_test_lst [tensor(38.7900), tensor(35.3153), tensor(50.1805), tensor(44.8582), tensor(39.4928), tensor(39.2336), tensor(40.2174), tensor(44.1652), tensor(39.3773), tensor(42.3358)]
fb, day 69 acc_test tensor(41.3966) train_loss 2.0637362233490006
test_semi_fb acc_test_lst [tensor(39.3238), tensor(34.7748), tensor(49.8195), tensor(44.6809), tensor(39.4928), tensor(39.0511), tensor(39.8551), tensor(44.1652), tensor(39.3773), tensor(42.5182)]
fb, day 70 acc_test tensor(41.3059) train_loss 2.073375594521229
test_semi_fb acc_test_lst [tensor(39.1459), tensor(35.3153), tensor(50.1805), tensor(44.8582), tensor(40.2174), tensor(39.2336), tensor(40.2174), tensor(43.9856), tensor(40.2930), tensor(41.6058)]
fb, day 71 acc_test tensor(41.5053) train_loss 2.0915496653199313
test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.1351), tensor(49.6390), tensor(44.8582), tensor(39.8551), tensor(39.5985), tensor(40.2174), tensor(43.8061), tensor(39.7436), tensor(41.9708)]
fb, day 72 acc_test tensor(41.4148) train_loss 2.107992938430415
test_semi_fb acc_test_lst [tensor(39.5018), tensor(35.8559), tensor(50.1805), tensor(44.6809), tensor(39.3116), tensor(39.0511), tensor(40.0362), tensor(44.5242), tensor(39.9267), tensor(42.5182)]
fb, day 73 acc_test tensor(41.5587) train_loss 2.125999427615116
test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.3153), tensor(49.8195), tensor(44.3262), tensor(39.3116), tensor(39.2336), tensor(40.2174), tensor(44.7038), tensor(39.3773), tensor(42.1533)]
fb, day 74 acc_test tensor(41.3782) train_loss 2.1378308974562565
test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.4955), tensor(50.), tensor(44.5035), tensor(39.8551), tensor(39.5985), tensor(40.3986), tensor(44.3447), tensor(40.1099), tensor(41.7883)]
fb, day 75 acc_test tensor(41.5418) train_loss 2.149369612076948
test_semi_fb acc_test_lst [tensor(39.5018), tensor(34.7748), tensor(49.8195), tensor(44.5035), tensor(39.6739), tensor(38.6861), tensor(40.3986), tensor(44.7038), tensor(39.9267), tensor(41.9708)]
fb, day 76 acc_test tensor(41.3959) train_loss 2.161574499335291
test_semi_fb acc_test_lst [tensor(39.8577), tensor(35.1351), tensor(50.3610), tensor(44.3262), tensor(39.6739), tensor(39.2336), tensor(40.2174), tensor(45.0628), tensor(39.9267), tensor(42.1533)]
fb, day 77 acc_test tensor(41.5948) train_loss 2.1824048596564576
test_semi_fb acc_test_lst [tensor(39.8577), tensor(35.4955), tensor(50.3610), tensor(44.3262), tensor(39.3116), tensor(39.0511), tensor(40.3986), tensor(45.0628), tensor(39.5604), tensor(42.1533)]
fb, day 78 acc_test tensor(41.5578) train_loss 2.1981835731943162
test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.3153), tensor(49.8195), tensor(43.9716), tensor(39.1304), tensor(39.2336), tensor(40.2174), tensor(44.5242), tensor(39.7436), tensor(42.1533)]
fb, day 79 acc_test tensor(41.3433) train_loss 2.2122162847603746
test_semi_fb acc_test_lst [tensor(39.5018), tensor(35.6757), tensor(50.3610), tensor(43.9716), tensor(38.5870), tensor(39.0511), tensor(40.2174), tensor(44.7038), tensor(40.1099), tensor(42.3358)]
fb, day 80 acc_test tensor(41.4515) train_loss 2.2304987136863073
test_semi_fb acc_test_lst [tensor(39.6797), tensor(34.9550), tensor(51.2635), tensor(44.1489), tensor(39.4928), tensor(39.4161), tensor(39.8551), tensor(44.1652), tensor(39.7436), tensor(41.9708)]
fb, day 81 acc_test tensor(41.4691) train_loss 2.2355876002412622
test_semi_fb acc_test_lst [tensor(39.5018), tensor(35.1351), tensor(50.1805), tensor(44.1489), tensor(39.4928), tensor(39.7810), tensor(40.0362), tensor(45.0628), tensor(40.1099), tensor(41.9708)]
fb, day 82 acc_test tensor(41.5420) train_loss 2.264374027439024
test_semi_fb acc_test_lst [tensor(39.3238), tensor(34.4144), tensor(51.0830), tensor(43.2624), tensor(39.3116), tensor(38.8686), tensor(40.2174), tensor(44.7038), tensor(40.1099), tensor(41.9708)]
fb, day 83 acc_test tensor(41.3266) train_loss 2.2716484364783454
test_semi_fb acc_test_lst [tensor(39.1459), tensor(34.5946), tensor(50.3610), tensor(43.9716), tensor(39.1304), tensor(39.4161), tensor(40.0362), tensor(44.5242), tensor(40.1099), tensor(41.9708)]
fb, day 84 acc_test tensor(41.3261) train_loss 2.2811419238562745
test_semi_fb acc_test_lst [tensor(39.6797), tensor(34.7748), tensor(50.5415), tensor(43.2624), tensor(39.3116), tensor(39.9635), tensor(39.8551), tensor(44.3447), tensor(40.1099), tensor(41.9708)]
fb, day 85 acc_test tensor(41.3814) train_loss 2.2959414780182597
test_semi_fb acc_test_lst [tensor(39.5018), tensor(34.5946), tensor(50.9025), tensor(43.0851), tensor(38.9493), tensor(39.4161), tensor(39.8551), tensor(44.5242), tensor(40.2930), tensor(42.5182)]
fb, day 86 acc_test tensor(41.3640) train_loss 2.3119129681190866
test_semi_fb acc_test_lst [tensor(39.8577), tensor(35.3153), tensor(50.5415), tensor(43.2624), tensor(38.7681), tensor(39.2336), tensor(39.6739), tensor(44.7038), tensor(40.8425), tensor(42.3358)]
fb, day 87 acc_test tensor(41.4535) train_loss 2.316265101810792
test_semi_fb acc_test_lst [tensor(40.0356), tensor(34.4144), tensor(50.7220), tensor(43.2624), tensor(39.1304), tensor(39.4161), tensor(40.0362), tensor(44.5242), tensor(40.8425), tensor(41.6058)]
fb, day 88 acc_test tensor(41.3990) train_loss 2.3375712083748965
test_semi_fb acc_test_lst [tensor(39.6797), tensor(34.7748), tensor(50.7220), tensor(43.6170), tensor(39.3116), tensor(39.4161), tensor(39.6739), tensor(44.8833), tensor(41.2088), tensor(41.6058)]
fb, day 89 acc_test tensor(41.4893) train_loss 2.362649836570738
test_semi_fb acc_test_lst [tensor(39.6797), tensor(34.9550), tensor(50.9025), tensor(43.0851), tensor(38.7681), tensor(39.5985), tensor(39.8551), tensor(44.5242), tensor(41.5751), tensor(41.6058)]
fb, day 90 acc_test tensor(41.4549) train_loss 2.3664987033986797
test_semi_fb acc_test_lst [tensor(39.8577), tensor(34.5946), tensor(50.7220), tensor(43.0851), tensor(38.7681), tensor(39.5985), tensor(40.0362), tensor(44.8833), tensor(41.0256), tensor(41.7883)]
fb, day 91 acc_test tensor(41.4360) train_loss 2.3790433059525786
test_semi_fb acc_test_lst [tensor(40.0356), tensor(34.9550), tensor(50.9025), tensor(43.0851), tensor(38.7681), tensor(39.9635), tensor(40.0362), tensor(44.3447), tensor(41.3919), tensor(42.1533)]
fb, day 92 acc_test tensor(41.5636) train_loss 2.3979932592725923
test_semi_fb acc_test_lst [tensor(39.8577), tensor(35.3153), tensor(50.5415), tensor(42.9078), tensor(38.7681), tensor(39.7810), tensor(40.3986), tensor(44.1652), tensor(41.2088), tensor(42.1533)]
fb, day 93 acc_test tensor(41.5097) train_loss 2.408656664746099
test_semi_fb acc_test_lst [tensor(39.5018), tensor(35.3153), tensor(50.1805), tensor(43.2624), tensor(38.5870), tensor(40.1460), tensor(40.3986), tensor(44.1652), tensor(41.5751), tensor(41.7883)]
fb, day 94 acc_test tensor(41.4920) train_loss 2.4248413187004405
test_semi_fb acc_test_lst [tensor(39.5018), tensor(35.3153), tensor(50.1805), tensor(43.0851), tensor(38.7681), tensor(40.1460), tensor(40.2174), tensor(43.9856), tensor(41.3919), tensor(41.9708)]
fb, day 95 acc_test tensor(41.4563) train_loss 2.430579334388783
test_semi_fb acc_test_lst [tensor(39.8577), tensor(35.1351), tensor(50.5415), tensor(43.0851), tensor(38.7681), tensor(39.9635), tensor(40.0362), tensor(43.8061), tensor(41.5751), tensor(41.9708)]
fb, day 96 acc_test tensor(41.4739) train_loss 2.4409673563770697
test_semi_fb acc_test_lst [tensor(40.2135), tensor(34.7748), tensor(50.1805), tensor(42.7305), tensor(38.7681), tensor(39.7810), tensor(39.8551), tensor(44.1652), tensor(41.5751), tensor(41.9708)]
fb, day 97 acc_test tensor(41.4015) train_loss 2.4587629021513524
test_semi_fb acc_test_lst [tensor(40.2135), tensor(33.8739), tensor(50.7220), tensor(42.7305), tensor(38.9493), tensor(40.3285), tensor(40.0362), tensor(43.6266), tensor(41.7582), tensor(41.9708)]
fb, day 98 acc_test tensor(41.4210) train_loss 2.4709103417058325
test_semi_fb acc_test_lst [tensor(40.2135), tensor(34.4144), tensor(50.), tensor(42.5532), tensor(38.9493), tensor(40.1460), tensor(39.6739), tensor(44.3447), tensor(41.5751), tensor(41.9708)]
fb, day 99 acc_test tensor(41.3841) train_loss 2.492079746297487
test_semi_fb acc_test_lst [tensor(40.5694), tensor(34.0541), tensor(50.3610), tensor(42.7305), tensor(38.5870), tensor(40.6934), tensor(40.0362), tensor(44.1652), tensor(41.5751), tensor(42.1533)]
fb, day 100 acc_test tensor(41.4925) train_loss 2.4982029454125456
test_semi_fb acc_test_lst [tensor(40.5694), tensor(34.0541), tensor(50.), tensor(42.7305), tensor(39.1304), tensor(40.3285), tensor(40.0362), tensor(43.9856), tensor(41.5751), tensor(42.1533)]
fb, day 101 acc_test tensor(41.4563) train_loss 2.4972430376113133
test_semi_fb acc_test_lst [tensor(40.9253), tensor(34.2342), tensor(49.6390), tensor(42.9078), tensor(38.9493), tensor(40.5109), tensor(39.8551), tensor(43.9856), tensor(41.5751), tensor(41.9708)]
fb, day 102 acc_test tensor(41.4553) train_loss 2.5240058431378816
test_semi_fb acc_test_lst [tensor(40.9253), tensor(34.5946), tensor(49.6390), tensor(42.5532), tensor(38.9493), tensor(40.5109), tensor(39.8551), tensor(44.1652), tensor(41.2088), tensor(42.1533)]
fb, day 103 acc_test tensor(41.4555) train_loss 2.533978229578995
test_semi_fb acc_test_lst [tensor(41.2811), tensor(34.4144), tensor(49.2780), tensor(42.3759), tensor(38.9493), tensor(40.5109), tensor(40.0362), tensor(44.1652), tensor(41.0256), tensor(41.9708)]
fb, day 104 acc_test tensor(41.4007) train_loss 2.549091481758576
test_semi_fb acc_test_lst [tensor(41.2811), tensor(34.2342), tensor(49.2780), tensor(42.7305), tensor(38.9493), tensor(40.3285), tensor(39.8551), tensor(43.8061), tensor(41.0256), tensor(41.9708)]
fb, day 105 acc_test tensor(41.3459) train_loss 2.556909463955184
test_semi_fb acc_test_lst [tensor(41.2811), tensor(34.0541), tensor(49.2780), tensor(42.5532), tensor(38.5870), tensor(40.1460), tensor(39.6739), tensor(43.9856), tensor(41.3919), tensor(42.1533)]
fb, day 106 acc_test tensor(41.3104) train_loss 2.562337158508176
test_semi_fb acc_test_lst [tensor(41.4591), tensor(34.0541), tensor(49.0975), tensor(42.9078), tensor(38.7681), tensor(40.3285), tensor(40.0362), tensor(44.1652), tensor(41.3919), tensor(42.1533)]
fb, day 107 acc_test tensor(41.4362) train_loss 2.5680890910652128
test_semi_fb acc_test_lst [tensor(41.4591), tensor(34.0541), tensor(48.9170), tensor(42.9078), tensor(38.9493), tensor(40.3285), tensor(39.6739), tensor(43.4470), tensor(41.2088), tensor(42.1533)]
fb, day 108 acc_test tensor(41.3099) train_loss 2.5863755571809164
test_semi_fb acc_test_lst [tensor(41.8149), tensor(33.8739), tensor(48.5560), tensor(42.9078), tensor(38.9493), tensor(39.9635), tensor(39.6739), tensor(43.6266), tensor(41.0256), tensor(42.1533)]
fb, day 109 acc_test tensor(41.2545) train_loss 2.6031256395439346
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.9170), tensor(42.9078), tensor(38.9493), tensor(40.3285), tensor(39.8551), tensor(43.4470), tensor(41.2088), tensor(42.3358)]
fb, day 110 acc_test tensor(41.3640) train_loss 2.618097334146337
test_semi_fb acc_test_lst [tensor(41.6370), tensor(33.6937), tensor(48.7365), tensor(42.7305), tensor(39.1304), tensor(40.5109), tensor(39.8551), tensor(43.2675), tensor(41.0256), tensor(41.9708)]
fb, day 111 acc_test tensor(41.2558) train_loss 2.6299966204283844
test_semi_fb acc_test_lst [tensor(41.8149), tensor(33.8739), tensor(48.7365), tensor(42.9078), tensor(38.4058), tensor(40.6934), tensor(39.8551), tensor(43.2675), tensor(41.0256), tensor(42.1533)]
fb, day 112 acc_test tensor(41.2734) train_loss 2.6354045854589994
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.0541), tensor(48.7365), tensor(42.7305), tensor(38.4058), tensor(40.6934), tensor(39.8551), tensor(43.2675), tensor(40.8425), tensor(42.5182)]
fb, day 113 acc_test tensor(41.2919) train_loss 2.6485852660372986
test_semi_fb acc_test_lst [tensor(41.6370), tensor(33.8739), tensor(48.7365), tensor(42.7305), tensor(38.7681), tensor(41.0584), tensor(39.8551), tensor(43.2675), tensor(40.6593), tensor(42.7007)]
fb, day 114 acc_test tensor(41.3287) train_loss 2.657270867979502
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.2342), tensor(48.7365), tensor(42.9078), tensor(38.5870), tensor(41.0584), tensor(39.6739), tensor(43.4470), tensor(40.8425), tensor(42.5182)]
fb, day 115 acc_test tensor(41.3643) train_loss 2.6675965117715212
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.7365), tensor(42.5532), tensor(38.4058), tensor(40.8759), tensor(39.8551), tensor(43.4470), tensor(40.8425), tensor(42.5182)]
fb, day 116 acc_test tensor(41.2925) train_loss 2.672585230703473
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.7365), tensor(42.5532), tensor(38.2246), tensor(40.8759), tensor(39.6739), tensor(43.2675), tensor(40.6593), tensor(42.5182)]
fb, day 117 acc_test tensor(41.2200) train_loss 2.695919712880896
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.7365), tensor(42.5532), tensor(38.7681), tensor(41.0584), tensor(39.8551), tensor(43.2675), tensor(40.8425), tensor(42.5182)]
fb, day 118 acc_test tensor(41.3291) train_loss 2.696499484532863
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.9170), tensor(42.5532), tensor(38.9493), tensor(40.8759), tensor(39.8551), tensor(43.2675), tensor(40.6593), tensor(42.3358)]
fb, day 119 acc_test tensor(41.3104) train_loss 2.7132509712992667
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.9170), tensor(42.5532), tensor(38.7681), tensor(41.2409), tensor(39.8551), tensor(43.4470), tensor(40.6593), tensor(42.5182)]
fb, day 120 acc_test tensor(41.3650) train_loss 2.7047264286238435
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.5560), tensor(42.3759), tensor(38.4058), tensor(41.0584), tensor(39.8551), tensor(43.0880), tensor(40.8425), tensor(42.7007)]
fb, day 121 acc_test tensor(41.2573) train_loss 2.7330956785878016
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.0541), tensor(48.5560), tensor(42.3759), tensor(38.5870), tensor(41.0584), tensor(39.8551), tensor(43.2675), tensor(40.6593), tensor(42.3358)]
fb, day 122 acc_test tensor(41.2742) train_loss 2.7288959346026256
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.0541), tensor(48.5560), tensor(42.5532), tensor(38.5870), tensor(41.4234), tensor(39.8551), tensor(43.4470), tensor(40.6593), tensor(42.7007)]
fb, day 123 acc_test tensor(41.3651) train_loss 2.740529048973723
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.0541), tensor(48.5560), tensor(42.3759), tensor(38.4058), tensor(41.0584), tensor(39.8551), tensor(43.0880), tensor(40.6593), tensor(42.7007)]
fb, day 124 acc_test tensor(41.2568) train_loss 2.753109864805869
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.0541), tensor(48.3755), tensor(42.9078), tensor(38.4058), tensor(41.2409), tensor(39.8551), tensor(43.8061), tensor(40.6593), tensor(42.7007)]
fb, day 125 acc_test tensor(41.3998) train_loss 2.7757811328767183
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.0541), tensor(48.5560), tensor(42.5532), tensor(38.4058), tensor(41.4234), tensor(39.8551), tensor(43.6266), tensor(40.4762), tensor(42.7007)]
fb, day 126 acc_test tensor(41.3644) train_loss 2.772017200761774
test_semi_fb acc_test_lst [tensor(41.8149), tensor(33.8739), tensor(48.5560), tensor(42.7305), tensor(38.4058), tensor(41.4234), tensor(39.6739), tensor(43.6266), tensor(40.8425), tensor(42.8832)]
fb, day 127 acc_test tensor(41.3831) train_loss 2.783076486172102
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.0541), tensor(48.5560), tensor(42.7305), tensor(38.2246), tensor(41.4234), tensor(39.8551), tensor(43.6266), tensor(41.0256), tensor(43.0657)]
fb, day 128 acc_test tensor(41.4554) train_loss 2.7972592189811594
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.0541), tensor(48.5560), tensor(42.5532), tensor(38.0435), tensor(41.7883), tensor(39.8551), tensor(43.6266), tensor(40.8425), tensor(43.0657)]
fb, day 129 acc_test tensor(41.4378) train_loss 2.797889067590691
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.0541), tensor(48.3755), tensor(42.9078), tensor(38.2246), tensor(41.7883), tensor(40.0362), tensor(43.8061), tensor(40.8425), tensor(42.8832)]
fb, day 130 acc_test tensor(41.4911) train_loss 2.804065128636331
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.2342), tensor(48.3755), tensor(43.2624), tensor(38.2246), tensor(41.7883), tensor(40.0362), tensor(43.6266), tensor(40.6593), tensor(42.8832)]
fb, day 131 acc_test tensor(41.5083) train_loss 2.8215635669728227
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.0541), tensor(48.5560), tensor(43.0851), tensor(38.0435), tensor(41.7883), tensor(40.0362), tensor(43.6266), tensor(41.0256), tensor(43.4307)]
fb, day 132 acc_test tensor(41.5461) train_loss 2.8342387491939314
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.0541), tensor(48.3755), tensor(43.0851), tensor(38.0435), tensor(41.7883), tensor(40.0362), tensor(43.6266), tensor(40.8425), tensor(43.0657)]
fb, day 133 acc_test tensor(41.4732) train_loss 2.8300846402560706
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.1949), tensor(43.4397), tensor(37.8623), tensor(41.7883), tensor(40.0362), tensor(43.6266), tensor(40.8425), tensor(43.2482)]
fb, day 134 acc_test tensor(41.4730) train_loss 2.857657075257974
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.0541), tensor(48.3755), tensor(42.9078), tensor(38.0435), tensor(41.7883), tensor(40.0362), tensor(43.6266), tensor(40.6593), tensor(43.2482)]
fb, day 135 acc_test tensor(41.4732) train_loss 2.8565957285021284
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.0541), tensor(48.5560), tensor(42.9078), tensor(38.0435), tensor(41.9708), tensor(40.0362), tensor(43.4470), tensor(40.6593), tensor(43.4307)]
fb, day 136 acc_test tensor(41.4920) train_loss 2.8602624140284907
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.2342), tensor(48.7365), tensor(42.9078), tensor(38.0435), tensor(41.9708), tensor(40.0362), tensor(43.4470), tensor(40.6593), tensor(43.4307)]
fb, day 137 acc_test tensor(41.5281) train_loss 2.8791196008483433
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.2342), tensor(48.5560), tensor(42.9078), tensor(38.0435), tensor(41.6058), tensor(39.8551), tensor(43.6266), tensor(40.2930), tensor(43.0657)]
fb, day 138 acc_test tensor(41.4003) train_loss 2.879267690642976
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.4144), tensor(48.5560), tensor(42.9078), tensor(38.0435), tensor(41.9708), tensor(40.0362), tensor(43.4470), tensor(40.2930), tensor(43.2482)]
fb, day 139 acc_test tensor(41.4554) train_loss 2.8935495933365125
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.4144), tensor(48.7365), tensor(42.9078), tensor(37.8623), tensor(41.7883), tensor(40.0362), tensor(43.4470), tensor(40.2930), tensor(43.2482)]
fb, day 140 acc_test tensor(41.4371) train_loss 2.89946391695394
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.2342), tensor(48.5560), tensor(43.0851), tensor(38.0435), tensor(41.7883), tensor(40.0362), tensor(43.4470), tensor(40.2930), tensor(43.2482)]
fb, day 141 acc_test tensor(41.4369) train_loss 2.917222529145217
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.2342), tensor(48.7365), tensor(42.9078), tensor(37.8623), tensor(41.7883), tensor(39.6739), tensor(43.4470), tensor(40.2930), tensor(43.2482)]
fb, day 142 acc_test tensor(41.3828) train_loss 2.903529359607647
test_semi_fb acc_test_lst [tensor(41.4591), tensor(34.4144), tensor(48.3755), tensor(42.9078), tensor(38.0435), tensor(41.6058), tensor(39.8551), tensor(43.4470), tensor(40.4762), tensor(43.6131)]
fb, day 143 acc_test tensor(41.4197) train_loss 2.91197556022031
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.7365), tensor(42.7305), tensor(37.8623), tensor(41.7883), tensor(39.6739), tensor(43.4470), tensor(40.1099), tensor(43.4307)]
fb, day 144 acc_test tensor(41.3470) train_loss 2.9414796725037426
test_semi_fb acc_test_lst [tensor(41.4591), tensor(34.0541), tensor(48.7365), tensor(42.9078), tensor(37.8623), tensor(41.9708), tensor(39.6739), tensor(43.4470), tensor(40.2930), tensor(43.6131)]
fb, day 145 acc_test tensor(41.4018) train_loss 2.9432244918166215
test_semi_fb acc_test_lst [tensor(41.6370), tensor(33.8739), tensor(48.7365), tensor(42.7305), tensor(37.8623), tensor(42.1533), tensor(39.8551), tensor(42.9084), tensor(40.2930), tensor(43.6131)]
fb, day 146 acc_test tensor(41.3663) train_loss 2.947572243430473
test_semi_fb acc_test_lst [tensor(41.8149), tensor(33.8739), tensor(48.5560), tensor(42.9078), tensor(37.8623), tensor(41.9708), tensor(39.6739), tensor(43.0880), tensor(40.4762), tensor(43.4307)]
fb, day 147 acc_test tensor(41.3654) train_loss 2.9518164275440797
test_semi_fb acc_test_lst [tensor(41.8149), tensor(33.6937), tensor(48.5560), tensor(42.7305), tensor(37.8623), tensor(42.1533), tensor(39.6739), tensor(43.0880), tensor(40.2930), tensor(43.6131)]
fb, day 148 acc_test tensor(41.3479) train_loss 2.956805831016462
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.0541), tensor(48.3755), tensor(42.5532), tensor(37.8623), tensor(42.1533), tensor(39.8551), tensor(43.0880), tensor(40.4762), tensor(43.6131)]
fb, day 149 acc_test tensor(41.3846) train_loss 2.955620016615278
test_semi_fb acc_test_lst [tensor(41.8149), tensor(33.8739), tensor(48.5560), tensor(42.5532), tensor(37.8623), tensor(42.1533), tensor(39.6739), tensor(42.9084), tensor(40.2930), tensor(43.7956)]
fb, day 150 acc_test tensor(41.3485) train_loss 2.9740117871996863
test_semi_fb acc_test_lst [tensor(41.9929), tensor(33.8739), tensor(48.5560), tensor(42.5532), tensor(38.0435), tensor(42.1533), tensor(39.8551), tensor(42.9084), tensor(40.4762), tensor(43.6131)]
fb, day 151 acc_test tensor(41.4025) train_loss 2.9703223259396885
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.0541), tensor(48.5560), tensor(42.5532), tensor(38.0435), tensor(41.9708), tensor(39.6739), tensor(43.0880), tensor(40.6593), tensor(43.7956)]
fb, day 152 acc_test tensor(41.4031) train_loss 2.9823736485056047
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.0541), tensor(48.5560), tensor(42.5532), tensor(38.0435), tensor(41.9708), tensor(39.8551), tensor(42.7289), tensor(40.6593), tensor(43.6131)]
fb, day 153 acc_test tensor(41.4205) train_loss 2.9967074461067487
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.2342), tensor(48.3755), tensor(42.5532), tensor(38.0435), tensor(41.7883), tensor(39.8551), tensor(42.9084), tensor(40.4762), tensor(43.7956)]
fb, day 154 acc_test tensor(41.3845) train_loss 2.993359178717865
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.4144), tensor(48.5560), tensor(42.5532), tensor(38.2246), tensor(41.9708), tensor(39.6739), tensor(42.9084), tensor(40.6593), tensor(43.7956)]
fb, day 155 acc_test tensor(41.4393) train_loss 3.0105972354042168
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.4144), tensor(48.3755), tensor(42.7305), tensor(38.0435), tensor(41.9708), tensor(40.0362), tensor(42.9084), tensor(40.4762), tensor(43.7956)]
fb, day 156 acc_test tensor(41.4566) train_loss 3.0127379753766768
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.2342), tensor(48.3755), tensor(42.5532), tensor(38.0435), tensor(41.9708), tensor(40.2174), tensor(42.9084), tensor(40.6593), tensor(43.6131)]
fb, day 157 acc_test tensor(41.4746) train_loss 3.0318009788454496
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.4144), tensor(48.1949), tensor(42.7305), tensor(38.0435), tensor(42.1533), tensor(39.8551), tensor(42.7289), tensor(40.4762), tensor(43.7956)]
fb, day 158 acc_test tensor(41.4563) train_loss 3.040541272141384
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.5946), tensor(48.0144), tensor(42.7305), tensor(37.8623), tensor(41.9708), tensor(39.6739), tensor(42.9084), tensor(40.6593), tensor(43.7956)]
fb, day 159 acc_test tensor(41.4381) train_loss 3.0435663805442217
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.4144), tensor(48.0144), tensor(42.7305), tensor(37.8623), tensor(41.7883), tensor(39.8551), tensor(42.7289), tensor(40.4762), tensor(43.7956)]
fb, day 160 acc_test tensor(41.3659) train_loss 3.0293942004569847
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.4144), tensor(48.0144), tensor(42.7305), tensor(37.8623), tensor(41.9708), tensor(39.6739), tensor(42.7289), tensor(40.6593), tensor(43.7956)]
fb, day 161 acc_test tensor(41.3843) train_loss 3.0454816422985624
test_semi_fb acc_test_lst [tensor(42.3488), tensor(34.7748), tensor(47.8339), tensor(42.7305), tensor(38.0435), tensor(41.7883), tensor(39.4928), tensor(42.7289), tensor(40.6593), tensor(43.7956)]
fb, day 162 acc_test tensor(41.4196) train_loss 3.063966765329803
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.7748), tensor(47.8339), tensor(42.7305), tensor(37.8623), tensor(41.6058), tensor(39.6739), tensor(42.7289), tensor(40.6593), tensor(43.6131)]
fb, day 163 acc_test tensor(41.3653) train_loss 3.064741566155186
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.7748), tensor(47.8339), tensor(42.7305), tensor(37.8623), tensor(41.6058), tensor(39.6739), tensor(42.1903), tensor(40.4762), tensor(43.7956)]
fb, day 164 acc_test tensor(41.2936) train_loss 3.069897507787189
test_semi_fb acc_test_lst [tensor(42.3488), tensor(34.7748), tensor(47.8339), tensor(42.7305), tensor(38.0435), tensor(41.6058), tensor(39.4928), tensor(42.1903), tensor(40.8425), tensor(43.6131)]
fb, day 165 acc_test tensor(41.3476) train_loss 3.0762263203353153
test_semi_fb acc_test_lst [tensor(42.3488), tensor(34.9550), tensor(47.6534), tensor(42.9078), tensor(38.0435), tensor(41.6058), tensor(39.6739), tensor(42.0108), tensor(40.6593), tensor(43.6131)]
fb, day 166 acc_test tensor(41.3471) train_loss 3.072190247986587
test_semi_fb acc_test_lst [tensor(42.3488), tensor(34.7748), tensor(47.8339), tensor(42.9078), tensor(38.0435), tensor(41.2409), tensor(39.6739), tensor(42.1903), tensor(40.8425), tensor(43.6131)]
fb, day 167 acc_test tensor(41.3469) train_loss 3.095328949606938
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.7748), tensor(47.8339), tensor(42.7305), tensor(38.2246), tensor(41.4234), tensor(39.6739), tensor(42.1903), tensor(40.6593), tensor(43.6131)]
fb, day 168 acc_test tensor(41.3295) train_loss 3.090475745766615
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.5946), tensor(47.6534), tensor(42.7305), tensor(38.0435), tensor(41.0584), tensor(39.6739), tensor(42.0108), tensor(40.6593), tensor(43.6131)]
fb, day 169 acc_test tensor(41.2208) train_loss 3.1095240983056702
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.7748), tensor(47.8339), tensor(42.7305), tensor(38.2246), tensor(41.4234), tensor(39.6739), tensor(42.0108), tensor(40.6593), tensor(43.7956)]
fb, day 170 acc_test tensor(41.3298) train_loss 3.0995554646085886
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.9550), tensor(47.8339), tensor(42.7305), tensor(38.2246), tensor(41.0584), tensor(39.6739), tensor(41.8312), tensor(40.6593), tensor(43.7956)]
fb, day 171 acc_test tensor(41.2933) train_loss 3.117663414178545
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.7748), tensor(47.6534), tensor(42.7305), tensor(38.2246), tensor(41.0584), tensor(39.6739), tensor(41.8312), tensor(40.6593), tensor(43.7956)]
fb, day 172 acc_test tensor(41.2573) train_loss 3.1216863302371496
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.7748), tensor(47.6534), tensor(42.7305), tensor(38.2246), tensor(41.0584), tensor(39.6739), tensor(41.8312), tensor(40.6593), tensor(43.9781)]
fb, day 173 acc_test tensor(41.2755) train_loss 3.1213104268014846
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.7748), tensor(47.8339), tensor(42.9078), tensor(38.2246), tensor(41.0584), tensor(39.6739), tensor(41.6517), tensor(40.8425), tensor(43.9781)]
fb, day 174 acc_test tensor(41.3117) train_loss 3.1325553518769027
test_semi_fb acc_test_lst [tensor(42.1708), tensor(34.7748), tensor(47.4729), tensor(42.9078), tensor(38.2246), tensor(41.0584), tensor(39.6739), tensor(41.8312), tensor(40.4762), tensor(43.7956)]
fb, day 175 acc_test tensor(41.2386) train_loss 3.1357403507822106
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.7748), tensor(47.6534), tensor(42.9078), tensor(38.0435), tensor(41.2409), tensor(39.6739), tensor(41.6517), tensor(40.6593), tensor(43.9781)]
fb, day 176 acc_test tensor(41.2576) train_loss 3.1458713897775032
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.7748), tensor(47.4729), tensor(42.9078), tensor(38.0435), tensor(41.0584), tensor(39.8551), tensor(41.6517), tensor(40.6593), tensor(43.9781)]
fb, day 177 acc_test tensor(41.2394) train_loss 3.1402348410075276
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.7748), tensor(47.4729), tensor(42.9078), tensor(38.0435), tensor(41.2409), tensor(39.8551), tensor(41.6517), tensor(40.6593), tensor(43.9781)]
fb, day 178 acc_test tensor(41.2577) train_loss 3.1430759091717255
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.7748), tensor(47.2924), tensor(42.9078), tensor(38.0435), tensor(41.0584), tensor(39.6739), tensor(41.8312), tensor(40.6593), tensor(43.9781)]
fb, day 179 acc_test tensor(41.2212) train_loss 3.16389961210713
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.2924), tensor(42.9078), tensor(38.0435), tensor(41.0584), tensor(39.8551), tensor(41.4722), tensor(40.6593), tensor(43.9781)]
fb, day 180 acc_test tensor(41.1856) train_loss 3.164289448989288
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.4729), tensor(42.9078), tensor(38.0435), tensor(41.2409), tensor(39.8551), tensor(41.6517), tensor(40.6593), tensor(43.9781)]
fb, day 181 acc_test tensor(41.2399) train_loss 3.167939700100661
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.2924), tensor(42.9078), tensor(38.0435), tensor(41.0584), tensor(39.8551), tensor(41.4722), tensor(40.4762), tensor(43.9781)]
fb, day 182 acc_test tensor(41.1673) train_loss 3.1682773897019327
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.1119), tensor(42.9078), tensor(38.0435), tensor(41.2409), tensor(39.8551), tensor(41.4722), tensor(40.2930), tensor(43.9781)]
fb, day 183 acc_test tensor(41.1492) train_loss 3.17544113039603
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.2924), tensor(42.9078), tensor(38.0435), tensor(41.2409), tensor(39.8551), tensor(41.4722), tensor(40.1099), tensor(43.9781)]
fb, day 184 acc_test tensor(41.1490) train_loss 3.193355772463605
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.2924), tensor(42.9078), tensor(38.4058), tensor(41.2409), tensor(39.8551), tensor(41.4722), tensor(39.9267), tensor(44.1606)]
fb, day 185 acc_test tensor(41.1851) train_loss 3.1949684172164456
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.1119), tensor(42.9078), tensor(38.2246), tensor(41.0584), tensor(39.8551), tensor(41.4722), tensor(39.9267), tensor(44.1606)]
fb, day 186 acc_test tensor(41.1307) train_loss 3.184796346902522
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.1119), tensor(42.9078), tensor(38.4058), tensor(41.2409), tensor(39.8551), tensor(41.4722), tensor(40.1099), tensor(44.1606)]
fb, day 187 acc_test tensor(41.1854) train_loss 3.2088093873548895
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(47.1119), tensor(42.7305), tensor(38.4058), tensor(41.2409), tensor(39.8551), tensor(41.4722), tensor(39.9267), tensor(44.1606)]
fb, day 188 acc_test tensor(41.1493) train_loss 3.2090884430497444
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.7748), tensor(47.1119), tensor(42.7305), tensor(38.4058), tensor(41.2409), tensor(39.8551), tensor(41.4722), tensor(40.1099), tensor(44.3431)]
fb, day 189 acc_test tensor(41.1681) train_loss 3.2138355035612163
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.7748), tensor(46.9314), tensor(42.7305), tensor(38.5870), tensor(41.2409), tensor(40.0362), tensor(41.4722), tensor(40.1099), tensor(44.3431)]
fb, day 190 acc_test tensor(41.1863) train_loss 3.2196944465764035
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(46.9314), tensor(42.7305), tensor(38.4058), tensor(41.2409), tensor(39.8551), tensor(41.4722), tensor(40.4762), tensor(44.1606)]
fb, day 191 acc_test tensor(41.1862) train_loss 3.2307127177490917
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.7748), tensor(47.1119), tensor(42.7305), tensor(38.4058), tensor(40.8759), tensor(39.8551), tensor(41.4722), tensor(40.2930), tensor(44.1606)]
fb, day 192 acc_test tensor(41.1317) train_loss 3.2261530548952453
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.9314), tensor(42.7305), tensor(38.4058), tensor(41.2409), tensor(40.0362), tensor(41.4722), tensor(40.2930), tensor(44.1606)]
fb, day 193 acc_test tensor(41.1863) train_loss 3.2359612346087108
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.9314), tensor(42.7305), tensor(38.4058), tensor(41.2409), tensor(40.0362), tensor(41.4722), tensor(40.2930), tensor(44.1606)]
fb, day 194 acc_test tensor(41.1863) train_loss 3.2500888717884653
test_semi_fb acc_test_lst [tensor(41.6370), tensor(35.1351), tensor(46.7509), tensor(42.9078), tensor(38.4058), tensor(41.2409), tensor(40.2174), tensor(41.4722), tensor(40.4762), tensor(44.1606)]
fb, day 195 acc_test tensor(41.2404) train_loss 3.2509963927632723
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(47.1119), tensor(42.9078), tensor(38.5870), tensor(41.2409), tensor(40.2174), tensor(41.4722), tensor(40.4762), tensor(44.1606)]
fb, day 196 acc_test tensor(41.2766) train_loss 3.237988176479115
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.9314), tensor(42.9078), tensor(38.5870), tensor(41.2409), tensor(40.3986), tensor(41.4722), tensor(40.4762), tensor(44.1606)]
fb, day 197 acc_test tensor(41.3125) train_loss 3.237329424581525
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.7509), tensor(42.9078), tensor(38.5870), tensor(41.0584), tensor(40.3986), tensor(41.4722), tensor(40.4762), tensor(44.1606)]
fb, day 198 acc_test tensor(41.2404) train_loss 3.2570174827585907
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.9314), tensor(42.9078), tensor(38.5870), tensor(41.4234), tensor(40.3986), tensor(41.4722), tensor(40.2930), tensor(44.1606)]
fb, day 199 acc_test tensor(41.3124) train_loss 3.2650083572744744
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(42.9078), tensor(38.7681), tensor(41.4234), tensor(40.3986), tensor(41.4722), tensor(40.1099), tensor(44.1606)]
fb, day 200 acc_test tensor(41.3302) train_loss 3.259876850465713
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(42.7305), tensor(38.5870), tensor(41.4234), tensor(40.3986), tensor(41.4722), tensor(40.2930), tensor(44.3431)]
fb, day 201 acc_test tensor(41.3310) train_loss 3.2760998150455696
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.9314), tensor(42.7305), tensor(38.7681), tensor(41.4234), tensor(40.3986), tensor(41.4722), tensor(40.2930), tensor(44.1606)]
fb, day 202 acc_test tensor(41.3128) train_loss 3.2771111574572824
test_semi_fb acc_test_lst [tensor(41.6370), tensor(35.1351), tensor(46.9314), tensor(42.7305), tensor(38.5870), tensor(41.2409), tensor(40.3986), tensor(41.4722), tensor(40.2930), tensor(44.1606)]
fb, day 203 acc_test tensor(41.2586) train_loss 3.2695766143070615
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.9314), tensor(42.5532), tensor(38.7681), tensor(41.4234), tensor(40.3986), tensor(41.4722), tensor(40.2930), tensor(44.3431)]
fb, day 204 acc_test tensor(41.3133) train_loss 3.282432380764905
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.9314), tensor(42.9078), tensor(38.7681), tensor(41.2409), tensor(40.3986), tensor(41.4722), tensor(40.2930), tensor(44.3431)]
fb, day 205 acc_test tensor(41.3305) train_loss 3.266207029754054
test_semi_fb acc_test_lst [tensor(41.6370), tensor(35.1351), tensor(47.2924), tensor(42.9078), tensor(38.5870), tensor(41.6058), tensor(40.2174), tensor(41.4722), tensor(40.4762), tensor(44.3431)]
fb, day 206 acc_test tensor(41.3674) train_loss 3.2876681669724572
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(42.9078), tensor(38.7681), tensor(41.4234), tensor(40.3986), tensor(41.2926), tensor(40.4762), tensor(44.3431)]
fb, day 207 acc_test tensor(41.3672) train_loss 3.3021885143082756
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(42.7305), tensor(38.7681), tensor(41.2409), tensor(40.2174), tensor(41.4722), tensor(40.4762), tensor(44.3431)]
fb, day 208 acc_test tensor(41.3310) train_loss 3.288098813033933
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.3153), tensor(47.1119), tensor(43.2624), tensor(38.5870), tensor(41.6058), tensor(40.2174), tensor(41.2926), tensor(40.2930), tensor(44.3431)]
fb, day 209 acc_test tensor(41.3843) train_loss 3.294955175766099
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(47.1119), tensor(42.9078), tensor(38.7681), tensor(41.4234), tensor(40.2174), tensor(41.4722), tensor(40.4762), tensor(44.3431)]
fb, day 210 acc_test tensor(41.3848) train_loss 3.30481885678914
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(43.0851), tensor(38.7681), tensor(41.2409), tensor(40.0362), tensor(41.2926), tensor(40.4762), tensor(44.5255)]
fb, day 211 acc_test tensor(41.3487) train_loss 3.3231409323065133
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(42.9078), tensor(38.7681), tensor(41.4234), tensor(39.8551), tensor(41.4722), tensor(40.4762), tensor(44.3431)]
fb, day 212 acc_test tensor(41.3308) train_loss 3.3398293235652723
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(43.0851), tensor(38.7681), tensor(41.4234), tensor(39.8551), tensor(41.2926), tensor(40.4762), tensor(44.3431)]
fb, day 213 acc_test tensor(41.3306) train_loss 3.325795981446697
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.9314), tensor(43.0851), tensor(38.7681), tensor(41.4234), tensor(39.8551), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fb, day 214 acc_test tensor(41.3487) train_loss 3.3251410290323595
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(47.1119), tensor(42.7305), tensor(38.9493), tensor(41.6058), tensor(39.8551), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fb, day 215 acc_test tensor(41.3677) train_loss 3.3320290216738417
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(47.1119), tensor(42.9078), tensor(38.5870), tensor(41.6058), tensor(39.6739), tensor(41.2926), tensor(40.6593), tensor(44.5255)]
fb, day 216 acc_test tensor(41.3492) train_loss 3.3396810468384257
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.7509), tensor(43.0851), tensor(38.7681), tensor(41.4234), tensor(39.6739), tensor(41.4722), tensor(40.6593), tensor(44.5255)]
fb, day 217 acc_test tensor(41.3486) train_loss 3.339100108948875
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.7509), tensor(43.0851), tensor(38.9493), tensor(41.4234), tensor(39.6739), tensor(41.4722), tensor(40.6593), tensor(44.5255)]
fb, day 218 acc_test tensor(41.3490) train_loss 3.361026560704025
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.9078), tensor(38.9493), tensor(41.4234), tensor(39.6739), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fb, day 219 acc_test tensor(41.3127) train_loss 3.3426545961516756
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.9314), tensor(43.2624), tensor(38.9493), tensor(41.4234), tensor(39.6739), tensor(41.4722), tensor(40.6593), tensor(44.5255)]
fb, day 220 acc_test tensor(41.4025) train_loss 3.3494403658229674
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.9314), tensor(42.9078), tensor(38.9493), tensor(41.2409), tensor(39.6739), tensor(41.4722), tensor(40.6593), tensor(44.5255)]
fb, day 221 acc_test tensor(41.3488) train_loss 3.3747341532778465
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.9314), tensor(42.9078), tensor(38.9493), tensor(41.4234), tensor(39.6739), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fb, day 222 acc_test tensor(41.3488) train_loss 3.369682796239794
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.7509), tensor(43.0851), tensor(38.9493), tensor(41.4234), tensor(39.6739), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fb, day 223 acc_test tensor(41.3484) train_loss 3.366746549595829
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.7305), tensor(38.9493), tensor(41.6058), tensor(39.6739), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fb, day 224 acc_test tensor(41.3132) train_loss 3.3790069757141454
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.7509), tensor(42.9078), tensor(38.9493), tensor(41.6058), tensor(39.6739), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fb, day 225 acc_test tensor(41.3490) train_loss 3.369689538354471
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.7305), tensor(38.9493), tensor(41.2409), tensor(39.6739), tensor(41.4722), tensor(40.4762), tensor(44.5255)]
fb, day 226 acc_test tensor(41.2767) train_loss 3.371739869378067
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.7305), tensor(39.1304), tensor(41.2409), tensor(39.6739), tensor(41.6517), tensor(40.2930), tensor(44.5255)]
fb, day 227 acc_test tensor(41.2944) train_loss 3.3733784230396306
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.3899), tensor(42.3759), tensor(39.1304), tensor(41.2409), tensor(39.6739), tensor(41.8312), tensor(40.2930), tensor(44.5255)]
fb, day 228 acc_test tensor(41.2589) train_loss 3.3854609998977283
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.5704), tensor(42.5532), tensor(39.1304), tensor(41.2409), tensor(39.6739), tensor(41.6517), tensor(40.2930), tensor(44.5255)]
fb, day 229 acc_test tensor(41.2589) train_loss 3.3998658264930737
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.3759), tensor(39.1304), tensor(41.4234), tensor(39.8551), tensor(41.8312), tensor(40.4762), tensor(44.5255)]
fb, day 230 acc_test tensor(41.3316) train_loss 3.386267046800185
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.3899), tensor(42.3759), tensor(39.1304), tensor(41.4234), tensor(39.6739), tensor(41.4722), tensor(40.2930), tensor(44.5255)]
fb, day 231 acc_test tensor(41.2234) train_loss 3.3956596294394426
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.4928), tensor(41.2409), tensor(39.8551), tensor(42.0108), tensor(40.2930), tensor(44.5255)]
fb, day 232 acc_test tensor(41.3489) train_loss 3.3818219578602338
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.3899), tensor(42.5532), tensor(39.4928), tensor(41.4234), tensor(39.8551), tensor(41.8312), tensor(40.2930), tensor(44.5255)]
fb, day 233 acc_test tensor(41.3134) train_loss 3.389322084349813
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.3759), tensor(39.3116), tensor(41.2409), tensor(39.8551), tensor(41.8312), tensor(40.2930), tensor(44.5255)]
fb, day 234 acc_test tensor(41.2596) train_loss 3.4153943720259416
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.3899), tensor(42.5532), tensor(39.4928), tensor(41.4234), tensor(39.8551), tensor(41.8312), tensor(40.4762), tensor(44.5255)]
fb, day 235 acc_test tensor(41.3139) train_loss 3.4011044435117737
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.7305), tensor(39.3116), tensor(41.2409), tensor(39.6739), tensor(42.0108), tensor(40.4762), tensor(44.5255)]
fb, day 236 acc_test tensor(41.3132) train_loss 3.40233748693033
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.4928), tensor(41.4234), tensor(39.6739), tensor(41.8312), tensor(40.4762), tensor(44.5255)]
fb, day 237 acc_test tensor(41.3139) train_loss 3.431978004886369
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.7305), tensor(39.1304), tensor(41.2409), tensor(39.8551), tensor(42.0108), tensor(40.2930), tensor(44.5255)]
fb, day 238 acc_test tensor(41.2949) train_loss 3.445452323019569
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.3899), tensor(42.7305), tensor(39.8551), tensor(41.2409), tensor(39.6739), tensor(42.0108), tensor(40.4762), tensor(44.5255)]
fb, day 239 acc_test tensor(41.3495) train_loss 3.4218648470295006
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.4928), tensor(41.2409), tensor(39.6739), tensor(41.6517), tensor(40.4762), tensor(44.5255)]
fb, day 240 acc_test tensor(41.2777) train_loss 3.431604220284367
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.3899), tensor(42.5532), tensor(39.6739), tensor(41.2409), tensor(39.6739), tensor(41.8312), tensor(40.4762), tensor(44.5255)]
fb, day 241 acc_test tensor(41.2957) train_loss 3.4326054467551774
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.3899), tensor(42.5532), tensor(39.4928), tensor(41.4234), tensor(39.6739), tensor(42.0108), tensor(40.4762), tensor(44.5255)]
fb, day 242 acc_test tensor(41.3138) train_loss 3.4469524806380156
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.3899), tensor(42.5532), tensor(39.4928), tensor(41.4234), tensor(39.8551), tensor(42.0108), tensor(40.2930), tensor(44.5255)]
fb, day 243 acc_test tensor(41.3136) train_loss 3.4610852999095187
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.3899), tensor(42.5532), tensor(39.6739), tensor(41.2409), tensor(39.6739), tensor(41.8312), tensor(40.2930), tensor(44.5255)]
fb, day 244 acc_test tensor(41.2774) train_loss 3.4488652616178515
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.4234), tensor(39.8551), tensor(41.8312), tensor(40.2930), tensor(44.5255)]
fb, day 245 acc_test tensor(41.3318) train_loss 3.4463056646577233
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.4234), tensor(39.8551), tensor(41.8312), tensor(40.2930), tensor(44.5255)]
fb, day 246 acc_test tensor(41.3318) train_loss 3.4707291549631565
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.2409), tensor(39.8551), tensor(41.8312), tensor(40.2930), tensor(44.5255)]
fb, day 247 acc_test tensor(41.3135) train_loss 3.4380885199257616
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.4234), tensor(39.8551), tensor(41.8312), tensor(40.1099), tensor(44.3431)]
fb, day 248 acc_test tensor(41.2952) train_loss 3.471070833773964
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.8551), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(40.2930), tensor(44.3431)]
fb, day 249 acc_test tensor(41.4043) train_loss 3.4579453633813313
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(40.1099), tensor(44.3431)]
fb, day 250 acc_test tensor(41.3317) train_loss 3.4559057081281184
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.2409), tensor(39.8551), tensor(41.6517), tensor(40.1099), tensor(44.3431)]
fb, day 251 acc_test tensor(41.2768) train_loss 3.4856424409885496
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.6739), tensor(41.6058), tensor(39.8551), tensor(41.6517), tensor(40.1099), tensor(44.3431)]
fb, day 252 acc_test tensor(41.3313) train_loss 3.4715379956006966
test_semi_fb acc_test_lst [tensor(41.6370), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fb, day 253 acc_test tensor(41.3496) train_loss 3.4709235586576246
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(40.1099), tensor(44.3431)]
fb, day 254 acc_test tensor(41.3675) train_loss 3.4895750776496395
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.6739), tensor(41.6058), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fb, day 255 acc_test tensor(41.3491) train_loss 3.5028692948504867
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fb, day 256 acc_test tensor(41.3673) train_loss 3.4914112688563406
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.8551), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.3431)]
fb, day 257 acc_test tensor(41.4038) train_loss 3.485359187406159
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fb, day 258 acc_test tensor(41.3492) train_loss 3.4993627212489833
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.9314), tensor(42.3759), tensor(39.6739), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fb, day 259 acc_test tensor(41.3677) train_loss 3.5032088440410267
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(46.5704), tensor(42.3759), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(39.9267), tensor(44.1606)]
fb, day 260 acc_test tensor(41.2772) train_loss 3.4999863318295628
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(46.5704), tensor(42.1986), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(39.9267), tensor(44.1606)]
fb, day 261 acc_test tensor(41.2595) train_loss 3.5016313219165944
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(46.7509), tensor(42.1986), tensor(39.8551), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(43.9781)]
fb, day 262 acc_test tensor(41.2955) train_loss 3.521152112741076
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.5704), tensor(42.1986), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(39.9267), tensor(43.9781)]
fb, day 263 acc_test tensor(41.2592) train_loss 3.516510125932742
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.7748), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(39.9267), tensor(43.9781)]
fb, day 264 acc_test tensor(41.2767) train_loss 3.530462866335043
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.8551), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(43.9781)]
fb, day 265 acc_test tensor(41.3490) train_loss 3.5310730518458318
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(39.9267), tensor(44.1606)]
fb, day 266 acc_test tensor(41.3488) train_loss 3.5296364731092007
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.5532), tensor(39.4928), tensor(41.7883), tensor(39.8551), tensor(41.8312), tensor(39.9267), tensor(44.1606)]
fb, day 267 acc_test tensor(41.3129) train_loss 3.537706170409702
test_semi_fb acc_test_lst [tensor(41.9929), tensor(34.9550), tensor(46.7509), tensor(42.3759), tensor(39.6739), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.1606)]
fb, day 268 acc_test tensor(41.3492) train_loss 3.541404968881358
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.5704), tensor(42.5532), tensor(39.6739), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.1606)]
fb, day 269 acc_test tensor(41.4028) train_loss 3.5236599727096514
test_semi_fb acc_test_lst [tensor(41.8149), tensor(34.9550), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.1606)]
fb, day 270 acc_test tensor(41.3133) train_loss 3.5367567286740984
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.1606)]
fb, day 271 acc_test tensor(41.3312) train_loss 3.5552637545265533
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.3153), tensor(46.5704), tensor(42.5532), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.1606)]
fb, day 272 acc_test tensor(41.3669) train_loss 3.5697436703000447
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.3153), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(40.1099), tensor(44.1606)]
fb, day 273 acc_test tensor(41.3675) train_loss 3.5572515951411
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.1606)]
fb, day 274 acc_test tensor(41.3490) train_loss 3.559343205907736
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.1606)]
fb, day 275 acc_test tensor(41.3670) train_loss 3.552048355336444
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.1606)]
fb, day 276 acc_test tensor(41.3670) train_loss 3.571650852519335
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.3431)]
fb, day 277 acc_test tensor(41.3494) train_loss 3.5642789935428674
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.3153), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(40.1099), tensor(44.1606)]
fb, day 278 acc_test tensor(41.4031) train_loss 3.552879116753299
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.3431)]
fb, day 279 acc_test tensor(41.3495) train_loss 3.581292882532897
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.1351), tensor(46.5704), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.3431)]
fb, day 280 acc_test tensor(41.3136) train_loss 3.575095735635116
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.5704), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.7436), tensor(44.3431)]
fb, day 281 acc_test tensor(41.3311) train_loss 3.579299311508054
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.1351), tensor(46.5704), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.7436), tensor(44.3431)]
fb, day 282 acc_test tensor(41.3129) train_loss 3.589756799674318
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.5704), tensor(42.1986), tensor(39.1304), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.7436), tensor(44.3431)]
fb, day 283 acc_test tensor(41.2770) train_loss 3.5840306799395436
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.3431)]
fb, day 284 acc_test tensor(41.3856) train_loss 3.572667312003375
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.7509), tensor(42.1986), tensor(39.1304), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.7436), tensor(44.3431)]
fb, day 285 acc_test tensor(41.2950) train_loss 3.5828436689787817
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.1351), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.3431)]
fb, day 286 acc_test tensor(41.3498) train_loss 3.5961568046788672
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.4955), tensor(46.7509), tensor(42.1986), tensor(39.1304), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fb, day 287 acc_test tensor(41.3494) train_loss 3.61177430647777
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fb, day 288 acc_test tensor(41.3495) train_loss 3.598660544570919
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.4955), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.7080)]
fb, day 289 acc_test tensor(41.4040) train_loss 3.5929076191178
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.1304), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.3431)]
fb, day 290 acc_test tensor(41.3314) train_loss 3.6071285414935788
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.1304), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.7436), tensor(44.3431)]
fb, day 291 acc_test tensor(41.3131) train_loss 3.6054310124322315
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fb, day 292 acc_test tensor(41.3860) train_loss 3.6131616892199827
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.1304), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(39.7436), tensor(44.3431)]
fb, day 293 acc_test tensor(41.3313) train_loss 3.6060491497096696
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fb, day 294 acc_test tensor(41.3860) train_loss 3.617465470396787
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fb, day 295 acc_test tensor(41.3860) train_loss 3.617696922798155
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.1304), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fb, day 296 acc_test tensor(41.4039) train_loss 3.617881320715498
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.4955), tensor(46.7509), tensor(42.3759), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fb, day 297 acc_test tensor(41.4223) train_loss 3.6300427640457906
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.1304), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fb, day 298 acc_test tensor(41.3862) train_loss 3.613776443810961
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fb, day 299 acc_test tensor(41.3865) train_loss 3.64151509606535
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.1304), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.3431)]
fb, day 300 acc_test tensor(41.3857) train_loss 3.649513512410075
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fb, day 301 acc_test tensor(41.3865) train_loss 3.630162591534058
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.3153), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fb, day 302 acc_test tensor(41.3865) train_loss 3.626906773435018
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.4955), tensor(46.7509), tensor(42.1986), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fb, day 303 acc_test tensor(41.4223) train_loss 3.6358327421785117
test_semi_fb acc_test_lst [tensor(41.8149), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fb, day 304 acc_test tensor(41.4042) train_loss 3.6391282523204835
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fb, day 305 acc_test tensor(41.3855) train_loss 3.6481222880131976
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fb, day 306 acc_test tensor(41.4038) train_loss 3.634795212208502
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.3116), tensor(41.9708), tensor(40.0362), tensor(41.8312), tensor(40.1099), tensor(44.5255)]
fb, day 307 acc_test tensor(41.4220) train_loss 3.6567595851595796
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(40.1099), tensor(44.5255)]
fb, day 308 acc_test tensor(41.4217) train_loss 3.6545351863835753
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.1304), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fb, day 309 acc_test tensor(41.3673) train_loss 3.647330716751895
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fb, day 310 acc_test tensor(41.4036) train_loss 3.6599858779979426
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.1304), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.7436), tensor(44.5255)]
fb, day 311 acc_test tensor(41.3490) train_loss 3.647639489139057
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fb, day 312 acc_test tensor(41.4036) train_loss 3.642015733586468
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 313 acc_test tensor(41.4215) train_loss 3.655589742679224
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fb, day 314 acc_test tensor(41.4036) train_loss 3.6665925837431654
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 315 acc_test tensor(41.4215) train_loss 3.6716487726728038
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(41.8312), tensor(39.9267), tensor(44.5255)]
fb, day 316 acc_test tensor(41.4036) train_loss 3.666038193804497
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.3153), tensor(46.7509), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 317 acc_test tensor(41.4393) train_loss 3.670938719532349
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 318 acc_test tensor(41.4035) train_loss 3.681864821624622
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.3153), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 319 acc_test tensor(41.4035) train_loss 3.6710102004370744
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.3153), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.9708), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 320 acc_test tensor(41.4218) train_loss 3.6854187107603242
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.3153), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 321 acc_test tensor(41.4035) train_loss 3.694470085981986
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.3153), tensor(46.5704), tensor(42.3759), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 322 acc_test tensor(41.4213) train_loss 3.6987486235535427
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.3153), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.9708), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 323 acc_test tensor(41.4218) train_loss 3.7001845801571256
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.6757), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 324 acc_test tensor(41.4396) train_loss 3.6848860440707916
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 325 acc_test tensor(41.4216) train_loss 3.683461148489548
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 326 acc_test tensor(41.4216) train_loss 3.712545497226803
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 327 acc_test tensor(41.4216) train_loss 3.6911671113312714
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 328 acc_test tensor(41.4216) train_loss 3.714706752988602
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 329 acc_test tensor(41.4216) train_loss 3.701797548522297
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 330 acc_test tensor(41.4216) train_loss 3.721824549685181
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 331 acc_test tensor(41.4216) train_loss 3.724614805237376
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 332 acc_test tensor(41.4398) train_loss 3.730721190221825
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 333 acc_test tensor(41.4216) train_loss 3.718385823075475
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.6757), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 334 acc_test tensor(41.4578) train_loss 3.7398313002570855
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.8559), tensor(46.5704), tensor(42.1986), tensor(39.4928), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.5255)]
fb, day 335 acc_test tensor(41.4576) train_loss 3.7219872478597456
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 336 acc_test tensor(41.4217) train_loss 3.7402038659184917
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.6757), tensor(46.5704), tensor(42.1986), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 337 acc_test tensor(41.4397) train_loss 3.7288045707295514
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.4955), tensor(46.5704), tensor(42.0213), tensor(39.3116), tensor(41.7883), tensor(40.2174), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 338 acc_test tensor(41.4221) train_loss 3.7371417203881947
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.6757), tensor(46.5704), tensor(42.0213), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 339 acc_test tensor(41.4220) train_loss 3.746413017221721
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.6757), tensor(46.7509), tensor(42.0213), tensor(39.3116), tensor(41.7883), tensor(40.2174), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 340 acc_test tensor(41.4582) train_loss 3.7382682450013816
test_semi_fb acc_test_lst [tensor(42.1708), tensor(36.0360), tensor(46.5704), tensor(42.0213), tensor(39.3116), tensor(41.7883), tensor(40.0362), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 341 acc_test tensor(41.4580) train_loss 3.7454890428895826
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.6757), tensor(46.7509), tensor(42.0213), tensor(39.3116), tensor(41.7883), tensor(40.2174), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 342 acc_test tensor(41.4582) train_loss 3.7456987665400034
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.6757), tensor(46.7509), tensor(42.0213), tensor(39.3116), tensor(41.6058), tensor(40.2174), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 343 acc_test tensor(41.4399) train_loss 3.751583154463613
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.6757), tensor(46.7509), tensor(42.0213), tensor(39.3116), tensor(41.7883), tensor(40.2174), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 344 acc_test tensor(41.4582) train_loss 3.7527399932712764
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.8559), tensor(46.5704), tensor(42.0213), tensor(39.3116), tensor(41.7883), tensor(40.2174), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 345 acc_test tensor(41.4581) train_loss 3.7387669330827773
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.6757), tensor(46.5704), tensor(42.0213), tensor(39.3116), tensor(41.6058), tensor(40.2174), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 346 acc_test tensor(41.4219) train_loss 3.7442729700509947
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.6757), tensor(46.5704), tensor(42.0213), tensor(39.3116), tensor(41.7883), tensor(40.2174), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 347 acc_test tensor(41.4401) train_loss 3.739415241724882
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.6757), tensor(46.5704), tensor(42.0213), tensor(39.3116), tensor(41.6058), tensor(40.2174), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 348 acc_test tensor(41.4219) train_loss 3.7545693787848067
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.6757), tensor(46.5704), tensor(42.0213), tensor(39.3116), tensor(41.6058), tensor(40.2174), tensor(42.0108), tensor(39.9267), tensor(44.8905)]
fb, day 349 acc_test tensor(41.4401) train_loss 3.7727486110975805
test_semi_fb acc_test_lst [tensor(42.1708), tensor(35.8559), tensor(46.5704), tensor(42.0213), tensor(39.3116), tensor(41.7883), tensor(40.2174), tensor(42.0108), tensor(39.9267), tensor(44.7080)]
fb, day 350 acc_test tensor(41.4581) train_loss 3.781054635705059
test_semi_fb acc_test_lst [tensor(41.9929), tensor(35.6757), tensor(46.5704), tensor(42.0213), tensor(39.3116), tensor(41.7883), tensor(40.2174), tensor(42.0108), tensor(39.9267), tensor(44.8905)]
fb, day 351 acc_test tensor(41.4406) train_loss 3.772594421770261"""

pla_s = """test_semi_pla acc_test_lst [tensor(27.4021), tensor(28.4685), tensor(36.2816), tensor(34.9291), tensor(39.4928), tensor(41.2409), tensor(38.2246), tensor(40.3950), tensor(42.8571), tensor(44.5255)]
pla, day 0 acc_test tensor(37.3817) train_loss 1.9550167866511492
test_semi_pla acc_test_lst [tensor(35.9431), tensor(34.2342), tensor(41.3357), tensor(39.8936), tensor(42.7536), tensor(43.9781), tensor(41.3043), tensor(42.5494), tensor(42.8571), tensor(45.2555)]
pla, day 1 acc_test tensor(41.0105) train_loss 1.769954332504641
test_semi_pla acc_test_lst [tensor(37.1886), tensor(35.3153), tensor(42.4188), tensor(41.6667), tensor(44.7464), tensor(45.4380), tensor(42.3913), tensor(43.8061), tensor(43.4066), tensor(46.7153)]
pla, day 2 acc_test tensor(42.3093) train_loss 1.7335850618161817
test_semi_pla acc_test_lst [tensor(38.9680), tensor(35.8559), tensor(43.6823), tensor(43.7943), tensor(45.6522), tensor(46.1679), tensor(42.7536), tensor(44.5242), tensor(43.5897), tensor(47.0803)]
pla, day 3 acc_test tensor(43.2068) train_loss 1.7187303480619607
test_semi_pla acc_test_lst [tensor(40.7473), tensor(35.6757), tensor(46.0289), tensor(44.3262), tensor(45.6522), tensor(47.2628), tensor(43.8406), tensor(44.1652), tensor(43.7729), tensor(46.8978)]
pla, day 4 acc_test tensor(43.8370) train_loss 1.7036051233090104
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.2973), tensor(47.2924), tensor(44.3262), tensor(46.1957), tensor(47.4453), tensor(43.8406), tensor(44.7038), tensor(43.9560), tensor(47.2628)]
pla, day 5 acc_test tensor(44.3601) train_loss 1.694697996674045
test_semi_pla acc_test_lst [tensor(41.4591), tensor(38.0180), tensor(47.2924), tensor(44.6809), tensor(46.9203), tensor(47.6277), tensor(43.4783), tensor(44.8833), tensor(44.1392), tensor(47.9927)]
pla, day 6 acc_test tensor(44.6492) train_loss 1.6849875073432212
test_semi_pla acc_test_lst [tensor(41.1032), tensor(37.4775), tensor(47.6534), tensor(44.5035), tensor(46.9203), tensor(47.4453), tensor(44.2029), tensor(45.4219), tensor(44.3223), tensor(48.1752)]
pla, day 7 acc_test tensor(44.7226) train_loss 1.6784107839082274
test_semi_pla acc_test_lst [tensor(40.7473), tensor(37.4775), tensor(47.6534), tensor(44.5035), tensor(47.4638), tensor(48.1752), tensor(44.7464), tensor(45.6014), tensor(45.0549), tensor(48.3577)]
pla, day 8 acc_test tensor(44.9781) train_loss 1.6783725138923904
test_semi_pla acc_test_lst [tensor(40.3915), tensor(37.8378), tensor(48.0144), tensor(44.8582), tensor(48.0072), tensor(48.1752), tensor(44.7464), tensor(45.9605), tensor(44.5055), tensor(48.1752)]
pla, day 9 acc_test tensor(45.0672) train_loss 1.6734379067383094
test_semi_pla acc_test_lst [tensor(40.2135), tensor(38.1982), tensor(48.0144), tensor(44.6809), tensor(48.0072), tensor(48.1752), tensor(45.2899), tensor(46.3196), tensor(44.6886), tensor(48.1752)]
pla, day 10 acc_test tensor(45.1763) train_loss 1.6681598991095254
test_semi_pla acc_test_lst [tensor(40.7473), tensor(38.0180), tensor(48.5560), tensor(44.6809), tensor(48.1884), tensor(48.5401), tensor(45.2899), tensor(46.3196), tensor(44.5055), tensor(48.3577)]
pla, day 11 acc_test tensor(45.3203) train_loss 1.6672587051265588
test_semi_pla acc_test_lst [tensor(40.5694), tensor(38.0180), tensor(48.1949), tensor(44.5035), tensor(47.8261), tensor(48.5401), tensor(45.4710), tensor(46.6786), tensor(44.6886), tensor(48.5401)]
pla, day 12 acc_test tensor(45.3031) train_loss 1.663296511618238
test_semi_pla acc_test_lst [tensor(40.5694), tensor(38.3784), tensor(48.1949), tensor(44.5035), tensor(47.4638), tensor(48.5401), tensor(45.6522), tensor(46.3196), tensor(45.0549), tensor(48.9051)]
pla, day 13 acc_test tensor(45.3582) train_loss 1.6550681037390962
test_semi_pla acc_test_lst [tensor(40.7473), tensor(38.0180), tensor(48.0144), tensor(44.3262), tensor(47.4638), tensor(49.0876), tensor(45.4710), tensor(46.1400), tensor(45.4212), tensor(48.7226)]
pla, day 14 acc_test tensor(45.3412) train_loss 1.6614717219998176
test_semi_pla acc_test_lst [tensor(40.5694), tensor(37.6577), tensor(48.0144), tensor(44.5035), tensor(47.4638), tensor(49.4526), tensor(45.8333), tensor(46.4991), tensor(45.2381), tensor(48.9051)]
pla, day 15 acc_test tensor(45.4137) train_loss 1.651991608370595
test_semi_pla acc_test_lst [tensor(40.5694), tensor(37.6577), tensor(47.8339), tensor(44.6809), tensor(47.6449), tensor(49.4526), tensor(45.8333), tensor(46.4991), tensor(45.2381), tensor(48.7226)]
pla, day 16 acc_test tensor(45.4132) train_loss 1.6556492170606862
test_semi_pla acc_test_lst [tensor(40.5694), tensor(37.4775), tensor(47.8339), tensor(44.6809), tensor(48.5507), tensor(49.4526), tensor(45.6522), tensor(46.4991), tensor(45.2381), tensor(49.0876)]
pla, day 17 acc_test tensor(45.5042) train_loss 1.653833699573259
test_semi_pla acc_test_lst [tensor(40.5694), tensor(37.2973), tensor(48.3755), tensor(44.6809), tensor(48.5507), tensor(49.4526), tensor(45.6522), tensor(46.6786), tensor(45.0549), tensor(49.0876)]
pla, day 18 acc_test tensor(45.5400) train_loss 1.6463448099128442
test_semi_pla acc_test_lst [tensor(40.5694), tensor(37.4775), tensor(48.7365), tensor(45.0355), tensor(48.5507), tensor(49.4526), tensor(45.8333), tensor(47.0377), tensor(45.0549), tensor(48.9051)]
pla, day 19 acc_test tensor(45.6653) train_loss 1.6484174755179273
test_semi_pla acc_test_lst [tensor(40.3915), tensor(37.6577), tensor(48.5560), tensor(45.0355), tensor(48.3696), tensor(49.4526), tensor(45.6522), tensor(47.2172), tensor(45.0549), tensor(48.9051)]
pla, day 20 acc_test tensor(45.6292) train_loss 1.650042131968044
test_semi_pla acc_test_lst [tensor(40.3915), tensor(37.8378), tensor(49.0975), tensor(45.0355), tensor(48.5507), tensor(49.6350), tensor(45.8333), tensor(47.3968), tensor(45.0549), tensor(48.9051)]
pla, day 21 acc_test tensor(45.7738) train_loss 1.6468314488260516
test_semi_pla acc_test_lst [tensor(40.2135), tensor(37.8378), tensor(49.0975), tensor(45.0355), tensor(48.3696), tensor(49.6350), tensor(46.0145), tensor(47.2172), tensor(44.8718), tensor(49.0876)]
pla, day 22 acc_test tensor(45.7380) train_loss 1.6458008200423884
test_semi_pla acc_test_lst [tensor(40.0356), tensor(37.8378), tensor(48.9170), tensor(45.2128), tensor(48.3696), tensor(49.6350), tensor(46.3768), tensor(47.3968), tensor(44.8718), tensor(49.0876)]
pla, day 23 acc_test tensor(45.7741) train_loss 1.6435579420048052
test_semi_pla acc_test_lst [tensor(39.8577), tensor(38.1982), tensor(48.7365), tensor(45.2128), tensor(48.5507), tensor(49.6350), tensor(46.5580), tensor(47.0377), tensor(44.6886), tensor(48.9051)]
pla, day 24 acc_test tensor(45.7380) train_loss 1.6408307109070992
test_semi_pla acc_test_lst [tensor(39.8577), tensor(38.1982), tensor(48.7365), tensor(45.2128), tensor(48.5507), tensor(49.6350), tensor(46.7391), tensor(47.2172), tensor(44.6886), tensor(49.0876)]
pla, day 25 acc_test tensor(45.7923) train_loss 1.6426058632184892
test_semi_pla acc_test_lst [tensor(39.8577), tensor(38.0180), tensor(48.7365), tensor(45.5674), tensor(48.5507), tensor(49.4526), tensor(46.5580), tensor(47.2172), tensor(44.6886), tensor(49.0876)]
pla, day 26 acc_test tensor(45.7734) train_loss 1.6381744464647712
test_semi_pla acc_test_lst [tensor(39.6797), tensor(38.0180), tensor(48.7365), tensor(45.5674), tensor(48.5507), tensor(49.6350), tensor(46.9203), tensor(47.5763), tensor(44.6886), tensor(49.4526)]
pla, day 27 acc_test tensor(45.8825) train_loss 1.631323443815926
test_semi_pla acc_test_lst [tensor(39.8577), tensor(37.8378), tensor(49.0975), tensor(45.5674), tensor(48.5507), tensor(49.6350), tensor(47.1014), tensor(47.5763), tensor(44.6886), tensor(48.9051)]
pla, day 28 acc_test tensor(45.8818) train_loss 1.638523370232468
test_semi_pla acc_test_lst [tensor(39.8577), tensor(37.6577), tensor(48.9170), tensor(45.5674), tensor(48.5507), tensor(49.6350), tensor(47.2826), tensor(47.3968), tensor(44.8718), tensor(49.0876)]
pla, day 29 acc_test tensor(45.8824) train_loss 1.635882983997456
test_semi_pla acc_test_lst [tensor(39.8577), tensor(37.6577), tensor(48.9170), tensor(45.5674), tensor(48.5507), tensor(49.6350), tensor(47.1014), tensor(47.7558), tensor(44.8718), tensor(48.9051)]
pla, day 30 acc_test tensor(45.8820) train_loss 1.6388095449697244
test_semi_pla acc_test_lst [tensor(39.8577), tensor(37.8378), tensor(49.0975), tensor(45.5674), tensor(48.7319), tensor(49.6350), tensor(47.2826), tensor(47.7558), tensor(44.8718), tensor(49.0876)]
pla, day 31 acc_test tensor(45.9725) train_loss 1.6391127989044378
test_semi_pla acc_test_lst [tensor(39.8577), tensor(37.8378), tensor(49.0975), tensor(45.5674), tensor(48.7319), tensor(49.8175), tensor(47.1014), tensor(47.7558), tensor(44.8718), tensor(49.2701)]
pla, day 32 acc_test tensor(45.9909) train_loss 1.6365047010971394
test_semi_pla acc_test_lst [tensor(40.0356), tensor(37.6577), tensor(49.0975), tensor(45.3901), tensor(48.7319), tensor(49.8175), tensor(47.1014), tensor(47.7558), tensor(44.8718), tensor(48.9051)]
pla, day 33 acc_test tensor(45.9364) train_loss 1.6339809713805156
test_semi_pla acc_test_lst [tensor(40.0356), tensor(37.6577), tensor(48.9170), tensor(45.3901), tensor(48.7319), tensor(50.), tensor(47.1014), tensor(47.7558), tensor(44.8718), tensor(48.9051)]
pla, day 34 acc_test tensor(45.9366) train_loss 1.6319270084358033
test_semi_pla acc_test_lst [tensor(40.0356), tensor(37.4775), tensor(48.9170), tensor(45.3901), tensor(48.9130), tensor(49.8175), tensor(47.1014), tensor(47.9354), tensor(45.2381), tensor(49.2701)]
pla, day 35 acc_test tensor(46.0096) train_loss 1.6309226192621302
test_semi_pla acc_test_lst [tensor(40.0356), tensor(37.4775), tensor(49.0975), tensor(45.5674), tensor(48.9130), tensor(50.), tensor(46.9203), tensor(48.1149), tensor(45.2381), tensor(49.2701)]
pla, day 36 acc_test tensor(46.0634) train_loss 1.628582185466894
test_semi_pla acc_test_lst [tensor(40.2135), tensor(37.6577), tensor(49.0975), tensor(45.5674), tensor(48.9130), tensor(50.), tensor(47.2826), tensor(48.2944), tensor(45.2381), tensor(49.2701)]
pla, day 37 acc_test tensor(46.1534) train_loss 1.632447779061746
test_semi_pla acc_test_lst [tensor(40.2135), tensor(37.4775), tensor(49.0975), tensor(45.5674), tensor(48.9130), tensor(50.), tensor(47.2826), tensor(48.6535), tensor(45.0549), tensor(49.0876)]
pla, day 38 acc_test tensor(46.1348) train_loss 1.6288082211680008
test_semi_pla acc_test_lst [tensor(40.0356), tensor(37.2973), tensor(48.9170), tensor(45.5674), tensor(48.9130), tensor(49.8175), tensor(47.2826), tensor(48.8330), tensor(45.0549), tensor(49.4526)]
pla, day 39 acc_test tensor(46.1171) train_loss 1.6309047678132558
test_semi_pla acc_test_lst [tensor(40.0356), tensor(37.4775), tensor(48.9170), tensor(45.7447), tensor(48.9130), tensor(49.8175), tensor(47.1014), tensor(48.8330), tensor(45.0549), tensor(49.4526)]
pla, day 40 acc_test tensor(46.1347) train_loss 1.627205082435388
test_semi_pla acc_test_lst [tensor(40.2135), tensor(37.2973), tensor(48.9170), tensor(46.0993), tensor(48.9130), tensor(49.8175), tensor(47.1014), tensor(48.8330), tensor(45.0549), tensor(49.2701)]
pla, day 41 acc_test tensor(46.1517) train_loss 1.6262001844205543
test_semi_pla acc_test_lst [tensor(40.0356), tensor(37.1171), tensor(48.7365), tensor(46.0993), tensor(48.9130), tensor(49.8175), tensor(47.1014), tensor(48.8330), tensor(45.0549), tensor(49.2701)]
pla, day 42 acc_test tensor(46.0979) train_loss 1.629673230576137
test_semi_pla acc_test_lst [tensor(40.0356), tensor(36.9369), tensor(48.9170), tensor(45.9220), tensor(49.0942), tensor(49.8175), tensor(47.1014), tensor(49.0126), tensor(45.0549), tensor(49.2701)]
pla, day 43 acc_test tensor(46.1162) train_loss 1.6253019438936251
test_semi_pla acc_test_lst [tensor(40.0356), tensor(37.1171), tensor(49.0975), tensor(45.9220), tensor(49.0942), tensor(49.8175), tensor(47.1014), tensor(49.0126), tensor(45.0549), tensor(49.6350)]
pla, day 44 acc_test tensor(46.1888) train_loss 1.6309533336828839
test_semi_pla acc_test_lst [tensor(40.0356), tensor(37.1171), tensor(49.0975), tensor(46.0993), tensor(49.0942), tensor(50.), tensor(46.9203), tensor(49.1921), tensor(45.2381), tensor(49.6350)]
pla, day 45 acc_test tensor(46.2429) train_loss 1.6268063156954224
test_semi_pla acc_test_lst [tensor(40.2135), tensor(37.1171), tensor(49.0975), tensor(45.9220), tensor(49.0942), tensor(50.), tensor(46.9203), tensor(49.1921), tensor(45.4212), tensor(49.6350)]
pla, day 46 acc_test tensor(46.2613) train_loss 1.623052374793879
test_semi_pla acc_test_lst [tensor(39.8577), tensor(37.1171), tensor(49.0975), tensor(45.9220), tensor(49.0942), tensor(50.), tensor(46.9203), tensor(49.0126), tensor(45.4212), tensor(49.6350)]
pla, day 47 acc_test tensor(46.2078) train_loss 1.6280436508898206
test_semi_pla acc_test_lst [tensor(40.0356), tensor(37.1171), tensor(49.0975), tensor(45.9220), tensor(49.0942), tensor(50.), tensor(46.9203), tensor(49.3716), tensor(45.2381), tensor(49.8175)]
pla, day 48 acc_test tensor(46.2614) train_loss 1.6232305586254534
test_semi_pla acc_test_lst [tensor(40.2135), tensor(37.1171), tensor(49.0975), tensor(45.9220), tensor(48.9130), tensor(50.), tensor(46.9203), tensor(49.1921), tensor(45.4212), tensor(50.)]
pla, day 49 acc_test tensor(46.2797) train_loss 1.622423559178696
test_semi_pla acc_test_lst [tensor(40.3915), tensor(37.1171), tensor(49.0975), tensor(46.0993), tensor(49.0942), tensor(50.), tensor(46.9203), tensor(49.1921), tensor(45.4212), tensor(50.1825)]
pla, day 50 acc_test tensor(46.3516) train_loss 1.621062648941498
test_semi_pla acc_test_lst [tensor(40.3915), tensor(37.2973), tensor(49.0975), tensor(46.0993), tensor(49.0942), tensor(50.1825), tensor(47.1014), tensor(49.1921), tensor(45.6044), tensor(50.1825)]
pla, day 51 acc_test tensor(46.4243) train_loss 1.6251983711418578
test_semi_pla acc_test_lst [tensor(40.7473), tensor(37.2973), tensor(49.2780), tensor(46.0993), tensor(49.0942), tensor(50.1825), tensor(47.1014), tensor(49.1921), tensor(45.6044), tensor(50.1825)]
pla, day 52 acc_test tensor(46.4779) train_loss 1.625290153551856
test_semi_pla acc_test_lst [tensor(40.7473), tensor(37.2973), tensor(49.2780), tensor(46.4539), tensor(49.0942), tensor(50.1825), tensor(47.1014), tensor(49.1921), tensor(45.6044), tensor(50.1825)]
pla, day 53 acc_test tensor(46.5134) train_loss 1.6218194030996806
test_semi_pla acc_test_lst [tensor(40.9253), tensor(37.2973), tensor(49.2780), tensor(46.4539), tensor(49.0942), tensor(50.), tensor(47.1014), tensor(49.1921), tensor(45.6044), tensor(50.1825)]
pla, day 54 acc_test tensor(46.5129) train_loss 1.6208941910441197
test_semi_pla acc_test_lst [tensor(41.1032), tensor(37.2973), tensor(49.2780), tensor(46.6312), tensor(49.0942), tensor(50.), tensor(47.1014), tensor(49.3716), tensor(45.6044), tensor(50.1825)]
pla, day 55 acc_test tensor(46.5664) train_loss 1.6240149427220008
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.2973), tensor(49.0975), tensor(46.6312), tensor(49.0942), tensor(50.), tensor(47.1014), tensor(49.3716), tensor(45.6044), tensor(50.1825)]
pla, day 56 acc_test tensor(46.5661) train_loss 1.6242098263259752
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.2973), tensor(49.0975), tensor(46.6312), tensor(49.2754), tensor(50.), tensor(47.1014), tensor(49.0126), tensor(45.7875), tensor(50.)]
pla, day 57 acc_test tensor(46.5484) train_loss 1.621591794648274
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.2973), tensor(48.9170), tensor(46.9858), tensor(49.2754), tensor(50.), tensor(47.1014), tensor(49.0126), tensor(45.9707), tensor(50.1825)]
pla, day 58 acc_test tensor(46.6024) train_loss 1.621104265199388
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.2973), tensor(48.9170), tensor(46.9858), tensor(49.2754), tensor(50.), tensor(47.1014), tensor(49.0126), tensor(46.1538), tensor(50.1825)]
pla, day 59 acc_test tensor(46.6207) train_loss 1.6162379088560732
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.2973), tensor(48.7365), tensor(46.9858), tensor(49.4565), tensor(50.), tensor(47.1014), tensor(49.0126), tensor(46.1538), tensor(50.)]
pla, day 60 acc_test tensor(46.6025) train_loss 1.6151134518238217
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.2973), tensor(48.5560), tensor(47.1631), tensor(49.4565), tensor(50.), tensor(47.1014), tensor(49.0126), tensor(46.1538), tensor(50.)]
pla, day 61 acc_test tensor(46.6022) train_loss 1.619530502483829
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.2973), tensor(48.7365), tensor(47.1631), tensor(49.4565), tensor(50.), tensor(47.1014), tensor(49.0126), tensor(46.1538), tensor(50.)]
pla, day 62 acc_test tensor(46.6202) train_loss 1.619175888149648
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.2973), tensor(48.7365), tensor(47.1631), tensor(49.4565), tensor(50.), tensor(47.1014), tensor(49.0126), tensor(46.1538), tensor(49.8175)]
pla, day 63 acc_test tensor(46.6020) train_loss 1.617416322453327
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.1171), tensor(48.9170), tensor(47.1631), tensor(49.4565), tensor(50.), tensor(47.1014), tensor(48.8330), tensor(46.1538), tensor(49.8175)]
pla, day 64 acc_test tensor(46.5841) train_loss 1.6185422816011457
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.4775), tensor(48.9170), tensor(47.1631), tensor(49.6377), tensor(50.), tensor(47.1014), tensor(48.8330), tensor(46.1538), tensor(49.8175)]
pla, day 65 acc_test tensor(46.6382) train_loss 1.6128028826722332
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.4775), tensor(48.9170), tensor(47.1631), tensor(49.8188), tensor(50.), tensor(47.1014), tensor(49.0126), tensor(46.1538), tensor(50.)]
pla, day 66 acc_test tensor(46.6925) train_loss 1.6129360413476548
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.2973), tensor(49.0975), tensor(47.1631), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(48.6535), tensor(46.1538), tensor(49.8175)]
pla, day 67 acc_test tensor(46.6567) train_loss 1.6188638563444078
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.2973), tensor(49.0975), tensor(47.1631), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(49.0126), tensor(46.1538), tensor(49.6350)]
pla, day 68 acc_test tensor(46.6743) train_loss 1.6188129332581735
test_semi_pla acc_test_lst [tensor(41.2811), tensor(37.2973), tensor(49.0975), tensor(47.1631), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(48.8330), tensor(46.1538), tensor(49.8175)]
pla, day 69 acc_test tensor(46.6746) train_loss 1.6160162541923546
test_semi_pla acc_test_lst [tensor(41.4591), tensor(37.2973), tensor(49.0975), tensor(46.8085), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(49.0126), tensor(46.1538), tensor(50.)]
pla, day 70 acc_test tensor(46.6932) train_loss 1.6166567888830123
test_semi_pla acc_test_lst [tensor(41.4591), tensor(37.2973), tensor(49.0975), tensor(46.8085), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(48.8330), tensor(46.3370), tensor(49.8175)]
pla, day 71 acc_test tensor(46.6753) train_loss 1.6135138211875288
test_semi_pla acc_test_lst [tensor(41.6370), tensor(37.4775), tensor(49.0975), tensor(46.8085), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(49.0126), tensor(46.3370), tensor(49.8175)]
pla, day 72 acc_test tensor(46.7290) train_loss 1.6179854429240514
test_semi_pla acc_test_lst [tensor(41.6370), tensor(37.4775), tensor(49.0975), tensor(47.1631), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(49.0126), tensor(46.7033), tensor(49.6350)]
pla, day 73 acc_test tensor(46.7829) train_loss 1.6143492763809644
test_semi_pla acc_test_lst [tensor(41.6370), tensor(37.4775), tensor(49.2780), tensor(47.1631), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(49.0126), tensor(46.7033), tensor(49.6350)]
pla, day 74 acc_test tensor(46.8009) train_loss 1.6144650206506186
test_semi_pla acc_test_lst [tensor(41.6370), tensor(37.2973), tensor(49.2780), tensor(47.3404), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(49.0126), tensor(46.7033), tensor(49.6350)]
pla, day 75 acc_test tensor(46.8006) train_loss 1.6164697874048664
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.2973), tensor(49.2780), tensor(47.5177), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(49.0126), tensor(46.5201), tensor(49.8175)]
pla, day 76 acc_test tensor(46.8361) train_loss 1.613719317781318
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.2973), tensor(49.2780), tensor(47.5177), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(49.0126), tensor(46.5201), tensor(49.8175)]
pla, day 77 acc_test tensor(46.8539) train_loss 1.6131154562216727
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.2973), tensor(49.2780), tensor(47.6950), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(49.0126), tensor(46.7033), tensor(49.8175)]
pla, day 78 acc_test tensor(46.8899) train_loss 1.6046082082172015
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.2973), tensor(49.2780), tensor(47.6950), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(49.0126), tensor(46.7033), tensor(49.8175)]
pla, day 79 acc_test tensor(46.8899) train_loss 1.6108375072970516
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.2973), tensor(49.2780), tensor(47.6950), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(49.0126), tensor(46.8864), tensor(49.8175)]
pla, day 80 acc_test tensor(46.9083) train_loss 1.6130601448589386
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.2973), tensor(49.2780), tensor(47.6950), tensor(49.8188), tensor(50.1825), tensor(47.1014), tensor(49.0126), tensor(46.8864), tensor(49.8175)]
pla, day 81 acc_test tensor(46.9083) train_loss 1.6122301877305665
test_semi_pla acc_test_lst [tensor(42.1708), tensor(37.4775), tensor(49.2780), tensor(48.0496), tensor(50.), tensor(50.1825), tensor(47.1014), tensor(49.0126), tensor(46.8864), tensor(49.8175)]
pla, day 82 acc_test tensor(46.9976) train_loss 1.6155657307660178
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(49.2780), tensor(48.0496), tensor(50.), tensor(50.1825), tensor(47.4638), tensor(49.1921), tensor(46.8864), tensor(49.8175)]
pla, day 83 acc_test tensor(47.0340) train_loss 1.6112606451637737
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.6577), tensor(49.2780), tensor(48.0496), tensor(50.), tensor(50.1825), tensor(47.4638), tensor(49.1921), tensor(46.8864), tensor(50.)]
pla, day 84 acc_test tensor(47.0703) train_loss 1.609056800986642
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.6577), tensor(49.2780), tensor(48.0496), tensor(50.1812), tensor(50.3650), tensor(47.2826), tensor(49.1921), tensor(46.8864), tensor(50.)]
pla, day 85 acc_test tensor(47.0885) train_loss 1.6120498528300131
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.6577), tensor(49.4585), tensor(48.0496), tensor(50.1812), tensor(50.3650), tensor(47.2826), tensor(49.1921), tensor(46.8864), tensor(50.)]
pla, day 86 acc_test tensor(47.1066) train_loss 1.6128972975534845
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.8378), tensor(49.4585), tensor(48.2270), tensor(50.3623), tensor(50.5474), tensor(47.6449), tensor(49.1921), tensor(47.0696), tensor(50.)]
pla, day 87 acc_test tensor(47.2333) train_loss 1.6139139286280693
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.8378), tensor(49.4585), tensor(48.2270), tensor(50.3623), tensor(50.5474), tensor(47.6449), tensor(49.1921), tensor(47.0696), tensor(50.)]
pla, day 88 acc_test tensor(47.2333) train_loss 1.60788011267404
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.8378), tensor(49.4585), tensor(48.4043), tensor(50.3623), tensor(50.7299), tensor(47.4638), tensor(49.1921), tensor(47.0696), tensor(50.)]
pla, day 89 acc_test tensor(47.2511) train_loss 1.6129193160568565
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.8378), tensor(49.4585), tensor(48.4043), tensor(50.3623), tensor(50.7299), tensor(47.2826), tensor(49.1921), tensor(47.0696), tensor(50.)]
pla, day 90 acc_test tensor(47.2330) train_loss 1.6041650661036524
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.8378), tensor(49.4585), tensor(48.4043), tensor(50.3623), tensor(50.7299), tensor(47.4638), tensor(49.1921), tensor(47.0696), tensor(50.)]
pla, day 91 acc_test tensor(47.2511) train_loss 1.6073179082770919
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.8378), tensor(49.4585), tensor(48.5816), tensor(50.3623), tensor(50.7299), tensor(47.2826), tensor(49.1921), tensor(47.0696), tensor(50.)]
pla, day 92 acc_test tensor(47.2507) train_loss 1.6060487312436689
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.8378), tensor(49.4585), tensor(48.5816), tensor(50.3623), tensor(50.5474), tensor(47.2826), tensor(49.1921), tensor(47.0696), tensor(50.)]
pla, day 93 acc_test tensor(47.2325) train_loss 1.6087586546153452
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.8378), tensor(49.4585), tensor(48.5816), tensor(50.3623), tensor(50.7299), tensor(47.2826), tensor(49.1921), tensor(47.0696), tensor(50.)]
pla, day 94 acc_test tensor(47.2507) train_loss 1.6089157527115494
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.8378), tensor(49.4585), tensor(48.5816), tensor(50.5435), tensor(50.5474), tensor(47.2826), tensor(49.1921), tensor(47.0696), tensor(50.)]
pla, day 95 acc_test tensor(47.2506) train_loss 1.6059659872218686
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.8378), tensor(49.6390), tensor(48.5816), tensor(50.7246), tensor(50.7299), tensor(47.2826), tensor(49.1921), tensor(47.0696), tensor(50.)]
pla, day 96 acc_test tensor(47.3050) train_loss 1.6099193712813866
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.8378), tensor(49.6390), tensor(48.5816), tensor(50.7246), tensor(50.7299), tensor(47.6449), tensor(49.1921), tensor(47.0696), tensor(50.)]
pla, day 97 acc_test tensor(47.3412) train_loss 1.6092711766892052
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.6577), tensor(49.6390), tensor(48.5816), tensor(50.7246), tensor(50.7299), tensor(47.6449), tensor(49.1921), tensor(47.0696), tensor(50.)]
pla, day 98 acc_test tensor(47.3232) train_loss 1.6055195168141156
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.6577), tensor(49.4585), tensor(48.7589), tensor(50.7246), tensor(50.7299), tensor(47.6449), tensor(49.1921), tensor(47.2527), tensor(50.)]
pla, day 99 acc_test tensor(47.3412) train_loss 1.613024510307084
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.6577), tensor(49.6390), tensor(48.7589), tensor(50.7246), tensor(50.7299), tensor(47.6449), tensor(49.1921), tensor(47.2527), tensor(50.)]
pla, day 100 acc_test tensor(47.3593) train_loss 1.6067021836534414
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.6577), tensor(49.6390), tensor(48.7589), tensor(50.7246), tensor(50.7299), tensor(47.6449), tensor(49.1921), tensor(47.2527), tensor(49.8175)]
pla, day 101 acc_test tensor(47.3410) train_loss 1.6064214346533685
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.6577), tensor(49.8195), tensor(48.9362), tensor(50.7246), tensor(50.7299), tensor(47.4638), tensor(49.1921), tensor(47.4359), tensor(49.8175)]
pla, day 102 acc_test tensor(47.3770) train_loss 1.6047009737255329
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.6577), tensor(49.8195), tensor(48.7589), tensor(50.7246), tensor(50.7299), tensor(47.6449), tensor(49.1921), tensor(47.6190), tensor(50.)]
pla, day 103 acc_test tensor(47.4140) train_loss 1.6079261394475015
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.6577), tensor(49.8195), tensor(48.7589), tensor(50.7246), tensor(50.7299), tensor(47.6449), tensor(49.1921), tensor(47.6190), tensor(50.)]
pla, day 104 acc_test tensor(47.4140) train_loss 1.6049336527410163
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.6577), tensor(49.8195), tensor(48.9362), tensor(50.7246), tensor(50.7299), tensor(47.6449), tensor(49.1921), tensor(47.6190), tensor(50.)]
pla, day 105 acc_test tensor(47.4317) train_loss 1.605569402374779
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.6577), tensor(49.8195), tensor(48.9362), tensor(50.7246), tensor(50.7299), tensor(48.0072), tensor(49.1921), tensor(47.6190), tensor(50.)]
pla, day 106 acc_test tensor(47.4679) train_loss 1.6083406835391012
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(49.6390), tensor(48.9362), tensor(50.7246), tensor(50.7299), tensor(48.0072), tensor(49.1921), tensor(47.6190), tensor(50.)]
pla, day 107 acc_test tensor(47.4318) train_loss 1.607532367911898
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(49.6390), tensor(48.9362), tensor(50.5435), tensor(50.7299), tensor(48.0072), tensor(49.1921), tensor(47.6190), tensor(50.)]
pla, day 108 acc_test tensor(47.4137) train_loss 1.6004712915705264
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(49.6390), tensor(49.1135), tensor(50.7246), tensor(50.7299), tensor(48.0072), tensor(49.1921), tensor(47.6190), tensor(50.)]
pla, day 109 acc_test tensor(47.4496) train_loss 1.6107988600221268
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(49.8195), tensor(49.1135), tensor(50.5435), tensor(50.7299), tensor(48.0072), tensor(49.1921), tensor(47.6190), tensor(50.)]
pla, day 110 acc_test tensor(47.4495) train_loss 1.6019641586845481
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(49.8195), tensor(49.2908), tensor(50.5435), tensor(50.7299), tensor(48.0072), tensor(49.1921), tensor(47.6190), tensor(50.)]
pla, day 111 acc_test tensor(47.4672) train_loss 1.6032350757003824
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.), tensor(49.2908), tensor(50.7246), tensor(50.9124), tensor(48.0072), tensor(49.1921), tensor(47.2527), tensor(50.)]
pla, day 112 acc_test tensor(47.4850) train_loss 1.6039509534226521
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.1805), tensor(49.2908), tensor(50.7246), tensor(50.9124), tensor(48.0072), tensor(49.1921), tensor(47.2527), tensor(50.)]
pla, day 113 acc_test tensor(47.5031) train_loss 1.6026954301287786
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.1805), tensor(49.2908), tensor(50.7246), tensor(50.9124), tensor(48.0072), tensor(49.1921), tensor(47.2527), tensor(50.)]
pla, day 114 acc_test tensor(47.5031) train_loss 1.6039956187986086
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.), tensor(49.2908), tensor(50.7246), tensor(50.9124), tensor(48.0072), tensor(49.1921), tensor(47.4359), tensor(50.)]
pla, day 115 acc_test tensor(47.5033) train_loss 1.6045810734261337
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.3610), tensor(49.2908), tensor(50.7246), tensor(50.9124), tensor(48.0072), tensor(49.1921), tensor(47.4359), tensor(50.)]
pla, day 116 acc_test tensor(47.5394) train_loss 1.6025264546915525
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.5415), tensor(49.2908), tensor(50.7246), tensor(50.9124), tensor(48.0072), tensor(49.1921), tensor(47.4359), tensor(50.)]
pla, day 117 acc_test tensor(47.5575) train_loss 1.6039913098677905
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.3610), tensor(49.2908), tensor(50.7246), tensor(50.9124), tensor(48.1884), tensor(49.1921), tensor(47.4359), tensor(50.)]
pla, day 118 acc_test tensor(47.5576) train_loss 1.6069952076191256
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.5415), tensor(49.2908), tensor(50.7246), tensor(50.9124), tensor(48.1884), tensor(49.1921), tensor(47.4359), tensor(50.)]
pla, day 119 acc_test tensor(47.5756) train_loss 1.5993232980919858
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.5415), tensor(49.2908), tensor(50.7246), tensor(50.9124), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 120 acc_test tensor(47.6122) train_loss 1.6007878314991757
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.1805), tensor(49.2908), tensor(50.7246), tensor(50.9124), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 121 acc_test tensor(47.5761) train_loss 1.602191603729787
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.1805), tensor(49.2908), tensor(50.7246), tensor(50.9124), tensor(48.0072), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 122 acc_test tensor(47.5580) train_loss 1.607017441338468
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.1805), tensor(49.2908), tensor(50.7246), tensor(50.9124), tensor(48.1884), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 123 acc_test tensor(47.5944) train_loss 1.6038019053942427
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.1805), tensor(49.2908), tensor(50.7246), tensor(50.9124), tensor(48.1884), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 124 acc_test tensor(47.5944) train_loss 1.606875609671806
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.1805), tensor(49.2908), tensor(50.7246), tensor(50.9124), tensor(48.1884), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 125 acc_test tensor(47.5944) train_loss 1.6023222529544123
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.7246), tensor(50.9124), tensor(48.1884), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 126 acc_test tensor(47.6302) train_loss 1.6018771297820362
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.7246), tensor(50.9124), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 127 acc_test tensor(47.6119) train_loss 1.6021391561994813
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.2973), tensor(50.3610), tensor(49.4681), tensor(50.7246), tensor(50.9124), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 128 acc_test tensor(47.5938) train_loss 1.5995900914712775
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.2973), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(50.9124), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 129 acc_test tensor(47.6119) train_loss 1.602729990987315
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.2973), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(50.9124), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 130 acc_test tensor(47.6119) train_loss 1.601956934305037
test_semi_pla acc_test_lst [tensor(42.1708), tensor(37.2973), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.0949), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 131 acc_test tensor(47.6661) train_loss 1.598263929210812
test_semi_pla acc_test_lst [tensor(42.1708), tensor(37.2973), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.0949), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 132 acc_test tensor(47.6661) train_loss 1.60434868155195
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.0949), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 133 acc_test tensor(47.6663) train_loss 1.6023927873442398
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.0949), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 134 acc_test tensor(47.6663) train_loss 1.601842368575095
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.0949), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 135 acc_test tensor(47.6663) train_loss 1.6020050520645044
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.0949), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 136 acc_test tensor(47.6663) train_loss 1.5966862341342432
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.0949), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 137 acc_test tensor(47.6485) train_loss 1.605215608770042
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.0949), tensor(48.3696), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 138 acc_test tensor(47.6669) train_loss 1.6002239527157087
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.0949), tensor(48.3696), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 139 acc_test tensor(47.6669) train_loss 1.5994022607643326
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.0949), tensor(48.3696), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 140 acc_test tensor(47.6669) train_loss 1.598750739960464
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.2774), tensor(48.3696), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 141 acc_test tensor(47.6851) train_loss 1.6036464363776557
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.2774), tensor(48.3696), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 142 acc_test tensor(47.6851) train_loss 1.5956376665805734
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.2774), tensor(48.3696), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 143 acc_test tensor(47.6851) train_loss 1.594760619207044
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.2774), tensor(48.3696), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 144 acc_test tensor(47.6851) train_loss 1.5989830455168093
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.4775), tensor(50.3610), tensor(49.4681), tensor(50.9058), tensor(51.2774), tensor(48.3696), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 145 acc_test tensor(47.6851) train_loss 1.6025083650351961
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.4775), tensor(50.7220), tensor(49.4681), tensor(50.9058), tensor(51.2774), tensor(48.3696), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 146 acc_test tensor(47.7212) train_loss 1.5952305369738462
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.4775), tensor(50.7220), tensor(49.4681), tensor(50.9058), tensor(51.2774), tensor(48.3696), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 147 acc_test tensor(47.7212) train_loss 1.5950076236730817
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.6577), tensor(50.5415), tensor(49.4681), tensor(50.9058), tensor(51.2774), tensor(48.3696), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 148 acc_test tensor(47.7212) train_loss 1.6050707808423288
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.6577), tensor(50.9025), tensor(49.4681), tensor(50.7246), tensor(51.2774), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 149 acc_test tensor(47.7208) train_loss 1.6009476123268427
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.6577), tensor(50.5415), tensor(49.4681), tensor(50.7246), tensor(51.2774), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 150 acc_test tensor(47.6847) train_loss 1.5952429597025155
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.6577), tensor(50.7220), tensor(49.4681), tensor(50.7246), tensor(51.2774), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 151 acc_test tensor(47.7209) train_loss 1.6017680455575185
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.8378), tensor(50.7220), tensor(49.6454), tensor(50.7246), tensor(51.2774), tensor(48.9130), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 152 acc_test tensor(47.7929) train_loss 1.5988810483721536
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.8378), tensor(50.7220), tensor(49.6454), tensor(50.7246), tensor(51.2774), tensor(48.9130), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 153 acc_test tensor(47.7929) train_loss 1.59660157116635
test_semi_pla acc_test_lst [tensor(41.8149), tensor(37.8378), tensor(50.7220), tensor(49.6454), tensor(50.7246), tensor(51.2774), tensor(48.9130), tensor(49.1921), tensor(47.8022), tensor(50.1825)]
pla, day 154 acc_test tensor(47.8112) train_loss 1.5978789483207334
test_semi_pla acc_test_lst [tensor(41.9929), tensor(37.8378), tensor(50.7220), tensor(49.8227), tensor(50.7246), tensor(51.2774), tensor(48.9130), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 155 acc_test tensor(47.8284) train_loss 1.595509543440454
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.7220), tensor(49.8227), tensor(50.7246), tensor(51.2774), tensor(48.9130), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 156 acc_test tensor(47.8642) train_loss 1.5947772358657721
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.7220), tensor(49.8227), tensor(50.7246), tensor(51.2774), tensor(48.7319), tensor(49.0126), tensor(47.6190), tensor(50.1825)]
pla, day 157 acc_test tensor(47.8104) train_loss 1.59662743537761
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.7220), tensor(49.8227), tensor(50.5435), tensor(51.4599), tensor(48.9130), tensor(49.0126), tensor(47.6190), tensor(50.1825)]
pla, day 158 acc_test tensor(47.8286) train_loss 1.5901094203867259
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.7220), tensor(49.8227), tensor(50.5435), tensor(51.0949), tensor(48.9130), tensor(49.0126), tensor(47.6190), tensor(50.1825)]
pla, day 159 acc_test tensor(47.7921) train_loss 1.5961305226232665
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.7220), tensor(49.8227), tensor(50.5435), tensor(51.2774), tensor(48.9130), tensor(49.0126), tensor(47.6190), tensor(50.1825)]
pla, day 160 acc_test tensor(47.8104) train_loss 1.593189967677158
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.7220), tensor(49.8227), tensor(50.5435), tensor(51.2774), tensor(48.7319), tensor(49.0126), tensor(47.6190), tensor(50.1825)]
pla, day 161 acc_test tensor(47.7922) train_loss 1.6007839703969033
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.7220), tensor(49.8227), tensor(50.5435), tensor(51.2774), tensor(48.9130), tensor(49.0126), tensor(47.6190), tensor(50.)]
pla, day 162 acc_test tensor(47.7921) train_loss 1.5937395984422909
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.7220), tensor(49.8227), tensor(50.5435), tensor(51.2774), tensor(48.7319), tensor(49.0126), tensor(47.6190), tensor(50.)]
pla, day 163 acc_test tensor(47.7740) train_loss 1.5977300235790601
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.7220), tensor(49.8227), tensor(50.5435), tensor(51.2774), tensor(48.7319), tensor(49.0126), tensor(47.6190), tensor(50.)]
pla, day 164 acc_test tensor(47.7740) train_loss 1.5982102641786409
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.2774), tensor(48.7319), tensor(49.0126), tensor(47.6190), tensor(50.)]
pla, day 165 acc_test tensor(47.7920) train_loss 1.5959029507712494
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.2774), tensor(48.7319), tensor(49.0126), tensor(47.6190), tensor(50.)]
pla, day 166 acc_test tensor(47.7920) train_loss 1.5986558294401747
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.2774), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
pla, day 167 acc_test tensor(47.7741) train_loss 1.5979086230306156
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
pla, day 168 acc_test tensor(47.7923) train_loss 1.5958803203311218
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
pla, day 169 acc_test tensor(47.7923) train_loss 1.5936620613028898
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
pla, day 170 acc_test tensor(47.7923) train_loss 1.594587805740897
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
pla, day 171 acc_test tensor(47.7923) train_loss 1.5958570503432126
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
pla, day 172 acc_test tensor(47.7923) train_loss 1.5977036108774039
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.4599), tensor(48.5507), tensor(48.8330), tensor(47.6190), tensor(50.)]
pla, day 173 acc_test tensor(47.7742) train_loss 1.5926709310471614
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.4599), tensor(48.5507), tensor(48.8330), tensor(47.6190), tensor(50.)]
pla, day 174 acc_test tensor(47.7742) train_loss 1.5895578895494662
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.4599), tensor(48.5507), tensor(48.8330), tensor(47.6190), tensor(49.8175)]
pla, day 175 acc_test tensor(47.7560) train_loss 1.5929665906630093
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(49.8175)]
pla, day 176 acc_test tensor(47.7741) train_loss 1.5969525845293295
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(49.8175)]
pla, day 177 acc_test tensor(47.7741) train_loss 1.5956501023596785
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
pla, day 178 acc_test tensor(47.8279) train_loss 1.5998082530375632
test_semi_pla acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
pla, day 179 acc_test tensor(47.7923) train_loss 1.5908006057965742
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
pla, day 180 acc_test tensor(47.8101) train_loss 1.5923973135009606
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
pla, day 181 acc_test tensor(47.8279) train_loss 1.5891584546576158
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
pla, day 182 acc_test tensor(47.8279) train_loss 1.603917001608237
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
pla, day 183 acc_test tensor(47.8279) train_loss 1.5903481313200103
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.), tensor(50.5435), tensor(51.4599), tensor(48.5507), tensor(48.8330), tensor(47.4359), tensor(50.1825)]
pla, day 184 acc_test tensor(47.8097) train_loss 1.5924123435073534
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.), tensor(50.7246), tensor(51.4599), tensor(48.5507), tensor(48.8330), tensor(47.4359), tensor(50.1825)]
pla, day 185 acc_test tensor(47.8278) train_loss 1.596959365891851
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.), tensor(50.9058), tensor(51.4599), tensor(48.5507), tensor(48.8330), tensor(47.4359), tensor(50.1825)]
pla, day 186 acc_test tensor(47.8459) train_loss 1.5916568162732012
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.), tensor(50.9058), tensor(51.4599), tensor(48.5507), tensor(48.8330), tensor(47.4359), tensor(50.)]
pla, day 187 acc_test tensor(47.8277) train_loss 1.591077888827138
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.), tensor(50.9058), tensor(51.4599), tensor(48.5507), tensor(49.0126), tensor(47.4359), tensor(50.)]
pla, day 188 acc_test tensor(47.8456) train_loss 1.5967656996098984
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.5507), tensor(49.0126), tensor(47.2527), tensor(50.1825)]
pla, day 189 acc_test tensor(47.8633) train_loss 1.596230267090215
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.5507), tensor(49.0126), tensor(47.4359), tensor(50.1825)]
pla, day 190 acc_test tensor(47.8816) train_loss 1.588920657990542
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.7319), tensor(49.1921), tensor(47.4359), tensor(50.1825)]
pla, day 191 acc_test tensor(47.9177) train_loss 1.5964059826630725
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.7319), tensor(49.1921), tensor(47.4359), tensor(50.1825)]
pla, day 192 acc_test tensor(47.9177) train_loss 1.593136237241773
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.7319), tensor(49.1921), tensor(47.4359), tensor(50.1825)]
pla, day 193 acc_test tensor(47.9177) train_loss 1.5957601914911865
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.3546), tensor(50.9058), tensor(51.4599), tensor(48.7319), tensor(49.1921), tensor(47.4359), tensor(50.1825)]
pla, day 194 acc_test tensor(47.9354) train_loss 1.5961909824112666
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.7319), tensor(49.1921), tensor(47.4359), tensor(50.1825)]
pla, day 195 acc_test tensor(47.9177) train_loss 1.5959546355822978
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.7319), tensor(49.1921), tensor(47.4359), tensor(50.1825)]
pla, day 196 acc_test tensor(47.9177) train_loss 1.5884927932802386
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.7319), tensor(49.1921), tensor(47.4359), tensor(50.1825)]
pla, day 197 acc_test tensor(47.9177) train_loss 1.5920246040862753
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.7319), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 198 acc_test tensor(47.9360) train_loss 1.5921481027928224
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 199 acc_test tensor(47.9179) train_loss 1.5896113561725371
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 200 acc_test tensor(47.9357) train_loss 1.5937926897870207
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.7319), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 201 acc_test tensor(47.9360) train_loss 1.5890535857301336
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.1825)]
pla, day 202 acc_test tensor(47.9357) train_loss 1.5949730760789438
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.7319), tensor(49.1921), tensor(47.6190), tensor(50.3650)]
pla, day 203 acc_test tensor(47.9720) train_loss 1.5935120154138767
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.3650)]
pla, day 204 acc_test tensor(47.9539) train_loss 1.590138206149901
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.4599), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.3650)]
pla, day 205 acc_test tensor(47.9539) train_loss 1.594555402703187
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.3650)]
pla, day 206 acc_test tensor(47.9722) train_loss 1.5920598979983793
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 207 acc_test tensor(47.9904) train_loss 1.5916359253605865
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 208 acc_test tensor(47.9904) train_loss 1.5913688504763253
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 209 acc_test tensor(47.9904) train_loss 1.5927015838969603
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 210 acc_test tensor(47.9904) train_loss 1.588033473543675
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 211 acc_test tensor(48.0084) train_loss 1.593231837594348
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 212 acc_test tensor(47.9906) train_loss 1.598906749307539
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 213 acc_test tensor(47.9906) train_loss 1.5928121888346525
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 214 acc_test tensor(47.9906) train_loss 1.5912095691316923
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 215 acc_test tensor(48.0084) train_loss 1.5878782508667708
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 216 acc_test tensor(48.0084) train_loss 1.5881577147008386
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 217 acc_test tensor(48.0084) train_loss 1.5915077751796636
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 218 acc_test tensor(47.9906) train_loss 1.595777935175696
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 219 acc_test tensor(47.9906) train_loss 1.590435164078325
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.6423), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 220 acc_test tensor(48.0084) train_loss 1.5926231871294894
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.8248), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 221 acc_test tensor(48.0267) train_loss 1.5920759891199896
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(50.9058), tensor(51.8248), tensor(48.5507), tensor(49.1921), tensor(47.6190), tensor(50.5474)]
pla, day 222 acc_test tensor(48.0267) train_loss 1.5908915379643809
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(51.0870), tensor(52.0073), tensor(48.5507), tensor(49.1921), tensor(47.4359), tensor(50.5474)]
pla, day 223 acc_test tensor(48.0269) train_loss 1.5931090598191704
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(51.0870), tensor(52.0073), tensor(48.5507), tensor(49.1921), tensor(47.4359), tensor(50.5474)]
pla, day 224 acc_test tensor(48.0269) train_loss 1.5902531360276664
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(51.2681), tensor(52.0073), tensor(48.5507), tensor(49.1921), tensor(47.4359), tensor(50.5474)]
pla, day 225 acc_test tensor(48.0628) train_loss 1.587977383848057
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(51.2681), tensor(52.0073), tensor(48.5507), tensor(49.1921), tensor(47.4359), tensor(50.5474)]
pla, day 226 acc_test tensor(48.0628) train_loss 1.5899901509880854
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(50.7299)]
pla, day 227 acc_test tensor(48.0630) train_loss 1.5937259349665291
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.1773), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(50.7299)]
pla, day 228 acc_test tensor(48.0630) train_loss 1.5908183110683973
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(50.9124)]
pla, day 229 acc_test tensor(48.0635) train_loss 1.5910497950485303
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.1884), tensor(49.1921), tensor(47.4359), tensor(50.9124)]
pla, day 230 acc_test tensor(48.0454) train_loss 1.5876827461941556
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.), tensor(51.0870), tensor(52.0073), tensor(48.1884), tensor(49.1921), tensor(47.4359), tensor(50.9124)]
pla, day 231 acc_test tensor(48.0273) train_loss 1.5845367966867756
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.1884), tensor(49.1921), tensor(47.4359), tensor(50.9124)]
pla, day 232 acc_test tensor(48.0454) train_loss 1.5875881961901412
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.1884), tensor(49.1921), tensor(47.4359), tensor(50.9124)]
pla, day 233 acc_test tensor(48.0454) train_loss 1.5889660714568064
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.1884), tensor(49.1921), tensor(47.4359), tensor(50.9124)]
pla, day 234 acc_test tensor(48.0454) train_loss 1.5946245191532253
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(50.7299)]
pla, day 235 acc_test tensor(48.0452) train_loss 1.5896747792412902
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 236 acc_test tensor(48.0817) train_loss 1.5899783611348803
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(50.9124)]
pla, day 237 acc_test tensor(48.0635) train_loss 1.5902407066411017
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 238 acc_test tensor(48.0817) train_loss 1.59545425699298
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 239 acc_test tensor(48.0817) train_loss 1.5891802112951898
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(50.9025), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 240 acc_test tensor(48.0817) train_loss 1.587008518910898
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 241 acc_test tensor(48.0998) train_loss 1.5858498620307986
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(50.9124)]
pla, day 242 acc_test tensor(48.0815) train_loss 1.5900794787384553
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(50.9124)]
pla, day 243 acc_test tensor(48.0815) train_loss 1.5863664926861158
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 244 acc_test tensor(48.0818) train_loss 1.5957988538232393
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 245 acc_test tensor(48.0818) train_loss 1.582738272595828
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 246 acc_test tensor(48.0818) train_loss 1.5896404617923394
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 247 acc_test tensor(48.0818) train_loss 1.5957738273898847
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 248 acc_test tensor(48.0818) train_loss 1.5863970699161312
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 249 acc_test tensor(48.0818) train_loss 1.5875381014360201
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 250 acc_test tensor(48.0818) train_loss 1.586538144368131
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 251 acc_test tensor(48.0818) train_loss 1.586659860742555
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 252 acc_test tensor(48.0998) train_loss 1.5918304053065486
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 253 acc_test tensor(48.1178) train_loss 1.5901448713782964
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 254 acc_test tensor(48.1178) train_loss 1.58757943811376
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 255 acc_test tensor(48.1178) train_loss 1.5902401959153358
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(50.9124)]
pla, day 256 acc_test tensor(48.0996) train_loss 1.5850276269935417
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 257 acc_test tensor(48.1178) train_loss 1.5901410287685147
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(50.9124)]
pla, day 258 acc_test tensor(48.0996) train_loss 1.5880997201064648
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.3784), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 259 acc_test tensor(48.1359) train_loss 1.588784745748422
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.3784), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 260 acc_test tensor(48.1359) train_loss 1.5948564111168273
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.3784), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 261 acc_test tensor(48.1359) train_loss 1.5866445445470956
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.3784), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 262 acc_test tensor(48.1359) train_loss 1.5885026916163563
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.3784), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 263 acc_test tensor(48.1359) train_loss 1.5873648008785175
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 264 acc_test tensor(48.1178) train_loss 1.5888453647987928
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 265 acc_test tensor(48.1181) train_loss 1.5889473109129115
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 266 acc_test tensor(48.0998) train_loss 1.5842015505497882
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 267 acc_test tensor(48.0998) train_loss 1.5877378865067369
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 268 acc_test tensor(48.0998) train_loss 1.584440310282748
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.4359), tensor(51.0949)]
pla, day 269 acc_test tensor(48.1181) train_loss 1.5859237451200228
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 270 acc_test tensor(48.1364) train_loss 1.580820480314215
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 271 acc_test tensor(48.1181) train_loss 1.5833484856537288
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 272 acc_test tensor(48.1364) train_loss 1.5861274008903279
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 273 acc_test tensor(48.1364) train_loss 1.5920518054675887
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 274 acc_test tensor(48.1544) train_loss 1.582572837676695
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 275 acc_test tensor(48.1544) train_loss 1.5850136357659559
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 276 acc_test tensor(48.1544) train_loss 1.5800705035720177
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.2635), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 277 acc_test tensor(48.1364) train_loss 1.5845012827178357
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 278 acc_test tensor(48.1183) train_loss 1.586839179025647
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 279 acc_test tensor(48.1363) train_loss 1.5827649530965104
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 280 acc_test tensor(48.1363) train_loss 1.5894213950562406
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 281 acc_test tensor(48.1365) train_loss 1.5890802848873333
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 282 acc_test tensor(48.1365) train_loss 1.585727140232421
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 283 acc_test tensor(48.1365) train_loss 1.5873651766876877
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 284 acc_test tensor(48.1546) train_loss 1.5848370251020247
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 285 acc_test tensor(48.1723) train_loss 1.5773561252479333
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 286 acc_test tensor(48.1723) train_loss 1.5843323262907736
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.1982), tensor(51.2635), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 287 acc_test tensor(48.1726) train_loss 1.5862185370695503
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.1982), tensor(51.2635), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 288 acc_test tensor(48.1726) train_loss 1.5881252969209751
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 289 acc_test tensor(48.1721) train_loss 1.5853976124917164
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.1982), tensor(51.2635), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 290 acc_test tensor(48.1543) train_loss 1.5866247168334677
test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.1982), tensor(51.2635), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 291 acc_test tensor(48.1726) train_loss 1.5853783182993268
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 292 acc_test tensor(48.1723) train_loss 1.5866976358960616
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 293 acc_test tensor(48.1904) train_loss 1.5856370591727054
test_semi_pla acc_test_lst [tensor(42.5267), tensor(38.1982), tensor(51.2635), tensor(50.1773), tensor(51.2681), tensor(52.0073), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 294 acc_test tensor(48.1899) train_loss 1.5870830406989185
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.1773), tensor(51.2681), tensor(52.0073), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 295 acc_test tensor(48.1540) train_loss 1.5861956306888514
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.1773), tensor(51.2681), tensor(52.0073), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 296 acc_test tensor(48.1540) train_loss 1.583892339559978
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.1773), tensor(51.2681), tensor(52.0073), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 297 acc_test tensor(48.1540) train_loss 1.5850110008686704
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.1773), tensor(51.2681), tensor(52.0073), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 298 acc_test tensor(48.1540) train_loss 1.5833842336118318
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.2635), tensor(50.1773), tensor(51.2681), tensor(52.0073), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 299 acc_test tensor(48.1358) train_loss 1.5901434905531036
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.0073), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.0949)]
pla, day 300 acc_test tensor(48.1177) train_loss 1.5852324024126343
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.0073), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 301 acc_test tensor(48.1360) train_loss 1.5848619050427863
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.0073), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 302 acc_test tensor(48.1360) train_loss 1.5863841073536817
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.6423)]
pla, day 303 acc_test tensor(48.1907) train_loss 1.5840174772202387
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.6423)]
pla, day 304 acc_test tensor(48.1907) train_loss 1.5882214812725965
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.6423)]
pla, day 305 acc_test tensor(48.1907) train_loss 1.584659614405316
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.4599)]
pla, day 306 acc_test tensor(48.1725) train_loss 1.58460141324858
test_semi_pla acc_test_lst [tensor(42.5267), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.4599)]
pla, day 307 acc_test tensor(48.1903) train_loss 1.5846558535337687
test_semi_pla acc_test_lst [tensor(42.3488), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.4599)]
pla, day 308 acc_test tensor(48.1725) train_loss 1.5856077239202893
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.4599)]
pla, day 309 acc_test tensor(48.2080) train_loss 1.5847087677674836
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.4599)]
pla, day 310 acc_test tensor(48.2262) train_loss 1.5823076546444397
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.4599)]
pla, day 311 acc_test tensor(48.2080) train_loss 1.5836398869777404
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.1982), tensor(51.0830), tensor(50.1773), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.4599)]
pla, day 312 acc_test tensor(48.2080) train_loss 1.5861247414966195
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.1982), tensor(50.9025), tensor(50.3546), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.6423)]
pla, day 313 acc_test tensor(48.2260) train_loss 1.5852306329759318
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.1982), tensor(50.9025), tensor(50.3546), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.6423)]
pla, day 314 acc_test tensor(48.2260) train_loss 1.5841171219757404
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.1982), tensor(50.9025), tensor(50.3546), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.6423)]
pla, day 315 acc_test tensor(48.2260) train_loss 1.583990626083422
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.1982), tensor(50.9025), tensor(50.3546), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.4599)]
pla, day 316 acc_test tensor(48.2258) train_loss 1.5865547295407358
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.1982), tensor(50.9025), tensor(50.3546), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.6423)]
pla, day 317 acc_test tensor(48.2260) train_loss 1.584162694515255
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.1982), tensor(50.9025), tensor(50.3546), tensor(51.2681), tensor(52.1898), tensor(48.1884), tensor(49.1921), tensor(47.6190), tensor(51.4599)]
pla, day 318 acc_test tensor(48.2077) train_loss 1.5853976340648086
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.1982), tensor(50.9025), tensor(50.3546), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.4599)]
pla, day 319 acc_test tensor(48.2258) train_loss 1.5858943592218653
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.1982), tensor(50.9025), tensor(50.3546), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 320 acc_test tensor(48.2076) train_loss 1.5808701145941817
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.0180), tensor(50.9025), tensor(50.3546), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 321 acc_test tensor(48.1896) train_loss 1.5867889865586247
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.1982), tensor(50.9025), tensor(50.3546), tensor(51.2681), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 322 acc_test tensor(48.2076) train_loss 1.5839685404521848
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.0180), tensor(50.9025), tensor(50.3546), tensor(51.4493), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.4599)]
pla, day 323 acc_test tensor(48.2259) train_loss 1.5903179342516
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.0180), tensor(50.9025), tensor(50.3546), tensor(51.4493), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 324 acc_test tensor(48.2077) train_loss 1.5819127998376425
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.0180), tensor(50.9025), tensor(50.3546), tensor(51.4493), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.2774)]
pla, day 325 acc_test tensor(48.2077) train_loss 1.580450475084479
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.0180), tensor(50.9025), tensor(50.3546), tensor(51.4493), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.6190), tensor(51.4599)]
pla, day 326 acc_test tensor(48.2259) train_loss 1.5835578111127089
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.0180), tensor(50.9025), tensor(50.3546), tensor(51.4493), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.8022), tensor(51.4599)]
pla, day 327 acc_test tensor(48.2443) train_loss 1.5861726609139388
test_semi_pla acc_test_lst [tensor(42.7046), tensor(38.0180), tensor(50.9025), tensor(50.3546), tensor(51.4493), tensor(52.1898), tensor(48.3696), tensor(49.1921), tensor(47.8022), tensor(51.4599)]
pla, day 328 acc_test tensor(48.2443) train_loss 1.5862085389160223"""

sep_s = """sep, group_id 9 acc_test_lst [tensor(27.4021), tensor(28.4685), tensor(36.2816), tensor(34.9291), tensor(39.4928), tensor(41.2409), tensor(38.2246), tensor(40.3950), tensor(42.8571), tensor(44.5255)]
sep, day 0 acc_test tensor(37.3817) train_loss 1.9550167866511492
sep, group_id 9 acc_test_lst [tensor(30.0712), tensor(30.6306), tensor(37.1841), tensor(36.7021), tensor(41.6667), tensor(41.6058), tensor(40.3986), tensor(41.8312), tensor(41.3919), tensor(43.6131)]
sep, day 1 acc_test tensor(38.5095) train_loss 1.8597009533990618
sep, group_id 9 acc_test_lst [tensor(31.1388), tensor(30.2703), tensor(37.9061), tensor(38.4752), tensor(42.9348), tensor(43.4307), tensor(41.8478), tensor(41.8312), tensor(41.3919), tensor(45.0730)]
sep, day 2 acc_test tensor(39.4300) train_loss 1.807562793874023
sep, group_id 9 acc_test_lst [tensor(32.5623), tensor(31.3514), tensor(40.4332), tensor(39.0071), tensor(42.2101), tensor(43.9781), tensor(41.1232), tensor(40.9336), tensor(42.8571), tensor(46.7153)]
sep, day 3 acc_test tensor(40.1171) train_loss 1.7681222064652962
sep, group_id 9 acc_test_lst [tensor(33.0961), tensor(31.7117), tensor(39.7112), tensor(40.9574), tensor(43.8406), tensor(43.7956), tensor(42.0290), tensor(41.4722), tensor(42.3077), tensor(47.0803)]
sep, day 4 acc_test tensor(40.6002) train_loss 1.7388962825116883
sep, group_id 9 acc_test_lst [tensor(32.7402), tensor(32.0721), tensor(38.9892), tensor(41.6667), tensor(44.3841), tensor(44.7080), tensor(43.1159), tensor(41.2926), tensor(42.4908), tensor(45.9854)]
sep, day 5 acc_test tensor(40.7445) train_loss 1.7129250577704729
sep, group_id 9 acc_test_lst [tensor(33.6299), tensor(32.9730), tensor(42.0578), tensor(41.6667), tensor(45.4710), tensor(45.8029), tensor(43.6594), tensor(42.0108), tensor(43.0403), tensor(46.5328)]
sep, day 6 acc_test tensor(41.6845) train_loss 1.687003265708944
sep, group_id 9 acc_test_lst [tensor(34.8754), tensor(34.5946), tensor(41.8773), tensor(41.6667), tensor(45.6522), tensor(44.8905), tensor(45.1087), tensor(43.0880), tensor(42.6740), tensor(45.9854)]
sep, day 7 acc_test tensor(42.0413) train_loss 1.6663782871850668
sep, group_id 9 acc_test_lst [tensor(35.0534), tensor(34.5946), tensor(41.5162), tensor(42.3759), tensor(46.0145), tensor(45.8029), tensor(44.0217), tensor(42.7289), tensor(42.8571), tensor(47.0803)]
sep, day 8 acc_test tensor(42.2046) train_loss 1.650115255530871
sep, group_id 9 acc_test_lst [tensor(35.9431), tensor(33.8739), tensor(42.9603), tensor(42.5532), tensor(45.4710), tensor(47.2628), tensor(44.5652), tensor(42.0108), tensor(42.4908), tensor(46.8978)]
sep, day 9 acc_test tensor(42.4029) train_loss 1.632218060509272
sep, group_id 9 acc_test_lst [tensor(36.4769), tensor(35.3153), tensor(43.8628), tensor(43.4397), tensor(45.2899), tensor(47.0803), tensor(45.6522), tensor(43.6266), tensor(43.2234), tensor(46.3504)]
sep, day 10 acc_test tensor(43.0317) train_loss 1.6142830066601177
sep, group_id 9 acc_test_lst [tensor(36.1210), tensor(35.8559), tensor(43.5018), tensor(44.3262), tensor(47.2826), tensor(47.4453), tensor(46.1957), tensor(43.4470), tensor(43.0403), tensor(47.4453)]
sep, day 11 acc_test tensor(43.4661) train_loss 1.6015021895330668
sep, group_id 9 acc_test_lst [tensor(35.5872), tensor(35.8559), tensor(43.5018), tensor(43.2624), tensor(48.1884), tensor(46.3504), tensor(47.6449), tensor(43.2675), tensor(42.4908), tensor(47.0803)]
sep, day 12 acc_test tensor(43.3230) train_loss 1.5852131438107164
sep, group_id 9 acc_test_lst [tensor(36.4769), tensor(35.8559), tensor(44.2238), tensor(44.1489), tensor(48.1884), tensor(47.4453), tensor(47.8261), tensor(42.5494), tensor(42.6740), tensor(46.1679)]
sep, day 13 acc_test tensor(43.5556) train_loss 1.564893772542151
sep, group_id 9 acc_test_lst [tensor(38.4342), tensor(36.5766), tensor(44.5848), tensor(42.7305), tensor(48.9130), tensor(47.6277), tensor(46.1957), tensor(43.4470), tensor(43.5897), tensor(47.6277)]
sep, day 14 acc_test tensor(43.9727) train_loss 1.5589185727570884
sep, group_id 9 acc_test_lst [tensor(36.4769), tensor(35.8559), tensor(45.4874), tensor(44.6809), tensor(47.8261), tensor(47.2628), tensor(47.1014), tensor(43.4470), tensor(42.8571), tensor(46.5328)]
sep, day 15 acc_test tensor(43.7528) train_loss 1.5414131014343633
sep, group_id 9 acc_test_lst [tensor(37.9004), tensor(35.8559), tensor(46.3899), tensor(45.3901), tensor(48.1884), tensor(47.9927), tensor(46.7391), tensor(43.8061), tensor(42.6740), tensor(46.7153)]
sep, day 16 acc_test tensor(44.1652) train_loss 1.5352647124098722
sep, group_id 9 acc_test_lst [tensor(37.5445), tensor(35.8559), tensor(45.6679), tensor(43.7943), tensor(46.9203), tensor(47.8102), tensor(47.8261), tensor(43.9856), tensor(42.8571), tensor(46.8978)]
sep, day 17 acc_test tensor(43.9160) train_loss 1.5222463799697734
sep, group_id 9 acc_test_lst [tensor(38.7900), tensor(36.5766), tensor(46.5704), tensor(45.0355), tensor(47.4638), tensor(47.6277), tensor(48.1884), tensor(44.8833), tensor(43.2234), tensor(46.7153)]
sep, day 18 acc_test tensor(44.5075) train_loss 1.5049759335509034
sep, group_id 9 acc_test_lst [tensor(39.1459), tensor(35.4955), tensor(46.3899), tensor(46.0993), tensor(48.0072), tensor(47.8102), tensor(46.1957), tensor(45.2424), tensor(43.5897), tensor(47.2628)]
sep, day 19 acc_test tensor(44.5239) train_loss 1.495781465447228
sep, group_id 9 acc_test_lst [tensor(39.3238), tensor(36.7568), tensor(47.1119), tensor(46.0993), tensor(47.4638), tensor(48.5401), tensor(48.1884), tensor(45.2424), tensor(43.9560), tensor(47.8102)]
sep, day 20 acc_test tensor(45.0493) train_loss 1.4889644856954876
sep, group_id 9 acc_test_lst [tensor(38.4342), tensor(37.6577), tensor(47.2924), tensor(45.2128), tensor(48.1884), tensor(47.0803), tensor(48.7319), tensor(46.1400), tensor(43.0403), tensor(47.9927)]
sep, day 21 acc_test tensor(44.9771) train_loss 1.4735301513875478
sep, group_id 9 acc_test_lst [tensor(39.5018), tensor(37.6577), tensor(47.2924), tensor(46.2766), tensor(48.7319), tensor(46.8978), tensor(47.2826), tensor(45.9605), tensor(43.4066), tensor(47.8102)]
sep, day 22 acc_test tensor(45.0818) train_loss 1.4658227659733227
sep, group_id 9 acc_test_lst [tensor(39.1459), tensor(36.5766), tensor(48.5560), tensor(46.0993), tensor(49.8188), tensor(47.9927), tensor(47.8261), tensor(45.4219), tensor(43.9560), tensor(47.4453)]
sep, day 23 acc_test tensor(45.2839) train_loss 1.4540993711816552
sep, group_id 9 acc_test_lst [tensor(39.3238), tensor(37.1171), tensor(48.1949), tensor(46.4539), tensor(48.5507), tensor(47.9927), tensor(48.1884), tensor(46.4991), tensor(43.5897), tensor(47.0803)]
sep, day 24 acc_test tensor(45.2991) train_loss 1.4402303786495554
sep, group_id 9 acc_test_lst [tensor(40.2135), tensor(36.3964), tensor(46.5704), tensor(46.8085), tensor(48.5507), tensor(47.9927), tensor(48.5507), tensor(45.9605), tensor(43.4066), tensor(46.1679)]
sep, day 25 acc_test tensor(45.0618) train_loss 1.4312571503663691
sep, group_id 9 acc_test_lst [tensor(39.3238), tensor(36.5766), tensor(47.6534), tensor(46.0993), tensor(49.0942), tensor(47.9927), tensor(48.9130), tensor(46.1400), tensor(43.5897), tensor(46.3504)]
sep, day 26 acc_test tensor(45.1733) train_loss 1.422086121120213
sep, group_id 9 acc_test_lst [tensor(39.1459), tensor(35.6757), tensor(46.2094), tensor(46.8085), tensor(48.7319), tensor(49.4526), tensor(50.3623), tensor(46.1400), tensor(43.4066), tensor(48.1752)]
sep, day 27 acc_test tensor(45.4108) train_loss 1.4065731385762876
sep, group_id 9 acc_test_lst [tensor(39.5018), tensor(36.3964), tensor(47.4729), tensor(46.8085), tensor(48.9130), tensor(48.3577), tensor(49.4565), tensor(46.8582), tensor(44.5055), tensor(47.0803)]
sep, day 28 acc_test tensor(45.5351) train_loss 1.4058586435643248
sep, group_id 9 acc_test_lst [tensor(39.3238), tensor(37.1171), tensor(46.3899), tensor(46.9858), tensor(49.8188), tensor(49.4526), tensor(48.1884), tensor(46.8582), tensor(43.5897), tensor(48.7226)]
sep, day 29 acc_test tensor(45.6447) train_loss 1.3913617331645582
sep, group_id 9 acc_test_lst [tensor(39.8577), tensor(35.6757), tensor(47.6534), tensor(47.1631), tensor(49.4565), tensor(48.3577), tensor(48.1884), tensor(46.6786), tensor(44.1392), tensor(46.8978)]
sep, day 30 acc_test tensor(45.4068) train_loss 1.3822408151996228
sep, group_id 9 acc_test_lst [tensor(40.0356), tensor(37.2973), tensor(48.0144), tensor(48.0496), tensor(48.7319), tensor(49.4526), tensor(48.1884), tensor(46.3196), tensor(43.7729), tensor(47.0803)]
sep, day 31 acc_test tensor(45.6943) train_loss 1.3781672807844751
sep, group_id 9 acc_test_lst [tensor(39.3238), tensor(36.5766), tensor(47.1119), tensor(46.9858), tensor(48.3696), tensor(49.2701), tensor(48.9130), tensor(46.4991), tensor(44.1392), tensor(46.7153)]
sep, day 32 acc_test tensor(45.3904) train_loss 1.3636593283188188
sep, group_id 9 acc_test_lst [tensor(38.7900), tensor(34.4144), tensor(47.8339), tensor(46.9858), tensor(49.2754), tensor(49.8175), tensor(48.0072), tensor(47.2172), tensor(43.7729), tensor(47.8102)]
sep, day 33 acc_test tensor(45.3925) train_loss 1.3563221521799074
sep, group_id 9 acc_test_lst [tensor(40.7473), tensor(36.9369), tensor(46.7509), tensor(47.8723), tensor(49.2754), tensor(49.0876), tensor(47.8261), tensor(46.6786), tensor(45.0549), tensor(47.2628)]
sep, day 34 acc_test tensor(45.7493) train_loss 1.342843235165398
sep, group_id 9 acc_test_lst [tensor(39.5018), tensor(36.9369), tensor(47.4729), tensor(46.6312), tensor(50.), tensor(50.1825), tensor(47.6449), tensor(47.2172), tensor(43.5897), tensor(45.8029)]
sep, day 35 acc_test tensor(45.4980) train_loss 1.3389414396397497
sep, group_id 9 acc_test_lst [tensor(40.2135), tensor(35.4955), tensor(46.7509), tensor(47.5177), tensor(49.8188), tensor(49.8175), tensor(47.8261), tensor(46.8582), tensor(43.9560), tensor(47.9927)]
sep, day 36 acc_test tensor(45.6247) train_loss 1.3242092885200605
sep, group_id 9 acc_test_lst [tensor(39.8577), tensor(36.3964), tensor(46.0289), tensor(46.6312), tensor(49.0942), tensor(49.8175), tensor(50.), tensor(46.4991), tensor(44.6886), tensor(46.8978)]
sep, day 37 acc_test tensor(45.5911) train_loss 1.320569439690888
sep, group_id 9 acc_test_lst [tensor(40.3915), tensor(36.7568), tensor(46.9314), tensor(50.), tensor(49.2754), tensor(49.8175), tensor(49.2754), tensor(47.3968), tensor(44.1392), tensor(47.4453)]
sep, day 38 acc_test tensor(46.1429) train_loss 1.3091566996270374
sep, group_id 9 acc_test_lst [tensor(40.0356), tensor(37.1171), tensor(48.7365), tensor(48.2270), tensor(50.), tensor(50.7299), tensor(50.3623), tensor(46.8582), tensor(44.5055), tensor(47.2628)]
sep, day 39 acc_test tensor(46.3835) train_loss 1.3042559461126388
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(36.2162), tensor(48.0144), tensor(49.1135), tensor(50.5435), tensor(49.4526), tensor(48.5507), tensor(47.2172), tensor(45.0549), tensor(46.1679)]
sep, day 40 acc_test tensor(46.1256) train_loss 1.2894993998823343
sep, group_id 9 acc_test_lst [tensor(40.0356), tensor(36.5766), tensor(48.1949), tensor(48.7589), tensor(49.2754), tensor(49.4526), tensor(50.3623), tensor(47.2172), tensor(44.6886), tensor(47.4453)]
sep, day 41 acc_test tensor(46.2007) train_loss 1.2822028895340107
sep, group_id 9 acc_test_lst [tensor(39.8577), tensor(36.7568), tensor(48.0144), tensor(47.6950), tensor(49.8188), tensor(48.9051), tensor(49.0942), tensor(48.1149), tensor(44.5055), tensor(47.4453)]
sep, day 42 acc_test tensor(46.0208) train_loss 1.2792628643009671
sep, group_id 9 acc_test_lst [tensor(39.8577), tensor(36.0360), tensor(46.9314), tensor(48.2270), tensor(48.9130), tensor(49.8175), tensor(47.8261), tensor(47.5763), tensor(44.3223), tensor(47.0803)]
sep, day 43 acc_test tensor(45.6588) train_loss 1.2661213859628364
sep, group_id 9 acc_test_lst [tensor(40.7473), tensor(36.7568), tensor(47.6534), tensor(48.4043), tensor(49.6377), tensor(49.8175), tensor(49.2754), tensor(46.8582), tensor(44.3223), tensor(47.9927)]
sep, day 44 acc_test tensor(46.1466) train_loss 1.2642706488664721
sep, group_id 9 acc_test_lst [tensor(40.7473), tensor(37.4775), tensor(47.4729), tensor(48.2270), tensor(49.6377), tensor(50.), tensor(48.9130), tensor(46.3196), tensor(43.7729), tensor(48.3577)]
sep, day 45 acc_test tensor(46.0926) train_loss 1.2524588772109055
sep, group_id 9 acc_test_lst [tensor(39.3238), tensor(36.0360), tensor(48.5560), tensor(48.9362), tensor(49.8188), tensor(49.4526), tensor(48.5507), tensor(47.3968), tensor(45.2381), tensor(47.2628)]
sep, day 46 acc_test tensor(46.0572) train_loss 1.2466139675597012
sep, group_id 9 acc_test_lst [tensor(40.7473), tensor(36.2162), tensor(48.3755), tensor(48.4043), tensor(48.3696), tensor(49.2701), tensor(49.6377), tensor(46.3196), tensor(44.8718), tensor(46.3504)]
sep, day 47 acc_test tensor(45.8562) train_loss 1.2379275182858347
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.1171), tensor(48.0144), tensor(50.), tensor(50.7246), tensor(50.1825), tensor(49.0942), tensor(47.3968), tensor(44.6886), tensor(46.7153)]
sep, day 48 acc_test tensor(46.5571) train_loss 1.222889625717312
sep, group_id 9 acc_test_lst [tensor(39.3238), tensor(36.5766), tensor(48.0144), tensor(48.9362), tensor(50.9058), tensor(50.3650), tensor(48.1884), tensor(47.3968), tensor(44.8718), tensor(47.2628)]
sep, day 49 acc_test tensor(46.1842) train_loss 1.2211659041519691
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.4775), tensor(48.0144), tensor(48.5816), tensor(49.4565), tensor(50.1825), tensor(47.2826), tensor(46.4991), tensor(44.6886), tensor(47.2628)]
sep, day 50 acc_test tensor(46.1083) train_loss 1.2115744348824784
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(37.6577), tensor(47.8339), tensor(48.7589), tensor(50.), tensor(50.5474), tensor(48.3696), tensor(46.4991), tensor(45.2381), tensor(47.9927)]
sep, day 51 acc_test tensor(46.4179) train_loss 1.208930569483907
sep, group_id 9 acc_test_lst [tensor(40.3915), tensor(36.9369), tensor(48.1949), tensor(48.0496), tensor(50.7246), tensor(50.7299), tensor(48.7319), tensor(47.9354), tensor(44.8718), tensor(47.8102)]
sep, day 52 acc_test tensor(46.4377) train_loss 1.1986220425560483
sep, group_id 9 acc_test_lst [tensor(40.7473), tensor(36.2162), tensor(48.1949), tensor(48.4043), tensor(48.9130), tensor(51.4599), tensor(50.1812), tensor(47.7558), tensor(45.0549), tensor(47.4453)]
sep, day 53 acc_test tensor(46.4373) train_loss 1.1870619274939116
sep, group_id 9 acc_test_lst [tensor(40.0356), tensor(36.9369), tensor(48.1949), tensor(49.2908), tensor(50.), tensor(50.5474), tensor(47.8261), tensor(47.9354), tensor(44.6886), tensor(47.2628)]
sep, day 54 acc_test tensor(46.2719) train_loss 1.1793707855386113
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(36.3964), tensor(47.8339), tensor(48.9362), tensor(49.6377), tensor(50.1825), tensor(47.8261), tensor(46.1400), tensor(45.4212), tensor(46.8978)]
sep, day 55 acc_test tensor(46.0197) train_loss 1.1811006951155305
sep, group_id 9 acc_test_lst [tensor(40.0356), tensor(37.4775), tensor(47.8339), tensor(48.4043), tensor(50.9058), tensor(50.7299), tensor(48.7319), tensor(47.2172), tensor(45.4212), tensor(48.1752)]
sep, day 56 acc_test tensor(46.4932) train_loss 1.1679823033570758
sep, group_id 9 acc_test_lst [tensor(39.8577), tensor(37.4775), tensor(47.8339), tensor(48.0496), tensor(50.5435), tensor(50.1825), tensor(48.7319), tensor(46.1400), tensor(44.5055), tensor(48.1752)]
sep, day 57 acc_test tensor(46.1497) train_loss 1.1589894307895872
sep, group_id 9 acc_test_lst [tensor(40.3915), tensor(37.4775), tensor(48.1949), tensor(48.9362), tensor(50.7246), tensor(51.4599), tensor(48.1884), tensor(47.0377), tensor(45.2381), tensor(48.1752)]
sep, day 58 acc_test tensor(46.5824) train_loss 1.1525624365199774
sep, group_id 9 acc_test_lst [tensor(40.7473), tensor(36.9369), tensor(48.1949), tensor(48.7589), tensor(49.4565), tensor(50.3650), tensor(48.0072), tensor(47.7558), tensor(45.2381), tensor(46.3504)]
sep, day 59 acc_test tensor(46.1811) train_loss 1.1424136970007732
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(36.7568), tensor(48.3755), tensor(47.8723), tensor(49.4565), tensor(50.1825), tensor(48.9130), tensor(47.2172), tensor(44.8718), tensor(48.1752)]
sep, day 60 acc_test tensor(46.2746) train_loss 1.1307619193160936
sep, group_id 9 acc_test_lst [tensor(39.8577), tensor(36.9369), tensor(47.8339), tensor(47.8723), tensor(50.), tensor(51.0949), tensor(48.5507), tensor(46.6786), tensor(43.9560), tensor(46.7153)]
sep, day 61 acc_test tensor(45.9497) train_loss 1.127347562749972
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(35.8559), tensor(48.7365), tensor(48.4043), tensor(50.3623), tensor(50.7299), tensor(49.0942), tensor(47.0377), tensor(45.9707), tensor(46.5328)]
sep, day 62 acc_test tensor(46.3294) train_loss 1.1237018416380065
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(36.7568), tensor(46.7509), tensor(48.5816), tensor(49.4565), tensor(50.9124), tensor(48.0072), tensor(46.6786), tensor(45.9707), tensor(47.6277)]
sep, day 63 acc_test tensor(46.1312) train_loss 1.1108450364245035
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(35.4955), tensor(47.1119), tensor(48.0496), tensor(50.1812), tensor(49.2701), tensor(47.2826), tensor(48.2944), tensor(44.6886), tensor(48.5401)]
sep, day 64 acc_test tensor(46.0017) train_loss 1.1049324491081673
sep, group_id 9 acc_test_lst [tensor(40.7473), tensor(35.4955), tensor(47.6534), tensor(48.5816), tensor(50.3623), tensor(51.2774), tensor(48.7319), tensor(48.1149), tensor(45.4212), tensor(47.4453)]
sep, day 65 acc_test tensor(46.3831) train_loss 1.0986371830113593
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(37.1171), tensor(47.8339), tensor(47.5177), tensor(48.7319), tensor(51.4599), tensor(47.8261), tensor(47.3968), tensor(44.6886), tensor(47.6277)]
sep, day 66 acc_test tensor(46.2015) train_loss 1.086210456476241
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(36.3964), tensor(47.2924), tensor(47.8723), tensor(49.2754), tensor(50.5474), tensor(47.8261), tensor(47.9354), tensor(45.0549), tensor(47.0803)]
sep, day 67 acc_test tensor(45.9850) train_loss 1.0893764837309552
sep, group_id 9 acc_test_lst [tensor(40.2135), tensor(37.2973), tensor(48.0144), tensor(48.7589), tensor(50.5435), tensor(50.9124), tensor(48.7319), tensor(47.2172), tensor(45.9707), tensor(46.3504)]
sep, day 68 acc_test tensor(46.4010) train_loss 1.0827606624820183
sep, group_id 9 acc_test_lst [tensor(40.0356), tensor(35.8559), tensor(47.4729), tensor(47.6950), tensor(50.7246), tensor(50.5474), tensor(48.5507), tensor(47.2172), tensor(46.3370), tensor(45.8029)]
sep, day 69 acc_test tensor(46.0239) train_loss 1.0757938779365883
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(37.1171), tensor(48.0144), tensor(47.8723), tensor(50.7246), tensor(50.5474), tensor(48.3696), tensor(47.9354), tensor(45.0549), tensor(45.6204)]
sep, day 70 acc_test tensor(46.1826) train_loss 1.064355242626848
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(36.7568), tensor(47.4729), tensor(48.0496), tensor(51.0870), tensor(50.7299), tensor(48.0072), tensor(47.7558), tensor(45.6044), tensor(48.1752)]
sep, day 71 acc_test tensor(46.4564) train_loss 1.0519488417658907
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(36.9369), tensor(48.1949), tensor(48.9362), tensor(50.1812), tensor(51.6423), tensor(48.3696), tensor(47.9354), tensor(45.6044), tensor(47.9927)]
sep, day 72 acc_test tensor(46.6897) train_loss 1.057688241280191
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(35.8559), tensor(49.0975), tensor(49.2908), tensor(50.), tensor(50.3650), tensor(50.), tensor(47.3968), tensor(44.8718), tensor(46.7153)]
sep, day 73 acc_test tensor(46.5052) train_loss 1.0422484738509743
sep, group_id 9 acc_test_lst [tensor(40.3915), tensor(37.1171), tensor(47.1119), tensor(48.2270), tensor(50.9058), tensor(51.0949), tensor(49.2754), tensor(48.1149), tensor(45.7875), tensor(46.1679)]
sep, day 74 acc_test tensor(46.4194) train_loss 1.036763163762909
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(36.2162), tensor(48.7365), tensor(47.8723), tensor(50.9058), tensor(51.6423), tensor(49.6377), tensor(48.6535), tensor(45.6044), tensor(46.3504)]
sep, day 75 acc_test tensor(46.6189) train_loss 1.0345623231445946
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(36.0360), tensor(48.5560), tensor(49.1135), tensor(49.6377), tensor(51.0949), tensor(48.3696), tensor(47.0377), tensor(45.6044), tensor(46.8978)]
sep, day 76 acc_test tensor(46.3629) train_loss 1.020693024907818
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.2973), tensor(48.1949), tensor(48.4043), tensor(49.4565), tensor(51.6423), tensor(49.2754), tensor(47.7558), tensor(44.8718), tensor(46.7153)]
sep, day 77 acc_test tensor(46.5251) train_loss 1.0130066882250255
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(37.1171), tensor(48.3755), tensor(48.7589), tensor(49.8188), tensor(51.0949), tensor(48.5507), tensor(47.7558), tensor(45.2381), tensor(46.3504)]
sep, day 78 acc_test tensor(46.4341) train_loss 0.9991804453295446
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(37.2973), tensor(48.5560), tensor(48.0496), tensor(48.5507), tensor(51.0949), tensor(49.2754), tensor(47.0377), tensor(44.3223), tensor(45.9854)]
sep, day 79 acc_test tensor(46.1095) train_loss 0.9995964238457336
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(38.1982), tensor(48.3755), tensor(48.7589), tensor(50.1812), tensor(51.0949), tensor(48.0072), tensor(47.5763), tensor(44.8718), tensor(47.9927)]
sep, day 80 acc_test tensor(46.5626) train_loss 0.9999129051128429
sep, group_id 9 acc_test_lst [tensor(40.3915), tensor(36.2162), tensor(47.8339), tensor(47.8723), tensor(50.7246), tensor(50.9124), tensor(48.3696), tensor(47.0377), tensor(45.9707), tensor(46.3504)]
sep, day 81 acc_test tensor(46.1679) train_loss 0.9918723890076895
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(38.0180), tensor(47.2924), tensor(47.6950), tensor(50.5435), tensor(50.7299), tensor(48.9130), tensor(47.9354), tensor(45.4212), tensor(46.1679)]
sep, day 82 acc_test tensor(46.3820) train_loss 0.9876528612969738
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.2973), tensor(47.4729), tensor(48.2270), tensor(51.0870), tensor(51.0949), tensor(48.3696), tensor(47.5763), tensor(45.7875), tensor(46.3504)]
sep, day 83 acc_test tensor(46.4900) train_loss 0.9748822588158341
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(36.5766), tensor(46.9314), tensor(49.1135), tensor(50.5435), tensor(50.), tensor(47.1014), tensor(47.5763), tensor(45.4212), tensor(46.3504)]
sep, day 84 acc_test tensor(46.1963) train_loss 0.9712448521688615
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(37.1171), tensor(48.9170), tensor(47.6950), tensor(50.1812), tensor(50.7299), tensor(46.9203), tensor(47.9354), tensor(47.2527), tensor(46.8978)]
sep, day 85 acc_test tensor(46.4216) train_loss 0.9630288098807336
sep, group_id 9 acc_test_lst [tensor(40.2135), tensor(36.9369), tensor(48.0144), tensor(48.7589), tensor(49.8188), tensor(51.0949), tensor(48.7319), tensor(46.6786), tensor(46.3370), tensor(46.8978)]
sep, day 86 acc_test tensor(46.3483) train_loss 0.957772175232808
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(36.9369), tensor(48.9170), tensor(48.5816), tensor(50.3623), tensor(51.2774), tensor(49.0942), tensor(47.5763), tensor(46.1538), tensor(46.8978)]
sep, day 87 acc_test tensor(46.6723) train_loss 0.951351573371273
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(38.0180), tensor(48.9170), tensor(48.9362), tensor(50.1812), tensor(50.3650), tensor(48.1884), tensor(47.9354), tensor(45.2381), tensor(48.3577)]
sep, day 88 acc_test tensor(46.7062) train_loss 0.9482442134406611
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(36.7568), tensor(48.9170), tensor(47.8723), tensor(49.2754), tensor(50.), tensor(47.2826), tensor(47.5763), tensor(45.4212), tensor(47.2628)]
sep, day 89 acc_test tensor(46.2713) train_loss 0.9473125088598051
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(37.2973), tensor(47.8339), tensor(48.0496), tensor(50.5435), tensor(50.), tensor(48.3696), tensor(47.7558), tensor(44.8718), tensor(47.0803)]
sep, day 90 acc_test tensor(46.3973) train_loss 0.928690229046153
sep, group_id 9 acc_test_lst [tensor(42.5267), tensor(37.1171), tensor(46.9314), tensor(48.0496), tensor(49.4565), tensor(51.2774), tensor(49.2754), tensor(46.4991), tensor(45.4212), tensor(45.2555)]
sep, day 91 acc_test tensor(46.1810) train_loss 0.9266761210655236
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(36.7568), tensor(48.7365), tensor(47.6950), tensor(50.3623), tensor(50.3650), tensor(49.4565), tensor(47.5763), tensor(44.6886), tensor(47.0803)]
sep, day 92 acc_test tensor(46.4888) train_loss 0.915484522622038
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(35.8559), tensor(48.5560), tensor(48.0496), tensor(50.1812), tensor(50.5474), tensor(47.4638), tensor(46.8582), tensor(45.2381), tensor(47.4453)]
sep, day 93 acc_test tensor(46.2010) train_loss 0.9230407744873415
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(34.9550), tensor(47.8339), tensor(47.1631), tensor(49.2754), tensor(51.4599), tensor(48.0072), tensor(47.3968), tensor(44.5055), tensor(45.9854)]
sep, day 94 acc_test tensor(45.7152) train_loss 0.9115355063410553
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(37.1171), tensor(48.1949), tensor(46.9858), tensor(50.), tensor(50.7299), tensor(48.0072), tensor(47.9354), tensor(44.5055), tensor(47.0803)]
sep, day 95 acc_test tensor(46.2549) train_loss 0.9033945770064489
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(36.0360), tensor(47.8339), tensor(48.0496), tensor(51.0870), tensor(50.5474), tensor(48.9130), tensor(48.1149), tensor(45.9707), tensor(45.4380)]
sep, day 96 acc_test tensor(46.4339) train_loss 0.8951718244713995
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(33.8739), tensor(46.3899), tensor(47.6950), tensor(49.8188), tensor(51.2774), tensor(48.1884), tensor(47.5763), tensor(44.8718), tensor(47.4453)]
sep, day 97 acc_test tensor(45.8952) train_loss 0.8921830039020232
sep, group_id 9 acc_test_lst [tensor(42.5267), tensor(36.7568), tensor(48.7365), tensor(49.1135), tensor(49.8188), tensor(50.7299), tensor(45.8333), tensor(47.7558), tensor(44.8718), tensor(47.2628)]
sep, day 98 acc_test tensor(46.3406) train_loss 0.8834988926626448
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(37.8378), tensor(47.2924), tensor(47.8723), tensor(48.7319), tensor(51.0949), tensor(47.8261), tensor(47.3968), tensor(44.6886), tensor(47.2628)]
sep, day 99 acc_test tensor(46.1819) train_loss 0.8919037558639198
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(36.9369), tensor(48.1949), tensor(47.3404), tensor(50.5435), tensor(50.5474), tensor(47.1014), tensor(47.0377), tensor(45.6044), tensor(47.4453)]
sep, day 100 acc_test tensor(46.1321) train_loss 0.8811986825691194
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(35.4955), tensor(47.8339), tensor(48.2270), tensor(49.2754), tensor(50.9124), tensor(47.4638), tensor(47.0377), tensor(44.3223), tensor(47.8102)]
sep, day 101 acc_test tensor(46.0015) train_loss 0.86922332658778
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.1171), tensor(47.2924), tensor(47.5177), tensor(48.3696), tensor(50.9124), tensor(47.4638), tensor(47.5763), tensor(45.2381), tensor(46.7153)]
sep, day 102 acc_test tensor(45.9840) train_loss 0.863800577910712
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(37.6577), tensor(48.5560), tensor(47.5177), tensor(49.4565), tensor(50.), tensor(48.1884), tensor(46.4991), tensor(45.4212), tensor(46.3504)]
sep, day 103 acc_test tensor(46.1106) train_loss 0.8622603214358971
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(36.9369), tensor(48.0144), tensor(48.4043), tensor(49.0942), tensor(50.7299), tensor(47.1014), tensor(47.0377), tensor(44.8718), tensor(45.9854)]
sep, day 104 acc_test tensor(45.9635) train_loss 0.851852077491889
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(37.2973), tensor(47.4729), tensor(48.4043), tensor(49.8188), tensor(49.6350), tensor(47.8261), tensor(47.3968), tensor(45.6044), tensor(47.4453)]
sep, day 105 acc_test tensor(46.2360) train_loss 0.8511873818653005
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(38.3784), tensor(48.0144), tensor(49.6454), tensor(51.0870), tensor(50.9124), tensor(48.7319), tensor(47.7558), tensor(45.0549), tensor(45.9854)]
sep, day 106 acc_test tensor(46.7736) train_loss 0.8461715017802378
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(37.1171), tensor(46.5704), tensor(48.7589), tensor(49.0942), tensor(50.1825), tensor(49.0942), tensor(46.8582), tensor(44.6886), tensor(46.5328)]
sep, day 107 acc_test tensor(46.0890) train_loss 0.8356503202667247
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(38.0180), tensor(46.9314), tensor(46.9858), tensor(49.0942), tensor(50.), tensor(48.3696), tensor(48.2944), tensor(44.6886), tensor(46.1679)]
sep, day 108 acc_test tensor(45.9653) train_loss 0.8273851183220239
sep, group_id 9 acc_test_lst [tensor(42.7046), tensor(37.2973), tensor(48.3755), tensor(48.4043), tensor(50.7246), tensor(49.8175), tensor(47.6449), tensor(46.3196), tensor(45.2381), tensor(46.1679)]
sep, day 109 acc_test tensor(46.2694) train_loss 0.8341979642357644
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.2973), tensor(48.5560), tensor(48.9362), tensor(49.4565), tensor(49.8175), tensor(47.8261), tensor(46.8582), tensor(44.1392), tensor(45.9854)]
sep, day 110 acc_test tensor(46.0509) train_loss 0.8185872914328752
sep, group_id 9 acc_test_lst [tensor(43.2384), tensor(36.3964), tensor(47.6534), tensor(48.9362), tensor(49.4565), tensor(50.7299), tensor(47.2826), tensor(47.3968), tensor(44.5055), tensor(45.8029)]
sep, day 111 acc_test tensor(46.1399) train_loss 0.8146332593782999
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(36.9369), tensor(48.3755), tensor(46.8085), tensor(49.6377), tensor(50.5474), tensor(48.0072), tensor(47.0377), tensor(43.9560), tensor(47.4453)]
sep, day 112 acc_test tensor(46.0923) train_loss 0.8132878904703901
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(36.5766), tensor(47.6534), tensor(48.4043), tensor(49.0942), tensor(51.2774), tensor(48.0072), tensor(45.7810), tensor(44.5055), tensor(46.8978)]
sep, day 113 acc_test tensor(45.8767) train_loss 0.8076353978151437
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(37.8378), tensor(48.5560), tensor(48.2270), tensor(50.7246), tensor(50.9124), tensor(47.4638), tensor(46.4991), tensor(45.0549), tensor(46.8978)]
sep, day 114 acc_test tensor(46.3099) train_loss 0.8035154445114671
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(37.2973), tensor(47.6534), tensor(47.6950), tensor(48.9130), tensor(50.9124), tensor(49.4565), tensor(46.3196), tensor(44.3223), tensor(45.8029)]
sep, day 115 acc_test tensor(46.0365) train_loss 0.7966911977040944
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(36.2162), tensor(47.4729), tensor(49.8227), tensor(49.4565), tensor(50.7299), tensor(48.7319), tensor(47.0377), tensor(44.8718), tensor(46.8978)]
sep, day 116 acc_test tensor(46.2874) train_loss 0.7945750253402954
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(37.2973), tensor(48.1949), tensor(48.4043), tensor(49.0942), tensor(50.3650), tensor(48.7319), tensor(47.9354), tensor(45.7875), tensor(46.8978)]
sep, day 117 acc_test tensor(46.4701) train_loss 0.7898850062531045
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(36.7568), tensor(48.1949), tensor(48.7589), tensor(50.), tensor(50.5474), tensor(47.8261), tensor(47.9354), tensor(45.0549), tensor(48.1752)]
sep, day 118 acc_test tensor(46.4887) train_loss 0.7847409077793541
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(38.1982), tensor(48.7365), tensor(48.7589), tensor(49.6377), tensor(51.4599), tensor(48.9130), tensor(47.7558), tensor(45.6044), tensor(46.7153)]
sep, day 119 acc_test tensor(46.7595) train_loss 0.7772950740551239
sep, group_id 9 acc_test_lst [tensor(42.5267), tensor(36.5766), tensor(49.0975), tensor(48.7589), tensor(48.5507), tensor(51.8248), tensor(48.9130), tensor(45.6014), tensor(45.0549), tensor(46.3504)]
sep, day 120 acc_test tensor(46.3255) train_loss 0.7674403087931242
sep, group_id 9 acc_test_lst [tensor(42.7046), tensor(37.6577), tensor(48.3755), tensor(48.5816), tensor(49.2754), tensor(50.3650), tensor(47.2826), tensor(46.8582), tensor(44.5055), tensor(47.4453)]
sep, day 121 acc_test tensor(46.3051) train_loss 0.7673266988687593
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.4775), tensor(48.5560), tensor(48.9362), tensor(50.), tensor(50.5474), tensor(48.5507), tensor(45.2424), tensor(46.3370), tensor(47.6277)]
sep, day 122 acc_test tensor(46.4912) train_loss 0.7710153158528926
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(35.6757), tensor(48.7365), tensor(47.1631), tensor(49.2754), tensor(51.0949), tensor(47.8261), tensor(46.8582), tensor(44.3223), tensor(46.5328)]
sep, day 123 acc_test tensor(45.9122) train_loss 0.7540692553509974
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(37.4775), tensor(49.0975), tensor(48.2270), tensor(48.9130), tensor(50.7299), tensor(46.9203), tensor(46.6786), tensor(45.2381), tensor(47.4453)]
sep, day 124 acc_test tensor(46.2542) train_loss 0.7567816538383109
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(36.9369), tensor(48.3755), tensor(47.6950), tensor(49.8188), tensor(50.9124), tensor(47.8261), tensor(46.6786), tensor(45.6044), tensor(46.5328)]
sep, day 125 acc_test tensor(46.2374) train_loss 0.7533191578258028
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(37.1171), tensor(48.0144), tensor(48.2270), tensor(49.2754), tensor(52.3723), tensor(47.8261), tensor(46.8582), tensor(44.5055), tensor(47.9927)]
sep, day 126 acc_test tensor(46.4537) train_loss 0.7431782035414366
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(37.2973), tensor(47.8339), tensor(48.0496), tensor(49.8188), tensor(50.1825), tensor(48.3696), tensor(46.8582), tensor(44.8718), tensor(47.2628)]
sep, day 127 acc_test tensor(46.2715) train_loss 0.7399040326392833
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(38.0180), tensor(48.7365), tensor(48.4043), tensor(50.1812), tensor(50.9124), tensor(47.8261), tensor(46.4991), tensor(45.2381), tensor(45.9854)]
sep, day 128 acc_test tensor(46.3082) train_loss 0.7293681404999277
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(36.9369), tensor(48.7365), tensor(48.0496), tensor(49.0942), tensor(51.6423), tensor(46.3768), tensor(46.8582), tensor(44.5055), tensor(46.7153)]
sep, day 129 acc_test tensor(46.0552) train_loss 0.7276147401444848
sep, group_id 9 acc_test_lst [tensor(42.7046), tensor(36.0360), tensor(48.0144), tensor(46.6312), tensor(50.1812), tensor(51.2774), tensor(47.6449), tensor(46.3196), tensor(45.0549), tensor(47.4453)]
sep, day 130 acc_test tensor(46.1310) train_loss 0.725104745775116
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(37.2973), tensor(48.5560), tensor(47.6950), tensor(49.8188), tensor(51.4599), tensor(47.8261), tensor(45.7810), tensor(44.1392), tensor(47.2628)]
sep, day 131 acc_test tensor(46.0939) train_loss 0.7208360767396481
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(36.2162), tensor(49.4585), tensor(48.5816), tensor(50.1812), tensor(50.3650), tensor(47.4638), tensor(46.8582), tensor(44.6886), tensor(45.2555)]
sep, day 132 acc_test tensor(46.0705) train_loss 0.7194075059499777
sep, group_id 9 acc_test_lst [tensor(40.2135), tensor(37.6577), tensor(49.4585), tensor(48.0496), tensor(49.4565), tensor(51.8248), tensor(47.1014), tensor(45.9605), tensor(45.2381), tensor(46.8978)]
sep, day 133 acc_test tensor(46.1859) train_loss 0.7026008475462117
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(37.1171), tensor(49.0975), tensor(48.4043), tensor(49.4565), tensor(51.0949), tensor(47.2826), tensor(46.4991), tensor(44.8718), tensor(47.6277)]
sep, day 134 acc_test tensor(46.2377) train_loss 0.7082602661384838
sep, group_id 9 acc_test_lst [tensor(42.8826), tensor(37.2973), tensor(48.5560), tensor(47.6950), tensor(50.1812), tensor(50.9124), tensor(49.0942), tensor(47.3968), tensor(45.4212), tensor(46.8978)]
sep, day 135 acc_test tensor(46.6334) train_loss 0.703835976213538
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(37.4775), tensor(49.0975), tensor(48.4043), tensor(50.7246), tensor(51.6423), tensor(49.0942), tensor(46.4991), tensor(44.6886), tensor(47.2628)]
sep, day 136 acc_test tensor(46.6172) train_loss 0.6913180850840939
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(37.4775), tensor(48.1949), tensor(49.6454), tensor(50.3623), tensor(51.6423), tensor(48.5507), tensor(46.8582), tensor(45.0549), tensor(47.0803)]
sep, day 137 acc_test tensor(46.7215) train_loss 0.7014146490320692
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(35.4955), tensor(48.3755), tensor(48.5816), tensor(50.1812), tensor(50.7299), tensor(48.3696), tensor(47.3968), tensor(45.0549), tensor(45.9854)]
sep, day 138 acc_test tensor(46.2163) train_loss 0.6939002022023837
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(37.2973), tensor(49.0975), tensor(48.4043), tensor(50.3623), tensor(50.5474), tensor(48.1884), tensor(46.8582), tensor(45.4212), tensor(47.0803)]
sep, day 139 acc_test tensor(46.4716) train_loss 0.6891212102597981
sep, group_id 9 acc_test_lst [tensor(42.8826), tensor(36.5766), tensor(48.3755), tensor(48.2270), tensor(50.), tensor(51.6423), tensor(49.0942), tensor(46.6786), tensor(44.5055), tensor(46.5328)]
sep, day 140 acc_test tensor(46.4515) train_loss 0.6863288668753991
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(36.0360), tensor(48.1949), tensor(48.9362), tensor(50.7246), tensor(50.3650), tensor(47.2826), tensor(46.8582), tensor(44.1392), tensor(46.7153)]
sep, day 141 acc_test tensor(46.1601) train_loss 0.6844800046460984
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(36.9369), tensor(48.1949), tensor(48.9362), tensor(48.9130), tensor(50.3650), tensor(47.8261), tensor(47.3968), tensor(45.2381), tensor(47.8102)]
sep, day 142 acc_test tensor(46.2898) train_loss 0.6711393762360613
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(37.8378), tensor(47.4729), tensor(49.2908), tensor(49.0942), tensor(50.3650), tensor(47.6449), tensor(46.1400), tensor(44.6886), tensor(45.9854)]
sep, day 143 acc_test tensor(46.0691) train_loss 0.6665918896240066
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(36.7568), tensor(48.0144), tensor(49.4681), tensor(50.1812), tensor(50.1825), tensor(47.8261), tensor(47.3968), tensor(43.5897), tensor(46.7153)]
sep, day 144 acc_test tensor(46.2124) train_loss 0.6717152071152607
sep, group_id 9 acc_test_lst [tensor(42.5267), tensor(36.2162), tensor(48.9170), tensor(48.9362), tensor(50.3623), tensor(50.5474), tensor(49.8188), tensor(47.0377), tensor(45.0549), tensor(46.3504)]
sep, day 145 acc_test tensor(46.5768) train_loss 0.6630300032094202
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(38.3784), tensor(48.3755), tensor(48.7589), tensor(50.3623), tensor(51.6423), tensor(48.1884), tensor(46.3196), tensor(44.3223), tensor(46.7153)]
sep, day 146 acc_test tensor(46.5412) train_loss 0.6618122535443708
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(36.3964), tensor(47.1119), tensor(47.1631), tensor(50.), tensor(50.9124), tensor(48.7319), tensor(46.8582), tensor(44.5055), tensor(45.0730)]
sep, day 147 acc_test tensor(45.7856) train_loss 0.6548277763494512
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(36.9369), tensor(48.5560), tensor(49.2908), tensor(50.1812), tensor(50.1825), tensor(48.7319), tensor(45.7810), tensor(44.8718), tensor(48.3577)]
sep, day 148 acc_test tensor(46.4349) train_loss 0.6537729806721679
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(36.9369), tensor(49.0975), tensor(49.6454), tensor(50.1812), tensor(50.5474), tensor(46.9203), tensor(47.2172), tensor(45.2381), tensor(47.2628)]
sep, day 149 acc_test tensor(46.4862) train_loss 0.6532008854041965
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(38.0180), tensor(48.5560), tensor(49.6454), tensor(50.), tensor(50.9124), tensor(47.4638), tensor(45.9605), tensor(44.6886), tensor(47.0803)]
sep, day 150 acc_test tensor(46.4318) train_loss 0.6392826042716534
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(36.9369), tensor(49.2780), tensor(48.5816), tensor(50.), tensor(49.8175), tensor(46.7391), tensor(46.3196), tensor(45.0549), tensor(45.9854)]
sep, day 151 acc_test tensor(46.0884) train_loss 0.6351352476848564
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(36.3964), tensor(48.9170), tensor(47.6950), tensor(49.6377), tensor(50.), tensor(48.1884), tensor(45.9605), tensor(44.6886), tensor(45.6204)]
sep, day 152 acc_test tensor(45.8741) train_loss 0.6386065674184924
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(36.0360), tensor(49.0975), tensor(48.2270), tensor(49.4565), tensor(49.8175), tensor(48.3696), tensor(46.3196), tensor(43.9560), tensor(47.2628)]
sep, day 153 acc_test tensor(45.9646) train_loss 0.6361657558293489
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(36.2162), tensor(49.2780), tensor(49.4681), tensor(50.1812), tensor(49.0876), tensor(48.3696), tensor(46.4991), tensor(45.4212), tensor(46.8978)]
sep, day 154 acc_test tensor(46.3768) train_loss 0.6380955909028174
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(36.5766), tensor(47.8339), tensor(50.1773), tensor(50.), tensor(48.7226), tensor(46.9203), tensor(45.7810), tensor(45.2381), tensor(46.3504)]
sep, day 155 acc_test tensor(45.8703) train_loss 0.6274058453141881
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(35.8559), tensor(48.0144), tensor(48.2270), tensor(49.2754), tensor(49.0876), tensor(47.4638), tensor(45.2424), tensor(45.0549), tensor(47.4453)]
sep, day 156 acc_test tensor(45.8015) train_loss 0.6193752038416106
sep, group_id 9 acc_test_lst [tensor(40.3915), tensor(37.4775), tensor(47.4729), tensor(48.4043), tensor(49.4565), tensor(48.9051), tensor(48.3696), tensor(46.1400), tensor(45.0549), tensor(46.8978)]
sep, day 157 acc_test tensor(45.8570) train_loss 0.6201450948482732
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(36.3964), tensor(47.2924), tensor(49.2908), tensor(50.7246), tensor(49.4526), tensor(47.8261), tensor(46.4991), tensor(43.9560), tensor(47.0803)]
sep, day 158 acc_test tensor(45.9088) train_loss 0.6143382010261256
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(36.3964), tensor(47.2924), tensor(49.6454), tensor(49.6377), tensor(50.3650), tensor(47.8261), tensor(46.6786), tensor(43.9560), tensor(47.6277)]
sep, day 159 acc_test tensor(46.0706) train_loss 0.606101379416818
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(36.0360), tensor(48.0144), tensor(49.1135), tensor(49.6377), tensor(49.4526), tensor(47.6449), tensor(46.4991), tensor(43.9560), tensor(47.0803)]
sep, day 160 acc_test tensor(45.8538) train_loss 0.6074192010280787
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(37.4775), tensor(47.6534), tensor(48.9362), tensor(49.4565), tensor(49.4526), tensor(48.3696), tensor(46.4991), tensor(43.7729), tensor(47.4453)]
sep, day 161 acc_test tensor(46.0522) train_loss 0.5971459983927756
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(36.3964), tensor(47.4729), tensor(48.9362), tensor(49.0942), tensor(49.4526), tensor(47.1014), tensor(47.0377), tensor(44.5055), tensor(47.4453)]
sep, day 162 acc_test tensor(45.9079) train_loss 0.5972316051133436
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(37.4775), tensor(47.6534), tensor(49.4681), tensor(51.2681), tensor(50.5474), tensor(47.8261), tensor(46.3196), tensor(43.9560), tensor(47.4453)]
sep, day 163 acc_test tensor(46.3421) train_loss 0.5977734226074959
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(36.9369), tensor(46.5704), tensor(48.5816), tensor(50.9058), tensor(50.5474), tensor(48.1884), tensor(45.2424), tensor(43.4066), tensor(47.6277)]
sep, day 164 acc_test tensor(46.0000) train_loss 0.594744897976505
sep, group_id 9 acc_test_lst [tensor(42.7046), tensor(36.3964), tensor(47.6534), tensor(49.4681), tensor(50.3623), tensor(50.), tensor(48.9130), tensor(46.1400), tensor(45.2381), tensor(45.8029)]
sep, day 165 acc_test tensor(46.2679) train_loss 0.5866461607706749
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(37.2973), tensor(47.1119), tensor(48.0496), tensor(49.8188), tensor(50.1825), tensor(48.3696), tensor(45.9605), tensor(43.2234), tensor(47.0803)]
sep, day 166 acc_test tensor(45.8909) train_loss 0.5887852660589367
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(36.9369), tensor(48.1949), tensor(49.2908), tensor(49.4565), tensor(49.6350), tensor(47.4638), tensor(46.3196), tensor(44.3223), tensor(46.3504)]
sep, day 167 acc_test tensor(45.9607) train_loss 0.5862521270650334
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(38.0180), tensor(46.9314), tensor(48.4043), tensor(50.), tensor(49.2701), tensor(47.1014), tensor(45.0628), tensor(44.1392), tensor(46.3504)]
sep, day 168 acc_test tensor(45.6915) train_loss 0.5836106262703885
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(36.3964), tensor(46.7509), tensor(48.2270), tensor(49.4565), tensor(48.3577), tensor(48.7319), tensor(45.7810), tensor(44.5055), tensor(46.7153)]
sep, day 169 acc_test tensor(45.6025) train_loss 0.5621474254826301
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(35.6757), tensor(47.2924), tensor(49.4681), tensor(49.2754), tensor(49.6350), tensor(47.4638), tensor(45.4219), tensor(44.1392), tensor(46.3504)]
sep, day 170 acc_test tensor(45.6715) train_loss 0.5663376369542042
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(37.1171), tensor(47.2924), tensor(49.4681), tensor(49.2754), tensor(50.3650), tensor(48.5507), tensor(47.0377), tensor(43.2234), tensor(46.3504)]
sep, day 171 acc_test tensor(45.9961) train_loss 0.5652898090974111
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(37.8378), tensor(47.6534), tensor(48.5816), tensor(50.1812), tensor(50.5474), tensor(47.8261), tensor(45.9605), tensor(43.5897), tensor(46.7153)]
sep, day 172 acc_test tensor(46.1242) train_loss 0.5586236277441664
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(37.8378), tensor(47.4729), tensor(49.8227), tensor(49.8188), tensor(49.6350), tensor(47.8261), tensor(46.1400), tensor(43.0403), tensor(47.8102)]
sep, day 173 acc_test tensor(46.1397) train_loss 0.5574863936608778
sep, group_id 9 acc_test_lst [tensor(42.5267), tensor(38.1982), tensor(47.6534), tensor(49.2908), tensor(50.), tensor(49.6350), tensor(47.6449), tensor(45.6014), tensor(43.2234), tensor(45.6204)]
sep, day 174 acc_test tensor(45.9394) train_loss 0.548606885012083
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(36.9369), tensor(47.4729), tensor(50.1773), tensor(49.8188), tensor(50.3650), tensor(46.7391), tensor(45.6014), tensor(44.1392), tensor(46.1679)]
sep, day 175 acc_test tensor(45.8344) train_loss 0.5471504616725072
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(36.3964), tensor(47.8339), tensor(49.2908), tensor(49.2754), tensor(49.0876), tensor(47.1014), tensor(45.2424), tensor(43.5897), tensor(44.7080)]
sep, day 176 acc_test tensor(45.4519) train_loss 0.5471067425233203
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(37.1171), tensor(47.1119), tensor(48.5816), tensor(49.0942), tensor(50.), tensor(47.8261), tensor(46.4991), tensor(43.9560), tensor(45.8029)]
sep, day 177 acc_test tensor(45.7804) train_loss 0.5422279923659881
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(38.1982), tensor(47.1119), tensor(49.1135), tensor(49.0942), tensor(49.6350), tensor(47.6449), tensor(45.0628), tensor(43.0403), tensor(46.1679)]
sep, day 178 acc_test tensor(45.7240) train_loss 0.5447392420200304
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(37.2973), tensor(47.2924), tensor(48.4043), tensor(49.8188), tensor(50.1825), tensor(48.9130), tensor(45.0628), tensor(44.8718), tensor(46.7153)]
sep, day 179 acc_test tensor(46.0373) train_loss 0.5350558976351664
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(36.9369), tensor(47.6534), tensor(48.7589), tensor(49.4565), tensor(50.), tensor(48.7319), tensor(45.4219), tensor(44.6886), tensor(46.8978)]
sep, day 180 acc_test tensor(45.9649) train_loss 0.5437964237138562
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(36.7568), tensor(47.8339), tensor(48.7589), tensor(49.8188), tensor(49.6350), tensor(46.9203), tensor(46.8582), tensor(45.0549), tensor(47.6277)]
sep, day 181 acc_test tensor(46.0190) train_loss 0.5298381744807241
sep, group_id 9 acc_test_lst [tensor(39.8577), tensor(36.2162), tensor(47.8339), tensor(48.7589), tensor(50.5435), tensor(49.8175), tensor(48.3696), tensor(45.7810), tensor(45.4212), tensor(45.2555)]
sep, day 182 acc_test tensor(45.7855) train_loss 0.5305068020986812
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(38.1982), tensor(47.6534), tensor(48.9362), tensor(49.4565), tensor(49.4526), tensor(48.7319), tensor(46.1400), tensor(44.5055), tensor(46.5328)]
sep, day 183 acc_test tensor(46.0710) train_loss 0.5322171535046126
sep, group_id 9 acc_test_lst [tensor(39.5018), tensor(37.4775), tensor(46.9314), tensor(50.), tensor(50.3623), tensor(50.), tensor(48.5507), tensor(46.8582), tensor(45.0549), tensor(45.0730)]
sep, day 184 acc_test tensor(45.9810) train_loss 0.5299981262047144
sep, group_id 9 acc_test_lst [tensor(42.8826), tensor(38.1982), tensor(45.6679), tensor(49.8227), tensor(49.6377), tensor(49.6350), tensor(46.3768), tensor(45.4219), tensor(44.5055), tensor(45.6204)]
sep, day 185 acc_test tensor(45.7769) train_loss 0.5303275619239862
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(36.9369), tensor(47.8339), tensor(49.2908), tensor(48.9130), tensor(50.), tensor(47.4638), tensor(45.9605), tensor(43.9560), tensor(46.7153)]
sep, day 186 acc_test tensor(45.9419) train_loss 0.5180642077865266
sep, group_id 9 acc_test_lst [tensor(42.5267), tensor(37.1171), tensor(48.0144), tensor(48.9362), tensor(50.1812), tensor(49.6350), tensor(48.0072), tensor(46.1400), tensor(43.9560), tensor(46.3504)]
sep, day 187 acc_test tensor(46.0864) train_loss 0.5165137487199286
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(37.2973), tensor(48.5560), tensor(48.7589), tensor(50.7246), tensor(49.4526), tensor(48.5507), tensor(46.4991), tensor(44.3223), tensor(47.2628)]
sep, day 188 acc_test tensor(46.3773) train_loss 0.5246743509399047
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(37.1171), tensor(47.1119), tensor(50.7092), tensor(50.5435), tensor(49.2701), tensor(48.7319), tensor(47.0377), tensor(44.8718), tensor(46.7153)]
sep, day 189 acc_test tensor(46.4457) train_loss 0.5147740088060802
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(38.1982), tensor(46.7509), tensor(49.6454), tensor(50.7246), tensor(48.7226), tensor(47.4638), tensor(46.8582), tensor(43.4066), tensor(45.6204)]
sep, day 190 acc_test tensor(45.9028) train_loss 0.5031378000822859
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(38.0180), tensor(48.7365), tensor(49.4681), tensor(50.9058), tensor(50.), tensor(49.0942), tensor(46.3196), tensor(44.1392), tensor(46.8978)]
sep, day 191 acc_test tensor(46.5216) train_loss 0.5143869555328611
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(38.3784), tensor(47.8339), tensor(49.1135), tensor(51.0870), tensor(49.8175), tensor(47.8261), tensor(46.6786), tensor(44.3223), tensor(46.3504)]
sep, day 192 acc_test tensor(46.2689) train_loss 0.5021990429206612
sep, group_id 9 acc_test_lst [tensor(43.0605), tensor(37.2973), tensor(48.1949), tensor(48.0496), tensor(51.0870), tensor(49.2701), tensor(47.4638), tensor(46.6786), tensor(42.8571), tensor(44.8905)]
sep, day 193 acc_test tensor(45.8849) train_loss 0.5034198868694866
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(38.3784), tensor(47.8339), tensor(49.4681), tensor(50.7246), tensor(48.7226), tensor(47.8261), tensor(47.0377), tensor(43.9560), tensor(45.6204)]
sep, day 194 acc_test tensor(46.1205) train_loss 0.5039544105310121
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(38.1982), tensor(47.6534), tensor(50.7092), tensor(50.5435), tensor(49.4526), tensor(47.1014), tensor(48.1149), tensor(45.4212), tensor(46.7153)]
sep, day 195 acc_test tensor(46.6081) train_loss 0.49933213564709944
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(37.2973), tensor(46.9314), tensor(48.7589), tensor(50.3623), tensor(49.2701), tensor(48.0072), tensor(47.0377), tensor(44.8718), tensor(45.9854)]
sep, day 196 acc_test tensor(46.0871) train_loss 0.48752578701249105
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(37.4775), tensor(48.1949), tensor(48.4043), tensor(50.9058), tensor(48.7226), tensor(48.5507), tensor(46.4991), tensor(43.7729), tensor(45.6204)]
sep, day 197 acc_test tensor(46.0319) train_loss 0.4963186343631575
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.4775), tensor(48.0144), tensor(48.9362), tensor(48.7319), tensor(49.0876), tensor(48.0072), tensor(46.4991), tensor(42.6740), tensor(45.2555)]
sep, day 198 acc_test tensor(45.6320) train_loss 0.4852972548372773
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(36.9369), tensor(46.9314), tensor(49.2908), tensor(48.9130), tensor(48.5401), tensor(47.8261), tensor(46.4991), tensor(43.5897), tensor(46.3504)]
sep, day 199 acc_test tensor(45.5447) train_loss 0.487444468081321
sep, group_id 9 acc_test_lst [tensor(42.8826), tensor(37.8378), tensor(48.5560), tensor(49.2908), tensor(49.4565), tensor(48.5401), tensor(48.7319), tensor(46.3196), tensor(44.5055), tensor(46.8978)]
sep, day 200 acc_test tensor(46.3019) train_loss 0.4802385837300892
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(37.6577), tensor(47.2924), tensor(49.2908), tensor(48.9130), tensor(48.9051), tensor(47.6449), tensor(45.4219), tensor(43.5897), tensor(47.0803)]
sep, day 201 acc_test tensor(45.7077) train_loss 0.4827723746221234
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(37.2973), tensor(47.2924), tensor(48.7589), tensor(49.4565), tensor(49.8175), tensor(46.5580), tensor(46.8582), tensor(44.3223), tensor(45.4380)]
sep, day 202 acc_test tensor(45.7614) train_loss 0.48678435952093807
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.1171), tensor(47.1119), tensor(49.2908), tensor(49.0942), tensor(50.1825), tensor(47.1014), tensor(46.6786), tensor(44.5055), tensor(45.6204)]
sep, day 203 acc_test tensor(45.8340) train_loss 0.47955065759005444
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(37.1171), tensor(47.2924), tensor(49.4681), tensor(49.6377), tensor(49.4526), tensor(48.3696), tensor(46.3196), tensor(44.3223), tensor(46.5328)]
sep, day 204 acc_test tensor(46.0683) train_loss 0.46958979709841114
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(37.2973), tensor(48.3755), tensor(48.7589), tensor(49.6377), tensor(49.2701), tensor(46.9203), tensor(46.1400), tensor(44.3223), tensor(46.7153)]
sep, day 205 acc_test tensor(45.8363) train_loss 0.467675187339285
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(36.9369), tensor(46.9314), tensor(50.1773), tensor(50.), tensor(50.), tensor(47.8261), tensor(45.9605), tensor(43.9560), tensor(47.2628)]
sep, day 206 acc_test tensor(46.1044) train_loss 0.4705578556185733
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(37.1171), tensor(47.2924), tensor(48.5816), tensor(49.8188), tensor(49.0876), tensor(47.1014), tensor(45.2424), tensor(44.3223), tensor(46.3504)]
sep, day 207 acc_test tensor(45.7263) train_loss 0.4681149270214149
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.8378), tensor(46.0289), tensor(48.7589), tensor(49.6377), tensor(49.2701), tensor(48.3696), tensor(46.8582), tensor(43.7729), tensor(46.1679)]
sep, day 208 acc_test tensor(45.8339) train_loss 0.46296818951493124
sep, group_id 9 acc_test_lst [tensor(40.3915), tensor(37.1171), tensor(47.8339), tensor(49.1135), tensor(50.), tensor(49.2701), tensor(47.8261), tensor(45.7810), tensor(43.5897), tensor(46.7153)]
sep, day 209 acc_test tensor(45.7638) train_loss 0.460292589090786
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(35.3153), tensor(46.3899), tensor(48.5816), tensor(48.5507), tensor(49.4526), tensor(49.0942), tensor(43.8061), tensor(43.7729), tensor(44.3431)]
sep, day 210 acc_test tensor(45.0587) train_loss 0.45041670558871333
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(36.7568), tensor(46.3899), tensor(48.5816), tensor(48.9130), tensor(49.2701), tensor(48.1884), tensor(46.6786), tensor(43.7729), tensor(45.6204)]
sep, day 211 acc_test tensor(45.5097) train_loss 0.464432926574107
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(36.7568), tensor(48.0144), tensor(48.9362), tensor(50.1812), tensor(49.6350), tensor(47.4638), tensor(45.0628), tensor(43.7729), tensor(47.2628)]
sep, day 212 acc_test tensor(45.7655) train_loss 0.45474089956328617
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(36.3964), tensor(46.9314), tensor(49.8227), tensor(49.8188), tensor(49.6350), tensor(49.0942), tensor(45.4219), tensor(42.8571), tensor(46.7153)]
sep, day 213 acc_test tensor(45.7262) train_loss 0.4500571704813992
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(36.9369), tensor(46.5704), tensor(50.), tensor(48.7319), tensor(49.6350), tensor(48.3696), tensor(46.3196), tensor(43.9560), tensor(47.0803)]
sep, day 214 acc_test tensor(45.9415) train_loss 0.45407495352553284
sep, group_id 9 acc_test_lst [tensor(40.0356), tensor(37.8378), tensor(47.1119), tensor(49.1135), tensor(49.6377), tensor(49.6350), tensor(46.1957), tensor(45.2424), tensor(43.7729), tensor(44.5255)]
sep, day 215 acc_test tensor(45.3108) train_loss 0.4503527557015141
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(37.6577), tensor(47.2924), tensor(50.1773), tensor(49.8188), tensor(49.8175), tensor(46.3768), tensor(45.2424), tensor(43.9560), tensor(46.1679)]
sep, day 216 acc_test tensor(45.8322) train_loss 0.44554856929679715
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(39.4595), tensor(47.4729), tensor(50.), tensor(49.8188), tensor(49.2701), tensor(46.5580), tensor(45.9605), tensor(43.2234), tensor(46.8978)]
sep, day 217 acc_test tensor(46.0832) train_loss 0.4394582568952094
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(37.1171), tensor(48.9170), tensor(49.4681), tensor(48.3696), tensor(49.0876), tensor(46.3768), tensor(46.6786), tensor(42.3077), tensor(45.4380)]
sep, day 218 acc_test tensor(45.5042) train_loss 0.43677546985192917
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(37.8378), tensor(47.6534), tensor(49.6454), tensor(49.6377), tensor(48.3577), tensor(46.5580), tensor(46.6786), tensor(43.5897), tensor(46.3504)]
sep, day 219 acc_test tensor(45.7590) train_loss 0.4279036977229416
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(37.4775), tensor(48.1949), tensor(48.9362), tensor(49.2754), tensor(48.9051), tensor(47.8261), tensor(46.1400), tensor(44.5055), tensor(45.6204)]
sep, day 220 acc_test tensor(45.7984) train_loss 0.4267961109083737
sep, group_id 9 acc_test_lst [tensor(40.0356), tensor(38.9189), tensor(47.6534), tensor(48.9362), tensor(48.5507), tensor(50.), tensor(47.6449), tensor(46.6786), tensor(44.6886), tensor(45.9854)]
sep, day 221 acc_test tensor(45.9092) train_loss 0.42996837026196333
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(37.4775), tensor(48.0144), tensor(48.7589), tensor(48.9130), tensor(49.4526), tensor(47.2826), tensor(45.7810), tensor(43.0403), tensor(44.8905)]
sep, day 222 acc_test tensor(45.5426) train_loss 0.42938593459927815
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(37.1171), tensor(46.9314), tensor(50.1773), tensor(49.6377), tensor(49.6350), tensor(47.8261), tensor(45.7810), tensor(43.4066), tensor(45.4380)]
sep, day 223 acc_test tensor(45.7231) train_loss 0.42174706114645594
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(38.1982), tensor(46.9314), tensor(49.2908), tensor(49.0942), tensor(50.1825), tensor(45.1087), tensor(45.6014), tensor(43.0403), tensor(45.2555)]
sep, day 224 acc_test tensor(45.3628) train_loss 0.4187466757712847
sep, group_id 9 acc_test_lst [tensor(40.3915), tensor(36.7568), tensor(46.9314), tensor(48.9362), tensor(49.4565), tensor(50.5474), tensor(47.6449), tensor(45.4219), tensor(43.0403), tensor(47.4453)]
sep, day 225 acc_test tensor(45.6572) train_loss 0.422945020104922
sep, group_id 9 acc_test_lst [tensor(42.5267), tensor(38.1982), tensor(46.7509), tensor(48.7589), tensor(48.9130), tensor(51.2774), tensor(48.3696), tensor(45.0628), tensor(43.9560), tensor(46.8978)]
sep, day 226 acc_test tensor(46.0711) train_loss 0.41450077527295165
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(36.9369), tensor(46.7509), tensor(50.), tensor(48.5507), tensor(49.2701), tensor(47.4638), tensor(47.2172), tensor(43.5897), tensor(45.8029)]
sep, day 227 acc_test tensor(45.7219) train_loss 0.41136969107238736
sep, group_id 9 acc_test_lst [tensor(40.7473), tensor(37.1171), tensor(46.9314), tensor(49.6454), tensor(48.3696), tensor(49.2701), tensor(46.9203), tensor(47.0377), tensor(42.6740), tensor(45.9854)]
sep, day 228 acc_test tensor(45.4698) train_loss 0.4160460192137601
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(36.9369), tensor(46.5704), tensor(49.8227), tensor(49.4565), tensor(50.3650), tensor(47.6449), tensor(45.6014), tensor(42.6740), tensor(45.6204)]
sep, day 229 acc_test tensor(45.6329) train_loss 0.4092851526526972
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(37.1171), tensor(47.8339), tensor(49.1135), tensor(48.7319), tensor(49.4526), tensor(46.7391), tensor(47.2172), tensor(44.6886), tensor(46.7153)]
sep, day 230 acc_test tensor(45.9602) train_loss 0.406150191370431
sep, group_id 9 acc_test_lst [tensor(43.0605), tensor(36.0360), tensor(46.7509), tensor(49.6454), tensor(48.0072), tensor(49.4526), tensor(48.0072), tensor(46.1400), tensor(43.0403), tensor(44.1606)]
sep, day 231 acc_test tensor(45.4301) train_loss 0.40357392589528795
sep, group_id 9 acc_test_lst [tensor(42.5267), tensor(36.7568), tensor(47.2924), tensor(49.1135), tensor(49.2754), tensor(49.0876), tensor(46.9203), tensor(46.4991), tensor(43.7729), tensor(45.0730)]
sep, day 232 acc_test tensor(45.6318) train_loss 0.4099890740033315
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(37.1171), tensor(47.6534), tensor(49.6454), tensor(49.2754), tensor(49.2701), tensor(47.6449), tensor(46.4991), tensor(43.7729), tensor(45.2555)]
sep, day 233 acc_test tensor(45.7415) train_loss 0.4005221563422998
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(37.2973), tensor(47.4729), tensor(48.9362), tensor(49.4565), tensor(48.9051), tensor(47.4638), tensor(45.2424), tensor(43.5897), tensor(45.4380)]
sep, day 234 acc_test tensor(45.5617) train_loss 0.4085143840275943
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(39.0991), tensor(47.4729), tensor(48.5816), tensor(48.9130), tensor(48.9051), tensor(48.0072), tensor(45.2424), tensor(43.2234), tensor(46.5328)]
sep, day 235 acc_test tensor(45.6903) train_loss 0.4004958325266628
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(36.5766), tensor(46.5704), tensor(48.7589), tensor(48.9130), tensor(50.1825), tensor(46.9203), tensor(47.0377), tensor(43.4066), tensor(46.1679)]
sep, day 236 acc_test tensor(45.5815) train_loss 0.4012170388495539
sep, group_id 9 acc_test_lst [tensor(40.3915), tensor(37.8378), tensor(46.5704), tensor(49.4681), tensor(50.), tensor(49.4526), tensor(48.3696), tensor(45.0628), tensor(43.7729), tensor(45.9854)]
sep, day 237 acc_test tensor(45.6911) train_loss 0.3910679499516565
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(37.1171), tensor(48.7365), tensor(49.4681), tensor(49.8188), tensor(49.6350), tensor(47.4638), tensor(45.4219), tensor(43.4066), tensor(45.2555)]
sep, day 238 acc_test tensor(45.8316) train_loss 0.3859334942460642
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(38.0180), tensor(48.3755), tensor(48.4043), tensor(49.0942), tensor(48.9051), tensor(46.7391), tensor(46.6786), tensor(43.7729), tensor(46.8978)]
sep, day 239 acc_test tensor(45.8700) train_loss 0.38996995902389714
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(38.0180), tensor(47.1119), tensor(48.0496), tensor(49.0942), tensor(49.4526), tensor(45.8333), tensor(45.0628), tensor(43.0403), tensor(45.9854)]
sep, day 240 acc_test tensor(45.2573) train_loss 0.38970677504343504
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(37.2973), tensor(47.2924), tensor(50.3546), tensor(49.2754), tensor(49.4526), tensor(45.6522), tensor(46.3196), tensor(43.2234), tensor(44.1606)]
sep, day 241 acc_test tensor(45.3953) train_loss 0.38074205916564857
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(37.1171), tensor(48.0144), tensor(49.2908), tensor(49.6377), tensor(49.4526), tensor(48.3696), tensor(45.2424), tensor(42.8571), tensor(45.9854)]
sep, day 242 acc_test tensor(45.7248) train_loss 0.3848005480920332
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(36.5766), tensor(47.4729), tensor(49.4681), tensor(49.0942), tensor(49.4526), tensor(47.8261), tensor(46.4991), tensor(42.4908), tensor(47.0803)]
sep, day 243 acc_test tensor(45.7420) train_loss 0.3852990690997483
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(38.1982), tensor(48.1949), tensor(49.2908), tensor(49.0942), tensor(49.4526), tensor(47.1014), tensor(45.6014), tensor(42.3077), tensor(45.4380)]
sep, day 244 acc_test tensor(45.6316) train_loss 0.37942632231653733
sep, group_id 9 acc_test_lst [tensor(40.2135), tensor(37.2973), tensor(48.0144), tensor(51.2411), tensor(49.4565), tensor(49.2701), tensor(45.8333), tensor(47.5763), tensor(43.5897), tensor(45.9854)]
sep, day 245 acc_test tensor(45.8478) train_loss 0.37740641310721934
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(37.4775), tensor(47.2924), tensor(49.2908), tensor(49.4565), tensor(48.5401), tensor(46.3768), tensor(45.9605), tensor(43.7729), tensor(45.9854)]
sep, day 246 acc_test tensor(45.5078) train_loss 0.3877910949289634
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.6577), tensor(48.0144), tensor(50.), tensor(48.9130), tensor(49.2701), tensor(47.2826), tensor(45.4219), tensor(42.6740), tensor(45.8029)]
sep, day 247 acc_test tensor(45.6674) train_loss 0.38053427363704734
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(37.4775), tensor(48.3755), tensor(48.9362), tensor(49.0942), tensor(49.4526), tensor(46.7391), tensor(45.2424), tensor(44.1392), tensor(46.1679)]
sep, day 248 acc_test tensor(45.7973) train_loss 0.3811891997579188
sep, group_id 9 acc_test_lst [tensor(42.7046), tensor(35.4955), tensor(47.2924), tensor(49.8227), tensor(49.2754), tensor(49.2701), tensor(47.4638), tensor(46.4991), tensor(43.9560), tensor(46.8978)]
sep, day 249 acc_test tensor(45.8677) train_loss 0.36111513456008504
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.1171), tensor(48.3755), tensor(50.3546), tensor(50.), tensor(49.2701), tensor(46.7391), tensor(45.9605), tensor(42.8571), tensor(44.1606)]
sep, day 250 acc_test tensor(45.6472) train_loss 0.36994333844858945
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(37.6577), tensor(47.6534), tensor(50.5319), tensor(50.1812), tensor(49.0876), tensor(46.1957), tensor(45.2424), tensor(43.0403), tensor(46.1679)]
sep, day 251 acc_test tensor(45.7929) train_loss 0.36213323381886636
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(37.4775), tensor(48.9170), tensor(50.), tensor(49.8188), tensor(48.5401), tensor(47.2826), tensor(46.1400), tensor(43.7729), tensor(44.7080)]
sep, day 252 acc_test tensor(45.8828) train_loss 0.3686787688074029
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(37.1171), tensor(46.9314), tensor(49.2908), tensor(49.0942), tensor(49.8175), tensor(46.3768), tensor(45.9605), tensor(43.2234), tensor(44.1606)]
sep, day 253 acc_test tensor(45.4143) train_loss 0.36633861183036664
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(38.3784), tensor(46.5704), tensor(51.2411), tensor(48.9130), tensor(49.6350), tensor(48.0072), tensor(46.1400), tensor(43.9560), tensor(43.6131)]
sep, day 254 acc_test tensor(45.8269) train_loss 0.3599695777884929
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(37.2973), tensor(47.8339), tensor(48.2270), tensor(48.7319), tensor(49.6350), tensor(48.0072), tensor(45.9605), tensor(43.2234), tensor(45.2555)]
sep, day 255 acc_test tensor(45.4741) train_loss 0.3617124692254732
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(36.2162), tensor(47.8339), tensor(49.6454), tensor(49.4565), tensor(49.2701), tensor(47.2826), tensor(45.6014), tensor(43.5897), tensor(44.8905)]
sep, day 256 acc_test tensor(45.5246) train_loss 0.3541665387258827
sep, group_id 9 acc_test_lst [tensor(40.7473), tensor(37.2973), tensor(47.2924), tensor(49.2908), tensor(49.0942), tensor(49.6350), tensor(46.5580), tensor(45.9605), tensor(42.4908), tensor(45.4380)]
sep, day 257 acc_test tensor(45.3804) train_loss 0.35779341090081884
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(38.0180), tensor(46.7509), tensor(50.), tensor(50.7246), tensor(48.9051), tensor(47.6449), tensor(45.7810), tensor(43.0403), tensor(45.6204)]
sep, day 258 acc_test tensor(45.8300) train_loss 0.3546574308964145
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.4775), tensor(46.9314), tensor(49.6454), tensor(49.4565), tensor(49.6350), tensor(47.2826), tensor(45.6014), tensor(42.8571), tensor(43.9781)]
sep, day 259 acc_test tensor(45.4502) train_loss 0.3455315383579531
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(36.9369), tensor(47.1119), tensor(50.3546), tensor(49.6377), tensor(47.2628), tensor(46.1957), tensor(47.3968), tensor(41.2088), tensor(43.9781)]
sep, day 260 acc_test tensor(45.1364) train_loss 0.3499356346357812
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.8378), tensor(47.1119), tensor(50.7092), tensor(49.2754), tensor(49.8175), tensor(48.3696), tensor(46.3196), tensor(44.6886), tensor(47.0803)]
sep, day 261 acc_test tensor(46.2847) train_loss 0.3467312533833446
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(36.9369), tensor(47.8339), tensor(49.4681), tensor(48.3696), tensor(50.1825), tensor(47.4638), tensor(46.6786), tensor(42.4908), tensor(46.3504)]
sep, day 262 acc_test tensor(45.7945) train_loss 0.3470821682456895
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(37.6577), tensor(48.0144), tensor(50.1773), tensor(49.6377), tensor(50.), tensor(46.1957), tensor(46.6786), tensor(42.3077), tensor(45.8029)]
sep, day 263 acc_test tensor(45.7753) train_loss 0.3552892083487664
sep, group_id 9 acc_test_lst [tensor(40.7473), tensor(38.1982), tensor(47.6534), tensor(50.), tensor(49.8188), tensor(49.8175), tensor(47.4638), tensor(47.5763), tensor(43.0403), tensor(46.8978)]
sep, day 264 acc_test tensor(46.1213) train_loss 0.33876321577306756
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(37.6577), tensor(46.2094), tensor(49.8227), tensor(49.6377), tensor(50.), tensor(46.9203), tensor(47.2172), tensor(44.6886), tensor(44.8905)]
sep, day 265 acc_test tensor(45.8147) train_loss 0.34296292123537264
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(36.7568), tensor(48.0144), tensor(49.4681), tensor(49.4565), tensor(50.), tensor(46.0145), tensor(48.8330), tensor(43.4066), tensor(44.7080)]
sep, day 266 acc_test tensor(45.8473) train_loss 0.34002454912110935
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(35.6757), tensor(48.1949), tensor(49.4681), tensor(49.8188), tensor(51.0949), tensor(47.2826), tensor(46.1400), tensor(43.9560), tensor(45.0730)]
sep, day 267 acc_test tensor(45.8697) train_loss 0.3458524526883436
sep, group_id 9 acc_test_lst [tensor(43.0605), tensor(38.1982), tensor(49.2780), tensor(49.1135), tensor(49.2754), tensor(50.1825), tensor(46.5580), tensor(47.2172), tensor(42.4908), tensor(43.7956)]
sep, day 268 acc_test tensor(45.9170) train_loss 0.33271371928760507
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(35.6757), tensor(48.7365), tensor(49.4681), tensor(50.), tensor(51.2774), tensor(46.7391), tensor(47.0377), tensor(42.3077), tensor(45.6204)]
sep, day 269 acc_test tensor(45.8322) train_loss 0.3385303669067993
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(35.8559), tensor(48.0144), tensor(48.7589), tensor(49.6377), tensor(50.), tensor(46.5580), tensor(46.8582), tensor(43.2234), tensor(45.2555)]
sep, day 270 acc_test tensor(45.6511) train_loss 0.3345757429691681
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(36.3964), tensor(48.5560), tensor(49.4681), tensor(50.7246), tensor(49.4526), tensor(46.5580), tensor(46.6786), tensor(41.7582), tensor(45.8029)]
sep, day 271 acc_test tensor(45.7744) train_loss 0.3299485271209139
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(37.1171), tensor(47.4729), tensor(50.), tensor(49.8188), tensor(49.0876), tensor(47.6449), tensor(46.3196), tensor(43.0403), tensor(45.6204)]
sep, day 272 acc_test tensor(45.8115) train_loss 0.32839298580166726
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(36.3964), tensor(46.9314), tensor(48.9362), tensor(50.), tensor(49.6350), tensor(46.3768), tensor(46.6786), tensor(43.5897), tensor(45.4380)]
sep, day 273 acc_test tensor(45.6153) train_loss 0.3231206699755772
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(36.5766), tensor(48.1949), tensor(48.9362), tensor(49.8188), tensor(49.4526), tensor(46.0145), tensor(45.9605), tensor(43.7729), tensor(46.7153)]
sep, day 274 acc_test tensor(45.7079) train_loss 0.3159232673568562
sep, group_id 9 acc_test_lst [tensor(42.5267), tensor(36.9369), tensor(48.0144), tensor(48.7589), tensor(50.), tensor(48.7226), tensor(47.1014), tensor(45.4219), tensor(42.8571), tensor(44.8905)]
sep, day 275 acc_test tensor(45.5231) train_loss 0.3298235680690223
sep, group_id 9 acc_test_lst [tensor(38.7900), tensor(36.2162), tensor(48.9170), tensor(49.8227), tensor(49.2754), tensor(49.4526), tensor(47.8261), tensor(47.2172), tensor(43.2234), tensor(44.5255)]
sep, day 276 acc_test tensor(45.5266) train_loss 0.3294349594676537
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.4775), tensor(47.6534), tensor(49.4681), tensor(48.7319), tensor(49.2701), tensor(46.9203), tensor(46.4991), tensor(43.0403), tensor(43.4307)]
sep, day 277 acc_test tensor(45.4128) train_loss 0.3245761190734571
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(37.8378), tensor(47.4729), tensor(48.9362), tensor(49.2754), tensor(50.5474), tensor(47.2826), tensor(46.3196), tensor(42.8571), tensor(44.8905)]
sep, day 278 acc_test tensor(45.7412) train_loss 0.32193555035211047
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(37.4775), tensor(47.2924), tensor(49.6454), tensor(49.8188), tensor(50.3650), tensor(47.4638), tensor(47.5763), tensor(43.4066), tensor(44.3431)]
sep, day 279 acc_test tensor(45.8848) train_loss 0.31589200281032903
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(37.8378), tensor(47.6534), tensor(49.8227), tensor(48.9130), tensor(49.6350), tensor(48.9130), tensor(47.0377), tensor(43.5897), tensor(45.8029)]
sep, day 280 acc_test tensor(46.0131) train_loss 0.32184077654951937
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(38.1982), tensor(46.9314), tensor(48.7589), tensor(49.6377), tensor(49.6350), tensor(46.7391), tensor(47.3968), tensor(41.7582), tensor(46.3504)]
sep, day 281 acc_test tensor(45.6509) train_loss 0.31964438169268655
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(37.1171), tensor(47.6534), tensor(49.6454), tensor(49.8188), tensor(49.4526), tensor(46.9203), tensor(48.4740), tensor(42.1245), tensor(45.6204)]
sep, day 282 acc_test tensor(45.8641) train_loss 0.30660829121245925
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(36.5766), tensor(47.6534), tensor(49.4681), tensor(50.), tensor(49.0876), tensor(46.3768), tensor(47.2172), tensor(43.4066), tensor(45.2555)]
sep, day 283 acc_test tensor(45.6501) train_loss 0.3113970723875295
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(36.2162), tensor(48.7365), tensor(50.1773), tensor(48.7319), tensor(49.6350), tensor(47.1014), tensor(47.5763), tensor(43.9560), tensor(46.3504)]
sep, day 284 acc_test tensor(46.0296) train_loss 0.30600254779898084
sep, group_id 9 acc_test_lst [tensor(39.8577), tensor(37.6577), tensor(47.4729), tensor(48.4043), tensor(49.0942), tensor(50.), tensor(46.7391), tensor(46.4991), tensor(43.2234), tensor(45.9854)]
sep, day 285 acc_test tensor(45.4934) train_loss 0.3147549802472843
sep, group_id 9 acc_test_lst [tensor(40.2135), tensor(37.6577), tensor(46.9314), tensor(48.7589), tensor(49.4565), tensor(48.9051), tensor(45.8333), tensor(46.6786), tensor(41.7582), tensor(45.0730)]
sep, day 286 acc_test tensor(45.1266) train_loss 0.30697537754375875
sep, group_id 9 acc_test_lst [tensor(39.8577), tensor(37.2973), tensor(48.0144), tensor(48.4043), tensor(50.1812), tensor(50.7299), tensor(46.3768), tensor(46.8582), tensor(43.0403), tensor(45.2555)]
sep, day 287 acc_test tensor(45.6015) train_loss 0.31007932522248605
sep, group_id 9 acc_test_lst [tensor(39.8577), tensor(36.5766), tensor(46.7509), tensor(48.7589), tensor(49.6377), tensor(50.1825), tensor(47.1014), tensor(46.8582), tensor(43.4066), tensor(43.7956)]
sep, day 288 acc_test tensor(45.2926) train_loss 0.3079750238223488
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(37.2973), tensor(46.9314), tensor(46.9858), tensor(49.8188), tensor(49.8175), tensor(47.4638), tensor(47.2172), tensor(43.7729), tensor(44.1606)]
sep, day 289 acc_test tensor(45.4391) train_loss 0.3030848498448602
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(37.6577), tensor(46.9314), tensor(48.2270), tensor(49.4565), tensor(49.8175), tensor(46.3768), tensor(45.4219), tensor(42.3077), tensor(43.9781)]
sep, day 290 acc_test tensor(45.1456) train_loss 0.31357267756863955
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(36.3964), tensor(47.8339), tensor(48.4043), tensor(49.8188), tensor(49.2701), tensor(47.4638), tensor(45.7810), tensor(43.4066), tensor(44.7080)]
sep, day 291 acc_test tensor(45.4008) train_loss 0.30821034457722873
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(36.7568), tensor(47.1119), tensor(49.1135), tensor(50.), tensor(49.2701), tensor(47.1014), tensor(46.6786), tensor(43.9560), tensor(45.8029)]
sep, day 292 acc_test tensor(45.6717) train_loss 0.3066041341711241
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(36.7568), tensor(47.1119), tensor(49.1135), tensor(49.6377), tensor(49.0876), tensor(46.1957), tensor(47.0377), tensor(43.5897), tensor(44.8905)]
sep, day 293 acc_test tensor(45.5592) train_loss 0.300557035418429
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(37.2973), tensor(46.9314), tensor(50.7092), tensor(49.4565), tensor(48.5401), tensor(47.1014), tensor(46.4991), tensor(43.0403), tensor(44.5255)]
sep, day 294 acc_test tensor(45.5560) train_loss 0.2999822542081534
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(37.2973), tensor(47.6534), tensor(49.8227), tensor(49.6377), tensor(49.6350), tensor(46.1957), tensor(45.7810), tensor(41.9414), tensor(44.1606)]
sep, day 295 acc_test tensor(45.3406) train_loss 0.29160603061243207
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(37.1171), tensor(47.1119), tensor(48.7589), tensor(49.8188), tensor(50.), tensor(46.9203), tensor(44.8833), tensor(43.0403), tensor(44.8905)]
sep, day 296 acc_test tensor(45.4356) train_loss 0.29513222541099093
sep, group_id 9 acc_test_lst [tensor(39.5018), tensor(36.3964), tensor(46.9314), tensor(49.8227), tensor(49.6377), tensor(49.0876), tensor(46.1957), tensor(46.8582), tensor(44.1392), tensor(45.4380)]
sep, day 297 acc_test tensor(45.4009) train_loss 0.2963377656893558
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(35.6757), tensor(48.1949), tensor(49.8227), tensor(49.6377), tensor(48.9051), tensor(46.3768), tensor(46.1400), tensor(42.1245), tensor(45.0730)]
sep, day 298 acc_test tensor(45.2876) train_loss 0.2961944784112675
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(38.1982), tensor(48.0144), tensor(50.5319), tensor(48.7319), tensor(49.6350), tensor(47.2826), tensor(46.8582), tensor(41.9414), tensor(43.7956)]
sep, day 299 acc_test tensor(45.5915) train_loss 0.2964013462418657
sep, group_id 9 acc_test_lst [tensor(40.2135), tensor(36.7568), tensor(47.4729), tensor(49.4681), tensor(49.2754), tensor(48.5401), tensor(46.9203), tensor(47.0377), tensor(43.5897), tensor(45.8029)]
sep, day 300 acc_test tensor(45.5077) train_loss 0.2809930056752301
sep, group_id 9 acc_test_lst [tensor(40.3915), tensor(38.3784), tensor(46.5704), tensor(48.9362), tensor(48.7319), tensor(49.2701), tensor(46.3768), tensor(45.9605), tensor(43.9560), tensor(46.1679)]
sep, day 301 acc_test tensor(45.4740) train_loss 0.29592825558900593
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(36.3964), tensor(46.9314), tensor(50.), tensor(49.8188), tensor(49.4526), tensor(47.2826), tensor(47.0377), tensor(43.2234), tensor(45.8029)]
sep, day 302 acc_test tensor(45.8117) train_loss 0.2870598196787456
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(37.4775), tensor(47.1119), tensor(49.8227), tensor(48.5507), tensor(48.1752), tensor(48.1884), tensor(47.0377), tensor(42.8571), tensor(46.5328)]
sep, day 303 acc_test tensor(45.7213) train_loss 0.28479193732344216
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(37.1171), tensor(46.7509), tensor(49.6454), tensor(49.2754), tensor(49.6350), tensor(46.7391), tensor(46.6786), tensor(42.3077), tensor(43.9781)]
sep, day 304 acc_test tensor(45.3764) train_loss 0.27660588021440324
sep, group_id 9 acc_test_lst [tensor(41.4591), tensor(36.7568), tensor(47.2924), tensor(50.3546), tensor(48.5507), tensor(48.9051), tensor(46.9203), tensor(46.8582), tensor(42.4908), tensor(44.5255)]
sep, day 305 acc_test tensor(45.4114) train_loss 0.2784323885035543
sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(36.0360), tensor(47.2924), tensor(50.), tensor(50.), tensor(48.3577), tensor(46.7391), tensor(47.7558), tensor(43.4066), tensor(43.0657)]
sep, day 306 acc_test tensor(45.3935) train_loss 0.2814435076444574
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(36.2162), tensor(47.1119), tensor(49.2908), tensor(49.6377), tensor(48.7226), tensor(46.5580), tensor(47.0377), tensor(42.6740), tensor(43.6131)]
sep, day 307 acc_test tensor(45.1787) train_loss 0.28386260364169585
sep, group_id 9 acc_test_lst [tensor(41.8149), tensor(36.2162), tensor(48.7365), tensor(50.3546), tensor(49.0942), tensor(49.4526), tensor(46.5580), tensor(45.9605), tensor(43.2234), tensor(45.0730)]
sep, day 308 acc_test tensor(45.6484) train_loss 0.27164392516839414
sep, group_id 9 acc_test_lst [tensor(40.5694), tensor(36.0360), tensor(47.4729), tensor(48.7589), tensor(49.2754), tensor(49.6350), tensor(47.1014), tensor(47.3968), tensor(42.6740), tensor(44.3431)]
sep, day 309 acc_test tensor(45.3263) train_loss 0.27536481027924453
sep, group_id 9 acc_test_lst [tensor(40.3915), tensor(36.5766), tensor(47.6534), tensor(48.2270), tensor(49.2754), tensor(49.8175), tensor(46.7391), tensor(46.3196), tensor(42.3077), tensor(44.7080)]
sep, day 310 acc_test tensor(45.2016) train_loss 0.2844639076003209
sep, group_id 9 acc_test_lst [tensor(40.3915), tensor(36.7568), tensor(47.4729), tensor(49.1135), tensor(49.4565), tensor(48.5401), tensor(46.7391), tensor(45.9605), tensor(42.4908), tensor(44.1606)]
sep, day 311 acc_test tensor(45.1082) train_loss 0.2761055172502951
sep, group_id 9 acc_test_lst [tensor(40.7473), tensor(37.4775), tensor(47.6534), tensor(49.8227), tensor(49.2754), tensor(47.2628), tensor(46.7391), tensor(46.4991), tensor(43.0403), tensor(44.3431)]
sep, day 312 acc_test tensor(45.2861) train_loss 0.27515920878044664
sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(38.0180), tensor(47.1119), tensor(49.2908), tensor(49.0942), tensor(48.5401), tensor(47.6449), tensor(47.0377), tensor(42.6740), tensor(43.6131)]
sep, day 313 acc_test tensor(45.5374) train_loss 0.27837885060295525
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(35.8559), tensor(46.7509), tensor(50.3546), tensor(49.6377), tensor(48.5401), tensor(47.6449), tensor(45.9605), tensor(43.0403), tensor(44.7080)]
sep, day 314 acc_test tensor(45.4486) train_loss 0.27243613974094244
sep, group_id 9 acc_test_lst [tensor(40.3915), tensor(37.1171), tensor(47.8339), tensor(49.4681), tensor(50.1812), tensor(49.2701), tensor(47.1014), tensor(46.6786), tensor(43.4066), tensor(45.8029)]
sep, day 315 acc_test tensor(45.7251) train_loss 0.2625212269606324
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(36.2162), tensor(47.4729), tensor(50.1773), tensor(49.4565), tensor(49.0876), tensor(46.1957), tensor(47.2172), tensor(43.5897), tensor(44.1606)]
sep, day 316 acc_test tensor(45.5567) train_loss 0.2741337987843334
sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(36.7568), tensor(47.4729), tensor(49.4681), tensor(48.9130), tensor(48.7226), tensor(46.7391), tensor(45.9605), tensor(43.7729), tensor(45.8029)]
sep, day 317 acc_test tensor(45.4534) train_loss 0.2676715241216069
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(37.1171), tensor(47.8339), tensor(48.4043), tensor(48.9130), tensor(49.2701), tensor(46.9203), tensor(46.3196), tensor(43.7729), tensor(45.6204)]
sep, day 318 acc_test tensor(45.5275) train_loss 0.26533878473498906
sep, group_id 9 acc_test_lst [tensor(41.6370), tensor(36.3964), tensor(47.6534), tensor(48.4043), tensor(49.4565), tensor(48.7226), tensor(45.8333), tensor(47.2172), tensor(42.8571), tensor(45.6204)]
sep, day 319 acc_test tensor(45.3798) train_loss 0.27208211503478963
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(37.4775), tensor(47.2924), tensor(50.1773), tensor(48.9130), tensor(48.5401), tensor(46.7391), tensor(46.4991), tensor(41.5751), tensor(44.1606)]
sep, day 320 acc_test tensor(45.2478) train_loss 0.26625536100767694
sep, group_id 9 acc_test_lst [tensor(40.3915), tensor(36.3964), tensor(48.1949), tensor(47.6950), tensor(48.3696), tensor(48.7226), tensor(46.3768), tensor(46.6786), tensor(42.4908), tensor(43.6131)]
sep, day 321 acc_test tensor(44.8929) train_loss 0.26182474894064733
sep, group_id 9 acc_test_lst [tensor(42.1708), tensor(36.2162), tensor(47.8339), tensor(50.3546), tensor(48.5507), tensor(47.6277), tensor(46.7391), tensor(47.5763), tensor(42.4908), tensor(44.8905)]
sep, day 322 acc_test tensor(45.4451) train_loss 0.2599209985152308
sep, group_id 9 acc_test_lst [tensor(41.9929), tensor(36.9369), tensor(47.4729), tensor(48.5816), tensor(49.2754), tensor(48.1752), tensor(46.1957), tensor(47.9354), tensor(43.7729), tensor(44.7080)]
sep, day 323 acc_test tensor(45.5047) train_loss 0.2600282144585873
sep, group_id 9 acc_test_lst [tensor(41.1032), tensor(36.7568), tensor(48.5560), tensor(49.2908), tensor(48.5507), tensor(48.1752), tensor(46.9203), tensor(47.3968), tensor(43.5897), tensor(44.1606)]
sep, day 324 acc_test tensor(45.4500) train_loss 0.25108393538521734
sep, group_id 9 acc_test_lst [tensor(40.2135), tensor(36.5766), tensor(48.5560), tensor(48.7589), tensor(49.2754), tensor(48.1752), tensor(46.9203), tensor(45.7810), tensor(42.6740), tensor(44.7080)]
sep, day 325 acc_test tensor(45.1639) train_loss 0.25860714127853
sep, group_id 9 acc_test_lst [tensor(40.7473), tensor(36.3964), tensor(49.0975), tensor(48.4043), tensor(48.7319), tensor(48.5401), tensor(45.6522), tensor(45.7810), tensor(42.6740), tensor(44.7080)]
sep, day 326 acc_test tensor(45.0733) train_loss 0.2611633735213435
"""




# fedavg, day 1 acc_test tensor(30.1883) train_loss 1.8673907011206423
# test_semi_fb acc_test_lst [tensor(29.3594), tensor(33.1532), tensor(42.2383), tensor(35.2837), tensor(32.4275), tensor(30.8394), tensor(30.2536), tensor(35.1885), tensor(28.7546), tensor(27.5547)]
# fedavg, day 2 acc_test tensor(32.5053) train_loss 1.811032896501418
# test_semi_fb acc_test_lst [tensor(32.0285), tensor(34.9550), tensor(44.2238), tensor(36.5248), tensor(32.4275), tensor(32.8467), tensor(32.6087), tensor(36.8043), tensor(30.2198), tensor(28.8321)]
# fedavg, day 3 acc_test tensor(34.1471) train_loss 1.7726796752873684

fedavg_y_lst = []
fedavg_lst = fedavg_s.split('\n')
for line in fedavg_lst:
    if line.startswith("fedavg, day"):
        line_lst = line.split()
        for a in line_lst:
            if a.startswith("tensor("):
                fedavg_y_lst.append(float(a.replace("tensor(", "").replace(")", "")))

print(fedavg_y_lst)


# rr, day 49 acc_test tensor(44.1723) train_loss 1.7887232258932426
# test_semi_fb acc_test_lst [tensor(44.6619), tensor(35.6757), tensor(42.4188), tensor(43.9716), tensor(43.6594), tensor(47.0803), tensor(47.4638), tensor(47.5763), tensor(42.6740), tensor(47.6277)]
# rr, day 50 acc_test tensor(44.2810) train_loss 1.804560618283744
# test_semi_fb acc_test_lst [tensor(45.5516), tensor(34.9550), tensor(42.4188), tensor(43.9716), tensor(43.1159), tensor(46.5328), tensor(47.2826), tensor(47.0377), tensor(42.4908), tensor(47.4453)]
# rr, day 51 acc_test tensor(44.0802) train_loss 1.8183922280365183
# test_semi_fb acc_test_lst [tensor(45.1957), tensor(35.6757), tensor(42.2383), tensor(43.9716), tensor(42.9348), tensor(46.7153), tensor(46.7391), tensor(47.5763), tensor(42.6740), tensor(47.4453)]
# rr, day 52 acc_test tensor(44.1166) train_loss 1.833137614278769


rr_y_lst = []
rr_lst = rr_s.split('\n')
for line in rr_lst:
    if line.startswith("rr, day"):
        line_lst = line.split()
        for a in line_lst:
            if a.startswith("tensor("):
                rr_y_lst.append(float(a.replace("tensor(", "").replace(")", "")))

print(rr_y_lst)



# fb, day 70 acc_test tensor(41.3059) train_loss 2.073375594521229
# test_semi_fb acc_test_lst [tensor(39.1459), tensor(35.3153), tensor(50.1805), tensor(44.8582), tensor(40.2174), tensor(39.2336), tensor(40.2174), tensor(43.9856), tensor(40.2930), tensor(41.6058)]
# fb, day 71 acc_test tensor(41.5053) train_loss 2.0915496653199313
# test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.1351), tensor(49.6390), tensor(44.8582), tensor(39.8551), tensor(39.5985), tensor(40.2174), tensor(43.8061), tensor(39.7436), tensor(41.9708)]
# fb, day 72 acc_test tensor(41.4148) train_loss 2.107992938430415
# test_semi_fb acc_test_lst [tensor(39.5018), tensor(35.8559), tensor(50.1805), tensor(44.6809), tensor(39.3116), tensor(39.0511), tensor(40.0362), tensor(44.5242), tensor(39.9267), tensor(42.5182)]
# fb, day 73 acc_test tensor(41.5587) train_loss 2.125999427615116
# test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.3153), tensor(49.8195), tensor(44.3262), tensor(39.3116), tensor(39.2336), tensor(40.2174), tensor(44.7038), tensor(39.3773), tensor(42.1533)]
# fb, day 74 acc_test tensor(41.3782) train_loss 2.1378308974562565
# test_semi_fb acc_test_lst [tensor(39.3238), tensor(35.4955), tensor(50.), tensor(44.5035), tensor(39.8551), tensor(39.5985), tensor(40.3986), tensor(44.3447), tensor(40.1099), tensor(41.7883)]
# fb, day 75 acc_test tensor(41.5418) train_loss 2.149369612076948


fb_y_lst = []
fb_lst = fb_s.split('\n')
for line in fb_lst:
    if line.startswith("fb, day"):
        line_lst = line.split()
        for a in line_lst:
            if a.startswith("tensor("):
                fb_y_lst.append(float(a.replace("tensor(", "").replace(")", "")))

print(fb_y_lst)

# pla, day 179 acc_test tensor(47.7923) train_loss 1.5908006057965742
# test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(49.8227), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
# pla, day 180 acc_test tensor(47.8101) train_loss 1.5923973135009606
# test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
# pla, day 181 acc_test tensor(47.8279) train_loss 1.5891584546576158
# test_semi_pla acc_test_lst [tensor(42.1708), tensor(38.0180), tensor(50.9025), tensor(50.), tensor(50.5435), tensor(51.4599), tensor(48.7319), tensor(48.8330), tensor(47.6190), tensor(50.)]
# pla, day 182 acc_test tensor(47.8279) train_loss 1.603917001608237


pla_y_lst = []
pla_lst = pla_s.split('\n')
for line in pla_lst:
    if line.startswith("pla, day"):
        line_lst = line.split()
        for a in line_lst:
            if a.startswith("tensor("):
                pla_y_lst.append(float(a.replace("tensor(", "").replace(")", "")))

print(pla_y_lst)


# sep, day 133 acc_test tensor(46.1859) train_loss 0.7026008475462117
# sep, group_id 9 acc_test_lst [tensor(40.9253), tensor(37.1171), tensor(49.0975), tensor(48.4043), tensor(49.4565), tensor(51.0949), tensor(47.2826), tensor(46.4991), tensor(44.8718), tensor(47.6277)]
# sep, day 134 acc_test tensor(46.2377) train_loss 0.7082602661384838
# sep, group_id 9 acc_test_lst [tensor(42.8826), tensor(37.2973), tensor(48.5560), tensor(47.6950), tensor(50.1812), tensor(50.9124), tensor(49.0942), tensor(47.3968), tensor(45.4212), tensor(46.8978)]
# sep, day 135 acc_test tensor(46.6334) train_loss 0.703835976213538
# sep, group_id 9 acc_test_lst [tensor(41.2811), tensor(37.4775), tensor(49.0975), tensor(48.4043), tensor(50.7246), tensor(51.6423), tensor(49.0942), tensor(46.4991), tensor(44.6886), tensor(47.2628)]
# sep, day 136 acc_test tensor(46.6172) train_loss 0.6913180850840939
# sep, group_id 9 acc_test_lst [tensor(42.3488), tensor(37.4775), tensor(48.1949), tensor(49.6454), tensor(50.3623), tensor(51.6423), tensor(48.5507), tensor(46.8582), tensor(45.0549), tensor(47.0803)]
# sep, day 137 acc_test tensor(46.7215) train_loss 0.7014146490320692

sep_y_lst = []
sep_lst = sep_s.split('\n')
for line in sep_lst:
    if line.startswith("sep, day"):
        line_lst = line.split()
        for a in line_lst:
            if a.startswith("tensor("):
                sep_y_lst.append(float(a.replace("tensor(", "").replace(")", "")))

print(sep_y_lst)


# 按照第一个元素对齐，后面补零
max_length = max(len(fedavg_y_lst), len(rr_y_lst), len(fb_y_lst), len(sep_y_lst), len(pla_y_lst))
if len(fedavg_y_lst) < max_length:
    fedavg_y_lst.extend([0] * (max_length-len(fedavg_y_lst)))
if len(rr_y_lst) < max_length:
    rr_y_lst.extend([0] * (max_length-len(rr_y_lst)))
if len(fb_y_lst) < max_length:
    fb_y_lst.extend([0] * (max_length-len(fb_y_lst)))
if len(pla_y_lst) < max_length:
    pla_y_lst.extend([0] * (max_length-len(pla_y_lst)))
if len(sep_y_lst) < max_length:
    sep_y_lst.extend([0] * (max_length-len(sep_y_lst)))


print()

print(fedavg_y_lst)
print(rr_y_lst)
print(fb_y_lst)
print(pla_y_lst)
print(sep_y_lst)

plt.plot(range(max_length), fedavg_y_lst, label="fedavg_y_lst", linestyle=":", marker="o")
plt.plot(range(max_length), rr_y_lst, label="rr_y_lst")
plt.plot(range(max_length), fb_y_lst, label="fb_y_lst")
plt.plot(range(max_length), pla_y_lst, label="pla_y_lst")
plt.plot(range(max_length), sep_y_lst, label="sep_y_lst")
plt.legend()
plt.show()