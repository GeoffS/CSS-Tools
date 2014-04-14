'''
Created on Apr 13, 2014

@author: Geoff
'''

import re
from test.test_pprint import set2

htmlClassRe = re.compile(r"class=\"(.*?)\"")
htmlIdRe    = re.compile(r"id=\"(.*?)\"")

cssClassRe  = re.compile(r"\.(\w+)")
cssIdRe     = re.compile(r"#(\w+)")

hexRe = re.compile(R"^[0-9a-fA-F]{6,6}$")

spaceRe = re.compile(r"\s.")
commaRe = re.compile(r",\s*")


def extractHtml(fileName, itemRe):
    itemSet = set()
    for line in open(fileName, 'r'):
        itemLists = itemRe.findall(line)
        for itemList in itemLists:
            for item in [s.strip() for s in spaceRe.split(itemList)]:
                itemSet.add(item)
    return itemSet


def extractCss(fileName, itemRe):
    itemSet = set()
    for line in open(fileName, 'r'):
        items = itemRe.findall(line)
        for item in items:
            if hexRe.match(item) == None:
                itemSet.add(item)
    return itemSet


def union(setDict):
    unionSet = set()
    for s in setDict.values():
        unionSet = unionSet.union(s)
    return unionSet


def set2sortedList(s):
    l = list(s)
    l.sort()
    return l


if __name__ == '__main__':
    topDir = r"C:\Users\Geoff\AppData\Local\Temp"
    
    exportDir = r"\AgWPGExport-66"
    
    htmlFiles = [r"\index.html", r"\content\IMG_6644_large.html", r"\content\IMG_6646_large.html"]
    nHtml = len(htmlFiles)
    
    cssFiles = [r"\content\custom.css", r"\resources\css\master.css"]
    nCss = len(cssFiles)
    
    print "Export Dir: "+exportDir
    
    htmlClasseSets = {}
    htmlIdSets = {}
    for f in htmlFiles:
        htmlClasseSets[f] = extractHtml( topDir+exportDir+f, htmlClassRe)
        htmlIdSets[f]     = extractHtml( topDir+exportDir+f, htmlIdRe)
    
    allHtmlClasses = union(htmlClasseSets)
    print "\nHTML Classes:", ', '.join(set2sortedList(allHtmlClasses))
    for f, s in htmlClasseSets.items():
        l = list(s)
        l.sort()
        print "   "+f+": "+', '.join(l)

    allHtmlIds = union(htmlIdSets)
    print "\n\nHTML Ids:", ', '.join(set2sortedList(allHtmlIds))
    for f, s in htmlIdSets.items():
        l = list(s)
        l.sort()
        print "   "+f+": "+', '.join(l)
        

    cssClasseSets = {}
    cssIdSets = {}
    for f in cssFiles:
        cssClasseSets[f] = extractCss( topDir+exportDir+f, cssClassRe)
        cssIdSets[f] = extractCss( topDir+exportDir+f, cssIdRe)
    
    allCssClasses = union(cssClasseSets)
    print "\n\nCSS Classes:", ', '.join(set2sortedList(allCssClasses))
    for f, s in cssClasseSets.items():
        l = list(s)
        l.sort()
        print "   "+f+": "+', '.join(l)

    allCssIds = union(cssIdSets)
    print "\n\nCSS Ids:", ', '.join(set2sortedList(allCssIds))
    for f, s in cssIdSets.items():
        l = list(s)
        l.sort()
        print "   "+f+": "+', '.join(l)
    
    
    print "\n\n==========================================\n"
    
    print "Unused classes in CSS:", allCssClasses.difference(allHtmlClasses)
    print "Unused ids in CSS:", allCssIds.difference(allHtmlIds)
    
    print "\n-----------\n"
    
    missingClasses = allHtmlClasses.difference(allCssClasses)
    print "Classes in HTML not found in CSS:", missingClasses
    for c in missingClasses:
        for f, s in htmlClasseSets.items():
            if c in s:
                print "   "+c+" is in "+f
        
                    
                
    
    
    
    
    