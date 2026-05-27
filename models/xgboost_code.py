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
                if input[43] < 132.0:
                    if input[6] < 2.0:
                        var0 = 0.0154102985
                    else:
                        var0 = -0.09647267
                else:
                    if input[19] < 616.0:
                        var0 = -0.124696374
                    else:
                        var0 = -0.043318372
            else:
                if input[46] < -603.0:
                    if input[19] < 1557.0:
                        var0 = -0.046150323
                    else:
                        var0 = 0.092762895
                else:
                    if input[19] < -892.0:
                        var0 = 0.018103411
                    else:
                        var0 = 0.116655864
        else:
            if input[3] < 10.0:
                if input[21] < 124.0:
                    if input[37] < 1740.0:
                        var0 = -0.16753824
                    else:
                        var0 = 0.03579882
                else:
                    if input[44] < 4.0:
                        var0 = 0.016532796
                    else:
                        var0 = -0.12396003
            else:
                if input[9] < 16.0:
                    if input[28] < -486.0:
                        var0 = -0.102174155
                    else:
                        var0 = -0.027870132
                else:
                    if input[30] < 144.0:
                        var0 = -0.13276969
                    else:
                        var0 = 0.021203587
    else:
        if input[9] < 16.0:
            if input[9] < 12.0:
                if input[3] < 17.0:
                    if input[21] < 105.0:
                        var0 = 0.06757557
                    else:
                        var0 = 0.13394146
                else:
                    if input[0] < 1.0:
                        var0 = 0.12070934
                    else:
                        var0 = 0.1801307
            else:
                if input[3] < 18.0:
                    if input[8] < 1.0:
                        var0 = -0.015259581
                    else:
                        var0 = 0.059100647
                else:
                    if input[6] < 1.0:
                        var0 = 0.14679307
                    else:
                        var0 = 0.07850838
        else:
            if input[3] < 18.0:
                if input[9] < 22.0:
                    if input[38] < 6717.0:
                        var0 = -0.09492932
                    else:
                        var0 = -0.010742123
                else:
                    if input[12] < 136.0:
                        var0 = -0.16659966
                    else:
                        var0 = 0.002457937
            else:
                if input[9] < 20.0:
                    if input[8] < 1.0:
                        var0 = 0.003392245
                    else:
                        var0 = 0.103608504
                else:
                    if input[44] < 2.0:
                        var0 = 0.113180295
                    else:
                        var0 = -0.10653261
    if input[3] < 13.0:
        if input[9] < 13.0:
            if input[3] < 10.0:
                if input[19] < -1032.0:
                    if input[43] < 113.0:
                        var1 = -0.016890835
                    else:
                        var1 = -0.12347893
                else:
                    if input[20] < 6330.0:
                        var1 = -0.048083954
                    else:
                        var1 = 0.04952925
            else:
                if input[24] < 6248.0:
                    if input[46] < -640.0:
                        var1 = 0.008670466
                    else:
                        var1 = 0.09977814
                else:
                    if input[46] < 413.0:
                        var1 = -0.06965829
                    else:
                        var1 = 0.040450238
        else:
            if input[3] < 10.0:
                if input[37] < 1740.0:
                    if input[21] < 126.0:
                        var1 = -0.1523216
                    else:
                        var1 = -0.06002603
                else:
                    if input[46] < -2621.0:
                        var1 = -0.107663415
                    else:
                        var1 = 0.13039164
            else:
                if input[9] < 16.0:
                    if input[62] < 1.0:
                        var1 = -0.089285865
                    else:
                        var1 = -0.021915745
                else:
                    if input[30] < 144.0:
                        var1 = -0.12044889
                    else:
                        var1 = 0.019464163
    else:
        if input[9] < 14.0:
            if input[8] < 2.0:
                if input[9] < 10.0:
                    if input[12] < 78.0:
                        var1 = -0.04571386
                    else:
                        var1 = 0.12796767
                else:
                    if input[25] < 107.0:
                        var1 = 0.0815328
                    else:
                        var1 = 0.017419774
            else:
                if input[11] < 4686.0:
                    if input[105] < 1.0:
                        var1 = 0.09242042
                    else:
                        var1 = -0.08511012
                else:
                    if input[34] < 151.0:
                        var1 = 0.16303949
                    else:
                        var1 = 0.0056825494
        else:
            if input[9] < 18.0:
                if input[3] < 18.0:
                    if input[28] < 360.0:
                        var1 = -0.038301017
                    else:
                        var1 = 0.032174557
                else:
                    if input[21] < 98.0:
                        var1 = 0.035049114
                    else:
                        var1 = 0.12531155
            else:
                if input[9] < 22.0:
                    if input[3] < 16.0:
                        var1 = -0.09501635
                    else:
                        var1 = -0.01625481
                else:
                    if input[46] < 2562.0:
                        var1 = -0.1401676
                    else:
                        var1 = 0.07447817
    if input[3] < 13.0:
        if input[9] < 13.0:
            if input[28] < -347.0:
                if input[42] < 6457.0:
                    if input[6] < 2.0:
                        var2 = 0.004062329
                    else:
                        var2 = -0.106440924
                else:
                    if input[38] < 7475.0:
                        var2 = -0.11849623
                    else:
                        var2 = 0.030137405
            else:
                if input[46] < -603.0:
                    if input[34] < 109.0:
                        var2 = 0.08062636
                    else:
                        var2 = -0.04320609
                else:
                    if input[19] < -1540.0:
                        var2 = -0.029692296
                    else:
                        var2 = 0.079629935
        else:
            if input[28] < -289.0:
                if input[2] < 1.0:
                    if input[19] < 2640.0:
                        var2 = -0.09042635
                    else:
                        var2 = 0.13688038
                else:
                    if input[37] < 166.0:
                        var2 = -0.14785337
                    else:
                        var2 = -0.10019906
            else:
                if input[46] < -1540.0:
                    if input[37] < 938.0:
                        var2 = -0.1217721
                    else:
                        var2 = -0.006132914
                else:
                    if input[14] < 5.0:
                        var2 = -0.014718682
                    else:
                        var2 = -0.10048751
    else:
        if input[9] < 16.0:
            if input[9] < 10.0:
                if input[11] < 4632.0:
                    if input[30] < 108.0:
                        var2 = -0.0940658
                    else:
                        var2 = 0.08211793
                else:
                    if input[37] < -673.0:
                        var2 = 0.062028985
                    else:
                        var2 = 0.14583428
            else:
                if input[3] < 17.0:
                    if input[6] < 1.0:
                        var2 = 0.06805608
                    else:
                        var2 = 0.006974148
                else:
                    if input[28] < -630.0:
                        var2 = 0.031377595
                    else:
                        var2 = 0.11182552
        else:
            if input[3] < 18.0:
                if input[38] < 6717.0:
                    if input[29] < 6726.0:
                        var2 = -0.112356305
                    else:
                        var2 = -0.030352583
                else:
                    if input[47] < 4718.0:
                        var2 = 0.019278452
                    else:
                        var2 = -0.071185276
            else:
                if input[9] < 20.0:
                    if input[6] < 2.0:
                        var2 = 0.0800667
                    else:
                        var2 = -0.04890961
                else:
                    if input[44] < 2.0:
                        var2 = 0.1082595
                    else:
                        var2 = -0.08972453
    if input[3] < 13.0:
        if input[9] < 13.0:
            if input[3] < 10.0:
                if input[2] < 1.0:
                    if input[28] < -542.0:
                        var3 = -0.066186264
                    else:
                        var3 = 0.027496835
                else:
                    if input[0] < 1.0:
                        var3 = -0.1075356
                    else:
                        var3 = -0.027892143
            else:
                if input[9] < 9.0:
                    if input[6] < 2.0:
                        var3 = 0.111711584
                    else:
                        var3 = 0.0028077175
                else:
                    if input[28] < 117.0:
                        var3 = -0.029684458
                    else:
                        var3 = 0.04845373
        else:
            if input[3] < 10.0:
                if input[0] < 1.0:
                    if input[33] < 4611.0:
                        var3 = 0.022829317
                    else:
                        var3 = -0.13808313
                else:
                    if input[21] < 135.0:
                        var3 = -0.09262875
                    else:
                        var3 = 0.0895629
            else:
                if input[9] < 16.0:
                    if input[28] < -649.0:
                        var3 = -0.081032954
                    else:
                        var3 = -0.016630283
                else:
                    if input[30] < 144.0:
                        var3 = -0.10118828
                    else:
                        var3 = 0.02530739
    else:
        if input[9] < 14.0:
            if input[8] < 2.0:
                if input[28] < -1601.0:
                    if input[11] < 6849.0:
                        var3 = -0.104419425
                    else:
                        var3 = 0.08031636
                else:
                    if input[0] < 1.0:
                        var3 = 0.036881987
                    else:
                        var3 = 0.093306415
            else:
                if input[19] < -1261.0:
                    if input[66] < 1.0:
                        var3 = 0.08672302
                    else:
                        var3 = -0.12817147
                else:
                    if input[34] < 151.0:
                        var3 = 0.14103001
                    else:
                        var3 = -0.0009849878
        else:
            if input[9] < 18.0:
                if input[3] < 18.0:
                    if input[28] < 360.0:
                        var3 = -0.034109063
                    else:
                        var3 = 0.029394273
                else:
                    if input[6] < 2.0:
                        var3 = 0.09074037
                    else:
                        var3 = -0.044619266
            else:
                if input[34] < 92.0:
                    if input[52] < 15.0:
                        var3 = -0.06778364
                    else:
                        var3 = 0.084775515
                else:
                    if input[9] < 22.0:
                        var3 = -0.054176934
                    else:
                        var3 = -0.12604241
    if input[2] < 1.0:
        if input[8] < 1.0:
            if input[28] < -529.0:
                if input[46] < 447.0:
                    if input[33] < 5490.0:
                        var4 = -0.045136184
                    else:
                        var4 = -0.12322372
                else:
                    if input[43] < 113.0:
                        var4 = -0.076439016
                    else:
                        var4 = 0.020790162
            else:
                if input[46] < -683.0:
                    if input[37] < -389.0:
                        var4 = -0.092317395
                    else:
                        var4 = 0.0042637587
                else:
                    if input[0] < 1.0:
                        var4 = 0.010231105
                    else:
                        var4 = 0.0793295
        else:
            if input[0] < 1.0:
                if input[8] < 2.0:
                    if input[51] < 3882.0:
                        var4 = 0.08815645
                    else:
                        var4 = -0.0035118659
                else:
                    if input[26] < 6.0:
                        var4 = 0.10612835
                    else:
                        var4 = 0.0073121013
            else:
                if input[18] < 3.0:
                    if input[37] < 632.0:
                        var4 = 0.032884054
                    else:
                        var4 = 0.11646818
                else:
                    if input[29] < 4691.0:
                        var4 = -0.0082722455
                    else:
                        var4 = 0.13466838
    else:
        if input[3] < 12.0:
            if input[9] < 13.0:
                if input[3] < 8.0:
                    if input[9] < 8.0:
                        var4 = -0.005013311
                    else:
                        var4 = -0.12109589
                else:
                    if input[12] < 128.0:
                        var4 = -0.036889564
                    else:
                        var4 = 0.033860113
            else:
                if input[28] < 310.0:
                    if input[34] < 88.0:
                        var4 = 0.013113866
                    else:
                        var4 = -0.1236521
                else:
                    if input[15] < 5724.0:
                        var4 = -0.016944824
                    else:
                        var4 = -0.09487828
        else:
            if input[9] < 18.0:
                if input[8] < 1.0:
                    if input[20] < 7266.0:
                        var4 = -0.04225297
                    else:
                        var4 = 0.03812818
                else:
                    if input[37] < -1909.0:
                        var4 = -0.057789333
                    else:
                        var4 = 0.052514214
            else:
                if input[28] < 1007.0:
                    if input[36] < 5.0:
                        var4 = -0.105487704
                    else:
                        var4 = -0.015637888
                else:
                    if input[25] < 95.0:
                        var4 = 0.051368415
                    else:
                        var4 = -0.07026003
    if input[2] < 1.0:
        if input[8] < 1.0:
            if input[28] < -529.0:
                if input[46] < 447.0:
                    if input[90] < 1.0:
                        var5 = -0.10090523
                    else:
                        var5 = 0.022600072
                else:
                    if input[43] < 113.0:
                        var5 = -0.06966051
                    else:
                        var5 = 0.01877291
            else:
                if input[46] < -603.0:
                    if input[28] < 1132.0:
                        var5 = -0.054508444
                    else:
                        var5 = 0.050941933
                else:
                    if input[0] < 1.0:
                        var5 = 0.008361146
                    else:
                        var5 = 0.075346775
        else:
            if input[0] < 1.0:
                if input[8] < 2.0:
                    if input[28] < -1476.0:
                        var5 = -0.08547793
                    else:
                        var5 = 0.022381587
                else:
                    if input[33] < 5943.0:
                        var5 = 0.108829536
                    else:
                        var5 = 0.0296843
            else:
                if input[18] < 2.0:
                    if input[37] < 1390.0:
                        var5 = 0.01801025
                    else:
                        var5 = 0.1165893
                else:
                    if input[24] < 6761.0:
                        var5 = 0.12679265
                    else:
                        var5 = 0.07261089
    else:
        if input[3] < 11.0:
            if input[0] < 1.0:
                if input[28] < -176.0:
                    if input[37] < 2024.0:
                        var5 = -0.12754153
                    else:
                        var5 = 0.05612562
                else:
                    if input[19] < -1187.0:
                        var5 = -0.11599656
                    else:
                        var5 = -0.04245123
            else:
                if input[37] < 220.0:
                    if input[39] < 130.0:
                        var5 = -0.101364516
                    else:
                        var5 = -0.03070956
                else:
                    if input[20] < 5490.0:
                        var5 = -0.065088354
                    else:
                        var5 = 0.053231638
        else:
            if input[9] < 18.0:
                if input[9] < 10.0:
                    if input[37] < -673.0:
                        var5 = -0.024415625
                    else:
                        var5 = 0.10104316
                else:
                    if input[28] < 1783.0:
                        var5 = -0.017540304
                    else:
                        var5 = 0.07721704
            else:
                if input[28] < 466.0:
                    if input[46] < 1601.0:
                        var5 = -0.10074454
                    else:
                        var5 = 0.028458713
                else:
                    if input[11] < 5084.0:
                        var5 = -0.0717118
                    else:
                        var5 = 0.012128884
    if input[3] < 14.0:
        if input[9] < 12.0:
            if input[3] < 11.0:
                if input[23] < 1.0:
                    if input[28] < 480.0:
                        var6 = -0.0047725807
                    else:
                        var6 = 0.100044444
                else:
                    if input[42] < 6487.0:
                        var6 = -0.0077856705
                    else:
                        var6 = -0.07272204
            else:
                if input[46] < -425.0:
                    if input[20] < 6108.0:
                        var6 = -0.08862941
                    else:
                        var6 = 0.020768981
                else:
                    if input[37] < 666.0:
                        var6 = 0.051661994
                    else:
                        var6 = 0.11547177
        else:
            if input[9] < 18.0:
                if input[3] < 10.0:
                    if input[37] < 1474.0:
                        var6 = -0.08526414
                    else:
                        var6 = 0.06853807
                else:
                    if input[19] < 2910.0:
                        var6 = -0.035558663
                    else:
                        var6 = 0.13420232
            else:
                if input[28] < 1077.0:
                    if input[11] < 5563.0:
                        var6 = -0.12613969
                    else:
                        var6 = -0.08266938
                else:
                    if input[51] < 4742.0:
                        var6 = 0.085457936
                    else:
                        var6 = -0.08008581
    else:
        if input[9] < 12.0:
            if input[37] < 150.0:
                if input[11] < 4567.0:
                    if input[20] < 6009.0:
                        var6 = 0.024026178
                    else:
                        var6 = -0.14201479
                else:
                    if input[28] < 590.0:
                        var6 = 0.015498987
                    else:
                        var6 = 0.097048946
            else:
                if input[46] < -905.0:
                    if input[113] < 1.0:
                        var6 = 0.0981203
                    else:
                        var6 = -0.026017874
                else:
                    if input[15] < 7540.0:
                        var6 = 0.11729546
                    else:
                        var6 = -0.066354156
        else:
            if input[9] < 20.0:
                if input[3] < 18.0:
                    if input[28] < 1873.0:
                        var6 = -0.006344979
                    else:
                        var6 = 0.07805729
                else:
                    if input[6] < 2.0:
                        var6 = 0.073824935
                    else:
                        var6 = -0.034483746
            else:
                if input[30] < 126.0:
                    if input[18] < 6.0:
                        var6 = -0.10413646
                    else:
                        var6 = 0.012030271
                else:
                    if input[15] < 5125.0:
                        var6 = -0.10659291
                    else:
                        var6 = 0.056974273
    if input[8] < 1.0:
        if input[28] < -397.0:
            if input[46] < 64.0:
                if input[37] < -356.0:
                    if input[12] < 139.0:
                        var7 = -0.12380822
                    else:
                        var7 = -0.03624839
                else:
                    if input[44] < 1.0:
                        var7 = 0.12164104
                    else:
                        var7 = -0.07388601
            else:
                if input[23] < 2.0:
                    if input[34] < 132.0:
                        var7 = 0.07064351
                    else:
                        var7 = -0.05264628
                else:
                    if input[11] < 6065.0:
                        var7 = -0.06414311
                    else:
                        var7 = 0.027316445
        else:
            if input[46] < -793.0:
                if input[19] < -1032.0:
                    if input[3] < 16.0:
                        var7 = -0.1130363
                    else:
                        var7 = -0.0012987677
                else:
                    if input[37] < 1080.0:
                        var7 = -0.041762695
                    else:
                        var7 = 0.05837631
            else:
                if input[19] < -361.0:
                    if input[37] < -1672.0:
                        var7 = -0.09427817
                    else:
                        var7 = 0.0040228404
                else:
                    if input[37] < 345.0:
                        var7 = 0.027796863
                    else:
                        var7 = 0.10177793
    else:
        if input[28] < 310.0:
            if input[42] < 6496.0:
                if input[37] < 1080.0:
                    if input[11] < 6746.0:
                        var7 = -0.0055167335
                    else:
                        var7 = 0.08388758
                else:
                    if input[32] < 4.0:
                        var7 = 0.1105712
                    else:
                        var7 = -0.051650047
            else:
                if input[37] < 1328.0:
                    if input[2] < 1.0:
                        var7 = -0.018339744
                    else:
                        var7 = -0.07729065
                else:
                    if input[34] < 91.0:
                        var7 = -0.051107246
                    else:
                        var7 = 0.06357
        else:
            if input[0] < 1.0:
                if input[30] < 114.0:
                    if input[46] < -1728.0:
                        var7 = -0.111753725
                    else:
                        var7 = 0.011779483
                else:
                    if input[46] < 775.0:
                        var7 = 0.035789575
                    else:
                        var7 = 0.10968293
            else:
                if input[37] < -1883.0:
                    if input[15] < 5298.0:
                        var7 = 0.07136841
                    else:
                        var7 = -0.0976735
                else:
                    if input[19] < -1261.0:
                        var7 = 0.045814637
                    else:
                        var7 = 0.112353794
    if input[2] < 1.0:
        if input[3] < 18.0:
            if input[28] < -529.0:
                if input[46] < 2308.0:
                    if input[11] < 6077.0:
                        var8 = -0.060061038
                    else:
                        var8 = 0.0034594424
                else:
                    if input[25] < 121.0:
                        var8 = 0.095093
                    else:
                        var8 = -0.036936793
            else:
                if input[37] < 730.0:
                    if input[19] < 498.0:
                        var8 = -0.007540104
                    else:
                        var8 = 0.048671525
                else:
                    if input[42] < 6988.0:
                        var8 = 0.09842292
                    else:
                        var8 = 0.008037906
        else:
            if input[9] < 18.0:
                if input[0] < 1.0:
                    if input[30] < 84.0:
                        var8 = -0.1440103
                    else:
                        var8 = 0.06865605
                else:
                    if input[46] < 733.0:
                        var8 = 0.084482536
                    else:
                        var8 = 0.12362627
            else:
                if input[22] < 5.0:
                    if input[34] < 98.0:
                        var8 = 0.020715691
                    else:
                        var8 = -0.13355438
                else:
                    if input[29] < 6831.0:
                        var8 = 0.07385092
                    else:
                        var8 = -0.106760025
    else:
        if input[3] < 11.0:
            if input[0] < 1.0:
                if input[28] < -176.0:
                    if input[37] < 2024.0:
                        var8 = -0.11161472
                    else:
                        var8 = 0.05682187
                else:
                    if input[19] < -817.0:
                        var8 = -0.09549638
                    else:
                        var8 = -0.028496256
            else:
                if input[37] < 220.0:
                    if input[47] < 4594.0:
                        var8 = -0.04636253
                    else:
                        var8 = -0.13738057
                else:
                    if input[20] < 5490.0:
                        var8 = -0.053992707
                    else:
                        var8 = 0.05326379
        else:
            if input[9] < 18.0:
                if input[9] < 10.0:
                    if input[84] < 1.0:
                        var8 = 0.07910542
                    else:
                        var8 = -0.08217885
                else:
                    if input[28] < 1783.0:
                        var8 = -0.015638908
                    else:
                        var8 = 0.063879795
            else:
                if input[33] < 6104.0:
                    if input[40] < 4.0:
                        var8 = -0.054747183
                    else:
                        var8 = 0.026951442
                else:
                    if input[46] < 1401.0:
                        var8 = -0.09070245
                    else:
                        var8 = 0.0042961943
    if input[8] < 1.0:
        if input[9] < 16.0:
            if input[20] < 6644.0:
                if input[6] < 1.0:
                    if input[42] < 6888.0:
                        var9 = 0.030914757
                    else:
                        var9 = -0.04334708
                else:
                    if input[29] < 5685.0:
                        var9 = -0.07463364
                    else:
                        var9 = -0.022231994
            else:
                if input[15] < 5574.0:
                    if input[42] < 6407.0:
                        var9 = 0.09522985
                    else:
                        var9 = 0.025558567
                else:
                    if input[38] < 6510.0:
                        var9 = -0.03596101
                    else:
                        var9 = 0.039137065
        else:
            if input[3] < 11.0:
                if input[15] < 5436.0:
                    if input[11] < 6088.0:
                        var9 = -0.081499785
                    else:
                        var9 = 0.06336191
                else:
                    if input[38] < 8030.0:
                        var9 = -0.11472183
                    else:
                        var9 = 0.023018872
            else:
                if input[12] < 99.0:
                    if input[47] < 3849.0:
                        var9 = 0.03380732
                    else:
                        var9 = -0.095528185
                else:
                    if input[38] < 6747.0:
                        var9 = -0.05487469
                    else:
                        var9 = 0.0072794356
    else:
        if input[28] < 510.0:
            if input[46] < 467.0:
                if input[37] < 7.0:
                    if input[19] < 3344.0:
                        var9 = -0.07314768
                    else:
                        var9 = 0.031555787
                else:
                    if input[28] < -1217.0:
                        var9 = -0.061583888
                    else:
                        var9 = 0.016933005
            else:
                if input[37] < 584.0:
                    if input[11] < 6332.0:
                        var9 = -0.01270426
                    else:
                        var9 = 0.06613865
                else:
                    if input[30] < 86.0:
                        var9 = -0.102848604
                    else:
                        var9 = 0.087167375
        else:
            if input[0] < 1.0:
                if input[55] < -618.0:
                    if input[30] < 124.0:
                        var9 = -0.07569402
                    else:
                        var9 = 0.022193843
                else:
                    if input[29] < 4969.0:
                        var9 = -0.039540615
                    else:
                        var9 = 0.06323112
            else:
                if input[37] < -1236.0:
                    if input[28] < 1489.0:
                        var9 = -0.038137764
                    else:
                        var9 = 0.0738763
                else:
                    if input[19] < -996.0:
                        var9 = 0.04707976
                    else:
                        var9 = 0.11008735
    if input[9] < 12.0:
        if input[3] < 11.0:
            if input[23] < 1.0:
                if input[11] < 4968.0:
                    if input[48] < 19.0:
                        var10 = 0.065413326
                    else:
                        var10 = -0.08577273
                else:
                    if input[30] < 127.0:
                        var10 = 0.022368878
                    else:
                        var10 = 0.13344403
            else:
                if input[42] < 6487.0:
                    if input[34] < 102.0:
                        var10 = 0.14021702
                    else:
                        var10 = -0.013949421
                else:
                    if input[42] < 8694.0:
                        var10 = -0.06765751
                    else:
                        var10 = 0.13695176
        else:
            if input[3] < 18.0:
                if input[9] < 7.0:
                    if input[119] < 1.0:
                        var10 = 0.116450325
                    else:
                        var10 = 0.028262883
                else:
                    if input[39] < 114.0:
                        var10 = -0.008169087
                    else:
                        var10 = 0.04616786
            else:
                if input[39] < 102.0:
                    if input[29] < 6592.0:
                        var10 = -0.07749489
                    else:
                        var10 = 0.059473664
                else:
                    if input[6] < 2.0:
                        var10 = 0.11098786
                    else:
                        var10 = -0.009331841
    else:
        if input[3] < 14.0:
            if input[9] < 18.0:
                if input[19] < 2910.0:
                    if input[43] < 128.0:
                        var10 = -0.022105379
                    else:
                        var10 = -0.065822355
                else:
                    if input[20] < 5835.0:
                        var10 = 0.010469278
                    else:
                        var10 = 0.15153645
            else:
                if input[28] < 1077.0:
                    if input[11] < 5563.0:
                        var10 = -0.108089164
                    else:
                        var10 = -0.06344638
                else:
                    if input[34] < 130.0:
                        var10 = 0.05498841
                    else:
                        var10 = -0.09198224
        else:
            if input[9] < 20.0:
                if input[3] < 18.0:
                    if input[16] < 145.0:
                        var10 = 0.006700754
                    else:
                        var10 = -0.08285827
                else:
                    if input[6] < 2.0:
                        var10 = 0.05682539
                    else:
                        var10 = -0.0344181
            else:
                if input[44] < 2.0:
                    if input[125] < 1.0:
                        var10 = 0.03146675
                    else:
                        var10 = 0.12106432
                else:
                    if input[32] < 1.0:
                        var10 = 0.09143382
                    else:
                        var10 = -0.07157985
    if input[28] < 310.0:
        if input[46] < 393.0:
            if input[37] < -546.0:
                if input[15] < 4934.0:
                    if input[37] < -1065.0:
                        var11 = -0.06508449
                    else:
                        var11 = 0.023893807
                else:
                    if input[51] < 3726.0:
                        var11 = 0.024245221
                    else:
                        var11 = -0.10570438
            else:
                if input[39] < 105.0:
                    if input[46] < -2260.0:
                        var11 = -0.102461316
                    else:
                        var11 = -0.046528384
                else:
                    if input[11] < 6198.0:
                        var11 = -0.032338534
                    else:
                        var11 = 0.02658217
        else:
            if input[11] < 5131.0:
                if input[37] < -1351.0:
                    if input[47] < 5752.0:
                        var11 = -0.108604446
                    else:
                        var11 = 0.07902124
                else:
                    if input[6] < 2.0:
                        var11 = 0.004812799
                    else:
                        var11 = -0.08892723
            else:
                if input[28] < -2060.0:
                    if input[21] < 88.0:
                        var11 = 0.066560976
                    else:
                        var11 = -0.07828634
                else:
                    if input[37] < -297.0:
                        var11 = 0.012359842
                    else:
                        var11 = 0.06876006
    else:
        if input[46] < 246.0:
            if input[19] < -1072.0:
                if input[18] < 4.0:
                    if input[48] < 16.0:
                        var11 = 0.0019506367
                    else:
                        var11 = -0.07828285
                else:
                    if input[28] < 1434.0:
                        var11 = -0.056777056
                    else:
                        var11 = 0.122751296
            else:
                if input[29] < 5702.0:
                    if input[0] < 1.0:
                        var11 = -0.044570826
                    else:
                        var11 = 0.033307705
                else:
                    if input[46] < -1493.0:
                        var11 = 0.017322835
                    else:
                        var11 = 0.06566494
        else:
            if input[37] < 359.0:
                if input[15] < 4766.0:
                    if input[21] < 94.0:
                        var11 = -0.013250281
                    else:
                        var11 = 0.11717861
                else:
                    if input[37] < -2231.0:
                        var11 = -0.06320801
                    else:
                        var11 = 0.0374556
            else:
                if input[12] < 85.0:
                    if input[18] < 3.0:
                        var11 = -0.069477156
                    else:
                        var11 = 0.06338012
                else:
                    if input[28] < 374.0:
                        var11 = -0.0003765675
                    else:
                        var11 = 0.1083078
    if input[0] < 1.0:
        if input[2] < 2.0:
            if input[8] < 2.0:
                if input[28] < -529.0:
                    if input[34] < 111.0:
                        var12 = -0.000894605
                    else:
                        var12 = -0.07078849
                else:
                    if input[46] < 710.0:
                        var12 = -0.019470988
                    else:
                        var12 = 0.033685286
            else:
                if input[38] < 7258.0:
                    if input[37] < 866.0:
                        var12 = -0.009734579
                    else:
                        var12 = 0.07677336
                else:
                    if input[16] < 143.0:
                        var12 = 0.09964066
                    else:
                        var12 = -0.057142444
        else:
            if input[27] < 2.0:
                if input[43] < 94.0:
                    var12 = 0.04941146
                else:
                    if input[20] < 8048.0:
                        var12 = -0.11073939
                    else:
                        var12 = 0.05468586
            else:
                if input[38] < 6613.0:
                    if input[48] < 29.0:
                        var12 = -0.082730755
                    else:
                        var12 = -0.0028850292
                else:
                    if input[11] < 4863.0:
                        var12 = -0.1041859
                    else:
                        var12 = 0.055467036
    else:
        if input[3] < 18.0:
            if input[28] < 104.0:
                if input[39] < 127.0:
                    if input[19] < 2455.0:
                        var12 = -0.047326326
                    else:
                        var12 = 0.076279275
                else:
                    if input[33] < 6157.0:
                        var12 = 0.036299635
                    else:
                        var12 = -0.026704475
            else:
                if input[33] < 5967.0:
                    if input[11] < 4675.0:
                        var12 = -0.0015437441
                    else:
                        var12 = 0.07509964
                else:
                    if input[15] < 5341.0:
                        var12 = 0.040446628
                    else:
                        var12 = -0.028786553
        else:
            if input[19] < -2654.0:
                if input[68] < 1.0:
                    var12 = -0.1539726
                else:
                    if input[36] < 5.0:
                        var12 = -0.02347268
                    else:
                        var12 = 0.10022875
            else:
                if input[46] < 1426.0:
                    if input[24] < 6732.0:
                        var12 = 0.079562254
                    else:
                        var12 = 0.016812563
                else:
                    if input[9] < 19.0:
                        var12 = 0.11281281
                    else:
                        var12 = -0.005826591
    if input[9] < 14.0:
        if input[3] < 12.0:
            if input[6] < 2.0:
                if input[39] < 129.0:
                    if input[34] < 97.0:
                        var13 = 0.097154275
                    else:
                        var13 = -0.025342999
                else:
                    if input[19] < -1021.0:
                        var13 = -0.014506525
                    else:
                        var13 = 0.05225994
            else:
                if input[34] < 110.0:
                    if input[21] < 102.0:
                        var13 = -0.06614439
                    else:
                        var13 = 0.09148886
                else:
                    if input[15] < 5843.0:
                        var13 = -0.04400742
                    else:
                        var13 = -0.11143094
        else:
            if input[8] < 2.0:
                if input[21] < 105.0:
                    if input[66] < 1.0:
                        var13 = 0.020988313
                    else:
                        var13 = -0.07348465
                else:
                    if input[37] < -1138.0:
                        var13 = -0.023206418
                    else:
                        var13 = 0.06072971
            else:
                if input[19] < -1261.0:
                    if input[48] < 23.0:
                        var13 = 0.03397728
                    else:
                        var13 = -0.15072295
                else:
                    if input[26] < 7.0:
                        var13 = 0.08866409
                    else:
                        var13 = -0.04455817
    else:
        if input[3] < 14.0:
            if input[9] < 18.0:
                if input[6] < 1.0:
                    if input[47] < 3656.0:
                        var13 = 0.14251773
                    else:
                        var13 = -0.0044908524
                else:
                    if input[28] < -1814.0:
                        var13 = -0.10370924
                    else:
                        var13 = -0.037968278
            else:
                if input[28] < 1077.0:
                    if input[11] < 5563.0:
                        var13 = -0.098021135
                    else:
                        var13 = -0.050995737
                else:
                    if input[55] < -891.0:
                        var13 = -0.07462182
                    else:
                        var13 = 0.07058206
        else:
            if input[9] < 22.0:
                if input[28] < 2233.0:
                    if input[6] < 1.0:
                        var13 = 0.029734049
                    else:
                        var13 = -0.01437094
                else:
                    if input[46] < -2814.0:
                        var13 = -0.056183558
                    else:
                        var13 = 0.10499012
            else:
                if input[44] < 2.0:
                    var13 = 0.07114728
                else:
                    if input[12] < 136.0:
                        var13 = -0.09728071
                    else:
                        var13 = 0.041565273
    if input[2] < 1.0:
        if input[6] < 2.0:
            if input[37] < 1361.0:
                if input[28] < -364.0:
                    if input[11] < 7142.0:
                        var14 = -0.022074215
                    else:
                        var14 = 0.07454043
                else:
                    if input[39] < 122.0:
                        var14 = 0.013584628
                    else:
                        var14 = 0.05985217
            else:
                if input[46] < -1272.0:
                    if input[20] < 7221.0:
                        var14 = -0.06485548
                    else:
                        var14 = 0.09979879
                else:
                    if input[24] < 8071.0:
                        var14 = 0.092418365
                    else:
                        var14 = -0.017658107
        else:
            if input[20] < 7193.0:
                if input[11] < 6927.0:
                    if input[39] < 154.0:
                        var14 = -0.061099816
                    else:
                        var14 = 0.10490276
                else:
                    if input[28] < -859.0:
                        var14 = -0.050936308
                    else:
                        var14 = 0.077151366
            else:
                if input[38] < 5743.0:
                    if input[19] < 1115.0:
                        var14 = 0.0055832546
                    else:
                        var14 = -0.12347436
                else:
                    if input[36] < 2.0:
                        var14 = -0.031058917
                    else:
                        var14 = 0.12490082
    else:
        if input[3] < 10.0:
            if input[0] < 1.0:
                if input[28] < -176.0:
                    if input[32] < 2.0:
                        var14 = -0.052510947
                    else:
                        var14 = -0.10590716
                else:
                    if input[15] < 6513.0:
                        var14 = -0.014573264
                    else:
                        var14 = -0.11329005
            else:
                if input[29] < 5878.0:
                    if input[47] < 4502.0:
                        var14 = -0.02715619
                    else:
                        var14 = -0.12242863
                else:
                    if input[34] < 110.0:
                        var14 = -0.06795751
                    else:
                        var14 = 0.06824125
        else:
            if input[21] < 118.0:
                if input[37] < -1793.0:
                    if input[51] < 3754.0:
                        var14 = 0.079056256
                    else:
                        var14 = -0.08386812
                else:
                    if input[46] < 370.0:
                        var14 = -0.028205955
                    else:
                        var14 = 0.014264971
            else:
                if input[46] < -2260.0:
                    if input[12] < 126.0:
                        var14 = -0.08053261
                    else:
                        var14 = 0.047412097
                else:
                    if input[11] < 5217.0:
                        var14 = 0.008115687
                    else:
                        var14 = 0.08105048
    if input[8] < 1.0:
        if input[9] < 16.0:
            if input[20] < 6857.0:
                if input[6] < 1.0:
                    if input[16] < 112.0:
                        var15 = 0.05845185
                    else:
                        var15 = -0.009894571
                else:
                    if input[37] < -1351.0:
                        var15 = -0.08341904
                    else:
                        var15 = -0.025459722
            else:
                if input[14] < 1.0:
                    if input[43] < 136.0:
                        var15 = 0.12475828
                    else:
                        var15 = 0.00081218046
                else:
                    if input[25] < 89.0:
                        var15 = 0.079707734
                    else:
                        var15 = 0.0035883442
        else:
            if input[11] < 4958.0:
                if input[28] < 923.0:
                    if input[46] < 2097.0:
                        var15 = -0.10286274
                    else:
                        var15 = 0.028398339
                else:
                    if input[34] < 128.0:
                        var15 = 0.028275672
                    else:
                        var15 = -0.102031425
            else:
                if input[40] < 4.0:
                    if input[34] < 84.0:
                        var15 = 0.072325945
                    else:
                        var15 = -0.06073563
                else:
                    if input[42] < 6988.0:
                        var15 = 0.058766365
                    else:
                        var15 = -0.028207868
    else:
        if input[28] < 510.0:
            if input[37] < 7.0:
                if input[42] < 7436.0:
                    if input[13] < 4.0:
                        var15 = -0.025429755
                    else:
                        var15 = 0.035418894
                else:
                    if input[25] < 91.0:
                        var15 = 0.03581411
                    else:
                        var15 = -0.102769755
            else:
                if input[46] < 2203.0:
                    if input[28] < -1277.0:
                        var15 = -0.037504386
                    else:
                        var15 = 0.028696775
                else:
                    if input[19] < -1873.0:
                        var15 = -0.01332711
                    else:
                        var15 = 0.096689634
        else:
            if input[33] < 5877.0:
                if input[46] < 585.0:
                    if input[12] < 126.0:
                        var15 = 0.008480302
                    else:
                        var15 = 0.07530107
                else:
                    if input[17] < 6.0:
                        var15 = 0.103166156
                    else:
                        var15 = 0.00039932784
            else:
                if input[21] < 128.0:
                    if input[47] < 4259.0:
                        var15 = -0.038776524
                    else:
                        var15 = 0.02881447
                else:
                    if input[117] < 1.0:
                        var15 = 0.10790215
                    else:
                        var15 = -0.02837037
    if input[6] < 1.0:
        if input[19] < -222.0:
            if input[46] < -603.0:
                if input[31] < 6.0:
                    if input[21] < 121.0:
                        var16 = -0.08170342
                    else:
                        var16 = 0.008679673
                else:
                    if input[2] < 1.0:
                        var16 = -0.09957402
                    else:
                        var16 = 0.08215409
            else:
                if input[37] < -1852.0:
                    if input[47] < 3993.0:
                        var16 = 0.053502202
                    else:
                        var16 = -0.10445901
                else:
                    if input[18] < 2.0:
                        var16 = 0.003257321
                    else:
                        var16 = 0.05474179
        else:
            if input[42] < 6307.0:
                if input[20] < 6613.0:
                    if input[37] < 570.0:
                        var16 = 0.0304148
                    else:
                        var16 = 0.10211503
                else:
                    if input[0] < 1.0:
                        var16 = 0.000763656
                    else:
                        var16 = 0.109098494
            else:
                if input[33] < 6002.0:
                    if input[26] < 7.0:
                        var16 = 0.062115062
                    else:
                        var16 = -0.1268797
                else:
                    if input[19] < 2195.0:
                        var16 = -0.0393585
                    else:
                        var16 = 0.071371205
    else:
        if input[28] < -1582.0:
            if input[21] < 117.0:
                if input[11] < 6332.0:
                    if input[52] < 37.0:
                        var16 = -0.09324701
                    else:
                        var16 = 0.03175728
                else:
                    if input[3] < 18.0:
                        var16 = -0.054395415
                    else:
                        var16 = 0.076775044
            else:
                if input[46] < -425.0:
                    if input[38] < 5239.0:
                        var16 = -0.014086035
                    else:
                        var16 = -0.08808013
                else:
                    if input[42] < 5665.0:
                        var16 = 0.023158206
                    else:
                        var16 = 0.1535392
        else:
            if input[11] < 5029.0:
                if input[42] < 6563.0:
                    if input[34] < 125.0:
                        var16 = 0.017643463
                    else:
                        var16 = -0.049314585
                else:
                    if input[37] < 1390.0:
                        var16 = -0.08049347
                    else:
                        var16 = 0.0140296165
            else:
                if input[38] < 6922.0:
                    if input[37] < -830.0:
                        var16 = -0.040893063
                    else:
                        var16 = 0.0037045632
                else:
                    if input[41] < 5.0:
                        var16 = 0.049601544
                    else:
                        var16 = -0.040538236
    if input[28] < 310.0:
        if input[46] < 2071.0:
            if input[37] < -34.0:
                if input[19] < 2640.0:
                    if input[19] < -1778.0:
                        var17 = -0.09668417
                    else:
                        var17 = -0.044070642
                else:
                    if input[37] < -1377.0:
                        var17 = -0.032815017
                    else:
                        var17 = 0.07095135
            else:
                if input[42] < 6487.0:
                    if input[23] < 5.0:
                        var17 = 0.02340155
                    else:
                        var17 = -0.08222019
                else:
                    if input[18] < 3.0:
                        var17 = -0.04743243
                    else:
                        var17 = 0.002112304
        else:
            if input[33] < 5362.0:
                if input[29] < 5013.0:
                    var17 = -0.043683205
                else:
                    if input[42] < 6116.0:
                        var17 = 0.106155895
                    else:
                        var17 = -0.01722002
            else:
                if input[19] < -3193.0:
                    var17 = -0.12872927
                else:
                    if input[81] < 1.0:
                        var17 = -0.0037469303
                    else:
                        var17 = 0.0565498
    else:
        if input[46] < 866.0:
            if input[15] < 5645.0:
                if input[29] < 5531.0:
                    if input[23] < 1.0:
                        var17 = 0.05925221
                    else:
                        var17 = -0.03226497
                else:
                    if input[46] < -2425.0:
                        var17 = -0.00488772
                    else:
                        var17 = 0.058506943
            else:
                if input[20] < 7168.0:
                    if input[11] < 4389.0:
                        var17 = -0.11805564
                    else:
                        var17 = -0.032274477
                else:
                    if input[37] < 345.0:
                        var17 = -0.027513703
                    else:
                        var17 = 0.0424322
        else:
            if input[37] < 247.0:
                if input[21] < 105.0:
                    if input[21] < 93.0:
                        var17 = 0.05387316
                    else:
                        var17 = -0.03325066
                else:
                    if input[37] < -2231.0:
                        var17 = -0.049002793
                    else:
                        var17 = 0.061802644
            else:
                if input[17] < 6.0:
                    if input[55] < -767.0:
                        var17 = 0.007271591
                    else:
                        var17 = 0.09985178
                else:
                    if input[26] < 2.0:
                        var17 = 0.069758795
                    else:
                        var17 = -0.07582608
    if input[0] < 1.0:
        if input[11] < 5424.0:
            if input[38] < 6240.0:
                if input[51] < 4414.0:
                    if input[25] < 98.0:
                        var18 = 0.044425692
                    else:
                        var18 = -0.06149999
                else:
                    if input[29] < 7718.0:
                        var18 = -0.09403538
                    else:
                        var18 = 0.03015908
            else:
                if input[29] < 4851.0:
                    if input[26] < 2.0:
                        var18 = 0.043295912
                    else:
                        var18 = -0.106816426
                else:
                    if input[11] < 4958.0:
                        var18 = -0.038496826
                    else:
                        var18 = 0.016100114
        else:
            if input[46] < -2468.0:
                if input[33] < 4904.0:
                    if input[26] < 5.0:
                        var18 = 0.07636257
                    else:
                        var18 = -0.08950767
                else:
                    if input[19] < 3006.0:
                        var18 = -0.08171955
                    else:
                        var18 = 0.033762433
            else:
                if input[29] < 5805.0:
                    if input[38] < 7528.0:
                        var18 = -0.028132735
                    else:
                        var18 = 0.05124274
                else:
                    if input[91] < 1.0:
                        var18 = 0.029162139
                    else:
                        var18 = 0.11451461
    else:
        if input[3] < 18.0:
            if input[33] < 5992.0:
                if input[21] < 108.0:
                    if input[46] < -516.0:
                        var18 = -0.04424965
                    else:
                        var18 = 0.02182942
                else:
                    if input[19] < -1414.0:
                        var18 = 0.00039814576
                    else:
                        var18 = 0.06255705
            else:
                if input[21] < 130.0:
                    if input[81] < 1.0:
                        var18 = -0.048183814
                    else:
                        var18 = -0.0018497758
                else:
                    if input[66] < 1.0:
                        var18 = 0.0956141
                    else:
                        var18 = -0.047795277
        else:
            if input[19] < -2654.0:
                if input[68] < 1.0:
                    var18 = -0.13986008
                else:
                    if input[36] < 5.0:
                        var18 = -0.021502353
                    else:
                        var18 = 0.09007557
            else:
                if input[46] < 1426.0:
                    if input[9] < 10.0:
                        var18 = 0.09863109
                    else:
                        var18 = 0.02831456
                else:
                    if input[33] < 6719.0:
                        var18 = 0.10377043
                    else:
                        var18 = 0.032744896
    if input[28] < -529.0:
        if input[46] < 393.0:
            if input[37] < -1325.0:
                if input[25] < 101.0:
                    if input[41] < 6.0:
                        var19 = -0.057014585
                    else:
                        var19 = 0.13919683
                else:
                    if input[106] < 1.0:
                        var19 = -0.11149956
                    else:
                        var19 = -0.017056977
            else:
                if input[39] < 105.0:
                    if input[11] < 6992.0:
                        var19 = -0.07819515
                    else:
                        var19 = 0.007063236
                else:
                    if input[3] < 13.0:
                        var19 = -0.03545552
                    else:
                        var19 = 0.022752648
        else:
            if input[24] < 6943.0:
                if input[20] < 5530.0:
                    if input[6] < 2.0:
                        var19 = 0.010606806
                    else:
                        var19 = -0.09452064
                else:
                    if input[38] < 7299.0:
                        var19 = 0.011870609
                    else:
                        var19 = 0.100509785
            else:
                if input[37] < 1328.0:
                    if input[55] < 14.0:
                        var19 = 0.0034184807
                    else:
                        var19 = -0.057834424
                else:
                    if input[15] < 6734.0:
                        var19 = 0.075753555
                    else:
                        var19 = -0.071436465
    else:
        if input[46] < -1470.0:
            if input[12] < 128.0:
                if input[37] < 1361.0:
                    if input[28] < 1369.0:
                        var19 = -0.07513725
                    else:
                        var19 = -0.01782095
                else:
                    if input[20] < 7221.0:
                        var19 = -0.022753332
                    else:
                        var19 = 0.09110545
            else:
                if input[28] < 923.0:
                    if input[69] < 1.0:
                        var19 = -0.025618762
                    else:
                        var19 = 0.121405415
                else:
                    if input[0] < 1.0:
                        var19 = 0.018774616
                    else:
                        var19 = 0.11521375
        else:
            if input[19] < 1423.0:
                if input[33] < 5992.0:
                    if input[11] < 4686.0:
                        var19 = -0.01499634
                    else:
                        var19 = 0.04201376
                else:
                    if input[46] < 3133.0:
                        var19 = -0.018479506
                    else:
                        var19 = 0.07068225
            else:
                if input[29] < 5702.0:
                    if input[39] < 101.0:
                        var19 = -0.101649754
                    else:
                        var19 = 0.055157807
                else:
                    if input[45] < 1.0:
                        var19 = -0.05322818
                    else:
                        var19 = 0.092379145
    if input[46] < 2071.0:
        if input[28] < 606.0:
            if input[37] < -34.0:
                if input[19] < -817.0:
                    if input[38] < 6135.0:
                        var20 = -0.1028124
                    else:
                        var20 = -0.049045485
                else:
                    if input[46] < -3116.0:
                        var20 = -0.10638614
                    else:
                        var20 = -0.016302088
            else:
                if input[42] < 6487.0:
                    if input[23] < 4.0:
                        var20 = 0.026196226
                    else:
                        var20 = -0.032785967
                else:
                    if input[11] < 5584.0:
                        var20 = -0.03911036
                    else:
                        var20 = 0.0031937794
        else:
            if input[19] < 498.0:
                if input[46] < -793.0:
                    if input[30] < 124.0:
                        var20 = -0.055371683
                    else:
                        var20 = 0.0048899273
                else:
                    if input[81] < 1.0:
                        var20 = -0.006869857
                    else:
                        var20 = 0.03691477
            else:
                if input[29] < 5702.0:
                    if input[46] < -2082.0:
                        var20 = -0.06400836
                    else:
                        var20 = 0.02783211
                else:
                    if input[42] < 7756.0:
                        var20 = 0.0770431
                    else:
                        var20 = 0.021777991
    else:
        if input[21] < 105.0:
            if input[37] < 388.0:
                if input[81] < 1.0:
                    if input[18] < 3.0:
                        var20 = -0.089948945
                    else:
                        var20 = 0.0028232026
                else:
                    if input[27] < 1.0:
                        var20 = -0.090729855
                    else:
                        var20 = 0.03602145
            else:
                if input[39] < 113.0:
                    var20 = -0.06414079
                else:
                    if input[24] < 8226.0:
                        var20 = 0.08951366
                    else:
                        var20 = -0.048609268
        else:
            if input[48] < 29.0:
                if input[33] < 6850.0:
                    if input[15] < 7540.0:
                        var20 = 0.09776893
                    else:
                        var20 = -0.020424087
                else:
                    if input[12] < 93.0:
                        var20 = -0.11220642
                    else:
                        var20 = 0.04898168
            else:
                if input[15] < 5878.0:
                    if input[37] < -11.0:
                        var20 = -0.050080307
                    else:
                        var20 = 0.08347805
                else:
                    var20 = -0.12402391
    if input[6] < 1.0:
        if input[19] < -182.0:
            if input[46] < 603.0:
                if input[39] < 131.0:
                    if input[34] < 91.0:
                        var21 = 0.04929923
                    else:
                        var21 = -0.044762388
                else:
                    if input[11] < 3967.0:
                        var21 = -0.1076916
                    else:
                        var21 = 0.04382129
            else:
                if input[37] < -1883.0:
                    if input[5] < 3.0:
                        var21 = -0.11044216
                    else:
                        var21 = 0.005440693
                else:
                    if input[48] < 31.0:
                        var21 = 0.03932003
                    else:
                        var21 = -0.076513775
        else:
            if input[42] < 6307.0:
                if input[23] < 2.0:
                    if input[24] < 7762.0:
                        var21 = 0.09876416
                    else:
                        var21 = -0.01913036
                else:
                    if input[19] < 634.0:
                        var21 = -0.00018347247
                    else:
                        var21 = 0.07567445
            else:
                if input[15] < 4993.0:
                    if input[26] < 7.0:
                        var21 = 0.058999676
                    else:
                        var21 = -0.091262996
                else:
                    if input[28] < 906.0:
                        var21 = -0.04067873
                    else:
                        var21 = 0.045153182
    else:
        if input[28] < -1814.0:
            if input[25] < 97.0:
                if input[11] < 5640.0:
                    var21 = -0.08773198
                else:
                    if input[31] < 2.0:
                        var21 = -0.0660746
                    else:
                        var21 = 0.1343529
            else:
                if input[19] < 3006.0:
                    if input[52] < 38.0:
                        var21 = -0.085329205
                    else:
                        var21 = 0.063431256
                else:
                    var21 = 0.07065011
        else:
            if input[37] < 1361.0:
                if input[11] < 4958.0:
                    if input[25] < 105.0:
                        var21 = -0.00988212
                    else:
                        var21 = -0.06565237
                else:
                    if input[51] < 3853.0:
                        var21 = 0.04587785
                    else:
                        var21 = -0.008875363
            else:
                if input[38] < 5915.0:
                    if input[52] < 25.0:
                        var21 = -0.03036563
                    else:
                        var21 = 0.08451519
                else:
                    if input[49] < 6.0:
                        var21 = 0.062004812
                    else:
                        var21 = -0.109953634
    if input[46] < 2071.0:
        if input[28] < 310.0:
            if input[33] < 6112.0:
                if input[28] < -1601.0:
                    if input[55] < 955.0:
                        var22 = -0.056977022
                    else:
                        var22 = 0.041263636
                else:
                    if input[6] < 2.0:
                        var22 = 0.01143797
                    else:
                        var22 = -0.0290607
            else:
                if input[11] < 4921.0:
                    if input[122] < 1.0:
                        var22 = -0.09025389
                    else:
                        var22 = -0.0026964187
                else:
                    if input[25] < 101.0:
                        var22 = 0.010786302
                    else:
                        var22 = -0.044533405
        else:
            if input[0] < 2.0:
                if input[19] < 2048.0:
                    if input[29] < 5309.0:
                        var22 = -0.030805513
                    else:
                        var22 = 0.007990192
                else:
                    if input[30] < 113.0:
                        var22 = -0.002787275
                    else:
                        var22 = 0.07645234
            else:
                if input[13] < 3.0:
                    if input[12] < 128.0:
                        var22 = 0.014927062
                    else:
                        var22 = 0.096196994
                else:
                    if input[42] < 8065.0:
                        var22 = 0.10936954
                    else:
                        var22 = -0.046509836
    else:
        if input[21] < 105.0:
            if input[37] < 388.0:
                if input[81] < 1.0:
                    if input[30] < 95.0:
                        var22 = 0.03781915
                    else:
                        var22 = -0.07149314
                else:
                    if input[32] < 2.0:
                        var22 = -0.049792834
                    else:
                        var22 = 0.041311726
            else:
                if input[46] < 2308.0:
                    if input[55] < 241.0:
                        var22 = -0.0816608
                    else:
                        var22 = 0.043029718
                else:
                    if input[44] < 3.0:
                        var22 = 0.10013368
                    else:
                        var22 = -0.011852687
        else:
            if input[48] < 29.0:
                if input[16] < 153.0:
                    if input[15] < 7540.0:
                        var22 = 0.085716285
                    else:
                        var22 = -0.04408296
                else:
                    if input[49] < 2.0:
                        var22 = 0.04065131
                    else:
                        var22 = -0.13838515
            else:
                if input[28] < 1022.0:
                    if input[16] < 109.0:
                        var22 = 0.037565093
                    else:
                        var22 = -0.13636594
                else:
                    var22 = 0.07142856
    if input[6] < 2.0:
        if input[46] < 2071.0:
            if input[19] < 1923.0:
                if input[28] < 130.0:
                    if input[37] < -1700.0:
                        var23 = -0.068073824
                    else:
                        var23 = -0.015136625
                else:
                    if input[0] < 2.0:
                        var23 = 0.003755829
                    else:
                        var23 = 0.049047258
            else:
                if input[33] < 5925.0:
                    if input[23] < 4.0:
                        var23 = 0.07664023
                    else:
                        var23 = -0.0220418
                else:
                    if input[124] < 1.0:
                        var23 = 0.03477528
                    else:
                        var23 = -0.07524147
        else:
            if input[37] < 310.0:
                if input[21] < 104.0:
                    if input[66] < 1.0:
                        var23 = 0.01205462
                    else:
                        var23 = -0.09448739
                else:
                    if input[48] < 25.0:
                        var23 = 0.07359744
                    else:
                        var23 = -0.038007464
            else:
                if input[15] < 6812.0:
                    if input[24] < 8463.0:
                        var23 = 0.09747063
                    else:
                        var23 = -0.030493615
                else:
                    if input[41] < 1.0:
                        var23 = -0.06138304
                    else:
                        var23 = 0.053510785
    else:
        if input[15] < 5943.0:
            if input[34] < 110.0:
                if input[21] < 102.0:
                    if input[28] < 1394.0:
                        var23 = -0.036604803
                    else:
                        var23 = 0.10958792
                else:
                    if input[25] < 98.0:
                        var23 = -0.034517594
                    else:
                        var23 = 0.09381279
            else:
                if input[28] < -427.0:
                    if input[106] < 1.0:
                        var23 = -0.06858262
                    else:
                        var23 = 0.08381215
                else:
                    if input[42] < 6642.0:
                        var23 = 0.0313048
                    else:
                        var23 = -0.037494708
        else:
            if input[55] < 1223.0:
                if input[52] < 33.0:
                    if input[91] < 1.0:
                        var23 = -0.08435261
                    else:
                        var23 = 0.026213938
                else:
                    if input[29] < 5622.0:
                        var23 = -0.043579184
                    else:
                        var23 = 0.103292525
            else:
                if input[27] < 3.0:
                    if input[43] < 116.0:
                        var23 = -0.0037353404
                    else:
                        var23 = 0.19656861
                else:
                    var23 = -0.05665352
    if input[28] < 1369.0:
        if input[46] < 393.0:
            if input[37] < -1018.0:
                if input[12] < 139.0:
                    if input[25] < 101.0:
                        var24 = -0.028132332
                    else:
                        var24 = -0.07950976
                else:
                    if input[39] < 117.0:
                        var24 = 0.07239664
                    else:
                        var24 = -0.051701147
            else:
                if input[15] < 6398.0:
                    if input[46] < -3353.0:
                        var24 = -0.06381511
                    else:
                        var24 = 0.0012933965
                else:
                    if input[39] < 107.0:
                        var24 = -0.0912522
                    else:
                        var24 = -0.025919938
        else:
            if input[19] < 1380.0:
                if input[28] < -1714.0:
                    if input[55] < -121.0:
                        var24 = 0.018975895
                    else:
                        var24 = -0.07215162
                else:
                    if input[29] < 6913.0:
                        var24 = 0.0040889196
                    else:
                        var24 = 0.06038099
            else:
                if input[26] < 6.0:
                    if input[12] < 111.0:
                        var24 = -0.026100338
                    else:
                        var24 = 0.07732501
                else:
                    if input[13] < 7.0:
                        var24 = -0.049549542
                    else:
                        var24 = 0.112926476
    else:
        if input[19] < -324.0:
            if input[18] < 4.0:
                if input[42] < 5737.0:
                    if input[29] < 5888.0:
                        var24 = 0.08144592
                    else:
                        var24 = -0.0016635036
                else:
                    if input[20] < 7254.0:
                        var24 = -0.0942783
                    else:
                        var24 = -0.009864609
            else:
                if input[22] < 5.0:
                    var24 = -0.05515767
                else:
                    if input[42] < 7820.0:
                        var24 = 0.12287873
                    else:
                        var24 = -0.030730093
        else:
            if input[55] < -1406.0:
                if input[37] < 651.0:
                    var24 = -0.15168202
                else:
                    var24 = 0.04675648
            else:
                if input[0] < 1.0:
                    if input[30] < 108.0:
                        var24 = -0.027869642
                    else:
                        var24 = 0.047568724
                else:
                    if input[37] < -315.0:
                        var24 = 0.039008807
                    else:
                        var24 = 0.09694006
    if input[6] < 2.0:
        if input[9] < 7.0:
            if input[48] < 17.0:
                if input[26] < 4.0:
                    if input[69] < 1.0:
                        var25 = 0.12143344
                    else:
                        var25 = 0.026163502
                else:
                    var25 = 0.02523082
            else:
                if input[19] < -976.0:
                    if input[16] < 134.0:
                        var25 = -0.1726542
                    else:
                        var25 = -0.009266139
                else:
                    if input[42] < 6407.0:
                        var25 = 0.08150017
                    else:
                        var25 = -0.020568466
        else:
            if input[19] < 1923.0:
                if input[46] < 2071.0:
                    if input[0] < 2.0:
                        var25 = -0.013098433
                    else:
                        var25 = 0.029971743
                else:
                    if input[48] < 19.0:
                        var25 = 0.0580095
                    else:
                        var25 = 0.0072922492
            else:
                if input[44] < 3.0:
                    if input[124] < 1.0:
                        var25 = 0.088930294
                    else:
                        var25 = -0.0029676075
                else:
                    if input[37] < -704.0:
                        var25 = -0.025044858
                    else:
                        var25 = 0.04308217
    else:
        if input[19] < -324.0:
            if input[45] < 3.0:
                if input[88] < 1.0:
                    if input[12] < 72.0:
                        var25 = 0.0052051707
                    else:
                        var25 = -0.08983671
                else:
                    var25 = 0.047963314
            else:
                if input[33] < 6112.0:
                    if input[11] < 4686.0:
                        var25 = -0.0610039
                    else:
                        var25 = 0.047844958
                else:
                    if input[19] < -1903.0:
                        var25 = -0.010718223
                    else:
                        var25 = -0.11532418
        else:
            if input[29] < 5702.0:
                if input[42] < 7504.0:
                    if input[48] < 23.0:
                        var25 = -0.041313644
                    else:
                        var25 = 0.031809725
                else:
                    if input[33] < 5418.0:
                        var25 = 0.009379369
                    else:
                        var25 = -0.10605373
            else:
                if input[28] < 544.0:
                    if input[43] < 134.0:
                        var25 = 0.014695498
                    else:
                        var25 = -0.047116112
                else:
                    if input[34] < 143.0:
                        var25 = 0.07951598
                    else:
                        var25 = -0.059652507
    if input[28] < -1582.0:
        if input[43] < 95.0:
            if input[37] < 111.0:
                if input[46] < 2035.0:
                    if input[43] < 91.0:
                        var26 = -0.10017594
                    else:
                        var26 = -0.006784975
                else:
                    if input[47] < 5097.0:
                        var26 = 0.1257105
                    else:
                        var26 = -0.039813887
            else:
                if input[46] < 2035.0:
                    var26 = 0.1639102
                else:
                    var26 = 0.009914414
        else:
            if input[37] < 1102.0:
                if input[34] < 84.0:
                    var26 = 0.114551246
                else:
                    if input[15] < 5464.0:
                        var26 = -0.030833185
                    else:
                        var26 = -0.081608355
            else:
                if input[12] < 124.0:
                    if input[122] < 1.0:
                        var26 = -0.06207943
                    else:
                        var26 = 0.11668757
                else:
                    if input[50] < 2.0:
                        var26 = -0.06525965
                    else:
                        var26 = 0.12750046
    else:
        if input[38] < 7020.0:
            if input[28] < 1900.0:
                if input[33] < 7271.0:
                    if input[46] < -1540.0:
                        var26 = -0.026466567
                    else:
                        var26 = 0.0022169615
                else:
                    if input[16] < 95.0:
                        var26 = 0.011442658
                    else:
                        var26 = -0.07633782
            else:
                if input[85] < 1.0:
                    if input[11] < 5395.0:
                        var26 = 0.0014439416
                    else:
                        var26 = 0.075562455
                else:
                    if input[28] < 2133.0:
                        var26 = 0.047661137
                    else:
                        var26 = -0.15605178
        else:
            if input[15] < 6147.0:
                if input[29] < 6405.0:
                    if input[116] < 1.0:
                        var26 = 0.030833507
                    else:
                        var26 = -0.07623925
                else:
                    if input[35] < 7.0:
                        var26 = 0.08421207
                    else:
                        var26 = -0.06872368
            else:
                if input[18] < 3.0:
                    if input[29] < 5479.0:
                        var26 = -0.059045114
                    else:
                        var26 = -0.0009102636
                else:
                    if input[18] < 4.0:
                        var26 = 0.07446827
                    else:
                        var26 = 0.0012343809
    if input[28] < 1369.0:
        if input[37] < 1342.0:
            if input[42] < 6868.0:
                if input[19] < 2680.0:
                    if input[33] < 5331.0:
                        var27 = 0.027675299
                    else:
                        var27 = -0.00874569
                else:
                    if input[37] < -1377.0:
                        var27 = -0.00673772
                    else:
                        var27 = 0.07769474
            else:
                if input[24] < 7137.0:
                    if input[11] < 7850.0:
                        var27 = -0.023025405
                    else:
                        var27 = 0.09391048
                else:
                    if input[37] < -929.0:
                        var27 = -0.10364654
                    else:
                        var27 = -0.041756663
        else:
            if input[15] < 6565.0:
                if input[39] < 89.0:
                    if input[87] < 1.0:
                        var27 = 0.016357033
                    else:
                        var27 = -0.113312855
                else:
                    if input[55] < 725.0:
                        var27 = 0.033272173
                    else:
                        var27 = 0.092067465
            else:
                if input[12] < 106.0:
                    if input[29] < 6705.0:
                        var27 = -0.07503822
                    else:
                        var27 = 0.06287355
                else:
                    if input[30] < 127.0:
                        var27 = 0.02449385
                    else:
                        var27 = -0.13326852
    else:
        if input[81] < 1.0:
            if input[19] < 306.0:
                if input[23] < 3.0:
                    if input[24] < 5113.0:
                        var27 = -0.0670686
                    else:
                        var27 = 0.023071647
                else:
                    if input[9] < 12.0:
                        var27 = 0.07359194
                    else:
                        var27 = -0.10852202
            else:
                if input[33] < 5877.0:
                    if input[48] < 22.0:
                        var27 = 0.104076855
                    else:
                        var27 = 0.022943228
                else:
                    if input[33] < 6248.0:
                        var27 = -0.08577989
                    else:
                        var27 = 0.03146784
        else:
            if input[46] < -1174.0:
                if input[34] < 137.0:
                    if input[39] < 92.0:
                        var27 = 0.107755184
                    else:
                        var27 = 0.004807594
                else:
                    if input[34] < 149.0:
                        var27 = -0.12274953
                    else:
                        var27 = 0.012175783
            else:
                if input[35] < 7.0:
                    if input[15] < 5932.0:
                        var27 = 0.09344571
                    else:
                        var27 = 0.031834483
                else:
                    if input[60] < 1.0:
                        var27 = -0.10666517
                    else:
                        var27 = 0.04634839
    if input[6] < 2.0:
        if input[39] < 119.0:
            if input[12] < 137.0:
                if input[38] < 6301.0:
                    if input[42] < 7519.0:
                        var28 = -0.015735978
                    else:
                        var28 = -0.060278524
                else:
                    if input[9] < 22.0:
                        var28 = 0.012954915
                    else:
                        var28 = -0.07474091
            else:
                if input[43] < 116.0:
                    if input[5] < 3.0:
                        var28 = -0.09137417
                    else:
                        var28 = 0.028316481
                else:
                    if input[44] < 6.0:
                        var28 = 0.03357676
                    else:
                        var28 = 0.13307966
        else:
            if input[15] < 4742.0:
                if input[29] < 4691.0:
                    if input[52] < 16.0:
                        var28 = 0.058482558
                    else:
                        var28 = -0.104651205
                else:
                    if input[28] < -1405.0:
                        var28 = -0.0025615217
                    else:
                        var28 = 0.07842792
            else:
                if input[33] < 5992.0:
                    if input[50] < 5.0:
                        var28 = 0.030036435
                    else:
                        var28 = -0.035197712
                else:
                    if input[25] < 101.0:
                        var28 = 0.015186727
                    else:
                        var28 = -0.022959108
    else:
        if input[15] < 5943.0:
            if input[34] < 110.0:
                if input[21] < 102.0:
                    if input[48] < 19.0:
                        var28 = 0.041989233
                    else:
                        var28 = -0.05378894
                else:
                    if input[25] < 105.0:
                        var28 = -0.005468385
                    else:
                        var28 = 0.09641013
            else:
                if input[28] < -427.0:
                    if input[106] < 1.0:
                        var28 = -0.059896242
                    else:
                        var28 = 0.08016093
                else:
                    if input[39] < 106.0:
                        var28 = -0.057686992
                    else:
                        var28 = 0.011543772
        else:
            if input[55] < 1223.0:
                if input[52] < 33.0:
                    if input[91] < 1.0:
                        var28 = -0.074855134
                    else:
                        var28 = 0.033025723
                else:
                    if input[29] < 5622.0:
                        var28 = -0.038910117
                    else:
                        var28 = 0.098368175
            else:
                if input[20] < 6229.0:
                    if input[43] < 109.0:
                        var28 = 0.002788605
                    else:
                        var28 = 0.17524573
                else:
                    var28 = -0.057766784
    if input[19] < -892.0:
        if input[2] < 3.0:
            if input[37] < -1852.0:
                if input[13] < 2.0:
                    if input[20] < 5554.0:
                        var29 = -0.014053262
                    else:
                        var29 = -0.11034738
                else:
                    if input[43] < 107.0:
                        var29 = 0.094889656
                    else:
                        var29 = -0.07965233
            else:
                if input[79] < 1.0:
                    if input[43] < 147.0:
                        var29 = -0.0016856393
                    else:
                        var29 = -0.087256126
                else:
                    if input[12] < 84.0:
                        var29 = 0.044216674
                    else:
                        var29 = -0.116580404
        else:
            if input[14] < 3.0:
                if input[34] < 123.0:
                    var29 = 0.062385645
                else:
                    var29 = -0.076379254
            else:
                if input[16] < 108.0:
                    var29 = -0.009955527
                else:
                    var29 = -0.10980713
    else:
        if input[6] < 1.0:
            if input[46] < 710.0:
                if input[15] < 5019.0:
                    if input[26] < 7.0:
                        var29 = 0.051274057
                    else:
                        var29 = -0.089641646
                else:
                    if input[87] < 1.0:
                        var29 = 0.024237797
                    else:
                        var29 = -0.037388816
            else:
                if input[24] < 6954.0:
                    if input[3] < 10.0:
                        var29 = -0.02749878
                    else:
                        var29 = 0.082096055
                else:
                    if input[30] < 128.0:
                        var29 = -0.040795453
                    else:
                        var29 = 0.07413243
        else:
            if input[91] < 1.0:
                if input[23] < 1.0:
                    if input[30] < 109.0:
                        var29 = -0.045193452
                    else:
                        var29 = 0.05629887
                else:
                    if input[11] < 7909.0:
                        var29 = -0.012433603
                    else:
                        var29 = 0.070975296
            else:
                if input[29] < 5086.0:
                    if input[38] < 7020.0:
                        var29 = -0.096353106
                    else:
                        var29 = 0.08759399
                else:
                    if input[16] < 98.0:
                        var29 = 0.0034033314
                    else:
                        var29 = 0.1073184
    if input[28] < -1582.0:
        if input[21] < 117.0:
            if input[11] < 6332.0:
                if input[6] < 1.0:
                    if input[125] < 1.0:
                        var30 = 0.07063357
                    else:
                        var30 = -0.055072486
                else:
                    if input[90] < 1.0:
                        var30 = -0.072043285
                    else:
                        var30 = 0.007130609
            else:
                if input[44] < 4.0:
                    if input[12] < 116.0:
                        var30 = 0.12780343
                    else:
                        var30 = 0.009046116
                else:
                    if input[27] < 3.0:
                        var30 = -0.08921837
                    else:
                        var30 = 0.024899377
        else:
            if input[29] < 5974.0:
                if input[38] < 7616.0:
                    var30 = -0.08488621
                else:
                    var30 = 0.07236748
            else:
                if input[87] < 1.0:
                    var30 = 0.14421901
                else:
                    var30 = 0.033528987
    else:
        if input[38] < 7020.0:
            if input[28] < 1900.0:
                if input[42] < 5177.0:
                    if input[104] < 1.0:
                        var30 = 0.06490466
                    else:
                        var30 = -0.08348648
                else:
                    if input[11] < 4258.0:
                        var30 = -0.06907536
                    else:
                        var30 = -0.0070836507
            else:
                if input[85] < 1.0:
                    if input[11] < 5395.0:
                        var30 = 0.0010102976
                    else:
                        var30 = 0.06757391
                else:
                    if input[28] < 2133.0:
                        var30 = 0.05062905
                    else:
                        var30 = -0.14483972
        else:
            if input[15] < 6147.0:
                if input[29] < 6405.0:
                    if input[16] < 92.0:
                        var30 = 0.073073916
                    else:
                        var30 = 0.013815935
                else:
                    if input[35] < 7.0:
                        var30 = 0.077093504
                    else:
                        var30 = -0.06280086
            else:
                if input[18] < 3.0:
                    if input[29] < 5479.0:
                        var30 = -0.0519961
                    else:
                        var30 = -0.00032629273
                else:
                    if input[21] < 120.0:
                        var30 = 0.021541325
                    else:
                        var30 = 0.11615123
    if input[37] < -1987.0:
        if input[12] < 109.0:
            if input[11] < 6531.0:
                if input[43] < 105.0:
                    if input[26] < 3.0:
                        var31 = 0.06292834
                    else:
                        var31 = -0.068094306
                else:
                    if input[21] < 120.0:
                        var31 = -0.1154949
                    else:
                        var31 = -0.033957906
            else:
                var31 = 0.06981043
        else:
            if input[38] < 7923.0:
                if input[20] < 6916.0:
                    if input[19] < 3477.0:
                        var31 = -0.056350213
                    else:
                        var31 = 0.08058534
                else:
                    if input[29] < 4648.0:
                        var31 = -0.056444455
                    else:
                        var31 = 0.07409284
            else:
                if input[25] < 108.0:
                    var31 = 0.12601967
                else:
                    if input[44] < 2.0:
                        var31 = 0.08707517
                    else:
                        var31 = -0.079934314
    else:
        if input[2] < 3.0:
            if input[42] < 4997.0:
                if input[48] < 19.0:
                    if input[24] < 7083.0:
                        var31 = 0.1020594
                    else:
                        var31 = 0.004103763
                else:
                    if input[37] < -943.0:
                        var31 = -0.07384669
                    else:
                        var31 = 0.041288827
            else:
                if input[28] < 2233.0:
                    if input[50] < 5.0:
                        var31 = 0.00430063
                    else:
                        var31 = -0.021137686
                else:
                    if input[85] < 1.0:
                        var31 = 0.05404572
                    else:
                        var31 = -0.09726048
        else:
            if input[17] < 2.0:
                if input[0] < 1.0:
                    if input[38] < 5475.0:
                        var31 = -0.007446901
                    else:
                        var31 = -0.0902174
                else:
                    var31 = 0.12246752
            else:
                if input[52] < 29.0:
                    var31 = -0.10879295
                else:
                    var31 = -0.021867177
    if input[3] < 22.0:
        if input[37] < -1987.0:
            if input[11] < 4852.0:
                if input[53] < 4.0:
                    if input[5] < 3.0:
                        var32 = -0.11638025
                    else:
                        var32 = -0.03128771
                else:
                    var32 = 0.0435246
            else:
                if input[38] < 7923.0:
                    if input[19] < 3477.0:
                        var32 = -0.040800776
                    else:
                        var32 = 0.08473803
                else:
                    if input[33] < 7791.0:
                        var32 = 0.096023284
                    else:
                        var32 = -0.049548972
        else:
            if input[2] < 3.0:
                if input[21] < 104.0:
                    if input[11] < 6880.0:
                        var32 = -0.014315805
                    else:
                        var32 = 0.033282004
                else:
                    if input[46] < 1890.0:
                        var32 = 0.0054383306
                    else:
                        var32 = 0.04635958
            else:
                if input[17] < 2.0:
                    if input[0] < 1.0:
                        var32 = -0.06528274
                    else:
                        var32 = 0.11084112
                else:
                    if input[52] < 29.0:
                        var32 = -0.10665295
                    else:
                        var32 = -0.020869603
    else:
        if input[24] < 7286.0:
            if input[33] < 7168.0:
                if input[47] < 4356.0:
                    var32 = -0.050619096
                else:
                    if input[82] < 1.0:
                        var32 = 0.09011372
                    else:
                        var32 = -0.015769465
            else:
                if input[21] < 95.0:
                    var32 = -0.11828991
                else:
                    if input[29] < 6355.0:
                        var32 = 0.084497154
                    else:
                        var32 = -0.039802894
        else:
            if input[31] < 8.0:
                if input[54] < 5.0:
                    var32 = 0.06557257
                else:
                    if input[43] < 91.0:
                        var32 = 0.026103035
                    else:
                        var32 = -0.15038204
            else:
                var32 = 0.09866338
    if input[11] < 4958.0:
        if input[42] < 5059.0:
            if input[33] < 6958.0:
                if input[43] < 102.0:
                    if input[24] < 7597.0:
                        var33 = 0.12108904
                    else:
                        var33 = -0.038901072
                else:
                    if input[28] < 400.0:
                        var33 = -0.033090636
                    else:
                        var33 = 0.08939302
            else:
                if input[48] < 18.0:
                    var33 = 0.020275278
                else:
                    var33 = -0.11082666
        else:
            if input[14] < 5.0:
                if input[29] < 5606.0:
                    if input[51] < 4354.0:
                        var33 = 0.0013048194
                    else:
                        var33 = -0.07413365
                else:
                    if input[6] < 2.0:
                        var33 = 0.019017834
                    else:
                        var33 = -0.04622454
            else:
                if input[33] < 5559.0:
                    if input[38] < 7405.0:
                        var33 = -0.043619037
                    else:
                        var33 = 0.055144984
                else:
                    if input[53] < 4.0:
                        var33 = -0.07737316
                    else:
                        var33 = 0.0062193233
    else:
        if input[46] < -2468.0:
            if input[82] < 1.0:
                if input[12] < 128.0:
                    if input[41] < 6.0:
                        var33 = -0.07868532
                    else:
                        var33 = -0.00035609942
                else:
                    if input[6] < 2.0:
                        var33 = 0.028526893
                    else:
                        var33 = -0.048663132
            else:
                var33 = 0.114226185
        else:
            if input[87] < 1.0:
                if input[37] < 881.0:
                    if input[28] < -2354.0:
                        var33 = -0.07359272
                    else:
                        var33 = 0.018139793
                else:
                    if input[21] < 100.0:
                        var33 = 0.015211477
                    else:
                        var33 = 0.06909902
            else:
                if input[25] < 101.0:
                    if input[39] < 129.0:
                        var33 = 0.00037924966
                    else:
                        var33 = 0.0627043
                else:
                    if input[34] < 145.0:
                        var33 = -0.007479136
                    else:
                        var33 = -0.06512783
    if input[0] < 2.0:
        if input[28] < -1749.0:
            if input[43] < 95.0:
                if input[68] < 1.0:
                    if input[62] < 1.0:
                        var34 = 0.11844198
                    else:
                        var34 = 0.011569588
                else:
                    if input[39] < 119.0:
                        var34 = -0.07805606
                    else:
                        var34 = 0.030942006
            else:
                if input[19] < -817.0:
                    if input[80] < 1.0:
                        var34 = -0.09100321
                    else:
                        var34 = 0.006185501
                else:
                    if input[19] < -714.0:
                        var34 = 0.11439176
                    else:
                        var34 = -0.03550896
        else:
            if input[19] < 2048.0:
                if input[91] < 1.0:
                    if input[42] < 5059.0:
                        var34 = 0.047122143
                    else:
                        var34 = -0.009714702
                else:
                    if input[11] < 5424.0:
                        var34 = -0.0024715634
                    else:
                        var34 = 0.079627044
            else:
                if input[46] < -2992.0:
                    if input[12] < 137.0:
                        var34 = -0.11339392
                    else:
                        var34 = -0.0028091064
                else:
                    if input[21] < 129.0:
                        var34 = 0.029698318
                    else:
                        var34 = 0.10257771
    else:
        if input[11] < 6167.0:
            if input[124] < 1.0:
                if input[12] < 95.0:
                    if input[16] < 128.0:
                        var34 = -0.10151875
                    else:
                        var34 = 0.02157216
                else:
                    if input[24] < 7278.0:
                        var34 = 0.029709196
                    else:
                        var34 = -0.049780417
            else:
                if input[43] < 105.0:
                    if input[37] < 150.0:
                        var34 = -0.13614474
                    else:
                        var34 = 0.05081162
                else:
                    if input[11] < 5347.0:
                        var34 = 0.13640803
                    else:
                        var34 = 0.042115983
        else:
            if input[43] < 138.0:
                if input[63] < 1.0:
                    if input[47] < 3719.0:
                        var34 = 0.0060601924
                    else:
                        var34 = 0.10219361
                else:
                    var34 = -0.038640063
            else:
                var34 = -0.08170878
    if input[6] < 2.0:
        if input[33] < 7651.0:
            if input[39] < 118.0:
                if input[18] < 3.0:
                    if input[12] < 128.0:
                        var35 = -0.034051176
                    else:
                        var35 = 0.020727241
                else:
                    if input[87] < 1.0:
                        var35 = 0.033141177
                    else:
                        var35 = -0.011621504
            else:
                if input[15] < 4742.0:
                    if input[20] < 6974.0:
                        var35 = 0.035230815
                    else:
                        var35 = 0.10739689
                else:
                    if input[25] < 95.0:
                        var35 = 0.03414618
                    else:
                        var35 = 0.0024256776
        else:
            if input[78] < 1.0:
                if input[112] < 1.0:
                    if input[54] < 7.0:
                        var35 = -0.07835426
                    else:
                        var35 = 0.06558751
                else:
                    var35 = 0.075965956
            else:
                if input[68] < 1.0:
                    var35 = -0.012211636
                else:
                    var35 = 0.099786
    else:
        if input[20] < 5315.0:
            if input[29] < 6155.0:
                if input[40] < 6.0:
                    if input[47] < 4967.0:
                        var35 = -0.105406895
                    else:
                        var35 = -0.0140967695
                else:
                    var35 = 0.035403296
            else:
                if input[24] < 5938.0:
                    var35 = 0.13027517
                else:
                    if input[111] < 1.0:
                        var35 = -0.098409824
                    else:
                        var35 = 0.03173056
        else:
            if input[19] < -243.0:
                if input[16] < 133.0:
                    if input[52] < 33.0:
                        var35 = -0.06657951
                    else:
                        var35 = 0.05012503
                else:
                    if input[53] < 1.0:
                        var35 = 0.061139375
                    else:
                        var35 = -0.034369424
            else:
                if input[51] < 5024.0:
                    if input[19] < 2793.0:
                        var35 = -0.02029359
                    else:
                        var35 = 0.062282722
                else:
                    if input[46] < -2425.0:
                        var35 = -0.04734437
                    else:
                        var35 = 0.065829925
    if input[28] < 2233.0:
        if input[29] < 6240.0:
            if input[42] < 6821.0:
                if input[33] < 7702.0:
                    if input[116] < 1.0:
                        var36 = 0.0050402577
                    else:
                        var36 = -0.06312269
                else:
                    if input[19] < 651.0:
                        var36 = -0.08987575
                    else:
                        var36 = 0.0027406514
            else:
                if input[16] < 115.0:
                    if input[52] < 15.0:
                        var36 = -0.06744282
                    else:
                        var36 = 0.008377348
                else:
                    if input[51] < 6437.0:
                        var36 = -0.04755472
                    else:
                        var36 = 0.09550624
        else:
            if input[19] < -2265.0:
                if input[33] < 5816.0:
                    if input[30] < 128.0:
                        var36 = 0.053139735
                    else:
                        var36 = -0.051114924
                else:
                    if input[17] < 9.0:
                        var36 = -0.09626924
                    else:
                        var36 = 0.050178517
            else:
                if input[16] < 89.0:
                    if input[50] < 3.0:
                        var36 = 0.031900316
                    else:
                        var36 = -0.06702076
                else:
                    if input[43] < 126.0:
                        var36 = 0.03483968
                    else:
                        var36 = 0.004500924
    else:
        if input[38] < 5955.0:
            if input[55] < -669.0:
                if input[34] < 104.0:
                    var36 = 0.0456548
                else:
                    var36 = -0.13757624
            else:
                if input[49] < 1.0:
                    if input[52] < 20.0:
                        var36 = 0.13368128
                    else:
                        var36 = -0.010755063
                else:
                    if input[16] < 100.0:
                        var36 = 0.08347489
                    else:
                        var36 = -0.060636815
        else:
            if input[93] < 1.0:
                if input[85] < 1.0:
                    if input[41] < 1.0:
                        var36 = -0.019052437
                    else:
                        var36 = 0.09110852
                else:
                    var36 = -0.049793992
            else:
                if input[15] < 5238.0:
                    var36 = 0.06277554
                else:
                    var36 = -0.12015609
    if input[9] < 7.0:
        if input[48] < 17.0:
            if input[35] < 3.0:
                if input[33] < 6469.0:
                    if input[26] < 4.0:
                        var37 = 0.12058299
                    else:
                        var37 = 0.0076326556
                else:
                    var37 = 0.004815815
            else:
                var37 = -0.004883286
        else:
            if input[46] < -1130.0:
                if input[25] < 105.0:
                    var37 = 0.028773969
                else:
                    var37 = -0.13240008
            else:
                if input[19] < -892.0:
                    if input[16] < 152.0:
                        var37 = -0.10489657
                    else:
                        var37 = 0.043996196
                else:
                    if input[37] < 310.0:
                        var37 = 0.0034474188
                    else:
                        var37 = 0.0813344
    else:
        if input[34] < 76.0:
            if input[41] < 6.0:
                if input[18] < 1.0:
                    var37 = -0.009150653
                else:
                    if input[24] < 5425.0:
                        var37 = 0.032188352
                    else:
                        var37 = 0.14214955
            else:
                var37 = -0.04467454
        else:
            if input[9] < 22.0:
                if input[87] < 1.0:
                    if input[11] < 6668.0:
                        var37 = 0.0034223057
                    else:
                        var37 = 0.044600658
                else:
                    if input[19] < -3105.0:
                        var37 = -0.10134647
                    else:
                        var37 = -0.007241809
            else:
                if input[25] < 105.0:
                    if input[29] < 4727.0:
                        var37 = 0.12893502
                    else:
                        var37 = -0.036170762
                else:
                    if input[17] < 9.0:
                        var37 = -0.09279189
                    else:
                        var37 = 0.033611566
    if input[27] < 6.0:
        if input[37] < -3096.0:
            if input[3] < 14.0:
                if input[46] < -2704.0:
                    var38 = -0.005213028
                else:
                    var38 = -0.110113285
            else:
                if input[15] < 4934.0:
                    var38 = 0.07738465
                else:
                    if input[32] < 5.0:
                        var38 = -0.003495833
                    else:
                        var38 = -0.076649815
        else:
            if input[46] < -3116.0:
                if input[60] < 1.0:
                    if input[66] < 1.0:
                        var38 = -0.07827505
                    else:
                        var38 = 0.023378335
                else:
                    if input[38] < 4676.0:
                        var38 = 0.14032122
                    else:
                        var38 = -0.02771143
            else:
                if input[19] < 2048.0:
                    if input[107] < 1.0:
                        var38 = -0.009043539
                    else:
                        var38 = 0.010119098
                else:
                    if input[21] < 129.0:
                        var38 = 0.02000368
                    else:
                        var38 = 0.092656754
    else:
        if input[50] < 5.0:
            if input[81] < 1.0:
                if input[113] < 1.0:
                    if input[33] < 5816.0:
                        var38 = 0.101286486
                    else:
                        var38 = -0.012326408
                else:
                    if input[9] < 9.0:
                        var38 = -0.11727337
                    else:
                        var38 = 0.025485544
            else:
                if input[33] < 6871.0:
                    var38 = 0.11963619
                else:
                    var38 = 0.021489305
        else:
            if input[16] < 112.0:
                var38 = 0.08037614
            else:
                if input[28] < 1158.0:
                    var38 = -0.12677686
                else:
                    var38 = -0.012844527
    if input[0] < 2.0:
        if input[28] < -1749.0:
            if input[43] < 95.0:
                if input[68] < 1.0:
                    if input[62] < 1.0:
                        var39 = 0.10903602
                    else:
                        var39 = 0.011264794
                else:
                    if input[39] < 119.0:
                        var39 = -0.07311364
                    else:
                        var39 = 0.030858133
            else:
                if input[19] < -817.0:
                    if input[30] < 84.0:
                        var39 = 0.02794291
                    else:
                        var39 = -0.084906496
                else:
                    if input[55] < -306.0:
                        var39 = 0.018140553
                    else:
                        var39 = -0.053213157
        else:
            if input[46] < 3058.0:
                if input[91] < 1.0:
                    if input[34] < 142.0:
                        var39 = -0.0002128335
                    else:
                        var39 = -0.0318927
                else:
                    if input[11] < 4904.0:
                        var39 = -0.026770508
                    else:
                        var39 = 0.054654974
            else:
                if input[18] < 2.0:
                    if input[33] < 5695.0:
                        var39 = -0.059424043
                    else:
                        var39 = 0.044266324
                else:
                    if input[36] < 2.0:
                        var39 = 0.013714479
                    else:
                        var39 = 0.10575606
    else:
        if input[11] < 6167.0:
            if input[124] < 1.0:
                if input[34] < 85.0:
                    var39 = 0.1095702
                else:
                    if input[34] < 107.0:
                        var39 = -0.05218291
                    else:
                        var39 = 0.009846254
            else:
                if input[43] < 105.0:
                    if input[37] < 150.0:
                        var39 = -0.124694824
                    else:
                        var39 = 0.047266018
                else:
                    if input[11] < 5347.0:
                        var39 = 0.12868068
                    else:
                        var39 = 0.03984894
        else:
            if input[43] < 138.0:
                if input[63] < 1.0:
                    if input[16] < 127.0:
                        var39 = 0.099311545
                    else:
                        var39 = 0.0145788565
                else:
                    var39 = -0.04060962
            else:
                var39 = -0.07684565
    if input[6] < 2.0:
        if input[15] < 7540.0:
            if input[46] < 2235.0:
                if input[25] < 104.0:
                    if input[85] < 1.0:
                        var40 = 0.016062489
                    else:
                        var40 = -0.053225774
                else:
                    if input[9] < 22.0:
                        var40 = -0.004383895
                    else:
                        var40 = -0.08367693
            else:
                if input[37] < 272.0:
                    if input[11] < 6030.0:
                        var40 = 0.0000806495
                    else:
                        var40 = 0.06362384
                else:
                    if input[16] < 130.0:
                        var40 = 0.09348875
                    else:
                        var40 = 0.01974174
        else:
            if input[21] < 123.0:
                if input[34] < 84.0:
                    var40 = 0.08282584
                else:
                    if input[63] < 1.0:
                        var40 = -0.069567874
                    else:
                        var40 = 0.044851985
            else:
                if input[42] < 6712.0:
                    var40 = 0.123965
                else:
                    var40 = -0.06594254
    else:
        if input[34] < 110.0:
            if input[12] < 103.0:
                if input[26] < 6.0:
                    if input[42] < 6366.0:
                        var40 = 0.04715723
                    else:
                        var40 = -0.12592031
                else:
                    if input[47] < 4197.0:
                        var40 = 0.12590288
                    else:
                        var40 = -0.04235777
            else:
                if input[25] < 105.0:
                    if input[37] < 1342.0:
                        var40 = -0.06549435
                    else:
                        var40 = 0.07033822
                else:
                    if input[45] < 4.0:
                        var40 = 0.037067
                    else:
                        var40 = 0.13648085
        else:
            if input[28] < -427.0:
                if input[106] < 1.0:
                    if input[25] < 121.0:
                        var40 = -0.032336745
                    else:
                        var40 = -0.08519911
                else:
                    var40 = 0.08751049
            else:
                if input[39] < 109.0:
                    if input[28] < 895.0:
                        var40 = -0.075951405
                    else:
                        var40 = 0.00780792
                else:
                    if input[41] < 4.0:
                        var40 = -0.012607676
                    else:
                        var40 = 0.06174902
    if input[37] < -3096.0:
        if input[3] < 14.0:
            if input[42] < 8240.0:
                var41 = -0.10708957
            else:
                var41 = -0.005463665
        else:
            if input[31] < 1.0:
                var41 = 0.07446436
            else:
                if input[12] < 108.0:
                    var41 = -0.080774866
                else:
                    var41 = 0.0012992461
    else:
        if input[34] < 76.0:
            if input[41] < 6.0:
                if input[18] < 1.0:
                    var41 = -0.008664627
                else:
                    if input[25] < 88.0:
                        var41 = 0.036950048
                    else:
                        var41 = 0.13364968
            else:
                var41 = -0.039879974
        else:
            if input[39] < 108.0:
                if input[25] < 80.0:
                    if input[38] < 5652.0:
                        var41 = -0.025134882
                    else:
                        var41 = 0.09060695
                else:
                    if input[16] < 89.0:
                        var41 = -0.068505645
                    else:
                        var41 = -0.011859248
            else:
                if input[50] < 5.0:
                    if input[11] < 6471.0:
                        var41 = 0.003656117
                    else:
                        var41 = 0.033342868
                else:
                    if input[11] < 5194.0:
                        var41 = -0.05839462
                    else:
                        var41 = -0.0070236954
    if input[23] < 1.0:
        if input[19] < -783.0:
            if input[43] < 99.0:
                var42 = 0.10151346
            else:
                if input[19] < -2299.0:
                    if input[14] < 6.0:
                        var42 = 0.10046061
                    else:
                        var42 = -0.049704444
                else:
                    if input[37] < 1988.0:
                        var42 = -0.06365927
                    else:
                        var42 = 0.065591894
        else:
            if input[30] < 127.0:
                if input[38] < 5967.0:
                    if input[52] < 28.0:
                        var42 = -0.061522402
                    else:
                        var42 = 0.10609803
                else:
                    if input[33] < 5816.0:
                        var42 = 0.074343644
                    else:
                        var42 = -0.0044656466
            else:
                if input[50] < 6.0:
                    if input[55] < -1059.0:
                        var42 = -0.056515463
                    else:
                        var42 = 0.08660569
                else:
                    var42 = -0.05170545
    else:
        if input[11] < 7909.0:
            if input[91] < 1.0:
                if input[0] < 1.0:
                    if input[47] < 3808.0:
                        var42 = -0.044505302
                    else:
                        var42 = -0.011160337
                else:
                    if input[16] < 139.0:
                        var42 = 0.010591659
                    else:
                        var42 = -0.025243282
            else:
                if input[56] < 1.0:
                    if input[38] < 5667.0:
                        var42 = -0.04204194
                    else:
                        var42 = 0.10386574
                else:
                    if input[34] < 140.0:
                        var42 = -0.033424493
                    else:
                        var42 = 0.09238489
        else:
            if input[41] < 6.0:
                if input[18] < 3.0:
                    var42 = -0.05187973
                else:
                    if input[24] < 5288.0:
                        var42 = -0.013641754
                    else:
                        var42 = 0.10079055
            else:
                var42 = -0.06406777
    if input[28] < 2233.0:
        if input[29] < 6240.0:
            if input[33] < 7878.0:
                if input[53] < 3.0:
                    if input[39] < 108.0:
                        var43 = -0.038783953
                    else:
                        var43 = -0.004326447
                else:
                    if input[52] < 30.0:
                        var43 = 0.005245845
                    else:
                        var43 = 0.088868245
            else:
                if input[48] < 15.0:
                    if input[9] < 19.0:
                        var43 = 0.089304276
                    else:
                        var43 = -0.062268008
                else:
                    if input[21] < 120.0:
                        var43 = -0.114805155
                    else:
                        var43 = 0.03652286
        else:
            if input[16] < 89.0:
                if input[21] < 113.0:
                    if input[52] < 17.0:
                        var43 = -0.14359073
                    else:
                        var43 = -0.01918955
                else:
                    if input[9] < 13.0:
                        var43 = 0.1022862
                    else:
                        var43 = -0.03360835
            else:
                if input[19] < -1072.0:
                    if input[110] < 1.0:
                        var43 = -0.014087136
                    else:
                        var43 = 0.07142937
                else:
                    if input[48] < 25.0:
                        var43 = 0.035889756
                    else:
                        var43 = -0.01156848
    else:
        if input[61] < 1.0:
            if input[38] < 5955.0:
                if input[55] < -669.0:
                    if input[34] < 104.0:
                        var43 = 0.040894907
                    else:
                        var43 = -0.12776187
                else:
                    if input[16] < 137.0:
                        var43 = 0.07133486
                    else:
                        var43 = -0.078750335
            else:
                if input[85] < 1.0:
                    if input[93] < 1.0:
                        var43 = 0.08511346
                    else:
                        var43 = -0.039687697
                else:
                    var43 = -0.04449395
        else:
            if input[17] < 3.0:
                var43 = 0.020611927
            else:
                var43 = -0.12822469
    if input[19] < 2862.0:
        if input[29] < 4648.0:
            if input[51] < 4178.0:
                if input[47] < 5144.0:
                    if input[12] < 104.0:
                        var44 = -0.067062944
                    else:
                        var44 = 0.064423166
                else:
                    var44 = -0.11846179
            else:
                if input[87] < 1.0:
                    if input[6] < 2.0:
                        var44 = 0.028391827
                    else:
                        var44 = -0.08856689
                else:
                    if input[14] < 1.0:
                        var44 = -0.009686886
                    else:
                        var44 = -0.12189915
        else:
            if input[91] < 1.0:
                if input[21] < 104.0:
                    if input[39] < 153.0:
                        var44 = -0.012899913
                    else:
                        var44 = 0.08266956
                else:
                    if input[46] < 1890.0:
                        var44 = 0.0012722505
                    else:
                        var44 = 0.037077434
            else:
                if input[34] < 140.0:
                    if input[28] < -1387.0:
                        var44 = -0.08962964
                    else:
                        var44 = 0.03433009
                else:
                    if input[39] < 108.0:
                        var44 = -0.0030870982
                    else:
                        var44 = 0.15456061
    else:
        if input[20] < 5855.0:
            if input[20] < 5554.0:
                if input[11] < 7220.0:
                    var44 = -0.073294245
                else:
                    if input[34] < 126.0:
                        var44 = -0.0005211235
                    else:
                        var44 = 0.1305907
            else:
                if input[46] < 246.0:
                    if input[29] < 5332.0:
                        var44 = -0.007742479
                    else:
                        var44 = -0.14456013
                else:
                    if input[40] < 5.0:
                        var44 = 0.07066438
                    else:
                        var44 = -0.05847572
        else:
            if input[16] < 72.0:
                if input[29] < 5385.0:
                    if input[81] < 1.0:
                        var44 = 0.11644894
                    else:
                        var44 = -0.013427595
                else:
                    if input[29] < 5983.0:
                        var44 = -0.13574563
                    else:
                        var44 = 0.025557129
            else:
                if input[29] < 5473.0:
                    if input[9] < 12.0:
                        var44 = -0.03748674
                    else:
                        var44 = 0.06686878
                else:
                    if input[19] < 2950.0:
                        var44 = 0.035671413
                    else:
                        var44 = 0.1107824
    if input[34] < 76.0:
        if input[41] < 6.0:
            if input[18] < 1.0:
                var45 = -0.008901053
            else:
                if input[25] < 88.0:
                    var45 = 0.03446422
                else:
                    var45 = 0.12810516
        else:
            var45 = -0.03738613
    else:
        if input[9] < 7.0:
            if input[48] < 17.0:
                if input[35] < 3.0:
                    if input[24] < 6359.0:
                        var45 = 0.11480402
                    else:
                        var45 = 0.029463751
                else:
                    var45 = -0.007922017
            else:
                if input[46] < -1174.0:
                    if input[24] < 5089.0:
                        var45 = 0.010644382
                    else:
                        var45 = -0.13395445
                else:
                    if input[19] < -892.0:
                        var45 = -0.058632683
                    else:
                        var45 = 0.04228698
        else:
            if input[107] < 1.0:
                if input[19] < 2015.0:
                    if input[43] < 127.0:
                        var45 = -0.0034757068
                    else:
                        var45 = -0.029919622
                else:
                    if input[25] < 127.0:
                        var45 = 0.02943184
                    else:
                        var45 = -0.09575906
            else:
                if input[24] < 7063.0:
                    if input[38] < 7299.0:
                        var45 = 0.004984932
                    else:
                        var45 = 0.04235549
                else:
                    if input[21] < 113.0:
                        var45 = -0.030186946
                    else:
                        var45 = 0.03972266
    if input[27] < 6.0:
        if input[106] < 1.0:
            if input[107] < 1.0:
                if input[34] < 82.0:
                    if input[47] < 3985.0:
                        var46 = -0.03440764
                    else:
                        var46 = 0.10020818
                else:
                    if input[42] < 5833.0:
                        var46 = 0.009091151
                    else:
                        var46 = -0.016153445
            else:
                if input[73] < 1.0:
                    if input[91] < 1.0:
                        var46 = 0.0019110717
                    else:
                        var46 = 0.051145285
                else:
                    if input[29] < 5498.0:
                        var46 = 0.13747789
                    else:
                        var46 = 0.03174979
        else:
            if input[2] < 2.0:
                if input[12] < 114.0:
                    if input[9] < 18.0:
                        var46 = 0.15343465
                    else:
                        var46 = -0.02129024
                else:
                    if input[19] < 1408.0:
                        var46 = -0.01477396
                    else:
                        var46 = 0.09458766
            else:
                if input[25] < 110.0:
                    var46 = -0.0837892
                else:
                    var46 = -0.022565758
    else:
        if input[50] < 5.0:
            if input[81] < 1.0:
                if input[113] < 1.0:
                    if input[33] < 5816.0:
                        var46 = 0.09705072
                    else:
                        var46 = -0.017187588
                else:
                    if input[9] < 9.0:
                        var46 = -0.11755376
                    else:
                        var46 = 0.02278906
            else:
                if input[33] < 6733.0:
                    var46 = 0.11592752
                else:
                    var46 = 0.024568794
        else:
            if input[16] < 112.0:
                var46 = 0.074532196
            else:
                if input[28] < 1158.0:
                    var46 = -0.11928109
                else:
                    var46 = -0.016466303
    if input[37] < -3096.0:
        if input[3] < 14.0:
            if input[46] < -2514.0:
                var47 = -0.005384664
            else:
                var47 = -0.10241896
        else:
            if input[15] < 4934.0:
                var47 = 0.07026762
            else:
                if input[27] < 3.0:
                    var47 = -0.005591175
                else:
                    var47 = -0.06904519
    else:
        if input[19] < -3193.0:
            if input[33] < 5456.0:
                if input[39] < 131.0:
                    if input[14] < 5.0:
                        var47 = 0.07751337
                    else:
                        var47 = -0.07141959
                else:
                    var47 = 0.12746269
            else:
                if input[28] < 360.0:
                    if input[29] < 6831.0:
                        var47 = -0.10948213
                    else:
                        var47 = -0.026798267
                else:
                    if input[42] < 6349.0:
                        var47 = 0.04478459
                    else:
                        var47 = -0.105799966
        else:
            if input[106] < 1.0:
                if input[28] < 1369.0:
                    if input[34] < 111.0:
                        var47 = 0.012932601
                    else:
                        var47 = -0.00794968
                else:
                    if input[81] < 1.0:
                        var47 = -0.0051008402
                    else:
                        var47 = 0.04017099
            else:
                if input[12] < 114.0:
                    if input[9] < 18.0:
                        var47 = 0.1371956
                    else:
                        var47 = -0.023211563
                else:
                    if input[19] < 1408.0:
                        var47 = -0.018589405
                    else:
                        var47 = 0.08839788
    if input[18] < 5.0:
        if input[31] < 5.0:
            if input[9] < 6.0:
                if input[23] < 1.0:
                    if input[12] < 98.0:
                        var48 = 0.01821719
                    else:
                        var48 = 0.11102271
                else:
                    if input[37] < 509.0:
                        var48 = -0.04886939
                    else:
                        var48 = 0.08227067
            else:
                if input[106] < 1.0:
                    if input[31] < 4.0:
                        var48 = -0.0063464413
                    else:
                        var48 = -0.03437557
                else:
                    if input[37] < -1065.0:
                        var48 = -0.026501624
                    else:
                        var48 = 0.07860859
        else:
            if input[29] < 6332.0:
                if input[19] < -1873.0:
                    if input[9] < 16.0:
                        var48 = 0.13371953
                    else:
                        var48 = -0.020106
                else:
                    if input[22] < 2.0:
                        var48 = -0.13955885
                    else:
                        var48 = -0.02972039
            else:
                if input[11] < 5260.0:
                    if input[6] < 2.0:
                        var48 = 0.013064248
                    else:
                        var48 = -0.055410665
                else:
                    if input[38] < 4996.0:
                        var48 = -0.046390157
                    else:
                        var48 = 0.05037828
    else:
        if input[16] < 111.0:
            if input[19] < 2015.0:
                if input[58] < 1.0:
                    if input[19] < 1042.0:
                        var48 = 0.008206818
                    else:
                        var48 = -0.05296698
                else:
                    if input[15] < 5053.0:
                        var48 = -0.032910656
                    else:
                        var48 = 0.12522176
            else:
                if input[42] < 7706.0:
                    if input[12] < 126.0:
                        var48 = 0.08317809
                    else:
                        var48 = 0.020474765
                else:
                    if input[54] < 5.0:
                        var48 = -0.06278935
                    else:
                        var48 = 0.0756998
        else:
            if input[20] < 5430.0:
                var48 = -0.09581276
            else:
                if input[47] < 4532.0:
                    if input[30] < 143.0:
                        var48 = 0.112015426
                    else:
                        var48 = -0.027736096
                else:
                    if input[12] < 113.0:
                        var48 = 0.083889656
                    else:
                        var48 = -0.051629215
    if input[42] < 4747.0:
        if input[37] < -943.0:
            if input[19] < -1207.0:
                if input[9] < 13.0:
                    var49 = -0.12574397
                else:
                    var49 = -0.00876461
            else:
                if input[34] < 137.0:
                    var49 = 0.08393387
                else:
                    var49 = -0.046725508
        else:
            if input[20] < 5568.0:
                var49 = -0.0198236
            else:
                if input[12] < 135.0:
                    if input[33] < 4811.0:
                        var49 = 0.025534926
                    else:
                        var49 = 0.11159487
                else:
                    var49 = -0.0047615357
    else:
        if input[11] < 4113.0:
            if input[34] < 91.0:
                var49 = 0.08124209
            else:
                if input[20] < 7740.0:
                    if input[25] < 130.0:
                        var49 = -0.078096375
                    else:
                        var49 = 0.04489757
                else:
                    if input[15] < 6645.0:
                        var49 = 0.11711836
                    else:
                        var49 = -0.039588153
        else:
            if input[4] < 1.0:
                if input[29] < 5743.0:
                    if input[116] < 1.0:
                        var49 = -0.0016176623
                    else:
                        var49 = -0.10094642
                else:
                    if input[29] < 5955.0:
                        var49 = 0.04926008
                    else:
                        var49 = 0.010610267
            else:
                if input[55] < 425.0:
                    if input[20] < 7580.0:
                        var49 = -0.0032171085
                    else:
                        var49 = 0.042640913
                else:
                    if input[26] < 1.0:
                        var49 = 0.06856046
                    else:
                        var49 = -0.030249
    var50 = sigmoid(var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44 + var45 + var46 + var47 + var48 + var49)
    return [1.0 - var50, var50]
