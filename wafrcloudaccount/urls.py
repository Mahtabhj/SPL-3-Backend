from django.urls import path
from rest_framework.routers import DefaultRouter
from wafrcloudaccount.views.add_aws_accounts import AwsAccountViewSet
from wafrcloudaccount.views.get_billing_accounts import GetBillingDataAPIView

router = DefaultRouter()
router.register(r'aws-accounts', AwsAccountViewSet)

urlpatterns = [
                path('get-billing-data/', GetBillingDataAPIView.as_view()),
              ] + router.urls