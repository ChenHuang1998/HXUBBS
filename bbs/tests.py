from django.test import TestCase
from django.contrib.auth.models import User
from time import sleep
from django.utils import timezone
from django.urls import reverse
from bbs.models import *
class PostViewTests(TestCase):

    def test_increase_views(self):
        # 请求详情视图时，阅读量 +1
        author = User(username='admin1', password='admin')
        author.save()
        UserProfile.objects.create(user=author)
        cate = Category.objects.create(name='test')
        Theme.objects.create(name='test', category=cate)
        post = Post(
            author= UserProfile.objects.get(id=1),
            title='test1',
            category_id='1',
            theme_id='1',
            content='test1',
            )
        post.save()
        self.assertIs(post.read_num, 0)

        url = reverse('postdetail', args=(post.id,))
        response = self.client.get(url)

        viewed_article = Post.objects.get(id=post.id)
        self.assertIs(viewed_article.read_num, 1)

    def test_increase_views_but_not_change_updated_field(self):
        # 请求详情视图时，不改变 updated 字段
        author = User(username='user2', password='test_password')
        author.save()
        user = UserProfile.objects.create(user=author)
        cate = Category.objects.create(name='test')
        Theme.objects.create(name='test',category=cate)
        post = Post(
            author=user,
            title='test2',
            content='test2',
            category_id='1',
            theme_id='1',

            )
        post.save()

        sleep(0.5)

        url = reverse('postdetail', args=(post.id,))
        response = self.client.get(url)

        viewed_article = Post.objects.get(id=post.id)
        self.assertIs(viewed_article.modify_time - viewed_article.created_time < timezone.timedelta(seconds=0.1), True)
# Create your tests here.
