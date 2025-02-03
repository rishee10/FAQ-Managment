from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from .models import FAQ

class FAQViewTest(TestCase):
    
    def setUp(self):
        """
        Create some FAQs to test the view.
        """
        FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")
        FAQ.objects.create(question="What is Python?", answer="Python is a programming language.")
    
    def test_faq_list_view(self):
        """
        Test the faq_list view to ensure it returns a valid response and renders the correct data.
        """
        
        response = self.client.get(reverse('faq_list'))  
        
        
        self.assertEqual(response.status_code, 200)
        
       
        self.assertContains(response, "What is Django?")
        self.assertContains(response, "Django is a web framework.")
        self.assertContains(response, "What is Python?")
        self.assertContains(response, "Python is a programming language.")
        
        
        self.assertIn('faqs', response.context)
        self.assertEqual(len(response.context['faqs']), 2) 


class FAQDetailViewTest(TestCase):
    
    def setUp(self):
        # Set up initial data: Create a FAQ object for testing
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a Python framework.")

    def test_faq_detail_valid(self):
        # Construct the URL for the faq_detail view with the valid pk
        url = reverse('faq_detail', kwargs={'pk': self.faq.pk})

        # Send a GET request to the URL
        response = self.client.get(url)

        # Ensure the response status is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Ensure the correct template is used
        self.assertTemplateUsed(response, 'faq_detail.html')

        # Ensure the correct FAQ object is passed in the context
        self.assertEqual(response.context['faq'], self.faq)

    def test_faq_detail_invalid_pk(self):
        # Construct the URL with an invalid pk (non-existent FAQ)
        url = reverse('faq_detail', kwargs={'pk': 999})  # Assuming FAQ with pk 999 does not exist
        
        # Send a GET request to the URL
        response = self.client.get(url)
        
        # Ensure the response status is 404 (Not Found)
        self.assertEqual(response.status_code, 404)


class FAQCreateViewTest(TestCase):
    
    def test_faq_create_get(self):
        # Send a GET request to the FAQ create page
        response = self.client.get(reverse('faq_create'))

        # Ensure the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Ensure the correct template is used
        self.assertTemplateUsed(response, 'faq_create.html')

        # Ensure the form is included in the context
        self.assertIn('form', response.context)

    



from django.test import TestCase
from django.urls import reverse
from .models import FAQ

class FAQUpdateViewTest(TestCase):

    def setUp(self):
        # Create an FAQ object for testing
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")
        self.url = reverse('faq_update', kwargs={'pk': self.faq.pk})

    def test_faq_update_get(self):
        # Send a GET request to the FAQ update page
        response = self.client.get(self.url)

        # Ensure the response status is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Ensure the correct template is used
        self.assertTemplateUsed(response, 'faq_update.html')

        # Ensure the form contains the current FAQ data
        self.assertEqual(response.context['form'].initial['question'], self.faq.question)
        self.assertEqual(response.context['form'].initial['answer'], self.faq.answer)

    def test_faq_update_valid_post(self):
        # Define valid data for the form
        data = {
            'question': 'What is Django?',
            'answer': 'Django is a Python-based web framework.',
        }

        # Send a POST request to the FAQ update page with valid data
        response = self.client.post(self.url, data)

        # Ensure the FAQ object is updated in the database
        self.faq.refresh_from_db()
        self.assertEqual(self.faq.question, 'What is Django?')
        self.assertEqual(self.faq.answer, 'Django is a Python-based web framework.')

        # Ensure the user is redirected to the faq_list page
        self.assertRedirects(response, reverse('faq_list'))
    

    
from django.test import TestCase
from django.urls import reverse
from .models import FAQ

class FAQDeleteViewTest(TestCase):
    
    def setUp(self):
        # Create an FAQ object for testing
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")
        self.url = reverse('faq_delete', kwargs={'pk': self.faq.pk})

    def test_faq_delete_get(self):
        # Send a GET request to the FAQ delete page
        response = self.client.get(self.url)

        # Ensure the response status is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Ensure the correct template is used
        self.assertTemplateUsed(response, 'faq_delete.html')

        # Ensure the correct FAQ is passed to the context
        self.assertEqual(response.context['faq'], self.faq)

    def test_faq_delete_post(self):
        # Send a POST request to the FAQ delete page
        response = self.client.post(self.url)

        # Ensure the FAQ object is deleted from the database
        self.assertEqual(FAQ.objects.count(), 0)

        # Ensure the user is redirected to the faq_list page
        self.assertRedirects(response, reverse('faq_list'))













    
