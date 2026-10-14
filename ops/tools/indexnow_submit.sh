#!/bin/bash
# usage: indexnow_submit.sh HOST KEY
H=$1; K=$2
python3 - "$H" "$K" > /tmp/in-$H.json <<'P'
import sys,re,json,urllib.request
h,k=sys.argv[1:]
sm=urllib.request.urlopen(f"https://{h}/sitemap.xml").read().decode()
urls=[u for u in re.findall(r"<loc>([^<]+)</loc>",sm) if urllib.parse.urlparse(u).hostname==h]
print(json.dumps({"host":h,"key":k,"keyLocation":f"https://{h}/{k}.txt","urlList":urls}))
P
echo "$H urls=$(jq '.urlList|length' /tmp/in-$H.json)"
for e in https://api.indexnow.org/indexnow https://www.bing.com/indexnow; do echo "  $e $(curl -s -o /tmp/in.out -w '%{http_code}' -H 'Content-Type: application/json; charset=utf-8' -X POST $e --data @/tmp/in-$H.json) $(head -c 150 /tmp/in.out)"; done
