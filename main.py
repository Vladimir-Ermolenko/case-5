"""Case-study #4 Анализ текста
Разработчики:
Ермоленко В.М. - 40%, Шарков К.Д. - 40% , Кеда C.В. - 30%
"""

from textblob import TextBlob
import string

lang = input('Enter the language you are going to work in(en, ru): ')
if lang == 'ru':
    import locru as loc
elif lang == 'en':
    import locen as loc

text_inp = input(loc.ENTER)

count_english = 0
count_russian = 0
for i in text_inp:
    if i in "abcdefghijklmnopqrstuvwxyz":
        count_english += 1
    elif i in "абвгдеёжзийклмнопрстуфхцчшщьыъэюя":
        count_russian += 1
if count_russian > count_english:
    language_text = "ru"
else:
    language_text = "eng"

if language_text == "eng":
    def slbl_cnt(word):
        word = word.lower()
        cnt = 0
        vwls = 'aeiouy'
        if word[0] in vwls:
            cnt += 1
        for ltr_nbr in range(1, len(word)):
            if word[ltr_nbr] in vwls and word[ltr_nbr - 1] not in vwls:
                cnt += 1
        if word.endswith('e'):
            cnt -= 1
        if cnt == 0:
            cnt += 1
        return cnt


    text = TextBlob(text_inp)
    term_list = [loc.SENTENCES, loc.WORDS, loc.SYLLABLE, loc.ASL, loc.ASW,
                 loc.FRE, loc.TON, loc.OBJ]
    fnl_slbl_qnt = 0
    for ltr_cnt in range(len(text.words)):
        slbls_in_word = slbl_cnt(text.words[ltr_cnt])
        fnl_slbl_qnt += slbls_in_word

    avg_stn_ln = len(text.words) / len(text.sentences)
    avg_wd_ln = fnl_slbl_qnt / len(text.words)
    fre = 206.835 - 1.015 * avg_stn_ln - 84.6 * avg_wd_ln

    mood_int = text.sentiment.polarity
    if mood_int <= -0.5:
        mood = loc.TON_1
    elif mood_int <= 0.5:
        mood = loc.TON_2
    elif mood_int <= 1:
        mood = loc.TON_3

    subj = str(text.sentiment.subjectivity * 100.0) + '%'

    dcr_val = [len(text.sentences), len(text.words), fnl_slbl_qnt, avg_stn_ln, avg_wd_ln, fre, mood, subj]

    for stn_nbr in range(8):
        print(term_list[stn_nbr], dcr_val[stn_nbr])
        if stn_nbr == 5:
            if fre >= 100:
                print(loc.TEXT_1)
            elif fre >= 65:
                print(loc.TEXT_2)
            elif fre >= 30:
                print(loc.TEXT_3)
            elif fre >= 0:
                print(loc.TEXT_4)
            else:
                print(loc.TEXT_4)
if language_text == "ru":
    punctuation_marks = ['.', '?', '!']
    sentences = []
    words = []
    count_syllables = 0
    prev_puncs = 0
    ruvowels = ['ё', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и']

    for i in range(len(text_inp)):
        if text_inp[i] in punctuation_marks:
            sentences.append(text_inp[prev_puncs:i])         # Finding sentences
            prev_puncs = i + 2
    count_sentences = len(sentences)

    mod_text = text_inp
    for char in mod_text:
        if char in string.punctuation:                    # Finding words
            mod_text = mod_text.replace(char, '')
    words = mod_text.split()
    count_words = len(words)

    for i in range(len(text_inp)):
        if text_inp[i].lower() in ruvowels:
            count_syllables += 1

    ASL = count_words / count_sentences
    ASW = count_syllables / count_words
    FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)
    print(loc.SENTENCES, count_sentences)
    print(loc.WORDS, count_words)
    print(loc.SYLLABLE, count_syllables)
    print(loc.ASL, ASL)
    print(loc.ASW, ASW)
    print(loc.FRE, FRE)
    if FRE > 80:
        print(loc.TEXT_1)
    elif FRE > 25:
        print(loc.TEXT_2)
    elif FRE > 25:
        print(loc.TEXT_3)
    else:
        print(loc.TEXT_4)
