from pathlib import Path

from django.test import SimpleTestCase


class SidebarTextWrappingTests(SimpleTestCase):
    def test_sidebar_nav_item_labels_do_not_wrap_when_collapsed(self) -> None:
        css_path = Path(__file__).resolve().parents[1] / "static" / "core" / "css" / "base.css"
        css = css_path.read_text(encoding="utf-8")

        self.assertIn(".nav-sidebar .nav-link p", css)
        self.assertIn("text-wrap-mode: nowrap;", css)
