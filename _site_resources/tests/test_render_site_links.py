from _site_resources import render_site_links as rs

# Tests for the link rewriting and linkifying functions used in the site rendering process. 
# These are not intended to be exhaustive tests of markdown parsing, but rather cover specific 
# cases encountered in the actual content of the site, including edge cases that caused problems
# during development.

def test_rewrite_target_relative_md():
    assert rs.rewrite_target("guide/users/index.md") == "guide/users/index.html"
    assert rs.rewrite_target("guide/foo/index.md") == "guide/foo/index.html"


def test_rewrite_target_relative_md_with_fragment():
    assert rs.rewrite_target("../../../index.md#glossary_Test") == "../../../index.html#glossary_Test"
    assert rs.rewrite_target("guide/foo/index.md#glossary_Test") == "guide/foo/index.html#glossary_Test"


def test_rewrite_target_readme():
    assert rs.rewrite_target("foo/README.md") == "foo/index.html"


def test_rewrite_target_owl_to_ttl():
    # Special case handling for owl ontology, rename as ttl so that site delivers with correct content type
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


def test_rewrite_markdown_links_title_with_multiple_markdown_links():
    src = '[DCMI](<../../../index.md#glossary_DCMI> "[DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/). Hosts dc:Namespace [dc:](https://purl.org/dc/elements/1.1/)")'
    out = rs.rewrite_markdown_links(src)
    assert out == '[DCMI](<../../../index.html#glossary_DCMI> "[DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/). Hosts dc:Namespace [dc:](https://purl.org/dc/elements/1.1/)")'


def test_rewrite_markdown_links_title_with_inline_code():
    src = '[Response](<../../list/bdqffdq/index.md#Response> "A bdqffdq:ReportConcept produced by a `bdqffdq:Implementation`.")'
    out = rs.rewrite_markdown_links(src)
    assert out == '[Response](<../../list/bdqffdq/index.html#Response> "A bdqffdq:ReportConcept produced by a `bdqffdq:Implementation`.")'


def test_rewrite_markdown_links_image():
    src = "![Diagram](bdqffdq_data_quality_layers.svg)"
    out = rs.rewrite_markdown_links(src)
    assert out == src


def test_rewrite_markdown_image_with_title():
    src = '![Diagram](figure.md "A figure title")'
    out = rs.rewrite_markdown_links(src)
    assert out == '![Diagram](figure.html "A figure title")'
	# do not rewrite if not .md extension (expected case)
    src = '![Diagram](figure.svg "A figure title")'
    out = rs.rewrite_markdown_links(src)
    assert out == '![Diagram](figure.svg "A figure title")'


def test_rewrite_markdown_links_readme():
    src = "[Home](README.md)"
    out = rs.rewrite_markdown_links(src)
    assert out == "[Home](index.html)"


def test_rewrite_markdown_links_two_level_glossary_reference():
    src = '[CORE](<../../index.md#glossary_CORE> "Tests that are useful...")'
    out = rs.rewrite_markdown_links(src)
    assert out == '[CORE](<../../index.html#glossary_CORE> "Tests that are useful...")'


def test_rewrite_html_links_relative_md_with_fragment():
    src = '<a href="./docs/guide/users/index.md#31-test-types-non-normative">Test Types</a>'
    out = rs.rewrite_html_links(src)
    assert out == '<a href="./docs/guide/users/index.html#31-test-types-non-normative">Test Types</a>'


def test_rewrite_html_links_owl_to_ttl():
    src = '<a href="./vocabulary/bdqffdq.owl">OWL Ontology</a>'
    out = rs.rewrite_html_links(src)
    assert out == '<a href="./vocabulary/bdqffdq.ttl">OWL Ontology</a>'
    # only rewrite .owl extension, not .xml
    src = '<a href="./vocabulary/bdqtest.xml">Tests as RDF/XML</a>'
    out = rs.rewrite_html_links(src)
    assert out == '<a href="./vocabulary/bdqtest.xml">Tests as RDF/XML</a>'
    # only rewrite .owl extension, not .ttl
    src = '<a href="./vocabulary/bdqtest.ttl">Tests as turtle</a>'
    out = rs.rewrite_html_links(src)
    assert out == '<a href="./vocabulary/bdqtest.ttl">Tests as turtle</a>'


def test_rewrite_html_links_external_unchanged():
    src = '<a href="https://www.tdwg.org/">TDWG</a>'
    out = rs.rewrite_html_links(src)
    assert out == src


def test_rewrite_html_links_bdq_rs_plain_mode_keeps_href():
    src = '<a href="https://rs.tdwg.org/bdqtest/">bdqtest</a>'
    out = rs.rewrite_html_links(src)
    assert out == src
    # even if link contains target attribute do not rewrite
    src = '<a href="https://rs.tdwg.org/bdqtest/" target="_blank">bdqtest</a>'
    out = rs.rewrite_html_links(src)
    assert out == src


def test_linkify_bare_url_in_markdown_line():
    src = "See https://example.org/file for details."
    out = rs.linkify_bare_urls_in_markdown_line(src)
    assert out == "See [https://example.org/file](https://example.org/file) for details."


