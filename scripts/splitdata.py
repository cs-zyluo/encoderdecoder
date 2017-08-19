from preprocess import *

#splitAssoData(['/home/zhiyi/temp/opennmt/OpenNMT-py/wikidata/because/short4-10_because_cause', '/home/zhiyi/temp/opennmt/OpenNMT-py/wikidata/because/short4-10_because_effect'], 0.8)
#splitAssoData(['/home/zhiyi/temp/opennmt/OpenNMT-py/wikidata/because/short4-10_because_cause-val', '/home/zhiyi/temp/opennmt/OpenNMT-py/wikidata/because/short4-10_because_effect-val'], 0.5)

splitAssoData(['/home/zhiyi/temp/opennmt/OpenNMT-py/wikicnetdata/cause.txt', '/home/zhiyi/temp/opennmt/OpenNMT-py/wikicnetdata/effect.txt'], 0.8)
splitAssoData(['/home/zhiyi/temp/opennmt/OpenNMT-py/wikicnetdata/cause-val.txt', '/home/zhiyi/temp/opennmt/OpenNMT-py/wikicnetdata/effect-val.txt'], 0.5)

