import codecs

def build_pattern_dict():
    patd = dict()
    for i in xrange(112):
        if 0<= i <= 4:
            patd[i] = 'cause'
        elif 5<= i <= 9:
            patd[i] = 'lead_to'
        elif 36<= i <= 37:
            patd[i] = 'dut_to'
        elif 25<= i <=30:
            patd[i] = 'because'
        else:
            pass
    return patd
        
sep = '\t#######\t'
patd = build_pattern_dict()

def selectSents(start, end, pattern, filename):
    """
    select sentences with certain pattern
    Params:
        start: start idx of pattern in patternMap.txt
        end: end idx of pattern in patternMap.txt
        pattern: a certain pattern, e.g. 'because'
        filename: the input filename 
    """
    outcfn = pattern+'_cause'
    outefn = pattern+'_effect'
    with codecs.open(filename, encoding='utf-8') as f, \
            codecs.open(outcfn, 'w', encoding='utf-8') as outcf, \
            codecs.open(outefn, 'w', encoding='utf-8') as outef:
        for line in f:
            span, idx = line.strip().rsplit('\t', 1)
            idx = int(idx)
            if start<= idx <=end:
                cause,effect = span.split(sep)
                outcf.write(cause+'\n')
                outef.write(effect +'\n')
            
# selectSents(25, 30, 'because', '/home/jessie/2017/causal/preprocess/result/span/wiki_articles_span.txt')

def selectShortSents(startlen, endlen, cfn, efn):
    outcfn = 'short{}-{}_'.format(startlen, endlen) + cfn 
    outefn = 'short{}-{}_'.format(startlen, endlen) + efn
    with codecs.open(cfn, encoding='utf-8') as cf, codecs.open(efn, encoding='utf-8') as ef,\
            codecs.open(outcfn, 'w', encoding='utf-8') as outcf, \
            codecs.open(outefn, 'w', encoding='utf-8') as outef:
                for cause in cf:
                    cause = cause.strip().strip(' .')
                    effect = ef.readline().strip().strip(' .')
                    clen = len(cause.split())
                    elen = len(effect.split())
                    if startlen <= clen <= endlen and startlen <= elen <= endlen :
                        outcf.write(cause+'\n')
                        outef.write(effect+'\n')

selectShortSents(4, 10, 'because_cause', 'because_effect')
selectShortSents(4, 15, 'because_cause', 'because_effect')
selectShortSents(4, 20, 'because_cause', 'because_effect')
selectShortSents(4, 25, 'because_cause', 'because_effect')
    
