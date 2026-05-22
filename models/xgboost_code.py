import math
def sigmoid(x):
    if x < 0.0:
        z = math.exp(x)
        return z / (1.0 + z)
    return 1.0 / (1.0 + math.exp(-x))
def score(input):
    if input[15] < 233.0:
        if input[37] < 0.4925226:
            if input[36] < 0.49157265:
                var0 = -0.0790959
            else:
                var0 = 0.08594081
        else:
            if input[36] < 0.506568:
                var0 = -0.15599127
            else:
                var0 = -0.029315615
    else:
        if input[36] < 0.49574596:
            if input[37] < 0.50315475:
                var0 = 0.06988556
            else:
                var0 = -0.10390387
        else:
            if input[37] < 0.5079031:
                var0 = 0.1664448
            else:
                var0 = 0.05552071
    if input[15] < -303.0:
        if input[37] < 0.4929352:
            if input[36] < 0.50623894:
                var1 = -0.045703273
            else:
                var1 = 0.11375453
        else:
            if input[36] < 0.5009344:
                var1 = -0.15569387
            else:
                var1 = -0.06590339
    else:
        if input[37] < 0.499669:
            if input[36] < 0.48749712:
                var1 = 0.019897139
            else:
                var1 = 0.14844617
        else:
            if input[36] < 0.501661:
                var1 = -0.07958388
            else:
                var1 = 0.08318778
    if input[15] < 629.0:
        if input[37] < 0.49862495:
            if input[36] < 0.49268258:
                var2 = -0.08418844
            else:
                var2 = 0.06314616
        else:
            if input[36] < 0.5103279:
                var2 = -0.13209815
            else:
                var2 = -0.016375205
    else:
        if input[37] < 0.5079031:
            if input[36] < 0.48978692:
                var2 = 0.036595482
            else:
                var2 = 0.13905047
        else:
            if input[36] < 0.49544358:
                var2 = -0.09334072
            else:
                var2 = 0.060968716
    if input[15] < -484.0:
        if input[37] < 0.49028215:
            if input[36] < 0.49268258:
                var3 = -0.07575027
            else:
                var3 = 0.0618609
        else:
            if input[36] < 0.50057554:
                var3 = -0.13683103
            else:
                var3 = -0.05610573
    else:
        if input[37] < 0.50547767:
            if input[36] < 0.49966013:
                var3 = 0.040199816
            else:
                var3 = 0.13500191
        else:
            if input[36] < 0.5024284:
                var3 = -0.086705975
            else:
                var3 = 0.05298177
    if input[16] < 385.0:
        if input[37] < 0.4942711:
            if input[36] < 0.5069425:
                var4 = -0.0183611
            else:
                var4 = 0.112094305
        else:
            if input[36] < 0.50623894:
                var4 = -0.11448492
            else:
                var4 = -0.0206231
    else:
        if input[37] < 0.50315475:
            if input[36] < 0.5043138:
                var4 = 0.080234855
            else:
                var4 = 0.14133506
        else:
            if input[36] < 0.5024284:
                var4 = -0.046903156
            else:
                var4 = 0.07708766
    if input[15] < -683.0:
        if input[37] < 0.4837096:
            if input[36] < 0.48135647:
                var5 = -0.106662825
            else:
                var5 = 0.072392024
        else:
            if input[36] < 0.5149982:
                var5 = -0.10609138
            else:
                var5 = 0.000990474
    else:
        if input[37] < 0.499669:
            if input[36] < 0.499963:
                var5 = 0.047857936
            else:
                var5 = 0.12571396
        else:
            if input[36] < 0.501661:
                var5 = -0.06101909
            else:
                var5 = 0.054604914
    if input[15] < 629.0:
        if input[37] < 0.5039959:
            if input[36] < 0.49903497:
                var6 = -0.05465905
            else:
                var6 = 0.051016003
        else:
            if input[36] < 0.5103279:
                var6 = -0.112490796
            else:
                var6 = -0.034817748
    else:
        if input[36] < 0.48978692:
            if input[16] < 1337.0:
                var6 = -0.07233142
            else:
                var6 = 0.05406809
        else:
            if input[37] < 0.51766545:
                var6 = 0.10316809
            else:
                var6 = -0.016580245
    if input[15] < -802.0:
        if input[37] < 0.4816635:
            if input[36] < 0.48444965:
                var7 = -0.06754045
            else:
                var7 = 0.0777903
        else:
            if input[36] < 0.49592552:
                var7 = -0.116727374
            else:
                var7 = -0.050737888
    else:
        if input[36] < 0.49666312:
            if input[15] < 1947.0:
                var7 = -0.051711973
            else:
                var7 = 0.07184136
        else:
            if input[37] < 0.51007336:
                var7 = 0.096222475
            else:
                var7 = 0.0020776335
    if input[15] < 1344.0:
        if input[37] < 0.4942711:
            if input[15] < -1782.0:
                var8 = -0.050708484
            else:
                var8 = 0.06487587
        else:
            if input[36] < 0.51278365:
                var8 = -0.081564136
            else:
                var8 = 0.016497042
    else:
        if input[37] < 0.5188288:
            if input[36] < 0.48470053:
                var8 = 0.018922849
            else:
                var8 = 0.103373125
        else:
            if input[36] < 0.51133436:
                var8 = -0.08983696
            else:
                var8 = 0.10934768
    if input[16] < -254.0:
        if input[37] < 0.49346763:
            if input[36] < 0.48676106:
                var9 = -0.088098906
            else:
                var9 = 0.036002126
        else:
            if input[36] < 0.49574596:
                var9 = -0.107510984
            else:
                var9 = -0.044957943
    else:
        if input[37] < 0.5079031:
            if input[36] < 0.49921107:
                var9 = 0.026546497
            else:
                var9 = 0.09780269
        else:
            if input[15] < 1989.0:
                var9 = -0.059549052
            else:
                var9 = 0.05612131
    if input[15] < -1437.0:
        if input[37] < 0.4837096:
            if input[36] < 0.4795307:
                var10 = -0.10960125
            else:
                var10 = 0.029671282
        else:
            if input[15] < -2794.0:
                var10 = -0.11293544
            else:
                var10 = -0.062420744
    else:
        if input[36] < 0.50623894:
            if input[37] < 0.49480662:
                var10 = 0.051359754
            else:
                var10 = -0.043194074
        else:
            if input[37] < 0.503665:
                var10 = 0.10392773
            else:
                var10 = 0.03904295
    if input[15] < 1344.0:
        if input[37] < 0.5039959:
            if input[36] < 0.48676106:
                var11 = -0.079221494
            else:
                var11 = 0.030427963
        else:
            if input[36] < 0.496443:
                var11 = -0.101785265
            else:
                var11 = -0.04054072
    else:
        if input[37] < 0.5188288:
            if input[36] < 0.48470053:
                var11 = 0.015665932
            else:
                var11 = 0.0910771
        else:
            if input[36] < 0.51133436:
                var11 = -0.080701895
            else:
                var11 = 0.09702265
    if input[15] < -802.0:
        if input[37] < 0.5119978:
            if input[36] < 0.5069425:
                var12 = -0.057989348
            else:
                var12 = 0.023279069
        else:
            if input[36] < 0.5219969:
                var12 = -0.11002469
            else:
                var12 = -0.029199142
    else:
        if input[36] < 0.50623894:
            if input[37] < 0.4898917:
                var12 = 0.063535385
            else:
                var12 = -0.023992607
        else:
            if input[37] < 0.4964771:
                var12 = 0.107705794
            else:
                var12 = 0.049927372
    if input[15] < 1564.0:
        if input[36] < 0.49287912:
            if input[37] < 0.48531362:
                var13 = 0.011358822
            else:
                var13 = -0.08303762
        else:
            if input[37] < 0.5151775:
                var13 = 0.023078648
            else:
                var13 = -0.07802149
    else:
        if input[37] < 0.524139:
            if input[36] < 0.48135647:
                var13 = 0.003499414
            else:
                var13 = 0.08578405
        else:
            if input[31] < 17063.0:
                var13 = 0.03314459
            else:
                var13 = -0.12085601
    if input[15] < -1610.0:
        if input[37] < 0.4843998:
            if input[5] < 3.0:
                var14 = -0.071191214
            else:
                var14 = 0.03617867
        else:
            if input[16] < -1865.0:
                var14 = -0.09702038
            else:
                var14 = -0.048057362
    else:
        if input[36] < 0.51055694:
            if input[37] < 0.4942711:
                var14 = 0.046933543
            else:
                var14 = -0.029794836
        else:
            if input[37] < 0.52289766:
                var14 = 0.08364162
            else:
                var14 = -0.023381185
    if input[16] < -874.0:
        if input[36] < 0.5151904:
            if input[37] < 0.47997773:
                var15 = 0.02361734
            else:
                var15 = -0.07247182
        else:
            if input[37] < 0.4971249:
                var15 = 0.0943374
            else:
                var15 = -0.029322714
    else:
        if input[37] < 0.5045668:
            if input[36] < 0.506568:
                var15 = 0.028952152
            else:
                var15 = 0.08870447
        else:
            if input[15] < 1989.0:
                var15 = -0.043736752
            else:
                var15 = 0.053509444
    if input[15] < 1989.0:
        if input[36] < 0.49287912:
            if input[37] < 0.48531362:
                var16 = 0.0068255365
            else:
                var16 = -0.07111557
        else:
            if input[37] < 0.51854736:
                var16 = 0.020215863
            else:
                var16 = -0.08182734
    else:
        if input[36] < 0.4879576:
            if input[37] < 0.5075082:
                var16 = 0.060999747
            else:
                var16 = -0.059322543
        else:
            if input[26] < 1.0:
                var16 = 0.09710956
            else:
                var16 = 0.043238457
    if input[15] < -1817.0:
        if input[15] < -3798.0:
            if input[10] < 15770.0:
                var17 = -0.11377964
            else:
                var17 = -0.0022314067
        else:
            if input[37] < 0.49346763:
                var17 = -0.0027035451
            else:
                var17 = -0.07097031
    else:
        if input[36] < 0.51055694:
            if input[37] < 0.5079031:
                var17 = 0.019809142
            else:
                var17 = -0.050090265
        else:
            if input[37] < 0.49469256:
                var17 = 0.097218595
            else:
                var17 = 0.044244744
    if input[16] < 914.0:
        if input[36] < 0.48676106:
            if input[15] < 1564.0:
                var18 = -0.081329964
            else:
                var18 = 0.017653568
        else:
            if input[37] < 0.5151775:
                var18 = 0.010674537
            else:
                var18 = -0.06972443
    else:
        if input[37] < 0.48968574:
            if input[19] < 87.0:
                var18 = 0.09104063
            else:
                var18 = -0.07448568
        else:
            if input[26] < 1.0:
                var18 = 0.05108912
            else:
                var18 = -0.017759966
    if input[15] < -1933.0:
        if input[15] < -3798.0:
            if input[10] < 15770.0:
                var19 = -0.108417384
            else:
                var19 = -0.00008347399
        else:
            if input[37] < 0.49346763:
                var19 = -0.0035622485
            else:
                var19 = -0.0668753
    else:
        if input[36] < 0.5143014:
            if input[37] < 0.48794916:
                var19 = 0.05265255
            else:
                var19 = -0.016287625
        else:
            if input[37] < 0.5151775:
                var19 = 0.08285367
            else:
                var19 = 0.004313514
    if input[15] < 1989.0:
        if input[36] < 0.48376793:
            if input[16] < 1337.0:
                var20 = -0.08180828
            else:
                var20 = 0.0021994088
        else:
            if input[37] < 0.51007336:
                var20 = 0.015565457
            else:
                var20 = -0.04742763
    else:
        if input[36] < 0.4879576:
            if input[37] < 0.5075082:
                var20 = 0.049088683
            else:
                var20 = -0.050864663
        else:
            if input[26] < 1.0:
                var20 = 0.088299826
            else:
                var20 = 0.035993975
    if input[16] < -874.0:
        if input[36] < 0.49287912:
            if input[37] < 0.4816635:
                var21 = -0.0061204084
            else:
                var21 = -0.08291944
        else:
            if input[16] < -2624.0:
                var21 = -0.07981672
            else:
                var21 = -0.003478458
    else:
        if input[37] < 0.49480662:
            if input[36] < 0.49903497:
                var21 = 0.023558848
            else:
                var21 = 0.07646595
        else:
            if input[36] < 0.5180251:
                var21 = -0.013316574
            else:
                var21 = 0.07019579
    if input[7] < 1.0:
        if input[36] < 0.51538676:
            if input[37] < 0.477046:
                var22 = 0.064660415
            else:
                var22 = -0.04046818
        else:
            if input[10] < 15958.0:
                var22 = -0.008044585
            else:
                var22 = 0.077619106
    else:
        if input[37] < 0.5079031:
            if input[15] < -1933.0:
                var22 = -0.024998011
            else:
                var22 = 0.06361581
        else:
            if input[16] < 2107.0:
                var22 = -0.022406844
            else:
                var22 = 0.08835693
    if input[15] < 2015.0:
        if input[36] < 0.48376793:
            if input[16] < 1337.0:
                var23 = -0.07419322
            else:
                var23 = 0.0028095571
        else:
            if input[37] < 0.51854736:
                var23 = 0.008749622
            else:
                var23 = -0.06713768
    else:
        if input[36] < 0.510964:
            if input[37] < 0.52489775:
                var23 = 0.050025623
            else:
                var23 = -0.06651702
        else:
            if input[32] < 242.0:
                var23 = 0.09978335
            else:
                var23 = 0.012052697
    if input[26] < 1.0:
        if input[36] < 0.48749712:
            if input[12] < 19920.0:
                var24 = -0.03402869
            else:
                var24 = 0.11163892
        else:
            if input[15] < -2105.0:
                var24 = -0.032778468
            else:
                var24 = 0.04333455
    else:
        if input[37] < 0.48097992:
            if input[36] < 0.5041161:
                var24 = 0.011384077
            else:
                var24 = 0.09420253
        else:
            if input[36] < 0.5172115:
                var24 = -0.048984177
            else:
                var24 = 0.029156515
    if input[15] < 1989.0:
        if input[36] < 0.5151904:
            if input[37] < 0.4843998:
                var25 = 0.032456066
            else:
                var25 = -0.03054735
        else:
            if input[37] < 0.4966571:
                var25 = 0.078373976
            else:
                var25 = 0.013619018
    else:
        if input[36] < 0.510964:
            if input[16] < 2469.0:
                var25 = 0.016895488
            else:
                var25 = 0.07156684
        else:
            if input[15] < 2015.0:
                var25 = 0.004699752
            else:
                var25 = 0.09473968
    if input[15] < -2141.0:
        if input[15] < -3798.0:
            if input[10] < 15649.0:
                var26 = -0.099195555
            else:
                var26 = 0.0046357163
        else:
            if input[37] < 0.49346763:
                var26 = 0.0020512294
            else:
                var26 = -0.057345252
    else:
        if input[37] < 0.5182543:
            if input[36] < 0.48399234:
                var26 = -0.034611948
            else:
                var26 = 0.027898615
        else:
            if input[15] < 3502.0:
                var26 = -0.05293827
            else:
                var26 = 0.0991128
    if input[7] < 1.0:
        if input[36] < 0.5172115:
            if input[37] < 0.477046:
                var27 = 0.054360665
            else:
                var27 = -0.03193141
        else:
            if input[37] < 0.51148725:
                var27 = 0.06538998
            else:
                var27 = -0.024761384
    else:
        if input[37] < 0.49638098:
            if input[29] < 16932.0:
                var27 = 0.07533982
            else:
                var27 = 0.019751301
        else:
            if input[16] < 2107.0:
                var27 = -0.0024607657
            else:
                var27 = 0.08276554
    if input[26] < 1.0:
        if input[36] < 0.4950648:
            if input[15] < -460.0:
                var28 = -0.047128595
            else:
                var28 = 0.009740667
        else:
            if input[12] < 17671.0:
                var28 = 0.005437614
            else:
                var28 = 0.05174432
    else:
        if input[31] < 19179.0:
            if input[36] < 0.5172115:
                var28 = -0.023903575
            else:
                var28 = 0.045341365
        else:
            if input[37] < 0.46350494:
                var28 = 0.11213352
            else:
                var28 = -0.077189036
    if input[16] < 1361.0:
        if input[36] < 0.48676106:
            if input[36] < 0.47538808:
                var29 = -0.087689765
            else:
                var29 = -0.03539182
        else:
            if input[10] < 14788.0:
                var29 = -0.053682692
            else:
                var29 = 0.008820247
    else:
        if input[37] < 0.4898917:
            if input[19] < 86.0:
                var29 = 0.08066213
            else:
                var29 = -0.06967678
        else:
            if input[29] < 14611.0:
                var29 = 0.06890009
            else:
                var29 = 0.010508954
    if input[37] < 0.51854736:
        if input[25] < 1.0:
            if input[36] < 0.52080965:
                var30 = 0.020985274
            else:
                var30 = 0.08400496
        else:
            if input[37] < 0.480677:
                var30 = 0.045451324
            else:
                var30 = -0.019720081
    else:
        if input[29] < 15914.0:
            if input[36] < 0.510964:
                var30 = -0.032886602
            else:
                var30 = 0.051084824
        else:
            if input[31] < 15927.0:
                var30 = 0.10748923
            else:
                var30 = -0.077150755
    if input[15] < -2794.0:
        if input[37] < 0.47443613:
            if input[5] < 3.0:
                var31 = -0.019058604
            else:
                var31 = 0.1001925
        else:
            if input[37] < 0.5010827:
                var31 = -0.04247005
            else:
                var31 = -0.086576566
    else:
        if input[36] < 0.506568:
            if input[37] < 0.5151775:
                var31 = 0.0016557798
            else:
                var31 = -0.05275182
        else:
            if input[36] < 0.52980304:
                var31 = 0.02621217
            else:
                var31 = 0.1013506
    if input[15] < 2015.0:
        if input[37] < 0.5151775:
            if input[36] < 0.5172115:
                var32 = -0.0071740374
            else:
                var32 = 0.04787333
        else:
            if input[15] < -802.0:
                var32 = -0.073511094
            else:
                var32 = -0.028910303
    else:
        if input[36] < 0.510964:
            if input[15] < 4957.0:
                var32 = 0.021793539
            else:
                var32 = 0.10323872
        else:
            if input[12] < 19069.0:
                var32 = 0.10653951
            else:
                var32 = 0.064055376
    if input[7] < 1.0:
        if input[31] < 19144.0:
            if input[36] < 0.499963:
                var33 = -0.024757152
            else:
                var33 = 0.015546656
        else:
            if input[10] < 16300.0:
                var33 = -0.0711037
            else:
                var33 = -0.017848073
    else:
        if input[37] < 0.49638098:
            if input[29] < 15810.0:
                var33 = 0.081328355
            else:
                var33 = 0.032500606
        else:
            if input[16] < 2107.0:
                var33 = -0.003585167
            else:
                var33 = 0.070485555
    if input[37] < 0.4843998:
        if input[12] < 18823.0:
            if input[36] < 0.47538808:
                var34 = -0.1084288
            else:
                var34 = 0.031961236
        else:
            if input[19] < 84.0:
                var34 = 0.091884375
            else:
                var34 = -0.023287786
    else:
        if input[16] < -1748.0:
            if input[36] < 0.49308518:
                var34 = -0.084423155
            else:
                var34 = -0.031423066
        else:
            if input[36] < 0.52980304:
                var34 = -0.0028088826
            else:
                var34 = 0.097299814
    if input[36] < 0.48376793:
        if input[15] < -973.0:
            if input[37] < 0.47195148:
                var35 = 0.051783543
            else:
                var35 = -0.08469229
        else:
            if input[37] < 0.47671697:
                var35 = 0.059439786
            else:
                var35 = -0.028859822
    else:
        if input[16] < -2624.0:
            if input[37] < 0.48663878:
                var35 = 0.011434488
            else:
                var35 = -0.07899167
        else:
            if input[37] < 0.52454764:
                var35 = 0.016200881
            else:
                var35 = -0.053209096
    if input[26] < 1.0:
        if input[16] < 2107.0:
            if input[37] < 0.4969986:
                var36 = 0.028826136
            else:
                var36 = -0.008013598
        else:
            if input[6] < 1.0:
                var36 = 0.02042577
            else:
                var36 = 0.07784334
    else:
        if input[37] < 0.4697763:
            if input[0] < 34.0:
                var36 = 0.11059127
            else:
                var36 = -0.00631558
        else:
            if input[37] < 0.5202151:
                var36 = -0.016885439
            else:
                var36 = -0.07474775
    if input[36] < 0.47930402:
        if input[12] < 19278.0:
            if input[29] < 13821.0:
                var37 = 0.08632175
            else:
                var37 = -0.06413354
        else:
            if input[13] < 237.0:
                var37 = -0.030411962
            else:
                var37 = 0.11619281
    else:
        if input[10] < 14788.0:
            if input[29] < 17898.0:
                var37 = -0.025034541
            else:
                var37 = -0.09638785
        else:
            if input[37] < 0.4898917:
                var37 = 0.039260667
            else:
                var37 = 0.0012414057
    if input[7] < 1.0:
        if input[31] < 17438.0:
            if input[36] < 0.5090931:
                var38 = 0.0015045466
            else:
                var38 = 0.052952286
        else:
            if input[37] < 0.47997773:
                var38 = 0.03654173
            else:
                var38 = -0.02782443
    else:
        if input[16] < 2107.0:
            if input[37] < 0.49638098:
                var38 = 0.03615408
            else:
                var38 = -0.0012359202
        else:
            if input[10] < 16812.0:
                var38 = 0.004690101
            else:
                var38 = 0.07977151
    if input[36] < 0.5219969:
        if input[29] < 15068.0:
            if input[16] < 720.0:
                var39 = -0.006743406
            else:
                var39 = 0.0438078
        else:
            if input[10] < 14788.0:
                var39 = -0.05051539
            else:
                var39 = -0.005186632
    else:
        if input[15] < -3563.0:
            if input[5] < 5.0:
                var39 = -0.09479985
            else:
                var39 = -0.0037105617
        else:
            if input[36] < 0.52980304:
                var39 = 0.03682497
            else:
                var39 = 0.09095069
    if input[36] < 0.47930402:
        if input[12] < 19278.0:
            if input[29] < 13821.0:
                var40 = 0.078698896
            else:
                var40 = -0.05964142
        else:
            if input[13] < 237.0:
                var40 = -0.02915824
            else:
                var40 = 0.106751405
    else:
        if input[16] < -2624.0:
            if input[37] < 0.48663878:
                var40 = 0.015716087
            else:
                var40 = -0.07071415
        else:
            if input[37] < 0.47997773:
                var40 = 0.051493205
            else:
                var40 = 0.0036683634
    if input[37] < 0.52048165:
        if input[36] < 0.506568:
            if input[26] < 1.0:
                var41 = 0.007825752
            else:
                var41 = -0.023613669
        else:
            if input[16] < -2624.0:
                var41 = -0.05198248
            else:
                var41 = 0.030731423
    else:
        if input[29] < 15914.0:
            if input[14] < 58.0:
                var41 = -0.03145754
            else:
                var41 = 0.050123464
        else:
            if input[14] < 44.0:
                var41 = -0.017725116
            else:
                var41 = -0.0774577
    if input[36] < 0.5291833:
        if input[15] < 2015.0:
            if input[36] < 0.47538808:
                var42 = -0.06602344
            else:
                var42 = -0.004640344
        else:
            if input[15] < 4957.0:
                var42 = 0.022063298
            else:
                var42 = 0.09522282
    else:
        if input[10] < 14591.0:
            if input[32] < 229.0:
                var42 = -0.0011609641
            else:
                var42 = -0.10878601
        else:
            if input[37] < 0.5141922:
                var42 = 0.1052855
            else:
                var42 = 0.013022156
    if input[37] < 0.51854736:
        if input[11] < 6.8:
            if input[16] < -3783.0:
                var43 = -0.09634561
            else:
                var43 = -0.016453013
        else:
            if input[36] < 0.516201:
                var43 = 0.0054863193
            else:
                var43 = 0.048482805
    else:
        if input[29] < 15914.0:
            if input[13] < 227.0:
                var43 = 0.03099134
            else:
                var43 = -0.039439443
        else:
            if input[31] < 15927.0:
                var43 = 0.10354697
            else:
                var43 = -0.05904339
    if input[26] < 1.0:
        if input[15] < 3822.0:
            if input[36] < 0.49592552:
                var44 = -0.009963256
            else:
                var44 = 0.019381845
        else:
            if input[12] < 18304.0:
                var44 = -0.004215162
            else:
                var44 = 0.08695444
    else:
        if input[37] < 0.5126745:
            if input[37] < 0.4697763:
                var44 = 0.08455285
            else:
                var44 = -0.010244499
        else:
            if input[14] < 71.0:
                var44 = -0.053659823
            else:
                var44 = 0.094055824
    var45 = var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44
    if input[7] < 1.0:
        if input[31] < 19559.0:
            if input[36] < 0.499963:
                var46 = -0.019058498
            else:
                var46 = 0.010240611
        else:
            if input[32] < 244.0:
                var46 = -0.08560958
            else:
                var46 = -0.0049489695
    else:
        if input[16] < 2107.0:
            if input[37] < 0.53031534:
                var46 = 0.013671811
            else:
                var46 = -0.08087607
        else:
            if input[36] < 0.4790924:
                var46 = -0.00843658
            else:
                var46 = 0.06973093
    if input[37] < 0.47997773:
        if input[29] < 16782.0:
            if input[36] < 0.49921107:
                var47 = 0.033784416
            else:
                var47 = 0.08833958
        else:
            if input[19] < 15.0:
                var47 = -0.06689577
            else:
                var47 = 0.021292306
    else:
        if input[10] < 14788.0:
            if input[0] < 19.0:
                var47 = -0.059117924
            else:
                var47 = 0.005653986
        else:
            if input[36] < 0.48399234:
                var47 = -0.033825703
            else:
                var47 = 0.006072542
    if input[36] < 0.5291833:
        if input[29] < 15279.0:
            if input[12] < 17258.0:
                var48 = -0.031068007
            else:
                var48 = 0.029018566
        else:
            if input[36] < 0.48399234:
                var48 = -0.037554603
            else:
                var48 = -0.0024069261
    else:
        if input[10] < 14591.0:
            if input[32] < 229.0:
                var48 = -0.00013645185
            else:
                var48 = -0.10185011
        else:
            if input[13] < 191.0:
                var48 = -0.003709073
            else:
                var48 = 0.09918757
    if input[37] < 0.52048165:
        if input[15] < 1711.0:
            if input[36] < 0.5291833:
                var49 = -0.003858634
            else:
                var49 = 0.06848947
        else:
            if input[36] < 0.510964:
                var49 = 0.018209089
            else:
                var49 = 0.065654635
    else:
        if input[14] < 59.0:
            if input[14] < 44.0:
                var49 = 0.0036105607
            else:
                var49 = -0.06768339
        else:
            if input[10] < 16379.0:
                var49 = -0.061378974
            else:
                var49 = 0.062010206
    if input[15] < -3179.0:
        if input[37] < 0.46714285:
            var50 = 0.09895716
        else:
            if input[32] < 214.0:
                var50 = -0.10703933
            else:
                var50 = -0.038341936
    else:
        if input[36] < 0.52980304:
            if input[37] < 0.4843998:
                var50 = 0.029364187
            else:
                var50 = -0.0037138239
        else:
            if input[13] < 191.0:
                var50 = -0.029207526
            else:
                var50 = 0.09486188
    if input[26] < 1.0:
        if input[29] < 18688.0:
            if input[15] < 3822.0:
                var51 = 0.009504272
            else:
                var51 = 0.07065991
        else:
            if input[37] < 0.4959949:
                var51 = -0.0011486419
            else:
                var51 = -0.0873019
    else:
        if input[37] < 0.5126745:
            if input[37] < 0.4697763:
                var51 = 0.07788567
            else:
                var51 = -0.008277797
        else:
            if input[5] < 11.0:
                var51 = -0.053021945
            else:
                var51 = 0.02910313
    if input[36] < 0.47538808:
        if input[12] < 19239.0:
            if input[20] < 1.0:
                var52 = 0.069496326
            else:
                var52 = -0.070146285
        else:
            if input[13] < 233.0:
                var52 = -0.029623827
            else:
                var52 = 0.11473683
    else:
        if input[37] < 0.47997773:
            if input[29] < 16967.0:
                var52 = 0.0576665
            else:
                var52 = -0.00024098731
        else:
            if input[29] < 14611.0:
                var52 = 0.041592907
            else:
                var52 = -0.00429305
    if input[37] < 0.52533597:
        if input[10] < 14788.0:
            if input[29] < 17898.0:
                var53 = -0.014235352
            else:
                var53 = -0.08258655
        else:
            if input[36] < 0.5291833:
                var53 = 0.004321553
            else:
                var53 = 0.0754531
    else:
        if input[12] < 18823.0:
            if input[3] < 8.0:
                var53 = -0.07906235
            else:
                var53 = 0.011866787
        else:
            if input[10] < 16875.0:
                var53 = 0.11317142
            else:
                var53 = -0.053484377
    if input[7] < 1.0:
        if input[31] < 19559.0:
            if input[36] < 0.506568:
                var54 = -0.012011795
            else:
                var54 = 0.014123452
        else:
            if input[32] < 252.0:
                var54 = -0.070925266
            else:
                var54 = 0.030291189
    else:
        if input[37] < 0.49638098:
            if input[29] < 15810.0:
                var54 = 0.06282404
            else:
                var54 = 0.016249422
        else:
            if input[14] < 59.0:
                var54 = -0.010412948
            else:
                var54 = 0.03573792
    if input[37] < 0.46914604:
        if input[0] < 30.0:
            if input[13] < 199.0:
                var55 = 0.0014643418
            else:
                var55 = 0.09440281
        else:
            if input[31] < 17644.0:
                var55 = 0.07224339
            else:
                var55 = -0.08029703
    else:
        if input[36] < 0.506568:
            if input[37] < 0.52713656:
                var55 = -0.006260328
            else:
                var55 = -0.06242481
        else:
            if input[31] < 16873.0:
                var55 = 0.06522008
            else:
                var55 = 0.005050897
    if input[14] < 60.0:
        if input[29] < 14885.0:
            if input[16] < 887.0:
                var56 = -0.010013159
            else:
                var56 = 0.044787567
        else:
            if input[37] < 0.5151775:
                var56 = -0.0034208607
            else:
                var56 = -0.03457689
    else:
        if input[12] < 19011.0:
            if input[36] < 0.47673076:
                var56 = -0.08621677
            else:
                var56 = 0.010698654
        else:
            if input[24] < 3.0:
                var56 = 0.001098431
            else:
                var56 = 0.06980031
    if input[36] < 0.47930402:
        if input[12] < 19278.0:
            if input[3] < 12.0:
                var57 = -0.035257787
            else:
                var57 = -0.14888145
        else:
            if input[10] < 17309.0:
                var57 = 0.15531099
            else:
                var57 = -0.0014706048
    else:
        if input[16] < -2624.0:
            if input[37] < 0.4886479:
                var57 = 0.019161915
            else:
                var57 = -0.05627898
        else:
            if input[36] < 0.5314829:
                var57 = 0.003794072
            else:
                var57 = 0.07656505
    if input[26] < 1.0:
        if input[15] < -3798.0:
            if input[24] < 14.0:
                var58 = -0.09622061
            else:
                var58 = 0.028755968
        else:
            if input[15] < 3822.0:
                var58 = 0.007281694
            else:
                var58 = 0.06361322
    else:
        if input[37] < 0.51173264:
            if input[36] < 0.51645863:
                var58 = -0.009509982
            else:
                var58 = 0.0342339
        else:
            if input[33] < 57.0:
                var58 = -0.058513075
            else:
                var58 = 0.010711659
    if input[37] < 0.46914604:
        if input[16] < -1268.0:
            if input[10] < 15273.0:
                var59 = 0.10515944
            else:
                var59 = -0.09938726
        else:
            if input[19] < 15.0:
                var59 = -0.0003405018
            else:
                var59 = 0.09961402
    else:
        if input[10] < 14788.0:
            if input[0] < 19.0:
                var59 = -0.04682419
            else:
                var59 = 0.016840193
        else:
            if input[36] < 0.48399234:
                var59 = -0.022482868
            else:
                var59 = 0.0056419037
    if input[36] < 0.4623477:
        if input[24] < 4.0:
            var60 = -0.025801549
        else:
            var60 = -0.10731659
    else:
        if input[6] < 2.0:
            if input[15] < 4957.0:
                var60 = -0.0026173533
            else:
                var60 = 0.098150216
        else:
            if input[10] < 15667.0:
                var60 = 0.09275073
            else:
                var60 = 0.019937538
    if input[36] < 0.5219969:
        if input[37] < 0.46914604:
            if input[19] < 15.0:
                var61 = -0.005795277
            else:
                var61 = 0.07414839
        else:
            if input[10] < 14788.0:
                var61 = -0.031322584
            else:
                var61 = -0.00079347723
    else:
        if input[16] < 227.0:
            if input[32] < 205.0:
                var61 = -0.07599493
            else:
                var61 = 0.030123299
        else:
            if input[4] < 4.0:
                var61 = 0.007357946
            else:
                var61 = 0.085356794
    if input[37] < 0.52533597:
        if input[25] < 1.0:
            if input[36] < 0.5123416:
                var62 = 0.004746175
            else:
                var62 = 0.034312665
        else:
            if input[31] < 19058.0:
                var62 = -0.00021860003
            else:
                var62 = -0.03409781
    else:
        if input[33] < 37.0:
            if input[10] < 17440.0:
                var62 = 0.10647637
            else:
                var62 = -0.04147109
        else:
            if input[12] < 18690.0:
                var62 = -0.06508496
            else:
                var62 = 0.0041948855
    if input[14] < 60.0:
        if input[29] < 14885.0:
            if input[0] < 38.0:
                var63 = 0.034664486
            else:
                var63 = -0.04019576
        else:
            if input[37] < 0.5151775:
                var63 = -0.0031143036
            else:
                var63 = -0.030087713
    else:
        if input[29] < 18506.0:
            if input[37] < 0.48457554:
                var63 = 0.07034206
            else:
                var63 = 0.013858032
        else:
            if input[36] < 0.5201621:
                var63 = -0.091588326
            else:
                var63 = 0.06073804
    if input[36] < 0.4623477:
        if input[24] < 4.0:
            var64 = -0.0254774
        else:
            var64 = -0.10470375
    else:
        if input[15] < 4957.0:
            if input[6] < 2.0:
                var64 = -0.0022685432
            else:
                var64 = 0.031304378
        else:
            if input[6] < 2.0:
                var64 = 0.09477349
            else:
                var64 = -0.014857471
    if input[36] < 0.5314829:
        if input[0] < 48.0:
            if input[37] < 0.46606225:
                var65 = 0.06970575
            else:
                var65 = 0.00013483499
        else:
            if input[16] < 1429.0:
                var65 = -0.044409122
            else:
                var65 = 0.034080546
    else:
        if input[13] < 191.0:
            if input[36] < 0.53493816:
                var65 = -0.0932912
            else:
                var65 = 0.04536088
        else:
            if input[11] < 6.8:
                var65 = -0.016138552
            else:
                var65 = 0.107295655
    if input[36] < 0.4623477:
        if input[37] < 0.5108272:
            var66 = -0.10505789
        else:
            var66 = -0.028937234
    else:
        if input[10] < 13602.0:
            if input[1] < 3.0:
                var66 = -0.10333172
            else:
                var66 = -0.029929651
        else:
            if input[37] < 0.49445194:
                var66 = 0.012480868
            else:
                var66 = -0.004322873
    if input[16] < -3783.0:
        if input[10] < 15423.0:
            if input[29] < 20239.0:
                var67 = -0.10829935
            else:
                var67 = -0.010028774
        else:
            var67 = 0.031175097
    else:
        if input[37] < 0.47671697:
            if input[19] < 15.0:
                var67 = -0.028971026
            else:
                var67 = 0.0506289
        else:
            if input[7] < 1.0:
                var67 = -0.006975873
            else:
                var67 = 0.009631597
    if input[15] < 4957.0:
        if input[37] < 0.53031534:
            if input[14] < 60.0:
                var68 = -0.0032111898
            else:
                var68 = 0.016765654
        else:
            if input[3] < 8.0:
                var68 = -0.07519429
            else:
                var68 = 0.013455157
    else:
        if input[11] < 7.6:
            if input[13] < 206.0:
                var68 = 0.010384894
            else:
                var68 = 0.10298868
        else:
            var68 = -0.016421087
    if input[36] < 0.4623477:
        if input[24] < 4.0:
            var69 = -0.019716034
        else:
            var69 = -0.09972047
    else:
        if input[36] < 0.5314829:
            if input[29] < 17811.0:
                var69 = 0.0029504746
            else:
                var69 = -0.017942283
        else:
            if input[13] < 191.0:
                var69 = -0.03507678
            else:
                var69 = 0.08264971
    if input[10] < 13602.0:
        if input[14] < 44.0:
            if input[15] < -4331.0:
                var70 = 0.038400386
            else:
                var70 = -0.06867618
        else:
            var70 = -0.09885302
    else:
        if input[36] < 0.506568:
            if input[37] < 0.46914604:
                var70 = 0.055758268
            else:
                var70 = -0.005934546
        else:
            if input[31] < 16873.0:
                var70 = 0.05751167
            else:
                var70 = 0.0049359105
    if input[36] < 0.47930402:
        if input[32] < 245.0:
            if input[13] < 245.0:
                var71 = -0.023267603
            else:
                var71 = 0.070572704
        else:
            if input[36] < 0.46551767:
                var71 = -0.028384093
            else:
                var71 = -0.10590502
    else:
        if input[3] < 12.0:
            if input[6] < 2.0:
                var71 = -0.00159614
            else:
                var71 = 0.02976194
        else:
            if input[0] < 21.0:
                var71 = 0.022649711
            else:
                var71 = 0.10089852
    if input[0] < 48.0:
        if input[36] < 0.5172115:
            if input[32] < 243.0:
                var72 = -0.0038068295
            else:
                var72 = 0.02095664
        else:
            if input[37] < 0.4929352:
                var72 = 0.07647432
            else:
                var72 = 0.0048744893
    else:
        if input[11] < 6.8:
            if input[36] < 0.51148075:
                var72 = -0.02592719
            else:
                var72 = -0.18158685
        else:
            if input[37] < 0.48309898:
                var72 = 0.07215892
            else:
                var72 = -0.027513925
    if input[16] < -3783.0:
        if input[4] < 14.0:
            if input[12] < 16533.0:
                var73 = -0.102782205
            else:
                var73 = -0.027098138
        else:
            if input[37] < 0.49619758:
                var73 = 0.09753385
            else:
                var73 = -0.05713143
    else:
        if input[36] < 0.4623477:
            if input[37] < 0.5108272:
                var73 = -0.09919917
            else:
                var73 = -0.021429004
        else:
            if input[37] < 0.52533597:
                var73 = 0.0029086699
            else:
                var73 = -0.029876724
    if input[15] < 4957.0:
        if input[37] < 0.53031534:
            if input[25] < 2.0:
                var74 = 0.0023527646
            else:
                var74 = -0.025189254
        else:
            if input[14] < 41.0:
                var74 = 0.043171752
            else:
                var74 = -0.061640646
    else:
        if input[6] < 2.0:
            if input[1] < 5.0:
                var74 = 0.101122335
            else:
                var74 = 0.008806704
        else:
            var74 = -0.02355843
    if input[3] < 4.0:
        if input[7] < 1.0:
            if input[0] < 19.0:
                var75 = -0.04059526
            else:
                var75 = 0.0026338573
        else:
            if input[20] < 4.0:
                var75 = 0.039927628
            else:
                var75 = -0.03501175
    else:
        if input[36] < 0.53493816:
            if input[37] < 0.49075243:
                var75 = 0.016537417
            else:
                var75 = -0.0025535335
        else:
            var75 = 0.09865042
    if input[14] < 60.0:
        if input[32] < 260.0:
            if input[0] < 48.0:
                var76 = -0.0019807229
            else:
                var76 = -0.03675131
        else:
            if input[1] < 1.0:
                var76 = 0.17220418
            else:
                var76 = 0.04142078
    else:
        if input[3] < 6.0:
            if input[36] < 0.5050462:
                var76 = -0.023598848
            else:
                var76 = 0.029462412
        else:
            if input[31] < 18324.0:
                var76 = 0.020231852
            else:
                var76 = 0.07035859
    if input[10] < 13602.0:
        if input[1] < 3.0:
            var77 = -0.09613593
        else:
            if input[16] < -3175.0:
                var77 = 0.035172366
            else:
                var77 = -0.06299807
    else:
        if input[36] < 0.4623477:
            if input[37] < 0.5108272:
                var77 = -0.096311346
            else:
                var77 = -0.01907243
        else:
            if input[15] < 4957.0:
                var77 = 0.00051830575
            else:
                var77 = 0.067463055
    if input[16] < -3783.0:
        if input[10] < 15423.0:
            if input[29] < 20239.0:
                var78 = -0.10395098
            else:
                var78 = -0.0065066367
        else:
            var78 = 0.032887537
    else:
        if input[36] < 0.47538808:
            if input[12] < 19239.0:
                var78 = -0.043016903
            else:
                var78 = 0.06971442
        else:
            if input[37] < 0.47997773:
                var78 = 0.025270626
            else:
                var78 = -0.00021420617
    if input[29] < 17811.0:
        if input[1] < 1.0:
            if input[5] < 4.0:
                var79 = -0.028334258
            else:
                var79 = 0.053771097
        else:
            if input[36] < 0.50057554:
                var79 = -0.008241394
            else:
                var79 = 0.009826593
    else:
        if input[0] < 20.0:
            if input[13] < 191.0:
                var79 = 0.041189004
            else:
                var79 = -0.017234117
        else:
            if input[31] < 17298.0:
                var79 = 0.07650696
            else:
                var79 = -0.06512638
    if input[36] < 0.5314829:
        if input[37] < 0.50529176:
            if input[31] < 18337.0:
                var80 = 0.012646212
            else:
                var80 = -0.009310575
        else:
            if input[33] < 59.0:
                var80 = -0.017028356
            else:
                var80 = 0.018299667
    else:
        if input[13] < 191.0:
            if input[24] < 7.0:
                var80 = -0.10492431
            else:
                var80 = 0.029690256
        else:
            if input[11] < 6.8:
                var80 = -0.024723088
            else:
                var80 = 0.1016477
    if input[15] < -4882.0:
        if input[5] < 5.0:
            var81 = -0.09790291
        else:
            if input[37] < 0.49236646:
                var81 = 0.12526084
            else:
                var81 = -0.05732855
    else:
        if input[14] < 60.0:
            if input[32] < 252.0:
                var81 = -0.0040470096
            else:
                var81 = 0.03993906
        else:
            if input[32] < 203.0:
                var81 = 0.054753482
            else:
                var81 = 0.005498245
    if input[37] < 0.5404521:
        if input[26] < 1.0:
            if input[33] < 69.0:
                var82 = 0.003759063
            else:
                var82 = 0.064165354
        else:
            if input[19] < 64.0:
                var82 = -0.0043342616
            else:
                var82 = -0.072312295
    else:
        var82 = -0.08488954
    if input[36] < 0.4623477:
        if input[37] < 0.5108272:
            var83 = -0.092335515
        else:
            var83 = -0.015704675
    else:
        if input[10] < 13602.0:
            if input[14] < 44.0:
                var83 = -0.014835623
            else:
                var83 = -0.09196872
        else:
            if input[29] < 13962.0:
                var83 = 0.046547525
            else:
                var83 = 0.00020428021
    if input[37] < 0.46606225:
        if input[32] < 232.0:
            if input[0] < 20.0:
                var84 = 0.10311576
            else:
                var84 = 0.018984038
        else:
            if input[26] < 1.0:
                var84 = -0.09775161
            else:
                var84 = 0.086224705
    else:
        if input[10] < 13602.0:
            if input[1] < 4.0:
                var84 = -0.09317344
            else:
                var84 = -0.008865271
        else:
            if input[36] < 0.506568:
                var84 = -0.004480366
            else:
                var84 = 0.00856855
    if input[0] < 48.0:
        if input[0] < 47.0:
            if input[31] < 16814.0:
                var85 = 0.018495172
            else:
                var85 = -0.001399184
        else:
            var85 = 0.12752925
    else:
        if input[11] < 6.8:
            if input[36] < 0.51148075:
                var85 = -0.018704306
            else:
                var85 = -0.16601624
        else:
            if input[37] < 0.48309898:
                var85 = 0.06943341
            else:
                var85 = -0.02288
    if input[15] < 4957.0:
        if input[6] < 2.0:
            if input[33] < 32.0:
                var86 = -0.06936608
            else:
                var86 = -0.0014325826
        else:
            if input[37] < 0.50989383:
                var86 = 0.04032397
            else:
                var86 = -0.017499337
    else:
        if input[11] < 7.6:
            if input[5] < 17.0:
                var86 = 0.096457735
            else:
                var86 = 0.005887082
        else:
            var86 = -0.031908024
    if input[36] < 0.5314829:
        if input[37] < 0.50529176:
            if input[1] < 5.0:
                var87 = -0.000596091
            else:
                var87 = 0.028009728
        else:
            if input[29] < 14258.0:
                var87 = 0.06003303
            else:
                var87 = -0.011064612
    else:
        if input[13] < 203.0:
            if input[24] < 6.0:
                var87 = -0.107315205
            else:
                var87 = 0.05104199
        else:
            if input[11] < 6.8:
                var87 = -0.00009034887
            else:
                var87 = 0.0979285
    if input[16] < -3783.0:
        if input[33] < 45.0:
            var88 = 0.04827632
        else:
            if input[12] < 16684.0:
                var88 = -0.09848251
            else:
                var88 = 0.00040545073
    else:
        if input[33] < 61.0:
            if input[37] < 0.51173264:
                var88 = 0.0026732513
            else:
                var88 = -0.018124266
        else:
            if input[15] < 147.0:
                var88 = -0.0056384425
            else:
                var88 = 0.04528753
    if input[36] < 0.4623477:
        if input[37] < 0.5108272:
            var89 = -0.09008373
        else:
            var89 = -0.0136703225
    else:
        if input[37] < 0.5404521:
            if input[26] < 1.0:
                var89 = 0.0054992223
            else:
                var89 = -0.005772822
        else:
            var89 = -0.081617564
    if input[36] < 0.47930402:
        if input[32] < 245.0:
            if input[13] < 245.0:
                var90 = -0.017685032
            else:
                var90 = 0.06822699
        else:
            if input[3] < 3.0:
                var90 = -0.024568705
            else:
                var90 = -0.10441168
    else:
        if input[3] < 12.0:
            if input[32] < 243.0:
                var90 = -0.0024910015
            else:
                var90 = 0.018968916
        else:
            if input[33] < 60.0:
                var90 = 0.054662734
            else:
                var90 = -0.054161053
    if input[37] < 0.46606225:
        if input[32] < 232.0:
            if input[0] < 20.0:
                var91 = 0.100647226
            else:
                var91 = 0.016975312
        else:
            if input[26] < 1.0:
                var91 = -0.087853424
            else:
                var91 = 0.08305433
    else:
        if input[10] < 13602.0:
            if input[1] < 4.0:
                var91 = -0.09052588
            else:
                var91 = -0.007545147
        else:
            if input[36] < 0.5219969:
                var91 = -0.0017083243
            else:
                var91 = 0.021874802
    if input[3] < 4.0:
        if input[29] < 17898.0:
            if input[13] < 201.0:
                var92 = 0.05263084
            else:
                var92 = -0.0133843515
        else:
            if input[33] < 71.0:
                var92 = -0.07458938
            else:
                var92 = 0.039204057
    else:
        if input[36] < 0.53493816:
            if input[36] < 0.48815367:
                var92 = -0.011698111
            else:
                var92 = 0.005575397
        else:
            var92 = 0.09281367
    if input[14] < 60.0:
        if input[32] < 260.0:
            if input[29] < 14885.0:
                var93 = 0.020198109
            else:
                var93 = -0.0060913465
        else:
            if input[1] < 1.0:
                var93 = 0.14933129
            else:
                var93 = 0.03677277
    else:
        if input[29] < 18506.0:
            if input[32] < 203.0:
                var93 = 0.05553017
            else:
                var93 = 0.007625531
        else:
            if input[36] < 0.5201621:
                var93 = -0.08724833
            else:
                var93 = 0.05264924
    if input[0] < 48.0:
        if input[0] < 47.0:
            if input[32] < 243.0:
                var94 = -0.0013016544
            else:
                var94 = 0.018607602
        else:
            var94 = 0.12204709
    else:
        if input[16] < 1429.0:
            if input[20] < 6.0:
                var94 = -0.040007275
            else:
                var94 = 0.056421418
        else:
            if input[32] < 195.0:
                var94 = -0.04192547
            else:
                var94 = 0.07791773
    if input[37] < 0.5404521:
        if input[0] < 15.0:
            if input[24] < 7.0:
                var95 = -0.02248269
            else:
                var95 = 0.00525343
        else:
            if input[20] < 1.0:
                var95 = 0.035865393
            else:
                var95 = 0.0016080233
    else:
        var95 = -0.07890805
    if input[12] < 14927.0:
        if input[36] < 0.5123416:
            var96 = -0.1078841
        else:
            var96 = 0.011260504
    else:
        if input[37] < 0.46914604:
            if input[0] < 30.0:
                var96 = 0.061311085
            else:
                var96 = -0.034750715
        else:
            if input[31] < 19630.0:
                var96 = 0.0009377549
            else:
                var96 = -0.02357854
    if input[33] < 61.0:
        if input[37] < 0.51173264:
            if input[19] < 18.0:
                var97 = -0.007544125
            else:
                var97 = 0.015993578
        else:
            if input[36] < 0.51133436:
                var97 = -0.029019445
            else:
                var97 = 0.0125281755
    else:
        if input[15] < 147.0:
            if input[32] < 208.0:
                var97 = -0.08021768
            else:
                var97 = 0.010716117
        else:
            if input[37] < 0.50877947:
                var97 = 0.010832728
            else:
                var97 = 0.110545754
    if input[19] < 38.0:
        if input[36] < 0.48676106:
            if input[20] < 9.0:
                var98 = -0.017388996
            else:
                var98 = 0.11712133
        else:
            if input[19] < 18.0:
                var98 = -0.000558414
            else:
                var98 = 0.020284813
    else:
        if input[25] < 2.0:
            if input[37] < 0.5168028:
                var98 = 0.004910928
            else:
                var98 = -0.07483982
        else:
            if input[15] < -2168.0:
                var98 = 0.02634702
            else:
                var98 = -0.14938655
    if input[3] < 4.0:
        if input[7] < 1.0:
            if input[0] < 19.0:
                var99 = -0.034888696
            else:
                var99 = 0.0063525103
        else:
            if input[10] < 15205.0:
                var99 = 0.041190587
            else:
                var99 = -0.032290783
    else:
        if input[36] < 0.53493816:
            if input[5] < 8.0:
                var99 = 0.0074565965
            else:
                var99 = -0.005493496
        else:
            var99 = 0.090043835
    if input[36] < 0.4623477:
        if input[37] < 0.5108272:
            var100 = -0.08606758
        else:
            var100 = -0.009493423
    else:
        if input[1] < 1.0:
            if input[29] < 17762.0:
                var100 = 0.036476117
            else:
                var100 = -0.04474876
        else:
            if input[36] < 0.5314829:
                var100 = -0.001842871
            else:
                var100 = 0.05767969
    var101 = sigmoid(var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96 + var97 + var98 + var99 + var100)
    return [1.0 - var101, var101]
