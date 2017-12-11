#!/usr/bin/env bash
#
# Runs the English PCFG parser on one or more files, printing trees only

if [ ! $# -ge 1 ]; then
  echo Usage: `basename $0` 'file(s)'
  echo
  exit
fi

scriptdir=`dirname $0`

## English
# java -mx150m -cp "$scriptdir/*:" edu.stanford.nlp.parser.lexparser.LexicalizedParser \
#  -outputFormat "penn,typedDependencies" edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz $*

## Chinese Lexparer
java -mx2g -cp "$scriptdir/*:" edu.stanford.nlp.parser.lexparser.LexicalizedParser \
-encoding utf-8 edu/stanford/nlp/models/lexparser/chineseFactored.ser.gz $*

## Chinese Lexparer with segmenter
# java -mx500m -cp "$scriptdir/*:" edu.stanford.nlp.parser.lexparser.LexicalizedParser \
# -encoding utf-8 edu/stanford/nlp/models/lexparser/xinhuaFactoredSegmenting.ser.gz $*

## NNDEP
## from http://stackoverflow.com/questions/33294148/how-to-use-nndep-parser-in-stanford-parser-to-process-chinese-data
## have not able to make it work
# java -cp "./*" edu.stanford.nlp.parser.nndep.DependencyParser -language chinese -model edu/stanford/nlp/models/parser/nndep/CTB_CoNLL_params.txt.gz -tagger.model edu/stanford/nlp/models/pos-tagger/chinese-distsim/chinese-distsim.tagger -escaper edu.stanford.nlp.trees.international.pennchinese.ChineseEscaper -textFile INPUT_FILE

# java -Xmx6g -cp "*:." -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -file sample_chinese_text.txt -props StanfordCoreNLP-chinese.properties -outputFormat text -parse.originalDependencies
