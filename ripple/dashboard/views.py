from django.shortcuts import render
from django.http import HttpResponse
from .models import UserIP
import json


# Create your views here.
def index(request):
	if request.is_ajax():
		queried_data = UserIP.objects.filter(ip_address=request.GET["current_ip_address"]).values("datetime", "frequency")
		json_response = {"data": []}
		for entry in queried_data:
			# json.dumps() cannot serialize datetime object so we need .isoformat() to conver it to String
			json_response["data"].append([entry["datetime"].isoformat(), entry["frequency"]])
		return HttpResponse(json.dumps(json_response), content_type='application/json')

	unique_ips = UserIP.objects.values("ip_address").distinct().order_by("ip_address")
	all_entries = UserIP.objects.all()
	return render(request, "index.html", {"unique_ips": unique_ips, "all_entries": all_entries})




# <!-- {% for entry in all_entries %}
# 	<p>IP Address: {{entry.ip_address}} Time: {{entry.datetime}} Frequency: {{entry.frequency}}<p>
# {% endfor %}
#  -->

