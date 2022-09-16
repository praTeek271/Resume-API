from django.http import HttpResponse

def index(request):
    html='''<html>
    <body>
    <div class="container" 
    style="
        align-content: center;
        display: flex;
        justify-content: space-around;
        margin-top: 20rem;
        font-size: 47px;
        ">
    <a href="/api/">Api Page</a>
    </div>
    </body>
    </html>'''
    return(HttpResponse(html))