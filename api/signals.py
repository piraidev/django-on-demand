import django.dispatch

mentorship_requested = django.dispatch.Signal(providing_args=["from_user", "to_user"])

mentorship_cancelled = django.dispatch.Signal(providing_args=["from_user", "to_user", "role_to_notify", "mentorship_cancelled"])

mentorship_finished = django.dispatch.Signal(providing_args=["from_user", "to_user", "mentorship", "mentor_ranking"])

mentorship_accepted = django.dispatch.Signal(providing_args=["from_user", "to_user", "mentorship"])

mentorship_rejected = django.dispatch.Signal(providing_args=["from_user", "to_user", "mentorship", "rejection_reason"])