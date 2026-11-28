from dataclasses import dataclass
from datetime import date


@dataclass
class NewsletterArticle:
    title: str
    url: str
    sponsored: bool
    text: str


@dataclass
class NewsletterIssue:
    source: str
    date: date
    articles: list[NewsletterArticle]
