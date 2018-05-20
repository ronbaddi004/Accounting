from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    url(r'^$',
        login_required(views.DashboardView.as_view()),
        name="dashboard"),

    # Organizations
    url(r'^organization/$',
        login_required(views.OrganizationListView.as_view()),
        name="organization-list"),
    url(r'^organization/selector/$',
        login_required(views.OrganizationSelectorView.as_view()),
        name="organization-selector"),
    url(r'^organization/create/$',
        login_required(views.OrganizationCreateView.as_view()),
        name="organization-create"),
    url(r'^organization/(?P<pk>\d+)/edit/$',
        login_required(views.OrganizationUpdateView.as_view()),
        name="organization-edit"),
    url(r'^organization/(?P<pk>\d+)/detail/$',
        login_required(views.OrganizationDetailView.as_view()),
        name="organization-detail"),
    url(r'^organization/(?P<pk>\d+)/select/$',
        login_required(views.OrganizationSelectionView.as_view()),
        name="organization-select"),

    # Tax Rates
    url(r'^tax_rates/$',
        login_required(views.TaxRateListView.as_view()),
        name="tax_rate-list"),
    url(r'^tax_rates/create/$',
        login_required(views.TaxRateCreateView.as_view()),
        name="tax_rate-create"),
    url(r'^tax_rates/(?P<pk>\d+)/edit/$',
        login_required(views.TaxRateUpdateView.as_view()),
        name="tax_rate-edit"),
    url(r'^tax_rates/(?P<pk>\d+)/delete/$',
        login_required(views.TaxRateDeleteView.as_view()),
        name="tax_rate-delete"),

    # Estimates
    url(r'^estimate/$',
        login_required(views.EstimateListView.as_view()),
        name="estimate-list"),
    url(r'^estimate/create/$',
        login_required(views.EstimateCreateView.as_view()),
        name="estimate-create"),
    url(r'^estimate/(?P<pk>\d+)/edit/$',
        login_required(views.EstimateUpdateView.as_view()),
        name="estimate-edit"),
    url(r'^estimate/(?P<pk>\d+)/delete/$',
        login_required(views.EstimateDeleteView.as_view()),
        name="estimate-delete"),
    url(r'^estimate/(?P<pk>\d+)/detail/$',
        login_required(views.EstimateDetailView.as_view()),
        name="estimate-detail"),

    # Invoices
    url(r'^invoice/$',
        login_required(views.InvoiceListView.as_view()),
        name="invoice-list"),
    url(r'^invoice/create/$',
        login_required(views.InvoiceCreateView.as_view()),
        name="invoice-create"),
    url(r'^invoice/(?P<pk>\d+)/edit/$',
        login_required(views.InvoiceUpdateView.as_view()),
        name="invoice-edit"),
    url(r'^invoice/(?P<pk>\d+)/delete/$',
        login_required(views.InvoiceDeleteView.as_view()),
        name="invoice-delete"),
    url(r'^invoice/(?P<pk>\d+)/detail/$',
        login_required(views.InvoiceDetailView.as_view()),
        name="invoice-detail"),

    # Bills
    url(r'^bill/$',
        login_required(views.BillListView.as_view()),
        name="bill-list"),
    url(r'^bill/create/$',
        login_required(views.BillCreateView.as_view()),
        name="bill-create"),
    url(r'^bill/(?P<pk>\d+)/edit/$',
        login_required(views.BillUpdateView.as_view()),
        name="bill-edit"),
    url(r'^bill/(?P<pk>\d+)/delete/$',
        login_required(views.BillDeleteView.as_view()),
        name="bill-delete"),
    url(r'^bill/(?P<pk>\d+)/detail/$',
        login_required(views.BillDetailView.as_view()),
        name="bill-detail"),

    # ExpenseClaims
    url(r'^expense-claim/$',
        login_required(views.ExpenseClaimListView.as_view()),
        name="expense_claim-list"),
    url(r'^expense-claim/create/$',
        login_required(views.ExpenseClaimCreateView.as_view()),
        name="expense_claim-create"),
    url(r'^expense-claim/(?P<pk>\d+)/edit/$',
        login_required(views.ExpenseClaimUpdateView.as_view()),
        name="expense_claim-edit"),
    url(r'^expense-claim/(?P<pk>\d+)/delete/$',
        login_required(views.ExpenseClaimDeleteView.as_view()),
        name="expense_claim-delete"),
    url(r'^expense-claim/(?P<pk>\d+)/detail/$',
        login_required(views.ExpenseClaimDetailView.as_view()),
        name="expense_claim-detail"),

    # Payments
    url(r'^payment/(?P<pk>\d+)/edit/$',
        login_required(views.PaymentUpdateView.as_view()),
        name="payment-edit"),
    url(r'^payment/(?P<pk>\d+)/delete/$',
        login_required(views.PaymentDeleteView.as_view()),
        name="payment-delete"),

    # Items
    url(r'^item/$', views.item_list, name="item-list"),
    url(r'^item/create/$', views.item_create, name="item-create"),
    url(r'^item/(?P<pk>\d+)/edit/$', login_required(views.ItemUpdateView.as_view()), name="item-edit"),
    url(r'^item/(?P<pk>\d+)/delete/$', views.item_delete, name="item-delete"),

    # ajax urls
    url(r'^ajax/item/autocomplete/$', views.item_autocomplete, name='item-autocomplete'),
    url(r'^ajax/item/get-id/', views.item_get_data, name='item-get-data'),
]
