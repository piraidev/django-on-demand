import django.dispatch

connection_requested = django.dispatch.Signal(providing_args=["from_user", "to_user"])

connection_cancelled = django.dispatch.Signal(providing_args=["from_user", "to_user", "role_to_notify", "connection_cancelled"])

connection_finished = django.dispatch.Signal(providing_args=["from_user", "to_user", "connection", "supplier_ranking"])

connection_accepted = django.dispatch.Signal(providing_args=["from_user", "to_user", "connection"])

connection_rejected = django.dispatch.Signal(providing_args=["from_user", "to_user", "connection", "rejection_reason"])