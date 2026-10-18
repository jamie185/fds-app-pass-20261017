# Builds index.html (GitHub Pages) from src.html + copy.json (rendered from the live template code).
import re,json
s=open('src.html').read()
icons=dict(re.findall(r"\n (\w+):'(<svg.*?</svg>)'",s))
head,script=s.split('<script>',1)
head=re.sub(r'\b(SMS|MAIL|PUSH|APP|AVA|OK|GIFT|WAIT)_I\b',lambda m:icons[m.group(1).lower()],head)
out=head+'<script>'+script.replace('COPY_JSON',json.dumps(json.load(open('copy.json'))))
page=out.replace('IMG/','../img/').replace('body{margin:0}','body{margin:0;padding:28px 18px 40px;background:#fff}')
open('index.html','w').write(page)
open('/tmp/flowgen/render.html','w').write(out.replace('IMG/','/home/jamie/Codebase/fds-app-pass-20261017/explainer/site/img/'))
