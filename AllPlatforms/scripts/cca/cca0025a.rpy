label cca0025a:
    太一 "「先輩……」"
    voice "vfcca0025amsa000"
    見里 "「なぁに？」"
    太一 "「俺のためにこれからずっと、みそ汁を作ってくれませんか？」"
    "なぜか俺はプロポーズしてしまった。"
    call gl(1,"TCMM0004c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0025amsa001"
    見里 "「えっ」"
    "先輩はうろたえる。"
    "体が傾いで、視線がそれる。"
    "小さな拳が口元に添えられ、額に思案の皺が刻まれた。"
    call gl(1,"TCMM0005c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0025amsa002"
    見里 "「ぺけくん……わたし……」"
    太一 "「はい」"
    voice "vfcca0025amsa003"
    見里 "「みそ汁、作れないんです」"
    太一 "「らりほー！」"
    "窓から叫んだ。"
    menu:
        "古式ゆかしいナイスボケだった。"
        "さらに迫る":
            $B=1
        "ボケる":
            $B=2
    return
    #