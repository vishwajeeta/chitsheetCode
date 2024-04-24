--------------- (root) -------------------------------
>vercel.json 
{
"version":2,
"builds":[
{
"src":"<root>/wsgi.py",
"use":"@vercel/python",
"config":{ "maxLamdbaSize":"15mb","runtime":"python3.9"}
},
{
"src":"build_files.sh",
"use":"@vercel/static-build",
"config":{
"distDir":"staticfiles_build"
}
}
],

"routes":[
{

"src":"/static/(.*)",
"dest":"/static/$1"
},
{
"src":"/(.*)",
"dest":"<root>/wsgi.py"
}
]
}




>build_files.sh

echo "Build Start"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "Build End"


>wsgi.py

app = application


>settings.py

ALLOWED_HOST=['.vercel.app','.now.sh']

import os
STATICFILES_DIRS=os.path.join(BASE_DIR,'static'),
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles_build','static')
