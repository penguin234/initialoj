dataset = [
    """1
    1""",
    """99
    13""",
    """35654
    59268""",
    """31071
    38937""",
    """54265
    25350""",
    """84419
    58042""",
    """80447
    19703""",
    """8750
    51732""",
    """65951
    72256""",
    """17495
    22765""",
    """30552
    848""",
    """67297
    43332""",
    """50541
    81406""",
    """62330
    36511""",
    """74177
    81649""",
    """71325
    71753""",
    """50398
    26144""",
    """67113
    28768""",
    """87961
    24953""",
    """99932
    12770""",
    """25349
    74332""",
    """53034
    75634""",
    """28107
    1849""",
    """97176
    7449""",
    """57398
    48443""",
    """59371
    80764""",
    """45474
    90324""",
    """10161
    51506""",
    """2429
    994""",
    """35229
    91702""",
    """38085
    72824""",
    """4507
    92786""",
    """64285
    49190""",
    """74691
    28884""",
    """41268
    52914""",
    """2717
    26973""",
    """19695
    3772""",
    """54855
    23300""",
    """74882
    26305""",
    """89073
    72751""",
    """99068
    31652""",
    """80311
    89803""",
    """8098
    17898""",
    """26291
    55940""",
    """81077
    88983""",
    """39002
    90712""",
    """19102
    68517""",
    """87104
    20653""",
    """88351
    35252""",
    """28546
    10546""",
    """33928
    12386""",
    """68241
    83241""",
    """70109
    57899""",
    """50781
    84417""",
    """94444
    73871""",
    """88397
    11760""",
    """89723
    33305""",
    """47662
    82195""",
    """54008
    3554""",
    """99827
    57642""",
    """63904
    61647""",
    """17984
    73419""",
    """90735
    64117""",
    """70736
    33276""",
    """20032
    3537""",
    """82584
    26766""",
    """6582
    30980""",
    """89747
    60254""",
    """365
    36972""",
    """96992
    77889""",
    """42004
    47710""",
    """74790
    18476""",
    """38830
    28057""",
    """80745
    66633""",
    """95614
    44750""",
    """73110
    49857""",
    """14530
    56844""",
    """25378
    22268""",
    """54335
    98742""",
    """38464
    23153""",
    """87265
    95907""",
    """56320
    71434""",
    """62356
    70935""",
    """50436
    14023""",
    """5651
    12269""",
    """87821
    43869""",
    """31359
    62099""",
    """23348
    13682""",
    """50287
    58006""",
    """99735
    44533""",
    """8615
    47683""",
    """68908
    73078""",
    """80591
    94543""",
    """6816
    23146""",
    """50328
    81437""",
    """44240
    33625""",
    """69229
    85473""",
    """5529
    90459""",
    """34595
    96924""",
    """30217
    69579""",
    """43251
    82358""",
    """41733
    66153""",

]


from problem import Problem

problems = dict()


addInputs = dataset[:]

addAnswerws = []
for addInput in addInputs:
    a, b = addInput.split('\n')
    addAnswerws.append(str(int(a) + int(b)))

addExamples = [
    ["""1
1""", '2'],
    ["""99
13""", '112'],
]

problems[1] = Problem(addInputs, addAnswerws, "더하기", 1, "정수 a, b를 입력받아 a + b를 출력하시오", addExamples)


subInputs = dataset[:]

subAnswerws = []
for subInput in subInputs:
    a, b = subInput.split('\n')
    subAnswerws.append(str(int(a) - int(b)))

subExamples = [
    ["""1
1""", '0'],
    ["""99
13""", '86'],
]

problems[2] = Problem(subInputs, subAnswerws, "빼기", 2, "정수 a, b를 입력받아 a - b를 출력하시오", subExamples)


multInputs = dataset[:]

multAnswerws = []
for multInput in multInputs:
    a, b = multInput.split('\n')
    multAnswerws.append(str(int(a) * int(b)))

multExamples = [
    ["""1
1""", '1'],
    ["""99
13""", '1287'],
]

problems[3] = Problem(multInputs, multAnswerws, "곱하기", 3, "정수 a, b를 입력받아 a * b를 출력하시오", multExamples)