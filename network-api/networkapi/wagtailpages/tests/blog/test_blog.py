import http

import wagtail_factories
from django import test
from django.core import exceptions
from taggit import models as tag_models
from wagtail import models as wagtail_models

from networkapi.wagtailpages.factory import homepage as home_factory
from networkapi.wagtailpages.factory import blog as blog_factory



class TestBlogPage(test.TestCase):
    @classmethod
    def setUpTestData(cls):
        root_node = wagtail_models.Page.get_first_root_node()
        site = wagtail_models.Site.objects.get(is_default_site=True)
        cls.homepage = home_factory.WagtailHomepageFactory(parent=root_node)
        site.root_page = cls.homepage
        site.clean()
        site.save()
        cls.blog_index = blog_factory.BlogIndexPageFactory(parent=cls.homepage)
        cls.blog_page = blog_factory.BlogPageFactory(parent=cls.blog_index)

    def test_page_loads(self):
        response = self.client.get(self.blog_page.url)

        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_clean_when_hero_image_and_hero_video_set(self):
        self.blog_page.hero_image = wagtail_factories.ImageFactory()
        self.blog_page.hero_video = "https://example.com/video.mp4"

        with self.assertRaises(exceptions.ValidationError):
            self.blog_page.clean()

    def test_clean_when_hero_image_but_not_hero_video_set(self):
        self.blog_page.hero_image = wagtail_factories.ImageFactory()
        self.blog_page.hero_video = ""

        result = self.blog_page.clean()

        self.assertIsNone(result)

    def test_clean_when_not_hero_image_but_hero_video_set(self):
        self.blog_page.hero_image = None
        self.blog_page.hero_video = "https://example.com/video.mp4"

        result = self.blog_page.clean()

        self.assertIsNone(result)

    def test_get_missing_related_posts(self):
        self.assertEqual(self.blog_page.related_posts.count(), 0)
        self.assertEqual(self.blog_page.related_post_count, 3)
        tag = tag_models.Tag.objects.create(name="test")
        self.blog_page.tags.add(tag)
        self.blog_page.save()
        other_post = blog_factory.BlogPageFactory(parent=self.blog_index)
        other_post.tags.add(tag)
        other_post.save()

        result = self.blog_page.get_missing_related_posts()

        self.assertEqual(len(result), 1)
        self.assertListEqual(result, [other_post])