def test_linkify_bare_doi_url():
    src = "https://doi.org/10.3897/biss.4.50889"
    out = rs.linkify_bare_urls_in_markdown_line(src)
    assert out == "[https://doi.org/10.3897/biss.4.50889](https://doi.org/10.3897/biss.4.50889)"


def test_linkify_bare_url_excludes_trailing_period():
    src = "See https://example.org/file."
    out = rs.linkify_bare_urls_in_markdown_line(src)
    assert out == "See [https://example.org/file](https://example.org/file)."


def test_linkify_does_not_touch_existing_markdown_link():
    src = "* [Audio File](https://github.com/tdwg/bdq/raw/refs/heads/master/tg2/products/BDQ_Overview_2025-07-26_8m.mp3)."
    out = rs.linkify_bare_urls_in_markdown_line(src)
    assert out == src


def test_linkify_does_not_touch_inline_code():
    src = "Use `https://example.org/file` as an example."
    out = rs.linkify_bare_urls_in_markdown_line(src)
    assert out == src


def test_linkify_markdown_line_does_not_touch_url_inside_existing_link_title():
    src = '[Darwin Core](<../../../index.html#glossary_Darwin_Core> "[Darwin Core](https://dwc.tdwg.org/).")'
    out = rs.linkify_bare_urls_in_markdown_line(src)
    assert out == src


def test_linkify_html_line_bare_url():
    src = "<li>See https://example.org/file</li>"
    out = rs.linkify_bare_urls_in_html_line(src)
    assert out == '<li>See <a href="https://example.org/file">https://example.org/file</a></li>'


def test_linkify_html_li_reference_line():
    src = "<li>ALA (2013) Data Processing. https://www.ala.org.au/blogs-news/data-processing/</li>"
    out = rs.linkify_bare_urls_in_html_line(src)
    assert out == '<li>ALA (2013) Data Processing. <a href="https://www.ala.org.au/blogs-news/data-processing/">https://www.ala.org.au/blogs-news/data-processing/</a></li>'


def test_linkify_html_line_does_not_touch_markdown_link():
    src = '<td>[DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)</td>'
    out = rs.linkify_bare_urls_in_html_line(src)
    assert out == src


def test_linkify_html_line_with_markdown_links_in_text_fragment():
    src = '<td>[DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/). (Dublin Core). Hosts dc:Namespace [dc:](https://purl.org/dc/elements/1.1/)</td>'
    out = rs.linkify_bare_urls_in_html_line(src)
    assert out == src


def test_linkify_html_line_mixed_markdown_links_and_bare_url():
    src = '<td>[DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/). More info at https://example.org/info</td>'
    out = rs.linkify_bare_urls_in_html_line(src)
    assert out == '<td>[DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/). More info at <a href="https://example.org/info">https://example.org/info</a></td>'


def test_bdq_rs_plain_mode_not_linkified_in_markdown():
    src = "https://rs.tdwg.org/bdqtest/terms/example"
    out = rs.linkify_bare_urls_in_markdown_line(src)
    assert out == src


def test_bdq_rs_plain_mode_markdown_link_collapses_to_label():
    src = "[Test](https://rs.tdwg.org/bdqtest/terms/example)"
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


def test_real_case_html_table_link_from_review_index():
    src = '<a href="./docs/guide/users/index.md#31-test-types-non-normative">Test Types</a>'
    out = rs.rewrite_html_links(src)
    assert out == '<a href="./docs/guide/users/index.html#31-test-types-non-normative">Test Types</a>'


def test_real_case_glossary_row_fragment_from_review_index():
    src = '<td>[DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/). (Dublin Core). Hosts dc:Namespace [dc:](https://purl.org/dc/elements/1.1/)</td>'
    out = rs.linkify_bare_urls_in_html_line(src)
    assert out == src


def test_real_case_audio_file_line_from_review_index():
    src = "* [Audio File](https://github.com/tdwg/bdq/raw/refs/heads/master/tg2/products/BDQ_Overview_2025-07-26_8m.mp3)."
    out = rs.linkify_bare_urls_in_markdown_line(src)
    assert out == src


def test_real_case_implementers_test_link():
    src = '[Test](<../../../index.md#glossary_Test> "A composition of a `bdqffdq:DataQualityNeed` with a `bdqffdq:DataQualityMethod` that links it to an instance of a `bdqffdq:Specification`, these instances being composed with a `bdqffdq:ResourceType` and linked to a `Use Case` through `Policies`.")'
    out = rs.rewrite_markdown_links(src)
    assert out.startswith('[Test](<../../../index.html#glossary_Test> "')


def test_real_case_response_link():
    src = '[bdqffdq:Response](<../../list/bdqffdq/index.md#Response> "A bdqffdq:ReportConcept produced by a bdqffdq:Implementation expressing a statement about data quality resulting from the application of a Test.")'
    out = rs.rewrite_markdown_links(src)
    assert out == '[bdqffdq:Response](<../../list/bdqffdq/index.html#Response> "A bdqffdq:ReportConcept produced by a bdqffdq:Implementation expressing a statement about data quality resulting from the application of a Test.")'


