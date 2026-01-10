you must have version 3.10 of python installed
to run, type `pip install -r requirements.txt`

then you should be able to run `python3 main.py "[acc_mail_addr]"`, make sure that the addr is in quotes

it will bring up a browser window with the account signed in

also don't forget to go into .env.example and replace [YOUR_PASSWORD] with your password and run `mv .env.example .env`

the xpath bookmarklet is:
```javascript
javascript:(function(){function getXPath(el){if(el===document.body)return'/html/body';if(el.id)return"//*[@id='"+el.id+"']";var ix=0;var siblings=el.parentNode?el.parentNode.children:[];for(var i=0;i<siblings.length;i++){var sib=siblings[i];if(sib===el)return getXPath(el.parentNode)+'/'+el.tagName.toLowerCase()+'['+(ix+1)+']';if(sib.tagName===el.tagName)ix++;}return'';}let box=document.createElement('div');box.style.cssText='position:fixed;z-index:2147483647;background:rgba(20,20,20,.9);color:#fff;font:12px monospace;padding:6px 8px;border-radius:6px;pointer-events:none;';document.body.appendChild(box);let lastXpath='';document.addEventListener('mousemove',e=>{let el=e.target;if(!el||el===document) return;let xp=getXPath(el);lastXpath=xp;box.textContent=xp;box.style.left=(e.clientX+12)+'px';box.style.top=(e.clientY+12)+'px';});document.addEventListener('keydown',async e=>{if(e.key.toLowerCase()==='c'&&lastXpath){try{await navigator.clipboard.writeText(lastXpath);box.textContent='Copied! '+lastXpath;}catch(err){box.textContent='Clipboard blocked: '+lastXpath;}}});})();
```