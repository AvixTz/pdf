import base64
t=open('merger-template.html',encoding='utf-8').read()
r=lambda p:open(p,encoding='utf-8').read()
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
for k,v in [('/*PDFLIB*/',r('pl/package/dist/pdf-lib.min.js')),('/*PDFJS*/',r('pj/package/build/pdf.min.js')),('/*PDFWORKER*/',r('pj/package/build/pdf.worker.min.js')),('/*PAKO*/',r('libs/pako/package/dist/pako.min.js')),('/*UTIF*/',r('libs/utif-3.1.0/package/UTIF.js')),('/*HEIC*/',r('libs/heic2any-0.0.4/package/dist/heic2any.min.js')),('/*FONTKIT*/',r('libs/pdf-lib-fontkit-1.1.1/package/dist/fontkit.umd.min.js')),('/*HEEBO*/',b('libs/expo-google-fonts-heebo-0.2.3/package/Heebo_400Regular.ttf')),('/*HEEBOB*/',b('libs/expo-google-fonts-heebo-0.2.3/package/Heebo_700Bold.ttf'))]:
    assert k in t, k; t=t.replace(k,v,1)
open('index.html','w',encoding='utf-8').write(t)
print(round(len(t.encode())/1e6,2),'MB')
