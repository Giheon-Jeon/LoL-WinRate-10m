import math
def sigmoid(x):
    if x < 0.0:
        z = math.exp(x)
        return z / (1.0 + z)
    return 1.0 / (1.0 + math.exp(-x))
def score(input):
    if input[15] < 233.0:
        if input[15] < -1610.0:
            if input[15] < -3290.0:
                var0 = -0.08429184
            else:
                var0 = -0.059496045
        else:
            if input[15] < -643.0:
                var0 = -0.03355117
            else:
                var0 = -0.006114103
    else:
        if input[15] < 1774.0:
            if input[16] < 914.0:
                var0 = 0.015340715
            else:
                var0 = 0.044948094
        else:
            if input[15] < 3502.0:
                var0 = 0.06516117
            else:
                var0 = 0.08664151
    if input[15] < 233.0:
        if input[15] < -1610.0:
            if input[15] < -3798.0:
                var1 = -0.08509296
            else:
                var1 = -0.058507957
        else:
            if input[15] < -643.0:
                var1 = -0.03189063
            else:
                var1 = -0.005809562
    else:
        if input[15] < 1564.0:
            if input[16] < 914.0:
                var1 = 0.012849969
            else:
                var1 = 0.04196072
        else:
            if input[15] < 3502.0:
                var1 = 0.059940316
            else:
                var1 = 0.082482725
    if input[15] < 233.0:
        if input[15] < -1556.0:
            if input[15] < -3290.0:
                var2 = -0.07682969
            else:
                var2 = -0.05319167
        else:
            if input[15] < -484.0:
                var2 = -0.027998993
            else:
                var2 = -0.003265998
    else:
        if input[15] < 1774.0:
            if input[16] < 385.0:
                var2 = 0.0075790025
            else:
                var2 = 0.034594662
        else:
            if input[7] < 1.0:
                var2 = 0.055658143
            else:
                var2 = 0.07499277
    if input[15] < -303.0:
        if input[15] < -1933.0:
            if input[15] < -3798.0:
                var3 = -0.078162484
            else:
                var3 = -0.05667764
        else:
            if input[7] < 1.0:
                var3 = -0.035255056
            else:
                var3 = -0.009315039
    else:
        if input[15] < 1344.0:
            if input[26] < 1.0:
                var3 = 0.022622136
            else:
                var3 = -0.0060695093
        else:
            if input[15] < 2015.0:
                var3 = 0.0411386
            else:
                var3 = 0.06529667
    if input[15] < 233.0:
        if input[15] < -1755.0:
            if input[15] < -3798.0:
                var4 = -0.075140014
            else:
                var4 = -0.05252136
        else:
            if input[15] < -643.0:
                var4 = -0.028698293
            else:
                var4 = -0.00503357
    else:
        if input[15] < 1947.0:
            if input[16] < 914.0:
                var4 = 0.013000171
            else:
                var4 = 0.039622482
        else:
            if input[15] < 3703.0:
                var4 = 0.05604992
            else:
                var4 = 0.07454774
    if input[15] < 233.0:
        if input[15] < -1556.0:
            if input[15] < -2794.0:
                var5 = -0.06462365
            else:
                var5 = -0.043894928
        else:
            if input[15] < -484.0:
                var5 = -0.024110926
            else:
                var5 = -0.0029495403
    else:
        if input[15] < 1564.0:
            if input[16] < 1454.0:
                var5 = 0.013575795
            else:
                var5 = 0.04761667
        else:
            if input[7] < 1.0:
                var5 = 0.045848295
            else:
                var5 = 0.06546092
    if input[15] < 629.0:
        if input[15] < -1556.0:
            if input[16] < -1828.0:
                var6 = -0.06002128
            else:
                var6 = -0.039308827
        else:
            if input[16] < -551.0:
                var6 = -0.024801575
            else:
                var6 = -0.000089686175
    else:
        if input[15] < 1989.0:
            if input[16] < 440.0:
                var6 = 0.011346421
            else:
                var6 = 0.035094302
        else:
            if input[7] < 1.0:
                var6 = 0.04900338
            else:
                var6 = 0.06571801
    if input[15] < -303.0:
        if input[15] < -1933.0:
            if input[15] < -3798.0:
                var7 = -0.06825453
            else:
                var7 = -0.047662217
        else:
            if input[7] < 1.0:
                var7 = -0.030163636
            else:
                var7 = -0.005589623
    else:
        if input[15] < 1344.0:
            if input[26] < 1.0:
                var7 = 0.019967072
            else:
                var7 = -0.007131611
        else:
            if input[16] < 2469.0:
                var7 = 0.042274766
            else:
                var7 = 0.06420375
    if input[15] < 629.0:
        if input[15] < -1469.0:
            if input[15] < -2794.0:
                var8 = -0.05812365
            else:
                var8 = -0.03744365
        else:
            if input[26] < 1.0:
                var8 = 0.0010475093
            else:
                var8 = -0.022635931
    else:
        if input[15] < 1989.0:
            if input[16] < 440.0:
                var8 = 0.00992724
            else:
                var8 = 0.032266043
        else:
            if input[15] < 3703.0:
                var8 = 0.047685884
            else:
                var8 = 0.06577402
    if input[15] < -303.0:
        if input[15] < -1933.0:
            if input[15] < -3798.0:
                var9 = -0.064370714
            else:
                var9 = -0.04392919
        else:
            if input[7] < 1.0:
                var9 = -0.02781245
            else:
                var9 = -0.00498131
    else:
        if input[15] < 1344.0:
            if input[26] < 1.0:
                var9 = 0.018477583
            else:
                var9 = -0.006503331
        else:
            if input[15] < 3502.0:
                var9 = 0.039675802
            else:
                var9 = 0.062620305
    if input[15] < 629.0:
        if input[15] < -1556.0:
            if input[15] < -3798.0:
                var10 = -0.06251667
            else:
                var10 = -0.038875528
        else:
            if input[16] < -551.0:
                var10 = -0.021817068
            else:
                var10 = 0.00068317115
    else:
        if input[15] < 1989.0:
            if input[16] < 440.0:
                var10 = 0.008637528
            else:
                var10 = 0.029707337
        else:
            if input[7] < 1.0:
                var10 = 0.041131403
            else:
                var10 = 0.058197696
    if input[15] < -303.0:
        if input[15] < -1933.0:
            if input[15] < -3798.0:
                var11 = -0.060786605
            else:
                var11 = -0.040709067
        else:
            if input[7] < 1.0:
                var11 = -0.025707295
            else:
                var11 = -0.00393348
    else:
        if input[15] < 1564.0:
            if input[26] < 1.0:
                var11 = 0.01868046
            else:
                var11 = -0.0042534685
        else:
            if input[7] < 1.0:
                var11 = 0.034709185
            else:
                var11 = 0.053945668
    if input[15] < 629.0:
        if input[15] < -802.0:
            if input[16] < -1748.0:
                var12 = -0.046988394
            else:
                var12 = -0.024349177
        else:
            if input[26] < 1.0:
                var12 = 0.007924678
            else:
                var12 = -0.01594309
    else:
        if input[15] < 1989.0:
            if input[16] < 440.0:
                var12 = 0.0075390115
            else:
                var12 = 0.027450552
        else:
            if input[15] < 3703.0:
                var12 = 0.040829845
            else:
                var12 = 0.059050184
    if input[15] < 233.0:
        if input[15] < -1933.0:
            if input[15] < -3798.0:
                var13 = -0.057975154
            else:
                var13 = -0.037716705
        else:
            if input[7] < 1.0:
                var13 = -0.019052971
            else:
                var13 = 0.00081540516
    else:
        if input[16] < 1337.0:
            if input[7] < 1.0:
                var13 = 0.0044872803
            else:
                var13 = 0.028518362
        else:
            if input[26] < 1.0:
                var13 = 0.048878968
            else:
                var13 = 0.02744556
    if input[16] < 385.0:
        if input[15] < -953.0:
            if input[15] < -2794.0:
                var14 = -0.048363324
            else:
                var14 = -0.026391981
        else:
            if input[7] < 1.0:
                var14 = -0.012237936
            else:
                var14 = 0.010589906
    else:
        if input[15] < 2015.0:
            if input[16] < 1454.0:
                var14 = 0.014103295
            else:
                var14 = 0.031804424
        else:
            if input[15] < 3502.0:
                var14 = 0.037911482
            else:
                var14 = 0.0554243
    if input[15] < 629.0:
        if input[15] < -1755.0:
            if input[15] < -3798.0:
                var15 = -0.055323977
            else:
                var15 = -0.03364802
        else:
            if input[7] < 1.0:
                var15 = -0.015214937
            else:
                var15 = 0.005099918
    else:
        if input[15] < 1989.0:
            if input[16] < 440.0:
                var15 = 0.0065902853
            else:
                var15 = 0.024182776
        else:
            if input[7] < 1.0:
                var15 = 0.033824537
            else:
                var15 = 0.050690413
    if input[15] < -303.0:
        if input[16] < -1748.0:
            if input[7] < 1.0:
                var16 = -0.045885947
            else:
                var16 = -0.024578935
        else:
            if input[7] < 1.0:
                var16 = -0.021162389
            else:
                var16 = -0.0047835717
    else:
        if input[15] < 1774.0:
            if input[26] < 1.0:
                var16 = 0.016335404
            else:
                var16 = -0.0030749885
        else:
            if input[26] < 1.0:
                var16 = 0.0442467
            else:
                var16 = 0.023444282
    if input[16] < -254.0:
        if input[15] < -1755.0:
            if input[15] < -3798.0:
                var17 = -0.053021837
            else:
                var17 = -0.032525696
        else:
            if input[26] < 1.0:
                var17 = -0.0055645937
            else:
                var17 = -0.02292396
    else:
        if input[15] < 1344.0:
            if input[7] < 1.0:
                var17 = -0.0013243993
            else:
                var17 = 0.020595437
        else:
            if input[16] < 2469.0:
                var17 = 0.028285408
            else:
                var17 = 0.048962478
    if input[16] < 385.0:
        if input[15] < -1817.0:
            if input[15] < -3798.0:
                var18 = -0.05179232
            else:
                var18 = -0.030781714
        else:
            if input[7] < 1.0:
                var18 = -0.015281252
            else:
                var18 = 0.005543912
    else:
        if input[15] < 2015.0:
            if input[16] < 1454.0:
                var18 = 0.012015526
            else:
                var18 = 0.028283373
        else:
            if input[15] < 3502.0:
                var18 = 0.03238925
            else:
                var18 = 0.05066508
    if input[15] < 629.0:
        if input[16] < -874.0:
            if input[10] < 14526.0:
                var19 = -0.048913572
            else:
                var19 = -0.02391292
        else:
            if input[15] < -802.0:
                var19 = -0.017357355
            else:
                var19 = 0.0037066643
    else:
        if input[15] < 2015.0:
            if input[14] < 59.0:
                var19 = 0.011483312
            else:
                var19 = 0.030012747
        else:
            if input[7] < 1.0:
                var19 = 0.028520672
            else:
                var19 = 0.04642934
    if input[16] < 385.0:
        if input[15] < -1817.0:
            if input[15] < -3798.0:
                var20 = -0.049764067
            else:
                var20 = -0.028538963
        else:
            if input[7] < 1.0:
                var20 = -0.014187343
            else:
                var20 = 0.005520145
    else:
        if input[15] < 2015.0:
            if input[16] < 1454.0:
                var20 = 0.010993142
            else:
                var20 = 0.026433349
        else:
            if input[15] < 3502.0:
                var20 = 0.029868145
            else:
                var20 = 0.048439384
    if input[15] < 629.0:
        if input[16] < -874.0:
            if input[10] < 14526.0:
                var21 = -0.046639066
            else:
                var21 = -0.02209274
        else:
            if input[15] < -802.0:
                var21 = -0.016092217
            else:
                var21 = 0.0034934531
    else:
        if input[16] < 2469.0:
            if input[7] < 1.0:
                var21 = 0.01189896
            else:
                var21 = 0.027555013
        else:
            if input[10] < 16812.0:
                var21 = -0.0016466773
            else:
                var21 = 0.047156263
    if input[16] < -254.0:
        if input[15] < -1755.0:
            if input[26] < 1.0:
                var22 = -0.021310005
            else:
                var22 = -0.039675113
        else:
            if input[26] < 1.0:
                var22 = -0.0039108745
            else:
                var22 = -0.019382155
    else:
        if input[15] < 1774.0:
            if input[7] < 1.0:
                var22 = 0.0011965059
            else:
                var22 = 0.017697552
        else:
            if input[15] < 3822.0:
                var22 = 0.027014766
            else:
                var22 = 0.047965933
    if input[15] < 629.0:
        if input[16] < -1748.0:
            if input[10] < 17527.0:
                var23 = -0.03430265
            else:
                var23 = 0.043898158
        else:
            if input[26] < 1.0:
                var23 = 0.00025749605
            else:
                var23 = -0.015604927
    else:
        if input[16] < 2469.0:
            if input[7] < 1.0:
                var23 = 0.010863992
            else:
                var23 = 0.025608618
        else:
            if input[10] < 16812.0:
                var23 = -0.002470262
            else:
                var23 = 0.044988003
    if input[16] < 385.0:
        if input[15] < -1933.0:
            if input[15] < -3798.0:
                var24 = -0.046441417
            else:
                var24 = -0.02507048
        else:
            if input[7] < 1.0:
                var24 = -0.012562505
            else:
                var24 = 0.0047438694
    else:
        if input[16] < 2001.0:
            if input[29] < 15117.0:
                var24 = 0.02587614
            else:
                var24 = 0.010640441
        else:
            if input[7] < 1.0:
                var24 = 0.023540499
            else:
                var24 = 0.048342217
    if input[15] < -484.0:
        if input[16] < -2244.0:
            if input[5] < 4.0:
                var25 = -0.045653168
            else:
                var25 = -0.026659284
        else:
            if input[10] < 14526.0:
                var25 = -0.03510231
            else:
                var25 = -0.011734656
    else:
        if input[15] < 1989.0:
            if input[16] < -530.0:
                var25 = -0.01158917
            else:
                var25 = 0.010144609
        else:
            if input[15] < 4957.0:
                var25 = 0.027811235
            else:
                var25 = 0.055959072
    if input[15] < -484.0:
        if input[15] < -2794.0:
            if input[10] < 15304.0:
                var26 = -0.0413426
            else:
                var26 = -0.016448027
        else:
            if input[33] < 55.0:
                var26 = -0.0082034385
            else:
                var26 = -0.021926029
    else:
        if input[16] < 1429.0:
            if input[16] < -530.0:
                var26 = -0.0102642225
            else:
                var26 = 0.009093707
        else:
            if input[15] < 3595.0:
                var26 = 0.023243645
            else:
                var26 = 0.044383936
    if input[15] < 629.0:
        if input[16] < -1748.0:
            if input[10] < 17527.0:
                var27 = -0.030443776
            else:
                var27 = 0.044092797
        else:
            if input[26] < 1.0:
                var27 = 0.0007634588
            else:
                var27 = -0.013834463
    else:
        if input[16] < 2469.0:
            if input[7] < 1.0:
                var27 = 0.008631452
            else:
                var27 = 0.022695286
        else:
            if input[10] < 16812.0:
                var27 = -0.00587149
            else:
                var27 = 0.041179698
    if input[16] < 385.0:
        if input[15] < -1933.0:
            if input[15] < -3798.0:
                var28 = -0.043195058
            else:
                var28 = -0.021591675
        else:
            if input[7] < 1.0:
                var28 = -0.011071064
            else:
                var28 = 0.0048002223
    else:
        if input[16] < 2469.0:
            if input[29] < 15117.0:
                var28 = 0.025185725
            else:
                var28 = 0.00947647
        else:
            if input[10] < 16135.0:
                var28 = -0.041876357
            else:
                var28 = 0.038695943
    if input[15] < -484.0:
        if input[10] < 14813.0:
            if input[29] < 17898.0:
                var29 = -0.02311018
            else:
                var29 = -0.05260554
        else:
            if input[31] < 19144.0:
                var29 = -0.0070905387
            else:
                var29 = -0.022718703
    else:
        if input[15] < 1989.0:
            if input[16] < -530.0:
                var29 = -0.010192125
            else:
                var29 = 0.008561979
        else:
            if input[7] < 1.0:
                var29 = 0.018751541
            else:
                var29 = 0.036847234
    if input[16] < 385.0:
        if input[16] < -1748.0:
            if input[10] < 17527.0:
                var30 = -0.027646247
            else:
                var30 = 0.043403234
        else:
            if input[7] < 1.0:
                var30 = -0.010410484
            else:
                var30 = 0.004247072
    else:
        if input[15] < 3502.0:
            if input[7] < 1.0:
                var30 = 0.0076266327
            else:
                var30 = 0.020979239
        else:
            if input[26] < 1.0:
                var30 = 0.045245633
            else:
                var30 = 0.015530621
    if input[15] < 629.0:
        if input[15] < -1933.0:
            if input[10] < 14591.0:
                var31 = -0.03754873
            else:
                var31 = -0.017984336
        else:
            if input[26] < 1.0:
                var31 = 0.0015137623
            else:
                var31 = -0.012459272
    else:
        if input[31] < 17470.0:
            if input[25] < 1.0:
                var31 = 0.030256202
            else:
                var31 = 0.012965719
        else:
            if input[14] < 60.0:
                var31 = 0.002147641
            else:
                var31 = 0.023926755
    if input[15] < -643.0:
        if input[15] < -3798.0:
            if input[10] < 15770.0:
                var32 = -0.04472511
            else:
                var32 = 0.019388497
        else:
            if input[26] < 1.0:
                var32 = -0.005704258
            else:
                var32 = -0.020731976
    else:
        if input[16] < 1361.0:
            if input[14] < 57.0:
                var32 = -0.00027469473
            else:
                var32 = 0.0164082
        else:
            if input[15] < 3595.0:
                var32 = 0.01833671
            else:
                var32 = 0.039825466
    if input[16] < -319.0:
        if input[10] < 14526.0:
            if input[13] < 229.0:
                var33 = -0.038166273
            else:
                var33 = -0.002966813
        else:
            if input[26] < 1.0:
                var33 = -0.0028485307
            else:
                var33 = -0.018579828
    else:
        if input[16] < 1429.0:
            if input[7] < 1.0:
                var33 = -0.0008474944
            else:
                var33 = 0.01341261
        else:
            if input[15] < 3595.0:
                var33 = 0.01807371
            else:
                var33 = 0.038680892
    if input[15] < 629.0:
        if input[16] < -1748.0:
            if input[10] < 17527.0:
                var34 = -0.024814997
            else:
                var34 = 0.04295937
        else:
            if input[12] < 18842.0:
                var34 = -0.0062408894
            else:
                var34 = 0.015628539
    else:
        if input[16] < 2469.0:
            if input[29] < 15413.0:
                var34 = 0.018187134
            else:
                var34 = 0.0055921613
        else:
            if input[10] < 16812.0:
                var34 = -0.010952095
            else:
                var34 = 0.035521336
    if input[15] < -683.0:
        if input[15] < -3798.0:
            if input[10] < 15770.0:
                var35 = -0.04292456
            else:
                var35 = 0.020112334
        else:
            if input[26] < 1.0:
                var35 = -0.004674421
            else:
                var35 = -0.019006599
    else:
        if input[15] < 1989.0:
            if input[16] < -530.0:
                var35 = -0.009323512
            else:
                var35 = 0.0067242794
        else:
            if input[15] < 4957.0:
                var35 = 0.019878462
            else:
                var35 = 0.050374497
    if input[15] < -683.0:
        if input[15] < -3798.0:
            if input[10] < 15770.0:
                var36 = -0.0420951
            else:
                var36 = 0.019094774
        else:
            if input[26] < 1.0:
                var36 = -0.004448601
            else:
                var36 = -0.018216074
    else:
        if input[15] < 1989.0:
            if input[14] < 57.0:
                var36 = -0.0002580451
            else:
                var36 = 0.014057032
        else:
            if input[7] < 1.0:
                var36 = 0.013583781
            else:
                var36 = 0.031811394
    if input[15] < 629.0:
        if input[15] < -2794.0:
            if input[10] < 15304.0:
                var37 = -0.032993987
            else:
                var37 = -0.008355464
        else:
            if input[26] < 1.0:
                var37 = 0.0007803035
            else:
                var37 = -0.011716262
    else:
        if input[31] < 17470.0:
            if input[25] < 1.0:
                var37 = 0.026192784
            else:
                var37 = 0.0093560545
        else:
            if input[33] < 61.0:
                var37 = 0.0005948533
            else:
                var37 = 0.023560492
    if input[16] < -551.0:
        if input[15] < -3290.0:
            if input[12] < 16723.0:
                var38 = -0.038166855
            else:
                var38 = -0.014310363
        else:
            if input[26] < 1.0:
                var38 = -0.0025374468
            else:
                var38 = -0.017411215
    else:
        if input[16] < 1429.0:
            if input[15] < -802.0:
                var38 = -0.011303126
            else:
                var38 = 0.0055054566
        else:
            if input[15] < 4957.0:
                var38 = 0.016930504
            else:
                var38 = 0.0488053
    if input[16] < -874.0:
        if input[10] < 14526.0:
            if input[33] < 34.0:
                var39 = 0.039710514
            else:
                var39 = -0.03432552
        else:
            if input[31] < 19144.0:
                var39 = -0.004335562
            else:
                var39 = -0.02043937
    else:
        if input[15] < 1344.0:
            if input[7] < 1.0:
                var39 = -0.0033860076
            else:
                var39 = 0.008388653
        else:
            if input[14] < 62.0:
                var39 = 0.012724193
            else:
                var39 = 0.035140775
    if input[16] < 385.0:
        if input[10] < 14526.0:
            if input[16] < -167.0:
                var40 = -0.030746717
            else:
                var40 = 0.018231241
        else:
            if input[31] < 19144.0:
                var40 = -0.0017532408
            else:
                var40 = -0.016825829
    else:
        if input[15] < 3502.0:
            if input[33] < 61.0:
                var40 = 0.0066238167
            else:
                var40 = 0.027787728
        else:
            if input[24] < 6.0:
                var40 = 0.039497033
            else:
                var40 = 0.006021993
    if input[16] < -874.0:
        if input[10] < 14526.0:
            if input[33] < 34.0:
                var41 = 0.03935464
            else:
                var41 = -0.032483995
        else:
            if input[31] < 19144.0:
                var41 = -0.0040409532
            else:
                var41 = -0.018931475
    else:
        if input[15] < 1989.0:
            if input[7] < 1.0:
                var41 = -0.0019172824
            else:
                var41 = 0.008751559
        else:
            if input[15] < 4957.0:
                var41 = 0.015857626
            else:
                var41 = 0.047725197
    if input[15] < -802.0:
        if input[15] < -3991.0:
            if input[10] < 15388.0:
                var42 = -0.043230753
            else:
                var42 = 0.009369467
        else:
            if input[32] < 239.0:
                var42 = -0.013407776
            else:
                var42 = 0.002283241
    else:
        if input[26] < 1.0:
            if input[16] < 2107.0:
                var42 = 0.0072576366
            else:
                var42 = 0.03133948
        else:
            if input[31] < 19058.0:
                var42 = -0.00053607294
            else:
                var42 = -0.035859045
    if input[16] < 385.0:
        if input[15] < -3179.0:
            if input[32] < 214.0:
                var43 = -0.04850199
            else:
                var43 = -0.020996721
        else:
            if input[7] < 1.0:
                var43 = -0.008416167
            else:
                var43 = 0.003757596
    else:
        if input[15] < 3502.0:
            if input[33] < 61.0:
                var43 = 0.005688888
            else:
                var43 = 0.026382495
        else:
            if input[24] < 6.0:
                var43 = 0.037640963
            else:
                var43 = 0.0038364276
    if input[15] < 629.0:
        if input[10] < 14813.0:
            if input[29] < 17898.0:
                var44 = -0.012456338
            else:
                var44 = -0.04552304
        else:
            if input[12] < 18823.0:
                var44 = -0.004906248
            else:
                var44 = 0.014199793
    else:
        if input[15] < 4957.0:
            if input[25] < 1.0:
                var44 = 0.014027759
            else:
                var44 = 0.0010939924
        else:
            if input[13] < 204.0:
                var44 = 0.0052751526
            else:
                var44 = 0.04838086
    var45 = var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44
    if input[16] < -874.0:
        if input[10] < 14526.0:
            if input[20] < 6.0:
                var46 = -0.03152256
            else:
                var46 = 0.013940676
        else:
            if input[31] < 19144.0:
                var46 = -0.0029602228
            else:
                var46 = -0.01712223
    else:
        if input[16] < 1429.0:
            if input[25] < 2.0:
                var46 = 0.002759149
            else:
                var46 = -0.017499309
        else:
            if input[12] < 17874.0:
                var46 = -0.01754711
            else:
                var46 = 0.01792247
    if input[15] < 1344.0:
        if input[31] < 17790.0:
            if input[10] < 16907.0:
                var47 = 0.0011696634
            else:
                var47 = 0.017870925
        else:
            if input[7] < 1.0:
                var47 = -0.012319609
            else:
                var47 = 0.0013229708
    else:
        if input[14] < 62.0:
            if input[15] < 4957.0:
                var47 = 0.0074129263
            else:
                var47 = 0.046473294
        else:
            if input[19] < 52.0:
                var47 = 0.035292547
            else:
                var47 = -0.010207584
    if input[16] < -874.0:
        if input[10] < 14526.0:
            if input[32] < 188.0:
                var48 = 0.043890018
            else:
                var48 = -0.028914506
        else:
            if input[31] < 19144.0:
                var48 = -0.0025131544
            else:
                var48 = -0.01606261
    else:
        if input[16] < 2469.0:
            if input[7] < 1.0:
                var48 = -0.0011532214
            else:
                var48 = 0.009209714
        else:
            if input[10] < 16812.0:
                var48 = -0.01886464
            else:
                var48 = 0.027754247
    if input[15] < 1344.0:
        if input[31] < 17790.0:
            if input[31] < 16544.0:
                var49 = -0.014703338
            else:
                var49 = 0.006988072
        else:
            if input[10] < 14526.0:
                var49 = -0.02737604
            else:
                var49 = -0.0054665445
    else:
        if input[14] < 62.0:
            if input[15] < 4957.0:
                var49 = 0.0067689205
            else:
                var49 = 0.04555598
        else:
            if input[19] < 52.0:
                var49 = 0.03397244
            else:
                var49 = -0.01015007
    if input[15] < -802.0:
        if input[15] < -3991.0:
            if input[10] < 15770.0:
                var50 = -0.03770271
            else:
                var50 = 0.030014707
        else:
            if input[32] < 239.0:
                var50 = -0.011196769
            else:
                var50 = 0.0046298495
    else:
        if input[26] < 1.0:
            if input[16] < 2107.0:
                var50 = 0.0058569973
            else:
                var50 = 0.027484296
        else:
            if input[13] < 234.0:
                var50 = 0.0022018133
            else:
                var50 = -0.015980022
    if input[15] < 1344.0:
        if input[11] < 6.8:
            if input[16] < -3783.0:
                var51 = -0.04481556
            else:
                var51 = -0.010440058
        else:
            if input[31] < 17326.0:
                var51 = 0.014424549
            else:
                var51 = -0.0028150463
    else:
        if input[14] < 62.0:
            if input[0] < 38.0:
                var51 = 0.010993919
            else:
                var51 = -0.015940482
        else:
            if input[19] < 52.0:
                var51 = 0.03271019
            else:
                var51 = -0.009978777
    if input[16] < -874.0:
        if input[15] < -3991.0:
            if input[10] < 15388.0:
                var52 = -0.039290074
            else:
                var52 = 0.013224791
        else:
            if input[32] < 238.0:
                var52 = -0.011129624
            else:
                var52 = 0.003239353
    else:
        if input[7] < 1.0:
            if input[31] < 17438.0:
                var52 = 0.0076294774
            else:
                var52 = -0.005241477
        else:
            if input[29] < 15761.0:
                var52 = 0.021685949
            else:
                var52 = 0.0011618247
    if input[26] < 1.0:
        if input[29] < 15761.0:
            if input[15] < 3502.0:
                var53 = 0.011559722
            else:
                var53 = 0.03690275
        else:
            if input[15] < -3900.0:
                var53 = -0.035841838
            else:
                var53 = 0.0007550916
    else:
        if input[31] < 19058.0:
            if input[3] < 4.0:
                var53 = -0.015872505
            else:
                var53 = 0.0005363121
        else:
            if input[32] < 221.0:
                var53 = -0.04596816
            else:
                var53 = -0.016787017
    if input[11] < 6.8:
        if input[10] < 17094.0:
            if input[29] < 17762.0:
                var54 = -0.008234142
            else:
                var54 = -0.027352974
        else:
            if input[32] < 198.0:
                var54 = -0.017689744
            else:
                var54 = 0.03103502
    else:
        if input[31] < 17470.0:
            if input[29] < 14070.0:
                var54 = 0.034389745
            else:
                var54 = 0.010119137
        else:
            if input[7] < 1.0:
                var54 = -0.005792359
            else:
                var54 = 0.0071182395
    if input[11] < 6.8:
        if input[16] < -3783.0:
            if input[4] < 14.0:
                var55 = -0.051928293
            else:
                var55 = 0.008519928
        else:
            if input[0] < 48.0:
                var55 = -0.006994462
            else:
                var55 = -0.038524795
    else:
        if input[31] < 17470.0:
            if input[25] < 1.0:
                var55 = 0.016914045
            else:
                var55 = 0.0035319354
        else:
            if input[7] < 1.0:
                var55 = -0.005508059
            else:
                var55 = 0.0067680976
    if input[26] < 1.0:
        if input[16] < 2107.0:
            if input[15] < -3900.0:
                var56 = -0.03433959
            else:
                var56 = 0.0028746233
        else:
            if input[6] < 1.0:
                var56 = 0.0049257674
            else:
                var56 = 0.0319244
    else:
        if input[31] < 19058.0:
            if input[3] < 4.0:
                var56 = -0.01468563
            else:
                var56 = 0.00078312895
        else:
            if input[32] < 221.0:
                var56 = -0.044317823
            else:
                var56 = -0.015346527
    if input[11] < 6.8:
        if input[16] < -3783.0:
            if input[4] < 14.0:
                var57 = -0.051344693
            else:
                var57 = 0.009218353
        else:
            if input[0] < 48.0:
                var57 = -0.006526479
            else:
                var57 = -0.03709995
    else:
        if input[31] < 17470.0:
            if input[15] < 4957.0:
                var57 = 0.009374557
            else:
                var57 = 0.041231077
        else:
            if input[7] < 1.0:
                var57 = -0.0050678053
            else:
                var57 = 0.006282332
    if input[15] < 1344.0:
        if input[12] < 18842.0:
            if input[31] < 17790.0:
                var58 = 0.0022240935
            else:
                var58 = -0.0073677786
        else:
            if input[15] < 1070.0:
                var58 = 0.016990189
            else:
                var58 = -0.014152214
    else:
        if input[14] < 62.0:
            if input[0] < 38.0:
                var58 = 0.008694204
            else:
                var58 = -0.017820438
        else:
            if input[31] < 17093.0:
                var58 = 0.009970462
            else:
                var58 = 0.03723229
    if input[26] < 1.0:
        if input[29] < 15761.0:
            if input[15] < 3703.0:
                var59 = 0.010036228
            else:
                var59 = 0.036202684
        else:
            if input[12] < 19534.0:
                var59 = -0.0017276517
            else:
                var59 = 0.02552316
    else:
        if input[31] < 19058.0:
            if input[19] < 89.0:
                var59 = -0.0012075207
            else:
                var59 = -0.044716112
        else:
            if input[32] < 221.0:
                var59 = -0.04289902
            else:
                var59 = -0.0141709065
    if input[11] < 6.8:
        if input[16] < -3783.0:
            if input[4] < 14.0:
                var60 = -0.050777476
            else:
                var60 = 0.009713672
        else:
            if input[0] < 50.0:
                var60 = -0.0060952357
            else:
                var60 = -0.037564185
    else:
        if input[31] < 17470.0:
            if input[29] < 14070.0:
                var60 = 0.031851567
            else:
                var60 = 0.007971558
        else:
            if input[7] < 1.0:
                var60 = -0.0045818347
            else:
                var60 = 0.005900702
    if input[11] < 6.8:
        if input[10] < 17094.0:
            if input[29] < 17762.0:
                var61 = -0.006346052
            else:
                var61 = -0.024439765
        else:
            if input[32] < 198.0:
                var61 = -0.016165322
            else:
                var61 = 0.030740036
    else:
        if input[31] < 17470.0:
            if input[15] < 4957.0:
                var61 = 0.008059278
            else:
                var61 = 0.03981728
        else:
            if input[7] < 1.0:
                var61 = -0.004356301
            else:
                var61 = 0.005610037
    if input[12] < 19125.0:
        if input[31] < 17326.0:
            if input[11] < 6.4:
                var62 = -0.035509206
            else:
                var62 = 0.006996609
        else:
            if input[13] < 198.0:
                var62 = 0.0049259746
            else:
                var62 = -0.006007252
    else:
        if input[14] < 61.0:
            if input[0] < 41.0:
                var62 = 0.006670262
            else:
                var62 = -0.030973865
        else:
            if input[14] < 65.0:
                var62 = 0.04983736
            else:
                var62 = 0.014324494
    if input[26] < 1.0:
        if input[15] < 3822.0:
            if input[33] < 70.0:
                var63 = 0.0016377586
            else:
                var63 = 0.032006547
        else:
            if input[13] < 214.0:
                var63 = 0.0030201909
            else:
                var63 = 0.04075648
    else:
        if input[31] < 19179.0:
            if input[3] < 4.0:
                var63 = -0.014021617
            else:
                var63 = 0.00089149346
        else:
            if input[32] < 221.0:
                var63 = -0.045770843
            else:
                var63 = -0.014545691
    if input[11] < 6.8:
        if input[16] < -3783.0:
            if input[4] < 14.0:
                var64 = -0.050149288
            else:
                var64 = 0.010799167
        else:
            if input[0] < 48.0:
                var64 = -0.005187788
            else:
                var64 = -0.034070976
    else:
        if input[29] < 15396.0:
            if input[26] < 1.0:
                var64 = 0.015944254
            else:
                var64 = -0.0013471126
        else:
            if input[29] < 15442.0:
                var64 = -0.030108793
            else:
                var64 = 0.00021594005
    if input[10] < 14526.0:
        if input[33] < 55.0:
            if input[13] < 226.0:
                var65 = -0.014440193
            else:
                var65 = 0.03795646
        else:
            if input[33] < 64.0:
                var65 = -0.04447178
            else:
                var65 = -0.007980223
    else:
        if input[14] < 60.0:
            if input[29] < 14866.0:
                var65 = 0.014385112
            else:
                var65 = -0.0024971594
        else:
            if input[12] < 19026.0:
                var65 = 0.0027331542
            else:
                var65 = 0.024090406
    if input[7] < 1.0:
        if input[3] < 4.0:
            if input[29] < 17898.0:
                var66 = -0.011261468
            else:
                var66 = -0.037640173
        else:
            if input[31] < 19490.0:
                var66 = 0.0011710072
            else:
                var66 = -0.018962886
    else:
        if input[29] < 15761.0:
            if input[0] < 42.0:
                var66 = 0.019345766
            else:
                var66 = -0.01229433
        else:
            if input[29] < 15830.0:
                var66 = -0.041959412
            else:
                var66 = 0.0010131326
    if input[11] < 6.8:
        if input[16] < -3783.0:
            if input[4] < 14.0:
                var67 = -0.04952089
            else:
                var67 = 0.011551374
        else:
            if input[0] < 50.0:
                var67 = -0.004763715
            else:
                var67 = -0.034517743
    else:
        if input[15] < 4957.0:
            if input[14] < 60.0:
                var67 = -0.0005159848
            else:
                var67 = 0.0084814085
        else:
            if input[6] < 2.0:
                var67 = 0.045679603
            else:
                var67 = 0.0023088702
    if input[26] < 1.0:
        if input[15] < 3822.0:
            if input[33] < 70.0:
                var68 = 0.0013778199
            else:
                var68 = 0.030679142
        else:
            if input[13] < 214.0:
                var68 = 0.0014625643
            else:
                var68 = 0.039320547
    else:
        if input[31] < 19179.0:
            if input[16] < -2396.0:
                var68 = -0.03244334
            else:
                var68 = -0.00081612676
        else:
            if input[32] < 221.0:
                var68 = -0.044466656
            else:
                var68 = -0.012867826
    if input[10] < 14526.0:
        if input[33] < 55.0:
            if input[13] < 226.0:
                var69 = -0.013144232
            else:
                var69 = 0.03639422
        else:
            if input[25] < 2.0:
                var69 = -0.03882078
            else:
                var69 = 0.0068003335
    else:
        if input[15] < 4957.0:
            if input[14] < 60.0:
                var69 = -0.0012294668
            else:
                var69 = 0.007957129
        else:
            if input[6] < 2.0:
                var69 = 0.04495776
            else:
                var69 = 0.0010467175
    if input[7] < 1.0:
        if input[3] < 4.0:
            if input[14] < 36.0:
                var70 = 0.03257313
            else:
                var70 = -0.015493983
        else:
            if input[31] < 19559.0:
                var70 = 0.0010540708
            else:
                var70 = -0.018879946
    else:
        if input[29] < 15761.0:
            if input[0] < 42.0:
                var70 = 0.018234186
            else:
                var70 = -0.012058943
        else:
            if input[29] < 15830.0:
                var70 = -0.039974645
            else:
                var70 = 0.0008410282
    if input[10] < 13602.0:
        if input[33] < 68.0:
            if input[20] < 6.0:
                var71 = -0.05027595
            else:
                var71 = -0.0064163483
        else:
            var71 = -0.002485751
    else:
        if input[15] < 4957.0:
            if input[14] < 60.0:
                var71 = -0.0016858347
            else:
                var71 = 0.007183734
        else:
            if input[6] < 2.0:
                var71 = 0.044402894
            else:
                var71 = 0.00053974515
    if input[26] < 1.0:
        if input[16] < 2107.0:
            if input[33] < 69.0:
                var72 = 0.0004061062
            else:
                var72 = 0.02914472
        else:
            if input[6] < 1.0:
                var72 = -0.00046184458
            else:
                var72 = 0.026944553
    else:
        if input[31] < 19179.0:
            if input[29] < 17028.0:
                var72 = -0.00496439
            else:
                var72 = 0.0073330523
        else:
            if input[32] < 238.0:
                var72 = -0.0298645
            else:
                var72 = -0.0024073587
    if input[10] < 13602.0:
        if input[33] < 68.0:
            if input[20] < 6.0:
                var73 = -0.04974195
            else:
                var73 = -0.0062082154
        else:
            var73 = -0.00242976
    else:
        if input[29] < 14258.0:
            if input[13] < 258.0:
                var73 = 0.022900743
            else:
                var73 = -0.028072072
        else:
            if input[14] < 60.0:
                var73 = -0.0019873537
            else:
                var73 = 0.007027355
    if input[11] < 6.8:
        if input[10] < 17094.0:
            if input[29] < 17762.0:
                var74 = -0.004494194
            else:
                var74 = -0.021497292
        else:
            if input[30] < 6.6:
                var74 = -0.031971645
            else:
                var74 = 0.024015406
    else:
        if input[15] < 4957.0:
            if input[13] < 196.0:
                var74 = 0.0111953905
            else:
                var74 = 0.000093100716
        else:
            if input[6] < 2.0:
                var74 = 0.043704078
            else:
                var74 = -0.00053996424
    if input[10] < 13602.0:
        if input[28] < 1.0:
            if input[14] < 33.0:
                var75 = -0.0032453828
            else:
                var75 = -0.04960343
        else:
            var75 = -0.0019618329
    else:
        if input[15] < 4957.0:
            if input[6] < 2.0:
                var75 = -0.0008889596
            else:
                var75 = 0.012108253
        else:
            if input[6] < 2.0:
                var75 = 0.04320648
            else:
                var75 = -0.00052224484
    if input[12] < 19125.0:
        if input[31] < 17326.0:
            if input[11] < 6.4:
                var76 = -0.03274921
            else:
                var76 = 0.006023249
        else:
            if input[13] < 198.0:
                var76 = 0.0060902857
            else:
                var76 = -0.005267217
    else:
        if input[14] < 61.0:
            if input[33] < 38.0:
                var76 = -0.038395386
            else:
                var76 = 0.0046828105
        else:
            if input[14] < 65.0:
                var76 = 0.04685707
            else:
                var76 = 0.010298286
    if input[10] < 13602.0:
        if input[28] < 1.0:
            if input[14] < 33.0:
                var77 = -0.0030944834
            else:
                var77 = -0.049107045
        else:
            var77 = -0.0019928825
    else:
        if input[26] < 1.0:
            if input[15] < 3822.0:
                var77 = 0.0020488203
            else:
                var77 = 0.029399296
        else:
            if input[31] < 19058.0:
                var77 = -0.00087121
            else:
                var77 = -0.016312346
    if input[10] < 13602.0:
        if input[28] < 1.0:
            if input[14] < 33.0:
                var78 = -0.003020202
            else:
                var78 = -0.04861489
        else:
            var78 = -0.0019443271
    else:
        if input[29] < 14258.0:
            if input[4] < 4.0:
                var78 = 0.021502998
            else:
                var78 = -0.027351214
        else:
            if input[14] < 60.0:
                var78 = -0.0018297384
            else:
                var78 = 0.0064634155
    if input[10] < 14526.0:
        if input[33] < 55.0:
            if input[0] < 19.0:
                var79 = -0.0148559585
            else:
                var79 = 0.023416499
        else:
            if input[25] < 2.0:
                var79 = -0.03713306
            else:
                var79 = 0.009396915
    else:
        if input[32] < 266.0:
            if input[15] < 4957.0:
                var79 = 0.00016531946
            else:
                var79 = 0.035047863
        else:
            if input[32] < 269.0:
                var79 = 0.0853906
            else:
                var79 = -0.0013923092
    if input[7] < 1.0:
        if input[3] < 4.0:
            if input[14] < 36.0:
                var80 = 0.033902615
            else:
                var80 = -0.014025207
        else:
            if input[0] < 110.0:
                var80 = -0.00037215947
            else:
                var80 = 0.045551267
    else:
        if input[12] < 19496.0:
            if input[29] < 15761.0:
                var80 = 0.0118037565
            else:
                var80 = -0.002498358
        else:
            if input[20] < 5.0:
                var80 = 0.03544801
            else:
                var80 = -0.008439732
    if input[15] < -4882.0:
        if input[5] < 5.0:
            var81 = -0.047901995
        else:
            if input[14] < 44.0:
                var81 = -0.031297397
            else:
                var81 = 0.06305957
    else:
        if input[26] < 1.0:
            if input[15] < 3822.0:
                var81 = 0.0019660904
            else:
                var81 = 0.027925087
        else:
            if input[31] < 19179.0:
                var81 = -0.0010515656
            else:
                var81 = -0.01705291
    if input[10] < 13602.0:
        if input[33] < 65.0:
            if input[1] < 4.0:
                var82 = -0.04666892
            else:
                var82 = -0.011240094
        else:
            var82 = -0.0018058487
    else:
        if input[15] < 4957.0:
            if input[6] < 2.0:
                var82 = -0.00078975
            else:
                var82 = 0.010944243
        else:
            if input[6] < 2.0:
                var82 = 0.04164539
            else:
                var82 = -0.004980516
    if input[11] < 6.8:
        if input[0] < 50.0:
            if input[31] < 18195.0:
                var83 = 0.0016172737
            else:
                var83 = -0.012427268
        else:
            if input[13] < 233.0:
                var83 = -0.039969366
            else:
                var83 = 0.026035711
    else:
        if input[19] < 33.0:
            if input[19] < 32.0:
                var83 = 0.002665829
            else:
                var83 = 0.060426444
        else:
            if input[25] < 2.0:
                var83 = -0.0016849155
            else:
                var83 = -0.05255406
    if input[10] < 13602.0:
        if input[32] < 254.0:
            if input[0] < 19.0:
                var84 = -0.046861503
            else:
                var84 = -0.009853459
        else:
            var84 = -0.0027240103
    else:
        if input[29] < 14258.0:
            if input[13] < 258.0:
                var84 = 0.020128323
            else:
                var84 = -0.030406857
        else:
            if input[14] < 60.0:
                var84 = -0.0017071592
            else:
                var84 = 0.006096931
    if input[15] < -4882.0:
        if input[5] < 5.0:
            var85 = -0.047344957
        else:
            if input[14] < 44.0:
                var85 = -0.030686611
            else:
                var85 = 0.060260948
    else:
        if input[15] < 4957.0:
            if input[6] < 2.0:
                var85 = -0.00071494374
            else:
                var85 = 0.010388918
        else:
            if input[6] < 2.0:
                var85 = 0.0410316
            else:
                var85 = -0.005049623
    if input[16] < -3960.0:
        if input[4] < 14.0:
            var86 = -0.047455575
        else:
            var86 = 0.017846191
    else:
        if input[26] < 1.0:
            if input[33] < 72.0:
                var86 = 0.0018461278
            else:
                var86 = 0.032116916
        else:
            if input[31] < 19179.0:
                var86 = -0.0009844516
            else:
                var86 = -0.015896335
    if input[10] < 13602.0:
        if input[29] < 17506.0:
            var87 = -0.046389874
        else:
            if input[13] < 195.0:
                var87 = -0.033797026
            else:
                var87 = 0.0236755
    else:
        if input[15] < 4957.0:
            if input[0] < 49.0:
                var87 = 0.0006712706
            else:
                var87 = -0.010737934
        else:
            if input[6] < 2.0:
                var87 = 0.040512763
            else:
                var87 = -0.004940972
    if input[12] < 19125.0:
        if input[31] < 17326.0:
            if input[31] < 16544.0:
                var88 = -0.004566116
            else:
                var88 = 0.008432754
        else:
            if input[13] < 196.0:
                var88 = 0.0073834024
            else:
                var88 = -0.0046417317
    else:
        if input[14] < 61.0:
            if input[33] < 38.0:
                var88 = -0.03829225
            else:
                var88 = 0.003465427
        else:
            if input[14] < 65.0:
                var88 = 0.04507668
            else:
                var88 = 0.008404761
    if input[15] < -4882.0:
        if input[5] < 5.0:
            var89 = -0.046871927
        else:
            if input[14] < 45.0:
                var89 = -0.032992598
            else:
                var89 = 0.070329405
    else:
        if input[29] < 20445.0:
            if input[32] < 261.0:
                var89 = -0.00023002776
            else:
                var89 = 0.022025546
        else:
            if input[19] < 17.0:
                var89 = -0.011878165
            else:
                var89 = 0.08173921
    if input[11] < 6.8:
        if input[12] < 17788.0:
            if input[0] < 48.0:
                var90 = -0.004735392
            else:
                var90 = -0.034803655
        else:
            if input[33] < 49.0:
                var90 = 0.06331887
            else:
                var90 = -0.0019274441
    else:
        if input[19] < 33.0:
            if input[19] < 32.0:
                var90 = 0.0024743765
            else:
                var90 = 0.058656435
        else:
            if input[25] < 2.0:
                var90 = -0.0016766706
            else:
                var90 = -0.05043149
    if input[16] < -3960.0:
        if input[4] < 14.0:
            var91 = -0.046908874
        else:
            var91 = 0.0178432
    else:
        if input[12] < 20574.0:
            if input[32] < 261.0:
                var91 = -0.00030779693
            else:
                var91 = 0.021313949
        else:
            if input[15] < 1989.0:
                var91 = -0.014442945
            else:
                var91 = 0.042262062
    if input[29] < 14258.0:
        if input[10] < 15612.0:
            if input[25] < 1.0:
                var92 = 0.05970148
            else:
                var92 = 0.0011788056
        else:
            if input[10] < 16135.0:
                var92 = -0.054884207
            else:
                var92 = 0.018580839
    else:
        if input[14] < 60.0:
            if input[32] < 260.0:
                var92 = -0.0022202304
            else:
                var92 = 0.03190422
        else:
            if input[12] < 18920.0:
                var92 = -0.00027567704
            else:
                var92 = 0.018360786
    if input[10] < 13602.0:
        if input[15] < -4331.0:
            if input[24] < 9.0:
                var93 = 0.023627764
            else:
                var93 = -0.032396045
        else:
            var93 = -0.045782212
    else:
        if input[15] < 4957.0:
            if input[16] < 3777.0:
                var93 = 0.00017525474
            else:
                var93 = -0.0366249
        else:
            if input[6] < 2.0:
                var93 = 0.039779197
            else:
                var93 = -0.0056750583
    if input[15] < -4882.0:
        if input[5] < 7.0:
            if input[32] < 257.0:
                var94 = -0.04670062
            else:
                var94 = -0.0031144964
        else:
            var94 = 0.030344864
    else:
        if input[29] < 20445.0:
            if input[31] < 19747.0:
                var94 = 0.00059971487
            else:
                var94 = -0.013361302
        else:
            if input[19] < 17.0:
                var94 = -0.011658583
            else:
                var94 = 0.07696392
    if input[7] < 1.0:
        if input[3] < 4.0:
            if input[14] < 36.0:
                var95 = 0.037063748
            else:
                var95 = -0.012568913
        else:
            if input[0] < 110.0:
                var95 = -0.00023883647
            else:
                var95 = 0.045453843
    else:
        if input[12] < 19496.0:
            if input[10] < 15273.0:
                var95 = 0.016382946
            else:
                var95 = -0.0012025915
        else:
            if input[32] < 198.0:
                var95 = -0.00089558744
            else:
                var95 = 0.03636548
    if input[16] < -3960.0:
        if input[4] < 14.0:
            var96 = -0.046375345
        else:
            var96 = 0.017792774
    else:
        if input[12] < 20574.0:
            if input[0] < 49.0:
                var96 = 0.0006611484
            else:
                var96 = -0.010013642
        else:
            if input[15] < 1989.0:
                var96 = -0.014420581
            else:
                var96 = 0.04142224
    if input[10] < 13602.0:
        if input[29] < 17506.0:
            var97 = -0.045259453
        else:
            if input[24] < 9.0:
                var97 = 0.022925062
            else:
                var97 = -0.030881573
    else:
        if input[4] < 17.0:
            if input[15] < -3991.0:
                var97 = -0.021571625
            else:
                var97 = 0.00044585095
        else:
            var97 = 0.0668576
    if input[29] < 14258.0:
        if input[4] < 4.0:
            if input[33] < 48.0:
                var98 = 0.036692042
            else:
                var98 = 0.0031089575
        else:
            if input[32] < 162.0:
                var98 = 0.02982378
            else:
                var98 = -0.07181235
    else:
        if input[14] < 60.0:
            if input[32] < 260.0:
                var98 = -0.0020999496
            else:
                var98 = 0.03041077
        else:
            if input[12] < 18920.0:
                var98 = -0.00019416075
            else:
                var98 = 0.017399127
    if input[15] < 4957.0:
        if input[16] < 3777.0:
            if input[6] < 2.0:
                var99 = -0.000673988
            else:
                var99 = 0.009504223
        else:
            if input[32] < 193.0:
                var99 = -0.07952462
            else:
                var99 = 0.017519535
    else:
        if input[6] < 2.0:
            if input[2] < 1.0:
                var99 = 0.002151283
            else:
                var99 = 0.04459929
        else:
            var99 = -0.006558028
    if input[10] < 13602.0:
        if input[15] < -4331.0:
            if input[24] < 9.0:
                var100 = 0.023693532
            else:
                var100 = -0.030835912
        else:
            var100 = -0.044710185
    else:
        if input[13] < 195.0:
            if input[14] < 42.0:
                var100 = -0.01220824
            else:
                var100 = 0.012049616
        else:
            if input[29] < 17811.0:
                var100 = 0.00044184932
            else:
                var100 = -0.010056447
    var101 = sigmoid(var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96 + var97 + var98 + var99 + var100)
    return [1.0 - var101, var101]
