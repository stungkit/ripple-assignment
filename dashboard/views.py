from django.shortcuts import render
from django.http import HttpResponse
from .models import UserIP
import datetime
import json


# Create your views here.
def index(request):
	if request.is_ajax():
		queried_data = UserIP.objects.filter(ip_address=request.GET["current_ip_address"]).values("datetime", "frequency").order_by("datetime")
		json_response = {"data": []}
		for entry in queried_data:
			# json.dumps() cannot serialize datetime object so we need .isoformat() to conver it to String			
			if isinstance(entry["datetime"] , datetime.datetime) is True:
				# Works in sqlite3	
				formatted_datetime = entry["datetime"].strftime("%b %d, %Y at %I:%M:%S %p")
			else:
				# Works in PostgreSQL
				formatted_datetime = datetime.datetime.strptime(entry["datetime"], "%Y-%m-%d %H:%M:%S").strftime("%b %d, %Y at %I:%M:%S %p")
			json_response["data"].append([formatted_datetime, entry["frequency"]])
		return HttpResponse(json.dumps(json_response), content_type='application/json')

	unique_ips = UserIP.objects.values("ip_address").distinct().order_by("ip_address")
	all_entries = UserIP.objects.all()
	return render(request, "index.html", {"unique_ips": unique_ips, "all_entries": all_entries})
