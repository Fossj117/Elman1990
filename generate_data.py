import random
import csv 

#dictionary for choosing examples from a category
cat_to_ex = {'NOUN-HUM': ['man', 'woman'],
             'NOUN-ANIM': ['cat', 'mouse'],
             'NOUN-INANIM': ['book', 'rock'],
             'NOUN-AGRESS': ['dragon', 'monster'],
             'NOUN-FRAG': ['glass', 'plate'],
             'NOUN-FOOD': ['cookie', 'break'],
             'VERB-TRAN': ['see', 'chase'],
             'VERB-INTRAN': ['think', 'sleep'],
             'VERB-AGPAT': ['move', 'break'],
             'VERB-PERCEPT': ['smell', 'see'],
             'VERB-DESTROY': ['break', 'smash'],
             'VERB-EAT': ['eat']
             }

def load_sentence_templates(path_to_csv):
    template_list = []
    with open(path_to_csv, 'rb') as f:
        rdr = csv.reader(f)
        for line in rdr: 
            line = [w.strip() for w in line]
            template_list.append(line)
    return template_list

def generate_sentences(sentence_temps, cat_to_ex, num):
    sent_stream = []
    #for each sentence to generate
    for i in xrange(num):
        sent_temp = random.choice(sentence_temps)
        for word in sent_temp:
            if word is '':
                continue 
            sent_stream.append(random.choice(cat_to_ex[word]))
    return sent_stream

if __name__ == "__main__":
    sent_temps = load_sentence_templates('sent_temps.csv')
    
    print "Generating sentences"
    random.seed(117)
    x = generate_sentences(sent_temps, cat_to_ex, 10000)
    print "Length of generated dataset is %d" % len(x)
   
    with open('dataset.txt', 'wb') as f:
        f.write(' '.join(x))
