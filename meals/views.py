
urlpatterns = [
    path('admin/', admin.site.urls),
    path('meals/', include('meals.urls')),
]
