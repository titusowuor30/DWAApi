from django.db.models import Count, Case, When
from django.http import JsonResponse
from .models import *
from authman.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import permissions, authentication
from rest_framework.response import Response
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response


class CountyConcodance(APIView):
    permission_classes = [permissions.AllowAny,]
    #authentication_classes = ()
    # Fetch the data and group by concordance categories

    def get(self, request, format=None):
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        category = request.query_params.get('category')
        data = []
        print(request.user)
        if request.user.is_authenticated:
            assigned_counties = RoleScreens.objects.filter(
                role_id__in=request.user.groups.all()).values("counties__name")
            if category.lower() == 'all':
                data = final_comparison_data.objects.filter(create_date__gte=from_date, create_date__lte=to_date, county__in=assigned_counties).values('county').annotate(
                    less_90=Count(Case(When(concodance__lt=0.9, then=1))),
                    between_90_100=Count(Case(When(concodance__gte=0.9, concodance__lte=1, then=1))),
                    more_100=Count(Case(When(concodance__gt=1, then=1)))
                ).order_by("-county")
            else:
                data = final_comparison_data.objects.filter(create_date__gte=from_date, create_date__lte=to_date, category=category, county__in=assigned_counties).values('county').annotate(
                    less_90=Count(Case(When(concodance__lt=0.90, then=1))),
                    between_90_100=Count(Case(When(concodance__gte=0.90, concodance__lte=1, then=1))),
                    more_100=Count(Case(When(concodance__gt=1, then=1)))).order_by("-county")
        else:
            if category.lower() == 'all':
                data = final_comparison_data.objects.filter(create_date__gte=from_date, create_date__lte=to_date).values('county').annotate(
                    less_90=Count(Case(When(concodance__lt=0.9, then=1))),
                    between_90_100=Count(Case(When(concodance__gte=0.9, concodance__lte=1, then=1))),
                    more_100=Count(Case(When(concodance__gt=1, then=1)))
                ).order_by("-county")
            else:
                data = final_comparison_data.objects.filter(create_date__gte=from_date, create_date__lte=to_date, category=category).values('county').annotate(
                    less_90=Count(Case(When(concodance__lt=0.9, then=1))),
                    between_90_100=Count(
                        Case(When(concodance__gte=0.90, concodance__lte=1, then=1))),
                    more_100=Count(Case(When(concodance__gt=1, then=1)))).order_by("-county")
        return Response(list(data))


class FaciltyConcodance(APIView):
    permission_classes = [permissions.AllowAny,]
    #authentication_classes = ()

    def get(self, request, format=None):
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        category = request.query_params.get('category')
        data = []
        if request.user.is_authenticated:
            assigned_facilities = RoleScreens.objects.filter(
                role_id__in=request.user.groups.all()).values("facilities__name")
            if category.lower() == 'all':
                data = [[float("{:.2f}".format(float(p['concodance']))), float("{:.2f}".format(float(p['concodance'])))] for p in final_comparison_data.objects.filter(
                    create_date__range=[from_date, to_date], facility__in=assigned_facilities).values('weight', 'concodance',)]
            else:
                data = [[float("{:.2f}".format(float(p['concodance']))), float("{:.2f}".format(float(p['concodance'])))] for p in final_comparison_data.objects.filter(
                    create_date__range=[from_date, to_date], category=category, facility__in=assigned_facilities).values('weight', 'concodance')]
        return Response(list(data))


class AssetsCount(APIView):
    permission_classes = [permissions.AllowAny,]
    #authentication_classes = ()

    def get(self, request, format=None):
        data = []
        if request.user.is_authenticated:
            assigned_facilities = RoleScreens.objects.filter(
                role_id__in=request.user.groups.all()).values("facilities__name")
            assigned_counties = RoleScreens.objects.filter(
                role_id__in=request.user.groups.all()).values("counties__name")
            print(assigned_counties)
            facilities_count = Facilities.objects.filter(
                name__in=assigned_facilities).count()
            counties_count = counties.objects.filter(
                name__in=assigned_counties).count()
            data.append({"facilities": facilities_count,
                        "counties": counties_count})
        else:
            facilities = Facilities.objects.count()
            counties_count = counties.objects.count()
            data.append({"facilities": facilities,
                        "counties": counties_count})
        return Response(data)
