# -*- coding: utf-8 -*-
import hashlib
import sys

if(len(sys.argv)!=2):
    print >> sys.stderr, '읽을 파일명 또는 파일 경로를 입력해 주세요' # print red error, division error and text
    exit(1)

f = open(sys.argv[1], 'rb')
data = f.read()
f.close()

print 'md5: ' + hashlib.md5(data).hexdigest()

