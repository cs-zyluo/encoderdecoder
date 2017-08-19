import os
import re
import codecs
import jieba
import numpy as np

def copyTextFileTo(fn, outf, logfn=False):
    if logfn: outf.write('\n\n\n####################################\n'+fn+'\n####################################\n')
    with codecs.open(fn, encoding='utf-8') as f:
        for line in f: outf.write(line)

def collectAssoData2File(source_dirs, outputfns, fnprefixs=None, filepats=[ re.compile('\w+\.txt$')]):
    """
    >>> collectAssoData2File(source_dir, outputfn)
    """
    for source_dir in source_dirs:
        if not os.path.exists(source_dir):
            raise ValueError("Not found {}".format(source_dir))
    outfs = [ codecs.open(outputfn, 'w', encoding='utf-8') for outputfn in outputfns]
    outf = outfs[0]
    sdir0 = source_dirs[0]

    for path, dirlist, filelist in os.walk(sdir0):
        for filename in filelist:
            if any([pat.match(filename) for pat in filepats]):
                filenames = [filename.replace(fnprefixs[0], prefix, 1) for prefix in fnprefixs]
                for i,sdir in enumerate(source_dirs):
                    fn = os.path.join( path.replace(sdir0, sdir, 1), filenames[i] )
                    copyTextFileTo(fn, outfs[i])
    for outf in outfs: outf.close()
    
## combine crawled data into single file
#source_dirs = ['/home/zhiyi/Projects/nmt4ccpoetry/data/chines_poems', '/home/zhiyi/Projects/nmt4ccpoetry/data/chines_translation','/home/zhiyi/Projects/nmt4ccpoetry/data/eng_translation']
#outputfns = ['/home/zhiyi/Projects/nmt4ccpoetry/opennmt/OpenNMT-py/poedata/src.txt', '/home/zhiyi/Projects/nmt4ccpoetry/opennmt/OpenNMT-py/poedata/ch_tgt.txt', '/home/zhiyi/Projects/nmt4ccpoetry/opennmt/OpenNMT-py/poedata/eng_tgt.txt']
#prefixs = ['cp', 'ct', 'et']
#collectAssoData2File(source_dirs, outputfns, prefixs)

# split data into train and val
def splitAssoData(fns, prop, label1='train', label2='val'):
    np.random.seed(541)
    if len(fns) == 0: return
    lens = [len(file(fn).readlines()) for fn in fns]
    for l in lens:
        assert( l == lens[0] )
    indices = np.arange(lens[0])
    np.random.shuffle(indices)
    splitpoint = int((lens[0]-1) * prop)
    trainidx = set(indices[:splitpoint])
    validx = set(indices[splitpoint:])
    print len(trainidx)
    print len(validx)
    for fn in fns:
        cnt = 0
        prefix, suffix = os.path.splitext(fn)
        trainfn = prefix + '-{}'.format(label1) + suffix
        valfn = prefix + '-{}'.format(label2) + suffix
        with codecs.open(fn, encoding='utf-8') as f, codecs.open(trainfn, 'w', encoding='utf-8') as outf1, codecs.open(valfn, 'w', encoding='utf-8') as outf2:
            for line in f:
                if cnt in trainidx:
                    outf1.write(line)
                else:
                    outf2.write(line)
                cnt += 1

#splitAssoData(['/home/zhiyi/Projects/nmt4ccpoetry/opennmt/OpenNMT-py/poedata/src.txt', '/home/zhiyi/Projects/nmt4ccpoetry/opennmt/OpenNMT-py/poedata/ch_tgt.txt'], 0.9)

def gentokens(fns):
    for fn in fns:
        prefix, suffix = os.path.split(fn)
        outfn = os.path.join(prefix, 't' + suffix)
        print outfn
        with codecs.open(fn, encoding='utf-8') as f, codecs.open(outfn, 'w', encoding='utf-8') as outf:
            for line in f:
                outf.write( ' '.join( list( jieba.cut(line.strip()) ) ) + '\n' )

#gentokens(['/home/zhiyi/Projects/nmt4ccpoetry/opennmt/OpenNMT-py/poedata/src.txt', '/home/zhiyi/Projects/nmt4ccpoetry/opennmt/OpenNMT-py/poedata/ch_tgt.txt','/home/zhiyi/Projects/nmt4ccpoetry/opennmt/OpenNMT-py/poedata/eng_tgt.txt'])
#splitAssoData(['cnetdata/cause.txt', 'cnetdata/effect.txt'], 0.9)

