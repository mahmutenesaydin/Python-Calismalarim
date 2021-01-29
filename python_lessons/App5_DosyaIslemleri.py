"""courses = [Python, CSharp, SQL, HTML, CSS, JavaScripts, MVC, WCF]
               liste elemanlarını bir dosyaya alt alta yazdırınız 
"""

courses = ['Python', 'CSharp', 'SQL', 'HTML', 'CSS', 'JavaScripts', 'MVC', 'WCF']

with open('AppDosyaIslem', 'w') as myFile:
    for course in courses:
        myFile.write(f'{course}\n')