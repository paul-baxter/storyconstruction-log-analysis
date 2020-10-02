import sys
import getopt
import os
import re
import numpy

###
### Very basic word frequency script, with descriptive stats
###
### removal of common/irrelevant words in "common" list
###

def main(argv):

    inputfile = 'allTTS.dat'   #default
    outputfile = 'ttsAnalysed.dat' #default
    numwords = 10   # default number of keywords to find

    try:
        opts, args = getopt.getopt(argv[1:], 'hi:n:', ['help', 'input=', 'numwords='])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit()

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-i', '--input'):
            inputfile = arg
        elif opt in ('-n', '--numwords'):
            numwords = int(arg)

    lineWordCount = 0
    lineNumbers = numpy.array([])
    words = {}
    delims = " ", ", ", "-", "\n", ".", "?", "!"            #delimiters
    regexPattern = '|'.join(map(re.escape, delims))     #regular expression
    if os.path.exists(inputfile):
        try:
            datafile = open(inputfile, 'r')
            for line in datafile:
                splitLine = re.split(regexPattern, line)
                #if splitLine[0] == '':
                    #continue
                lineWordCount += len(splitLine)
                lineNumbers = numpy.append(lineNumbers, [len(splitLine)])
                record_word_cnt(splitLine, words)
        finally:
            datafile.close()
    else:
        print('File does not exist: ', inputfile)
        sys.exit()

    remove_common(words)
    sorted_words = order_bag_of_words(words, desc=True)
    rankedwords = sorted_words[:numwords]

    print '\tNumber of lines read: ', len(lineNumbers)
    print '\tTotal words: ', numpy.sum(lineNumbers)
    print '\tMean words per line: ', numpy.mean(lineNumbers)
    print '\tStdev words per line: ', numpy.std(lineNumbers, ddof=1) #sample stdev
    print '\tMost frequent', numwords, 'words {}'.format(sorted_words[:numwords])
    print ''

    try:
        outfile = open(outputfile, "w")
        outfile.write('lines,' + str(len(lineNumbers)) + '\n')
        outfile.write('words,' + str(numpy.sum(lineNumbers)) + '\n')
        outfile.write('mean_words,' + str(numpy.mean(lineNumbers)) + '\n')
        outfile.write('stdev_words,' + str(numpy.std(lineNumbers, ddof=1)) + '\n')
        outfile.write('top ' + str(numwords) + ' words\n')
        for line in rankedwords:
            outfile.write(str(line[0]) + ',' + str(line[1]) + '\n')
    except err:
        print(err)
    finally:
        outfile.close()


#####################################################################

def usage():
    print('Usage: text-analysis.py -i <inputfile.csv> -n <numWords>')

#order_bag_of_words and record_word_cnt based on
# http://stackabuse.com/read-a-file-line-by-line-in-python/

def order_bag_of_words(bag_of_words, desc=False):
   words = [(word, cnt) for word, cnt in bag_of_words.items()]
   return sorted(words, key=lambda x: x[1], reverse=desc)

def record_word_cnt(words, bag_of_words):
   for word in words:
       if word != '':
           if word.lower() in bag_of_words:
               bag_of_words[word.lower()] += 1
           else:
               bag_of_words[word.lower()] = 1

def remove_common(words):
    common = ['a','to','the','and','lot','that','but','is','are','of','it']
    for word in words.keys():
        for commonword in common:
            if word == commonword:
                del words[commonword]

if __name__ == "__main__":
    main(sys.argv)
