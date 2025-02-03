from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_hi', 'answer_hi', 'question_bn', 'answer_bn']


    def to_representation(self, instance):
        lang = self.context.get('lang', 'en')
        translated_text = instance.get_translated_text(lang)
        return {
            'id': instance.id,
            'question': translated_text['question'],
            'answer': translated_text['answer']
        }