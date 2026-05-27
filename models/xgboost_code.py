import math
def sigmoid(x):
    if x < 0.0:
        z = math.exp(x)
        return z / (1.0 + z)
    return 1.0 / (1.0 + math.exp(-x))
def score(input):
    if input[3] < 13.0:
        if input[9] < 13.0:
            if input[28] < 117.0:
                var0 = -0.023479339
            else:
                var0 = 0.024327528
        else:
            if input[3] < 10.0:
                var0 = -0.07984637
            else:
                var0 = -0.050662417
    else:
        if input[9] < 16.0:
            if input[9] < 12.0:
                var0 = 0.071016744
            else:
                var0 = 0.029629141
        else:
            if input[3] < 18.0:
                var0 = -0.038998988
            else:
                var0 = 0.012243377
    if input[3] < 13.0:
        if input[9] < 13.0:
            if input[3] < 10.0:
                var1 = -0.024456596
            else:
                var1 = 0.02194187
        else:
            if input[3] < 10.0:
                var1 = -0.07610688
            else:
                var1 = -0.048218228
    else:
        if input[9] < 16.0:
            if input[9] < 10.0:
                var1 = 0.076446444
            else:
                var1 = 0.03647604
        else:
            if input[9] < 22.0:
                var1 = -0.010852824
            else:
                var1 = -0.070847176
    if input[3] < 13.0:
        if input[9] < 13.0:
            if input[28] < -347.0:
                var2 = -0.030944316
            else:
                var2 = 0.016097693
        else:
            if input[28] < -289.0:
                var2 = -0.069751106
            else:
                var2 = -0.041006062
    else:
        if input[9] < 14.0:
            if input[8] < 2.0:
                var2 = 0.0418598
            else:
                var2 = 0.07973589
        else:
            if input[9] < 18.0:
                var2 = 0.014139198
            else:
                var2 = -0.039532963
    if input[3] < 13.0:
        if input[9] < 13.0:
            if input[3] < 10.0:
                var3 = -0.022991348
            else:
                var3 = 0.020704119
        else:
            if input[3] < 10.0:
                var3 = -0.07013316
            else:
                var3 = -0.043287035
    else:
        if input[9] < 14.0:
            if input[8] < 2.0:
                var3 = 0.039853226
            else:
                var3 = 0.076158516
        else:
            if input[9] < 18.0:
                var3 = 0.013435291
            else:
                var3 = -0.037654977
    if input[3] < 14.0:
        if input[9] < 12.0:
            if input[46] < -640.0:
                var4 = -0.025837395
            else:
                var4 = 0.024755953
        else:
            if input[9] < 16.0:
                var4 = -0.030882264
            else:
                var4 = -0.06359139
    else:
        if input[9] < 14.0:
            if input[3] < 18.0:
                var4 = 0.03882202
            else:
                var4 = 0.07070523
        else:
            if input[9] < 20.0:
                var4 = 0.013091265
            else:
                var4 = -0.04843744
    if input[2] < 1.0:
        if input[8] < 1.0:
            if input[28] < -529.0:
                var5 = -0.039456706
            else:
                var5 = 0.016359385
        else:
            if input[0] < 1.0:
                var5 = 0.021381654
            else:
                var5 = 0.06357699
    else:
        if input[3] < 12.0:
            if input[9] < 13.0:
                var5 = -0.027316673
            else:
                var5 = -0.063518174
        else:
            if input[9] < 18.0:
                var5 = 0.010901225
            else:
                var5 = -0.044640306
    if input[3] < 13.0:
        if input[9] < 13.0:
            if input[28] < 117.0:
                var6 = -0.020730622
            else:
                var6 = 0.021311788
        else:
            if input[28] < -289.0:
                var6 = -0.060396593
            else:
                var6 = -0.033094056
    else:
        if input[9] < 12.0:
            if input[3] < 17.0:
                var6 = 0.04033995
            else:
                var6 = 0.06865924
        else:
            if input[3] < 18.0:
                var6 = -0.012606184
            else:
                var6 = 0.03456184
    if input[2] < 1.0:
        if input[8] < 1.0:
            if input[28] < -529.0:
                var7 = -0.036479812
            else:
                var7 = 0.015193532
        else:
            if input[0] < 1.0:
                var7 = 0.019768262
            else:
                var7 = 0.059360933
    else:
        if input[3] < 11.0:
            if input[0] < 1.0:
                var7 = -0.06283885
            else:
                var7 = -0.028895048
        else:
            if input[9] < 18.0:
                var7 = 0.005852638
            else:
                var7 = -0.0442069
    if input[8] < 1.0:
        if input[28] < -364.0:
            if input[46] < 393.0:
                var8 = -0.058195364
            else:
                var8 = -0.02109578
        else:
            if input[46] < -640.0:
                var8 = -0.030218178
            else:
                var8 = 0.014770895
    else:
        if input[28] < 310.0:
            if input[42] < 6496.0:
                var8 = 0.021853946
            else:
                var8 = -0.023425428
        else:
            if input[0] < 1.0:
                var8 = 0.02337544
            else:
                var8 = 0.06002627
    if input[2] < 1.0:
        if input[8] < 1.0:
            if input[28] < -529.0:
                var9 = -0.032930743
            else:
                var9 = 0.014535978
        else:
            if input[0] < 1.0:
                var9 = 0.018152284
            else:
                var9 = 0.05525088
    else:
        if input[3] < 11.0:
            if input[0] < 1.0:
                var9 = -0.059252203
            else:
                var9 = -0.02669827
        else:
            if input[9] < 16.0:
                var9 = 0.010333252
            else:
                var9 = -0.03225385
    if input[9] < 12.0:
        if input[3] < 11.0:
            if input[23] < 1.0:
                var10 = 0.028324762
            else:
                var10 = -0.018046796
        else:
            if input[3] < 17.0:
                var10 = 0.032999504
            else:
                var10 = 0.061919745
    else:
        if input[3] < 14.0:
            if input[9] < 18.0:
                var10 = -0.029342253
            else:
                var10 = -0.05978323
        else:
            if input[9] < 20.0:
                var10 = 0.015605333
            else:
                var10 = -0.04209034
    if input[2] < 1.0:
        if input[3] < 18.0:
            if input[9] < 11.0:
                var11 = 0.03214337
            else:
                var11 = -0.0065012486
        else:
            if input[9] < 18.0:
                var11 = 0.060618486
            else:
                var11 = -0.008150688
    else:
        if input[28] < 310.0:
            if input[46] < 1758.0:
                var11 = -0.044047777
            else:
                var11 = 0.010404371
        else:
            if input[38] < 6704.0:
                var11 = -0.011371619
            else:
                var11 = 0.032067947
    if input[3] < 12.0:
        if input[9] < 13.0:
            if input[28] < -347.0:
                var12 = -0.026038995
            else:
                var12 = 0.007228292
        else:
            if input[37] < 1117.0:
                var12 = -0.05066922
            else:
                var12 = 0.0006813045
    else:
        if input[9] < 14.0:
            if input[8] < 2.0:
                var12 = 0.02719143
            else:
                var12 = 0.05873409
        else:
            if input[3] < 18.0:
                var12 = -0.02061772
            else:
                var12 = 0.023417605
    if input[28] < 310.0:
        if input[46] < 393.0:
            if input[37] < -546.0:
                var13 = -0.055835623
            else:
                var13 = -0.022815188
        else:
            if input[37] < 7.0:
                var13 = -0.011308496
            else:
                var13 = 0.027887726
    else:
        if input[46] < -793.0:
            if input[11] < 5405.0:
                var13 = -0.035936043
            else:
                var13 = 0.010933757
        else:
            if input[19] < -960.0:
                var13 = 0.01279289
            else:
                var13 = 0.048722874
    if input[8] < 1.0:
        if input[9] < 16.0:
            if input[28] < 46.0:
                var14 = -0.025367305
            else:
                var14 = 0.010180157
        else:
            if input[3] < 11.0:
                var14 = -0.058862664
            else:
                var14 = -0.032746293
    else:
        if input[3] < 17.0:
            if input[33] < 5925.0:
                var14 = 0.023557406
            else:
                var14 = -0.014215069
        else:
            if input[9] < 18.0:
                var14 = 0.0511343
            else:
                var14 = -0.003869369
    if input[2] < 1.0:
        if input[0] < 1.0:
            if input[8] < 2.0:
                var15 = -0.009036831
            else:
                var15 = 0.04078083
        else:
            if input[3] < 17.0:
                var15 = 0.023222296
            else:
                var15 = 0.057128098
    else:
        if input[28] < 510.0:
            if input[46] < 393.0:
                var15 = -0.042672362
            else:
                var15 = -0.00791433
        else:
            if input[2] < 2.0:
                var15 = 0.016434258
            else:
                var15 = -0.027481511
    if input[9] < 12.0:
        if input[3] < 11.0:
            if input[23] < 1.0:
                var16 = 0.025823427
            else:
                var16 = -0.016264228
        else:
            if input[9] < 8.0:
                var16 = 0.057799477
            else:
                var16 = 0.02971805
    else:
        if input[3] < 15.0:
            if input[9] < 18.0:
                var16 = -0.022111183
            else:
                var16 = -0.05061247
        else:
            if input[9] < 20.0:
                var16 = 0.017329276
            else:
                var16 = -0.038047902
    if input[8] < 1.0:
        if input[28] < -397.0:
            if input[46] < 64.0:
                var17 = -0.048508663
            else:
                var17 = -0.019136027
        else:
            if input[46] < -640.0:
                var17 = -0.024151575
            else:
                var17 = 0.011819522
    else:
        if input[28] < 104.0:
            if input[37] < 1328.0:
                var17 = -0.009386274
            else:
                var17 = 0.03812721
        else:
            if input[0] < 1.0:
                var17 = 0.014813139
            else:
                var17 = 0.047076922
    if input[0] < 1.0:
        if input[3] < 10.0:
            if input[2] < 1.0:
                var18 = -0.02148438
            else:
                var18 = -0.053111997
        else:
            if input[8] < 2.0:
                var18 = -0.013812794
            else:
                var18 = 0.03221505
    else:
        if input[3] < 18.0:
            if input[9] < 13.0:
                var18 = 0.024036719
            else:
                var18 = -0.013580161
        else:
            if input[19] < -2654.0:
                var18 = -0.030411353
            else:
                var18 = 0.053499904
    if input[2] < 1.0:
        if input[0] < 1.0:
            if input[8] < 2.0:
                var19 = -0.0075381747
            else:
                var19 = 0.036891308
        else:
            if input[3] < 17.0:
                var19 = 0.020625662
            else:
                var19 = 0.052264877
    else:
        if input[3] < 11.0:
            if input[0] < 1.0:
                var19 = -0.047598895
            else:
                var19 = -0.017476017
        else:
            if input[9] < 18.0:
                var19 = 0.004003025
            else:
                var19 = -0.03165712
    if input[28] < 310.0:
        if input[46] < 393.0:
            if input[37] < -546.0:
                var20 = -0.048759975
            else:
                var20 = -0.017999656
        else:
            if input[11] < 5131.0:
                var20 = -0.01675461
            else:
                var20 = 0.019087253
    else:
        if input[46] < -516.0:
            if input[29] < 5622.0:
                var20 = -0.029192293
            else:
                var20 = 0.0117451595
        else:
            if input[37] < 359.0:
                var20 = 0.02016446
            else:
                var20 = 0.0498584
    if input[9] < 12.0:
        if input[3] < 11.0:
            if input[19] < -1261.0:
                var21 = -0.034451433
            else:
                var21 = 0.0017990184
        else:
            if input[9] < 10.0:
                var21 = 0.043992713
            else:
                var21 = 0.017878754
    else:
        if input[3] < 18.0:
            if input[3] < 10.0:
                var21 = -0.042351883
            else:
                var21 = -0.013768196
        else:
            if input[9] < 20.0:
                var21 = 0.029948806
            else:
                var21 = -0.02998283
    if input[8] < 1.0:
        if input[9] < 16.0:
            if input[20] < 6644.0:
                var22 = -0.017074868
            else:
                var22 = 0.014578841
        else:
            if input[11] < 4958.0:
                var22 = -0.052224804
            else:
                var22 = -0.026529789
    else:
        if input[37] < 601.0:
            if input[28] < 310.0:
                var22 = -0.010761276
            else:
                var22 = 0.021755496
        else:
            if input[46] < 370.0:
                var22 = 0.017900614
            else:
                var22 = 0.050150927
    if input[0] < 1.0:
        if input[2] < 2.0:
            if input[8] < 2.0:
                var23 = -0.014174016
            else:
                var23 = 0.030153805
        else:
            if input[27] < 2.0:
                var23 = -0.056281388
            else:
                var23 = -0.03246741
    else:
        if input[3] < 18.0:
            if input[9] < 13.0:
                var23 = 0.020893678
            else:
                var23 = -0.011295007
        else:
            if input[19] < -2654.0:
                var23 = -0.030690795
            else:
                var23 = 0.048452113
    if input[28] < -529.0:
        if input[46] < 393.0:
            if input[37] < -546.0:
                var24 = -0.049996745
            else:
                var24 = -0.023639068
        else:
            if input[11] < 6065.0:
                var24 = -0.014968621
            else:
                var24 = 0.021932704
    else:
        if input[46] < -516.0:
            if input[19] < -283.0:
                var24 = -0.031912323
            else:
                var24 = 0.0028391876
        else:
            if input[19] < -892.0:
                var24 = 0.001436443
            else:
                var24 = 0.03522834
    if input[28] < 606.0:
        if input[46] < 413.0:
            if input[37] < -546.0:
                var25 = -0.042690486
            else:
                var25 = -0.013083289
        else:
            if input[37] < 150.0:
                var25 = -0.0065946304
            else:
                var25 = 0.025622193
    else:
        if input[46] < -793.0:
            if input[11] < 5405.0:
                var25 = -0.027736498
            else:
                var25 = 0.014781627
        else:
            if input[33] < 7217.0:
                var25 = 0.03609093
            else:
                var25 = -0.020981187
    if input[0] < 1.0:
        if input[11] < 5424.0:
            if input[37] < 1277.0:
                var26 = -0.037037276
            else:
                var26 = 0.0044671944
        else:
            if input[29] < 5844.0:
                var26 = -0.016550561
            else:
                var26 = 0.01418691
    else:
        if input[3] < 18.0:
            if input[9] < 16.0:
                var26 = 0.014124473
            else:
                var26 = -0.02340462
        else:
            if input[19] < -2654.0:
                var26 = -0.030187448
            else:
                var26 = 0.045927864
    if input[2] < 1.0:
        if input[6] < 2.0:
            if input[28] < -364.0:
                var27 = 0.00087187265
            else:
                var27 = 0.030759294
        else:
            if input[20] < 7193.0:
                var27 = -0.024820916
            else:
                var27 = 0.028862325
    else:
        if input[3] < 10.0:
            if input[0] < 1.0:
                var27 = -0.045182057
            else:
                var27 = -0.015792426
        else:
            if input[9] < 22.0:
                var27 = -0.0022288386
            else:
                var27 = -0.046632886
    if input[8] < 1.0:
        if input[28] < -397.0:
            if input[46] < 64.0:
                var28 = -0.039339025
            else:
                var28 = -0.013726904
        else:
            if input[46] < -1493.0:
                var28 = -0.025727073
            else:
                var28 = 0.004630564
    else:
        if input[37] < 601.0:
            if input[28] < 1394.0:
                var28 = -0.0034326438
            else:
                var28 = 0.03263406
        else:
            if input[46] < 370.0:
                var28 = 0.015811797
            else:
                var28 = 0.045374118
    if input[6] < 1.0:
        if input[19] < -222.0:
            if input[46] < -603.0:
                var29 = -0.02741145
            else:
                var29 = 0.012522568
        else:
            if input[42] < 6307.0:
                var29 = 0.048723582
            else:
                var29 = 0.01979675
    else:
        if input[28] < -761.0:
            if input[28] < -1814.0:
                var29 = -0.04803216
            else:
                var29 = -0.02116604
        else:
            if input[19] < -382.0:
                var29 = -0.017514264
            else:
                var29 = 0.008696279
    if input[9] < 12.0:
        if input[3] < 11.0:
            if input[23] < 1.0:
                var30 = 0.024371654
            else:
                var30 = -0.012672441
        else:
            if input[9] < 8.0:
                var30 = 0.04659351
            else:
                var30 = 0.019915443
    else:
        if input[3] < 12.0:
            if input[37] < 1117.0:
                var30 = -0.03172397
            else:
                var30 = 0.014286952
        else:
            if input[9] < 22.0:
                var30 = 0.0026105111
            else:
                var30 = -0.04277342
    if input[8] < 2.0:
        if input[28] < -529.0:
            if input[28] < -1749.0:
                var31 = -0.041268643
            else:
                var31 = -0.016578194
        else:
            if input[46] < -543.0:
                var31 = -0.011076669
            else:
                var31 = 0.014295034
    else:
        if input[9] < 10.0:
            if input[19] < -783.0:
                var31 = -0.00049740734
            else:
                var31 = 0.05281357
        else:
            if input[38] < 6704.0:
                var31 = 0.002200729
            else:
                var31 = 0.03120162
    if input[28] < 606.0:
        if input[46] < 413.0:
            if input[37] < -546.0:
                var32 = -0.038240727
            else:
                var32 = -0.010590269
        else:
            if input[37] < 150.0:
                var32 = -0.0055022365
            else:
                var32 = 0.022095073
    else:
        if input[19] < -996.0:
            if input[3] < 10.0:
                var32 = -0.04253811
            else:
                var32 = 0.0037514742
        else:
            if input[0] < 1.0:
                var32 = 0.008216652
            else:
                var32 = 0.04023707
    if input[9] < 16.0:
        if input[3] < 17.0:
            if input[9] < 7.0:
                var33 = 0.037647393
            else:
                var33 = -0.002763447
        else:
            if input[24] < 6753.0:
                var33 = 0.038288157
            else:
                var33 = 0.009272131
    else:
        if input[3] < 16.0:
            if input[11] < 5267.0:
                var33 = -0.041438885
            else:
                var33 = -0.018955968
        else:
            if input[9] < 22.0:
                var33 = 0.009775525
            else:
                var33 = -0.043286543
    if input[6] < 1.0:
        if input[19] < -222.0:
            if input[37] < -1753.0:
                var34 = -0.046552863
            else:
                var34 = 0.008123114
        else:
            if input[42] < 6307.0:
                var34 = 0.045410883
            else:
                var34 = 0.017932959
    else:
        if input[37] < -929.0:
            if input[12] < 139.0:
                var34 = -0.033490762
            else:
                var34 = 0.00839587
        else:
            if input[19] < -817.0:
                var34 = -0.020192612
            else:
                var34 = 0.0062158545
    if input[37] < 345.0:
        if input[19] < 1953.0:
            if input[46] < 710.0:
                var35 = -0.024964435
            else:
                var35 = 0.0010289453
        else:
            if input[42] < 7706.0:
                var35 = 0.030938584
            else:
                var35 = -0.02608271
    else:
        if input[46] < 1426.0:
            if input[28] < 62.0:
                var35 = -0.008330986
            else:
                var35 = 0.020481719
        else:
            if input[28] < -1125.0:
                var35 = 0.00911718
            else:
                var35 = 0.046967562
    if input[0] < 1.0:
        if input[11] < 5424.0:
            if input[46] < -46.0:
                var36 = -0.038285848
            else:
                var36 = -0.012753378
        else:
            if input[46] < -2468.0:
                var36 = -0.033269256
            else:
                var36 = 0.0043336577
    else:
        if input[3] < 18.0:
            if input[33] < 5992.0:
                var36 = 0.015466439
            else:
                var36 = -0.011636953
        else:
            if input[19] < -2654.0:
                var36 = -0.03203128
            else:
                var36 = 0.039721828
    if input[28] < 374.0:
        if input[42] < 6868.0:
            if input[11] < 6731.0:
                var37 = -0.0057845
            else:
                var37 = 0.030409468
        else:
            if input[37] < 1342.0:
                var37 = -0.031769197
            else:
                var37 = 0.0115955565
    else:
        if input[46] < 246.0:
            if input[15] < 5724.0:
                var37 = 0.013638476
            else:
                var37 = -0.016896125
        else:
            if input[29] < 5013.0:
                var37 = -0.014846313
            else:
                var37 = 0.033577424
    if input[8] < 2.0:
        if input[28] < -529.0:
            if input[28] < -1749.0:
                var38 = -0.03795332
            else:
                var38 = -0.013609654
        else:
            if input[46] < -1540.0:
                var38 = -0.01757452
            else:
                var38 = 0.0092076585
    else:
        if input[9] < 10.0:
            if input[19] < -783.0:
                var38 = -0.0054095914
            else:
                var38 = 0.049077567
        else:
            if input[363] < 1.0:
                var38 = 0.02128995
            else:
                var38 = -0.048167326
    if input[37] < -34.0:
        if input[28] < 895.0:
            if input[46] < 393.0:
                var39 = -0.028948253
            else:
                var39 = -0.004121735
        else:
            if input[37] < -2175.0:
                var39 = -0.029651267
            else:
                var39 = 0.015185787
    else:
        if input[42] < 6487.0:
            if input[19] < -892.0:
                var39 = 0.0072305943
            else:
                var39 = 0.033719745
        else:
            if input[20] < 7254.0:
                var39 = -0.010179038
            else:
                var39 = 0.026901964
    if input[6] < 1.0:
        if input[19] < -892.0:
            if input[37] < 111.0:
                var40 = -0.018595379
            else:
                var40 = 0.011212687
        else:
            if input[46] < 710.0:
                var40 = 0.0140096545
            else:
                var40 = 0.040093668
    else:
        if input[28] < -1582.0:
            if input[21] < 117.0:
                var40 = -0.0404733
            else:
                var40 = 0.014669952
        else:
            if input[11] < 5029.0:
                var40 = -0.021684183
            else:
                var40 = 0.0031652153
    if input[37] < 804.0:
        if input[19] < 498.0:
            if input[46] < 710.0:
                var41 = -0.027097492
            else:
                var41 = 0.0018082956
        else:
            if input[46] < -2082.0:
                var41 = -0.023015058
            else:
                var41 = 0.012740383
    else:
        if input[19] < -1072.0:
            if input[46] < -348.0:
                var41 = -0.027927304
            else:
                var41 = 0.008093591
        else:
            if input[28] < 104.0:
                var41 = 0.010718859
            else:
                var41 = 0.037854735
    if input[9] < 18.0:
        if input[6] < 2.0:
            if input[3] < 18.0:
                var42 = 0.00479502
            else:
                var42 = 0.03289105
        else:
            if input[34] < 110.0:
                var42 = 0.007597317
            else:
                var42 = -0.023061803
    else:
        if input[34] < 92.0:
            if input[52] < 17.0:
                var42 = -0.020193607
            else:
                var42 = 0.0484513
        else:
            if input[38] < 6411.0:
                var42 = -0.040751513
            else:
                var42 = -0.014089777
    if input[28] < 1369.0:
        if input[37] < -1351.0:
            if input[11] < 4943.0:
                var43 = -0.051485475
            else:
                var43 = -0.018983953
        else:
            if input[46] < -617.0:
                var43 = -0.014962365
            else:
                var43 = 0.009066176
    else:
        if input[11] < 4701.0:
            if input[28] < 2233.0:
                var43 = -0.028552532
            else:
                var43 = 0.025430951
        else:
            if input[0] < 1.0:
                var43 = 0.014772045
            else:
                var43 = 0.039329343
    if input[28] < -529.0:
        if input[46] < 2071.0:
            if input[37] < -1351.0:
                var44 = -0.041433796
            else:
                var44 = -0.013514104
        else:
            if input[34] < 135.0:
                var44 = 0.027006289
            else:
                var44 = -0.02046059
    else:
        if input[11] < 4701.0:
            if input[25] < 95.0:
                var44 = 0.0063557136
            else:
                var44 = -0.025307233
        else:
            if input[46] < -1540.0:
                var44 = -0.011985596
            else:
                var44 = 0.018737163
    var45 = var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44
    if input[37] < 804.0:
        if input[19] < 2048.0:
            if input[46] < 978.0:
                var46 = -0.018045833
            else:
                var46 = 0.006301742
        else:
            if input[42] < 7690.0:
                var46 = 0.029200679
            else:
                var46 = -0.014345746
    else:
        if input[19] < -1540.0:
            if input[42] < 5085.0:
                var46 = 0.05487029
            else:
                var46 = -0.016006004
        else:
            if input[46] < -603.0:
                var46 = 0.0065349727
            else:
                var46 = 0.03426429
    if input[6] < 2.0:
        if input[37] < -1236.0:
            if input[12] < 107.0:
                var47 = -0.037096336
            else:
                var47 = -0.008023699
        else:
            if input[19] < 1923.0:
                var47 = 0.006280852
            else:
                var47 = 0.035510983
    else:
        if input[19] < -426.0:
            if input[55] < 1412.0:
                var47 = -0.037959974
            else:
                var47 = 0.03684288
        else:
            if input[29] < 5702.0:
                var47 = -0.024705857
            else:
                var47 = 0.006585756
    if input[28] < 606.0:
        if input[46] < 2071.0:
            if input[37] < -34.0:
                var48 = -0.020865362
            else:
                var48 = -0.00072910386
        else:
            if input[29] < 6427.0:
                var48 = 0.012474082
            else:
                var48 = 0.047283094
    else:
        if input[15] < 5645.0:
            if input[29] < 5546.0:
                var48 = 0.0022079886
            else:
                var48 = 0.033102762
        else:
            if input[46] < 853.0:
                var48 = -0.010132338
            else:
                var48 = 0.018569523
    if input[6] < 1.0:
        if input[19] < -222.0:
            if input[37] < -1883.0:
                var49 = -0.045985363
            else:
                var49 = 0.0051583196
        else:
            if input[42] < 6307.0:
                var49 = 0.03877961
            else:
                var49 = 0.013939914
    else:
        if input[28] < -1814.0:
            if input[11] < 6332.0:
                var49 = -0.046374913
            else:
                var49 = -0.0105670765
        else:
            if input[37] < 1361.0:
                var49 = -0.007445653
            else:
                var49 = 0.021667613
    if input[28] < 1369.0:
        if input[46] < -603.0:
            if input[19] < -783.0:
                var50 = -0.033927828
            else:
                var50 = -0.010437757
        else:
            if input[37] < 866.0:
                var50 = -0.0031625747
            else:
                var50 = 0.023019386
    else:
        if input[19] < -324.0:
            if input[18] < 4.0:
                var50 = -0.0020009407
            else:
                var50 = 0.044676214
        else:
            if input[55] < -1406.0:
                var50 = -0.04316396
            else:
                var50 = 0.035190564
    if input[28] < -1582.0:
        if input[21] < 117.0:
            if input[11] < 6285.0:
                var51 = -0.037088916
            else:
                var51 = -0.0074901953
        else:
            if input[29] < 5974.0:
                var51 = -0.023920303
            else:
                var51 = 0.06653624
    else:
        if input[6] < 2.0:
            if input[33] < 5992.0:
                var51 = 0.016140522
            else:
                var51 = -0.0038269472
        else:
            if input[19] < -324.0:
                var51 = -0.03133852
            else:
                var51 = -0.005316434
    if input[9] < 18.0:
        if input[3] < 18.0:
            if input[19] < -892.0:
                var52 = -0.013413126
            else:
                var52 = 0.0055964454
        else:
            if input[39] < 102.0:
                var52 = -0.013364044
            else:
                var52 = 0.030004844
    else:
        if input[34] < 92.0:
            if input[52] < 17.0:
                var52 = -0.018604418
            else:
                var52 = 0.046984937
        else:
            if input[38] < 6411.0:
                var52 = -0.037091386
            else:
                var52 = -0.010826971
    if input[46] < 2071.0:
        if input[19] < -1072.0:
            if input[3] < 10.0:
                var53 = -0.03537948
            else:
                var53 = -0.01080115
        else:
            if input[6] < 1.0:
                var53 = 0.01787713
            else:
                var53 = -0.0038723962
    else:
        if input[21] < 105.0:
            if input[37] < 388.0:
                var53 = -0.008373267
            else:
                var53 = 0.03586742
        else:
            if input[33] < 6850.0:
                var53 = 0.043244317
            else:
                var53 = 0.00013502713
    if input[28] < 1369.0:
        if input[37] < -1351.0:
            if input[11] < 4943.0:
                var54 = -0.047061946
            else:
                var54 = -0.015173698
        else:
            if input[39] < 108.0:
                var54 = -0.019079762
            else:
                var54 = 0.005420008
    else:
        if input[19] < -2737.0:
            if input[29] < 6287.0:
                var54 = 0.0060883905
            else:
                var54 = -0.08360626
        else:
            if input[55] < -1406.0:
                var54 = -0.030530408
            else:
                var54 = 0.025886511
    if input[28] < -1582.0:
        if input[21] < 117.0:
            if input[11] < 6332.0:
                var55 = -0.03530924
            else:
                var55 = -0.006824712
        else:
            if input[29] < 5974.0:
                var55 = -0.023181396
            else:
                var55 = 0.064017214
    else:
        if input[46] < 710.0:
            if input[19] < 2048.0:
                var55 = -0.007492242
            else:
                var55 = 0.020022456
        else:
            if input[11] < 4958.0:
                var55 = -0.001934298
            else:
                var55 = 0.022726048
    if input[6] < 2.0:
        if input[9] < 9.0:
            if input[18] < 3.0:
                var56 = 0.007248651
            else:
                var56 = 0.04222918
        else:
            if input[37] < -1959.0:
                var56 = -0.026568199
            else:
                var56 = 0.0030807857
    else:
        if input[15] < 5943.0:
            if input[34] < 110.0:
                var56 = 0.017207105
            else:
                var56 = -0.016696462
        else:
            if input[81] < 1.0:
                var56 = -0.03748998
            else:
                var56 = 0.031236509
    if input[28] < -529.0:
        if input[34] < 111.0:
            if input[39] < 114.0:
                var57 = -0.01800332
            else:
                var57 = 0.019424437
        else:
            if input[6] < 2.0:
                var57 = -0.011531249
            else:
                var57 = -0.0380727
    else:
        if input[11] < 4701.0:
            if input[25] < 95.0:
                var57 = 0.007059054
            else:
                var57 = -0.022264428
        else:
            if input[46] < -1540.0:
                var57 = -0.01074075
            else:
                var57 = 0.015884407
    if input[46] < 2071.0:
        if input[28] < 923.0:
            if input[11] < 4958.0:
                var58 = -0.025254209
            else:
                var58 = -0.0029775188
        else:
            if input[15] < 5507.0:
                var58 = 0.021781111
            else:
                var58 = 0.0009158981
    else:
        if input[21] < 105.0:
            if input[37] < 388.0:
                var58 = -0.00820293
            else:
                var58 = 0.034121748
        else:
            if input[48] < 29.0:
                var58 = 0.039289907
            else:
                var58 = -0.018450525
    if input[37] < 804.0:
        if input[19] < 2132.0:
            if input[46] < 710.0:
                var59 = -0.015497759
            else:
                var59 = 0.0035010893
        else:
            if input[42] < 7690.0:
                var59 = 0.026995003
            else:
                var59 = -0.012335075
    else:
        if input[19] < -1540.0:
            if input[25] < 84.0:
                var59 = 0.054688293
            else:
                var59 = -0.014517832
        else:
            if input[21] < 113.0:
                var59 = 0.009452244
            else:
                var59 = 0.037038725
    if input[28] < -1582.0:
        if input[43] < 95.0:
            if input[412] < 1.0:
                var60 = 0.041544944
            else:
                var60 = -0.025145793
        else:
            if input[0] < 2.0:
                var60 = -0.030499
            else:
                var60 = 0.010387448
    else:
        if input[33] < 5992.0:
            if input[42] < 6496.0:
                var60 = 0.019251399
            else:
                var60 = 0.00048983004
        else:
            if input[11] < 6167.0:
                var60 = -0.012705922
            else:
                var60 = 0.00808889
    if input[6] < 2.0:
        if input[37] < -1236.0:
            if input[12] < 107.0:
                var61 = -0.0319913
            else:
                var61 = -0.005390245
        else:
            if input[39] < 118.0:
                var61 = -0.0030169908
            else:
                var61 = 0.015673993
    else:
        if input[11] < 4979.0:
            if input[318] < 1.0:
                var61 = -0.036495704
            else:
                var61 = 0.04312
        else:
            if input[29] < 5702.0:
                var61 = -0.020812212
            else:
                var61 = 0.0022385304
    if input[28] < 1369.0:
        if input[37] < 1342.0:
            if input[42] < 6868.0:
                var62 = -0.00033865005
            else:
                var62 = -0.01843368
        else:
            if input[15] < 6565.0:
                var62 = 0.023566253
            else:
                var62 = -0.011582257
    else:
        if input[19] < -25.0:
            if input[425] < 1.0:
                var62 = -0.012784781
            else:
                var62 = 0.020624904
        else:
            if input[55] < -1406.0:
                var62 = -0.054840088
            else:
                var62 = 0.03266704
    if input[6] < 1.0:
        if input[15] < 5019.0:
            if input[26] < 7.0:
                var63 = 0.035905268
            else:
                var63 = -0.039235692
        else:
            if input[46] < 603.0:
                var63 = -0.0075248256
            else:
                var63 = 0.01572255
    else:
        if input[28] < -1814.0:
            if input[25] < 97.0:
                var63 = 0.015165932
            else:
                var63 = -0.03798308
        else:
            if input[37] < 1361.0:
                var63 = -0.0058689895
            else:
                var63 = 0.018073697
    if input[37] < -1959.0:
        if input[19] < 3477.0:
            if input[38] < 7883.0:
                var64 = -0.03457122
            else:
                var64 = 0.00854536
        else:
            var64 = 0.061803777
    else:
        if input[28] < 1469.0:
            if input[46] < -1540.0:
                var64 = -0.017691033
            else:
                var64 = 0.003183679
        else:
            if input[19] < -133.0:
                var64 = 0.0062442734
            else:
                var64 = 0.032181494
    if input[46] < 2071.0:
        if input[19] < 2048.0:
            if input[0] < 2.0:
                var65 = -0.00884346
            else:
                var65 = 0.018822167
        else:
            if input[46] < -2992.0:
                var65 = -0.04709023
            else:
                var65 = 0.022774588
    else:
        if input[21] < 105.0:
            if input[425] < 1.0:
                var65 = -0.017030869
            else:
                var65 = 0.022526529
        else:
            if input[48] < 29.0:
                var65 = 0.036857728
            else:
                var65 = -0.020157237
    if input[28] < -1582.0:
        if input[21] < 117.0:
            if input[11] < 6332.0:
                var66 = -0.031510476
            else:
                var66 = -0.003918288
        else:
            if input[29] < 5974.0:
                var66 = -0.020283539
            else:
                var66 = 0.06260545
    else:
        if input[38] < 7020.0:
            if input[28] < 1900.0:
                var66 = -0.005426228
            else:
                var66 = 0.022271229
        else:
            if input[15] < 6147.0:
                var66 = 0.021720802
            else:
                var66 = -0.002523639
    if input[37] < -1959.0:
        if input[19] < 3477.0:
            if input[38] < 7883.0:
                var67 = -0.033214938
            else:
                var67 = 0.0072613056
        else:
            var67 = 0.0592438
    else:
        if input[21] < 104.0:
            if input[11] < 6880.0:
                var67 = -0.009766658
            else:
                var67 = 0.020669091
        else:
            if input[46] < 1890.0:
                var67 = 0.0049118097
            else:
                var67 = 0.030671371
    if input[11] < 4958.0:
        if input[37] < -1753.0:
            if input[5] < 2.0:
                var68 = -0.059147913
            else:
                var68 = -0.008761897
        else:
            if input[42] < 5059.0:
                var68 = 0.029636666
            else:
                var68 = -0.011874209
    else:
        if input[46] < -2468.0:
            if input[12] < 128.0:
                var68 = -0.031855207
            else:
                var68 = -0.0013780349
        else:
            if input[21] < 113.0:
                var68 = 0.0014613714
            else:
                var68 = 0.01925707
    if input[6] < 2.0:
        if input[19] < 1923.0:
            if input[46] < 2071.0:
                var69 = -0.0026336603
            else:
                var69 = 0.019743647
        else:
            if input[23] < 4.0:
                var69 = 0.029336214
            else:
                var69 = -0.0066635646
    else:
        if input[15] < 5943.0:
            if input[34] < 110.0:
                var69 = 0.01695663
            else:
                var69 = -0.014080326
        else:
            if input[55] < 1223.0:
                var69 = -0.033692632
            else:
                var69 = 0.03745642
    if input[28] < 310.0:
        if input[37] < 1342.0:
            if input[42] < 6868.0:
                var70 = -0.0029155945
            else:
                var70 = -0.021494064
        else:
            if input[46] < -3265.0:
                var70 = -0.04618335
            else:
                var70 = 0.017567953
    else:
        if input[349] < 1.0:
            if input[30] < 119.0:
                var70 = 0.0004227685
            else:
                var70 = 0.017526342
        else:
            if input[46] < 775.0:
                var70 = -0.050370347
            else:
                var70 = 0.009704108
    if input[37] < -929.0:
        if input[12] < 139.0:
            if input[46] < 393.0:
                var71 = -0.027081564
            else:
                var71 = -0.0049420022
        else:
            if input[24] < 6173.0:
                var71 = 0.044525202
            else:
                var71 = -0.0044981516
    else:
        if input[21] < 104.0:
            if input[11] < 6088.0:
                var71 = -0.011379251
            else:
                var71 = 0.008565347
        else:
            if input[11] < 4632.0:
                var71 = -0.013180307
            else:
                var71 = 0.015004545
    if input[9] < 7.0:
        if input[46] < -1130.0:
            if input[18] < 5.0:
                var72 = -0.061058294
            else:
                var72 = 0.025645195
        else:
            if input[29] < 5489.0:
                var72 = 0.0034879127
            else:
                var72 = 0.043802496
    else:
        if input[0] < 2.0:
            if input[28] < -1684.0:
                var72 = -0.025303189
            else:
                var72 = -0.0017655758
        else:
            if input[85] < 1.0:
                var72 = 0.023238016
            else:
                var72 = -0.031785205
    if input[6] < 2.0:
        if input[19] < 1923.0:
            if input[39] < 129.0:
                var73 = -0.004954783
            else:
                var73 = 0.0109672835
        else:
            if input[23] < 4.0:
                var73 = 0.027863
            else:
                var73 = -0.0057590897
    else:
        if input[15] < 5943.0:
            if input[34] < 110.0:
                var73 = 0.016133215
            else:
                var73 = -0.013236741
        else:
            if input[81] < 1.0:
                var73 = -0.03223965
            else:
                var73 = 0.037267406
    if input[19] < -892.0:
        if input[2] < 3.0:
            if input[37] < -1852.0:
                var74 = -0.041356057
            else:
                var74 = -0.004641458
        else:
            if input[261] < 1.0:
                var74 = -0.053231474
            else:
                var74 = 0.01885253
    else:
        if input[46] < 2308.0:
            if input[19] < 2862.0:
                var74 = 0.00006961258
            else:
                var74 = 0.028799636
        else:
            if input[37] < 150.0:
                var74 = 0.015207804
            else:
                var74 = 0.0484746
    if input[37] < 1342.0:
        if input[28] < 1369.0:
            if input[19] < 2862.0:
                var75 = -0.007559077
            else:
                var75 = 0.02704595
        else:
            if input[425] < 1.0:
                var75 = -0.001400864
            else:
                var75 = 0.026049206
    else:
        if input[15] < 6474.0:
            if input[46] < -617.0:
                var75 = 0.0084914155
            else:
                var75 = 0.03130292
        else:
            if input[30] < 129.0:
                var75 = 0.01573601
            else:
                var75 = -0.03175379
    if input[28] < -1582.0:
        if input[43] < 95.0:
            if input[120] < 1.0:
                var76 = 0.033339962
            else:
                var76 = -0.041197132
        else:
            if input[331] < 1.0:
                var76 = -0.025780383
            else:
                var76 = 0.023505567
    else:
        if input[38] < 7020.0:
            if input[28] < 1900.0:
                var76 = -0.0048218374
            else:
                var76 = 0.020074824
        else:
            if input[15] < 6147.0:
                var76 = 0.019369034
            else:
                var76 = -0.0022019136
    if input[37] < -1959.0:
        if input[12] < 109.0:
            if input[11] < 6274.0:
                var77 = -0.047555756
            else:
                var77 = 0.01698724
        else:
            if input[38] < 7923.0:
                var77 = -0.017381696
            else:
                var77 = 0.039972723
    else:
        if input[46] < -2425.0:
            if input[12] < 135.0:
                var77 = -0.025860105
            else:
                var77 = 0.007814432
        else:
            if input[19] < 1408.0:
                var77 = 0.0005102552
            else:
                var77 = 0.018236589
    if input[37] < 345.0:
        if input[11] < 4958.0:
            if input[24] < 5727.0:
                var78 = 0.0077765407
            else:
                var78 = -0.024404183
        else:
            if input[46] < -2195.0:
                var78 = -0.02240355
            else:
                var78 = 0.002226237
    else:
        if input[46] < 1426.0:
            if input[20] < 6974.0:
                var78 = -0.0031245477
            else:
                var78 = 0.018259903
        else:
            if input[48] < 28.0:
                var78 = 0.031941347
            else:
                var78 = -0.014623256
    if input[6] < 2.0:
        if input[9] < 7.0:
            if input[19] < -976.0:
                var79 = -0.009822795
            else:
                var79 = 0.037116893
        else:
            if input[33] < 7651.0:
                var79 = 0.002913978
            else:
                var79 = -0.032066394
    else:
        if input[20] < 5315.0:
            if input[249] < 1.0:
                var79 = -0.043804538
            else:
                var79 = 0.030708132
        else:
            if input[349] < 1.0:
                var79 = -0.006532315
            else:
                var79 = -0.054499146
    if input[9] < 22.0:
        if input[28] < 2233.0:
            if input[29] < 6240.0:
                var80 = -0.004483602
            else:
                var80 = 0.009461952
        else:
            if input[429] < 1.0:
                var80 = 0.03222276
            else:
                var80 = -0.05156851
    else:
        if input[34] < 78.0:
            var80 = 0.060145862
        else:
            if input[44] < 2.0:
                var80 = 0.024441622
            else:
                var80 = -0.037447106
    if input[0] < 2.0:
        if input[28] < -1749.0:
            if input[43] < 95.0:
                var81 = 0.01833622
            else:
                var81 = -0.028628672
        else:
            if input[11] < 4701.0:
                var81 = -0.014655578
            else:
                var81 = 0.0026933397
    else:
        if input[11] < 6167.0:
            if input[33] < 6013.0:
                var81 = 0.018883867
            else:
                var81 = -0.008984192
        else:
            if input[43] < 138.0:
                var81 = 0.04855572
            else:
                var81 = -0.04416352
    if input[6] < 2.0:
        if input[18] < 3.0:
            if input[271] < 1.0:
                var82 = -0.0015495301
            else:
                var82 = -0.04606122
        else:
            if input[9] < 9.0:
                var82 = 0.035326626
            else:
                var82 = 0.005312595
    else:
        if input[20] < 5315.0:
            if input[29] < 6155.0:
                var82 = -0.048971824
            else:
                var82 = -0.0031226675
        else:
            if input[349] < 1.0:
                var82 = -0.006107461
            else:
                var82 = -0.052681196
    if input[9] < 22.0:
        if input[19] < 2862.0:
            if input[28] < 2233.0:
                var83 = -0.0015594488
            else:
                var83 = 0.025622625
        else:
            if input[20] < 5855.0:
                var83 = -0.0007684064
            else:
                var83 = 0.039471768
    else:
        if input[34] < 78.0:
            var83 = 0.05786362
        else:
            if input[44] < 2.0:
                var83 = 0.023903547
            else:
                var83 = -0.036261793
    if input[46] < 2071.0:
        if input[11] < 4958.0:
            if input[25] < 95.0:
                var84 = 0.008658583
            else:
                var84 = -0.019070312
        else:
            if input[349] < 1.0:
                var84 = 0.0027156582
            else:
                var84 = -0.030816171
    else:
        if input[48] < 19.0:
            if input[33] < 6850.0:
                var84 = 0.03495047
            else:
                var84 = -0.009752566
        else:
            if input[19] < -915.0:
                var84 = -0.023440922
            else:
                var84 = 0.01949671
    if input[37] < -1959.0:
        if input[12] < 109.0:
            if input[11] < 6274.0:
                var85 = -0.045317322
            else:
                var85 = 0.016474137
        else:
            if input[38] < 7923.0:
                var85 = -0.015654026
            else:
                var85 = 0.039302748
    else:
        if input[39] < 108.0:
            if input[20] < 6264.0:
                var85 = -0.024461882
            else:
                var85 = -0.0014852051
        else:
            if input[19] < 1408.0:
                var85 = 0.0015881216
            else:
                var85 = 0.019899929
    if input[37] < 1342.0:
        if input[24] < 7137.0:
            if input[38] < 7364.0:
                var86 = -0.0032733076
            else:
                var86 = 0.01367877
        else:
            if input[42] < 6374.0:
                var86 = -0.0021229452
            else:
                var86 = -0.025193011
    else:
        if input[15] < 6474.0:
            if input[52] < 20.0:
                var86 = 0.008045549
            else:
                var86 = 0.030100316
        else:
            if input[30] < 129.0:
                var86 = 0.015305734
            else:
                var86 = -0.030523567
    if input[0] < 2.0:
        if input[46] < -3116.0:
            if input[404] < 1.0:
                var87 = -0.03731225
            else:
                var87 = 0.015731102
        else:
            if input[19] < 2048.0:
                var87 = -0.003014431
            else:
                var87 = 0.016622305
    else:
        if input[85] < 1.0:
            if input[11] < 6167.0:
                var87 = 0.01356587
            else:
                var87 = 0.04298658
        else:
            if input[8] < 2.0:
                var87 = -0.05492094
            else:
                var87 = 0.045363232
    if input[9] < 7.0:
        if input[46] < -1130.0:
            if input[48] < 20.0:
                var88 = 0.013486092
            else:
                var88 = -0.06643285
        else:
            if input[29] < 5489.0:
                var88 = 0.0003279557
            else:
                var88 = 0.04039143
    else:
        if input[2] < 3.0:
            if input[349] < 1.0:
                var88 = 0.00070987135
            else:
                var88 = -0.026964098
        else:
            if input[19] < -935.0:
                var88 = -0.049014457
            else:
                var88 = 0.001219202
    if input[28] < -1582.0:
        if input[331] < 1.0:
            if input[42] < 6607.0:
                var89 = -0.009863577
            else:
                var89 = -0.03133228
        else:
            if input[19] < -426.0:
                var89 = -0.04374649
            else:
                var89 = 0.072791
    else:
        if input[363] < 1.0:
            if input[38] < 7020.0:
                var89 = -0.0013673451
            else:
                var89 = 0.011621705
        else:
            if input[34] < 94.0:
                var89 = 0.030507421
            else:
                var89 = -0.043927148
    if input[29] < 5702.0:
        if input[38] < 7364.0:
            if input[0] < 1.0:
                var90 = -0.017699206
            else:
                var90 = -0.0006155588
        else:
            if input[16] < 94.0:
                var90 = 0.04726613
            else:
                var90 = 0.0018918228
    else:
        if input[21] < 104.0:
            if input[30] < 144.0:
                var90 = -0.006446484
            else:
                var90 = 0.02678377
        else:
            if input[19] < -1032.0:
                var90 = -0.0044091977
            else:
                var90 = 0.01741041
    if input[23] < 1.0:
        if input[29] < 5309.0:
            if input[43] < 98.0:
                var91 = 0.04767514
            else:
                var91 = -0.015120833
        else:
            if input[19] < -222.0:
                var91 = 0.0038754542
            else:
                var91 = 0.036469128
    else:
        if input[219] < 1.0:
            if input[19] < 2862.0:
                var91 = -0.004386627
            else:
                var91 = 0.024373136
        else:
            if input[3] < 10.0:
                var91 = -0.013342552
            else:
                var91 = 0.04341563
    if input[37] < -1987.0:
        if input[19] < 3477.0:
            if input[197] < 1.0:
                var92 = -0.027739396
            else:
                var92 = 0.012775241
        else:
            var92 = 0.055343237
    else:
        if input[2] < 3.0:
            if input[21] < 104.0:
                var92 = -0.0041010585
            else:
                var92 = 0.0073946263
        else:
            if input[19] < -512.0:
                var92 = -0.052496083
            else:
                var92 = 0.002261205
    if input[3] < 22.0:
        if input[219] < 1.0:
            if input[37] < -3096.0:
                var93 = -0.04785608
            else:
                var93 = -0.0015414065
        else:
            if input[3] < 12.0:
                var93 = -0.0009893306
            else:
                var93 = 0.047625493
    else:
        if input[357] < 1.0:
            if input[24] < 7286.0:
                var93 = 0.03924803
            else:
                var93 = -0.008644528
        else:
            if input[11] < 5614.0:
                var93 = 0.030954603
            else:
                var93 = -0.06412791
    if input[6] < 2.0:
        if input[39] < 129.0:
            if input[20] < 6825.0:
                var94 = -0.007527499
            else:
                var94 = 0.008270244
        else:
            if input[37] < 916.0:
                var94 = 0.0064455247
            else:
                var94 = 0.029017126
    else:
        if input[386] < 1.0:
            if input[34] < 110.0:
                var94 = 0.0053933673
            else:
                var94 = -0.016643474
        else:
            if input[5] < 3.0:
                var94 = -0.0057959436
            else:
                var94 = 0.073347546
    if input[28] < 2233.0:
        if input[363] < 1.0:
            if input[29] < 6240.0:
                var95 = -0.0042051175
            else:
                var95 = 0.0083938325
        else:
            if input[54] < 1.0:
                var95 = 0.04489361
            else:
                var95 = -0.042550262
    else:
        if input[38] < 5955.0:
            if input[55] < -669.0:
                var95 = -0.049285214
            else:
                var95 = 0.014779796
        else:
            if input[135] < 1.0:
                var95 = 0.038943063
            else:
                var95 = -0.04199913
    if input[9] < 22.0:
        if input[25] < 86.0:
            if input[429] < 1.0:
                var96 = 0.02183164
            else:
                var96 = -0.044863056
        else:
            if input[15] < 7455.0:
                var96 = 0.0005869383
            else:
                var96 = -0.02608539
    else:
        if input[12] < 135.0:
            if input[44] < 2.0:
                var96 = 0.027999012
            else:
                var96 = -0.03742477
        else:
            if input[16] < 105.0:
                var96 = 0.060662974
            else:
                var96 = -0.024728348
    if input[19] < 2862.0:
        if input[46] < -2468.0:
            if input[34] < 125.0:
                var97 = -0.007443867
            else:
                var97 = -0.034196
        else:
            if input[264] < 1.0:
                var97 = -0.0005047983
            else:
                var97 = 0.03483786
    else:
        if input[20] < 5855.0:
            if input[11] < 7171.0:
                var97 = -0.07315684
            else:
                var97 = 0.012185293
        else:
            if input[336] < 1.0:
                var97 = 0.03836811
            else:
                var97 = -0.036105137
    if input[9] < 7.0:
        if input[46] < -1130.0:
            if input[18] < 5.0:
                var98 = -0.05913235
            else:
                var98 = 0.022725675
        else:
            if input[29] < 5489.0:
                var98 = 0.000053265838
            else:
                var98 = 0.03846474
    else:
        if input[0] < 2.0:
            if input[349] < 1.0:
                var98 = -0.0017437082
            else:
                var98 = -0.029900286
        else:
            if input[85] < 1.0:
                var98 = 0.019005971
            else:
                var98 = -0.032268602
    if input[11] < 4958.0:
        if input[37] < -1753.0:
            if input[5] < 2.0:
                var99 = -0.054649867
            else:
                var99 = 0.0013614098
        else:
            if input[42] < 5059.0:
                var99 = 0.027375637
            else:
                var99 = -0.008637214
    else:
        if input[435] < 1.0:
            if input[21] < 128.0:
                var99 = -0.00026303754
            else:
                var99 = 0.024273152
        else:
            if input[400] < 1.0:
                var99 = 0.052378166
            else:
                var99 = 0.010628616
    if input[28] < -1582.0:
        if input[21] < 117.0:
            if input[11] < 6332.0:
                var100 = -0.02433174
            else:
                var100 = -0.00018802001
        else:
            if input[5] < 2.0:
                var100 = -0.03272577
            else:
                var100 = 0.04752561
    else:
        if input[363] < 1.0:
            if input[349] < 1.0:
                var100 = 0.0038257118
            else:
                var100 = -0.02357417
        else:
            if input[34] < 94.0:
                var100 = 0.030413521
            else:
                var100 = -0.041055333
    var101 = sigmoid(var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96 + var97 + var98 + var99 + var100)
    return [1.0 - var101, var101]
