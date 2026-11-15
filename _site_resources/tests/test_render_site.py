import pathlib
import sys

# render_site.py runs as a script from _site_resources/ and imports render_site_links as a top-level module.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from _site_resources import render_site  # noqa: E402
from _site_resources import render_site_links as rs  # noqa: E402
from _site_resources.tests.test_render_site_links import bdq_rs_links  # noqa: E402


# Link rewriting must leave fenced code blocks unchanged: in RDF examples, <https://rs.tdwg.org/...> is an
# IRI, not a Markdown autolink, and rewriting it into a Markdown link breaks the example.
def test_fenced_turtle_example_is_not_rewritten():
    text = (
        "See <https://rs.tdwg.org/bdqtest/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134>.\n"
        "\n"
        "```turtle\n"
        "<https://rs.tdwg.org/bdqtest/method/04cee4e0-0c83-40cc-8de2-e7391f0a97a9> a bdqffdq:ValidationMethod ;\n"
        "    dcterms:hasVersion <https://rs.tdwg.org/bdqtest/method/version/04cee4e0-0c83-40cc-8de2-e7391f0a97a9-2023-09-18> .\n"
        "```\n"
        "\n"
        "After <https://rs.tdwg.org/bdqval/terms/>.\n"
    )
    with bdq_rs_links("rewrite"):
        result = render_site.outside_fenced_code(text, rs.rewrite_markdown_links)
    code = text[text.index("```turtle"):text.index("```\n\nAfter") + 4]
    assert code in result
    assert "[https://rs.tdwg.org/bdqtest/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134](https://bdq-public-review.rs.tdwg.org/bdqtest/terms/69b2efdc-6269-45a4-aecb-4cb99c2ae134)" in result
    assert "[https://rs.tdwg.org/bdqval/terms/](https://bdq-public-review.rs.tdwg.org/bdqval/terms/)" in result


def test_tilde_fence_and_unclosed_fence_are_left_unchanged():
    text = "~~~xml\n<https://rs.tdwg.org/bdqffdq/terms/>\n~~~\n```\n<https://rs.tdwg.org/bdqval/terms/>\n"
    with bdq_rs_links("rewrite"):
        assert render_site.outside_fenced_code(text, rs.rewrite_markdown_links) == text


def test_text_without_fences_is_transformed_whole():
    assert render_site.outside_fenced_code("a\nb\n", str.upper) == "A\nB\n"
