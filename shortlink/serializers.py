from rest_framework import serializers
from .models import Link, Click

# 1. Сериализатор для одного клика
class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = ['ip_address', 'created_at']  # User-Agent пока не берем, он длинный

# 2. основной сериализатор
class LinkSerializer(serializers.ModelSerializer):
    # Добавляем поле, которое вернет список кликов из функции get_recent_clicks
    recent_clicks = serializers.SerializerMethodField()

    class Meta:
        model = Link
        fields = ['id', 'url', 'title', 'clicks', 'recent_clicks'] # Добавь recent_clicks сюда

    # Функция, которая берет последние 5 кликов
    def get_recent_clicks(self, obj):
        clicks = obj.click_history.order_by('-created_at')[:5]
        return ClickSerializer(clicks, many=True).data