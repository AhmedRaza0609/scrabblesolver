import streamlit as st
def scrabble(deck):
    answer = []
    wordstxt = open('sowpods.txt', 'r').read()
    deck = deck.upper()
    count = {}
    ans = {}
    returnlist = []
    fin = ''
    score = {'A' : 1,
        'B' : 3,
        'C' : 3,
        'D' : 2,
        'E' : 1,
        'F' : 4,
        'G' : 2,
        'H' : 4,
        'I' : 1,
        'J' : 8,
        'K' : 5,
        'L' : 1,
        'M' : 3,
        'N' : 1,
        'O' : 1,
        'P' : 3,
        'Q' : 10,
        'R' : 1,
        'S' : 1,
        'T' : 1,
        'U' : 1,
        'V' : 4,
        'W' : 4,
        'X' : 8,
        'Y' : 4,
        'Z' : 8
    }
    for letter in deck:
        count[letter] = count.get(letter, 0) + 1
    key= list(count.keys())
    lines = wordstxt.split()
    for line in lines:
        temporarynum = 0
        countline = {}
        line.strip()
        if len(line) <= len(deck):
            for letter in line:
                countline[letter] = countline.get(letter, 0) + 1
            for letter in line:
                try:
                    if countline[letter] <= count[letter]:
                        temporarynum += 1
                except:
                    pass
            if temporarynum == len(line):
                answer.append(line)

    for word in answer:
        scorew = 0
        for letter in word:
            scorew += score[letter]
        ans[word] = scorew
    final = sorted(ans.items(), key=lambda x: x[1], reverse=True)
    for i in final:
        returnlist.append(f'{i[0]} {i[1]}')



    return returnlist


resultword = []
score =[]
st.title("Scrabble Solver")
st.header('By Ahmed Raza')
st.text('')
audio_file = open('rickrolling.mp3', 'rb')
st.audio(audio_file, format='audio/ogg', start_time=0)
st.text('')

title = st.text_input('Enter the letters in your deck', 'Hello World!', max_chars = 15)

if st.button('Submit'):
    if len(title) == 0:
        st.warning('Please input atleast one character')
    for word in scrabble(title):
        splitted = word.split()
        resultword.append(splitted[0])
        score.append(int(splitted[1]))
else:
    pass

if len(resultword) > 0:
    st.write('Possible words:')
    hef = st.dataframe({
          'Word': resultword,
          'Score': score,
      }, width = 250, height = 200)
else:
    pass
