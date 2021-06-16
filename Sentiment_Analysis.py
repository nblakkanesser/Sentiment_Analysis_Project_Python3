
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word=word.replace(char,"")
        else:
            word=word
    return(word)
            
def get_pos(sentence):
    sentence=sentence.split(" ")
    count=0
    for word in sentence:
        word=strip_punctuation(word).lower()
        if word in positive_words:
            count=count+1
    return(count)

def get_neg(sentence):
    sentence=sentence.split(" ")
    count=0
    for word in sentence:
        word=strip_punctuation(word).lower()
        if word in negative_words:
            count=count+1
    return(count)

newfile = open('resulting_data.csv','w')
newfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
newfile.write('\n')

project_data = open('project_twitter_data.csv','r')
rows = project_data.readlines()[1:]
for line in rows:
    values = line.split(",")
    Retweets = int(values[1])
    Replies = int(values[2])
    Positive = get_pos(values[0])
    Negative = get_neg(values[0])
    Net = Positive - Negative
    
    row_string = '{}, {}, {}, {}, {}'.format(Retweets, Replies, Positive, Negative, Net)
    print(row_string)
    newfile.write(row_string)
    newfile.write('\n')

newfile.close()


