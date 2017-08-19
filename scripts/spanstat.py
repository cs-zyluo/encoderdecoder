import codecs
import collections

def most_common_span(fns):
    spans = []
    for fn in fns:
        spans.extend(codecs.open(fn, encoding='utf-8').readlines())
    d = collections.Counter(spans)
    return d.most_common(len(d))

def stat_common_span(fns, outfn):
    stat = most_common_span(fns)
    with codecs.open(outfn, 'w', encoding='utf-8') as outf:
        for span, cnt in stat:
            outf.write(str(cnt)+'\t'+span)

stat_common_span(['/home/zhiyi/temp/opennmt/OpenNMT-py/wikidata/because/4-10/cause-train.txt', \
        '/home/zhiyi/temp/opennmt/OpenNMT-py/wikidata/because/4-10/effect-train.txt', \
        '/home/zhiyi/temp/opennmt/OpenNMT-py/wikidata/because/4-10/cause-val.txt', \
        '/home/zhiyi/temp/opennmt/OpenNMT-py/wikidata/because/4-10/effect-val.txt'], 'common_spans.txt')



