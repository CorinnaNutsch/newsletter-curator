import json
from datetime import date
from pathlib import Path

import pytest

from newsletter_curator.adapters.email_parser import parse_email
from newsletter_curator.domain.parsed_email import NewsletterArticle, NewsletterIssue

DATA_DIR = Path(__file__).parent / "fixtures/dataelixir/"


@pytest.fixture
def raw_html() -> str:
    return (DATA_DIR / "issue_1.html").read_text(encoding="utf-8")


@pytest.fixture
def expected_issue() -> NewsletterIssue:
    items = json.loads((DATA_DIR / "issue_1_expected.json").read_text(encoding="utf-8"))
    articles = [
        NewsletterArticle(
            title=item["title"],
            url=item["url"],
            sponsored=item["sponsored"],
            text=item["text"],
        )
        for item in items
    ]
    # source and date are the same on every item, so the first one is enough
    return NewsletterIssue(
        source=items[0]["source"],
        date=date.fromisoformat(items[0]["date"]),
        articles=articles,
    )


def test_complete_item_list_retrieved(raw_html: str) -> None:
    parsed_issue = parse_email(raw_html)
    assert len(parsed_issue.articles) == 10


def test_full_comparison_match(raw_html: str, expected_issue: NewsletterIssue) -> None:
    parsed_issue = parse_email(raw_html)
    assert parsed_issue == expected_issue