def test_mini_document_mixed_cases():
    src = (
        "# Example\n\n"
        '[Test](<../../../index.md#glossary_Test> "A composition of a `bdqffdq:DataQualityNeed`.")\n'
        "See https://example.org/info.\n\n"
        "<td>[DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/). More info at https://example.org/more</td>\n\n"
        "```sparql\n"
        "SELECT * WHERE { ?s ?p <https://example.org/object> }\n"
        "```\n"
    )
    rewritten = rs.rewrite_markdown_links(src)
    rewritten = rs.rewrite_html_links(rewritten)

    lines = rewritten.splitlines()
    processed = []
    in_fence = False
    for line in lines:
        if line.startswith("```"):
            in_fence = not in_fence
            processed.append(line)
            continue
        if in_fence:
            processed.append(line)
            continue
        if "<" in line and ">" in line:
            processed.append(rs.linkify_bare_urls_in_html_line(line))
        else:
            processed.append(rs.linkify_bare_urls_in_markdown_line(line))

    out = "\n".join(processed)

    assert '[Test](<../../../index.html#glossary_Test> "A composition of a `bdqffdq:DataQualityNeed`.")' in out
    assert "See [https://example.org/info](https://example.org/info)." in out
    assert '<td>[DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/). More info at <a href="https://example.org/more">https://example.org/more</a></td>' in out
    assert "SELECT * WHERE { ?s ?p <https://example.org/object> }" in out

def test_find_markdown_inline_spans_bold_label_with_parentheses():
    s = "[**Fitness For Use Framework Ontology List of Terms (bdqffdq:)**](docs/list/bdqffdq/index.md)"
    spans = rs.find_markdown_inline_spans(s)
    assert spans == [(0, len(s))]

def test_rewrite_markdown_links_bold_label_with_parentheses():
    src = "- [**Fitness For Use Framework Ontology List of Terms (bdqffdq:)**](docs/list/bdqffdq/index.md) - The definitions of terms in the bdqffdq: vocabulary."
    out = rs.rewrite_markdown_links(src)
    assert out == "- [**Fitness For Use Framework Ontology List of Terms (bdqffdq:)**](docs/list/bdqffdq/index.html) - The definitions of terms in the bdqffdq: vocabulary."

def test_linkify_markdown_line_does_not_damage_bold_label_link_with_parentheses():
    src = "- [**Fitness For Use Framework Ontology List of Terms (bdqffdq:)**](docs/list/bdqffdq/index.html) - The definitions of terms in the bdqffdq: vocabulary."
    out = rs.linkify_bare_urls_in_markdown_line(src)
    assert out == src

def test_rewrite_markdown_links_bold_label_with_parentheses_and_fragment():
    src = "- [**Data Quality Dimension Controlled Vocabulary List of Terms (bdqdim:)**](docs/list/bdqdim/index.md#bdqdim_Conformance)"
    out = rs.rewrite_markdown_links(src)
    assert out == "- [**Data Quality Dimension Controlled Vocabulary List of Terms (bdqdim:)**](docs/list/bdqdim/index.html#bdqdim_Conformance)"

def test_rewrite_markdown_links_complex_label_formatting():
    src = "[**BDQ Controlled Vocabulary List of Terms (bdqval:)**](docs/list/bdqval/index.md)"
    out = rs.rewrite_markdown_links(src)
    assert out == "[**BDQ Controlled Vocabulary List of Terms (bdqval:)**](docs/list/bdqval/index.html)"

def test_mini_list_document_with_bold_link_labels():
    src = (
        "- [**Fitness For Use Framework Ontology List of Terms (bdqffdq:)**](docs/list/bdqffdq/index.md) - Terms.\n"
        "- [**Data Quality Dimension Controlled Vocabulary List of Terms (bdqdim:)**](docs/list/bdqdim/index.md) - Terms.\n"
    )
    rewritten = rs.rewrite_markdown_links(src)
    out = rs.linkify_bare_urls_in_markdown_line(rewritten)
    assert "[**Fitness For Use Framework Ontology List of Terms (bdqffdq:)**](docs/list/bdqffdq/index.html)" in out
    assert "[**Data Quality Dimension Controlled Vocabulary List of Terms (bdqdim:)**](docs/list/bdqdim/index.html)" in out

def test_rewrite_markdown_links_plain_bold_label_with_parentheses():
    src = "[**Fitness For Use Framework Ontology List of Terms (bdqffdq:)**](docs/list/bdqffdq/index.md)"
    out = rs.rewrite_markdown_links(src)
    assert out == "[**Fitness For Use Framework Ontology List of Terms (bdqffdq:)**](docs/list/bdqffdq/index.html)"


def test_rewrite_markdown_links_plain_bold_label_with_parentheses_fragment():
    src = "[**Data Quality Dimension Controlled Vocabulary List of Terms (bdqdim:)**](docs/list/bdqdim/index.md#bdqdim_Conformance)"
    out = rs.rewrite_markdown_links(src)
    assert out == "[**Data Quality Dimension Controlled Vocabulary List of Terms (bdqdim:)**](docs/list/bdqdim/index.html#bdqdim_Conformance)"



