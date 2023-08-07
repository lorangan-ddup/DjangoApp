from django.http import HttpResponse
def index(request):
    line1 = '<h1 style="text-align:center">《终端上的宝让我想念》</h1>'
    line2 = '<img src="http://p1.music.126.net/pWOtcm_t041hKMu_0s1blA==/109951168715909095.jpg?param=177y177" width=600>'
    return HttpResponse(line1+line2)
# Create your views here.
