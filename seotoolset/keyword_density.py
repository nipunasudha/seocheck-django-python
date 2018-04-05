import operator
import re
from seotoolset.clean_text import *

regex = re.compile('[^a-zA-Z]')
stop_words = ["a", "about", "above", "across", "after", "afterwards", "again", "against", "ago", "all", "almost",
              "alone",
              "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an",
              "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "around", "as",
              "at", "back", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand",
              "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom", "but",
              "by", "call", "can", "cannot", "cant", "co", "computer", "con", "could", "couldnt", "cry", "de",
              "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven",
              "else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything",
              "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for",
              "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go",
              "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon",
              "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "i", "ie", "if", "in", "inc",
              "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least",
              "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover",
              "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never",
              "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now",
              "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others",
              "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps", "please", "put",
              "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she",
              "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone",
              "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than",
              "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby",
              "therefore", "therein", "thereupon", "these", "they", "thick", "thin", "third", "this", "those", "though",
              "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards",
              "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well",
              "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby",
              "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole",
              "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours",
              "yourself", "yourselves"]


def get_keyword_density(url):
    words = {}
    clean_text = get_clean_text(url)
    clean_text = regex.sub(' ', clean_text)
    print("Started word counting")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print(clean_text)
    count = 0
    for word in clean_text.split():
        count += 1
        word = word.lower()
        if word in stop_words: continue
        if len(word) < 2: continue
        if word in words:
            words[word] = words.get(word) + 1
        else:
            words[word] = 1
    # print(words)
    # print(list(reversed(sorted(words.items(), key=operator.itemgetter(1)))))
    if count == 0:
        return {}
    else:
        # return list(reversed(sorted(words.items(), key=operator.itemgetter(1))))
        return list([k, words[k]] for k in sorted(words, key=words.get, reverse=True))[:5]
