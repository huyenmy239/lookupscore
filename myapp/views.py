from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def index(request):
    return render(request, "index.html")

def score(request):
    is_available = 1
    id = request.POST["id"]
    year = request.POST.get("year")
    
    url = "https://diemthi.vnanet.vn/Home/SearchBySobaodanh"
    payload = {
        "code": id,
        "nam": year
    }
    response = requests.get(url, params = payload)
    data = json.loads(response.content)
        
    if data["result"]:
        result = data["result"][0]
            
        raw_data = {
            "ID": id,
            "Toan": result["Toan"],
            "Van": result["NguVan"],
            "NgoaiNgu": result["NgoaiNgu"],
            "Ly": result["VatLi"],
            "Hoa": result["HoaHoc"],
            "Sinh": result["SinhHoc"],
            "Su": result["LichSu"],
            "Dia": result["DiaLi"],
            "GDCD": result["GDCD"],
        }
            
        return render(request, "score.html", raw_data)
    else:
        is_available = 0
        return render(request, "index.html", {"is_available": is_available})