"""Tests for the templates.py module"""

from unittest import IsolatedAsyncioTestCase

from tgbot.utils.templates import RenderTemplate


class TestRenderTemplate(IsolatedAsyncioTestCase):
    """The unittest class for testing the RenderTemplate class"""

    def setUp(self) -> None:
        """A setup method that will be called before each test case"""
        self._render_template: RenderTemplate = RenderTemplate(path_to_templates="tests/templates")

    async def test_render_template(self) -> None:
        """A test method for testing the render method of the RenderTemplate class"""
        data: dict[str, str] = {"test_data": "some test data"}
        expected_output: str = f"This is {data.get('test_data')} for render template"
        output: str = await self._render_template.render(template_name="test_templates_render.jinja2", data=data)
        self.assertEqual(first=output, second=expected_output)

    async def test_render_template_not_found(self) -> None:
        """A test method for testing the render method of the RenderTemplate class when the template is not found"""
        expected_output: str = "❌ Answer template not found!"
        output: str = await self._render_template.render(template_name="nonexistent_template.jinja2")
        self.assertEqual(first=output, second=expected_output)
