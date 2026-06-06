from _site_resources import render_site_links as rs


def test_rewrite_target_relative_md():
    assert rs.rewrite_target("guide/users/index.md") == "guide/users/index.html"


def test_rewrite_target_relative_md_with_fragment():
    assert rs.rewrite_target("../../../index.md#glossary_Test") == "../../../index.html#glossary_Test"


def test_rewrite_target_readme():
    assert rs.rewrite_target("foo/README.md") == "foo/index.html"


def test_rewrite_target_owl_to_ttl():
    assert rs.rewrite_target("../../../vocabulary/bdqffdq.owl") == "../../../vocabulary/bdqffdq.ttl"


def test_rewrite_target_external_unchanged():
    assert rs.rewrite_target("https://example.org/x.md") == "https://example.org/x.md"


def test_rewrite_target_invalid_url_does_not_crash():
    bad = "http://[not-valid"
    assert rs.rewrite_target(bad) == bad


def test_parse_markdown_link_target_angle_with_title():
    dest, title = rs.parse_markdown_link_target('<../../../index.md#glossary_Test> "A title"')
    assert dest == "<../../../index.md#glossary_Test>"
    assert title == '"A title"'


def test_parse_markdown_link_target_bare_with_title_and_parens():
    dest, title = rs.parse_markdown_link_target('foo.md "A title with (parens)"')
    assert dest == "foo.md"
    assert title == '"A title with (parens)"'


def test_find_markdown_inline_spans_simple():
    spans = rs.find_markdown_inline_spans("[x](foo.md)")
    assert spans == [(0, len("[x](foo.md)"))]


def test_find_markdown_inline_spans_angle_with_title():
    s = '[Test](<../../../index.md#glossary_Test> "A title")'
    spans = rs.find_markdown_inline_spans(s)
    assert spans == [(0, len(s))]


def test_find_markdown_inline_spans_nested_label():
    s = "[outer [inner]](foo.md)"
    spans = rs.find_markdown_inline_spans(s)
    assert spans == [(0, len(s))]


def test_rewrite_markdown_links_simple():
    src = "[Test](../../../index.md#glossary_Test)"
    out = rs.rewrite_markdown_links(src)
    assert out == "[Test](../../../index.html#glossary_Test)"


def test_rewrite_markdown_links_angle_with_title():
    src = '[Test](<../../../index.md#glossary_Test> "A title")'
    out = rs.rewrite_markdown_links(src)
    assert out == '[Test](<../../../index.html#glossary_Test> "A title")'


def test_rewrite_markdown_links_title_containing_markdown_link():
    src = '[Darwin Core](<../../../index.md#glossary_Darwin_Core> "[Darwin Core](https://dwc.tdwg.org/).")'
    out = rs.rewrite_markdown_links(src)
    assert out == '[Darwin Core](<../../../index.html#glossary_Darwin_Core> "[Darwin Core](https://dwc.tdwg.org/).")'


def test_rewrite_markdown_links_image():
    src = '![Diagram](bdqffdq_data_quality_layers.svg)'
    out = rs.rewrite_markdown_links(src)
    assert out == src


def test_linkify_bare_url_in_markdown_line():
    src = "See https://example.org/file for details."
    out = rs.linkify_bare_urls_in_markdown_line(src)
    assert out == "See [https://example.org/file](https://example.org/file) for details."


def test_linkify_does_not_touch_existing_markdown_link():
    src = "* [Audio File](https://github.com/tdwg/bdq/raw/refs/heads/master/tg2/products/BDQ_Overview_2025-07-26_8m.mp3)."
    out = rs.linkify_bare_urls_in_markdown_line(src)
    assert out == src


def test_linkify_does_not_touch_inline_code():
    src = "Use `https://example.org/file` as an example."
    out = rs.linkify_bare_urls_in_markdown_line(src)
    assert out == src


def test_linkify_html_line_bare_url():
    src = "<li>See https://example.org/file</li>"
    out = rs.linkify_bare_urls_in_html_line(src)
    assert out == '<li>See <a href="https://example.org/file">https://example.org/file</a></li>'


def test_linkify_html_line_does_not_touch_markdown_link():
    src = '<td>[DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)</td>'
    out = rs.linkify_bare_urls_in_html_line(src)
    assert out == src


def test_linkify_html_line_does_not_touch_markdown_links_in_glossary_row_fragment():
    src = '<td>[DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/). Hosts dc:Namespace [dc:](https://purl.org/dc/elements/1.1/)</td>'
    out = rs.linkify_bare_urls_in_html_line(src)
    assert out == src


def test_bdq_rs_plain_mode_not_linkified_in_markdown():
    src = "https://rs.tdwg.org/bdqtest/terms/example"
    out = rs.linkify_bare_urls_in_markdown_line(src)
    assert out == src


def test_bdq_rs_plain_mode_markdown_link_collapses_to_label():
    src = '[Test](https://rs.tdwg.org/bdqtest/terms/example)'
    out = rs.rewrite_markdown_links(src)
    assert out == "Test"


def test_real_case_test_glossary_link():
    src = '[Test](<../../../index.md#glossary_Test> "A composition of a `bdqffdq:DataQualityNeed` with a `bdqffdq:DataQualityMethod` that links it to an instance of a `bdqffdq:Specification`.")'
    out = rs.rewrite_markdown_links(src)
    assert out.startswith('[Test](<../../../index.html#glossary_Test> "A composition of a `bdqffdq:DataQualityNeed`')


def test_real_case_darwin_core_glossary_link():
    src = '[Darwin Core](<../../../index.md#glossary_Darwin_Core> "[Darwin Core](https://dwc.tdwg.org/). A Standard intended to facilitate the sharing of information about biological diversity. Host of the dwc:namespace [dwc:](http://rs.tdwg.org/dwc/terms/)")'
    out = rs.rewrite_markdown_links(src)
    assert out.startswith('[Darwin Core](<../../../index.html#glossary_Darwin_Core> ')