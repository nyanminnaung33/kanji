"""N4 reading passages seeded into the passages table on app startup."""

PASSAGES = [
    {
        "title": "転職を決めた日",
        "level": "N4",
        "text": (
            "先月、今の会社を辞めることを決心しました。"
            "理由は給料が安いことと、人間関係が良くないことです。"
            "毎日残業が多くて、体も疲れていました。"
            "新しい仕事を探すために、インターネットで募集を調べました。"
            "いくつかの会社に履歴書を送りました。"
            "一週間後、電話で面接の連絡が来ました。"
            "面接の日は緊張しましたが、自分の意見をしっかり話しました。"
            "三日後、採用の通知をもらいました。"
            "給料も前より高くて、仕事の内容も面白そうでした。"
            "今の会社に辞める意思を伝えるときは、ちょっと怖かったです。"
            "上司は驚いていましたが、最後に「頑張れ」と言ってくれました。"
            "同僚には感謝の気持ちを伝えて、お菓子を配りました。"
            "最終出勤日の夜、みんなで食事会を開いてくれました。"
            "嬉しくて、ちょっと泣いてしまいました。"
            "来月から新しい職場で働き始めます。"
            "新しい環境が楽しみな半分、不安もあります。"
        ),
        "translation": (
            "Last month, I decided to quit my current company. "
            "The reasons were the low salary and poor human relationships. "
            "Every day there was a lot of overtime work, and my body was also tired. "
            "To look for a new job, I searched for recruitment listings online. "
            "I sent my resume to several companies. "
            "One week later, I received a phone call about an interview. "
            "On the interview day, I was nervous, but I clearly stated my opinions. "
            "Three days later, I received the hiring notice. "
            "The salary was higher than before, and the job content also seemed interesting. "
            "When I told my current company about my intention to quit, I was a little scared. "
            "My boss was surprised, but at the end he said \"Do your best.\" "
            "I expressed my gratitude to my colleagues and distributed sweets. "
            "On my last working day, everyone held a dinner party for me. "
            "I was happy and cried a little. "
            "I will start working at my new workplace from next month. "
            "I am half looking forward to the new environment and half anxious."
        ),
        "vocab": [
            ["先月", "せんげつ", "先 (previous) + 月 (month)", "last month"],
            ["今", "いま", "今 (now)", "now / current"],
            ["会社", "かいしゃ", "会 (meet/company) + 社 (company/shrine)", "company"],
            ["辞める", "やめる", "辞 (resign/quit)", "to quit"],
            ["決心", "けっしん", "決 (decide) + 心 (heart)", "decision / determination"],
            ["理由", "りゆう", "理 (reason/logic) + 由 (reason/cause)", "reason"],
            ["給料", "きゅうりょう", "給 (salary/provide) + 料 (fee/material)", "salary"],
            ["安い", "やすい", "安 (cheap/peaceful)", "cheap / low"],
            ["人間関係", "にんげんかんけい", "人 (person) + 間 (interval) + 関 (relation) + 係 (connection)", "human relationships"],
            ["毎日", "まいにち", "毎 (every) + 日 (day)", "every day"],
            ["残業", "ざんぎょう", "残 (remain) + 業 (work/business)", "overtime work"],
            ["体", "からだ", "体 (body)", "body"],
            ["疲れる", "つかれる", "疲 (tired/exhausted)", "to get tired"],
            ["新しい", "あたらしい", "新 (new)", "new"],
            ["仕事", "しごと", "仕 (serve/work) + 事 (thing/matter)", "work / job"],
            ["探す", "さがす", "探 (search/look for)", "to search"],
            ["募集", "ぼしゅう", "募 (recruit/gather) + 集 (collect/gather)", "recruitment"],
            ["履歴書", "りれきしょ", "履 (wear/shoe) + 歴 (history) + 書 (write/document)", "resume"],
            ["送る", "おくる", "送 (send)", "to send"],
            ["連絡", "れんらく", "連 (connect) + 絡 (entangle/contact)", "contact / communication"],
            ["面接", "めんせつ", "面 (face/surface) + 接 (contact/meet)", "interview"],
            ["意見", "いけん", "意 (mind/meaning) + 見 (see/opinion)", "opinion"],
            ["話す", "はなす", "話 (talk/speak)", "to speak"],
            ["採用", "さいよう", "採 (take/adopt) + 用 (use)", "hiring / adoption"],
            ["前", "まえ", "前 (before/front)", "before / previous"],
            ["高い", "たかい", "高 (high/expensive)", "expensive / high"],
            ["内容", "ないよう", "内 (inside) + 容 (contain/form)", "content"],
            ["意思", "いし", "意 (mind) + 思 (think)", "intention / will"],
            ["伝える", "つたえる", "伝 (transmit/tell)", "to tell / to convey"],
            ["怖い", "こわい", "怖 (scary/fearful)", "scary"],
            ["上司", "じょうし", "上 (up/above) + 司 (direct/office)", "boss / superior"],
            ["驚く", "おどろく", "驚 (surprise/amaze)", "to be surprised"],
            ["同僚", "どうりょう", "同 (same) + 僚 (colleague)", "colleague"],
            ["感謝", "かんしゃ", "感 (feeling) + 謝 (apologize/thank)", "gratitude"],
            ["気持ち", "きもち", "気 (spirit/energy) + 持 (hold)", "feeling"],
            ["お菓子", "おかし", "菓 (confectionery) + 子 (child/small)", "sweets / snacks"],
            ["配る", "くばる", "配 (distribute/arrange)", "to distribute"],
            ["最終", "さいしゅう", "最 (most/extreme) + 終 (end)", "final / last"],
            ["出勤", "しゅっきん", "出 (go out) + 勤 (work/duty)", "coming to work"],
            ["食事会", "しょくじかい", "食 (eat/food) + 事 (thing) + 会 (meeting)", "dinner party"],
            ["開く", "ひらく", "開 (open/hold)", "to hold (an event)"],
            ["泣く", "なく", "泣 (cry)", "to cry"],
            ["職場", "しょくば", "職 (job/employment) + 場 (place)", "workplace"],
            ["働く", "はたらく", "働 (work)", "to work"],
            ["始める", "はじめる", "始 (begin/start)", "to start"],
            ["環境", "かんきょう", "環 (ring/environment) + 境 (boundary)", "environment"],
            ["楽しみ", "たのしみ", "楽 (comfort/ease)", "anticipation / enjoyment"],
            ["半分", "はんぶん", "半 (half) + 分 (part)", "half"],
            ["不安", "ふあん", "不 (not/un-) + 安 (peaceful)", "anxiety"],
        ],
    },
    {
        "title": "母の誕生日サプライズ",
        "level": "N4",
        "text": (
            "先週の日曜日は母の60歳の誕生日でした。"
            "私と妹は内緒でサプライズを計画しました。"
            "一ヶ月前から準備を始めました。"
            "妹はケーキを予約して、私はプレゼントを選びました。"
            "母が好きな花と手紙も用意しました。"
            "当日の朝、早く起きて、妹と一緒に買い物に行きました。"
            "スーパーで美味しい肉と野菜を買いました。"
            "夜は私が料理を作ることになっていました。"
            "母には「今日は友達と食事する」と言って、家を出てもらいました。"
            "午後4時に妹とキッチンで料理を始めました。"
            "母の好きなカレーとサラダを作りました。"
            "ケーキもピックアップに行って、ろうそくを立てました。"
            "母が帰ってきたとき、電気を消して、ハッピーバースデーを歌いました。"
            "母は驚いて、すぐに泣き出しました。"
            "「ありがとう」を10回くらい言っていました。"
            "一緒にご飯を食べて、たくさん話しました。"
            "母が「今日は人生で一番嬉しい誕生日だった」と言って、私も嬉しくなりました。"
        ),
        "translation": (
            "Last Sunday was my mother's 60th birthday. "
            "My younger sister and I secretly planned a surprise. "
            "We started preparing one month in advance. "
            "My sister reserved a cake, and I chose a gift. "
            "I also prepared flowers and a letter that my mother likes. "
            "On the day of the event, I woke up early and went shopping with my sister. "
            "We bought delicious meat and vegetables at the supermarket. "
            "It was decided that I would cook dinner. "
            "I told my mother \"I'm going to eat with a friend today\" and had her leave the house. "
            "At 4 PM, my sister and I started cooking in the kitchen. "
            "We made curry and salad, which my mother likes. "
            "I also went to pick up the cake and set up candles. "
            "When my mother came home, we turned off the lights and sang Happy Birthday. "
            "My mother was surprised and immediately started crying. "
            "She said \"thank you\" about 10 times. "
            "We ate together and talked a lot. "
            "My mother said \"Today was the happiest birthday of my life,\" and I became happy too."
        ),
        "vocab": [
            ["先週", "せんしゅう", "先 (previous) + 週 (week)", "last week"],
            ["母", "はは", "母 (mother)", "mother"],
            ["誕生日", "たんじょうび", "誕 (birth) + 生 (life/birth) + 日 (day)", "birthday"],
            ["妹", "いもうと", "妹 (younger sister)", "younger sister"],
            ["内緒", "ないしょ", "内 (inside) + 緒 (thread/together)", "secret"],
            ["計画", "けいかく", "計 (measure/plan) + 画 (plan/drawing)", "plan"],
            ["前", "まえ", "前 (before)", "before"],
            ["準備", "じゅんび", "準 (standard/conform) + 備 (prepare)", "preparation"],
            ["始める", "はじめる", "始 (begin)", "to start"],
            ["予約", "よやく", "予 (beforehand) + 約 (promise)", "reservation"],
            ["プレゼント", "ぷれぜんと", "-", "gift / present"],
            ["選ぶ", "えらぶ", "選 (choose/select)", "to choose"],
            ["好きな", "すきな", "好 (like/fond)", "favorite / liked"],
            ["花", "はな", "花 (flower)", "flower"],
            ["手紙", "てがみ", "手 (hand) + 紙 (paper)", "letter"],
            ["用意", "ようい", "用 (use/business) + 意 (mind)", "preparation"],
            ["当日", "とうじつ", "当 (hit/appropriate) + 日 (day)", "the day (of the event)"],
            ["起きる", "おきる", "起 (wake up/rise)", "to wake up"],
            ["一緒に", "いっしょに", "一 (one) + 緒 (together)", "together"],
            ["買い物", "かいもの", "買 (buy) + 物 (thing)", "shopping"],
            ["美味しい", "おいしい", "美 (beautiful) + 味 (taste)", "delicious"],
            ["肉", "にく", "肉 (meat)", "meat"],
            ["野菜", "やさい", "野 (field) + 菜 (vegetable)", "vegetables"],
            ["夜", "よる", "夜 (night)", "night"],
            ["料理", "りょうり", "料 (fee/material) + 理 (arrangement)", "cooking / dish"],
            ["作る", "つくる", "作 (make)", "to make"],
            ["友達", "ともだち", "友 (friend) + 達 (plural)", "friend"],
            ["食事", "しょくじ", "食 (eat) + 事 (thing)", "meal"],
            ["家", "いえ", "家 (house)", "house"],
            ["出る", "でる", "出 (go out)", "to go out"],
            ["立てる", "たてる", "立 (stand/rise)", "to stand / to set up"],
            ["帰る", "かえる", "帰 (return)", "to return home"],
            ["電気", "でんき", "電 (electricity) + 気 (energy)", "electricity / light"],
            ["消す", "けす", "消 (erase/turn off)", "to turn off"],
            ["歌う", "うたう", "歌 (sing)", "to sing"],
            ["驚く", "おどろく", "驚 (surprise)", "to be surprised"],
            ["泣き出す", "なきだす", "泣 (cry) + 出 (start)", "to start crying"],
            ["ご飯", "ごはん", "飯 (meal/cooked rice)", "meal / rice"],
            ["人生", "じんせい", "人 (person) + 生 (life)", "human life"],
            ["一番", "いちばん", "一 (one) + 番 (number/turn)", "number one / best"],
        ],
    },
    {
        "title": "久しぶりの海外旅行",
        "level": "N4",
        "text": (
            "去年の冬、3年ぶりに海外旅行に行きました。"
            "行き先はハワイです。"
            "仕事が忙しくて、ずっと行けませんでしたが、やっと休みが取れました。"
            "飛行機のチケットとホテルはインターネットで予約しました。"
            "出発の一週間前から荷物を準備し始めました。"
            "服や薬、カメラなどを忘れないようにリストに書きました。"
            "空港には出発の2時間前に着きました。"
            "チェックインと手続きをして、搭乗口で待ちました。"
            "飛行機は10時間ほどで到着しました。"
            "現地の天気はとても良くて、暑かったです。"
            "ホテルの部屋から海が見えました。"
            "毎日プールで泳いだり、美味しい料理を食べたりしました。"
            "現地の人はとても親切で、困ったときはいつも助けてくれました。"
            "最終日はお土産をたくさん買いました。"
            "家族と友達に渡すのが楽しみです。"
            "帰りの飛行機の中で、「また来たい」と強く思いました。"
            "旅行の思い出は一生忘れられないです。"
        ),
        "translation": (
            "Last winter, I went on an overseas trip for the first time in three years. "
            "The destination was Hawaii. "
            "I couldn't go for a long time because work was busy, but I finally managed to take time off. "
            "I reserved the airplane tickets and hotel online. "
            "Starting one week before departure, I began preparing my luggage. "
            "I wrote a list of clothes, medicine, camera, etc., to make sure I wouldn't forget anything. "
            "I arrived at the airport two hours before departure. "
            "I did the check-in and procedures, then waited at the boarding gate. "
            "The flight took about 10 hours to arrive. "
            "The local weather was very good and hot. "
            "I could see the sea from my hotel room. "
            "Every day I swam in the pool and ate delicious food. "
            "The local people were very kind and always helped me when I was in trouble. "
            "On the last day, I bought many souvenirs. "
            "I was looking forward to giving them to my family and friends. "
            "On the return flight, I strongly thought \"I want to come again.\" "
            "The memories of the trip will be unforgettable for my entire life."
        ),
        "vocab": [
            ["去年", "きょねん", "去 (go past/leave) + 年 (year)", "last year"],
            ["冬", "ふゆ", "冬 (winter)", "winter"],
            ["久しぶり", "ひさしぶり", "久 (long time)", "after a long time"],
            ["海外旅行", "かいがいりょこう", "海 (sea) + 外 (outside) + 旅 (travel) + 行 (go)", "overseas travel"],
            ["行く", "いく", "行 (go)", "to go"],
            ["行き先", "いきさき", "行 (go) + 先 (ahead/destination)", "destination"],
            ["仕事", "しごと", "仕 (serve) + 事 (thing)", "work"],
            ["忙しい", "いそがしい", "忙 (busy)", "busy"],
            ["休み", "やすみ", "休 (rest)", "holiday / rest"],
            ["取る", "とる", "取 (take)", "to take (time off)"],
            ["飛行機", "ひこうき", "飛 (fly) + 行 (go) + 機 (machine)", "airplane"],
            ["予約", "よやく", "予 (beforehand) + 約 (promise)", "reservation"],
            ["出発", "しゅっぱつ", "出 (go out) + 発 (departure)", "departure"],
            ["前", "まえ", "前 (before)", "before"],
            ["荷物", "にもつ", "荷 (luggage) + 物 (thing)", "luggage"],
            ["準備", "じゅんび", "準 (standard) + 備 (prepare)", "preparation"],
            ["服", "ふく", "服 (clothes)", "clothes"],
            ["薬", "くすり", "薬 (medicine)", "medicine"],
            ["忘れる", "わすれる", "忘 (forget)", "to forget"],
            ["書く", "かく", "書 (write)", "to write"],
            ["空港", "くうこう", "空 (sky/empty) + 港 (harbor)", "airport"],
            ["着く", "つく", "着 (arrive/wear)", "to arrive"],
            ["手続き", "てつづき", "手 (hand) + 続 (continue)", "procedure"],
            ["搭乗口", "とうじょうぐち", "搭 (board) + 乗 (ride) + 口 (mouth)", "boarding gate"],
            ["待つ", "まつ", "待 (wait)", "to wait"],
            ["時間", "じかん", "時 (time) + 間 (interval)", "time"],
            ["到着", "とうちゃく", "到 (arrival) + 着 (arrive)", "arrival"],
            ["現地", "げんち", "現 (appear/current) + 地 (ground)", "local place"],
            ["天気", "てんき", "天 (sky/heaven) + 気 (energy)", "weather"],
            ["暑い", "あつい", "暑 (hot)", "hot"],
            ["部屋", "へや", "部 (part/room) + 屋 (shop)", "room"],
            ["海", "うみ", "海 (sea)", "sea"],
            ["見える", "みえる", "見 (see)", "can see / visible"],
            ["泳ぐ", "およぐ", "泳 (swim)", "to swim"],
            ["食べる", "たべる", "食 (eat)", "to eat"],
            ["親切", "しんせつ", "親 (parent) + 切 (cut/kind)", "kind"],
            ["困る", "こまる", "困 (trouble/distress)", "to be troubled"],
            ["助ける", "たすける", "助 (help)", "to help"],
            ["最終日", "さいしゅうび", "最 (most) + 終 (end) + 日 (day)", "last day"],
            ["お土産", "おみやげ", "土 (soil) + 産 (produce)", "souvenir"],
            ["買う", "かう", "買 (buy)", "to buy"],
            ["家族", "かぞく", "家 (house) + 族 (family)", "family"],
            ["渡す", "わたす", "渡 (hand over/cross)", "to hand over / give"],
            ["強く", "つよく", "強 (strong)", "strongly"],
            ["思う", "おもう", "思 (think)", "to think"],
            ["思い出", "おもいで", "思 (think) + 出 (go out)", "memory"],
            ["一生", "いっしょう", "一 (one) + 生 (life)", "entire life"],
            ["忘れられない", "わすれられない", "忘 (forget) + られ (passive) + ない", "unforgettable"],
        ],
    },
    {
        "title": "人間関係で悩んだ一年",
        "level": "N4",
        "text": (
            "去年は人間関係でとても悩んだ一年でした。"
            "新しい職場に移ったのが原因です。"
            "最初の数ヶ月は同僚と親しくなれませんでした。"
            "毎日一人で昼ご飯を食べて、休み時間も静かに過ごしました。"
            "自分から話しかけるのが苦手だからです。"
            "ある日、先輩が「一緒に食べない？」と声をかけてくれました。"
            "とても嬉しくて、すぐに「はい」と答えました。"
            "その日から、少しずつ会話が増えました。"
            "仕事の後にみんなで飲みに行くこともありました。"
            "時々意見が合わないこともありますが、話し合うようにしています。"
            "相手の気持ちを考えることが大切だと学びました。"
            "今では良い関係を築けていると思います。"
            "先月は同僚の結婚式に招待されました。"
            "式の後のパーティーでスピーチも頼まれました。"
            "緊張しましたが、心からお祝いの言葉を伝えました。"
            "人間関係は時間がかかるけど、努力すれば必ず良くなると感じています。"
        ),
        "translation": (
            "Last year was a year in which I greatly struggled with human relationships. "
            "The cause was moving to a new workplace. "
            "For the first several months, I couldn't become close with my colleagues. "
            "Every day I ate lunch alone and spent my break time quietly. "
            "That's because I'm not good at starting conversations with people. "
            "One day, a senior colleague called out to me, \"Want to eat together?\" "
            "I was very happy and immediately answered \"Yes.\" "
            "From that day, little by little, our conversations increased. "
            "Sometimes after work, I went drinking with everyone. "
            "There are times when our opinions don't match, but I make sure to discuss things. "
            "I learned that it's important to think about the other person's feelings. "
            "I think I've built good relationships now. "
            "Last month, I was invited to a colleague's wedding. "
            "After the ceremony, I was also asked to give a speech at the party. "
            "I was nervous, but I conveyed my heartfelt congratulations. "
            "I feel that although human relationships take time, they will certainly improve if you make an effort."
        ),
        "vocab": [
            ["去年", "きょねん", "去 (past) + 年 (year)", "last year"],
            ["人間関係", "にんげんかんけい", "人 (person) + 間 (space) + 関 (relation) + 係 (connection)", "human relationships"],
            ["悩む", "なやむ", "悩 (worry/anguish)", "to worry / to be troubled"],
            ["一年", "いちねん", "一 (one) + 年 (year)", "one year"],
            ["新しい", "あたらしい", "新 (new)", "new"],
            ["職場", "しょくば", "職 (job) + 場 (place)", "workplace"],
            ["移る", "うつる", "移 (move/transfer)", "to move / to transfer"],
            ["原因", "げんいん", "原 (original/cause) + 因 (cause)", "cause"],
            ["最初", "さいしょ", "最 (most) + 初 (first)", "first / beginning"],
            ["数ヶ月", "すうかげつ", "数 (number) + ヶ + 月 (month)", "several months"],
            ["同僚", "どうりょう", "同 (same) + 僚 (colleague)", "colleague"],
            ["親しい", "したしい", "親 (parent/familiar)", "close / intimate"],
            ["毎日", "まいにち", "毎 (every) + 日 (day)", "every day"],
            ["一人", "ひとり", "一 (one) + 人 (person)", "alone"],
            ["昼ご飯", "ひるごはん", "昼 (noon) + 飯 (meal)", "lunch"],
            ["食べる", "たべる", "食 (eat)", "to eat"],
            ["休み時間", "やすみじかん", "休 (rest) + 時 (time) + 間 (interval)", "break time"],
            ["静か", "しずか", "静 (quiet)", "quiet"],
            ["過ごす", "すごす", "過 (pass/spend)", "to spend (time)"],
            ["自分", "じぶん", "自 (self) + 分 (part)", "oneself"],
            ["話しかける", "はなしかける", "話 (talk) + かける (start to)", "to start talking to"],
            ["苦手", "にがて", "苦 (pain/suffer) + 手 (hand)", "weakness / not good at"],
            ["先輩", "せんぱい", "先 (previous/ahead) + 輩 (comrade)", "senior colleague"],
            ["声", "こえ", "声 (voice)", "voice"],
            ["嬉しい", "うれしい", "嬉 (glad/happy)", "happy / glad"],
            ["答える", "こたえる", "答 (answer)", "to answer"],
            ["少しずつ", "すこしずつ", "少 (few)", "little by little"],
            ["会話", "かいわ", "会 (meet) + 話 (talk)", "conversation"],
            ["増える", "ふえる", "増 (increase)", "to increase"],
            ["時々", "ときどき", "時 (time) + 々 (repetition)", "sometimes"],
            ["意見", "いけん", "意 (mind) + 見 (opinion)", "opinion"],
            ["話し合う", "はなしあう", "話 (talk) + 合 (mutually)", "to discuss"],
            ["相手", "あいて", "相 (mutual) + 手 (hand)", "partner / other person"],
            ["気持ち", "きもち", "気 (spirit) + 持 (hold)", "feelings"],
            ["考える", "かんがえる", "考 (think)", "to think"],
            ["大切", "たいせつ", "大 (big) + 切 (cut/important)", "important"],
            ["学ぶ", "まなぶ", "学 (learn)", "to learn"],
            ["良い", "よい", "良 (good)", "good"],
            ["関係", "かんけい", "関 (relation) + 係 (connection)", "relationship"],
            ["築く", "きずく", "築 (build)", "to build"],
            ["先月", "せんげつ", "先 (previous) + 月 (month)", "last month"],
            ["結婚式", "けっこんしき", "結 (tie) + 婚 (marriage) + 式 (ceremony)", "wedding ceremony"],
            ["招待", "しょうたい", "招 (invite) + 待 (wait)", "invitation"],
            ["緊張", "きんちょう", "緊 (tight) + 張 (stretch)", "nervousness / tension"],
            ["心", "こころ", "心 (heart)", "heart"],
            ["お祝い", "おいわい", "祝 (celebrate)", "celebration / congratulation"],
            ["言葉", "ことば", "言 (say) + 葉 (leaf/word)", "words"],
            ["伝える", "つたえる", "伝 (transmit)", "to convey"],
            ["努力", "どりょく", "努 (endeavor) + 力 (power)", "effort"],
            ["必ず", "かならず", "必 (certainly)", "without fail / certainly"],
            ["感じる", "かんじる", "感 (feel)", "to feel"],
        ],
    },
    {
        "title": "図書館で出会った本",
        "level": "N4",
        "text": (
            "先週の日曜日、久しぶりに図書館に行きました。"
            "目的は日本史の勉強のための資料を探すことです。"
            "図書館はとても静かで、勉強にぴったりでした。"
            "利用者は土曜日より少なくて、空いていました。"
            "私はすぐに歴史のコーナーに行きました。"
            "たくさんの本の中から、一冊の古い本に目が止まりました。"
            "題名は「日本の戦国時代」です。"
            "ページを開くと、美しい地図と写真がたくさんありました。"
            "その本はとても分かりやすく、すぐに夢中になりました。"
            "2時間ほど読んで、半分まで進みました。"
            "借りることに決めて、カウンターで手続きをしました。"
            "図書館員が「人気の本なので、返却は2週間後です」と教えてくれました。"
            "家に帰って、その本を読み続けました。"
            "寝る前の30分は必ず読むようにしています。"
            "歴史の知識が増えるのが楽しくて、毎日が充実しています。"
            "図書館は本当に素晴らしい場所だと再確認しました。"
        ),
        "translation": (
            "Last Sunday, I went to the library for the first time in a long time. "
            "My purpose was to search for materials to study Japanese history. "
            "The library was very quiet and perfect for studying. "
            "There were fewer users than on Saturdays, and it was not crowded. "
            "I immediately went to the history section. "
            "Among the many books, one old book caught my eye. "
            "The title was \"The Warring States Period of Japan.\" "
            "When I opened the pages, there were many beautiful maps and photographs. "
            "That book was very easy to understand, and I immediately became absorbed in it. "
            "I read for about 2 hours and progressed through half of it. "
            "I decided to borrow it and did the procedures at the counter. "
            "The librarian told me, \"This book is popular, so the return date is in two weeks.\" "
            "I went home and continued reading that book. "
            "I make sure to read for 30 minutes before sleeping every night. "
            "It's enjoyable that my historical knowledge increases, and every day feels fulfilling. "
            "I reconfirmed that the library is truly a wonderful place."
        ),
        "vocab": [
            ["先週", "せんしゅう", "先 (previous) + 週 (week)", "last week"],
            ["日曜日", "にちようび", "日 (sun/day) + 曜 (day of week) + 日 (day)", "Sunday"],
            ["久しぶり", "ひさしぶり", "久 (long time)", "after a long time"],
            ["図書館", "としょかん", "図 (picture/diagram) + 書 (book) + 館 (building)", "library"],
            ["行く", "いく", "行 (go)", "to go"],
            ["目的", "もくてき", "目 (eye) + 的 (target)", "purpose"],
            ["日本史", "にほんし", "日 (Japan) + 本 (origin) + 史 (history)", "Japanese history"],
            ["勉強", "べんきょう", "勉 (exertion/study) + 強 (strength)", "study"],
            ["資料", "しりょう", "資 (resources) + 料 (material)", "materials / documents"],
            ["探す", "さがす", "探 (search)", "to search"],
            ["静か", "しずか", "静 (quiet)", "quiet"],
            ["利用者", "りようしゃ", "利 (benefit/use) + 用 (use) + 者 (person)", "user"],
            ["土曜日", "どようび", "土 (earth/soil) + 曜 (day of week) + 日 (day)", "Saturday"],
            ["少ない", "すくない", "少 (few)", "few"],
            ["歴史", "れきし", "歴 (history) + 史 (history)", "history"],
            ["本", "ほん", "本 (book/origin)", "book"],
            ["古い", "ふるい", "古 (old)", "old"],
            ["止まる", "とまる", "止 (stop)", "to stop / to catch one's eye"],
            ["題名", "だいめい", "題 (title/subject) + 名 (name)", "title"],
            ["戦国時代", "せんごくじだい", "戦 (war) + 国 (country) + 時 (time) + 代 (era)", "Warring States period"],
            ["開く", "ひらく", "開 (open)", "to open"],
            ["美しい", "うつくしい", "美 (beautiful)", "beautiful"],
            ["地図", "ちず", "地 (ground) + 図 (picture/diagram)", "map"],
            ["写真", "しゃしん", "写 (copy) + 真 (truth/reality)", "photograph"],
            ["分かりやすい", "わかりやすい", "分 (understand) + やすい (easy to)", "easy to understand"],
            ["夢中", "むちゅう", "夢 (dream) + 中 (inside)", "absorbed / captivated"],
            ["読む", "よむ", "読 (read)", "to read"],
            ["半分", "はんぶん", "半 (half) + 分 (part)", "half"],
            ["進む", "すすむ", "進 (advance)", "to advance / to progress"],
            ["借りる", "かりる", "借 (borrow)", "to borrow"],
            ["決める", "きめる", "決 (decide)", "to decide"],
            ["図書館員", "としょかんいん", "図 + 書 + 館 + 員 (member)", "librarian"],
            ["人気", "にんき", "人 (person) + 気 (energy/spirit)", "popularity"],
            ["返却", "へんきゃく", "返 (return) + 却 (rejection)", "return (of borrowed item)"],
            ["帰る", "かえる", "帰 (return)", "to return home"],
            ["読み続ける", "よみつづける", "読 (read) + 続 (continue)", "to continue reading"],
            ["寝る前", "ねるまえ", "寝 (sleep) + 前 (before)", "before sleeping"],
            ["必ず", "かならず", "必 (certainly)", "without fail"],
            ["知識", "ちしき", "知 (know) + 識 (discernment)", "knowledge"],
            ["増える", "ふえる", "増 (increase)", "to increase"],
            ["楽しい", "たのしい", "楽 (comfort/ease)", "enjoyable"],
            ["毎日", "まいにち", "毎 (every) + 日 (day)", "every day"],
            ["充実", "じゅうじつ", "充 (fill) + 実 (fruit/reality)", "fulfillment"],
            ["再確認", "さいかくにん", "再 (again) + 確 (certain) + 認 (recognize)", "reconfirmation"],
        ],
    },
    {
        "title": "引っ越しで気づいたこと",
        "level": "N4",
        "text": (
            "先月、新しいアパートに引っ越しました。"
            "前の家は駅から遠くて、通勤に1時間かかりました。"
            "新しい家は駅から歩いて5分で、とても便利になりました。"
            "引っ越し業者に頼んで、荷物を運んでもらいました。"
            "業者の人は丁寧で早く、3時間で終わりました。"
            "新しい部屋は前より少し狭いですが、明るくて気持ちが良いです。"
            "引っ越しの後、いらない物をたくさん捨てました。"
            "服や本、古い家電などです。"
            "もったいないけど、スッキリしました。"
            "近所の人に挨拶に行きました。"
            "両隣と向かいの3軒に訪問しました。"
            "どの家も親切で安心しました。"
            "特に左隣のおばあさんは「困ったことがあったら何でも言って」と言ってくれました。"
            "嬉しかったです。"
            "新しい生活が始まって一ヶ月、毎日が新鮮です。"
            "前より朝早く起きられるようになりました。"
            "家の近くに公園もあって、週末は散歩を楽しんでいます。"
            "引っ越しを決めて良かったと心から思います。"
        ),
        "translation": (
            "Last month, I moved to a new apartment. "
            "My previous house was far from the station, and commuting took 1 hour. "
            "My new house is a 5-minute walk from the station, making it very convenient. "
            "I hired a moving company to transport my luggage. "
            "The movers were polite and fast, and finished in 3 hours. "
            "The new room is a little smaller than before, but it's bright and feels good. "
            "After moving, I threw away many unnecessary things. "
            "Clothes, books, old appliances, etc. "
            "It felt wasteful, but it's now clean and refreshing. "
            "I went to greet the neighbors. "
            "I visited the houses on both sides and the one across, three houses in total. "
            "Every household was kind, which was reassuring. "
            "Especially the elderly woman on my left said, \"If you have any trouble, just tell me anything.\" "
            "I was happy. "
            "One month has passed since my new life began, and every day feels fresh. "
            "I've been able to wake up earlier than before. "
            "There's also a park near my house, and on weekends I enjoy taking walks. "
            "I truly think from my heart that deciding to move was a good thing."
        ),
        "vocab": [
            ["先月", "せんげつ", "先 (previous) + 月 (month)", "last month"],
            ["新しい", "あたらしい", "新 (new)", "new"],
            ["引っ越す", "ひっこす", "引 (pull) + 越 (cross/over)", "to move (house)"],
            ["前", "まえ", "前 (before/front)", "previous / before"],
            ["家", "いえ", "家 (house)", "house"],
            ["駅", "えき", "駅 (station)", "station"],
            ["遠い", "とおい", "遠 (far/distant)", "far"],
            ["通勤", "つうきん", "通 (commute/pass) + 勤 (work)", "commuting to work"],
            ["時間", "じかん", "時 (time) + 間 (interval)", "time"],
            ["歩く", "あるく", "歩 (walk)", "to walk"],
            ["便利", "べんり", "便 (convenience) + 利 (benefit)", "convenient"],
            ["引っ越し業者", "ひっこしぎょうしゃ", "引 + 越 + 業 (business) + 者 (person)", "moving company"],
            ["頼む", "たのむ", "頼 (request)", "to request / hire"],
            ["荷物", "にもつ", "荷 (luggage) + 物 (thing)", "luggage"],
            ["運ぶ", "はこぶ", "運 (carry/luck)", "to carry / transport"],
            ["丁寧", "ていねい", "丁 (polite) + 寧 (peaceful/polite)", "polite / careful"],
            ["部屋", "へや", "部 (part/room) + 屋 (shop/roof)", "room"],
            ["狭い", "せまい", "狭 (narrow)", "narrow"],
            ["明るい", "あかるい", "明 (bright)", "bright"],
            ["気持ち", "きもち", "気 (spirit) + 持 (hold)", "feeling"],
            ["物", "もの", "物 (thing)", "thing"],
            ["捨てる", "すてる", "捨 (discard)", "to throw away"],
            ["服", "ふく", "服 (clothes)", "clothes"],
            ["古い", "ふるい", "古 (old)", "old"],
            ["家電", "かでん", "家 (house) + 電 (electricity)", "home appliance"],
            ["近所", "きんじょ", "近 (near) + 所 (place)", "neighborhood"],
            ["挨拶", "あいさつ", "挨 (open/approach) + 拶 (be near/hello)", "greeting"],
            ["両隣", "りょうどなり", "両 (both) + 隣 (next to)", "both neighbors"],
            ["向かい", "むかい", "向 (face/toward)", "opposite / across"],
            ["訪問", "ほうもん", "訪 (visit) + 問 (ask)", "visit"],
            ["特に", "とくに", "特 (special)", "especially"],
            ["困る", "こまる", "困 (trouble)", "to be troubled"],
            ["嬉しい", "うれしい", "嬉 (glad)", "happy"],
            ["生活", "せいかつ", "生 (life) + 活 (activity)", "life / living"],
            ["始まる", "はじまる", "始 (begin)", "to begin"],
            ["新鮮", "しんせん", "新 (new) + 鮮 (fresh)", "fresh / new"],
            ["朝", "あさ", "朝 (morning)", "morning"],
            ["起きる", "おきる", "起 (wake)", "to wake up"],
            ["近く", "ちかく", "近 (near)", "near"],
            ["公園", "こうえん", "公 (public) + 園 (park)", "park"],
            ["週末", "しゅうまつ", "週 (week) + 末 (end)", "weekend"],
            ["散歩", "さんぽ", "散 (scatter) + 歩 (walk)", "walk / stroll"],
            ["楽しむ", "たのしむ", "楽 (comfort)", "to enjoy"],
            ["心", "こころ", "心 (heart)", "heart"],
            ["思う", "おもう", "思 (think)", "to think"],
        ],
    },
    {
        "title": "料理教室に通う理由",
        "level": "N4",
        "text": (
            "私は今年の春から、料理教室に通っています。"
            "理由は一人暮らしを始めたからです。"
            "今まで母の料理に頼っていましたが、自分で作れるようになりたいと思いました。"
            "教室は週に1回、水曜日の夜7時からです。"
            "先生はプロの料理人で、とても優しく教えてくれます。"
            "先週は味噌汁と魚の煮物を習いました。"
            "だしの取り方から丁寧に教わりました。"
            "初めて自分で作った味噌汁は、母の味には負けるけど、美味しくできました。"
            "教室にはいろんな年齢の人が通っています。"
            "学生もいれば、60歳の男性もいます。"
            "みんな料理が好きで、楽しく話しながら作ります。"
            "家に帰ってからも復習して、家族や友達に食べてもらっています。"
            "「美味しい」と言われると、とても嬉しいです。"
            "目標は一人で晩ご飯を全部作れるようになることです。"
            "もっとレパートリーを増やして、いつか友達を家に招いて、手料理を振る舞いたいです。"
        ),
        "translation": (
            "I have been attending a cooking class since spring of this year. "
            "The reason is that I started living alone. "
            "Until now, I had relied on my mother's cooking, but I thought I wanted to become able to make it myself. "
            "The class is once a week, on Wednesday nights at 7 PM. "
            "The teacher is a professional chef who teaches very kindly. "
            "Last week, I learned how to make miso soup and simmered fish. "
            "I was carefully taught how to make broth, from the basics. "
            "The miso soup I made for the first time, although it loses compared to my mother's, turned out delicious. "
            "People of various ages attend the class. "
            "There are students, and there are also 60-year-old men. "
            "Everyone loves cooking, and we talk while enjoying making dishes. "
            "After returning home, I also review and have my family and friends eat what I made. "
            "When they tell me \"It's delicious,\" I'm very happy. "
            "My goal is to become able to make all of my own dinners. "
            "I want to increase my repertoire more and someday invite friends to my home and serve them home-cooked food."
        ),
        "vocab": [
            ["今年", "ことし", "今 (now) + 年 (year)", "this year"],
            ["春", "はる", "春 (spring)", "spring"],
            ["料理教室", "りょうりきょうしつ", "料 + 理 + 教 (teach) + 室 (room)", "cooking class"],
            ["通う", "かよう", "通 (commute/attend)", "to attend (regularly)"],
            ["理由", "りゆう", "理 (reason) + 由 (cause)", "reason"],
            ["一人暮らし", "ひとりぐらし", "一 (one) + 人 (person) + 暮 (live)", "living alone"],
            ["始める", "はじめる", "始 (begin)", "to start"],
            ["母", "はは", "母 (mother)", "mother"],
            ["料理", "りょうり", "料 (fee/material) + 理 (arrangement)", "cooking / dish"],
            ["頼る", "たよる", "頼 (rely/request)", "to rely on"],
            ["自分", "じぶん", "自 (self) + 分 (part)", "oneself"],
            ["作る", "つくる", "作 (make)", "to make"],
            ["思う", "おもう", "思 (think)", "to think"],
            ["水曜日", "すいようび", "水 (water) + 曜 + 日", "Wednesday"],
            ["夜", "よる", "夜 (night)", "night"],
            ["先生", "せんせい", "先 (previous) + 生 (life/birth)", "teacher"],
            ["料理人", "りょうりにん", "料 + 理 + 人 (person)", "cook / chef"],
            ["優しい", "やさしい", "優 (gentle/superior)", "kind / gentle"],
            ["教える", "おしえる", "教 (teach)", "to teach"],
            ["先週", "せんしゅう", "先 (previous) + 週 (week)", "last week"],
            ["味噌汁", "みそしる", "味 (taste) + 噌 + 汁 (soup)", "miso soup"],
            ["魚", "さかな", "魚 (fish)", "fish"],
            ["煮物", "にもの", "煮 (boil) + 物 (thing)", "simmered dish"],
            ["習う", "ならう", "習 (learn)", "to learn"],
            ["取り方", "とりかた", "取 (take) + 方 (way/method)", "how to take/extract"],
            ["丁寧", "ていねい", "丁 (polite) + 寧 (peaceful)", "careful / polite"],
            ["教わる", "おそわる", "教 (teach) + わる", "to be taught / to learn from"],
            ["初めて", "はじめて", "初 (first)", "for the first time"],
            ["負ける", "まける", "負 (lose/defeat)", "to lose (in comparison)"],
            ["美味しい", "おいしい", "美 (beautiful) + 味 (taste)", "delicious"],
            ["年齢", "ねんれい", "年 (year) + 齢 (age)", "age"],
            ["学生", "がくせい", "学 (study) + 生 (life)", "student"],
            ["男性", "だんせい", "男 (man) + 性 (gender/nature)", "man"],
            ["好き", "すき", "好 (like)", "like / fond of"],
            ["話す", "はなす", "話 (talk)", "to talk"],
            ["家", "いえ", "家 (house)", "house"],
            ["帰る", "かえる", "帰 (return)", "to return"],
            ["復習", "ふくしゅう", "復 (again/restore) + 習 (learn)", "review"],
            ["家族", "かぞく", "家 (house) + 族 (family)", "family"],
            ["友達", "ともだち", "友 (friend) + 達 (plural)", "friend"],
            ["嬉しい", "うれしい", "嬉 (glad)", "happy"],
            ["目標", "もくひょう", "目 (eye) + 標 (target)", "goal"],
            ["晩ご飯", "ばんごはん", "晩 (evening) + 飯 (meal)", "dinner"],
            ["全部", "ぜんぶ", "全 (all/whole) + 部 (part)", "all / everything"],
            ["増やす", "ふやす", "増 (increase)", "to increase (transitive)"],
            ["招く", "まねく", "招 (invite)", "to invite"],
            ["手料理", "てりょうり", "手 (hand) + 料 + 理", "home cooking"],
            ["振る舞う", "ふるまう", "振 (swing) + 舞 (dance)", "to serve (food/drink)"],
        ],
    },
    {
        "title": "銀行での手続き",
        "level": "N4",
        "text": (
            "先週、新しい口座を作るために銀行に行きました。"
            "今の口座は学生のときに作ったもので、今は使いにくくなったからです。"
            "銀行は家の近くにあります。"
            "午前10時に着いて、受付で用事を伝えました。"
            "係の人が「こちらにお書きください」と言って、用紙を渡しました。"
            "名前や住所、電話番号などを書きました。"
            "書いた後、機械に通して、本人確認をしました。"
            "運転免許証を見せて、問題ないと言われました。"
            "次に、暗証番号を決めました。"
            "覚えやすい番号が良いと言われて、誕生日は避けました。"
            "最後に通帳とキャッシュカードをもらいました。"
            "手続きは全部で30分ほどでした。"
            "その足でATMに行って、すぐにお金を入れてみました。"
            "ちゃんと使えて、安心しました。"
            "新しい口座ができて、気持ちが新しくなりました。"
            "これからは給料をこの口座に振り込んでもらう予定です。"
        ),
        "translation": (
            "Last week, I went to the bank to open a new account. "
            "My current account was one I opened when I was a student, and now it had become difficult to use. "
            "The bank is near my house. "
            "I arrived at 10 AM and told my business at the reception desk. "
            "The clerk said \"Please write here\" and handed me a form. "
            "I wrote my name, address, and phone number. "
            "After writing, I passed it through a machine to verify my identity. "
            "I showed my driver's license and was told there was no problem. "
            "Next, I decided on a PIN code. "
            "I was told an easy-to-remember number is good, so I avoided my birthday. "
            "Finally, I received a bankbook and cash card. "
            "The entire procedure took about 30 minutes. "
            "Right after that, I went to an ATM and tried depositing money right away. "
            "It worked properly, and I felt relieved. "
            "With my new account opened, I felt refreshed. "
            "From now on, I plan to have my salary transferred to this account."
        ),
        "vocab": [
            ["先週", "せんしゅう", "先 (previous) + 週 (week)", "last week"],
            ["新しい", "あたらしい", "新 (new)", "new"],
            ["口座", "こうざ", "口 (mouth) + 座 (seat)", "bank account"],
            ["作る", "つくる", "作 (make)", "to make / open"],
            ["銀行", "ぎんこう", "銀 (silver) + 行 (go)", "bank"],
            ["行く", "いく", "行 (go)", "to go"],
            ["学生", "がくせい", "学 (study) + 生 (life)", "student"],
            ["使いにくい", "つかいにくい", "使 (use) + にくい (difficult to)", "difficult to use"],
            ["家", "いえ", "家 (house)", "house"],
            ["近く", "ちかく", "近 (near)", "nearby"],
            ["午前", "ごぜん", "午 (noon) + 前 (before)", "morning / a.m."],
            ["着く", "つく", "着 (arrive)", "to arrive"],
            ["受付", "うけつけ", "受 (receive) + 付 (attach)", "reception desk"],
            ["用事", "ようじ", "用 (use/business) + 事 (thing)", "business / errand"],
            ["伝える", "つたえる", "伝 (transmit)", "to tell / convey"],
            ["係", "かかり", "係 (person in charge)", "clerk / attendant"],
            ["用紙", "ようし", "用 + 紙 (paper)", "form / paper"],
            ["渡す", "わたす", "渡 (hand over)", "to hand over"],
            ["名前", "なまえ", "名 (name) + 前", "name"],
            ["住所", "じゅうしょ", "住 (live) + 所 (place)", "address"],
            ["電話番号", "でんわばんごう", "電 + 話 + 番 (number) + 号 (number)", "phone number"],
            ["書く", "かく", "書 (write)", "to write"],
            ["機械", "きかい", "機 (machine) + 械 (tool)", "machine"],
            ["通す", "とおす", "通 (pass/through)", "to pass through"],
            ["本人確認", "ほんにんかくにん", "本 (origin) + 人 (person) + 確 (certain) + 認 (recognize)", "identity verification"],
            ["運転免許証", "うんてんめんきょしょう", "運 + 転 + 免 + 許 + 証", "driver's license"],
            ["見せる", "みせる", "見 (see) + せる (causative)", "to show"],
            ["問題", "もんだい", "問 (question) + 題 (topic)", "problem"],
            ["次に", "つぎに", "次 (next)", "next"],
            ["暗証番号", "あんしょうばんごう", "暗 (dark/secret) + 証 + 番 + 号", "PIN code"],
            ["決める", "きめる", "決 (decide)", "to decide"],
            ["覚えやすい", "おぼえやすい", "覚 (remember) + やすい (easy to)", "easy to remember"],
            ["誕生日", "たんじょうび", "誕 (birth) + 生 + 日 (day)", "birthday"],
            ["避ける", "さける", "避 (avoid)", "to avoid"],
            ["最後", "さいご", "最 (most) + 後 (after/end)", "finally / end"],
            ["通帳", "つうちょう", "通 + 帳 (notebook)", "bankbook"],
            ["もらう", "もらう", "-", "to receive"],
            ["手続き", "てつづき", "手 (hand) + 続 (continue)", "procedure"],
            ["全部", "ぜんぶ", "全 (whole) + 部 (part)", "all / whole"],
            ["お金", "おかね", "金 (money/gold)", "money"],
            ["入れる", "いれる", "入 (enter/put in)", "to put in / deposit"],
            ["安心", "あんしん", "安 (peaceful) + 心 (heart)", "relief"],
            ["気持ち", "きもち", "気 (spirit) + 持 (hold)", "feeling"],
            ["給料", "きゅうりょう", "給 (salary) + 料 (fee)", "salary"],
            ["振り込む", "ふりこむ", "振 (swing) + 込 (put in)", "to transfer (money)"],
            ["予定", "よてい", "予 (beforehand) + 定 (decide)", "plan / schedule"],
        ],
    },
    {
        "title": "電車で忘れ物をした日",
        "level": "N4",
        "text": (
            "先週の金曜日、仕事の帰りに電車で大切な忘れ物をしました。"
            "その日はとても疲れていて、うとうとしてしまいました。"
            "降りる駅で急いで降りたら、座っていた席に傘を置き忘れてしまいました。"
            "家に着いてから気づきました。"
            "とてもショックでした。"
            "その傘は母からもらった大切な物だからです。"
            "すぐに駅に電話しました。"
            "駅員に「傘を忘れました」と伝えると、「忘れ物の場所を確認します」と言われました。"
            "5分ほど待って、連絡が来ました。"
            "「見つかりました。改札口まで取りに来てください」と言われました。"
            "次の日の朝、駅に行って、傘を受け取りました。"
            "駅員にお礼をしっかり言いました。"
            "駅員は「お気をつけて」と笑ってくれました。"
            "それから、電車に乗るときは必ず降りる前に荷物を確認するようにしています。"
            "同じ間違いを繰り返さないために、今ではメモを貼って忘れないようにしています。"
            "親切な駅員に本当に感謝しています。"
        ),
        "translation": (
            "Last Friday, on my way home from work, I lost something precious on the train. "
            "That day I was very tired and dozed off unintentionally. "
            "When I got off in a hurry at my station, I left behind the umbrella on the seat I had been sitting on. "
            "I noticed after arriving home. "
            "I was very shocked. "
            "That's because that umbrella was something I received from my mother. "
            "I immediately called the station. "
            "When I told the station staff \"I forgot my umbrella,\" I was told \"We'll check the location of lost items.\" "
            "After waiting about 5 minutes, I received a call. "
            "I was told, \"It's been found. Please come to the ticket gate to pick it up.\" "
            "The next morning, I went to the station and received my umbrella. "
            "I properly expressed my thanks to the station staff. "
            "The station staff smiled and said, \"Please be careful.\" "
            "Since then, when I ride the train, I always check my luggage before getting off. "
            "To not repeat the same mistake, I now paste a memo to remind myself not to forget. "
            "I truly feel grateful to the kind station staff."
        ),
        "vocab": [
            ["先週", "せんしゅう", "先 (previous) + 週 (week)", "last week"],
            ["金曜日", "きんようび", "金 (gold/money) + 曜 + 日", "Friday"],
            ["仕事", "しごと", "仕 (serve) + 事 (thing)", "work"],
            ["帰り", "かえり", "帰 (return)", "on the way home"],
            ["電車", "でんしゃ", "電 (electricity) + 車 (car/vehicle)", "train"],
            ["大切な", "たいせつな", "大 (big) + 切 (cut/important)", "important / precious"],
            ["忘れ物", "わすれもの", "忘 (forget) + 物 (thing)", "lost item / forgotten item"],
            ["疲れる", "つかれる", "疲 (tired)", "to get tired"],
            ["降りる", "おりる", "降 (descend/get off)", "to get off"],
            ["駅", "えき", "駅 (station)", "station"],
            ["急ぐ", "いそぐ", "急 (hurry)", "to hurry"],
            ["座る", "すわる", "座 (sit)", "to sit"],
            ["席", "せき", "席 (seat)", "seat"],
            ["傘", "かさ", "傘 (umbrella)", "umbrella"],
            ["置き忘れる", "おきわすれる", "置 (put) + 忘 (forget)", "to leave behind / forget"],
            ["着く", "つく", "着 (arrive)", "to arrive"],
            ["気づく", "きづく", "気 (spirit) + づく (attach)", "to notice"],
            ["母", "はは", "母 (mother)", "mother"],
            ["もらう", "もらう", "-", "to receive"],
            ["すぐに", "すぐに", "-", "immediately"],
            ["電話", "でんわ", "電 (electricity) + 話 (talk)", "telephone / call"],
            ["駅員", "えきいん", "駅 (station) + 員 (member)", "station staff"],
            ["伝える", "つたえる", "伝 (transmit)", "to tell"],
            ["場所", "ばしょ", "場 (place) + 所 (place)", "place"],
            ["確認", "かくにん", "確 (certain) + 認 (recognize)", "confirmation"],
            ["待つ", "まつ", "待 (wait)", "to wait"],
            ["連絡", "れんらく", "連 (connect) + 絡 (entangle)", "contact"],
            ["来る", "くる", "来 (come)", "to come"],
            ["見つかる", "みつかる", "見 (see) + つかる", "to be found"],
            ["改札口", "かいさつぐち", "改 (revise) + 札 (ticket/tag) + 口 (opening)", "ticket gate"],
            ["取りに来る", "とりにくる", "取 (take) + 来 (come)", "to come to pick up"],
            ["次の日", "つぎのひ", "次 (next) + 日 (day)", "the next day"],
            ["朝", "あさ", "朝 (morning)", "morning"],
            ["受け取る", "うけとる", "受 (receive) + 取 (take)", "to receive"],
            ["お礼", "おれい", "礼 (thanks/bow)", "gratitude / thanks"],
            ["言う", "いう", "言 (say)", "to say"],
            ["笑う", "わらう", "笑 (laugh/smile)", "to smile"],
            ["乗る", "のる", "乗 (ride)", "to board"],
            ["必ず", "かならず", "必 (certainly)", "without fail"],
            ["荷物", "にもつ", "荷 (luggage) + 物 (thing)", "luggage"],
            ["同じ", "おなじ", "同 (same)", "same"],
            ["間違い", "まちがい", "間 (space) + 違 (different)", "mistake"],
            ["繰り返さない", "くりかえさない", "繰 (repeat) + 返 (return)", "to not repeat"],
            ["メモ", "めも", "-", "memo / note"],
            ["貼る", "はる", "貼 (paste/stick)", "to paste"],
            ["親切", "しんせつ", "親 (parent) + 切 (kind)", "kind"],
            ["本当に", "ほんとうに", "本 (true/origin) + 当 (hit/correct)", "truly / really"],
            ["感謝", "かんしゃ", "感 (feeling) + 謝 (apologize/thank)", "gratitude"],
        ],
    },
    {
        "title": "親友との約束",
        "level": "N4",
        "text": (
            "私には小学生のときからの親友がいます。"
            "名前は美咲です。"
            "彼女は今、大阪に住んでいます。"
            "私たちは毎年夏と冬に1回ずつ会う約束をしています。"
            "今年の夏は8月の連休に東京で会うことになりました。"
            "美咲が「久しぶりに一緒に旅行したい」と言ったからです。"
            "私は新幹線の切符とホテルを予約しました。"
            "美咲は美味しいレストランを調べてくれました。"
            "当日、東京駅で待ち合わせました。"
            "美咲は少し痩せて、髪も短くなっていました。"
            "それでも、笑顔は子供のときと全く変わっていませんでした。"
            "まず、浅草に行って、お寺を見学しました。"
            "次に、美味しいすし屋で昼ご飯を食べました。"
            "夜は屋形船に乗って、夜景を楽しみました。"
            "ホテルに帰ってからも、朝の3時まで話しました。"
            "仕事のこと、恋愛のこと、将来の夢など、話せば話すほど時間が足りませんでした。"
            "次の日、美咲を駅で見送りました。"
            "別れるとき少し泣いてしまいました。"
            "でも、次は冬にまた会うと約束しました。"
            "本当の友達は距離が遠くても、心は近いと感じた二日間でした。"
        ),
        "translation": (
            "I have a best friend from my elementary school days. "
            "Her name is Misaki. "
            "She currently lives in Osaka. "
            "We have a promise to meet once each summer and winter every year. "
            "This summer, it was decided that we would meet in Tokyo during the consecutive holidays in August. "
            "Misaki said, \"I want to travel together after a long time.\" "
            "I reserved the bullet train tickets and the hotel. "
            "Misaki looked up delicious restaurants for us. "
            "On the day, we met at Tokyo Station. "
            "Misaki had lost a little weight and her hair had become short. "
            "Even so, her smiling face was completely unchanged from when we were children. "
            "First, we went to Asakusa and toured the temple. "
            "Next, we ate lunch at a delicious sushi restaurant. "
            "At night, we boarded a roofed boat and enjoyed the night view. "
            "Even after returning to the hotel, we talked until 3 AM. "
            "About work, about love, about future dreams — the more we talked, the more time was insufficient. "
            "The next day, I saw Misaki off at the station. "
            "When we parted, I unintentionally cried a little. "
            "But we promised to meet again in winter. "
            "A true friend is someone you feel is close in heart even when the distance is far — that's what I felt during those two days."
        ),
        "vocab": [
            ["私", "わたし", "私 (I/private)", "I"],
            ["小学生", "しょうがくせい", "小 (small) + 学 (study) + 生 (student)", "elementary school student"],
            ["親友", "しんゆう", "親 (parent/familiar) + 友 (friend)", "best friend / close friend"],
            ["名前", "なまえ", "名 (name) + 前", "name"],
            ["彼女", "かのじょ", "彼 (he/that) + 女 (woman)", "she / girlfriend"],
            ["大阪", "おおさか", "大 (big) + 阪 (slope)", "Osaka"],
            ["住む", "すむ", "住 (live)", "to live"],
            ["私たち", "わたしたち", "私 (I) + たち (plural)", "we"],
            ["毎年", "まいとし", "毎 (every) + 年 (year)", "every year"],
            ["夏", "なつ", "夏 (summer)", "summer"],
            ["冬", "ふゆ", "冬 (winter)", "winter"],
            ["会う", "あう", "会 (meet)", "to meet"],
            ["約束", "やくそく", "約 (promise) + 束 (bundle)", "promise"],
            ["今年", "ことし", "今 (now) + 年 (year)", "this year"],
            ["連休", "れんきゅう", "連 (connect) + 休 (rest)", "consecutive holidays"],
            ["東京", "とうきょう", "東 (east) + 京 (capital)", "Tokyo"],
            ["久しぶり", "ひさしぶり", "久 (long time)", "after a long time"],
            ["一緒に", "いっしょに", "一 (one) + 緒 (together)", "together"],
            ["旅行", "りょこう", "旅 (travel) + 行 (go)", "travel"],
            ["言う", "いう", "言 (say)", "to say"],
            ["新幹線", "しんかんせん", "新 (new) + 幹 (trunk/main) + 線 (line)", "bullet train"],
            ["切符", "きっぷ", "切 (cut) + 符 (ticket)", "ticket"],
            ["予約", "よやく", "予 (beforehand) + 約 (promise)", "reservation"],
            ["美味しい", "おいしい", "美 (beautiful) + 味 (taste)", "delicious"],
            ["調べる", "しらべる", "調 (investigate)", "to look up / research"],
            ["当日", "とうじつ", "当 (hit/appropriate) + 日 (day)", "the day (of event)"],
            ["東京駅", "とうきょうえき", "東 + 京 + 駅 (station)", "Tokyo Station"],
            ["待ち合わせ", "まちあわせ", "待 (wait) + 合 (mutually)", "meeting up / arrangement"],
            ["少し", "すこし", "少 (few)", "a little"],
            ["痩せる", "やせる", "痩 (thin/lose weight)", "to lose weight"],
            ["髪", "かみ", "髪 (hair)", "hair"],
            ["短い", "みじかい", "短 (short)", "short"],
            ["笑顔", "えがお", "笑 (laugh/smile) + 顔 (face)", "smiling face"],
            ["子供", "こども", "子 (child) + 供 (provide/companion)", "child"],
            ["全く", "まったく", "全 (whole)", "completely / at all"],
            ["変わらない", "かわらない", "変 (change) + わらない (negative)", "unchanged"],
            ["浅草", "あさくさ", "浅 (shallow) + 草 (grass)", "Asakusa"],
            ["お寺", "おてら", "寺 (temple)", "temple"],
            ["見学", "けんがく", "見 (see) + 学 (learn)", "observation / tour"],
            ["すし屋", "すしや", "寿司 (sushi) + 屋 (shop)", "sushi restaurant"],
            ["昼ご飯", "ひるごはん", "昼 (noon) + 飯 (meal)", "lunch"],
            ["食べる", "たべる", "食 (eat)", "to eat"],
            ["夜", "よる", "夜 (night)", "night"],
            ["屋形船", "やかたぶね", "屋 (roof/shop) + 形 (shape) + 船 (boat)", "roofed pleasure boat"],
            ["乗る", "のる", "乗 (ride)", "to board"],
            ["夜景", "やけい", "夜 (night) + 景 (scenery)", "night view"],
            ["楽しむ", "たのしむ", "楽 (comfort)", "to enjoy"],
            ["帰る", "かえる", "帰 (return)", "to return"],
            ["話す", "はなす", "話 (talk)", "to talk"],
            ["恋愛", "れんあい", "恋 (love) + 愛 (affection)", "romantic love"],
            ["将来", "しょうらい", "将 (future/leader) + 来 (come)", "future"],
            ["夢", "ゆめ", "夢 (dream)", "dream"],
            ["時間", "じかん", "時 (time) + 間 (interval)", "time"],
            ["足りない", "たりない", "足 (sufficient)", "insufficient"],
            ["次の日", "つぎのひ", "次 (next) + 日 (day)", "the next day"],
            ["見送る", "みおくる", "見 (see) + 送 (send)", "to see off"],
            ["別れる", "わかれる", "別 (separate)", "to part / separate"],
            ["泣く", "なく", "泣 (cry)", "to cry"],
            ["本当", "ほんとう", "本 (true/origin) + 当 (hit/correct)", "real / true"],
            ["友達", "ともだち", "友 (friend) + 達 (plural)", "friend"],
            ["距離", "きょり", "距 (distance) + 離 (separate)", "distance"],
            ["心", "こころ", "心 (heart)", "heart"],
            ["近い", "ちかい", "近 (near)", "near"],
            ["感じる", "かんじる", "感 (feel)", "to feel"],
            ["二日間", "ふつかかん", "二 (two) + 日 (day) + 間 (interval)", "two days"],
        ],
    },
]
