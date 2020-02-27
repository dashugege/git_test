import binascii, os
import hashlib


def getFilesize(path):
    try:
        if os.path.isdir(path):
            files = os.listdir(path)
            for file in files:
                getFilesize(path + "/" + file)
        else:
            if '.DS_Store' in path: return
            if '.git' in path: return
            if '/build' in path: return
            if '/jniLibs' in path: return
            if '/assets' in path: return
            if '.gradle' in path: return
            if 'styles' in path: return
            if 'attrs' in path: return
            if '/string.xml' in path: return

            size = os.path.getsize(path)
            if not filesizes.has_key(size):
                filesizes[size] = []
            filesizes[size].append(path)
    except Exception as e:
        print e
        errfile.append(path)


def getSizeEq(filesizes):
    for key in filesizes.keys():
        if len(filesizes[key]) <= 1:
            # print filesizes[key]
            filesizes.pop(key)
    return filesizes;


def getFileHash(files):
    srcl = open(files, 'rb')
    m2 = hashlib.md5()
    m2.update(srcl.read())
    srcl.close()
    return m2.hexdigest()


def getCrc32(files):
    f = open(files, "r")
    crc = binascii.crc32(f.read())
    f.close()
    return crc


def Eq(val1, val2):
    if val1 == val2:
        return True
    return False


#######################
filesizes = {}
Eqlfiles = {}
errfile = []
path = "/Users/muhanxi/muhanxi/as_dict/SY/soyoung_main"

getFilesize(path)
filesizes = getSizeEq(filesizes)
for key in filesizes:
    files = filesizes[key]
    for i in files:
        md5a = getFileHash(i)
        crca = getCrc32(i)
        if Eqlfiles.has_key(md5a):
            if i in Eqlfiles[md5a]:
                continue
        for j in files:
            if files.index(i) > files.index(j):
                md5b = getFileHash(j)
                crcb = getCrc32(j)
                if Eq(md5a, md5b) and Eq(crca, crcb):
                    if not Eqlfiles.has_key(md5a):
                        Eqlfiles[md5a] = []
                    if i not in Eqlfiles[str(md5a)]:
                        Eqlfiles[str(md5a)].append(i)
                    if j not in Eqlfiles[str(md5a)]:
                        Eqlfiles[str(md5a)].append(j)

print u'error file:', errfile

for key in Eqlfiles:
    # print '----------------------------this duplicate files----------------------------------------'
    for i in Eqlfiles[key]:
        print 'file', i, key
