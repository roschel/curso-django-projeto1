from django.db.models import QuerySet
from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse("recipes:home"))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(path=reverse("recipes:home"))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(path=reverse("recipes:home"))
        self.assertTemplateUsed(response, "recipes/pages/home.html")

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipe(self):
        response = self.client.get(path=reverse("recipes:home"))
        self.assertIn("No recipes found", response.content.decode(response.charset))

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(path=reverse("recipes:home"))
        response_recipes = response.context.get("recipes")

        if not response_recipes:
            self.assertTrue(response_recipes, QuerySet)

        response_content = response.content.decode(response.charset)

        self.assertEqual(response_recipes.first().title, "Recipe Title")
        self.assertIn("Recipe Title", response_content)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse("recipes:category", kwargs={"category_id": 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_404_if_no_recipes_found(self):
        response = self.client.get(
            path=reverse("recipes:category", kwargs={"category_id": 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        new_title = "This is a category test"
        self.make_recipe(title=new_title)
        response = self.client.get(path=reverse("recipes:category", args=(1,)))

        response_content = response.content.decode(response.charset)
        self.assertIn(new_title, response_content)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse("recipes:recipe", kwargs={"id": 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_404_if_no_recipes_found(self):
        response = self.client.get(path=reverse("recipes:recipe", kwargs={"id": 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        new_title = "This is a detail"
        self.make_recipe(title=new_title)
        response = self.client.get(path=reverse("recipes:recipe", kwargs={"id": 1}))

        response_content = response.content.decode(response.charset)
        self.assertIn(new_title, response_content)
