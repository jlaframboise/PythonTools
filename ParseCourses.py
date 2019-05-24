import re


class Course:



    def __init__(self, cName, cNum, units, name):
        self.cName = cName
        self.cNum = cNum
        self.units = units
        self.name = name

        self.prerecs = []
        self.corecs = []
        self.desc = ""
        self.exclusions = []
        self.oneExclusions = []
        self.reccomendations = []
        self.notes = []
        self.learnHours = 0
#[a-zA-Z\\s]+

def parseList(fName):
    f = open(fName, 'r', encoding='utf-8')
    text = ''.join(f.readlines())
    #courses = re.split("[\n]([A-Z]{4} \d{3}/[\d]{1,2}.0    [a-zA-Z\\s]+)[\n]", text, )
    courses = re.split("(LEARNING HOURS|[A-Z]{5,}|NOTE)", text)

    #for course in courses:
        #print(course)
    # for line in lines[10]:
    #     print(line)

    return courses

def parseCourse(course):
    print(course)
    # cName = course[0:4]
    # cNum = course[5:8]
    # print(cName)
    # print(cNum)

if __name__ == '__main__':
    courses = parseList('coursetextraw.txt')
    for course in courses:
        parseCourse(course)