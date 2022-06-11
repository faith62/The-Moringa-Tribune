from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

class EditorTestClass(TestCase):

    #set up method
    def setUp(self):  # allows us to create an instance of the Editor class before every test.
        self.faith = Editor(first_name = 'faith',last_name='mumus', email='mumus@gmail.com')

    # Testing  instance
    def test_instance(self): #confirm that the object is being instantiated correctly.
        self.assertTrue(isinstance(self.faith,Editor))

    #testing save method
    def test_save_method(self):
        self.faith.save_editor()
        editors =Editor.objects.all()
        self.assertTrue(len(editors)>0)

class tagsTestClass(TestCase):

    def setUp(self):
        self.business = tags(name = 'business')

    def test_instance(self):
        self.assertTrue(isinstance(self.business, tags))

    def test_save_method(self):
        self.business.save_tags()
        tag = tags.objects.all()
        self.assertTrue(len(tag)>0)

class ArticleTestClass(TestCase): #define a new Editor and tag instance.

    def setUp(self):
        # Creating a new editor and saving it
        self.faith= Editor(first_name = 'faith', last_name ='mumus', email ='mumus@gmail.com')
        self.faith.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.faith)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self): #allow us to delete all instances of our models from the database after each test.
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

    

# 1. Test for deleting a model object.

# 2. Test for displaying all model objects saved.

# 3. Test for updating single object properties.
